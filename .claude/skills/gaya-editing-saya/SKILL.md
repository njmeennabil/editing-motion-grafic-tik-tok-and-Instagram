---
name: gaya-editing-saya
description: The owner's personal motion-graphics editing style for TikTok and Instagram (Reels) — the three widget types they use (Floating UI Widget, Kinetic Typography, Animated Infographic). Use for EVERY video, animation, motion graphic, overlay or edit made in this repo, before choosing motions, styles or sounds, and whenever the user says "gaya saya", "style saya", "macam biasa" or asks for a widget.
---

# Gaya Editing Saya (My Editing Style)

Platform: **TikTok & Instagram Reels** — vertical **9:16 (1080×1920)**, 30 fps unless told otherwise.
Keep text and widgets inside the safe area (avoid top ~250 px and bottom ~400 px where the app UI sits, and the right ~150 px with the like/comment buttons).

## Jenis widget (widget types)

Every edit is built from one or more of these three. Ask which one(s) if the user doesn't say.

### 1. Floating UI Widget
UI-style cards, panels, chat bubbles, notifications, buttons, stat cards or app mockups that float over the footage.
- Soft glass / rounded cards, gentle shadow, slight parallax drift or float (never fully static).
- Enter with a spring pop or slide-up + fade; exit quickly.
- Good sources: `opus-motion` (UI mockups, data/HUD, `testimonial-chat`, `app-store-preview`), `ui-ux-pro-max` / `ui-styling` / `design-system` for the card design, `motion-broll`.
- Sound: soft pops / UI clicks (`sfx-kit`).

### 2. Kinetic Typography
Animated words that carry the message — synced to the voice or beat.
- Big, bold, high-contrast words; one idea per beat; highlight the key word (colour, scale or stamp).
- Motion: word-by-word reveal, scale punch, slam, slide, mask wipe; timed to speech/beat.
- Good sources: `opus-motion` (titles, `stamp-slam`, `social-short-captions`), `explainer-high-energy` / `explainer-engaging`, `lemo-opuscar` styles.
- Sound: whooshes and hits on key words (`sfx-kit`, `sound-effects`).

### 3. Animated Infographic
Data and facts shown visually — numbers, charts, steps, timelines, comparisons.
- Count-up numbers, bars/lines that grow, icons that build step by step; one number per moment.
- Clear labels, readable on a phone in under 2 seconds.
- Good sources: `opus-motion` (`stats-reveal`, data/HUD, `history-timeline`, `onboarding-steps`), `explainer-default`, `openmontage` (animated-explainer pipeline).
- Sound: `tone-step-*` and data ticks as items build (`sfx-kit`).

## Rules
- Hook in the first 1–2 seconds; keep pace fast (cut or change something every ~1–2 s).
- Check a contact sheet / still of the render before handing over.
- If the user adds new style details (fonts, colours, brand, pacing), **add them to this file**.
