# ✅ New Lesson Checklist

Quick checklist for making one new lesson. Full detail in `PLAYBOOK.md`.

- [ ] Write narration script per scene (conversational, short sentences)
- [ ] Generate voice + word timings (edge-tts, `boundary="WordBoundary"`)
      → `public/audio/<scene>.mp3` + `<scene>.words.json`
- [ ] Copy `*.words.json` into `src/captions/`
- [ ] Measure each clip's seconds → set scene `durationInFrames` = ceil(s*30)+pad
- [ ] Copy `EightWastes.tsx` → new `src/lessons/<Name>.tsx`; build scenes
- [ ] Add per-scene `<Audio>` narration + `whoosh` SFX + `{Cap(words)}`
- [ ] Add top-level music `<Audio ... volume={0.16} loop />`
- [ ] Add `captions` prop (default true) for a Dub variant
- [ ] Register `<Name>` and `<Name>Dub` in `src/Root.tsx`
- [ ] Preview: `npx remotion studio` or `remotion still ... --frame=N`
- [ ] Render: `npx remotion render <Name> out/<name>.mp4`
- [ ] (If dubbing) export voice + music stems (see `DUB_WORKFLOW.md`)

---

## Starter prompt for a new chat
Paste this into a fresh session to continue the course:

> I'm continuing the Lean Manufacturing animated course in the `course_video/`
> Remotion project. Read `course_video/CLAUDE.md` and
> `course_video/docs/PLAYBOOK.md` first, then follow them exactly.
> Make a new lesson: **<LESSON NAME>**. Keep the same style, characters, voice,
> captions, music and sound design as the 8 Wastes lesson. Build both the normal
> and the `...Dub` (no-caption) composition, render a preview still for me to
> check, then render the full MP4. Don't install react-peeps. Keep characters
> tasteful and professional.
