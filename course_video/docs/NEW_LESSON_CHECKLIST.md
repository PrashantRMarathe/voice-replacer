# ✅ New Lesson Checklist

Quick checklist for making one new lesson. Full detail in `PLAYBOOK.md`.

- [ ] Write narration script per scene (conversational, short sentences)
- [ ] Generate voice + word timings (edge-tts, `boundary="WordBoundary"`)
      → `public/audio/<scene>.mp3` + `<scene>.words.json`
- [ ] Copy `*.words.json` into `src/captions/`
- [ ] Measure each clip's seconds → set scene `durationInFrames` = ceil(s*30)+pad
- [ ] Copy `EightWastes.tsx` → new `src/lessons/<Name>.tsx`; build scenes
- [ ] Add per-scene `<Audio>` narration + sentence captions
- [ ] Pure voice-only: NO music and NO sound effects (no whoosh, no ding)
- [ ] Insert 2 quizzes (QuizScene) — one mid-lesson, one before the outro
- [ ] Add `<BrandMark />` at the top level (FFIQ brand, top-left corner)
- [ ] Send the user a `<lesson>.json` script file to upload (content stays off GitHub)
- [ ] Final voice via clone-only pipeline (colab_clone_voice.ipynb) — user uploads
      their voice + lesson .json file(s); not the dub tool
- [ ] Rebuild timings.json + caption timings from the cloned clip durations
- [ ] Add `captions` prop (default true) for a Dub variant
- [ ] Register `<Name>` and `<Name>Dub` in `src/Root.tsx`
- [ ] Preview: `npx remotion studio` or `remotion still ... --frame=N`
- [ ] Render: `npx remotion render <Name> out/<name>.mp4`

---

## Starter prompt for a new chat
Paste this into a fresh session to continue the course:

> I'm continuing the Lean Manufacturing animated course in the `course_video/`
> Remotion project. Read `course_video/CLAUDE.md` and
> `course_video/docs/PLAYBOOK.md` first, then follow them exactly.
> Make a new lesson: **<LESSON NAME>** (content below). Keep the exact same style,
> characters, FFIQ brand, sentence captions (no word-highlight), **pure voice-only
> (no music, no SFX)**, and **2 quizzes** (one mid, one before the end), like the
> Zero Defects lesson. Build both the normal and the `...Dub` (no-caption)
> composition, render a preview still for me to check, then the full MP4. Then
> give me a `<lesson>.json` script file to upload to the clone notebook (keep my
> content off GitHub). Don't install react-peeps. Keep characters tasteful.
