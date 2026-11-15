---
name: openmontage
description: Produce a full video with the OpenMontage pipelines (animated explainer, cinematic, clip factory, talking head, podcast repurpose, screen demo, documentary montage, localization dub and more) — from idea to finished render with script, voice, music, Remotion composition and FFmpeg. Use when the user wants a complete video produced end to end, wants to cut a long video into short clips (TikTok / Reels / Shorts), or names OpenMontage.
---

# OpenMontage

The full project lives in the git submodule `vendor/OpenMontage` (AGPL-3.0, from github.com/OpenMontageInc/OpenMontage).

1. If `vendor/OpenMontage` is empty, run `git submodule update --init vendor/OpenMontage`.
2. Setup once (needs Python 3.10+, FFmpeg, Node 22+): `cd vendor/OpenMontage && make setup`.
3. **Read `vendor/OpenMontage/AGENT_GUIDE.md` before acting** — it holds the routing rules that decide the first step.
   Its own skills (ffmpeg, remotion, text-to-speech, music, video-edit, framer-motion, lottie, manim, …) are in
   `vendor/OpenMontage/.claude/skills/`; read the one the guide points to.
4. Pipelines are defined in `vendor/OpenMontage/pipeline_defs/*.yaml`.
5. Always apply the user's house style from the `gaya-editing-saya` skill (9:16 vertical, their three widget types).
