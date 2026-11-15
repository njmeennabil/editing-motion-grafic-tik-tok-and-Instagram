"""Build an SFX pass for the kinetic-type-slam video from sfx-kit, synced to word landings."""
import json, subprocess, sys
kit, timing_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
DURATION = sys.argv[4] if len(sys.argv) > 4 else '12'  # seconds
FPS = 30
sounds = {s['id']: s for s in json.load(open(f'{kit}/sounds.json'))['sounds']}
t = json.load(open(timing_path))
words = t['words']  # [frame_start, text, is_accent]
cues = []  # (sound_id, moment_seconds, gain_db)
LAND = 5  # frames from word start to landing (mask rise + snappy spring)
prev_start = None
for i, (f, txt, acc) in enumerate(words):
    land = (f + LAND) / FPS
    if i == 0:
        cues.append(('impact-deep-hard', land, -2))          # hook hit
    elif txt == '3':
        cues.append(('riser-1s-soft', land, -6))             # build into the key number
        cues.append(('boom-hit-medium', land, -1))
    elif acc:
        cues.append(('swish-medium', (f + 2) / FPS, -6))
        cues.append(('impact-heavy-hard', land, -3))
    else:
        cues.append(('impact-light-firm', land, -8))
# whoosh on each line push-off (a new line starts after a gap > 1 beat)
for i in range(1, len(words)):
    if words[i][0] - words[i - 1][0] > 15:
        cues.append(('whoosh-fast-medium', (words[i][0] - 2) / FPS, -7))
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi', '-t', DURATION, '-i', 'anullsrc=r=48000:cl=stereo']
filters, labels = [], []
for k, (sid, moment, gain) in enumerate(cues):
    s = sounds[sid]
    start = max(0.0, moment - s['sync']['at'])
    cmd += ['-i', f"{kit}/{s['file']}"]
    filters.append(f"[{k+1}:a]aresample=48000,aformat=channel_layouts=stereo,volume={gain}dB,adelay={int(start*1000)}:all=1[a{k}]")
    labels.append(f'[a{k}]')
filters.append(f"[0:a]{''.join(labels)}amix=inputs={len(labels)+1}:normalize=0:duration=first,loudnorm=I=-16:TP=-2:LRA=11,aresample=48000[out]")
cmd += ['-filter_complex', ';'.join(filters), '-map', '[out]', '-c:a', 'pcm_s16le', out]
subprocess.run(cmd, check=True)
for c in sorted(cues, key=lambda c: c[1]): print(f'{c[1]:6.2f}s  {c[0]}  {c[2]}dB')
