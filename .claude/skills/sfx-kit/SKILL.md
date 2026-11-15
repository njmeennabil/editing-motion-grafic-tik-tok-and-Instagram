---
name: sfx-kit
description: Pick, place and level sound effects from SFX Kit (320 CC0 WAV sounds in 28 categories — pops, whooshes, UI clicks, risers, impacts, data ticks, celebration) for motion graphics, kinetic typography, UI widget animations and short-form video. Use when a video or animation needs sound effects synced to on-screen moments.
---

# SFX Kit

The sounds live in the git submodule `vendor/sfx-kit` (CC0 1.0, from github.com/wyzowl/sfx-kit).
If it is empty, run `git submodule update --init vendor/sfx-kit`.

1. Read `vendor/sfx-kit/GUIDE.md` (on-screen moment → sound table, placing and fitting) and
   `vendor/sfx-kit/catalogue.md` (one line per sound). In code, load `vendor/sfx-kit/sounds.json`.
2. **Find** by what happens on screen: each sound's `use_for`, `avoid_for`, `tags`, `fits_seconds`.
3. **Place**: start the sound at *(moment − `sync.at`)* so its sync point lands on the moment.
4. **Level**: sounds are loudness-matched; under voice-over lower each by its `under_voiceover_db`.
5. Files: `vendor/sfx-kit/sounds/<category>/<id>.wav` (48 kHz, 24-bit).

House-style pairings (see `gaya-editing-saya`): Floating UI Widget → soft pops / UI clicks on entrance;
Kinetic Typography → whooshes and hits on key words; Animated Infographic → `tone-step-*` / data ticks as numbers and bars build.
