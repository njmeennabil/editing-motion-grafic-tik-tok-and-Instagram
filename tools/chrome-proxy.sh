#!/bin/bash
# Run headless Chromium through the session's HTTPS proxy (Remotion forces direct connections).
args=()
for a in "$@"; do
  case "$a" in
    --no-proxy-server|--proxy-server=*|--proxy-bypass-list=*) ;;
    *) args+=("$a") ;;
  esac
done
exec /opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell "${args[@]}" "--proxy-server=${HTTPS_PROXY:-http://127.0.0.1:46643}" "--proxy-bypass-list=localhost;127.0.0.1;[::1]"
