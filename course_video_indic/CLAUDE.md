# CLAUDE.md — Indian-language course videos (separate project)

Hindi, Marathi, Telugu and Tamil (later Kannada) versions of the Factory Flow IQ
lessons. **Kept fully separate from `../course_video/` (the English course) at the
user's request: never edit the English project, its Drive folder `FFIQ_voice/`
(except reading `voice_reference_A.wav`), its watcher or its notebooks from here.**
Another chat keeps changing the English project; this project only READS it.

## Staying in step with the English design
`python tools/sync_from_english.py` copies the English shared code and assets
(components, scenes, shared PageLesson/polish, plan.ts, theme, fonts, check/srt,
lesson_lib, lint, import_clones, public/fonts, sfx, music) and re-applies the
Indian-language changes with exact-match checks (it stops and names any spot the
English code changed). The changes:
- built-in screen words -> `src/ui.ts` (Hindi labels; this project's own file),
- Noto fonts after Poppins/Inter in theme.ts (`src/indicFonts.ts` loads them per lesson),
- danda `।` sentence ends (captions, caption sync, lint), Unicode cue matching in polish.tsx,
- letterSpacing 0 (spacing splits Devanagari letters apart),
- lint Indic mode (`LANG = "hi"` skips English-only rules; flags English left in the voice text),
- per-lesson edge-tts `VOICE`.
Run it before starting new work here, then `npm run check`.

## Lessons
Hindi set (31 Oct 2026): one per finished English lesson, translated from the current
English text, same pages/visuals/polish. Module `narration/<english_name>_hi.py`,
id `<english id>_hi`, composition `<EnglishComp>Hi` / `...HiDub`:
A3ProblemSolving (`a3_hi`), DesignThinking (`dt_hi`), Gemba (`gb_hi`), Hancho (`hc_hi`),
OnePointLesson (`op_hi`), QRQC (`qr_hi`, comp `QrqcHi`), UniformProduction (`up_hi`),
ValueStreamMapping (`vs_hi`, module `value_stream_hi`), WhyWhy (`ww_hi`), XMatrix (`xm_hi`),
Yamazumi (`yz_hi`), ZeroDefects (`zd_hi`). Older: PokaYokeHi (`pk_hi`), PokaYokeMr, QrqcMr.
Telugu / Tamil (31 Oct 2026, one lesson each for the user to review first):
A3ProblemSolvingTe (`a3_te`, module `a3_problem_solving_te`) and A3ProblemSolvingTa
(`a3_ta`, module `a3_problem_solving_ta`; Tamil says இடைவெளி for "gap").
Where the English polish disagreed with its own page numbers, the Hindi polish follows
the pages (Gemba recap 8, QRQC hook 24, UP recap 6,000, Why-Why recap 50 → 15).

Adding one: write the module, `bash tools/new_component.sh <id> <Comp> <DUR_CONST> <module> [lang]`
(TEXT + POLISH on stdin; lang `hi` default, `mr`, `te`, `ta`), add it to `tools/gen_root.py` and run it (writes Root.tsx and
scripts/lessons.ts), then `bash tools/build_hindi.sh <module>` (edge-tts + level + sync).
say() maps every English word left in the voice text (lint flags any Latin letters); it uses
ASCII lookarounds, not ``, so a suffix joined to an acronym ("MESతో", "A3-ஐ") still matches;
cues must match whole caption words (a cue ending in "साथ" won't match "साथ-साथ").
Each mirrors the English lesson (same pages, visuals, polish); cue phrases are in the lesson's language.
On-screen built-in words: `src/ui.ts` has one label set per language; each lesson
component calls `setUI("<lang>")` (and `ensureIndicFont("<lang>")`) at its top.

## Voice
- **RULE (31 Oct 2026): every voice is FEMALE, in every language.** The user asked for
  female voices only; never use a male voice (`hi-IN-MadhurNeural` was used until 31 Oct
  and all its videos were deleted).
- **Hindi: Microsoft neural voice `hi-IN-SwaraNeural` (female)**, set as `VOICE` in each
  `*_hi.py`. Generated with edge-tts, then `import_clones.py <module> out/ms_<id>` levels it
  to −29 LUFS and syncs captions/boxes to its real pauses (`tools/build_hindi.sh` does both;
  `--force` re-voices every clip after a voice change). Not the user's own voice. For
  paid release, use the official Azure Speech service (free tier 0.5M chars/month).
- Scripts are written for a neutral teacher voice (no first-person narrator), so a voice
  change needs no script edits; quoted characters keep their own gender.
- Own-voice options: IndicF5 via `colab_indic_clone.ipynb` (GitHub branch `indic-voice`,
  link https://colab.research.google.com/github/PrashantRMarathe/voice-replacer/blob/indic-voice/colab_indic_clone.ipynb;
  loads IndicF5 weights into f5-tts 1.1.22; free Colab GPU kept failing for the user), or
  ElevenLabs (paid). Drive folder `G:/My Drive/FFIQ_indic/` (`input/`, `out/`, `final/`).
- **Marathi (27 Oct 2026): FEMALE voice `mr-IN-AarohiNeural`** (the user asked for a female voice).
- **Telugu: FEMALE `te-IN-ShrutiNeural`. Tamil: FEMALE `ta-IN-PallaviNeural`** (31 Oct 2026).
  Fonts: Noto Sans Telugu / Tamil via `src/indicFonts.ts`; screen labels in `src/ui.ts`.
- Deliveries go to `final/<language>/` (full English name: `hindi/`, `marathi/`, `tamil/`, ...).

## Render checklist
Standard: `python tools/run_awake.py bash scripts/render_lesson.sh hindi <Comp> ...` does steps 1–3 (Edge
browser, concurrency 1, keeps the PC awake, copies to `final/hindi/` and Drive). Manual:
1. `npx remotion render <Comp> out/<language>/<Comp>.mp4 --concurrency=2` (`=1` if the English chat is rendering).
2. **Normalise the normal (captioned) render to −14 LUFS** (English PLAYBOOK rule; Remotion
   leaves it at the −29 LUFS voice level): `ffmpeg -i in.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -ar 48000 -c:a aac -b:a 192k out.mp4`.
   `...Dub` stays un-normalised (clean narration stem).
3. `npm run srt`, then copy the mp4 + `.srt` to `final/<language>/`.

## Setup notes
- `node_modules` is a junction to `../course_video/node_modules` (no second install).
- Render port **3927** (English uses 3917), so renders never clash.

```bash
python tools/sync_from_english.py                    # pull the latest English design
bash tools/build_hindi.sh gemba_hi [--force]         # female Hindi voice (edge-tts) + level + sync
python tools/gen_root.py                             # register lessons in Root.tsx + scripts/lessons.ts
npm run check
python tools/run_awake.py bash scripts/render_lesson.sh hindi GembaHi   # render -> final/hindi + Drive
```
