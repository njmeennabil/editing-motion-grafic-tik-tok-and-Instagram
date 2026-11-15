"""Word start frames for opus-motion `kinetic-type-slam` (mirrors its schedule: cursor 6, line end + 2)."""
import json, sys
p = json.load(open(sys.argv[1])); b = max(4, p['beatFrames']); cur = 6; words = []
for ln in p['lines']:
    raw = ln['text'].split(); start = ln.get('at', cur)
    for i, w in enumerate(raw):
        words.append([start + i * b, w, w.lower() == str(ln.get('accent', '')).lower()])
    cur = start + len(raw) * b + p['holdBeats'] * b + 2
json.dump({'end': cur, 'words': words}, open(sys.argv[2], 'w'))
print(f'{len(words)} words, last line ends at frame {cur:.0f}')
