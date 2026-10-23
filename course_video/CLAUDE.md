# CLAUDE.md — Lean Course Video project

This folder (`course_video/`) is a **Remotion** project that produces animated
lesson videos for a paid Lean Manufacturing course. Read `docs/PLAYBOOK.md` for
the full guide before making a new lesson.

## What this is
Code-driven animated explainer videos: dark navy + teal style, narration voice,
word-synced captions, music + SFX, and recurring flat-vector characters (a
female guide host + PPE factory workers). 1920×1080, 30 fps.

## Golden rules (do not break)
1. **One design system.** All colors/fonts come from `src/theme.ts`. Never
   hard-code a new palette; reuse theme tokens so all lessons match.
2. **Characters are custom SVG** in `src/components/characters.tsx`. Do **NOT**
   install `react-peeps` — it is broken on React 19. Keep characters tasteful
   and professional (this is a paid course); never sexualized.
3. **Narration = edge-tts** with `boundary="WordBoundary"` (the default is
   SentenceBoundary and gives no word timings). Captions depend on the
   per-scene `*.words.json`.
4. **Every lesson ships two composition variants:** the normal one (captions)
   and a `...Dub` one (`captions={false}`) for clean dubbing.
5. **Keep the voice as a stem.** Always be able to export voice-only and
   music+SFX-only tracks so dubbing never loses the music (see
   `DUB_WORKFLOW.md`). When dubbing, dub the voice stem, not the mixed video.
6. **Don't commit** `node_modules/` or `out/` (already in `.gitignore`).

## Common commands
```bash
npm install                                  # once
npx remotion studio                          # live preview
npx remotion render <CompId> out/x.mp4       # render a lesson
npx remotion still <CompId> out/x.png --frame=70   # check one frame
python narration/make_narration.py           # (re)generate voice + word timings
python narration/make_music.py               # regenerate music bed
python narration/make_sfx.py                 # regenerate sound effects
```

## Compositions (see `src/Root.tsx`)
- `EightWastes` — short lesson, with captions
- `EightWastesDub` — same, no burned captions (for dubbing)
- `FullEightWastes` — full ~9-min lesson
- `CharacterSample` — character demo

## Brand
Edit course name / author in `src/theme.ts` → `theme.brand`.
