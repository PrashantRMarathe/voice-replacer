# CLAUDE.md — Indian-language course videos (separate project)

Hindi (and later Marathi, Tamil, Kannada, Telugu) versions of the Factory Flow IQ
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
| Lesson | Module (ID) | Composition |
|---|---|---|
| Poka Yoke (P) | `narration/poka_yoke_hi.py` (`pk_hi`) | `PokaYokeHi` / `PokaYokeHiDub` |
| Uniform Production (U) | `narration/uniform_production_hi.py` (`up_hi`) | `UniformProductionHi` / `...Dub` |
| Poka Yoke (P), Marathi | `narration/poka_yoke_mr.py` (`pk_mr`) | `PokaYokeMr` / `PokaYokeMrDub` |
| QRQC (Q), Marathi | `narration/qrqc_mr.py` (`qr_mr`) | `QrqcMr` / `QrqcMrDub` |
Each mirrors the English lesson (same pages, visuals, polish); cue phrases are in the lesson's language.
On-screen built-in words: `src/ui.ts` has one label set per language; each lesson
component calls `setUI("<lang>")` (and `ensureIndicFont("<lang>")`) at its top.

## Voice
- **Current choice (26 Oct 2026): Microsoft Hindi neural voice `hi-IN-MadhurNeural`**
  (male), generated with edge-tts, then `import_clones.py <module> out/ms_<id>` levels it
  to −29 LUFS and syncs captions/boxes to its real pauses. Not the user's own voice. For
  paid release, use the official Azure Speech service (free tier 0.5M chars/month).
- Own-voice options: IndicF5 via `colab_indic_clone.ipynb` (GitHub branch `indic-voice`,
  link https://colab.research.google.com/github/PrashantRMarathe/voice-replacer/blob/indic-voice/colab_indic_clone.ipynb;
  loads IndicF5 weights into f5-tts 1.1.22; free Colab GPU kept failing for the user), or
  ElevenLabs (paid). Drive folder `G:/My Drive/FFIQ_indic/` (`input/`, `out/`, `final/`).
- **Marathi (27 Oct 2026): FEMALE voice `mr-IN-AarohiNeural`** (the user asked for a female voice).
- Deliveries go to `final/<language>/` (full English name: `hindi/`, `marathi/`, `tamil/`, ...).

## Render checklist
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
python narration/poka_yoke_hi.py                     # Hindi voice (edge-tts, missing clips)
python narration/import_clones.py poka_yoke_hi out/ms_pk   # level + sync (wav copies of the mp3s)
npm run check
npx remotion render PokaYokeHi out/poka-yoke-hi.mp4
```
