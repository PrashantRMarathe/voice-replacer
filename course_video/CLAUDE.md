# CLAUDE.md — Lean Course Video project

This folder (`course_video/`) is a **Remotion** project that produces animated
lesson videos for a paid Lean Manufacturing course. Read `docs/PLAYBOOK.md` for
the full guide before making a new lesson. Also: `docs/VOICE.md` (voice
standard and checks) and `docs/AUTOMATION.md` (the Google Drive pipeline).

## What this is
Code-driven animated explainer videos: dark navy + teal style, the user's
cloned narration voice (voice only), sentence captions synced to the voice's
real pauses, 2 narrated quizzes per lesson, and recurring flat-vector
characters (a female guide host + PPE factory workers). 1920×1080, 30 fps.

## Golden rules (do not break)
1. **One design system.** All colors/fonts come from `src/theme.ts`. Never
   hard-code a new palette; reuse theme tokens so all lessons match.
2. **Characters are custom SVG** in `src/components/characters.tsx`. Do **NOT**
   install `react-peeps` — it is broken on React 19. Keep characters tasteful
   and professional (this is a paid course); never sexualized.
3. **Voice is the CLONED voice via the clone-only pipeline** (not the full dub
   tool, which guesses timing and causes repeats/music loss). See
   `docs/PLAYBOOK.md` §6. Scripts are drafted and voiced for timing scouting
   with edge-tts, then re-voiced in the cloned voice per scene and imported with
   `narration/import_clones.py`, which rebuilds durations to the cloned clips.
   **Engine F5 1.1.22, voice clip `voice_reference_A.wav`, never XTTS**
   (`docs/VOICE.md`). Standard route: queue `out/<NAME>.json` in
   `G:/My Drive/FFIQ_voice/input/`, the user clicks Run all in
   `colab_clone_drive.ipynb`, `narration/watch_drive.py` does the rest
   (`docs/AUTOMATION.md`). Check every batch is F5 before importing.
4. **Audio: voice first, light polish on top (approved Oct 2026, Poka Yoke demo).**
   The normal composition gets the polish layer (`src/lessons/shared/polish.tsx`):
   a quiet music bed (volume 0.07) and soft card / quiz sounds
   (`narration/make_demo_sfx.py`), then the render is normalised to −14 LUFS.
   The **`...Dub` composition stays pure voice-only** (no music, no SFX): its
   audio is the clean narration stem used for dubbing (`DUB_WORKFLOW.md`).
5. **Captions: one line at a time, NO per-word highlight.** `Captions.tsx` shows
   the active sentence (long ones split at a comma, via `plan.ts`). Every
   lesson ships two variants: the normal one (captions) and a `...Dub` one
   (`captions={false}`). Caption timing is snapped to the voice's real pauses
   (PLAYBOOK §6, "Caption sync"); never spread words evenly for cloned clips.
6. **Every lesson has 2 quick-check quizzes** — one mid-lesson, one before the
   end, placed with `after: "<page key>"`. Narrated (`quizN_q` read during the
   think countdown, `quizN_a` on reveal); silent only until those clips are cloned.
7. **Every lesson shows the brand mark.** Add `<BrandMark />` at the top level of
   each composition's `<AbsoluteFill>`. Brand text in `src/theme.ts` →
   `theme.brand` (`shortName` "FFIQ", `fullName` "FACTORY FLOW IQ"); top-left.
8. **Scripts follow the style guide** (`docs/PLAYBOOK.md` §4b): hook, one story
   thread, short sentences, talk to the learner. `npm run check` lints them;
   `narration/zero_defects.py` is the reference.
9. **Calm background.** Keep `Background` subtle (few, faint particles; dim grid).
10. **Don't commit** `node_modules/` or `out/` (already in `.gitignore`).

## Common commands
```bash
npm install                                        # once
npm run check                                      # types + audio/captions/quizzes/Root checks
npx remotion studio                                # live preview
npx remotion still <CompId> out/x.png --frame=70   # check one frame
npx remotion render <CompId> out/x.mp4 --concurrency=2   # render a lesson (keep PC awake)
npm run srt                                        # .srt subtitles for page lessons -> out/
python narration/<lesson>.py                       # bootstrap MISSING clips (edge-tts) + data
python narration/import_clones.py <lesson>         # import the cloned voice, rebuild timing
python narration/import_clones.py <lesson> --realign   # redo caption sync from current clips
python narration/watch_drive.py                    # Drive watcher: auto check/import/render (PLAYBOOK §6a)
```

## How lessons are built
Page lessons (Zero Defects, Yamazumi, and every new one) are **data + titles**:
`narration/<lesson>.py` holds the scripts/pages/quizzes, `narration/lesson_lib.py`
runs the pipeline, `src/lessons/plan.ts` computes the timeline, and
`src/lessons/shared/PageLesson.tsx` renders it. Don't copy timeline code into a
lesson; use `renderBlock` for a custom scene.

## Compositions (see `src/Root.tsx`)
- `ZeroDefects` / `ZeroDefectsDub`: page lesson (id `zd`)
- `Yamazumi` / `YamazumiDub`: page lesson (id `yz`)
- `UniformProduction` / `UniformProductionDub`: page lesson (id `up`)
- `ValueStreamMapping` / `ValueStreamMappingDub`: page lesson (id `vs`)
- `WhyWhy` / `WhyWhyDub`: page lesson (id `ww`)
- `XMatrix` / `XMatrixDub`: page lesson (id `xm`)
- `MudaMuraMuri` (id `mm`), `NextInspection` (`ni`), `OnePointLesson` (`op`),
  `PokaYoke` (`pk`), `QRQC` (`qr`), `RootCauseAnalysis` (`rc`), `SkillMatrix` (`sk`),
  `TaktTime` (`tt`): page lessons M to T, each with a `...Dub`
- The course is an **A-to-Z series** (M Muda/Mura/Muri, N Next Inspection, O One
  Point Lesson, P Poka Yoke, Q QRQC, R Root Cause Analysis, S Skill Training Matrix,
  T TAKT Time, U Uniform Production, V VSM, W Why-Why, X X-Matrix, Y Yamazumi,
  Z Zero Defects): name each lesson by its letter's term.
- `EightWastes` / `EightWastesDub`: short hand-built lesson
- `FullEightWastes`: full ~9-min 8 Wastes lesson
- `CharacterSample`: character demo

## Brand
Edit course name / author in `src/theme.ts` → `theme.brand`.
