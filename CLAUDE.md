# Editing Motion Graphic — TikTok & Instagram

This repo makes motion graphics and edits for TikTok and Instagram Reels.

**Always follow the owner's house style in `.claude/skills/gaya-editing-saya/SKILL.md`**:
vertical 9:16, built from the three widget types — Floating UI Widget, Kinetic Typography, Animated Infographic.

## Installed skills (`.claude/skills/`)
| Skill(s) | From | Licence |
|---|---|---|
| ui-ux-pro-max, design, design-system, ui-styling, brand, banner-design, slides | nextlevelbuilder/ui-ux-pro-max-skill | MIT |
| lemo-opuscar | lemomo-ai/lemo-opuscar | MIT code / CC BY-NC 4.0 docs (see note) |
| opus-motion | GovinduSasanka/opus-motion-library | MIT |
| openmontage (wrapper) | OpenMontageInc/OpenMontage | AGPL-3.0 |
| motion-broll, explainer-default, explainer-engaging, explainer-high-energy, object-separation, sound-effects | Barty-Bart/motion-graphics | MIT |
| sfx-kit (wrapper) | wyzowl/sfx-kit | CC0 1.0 |
| gaya-editing-saya | own | — |

Full libraries are git submodules in `vendor/` (opus-motion-library, OpenMontage, sfx-kit). After cloning run:

```bash
git submodule update --init --recursive
```

Note on lemo-opuscar: its Markdown docs are CC BY-NC 4.0 — "Lemo-Opuscar by Lemomo (LemoLab)",
https://github.com/lemomo-ai/lemo-opuscar. Films you make with it are yours (commercial included);
selling or redistributing the docs themselves commercially needs their commercial licence.
