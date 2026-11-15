#!/bin/bash
# Rebuild kinetic-typography-01.mp4 (9:16, 12 s, 30 fps) from props.json + timing.json.
# Needs: Node 22+, ffmpeg, python3, and `npm install` once in vendor/opus-motion-library.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
LIB="$ROOT/vendor/opus-motion-library"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"; git -C "$LIB" checkout -q cli/mgl.mjs' EXIT

# Behind an HTTPS proxy (cloud sessions) Remotion's own Chrome can't load fonts: use a proxy-aware headless Chromium.
if [ -n "${HTTPS_PROXY:-}" ] && [ -d /opt/pw-browsers ]; then
  git -C "$LIB" apply "$ROOT/tools/opus-mgl-browser.patch"
  export REMOTION_BROWSER_EXECUTABLE="$ROOT/tools/chrome-proxy.sh"
fi

# 1. Picture: kinetic-type-slam with our lines
(cd "$LIB" && node cli/mgl.mjs render kinetic-type-slam --props "$(cat "$HERE/props.json")" \
  --format portrait --frames 360 --concurrency "$(nproc)" --out "$TMP/raw.mp4")

# 2. Sound: word timings from props.json, then
#     sfx-kit hits/whooshes synced to each word landing, mastered to -16 LUFS
python3 -I "$ROOT/tools/slam_timing.py" "$HERE/props.json" "$HERE/timing.json"
python3 -I "$ROOT/tools/sfx_mix.py" "$ROOT/vendor/sfx-kit" "$HERE/timing.json" "$TMP/sfx.wav"

# 3. Final: shrink to 80 % and shift left so text stays out of the TikTok/Reels button column, add audio
ffmpeg -v error -y -i "$TMP/raw.mp4" -i "$TMP/sfx.wav" \
  -filter_complex "[0:v]scale=864:1536:flags=lanczos,pad=1080:1920:60:192:color=0x070608,format=yuv420p[v]" \
  -map "[v]" -map 1:a -c:v libx264 -preset slow -crf 18 -profile:v high -r 30 \
  -c:a aac -b:a 192k -movflags +faststart -shortest "$HERE/kinetic-typography-01.mp4"
echo "-> $HERE/kinetic-typography-01.mp4"
