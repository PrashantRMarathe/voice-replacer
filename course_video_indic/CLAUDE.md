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
Run it before starting new work here, then `npm run check`. It skips any English item that
isn't there (the laptop has no English sfx/music: audio is untracked) and keeps ours; before
4 Nov 2026 it deleted ours first.

## Lessons
Hindi set (31 Oct 2026): one per finished English lesson, translated from the current
English text, same pages/visuals/polish. Module `narration/<english_name>_hi.py`,
id `<english id>_hi`, composition `<EnglishComp>Hi` / `...HiDub`:
A3ProblemSolving (`a3_hi`), DesignThinking (`dt_hi`), Gemba (`gb_hi`), Hancho (`hc_hi`),
OnePointLesson (`op_hi`), QRQC (`qr_hi`, comp `QrqcHi`), UniformProduction (`up_hi`),
ValueStreamMapping (`vs_hi`, module `value_stream_hi`), WhyWhy (`ww_hi`), XMatrix (`xm_hi`),
Yamazumi (`yz_hi`), ZeroDefects (`zd_hi`). Older: PokaYokeHi (`pk_hi`), PokaYokeMr, QrqcMr.
Added 2 Nov 2026, completing all 26: BurnDownChart (`bd_hi`), CycleTimeStudy (`ct_hi`),
EliminationOfWaste (`ew_hi`), FMEA (`fm_hi`, comp `FMEAHi`), Ishikawa (`ik_hi`), Jidoka (`jd_hi`),
Kaizen (`kz_hi`), LowCostAutomation (`lc_hi`), MudaMuraMuri (`mm_hi`), NextInspection (`ni_hi`),
RootCauseAnalysis (`rc_hi`, module `root_cause_hi`), SkillMatrix (`sk_hi`), TaktTime (`tt_hi`).
Telugu / Tamil pilots (made 31 Oct 2026, approved by the user 2 Nov 2026; both pass validate_video):
A3ProblemSolvingTe (`a3_te`, module `a3_problem_solving_te`) and A3ProblemSolvingTa
(`a3_ta`, module `a3_problem_solving_ta`; Tamil says இடைவெளி for "gap").
Telugu set (laptop, 2–3 Nov 2026): all 26, voiced (`te-IN-ShrutiNeural`), id `<english id>_te`,
comp `<EnglishComp>Te` (`FMEATe`, `QrqcTe`; modules mirror the Hindi names, e.g. `root_cause_te`).
Translated from the Hindi with `tools/translate_lesson.py` (`dump <x>_hi` -> numbered lines ->
`build <x>_hi te <file>`; sources in `out/te_tr/`). 13 per-language Telugu videos were rendered
(A3 … Low Cost Automation, in `final/telugu/`) before the switch to dub tracks stopped that render.
The pronunciation sample `out/pron_test/te_words.mp3` is still waiting for the user's notes.
Marathi set (PC, 6–7 Nov 2026): all 26, voiced (`mr-IN-AarohiNeural`), id `<english id>_mr`,
comp `<EnglishComp>Mr` (`FMEAMr`, `QrqcMr`; modules mirror the Hindi names, e.g. `root_cause_mr`).
Translated from the current Hindi with `tools/translate_lesson.py` (`build <x>_hi mr <file>`;
sources in `out/mr_tr/`, PC only). Marathi is Devanagari, so the tool skips its "no Hindi left"
checks for `mr`; English terms are voiced with `TERMS["mr"]` in `tools/lesson_terms.py`
(Hindi forms without nukta, झ for an English z, व्ही for V, ॅ/ॲ for the English "a").
Sentences end with "." (not the Hindi danda). The old PokaYokeMr/QrqcMr (27 Oct) were rebuilt
from the current Hindi; their old audio is in `out/old_mr/`. The user approved the Marathi voice
on a Poka Yoke demo (6 Nov 2026, "Marathi is good"). No per-language Marathi video is rendered:
Marathi exists only as a dub track. A Marathi `say_words.py` sample was not made.
Kannada pilot (PC, 7 Nov 2026): PokaYokeKn (`pk_kn`, module `poka_yoke_kn`), voiced
`kn-IN-SapnaNeural` (female), translated from the Hindi (`out/kn_tr/poka_yoke_kn.txt`, PC only).
`TERMS["kn"]` = the Telugu forms in Kannada letters (ಎಂ for M); screen labels `ui.ts` `kn`;
font Noto Sans Kannada. Sentences end with ".". Only a dub track (fastest clip 1.098), packed into
`final/dub/PokaYoke.mp4` with 5 tracks. The user approved it ("Kannada OK, do all").
Kannada set (PC, 7–10 Nov 2026): all 26, voiced (`kn-IN-SapnaNeural`), id `<english id>_kn`,
comp `<EnglishComp>Kn` (`FMEAKn`, `QrqcKn`; modules mirror the Hindi names). Translated from the
Hindi (`build <x>_hi kn <file>`; sources in `out/kn_tr/`, PC only). Only dub tracks, no
per-language video. 9 clips came out over 1.14 and were shortened + re-voiced (A3 p01/p09,
DT p06/quiz2_q, Ishikawa p10, MMM p10, OPL p14, QRQC intro, UP p03); all 26 are now ≤ 1.14.
Where the English polish disagreed with its own page numbers, the Hindi polish follows
the pages (Gemba recap 8, QRQC hook 24, UP recap 6,000, Why-Why hook 21 and recap 50 → 15).

Adding one: write the module, `bash tools/new_component.sh <id> <Comp> <DUR_CONST> <module> [lang]`
(TEXT + POLISH on stdin; lang `hi` default, `mr`, `te`, `ta`), add it to `tools/gen_root.py` and run it (writes Root.tsx and
scripts/lessons.ts), then `bash tools/build_hindi.sh <module>` (edge-tts + level + sync).
say() maps every English word left in the voice text (lint flags any Latin letters); it uses
ASCII lookarounds, not ``, so a suffix joined to an acronym ("MESతో", "A3-ஐ") still matches;
cues must match whole caption words (a cue ending in "साथ" won't match "साथ-साथ").
Each mirrors the English lesson (same pages, visuals, polish); cue phrases are in the lesson's language.
On-screen built-in words: `src/ui.ts` has one label set per language; each lesson
component calls `setUI("<lang>")` (and `ensureIndicFont("<lang>")`) at its top.

## Dub tracks (production, 4 Nov 2026)
The user's production plan: **one English video per lesson, every language as its own audio
track + soft subtitles** (like a dubbed film): ~15 MB per language instead of a ~320 MB video.
Pilot (Zero Defects, Hindi + Telugu) approved 4 Nov 2026; speed-ups up to 14% sound fine.
- `python tools/make_dub.py` -> `src/dub/<id>/` (copies of the English lesson data + `<Comp>Dub.tsx`,
  generated from `../course_video/src/lessons/<id>/`, read only), `src/dub/index.tsx`
  (own entry point, so Root.tsx and `npm run check` are untouched), `src/dub/lessons.json`.
  Re-run after the English lessons change. `<Comp>DubVideo` = English video, English screen
  words (`setUI("en")`), no captions, music + effects, no voice.
- `bash scripts/render_dub.sh "hi te" [Comp ...]` (wrap in `tools/run_awake.py`) renders each
  `<Comp>DubVideo` once to `out/dub/<Comp>_video.mp4` (skips ones already there), then runs
  `tools/fit_dub.py all <id> hi te`:
  - `fit`: the language's voiced clips (`public/audio/<id>_<lang>/`) -> `public/audio/<id>_dub_<lang>/`,
    end silence trimmed, sped up (atempo) only past the English clip length + 1 s (PAD is 2.2 s);
  - `track`: each clip placed at the English clip's start (same maths as plan.ts), mixed over the
    video's music/effects with ffmpeg (seconds, no render), -14 LUFS -> `<Comp>_<lang>.m4a`,
    plus `<Comp>_<lang>.srt` from the lesson's own caption words;
  - `pack`: `final/dub/<Comp>.mp4` = video + every language track + every subtitle (players switch
    language), and the separate .m4a/.srt, all copied to Drive `FFIQ_indic/final/dub/`.
- Visual highlights follow the English timing (the user accepted this). On-screen words stay English.
- Remotion audio-only render (`--codec=aac`) walks every frame and is as slow as video: don't use it.
- No English voice track yet: the English voice clips are on the PC only. To add one, voice
  folder `audio/<id>` from the English project with speed 1 (TODO on the PC).
- Telugu is ~5% longer than English, Hindi ~10%: only a few pages need 10–14% speed-up.
- Marathi runs ~15% longer. Rule for every dub track: no clip faster than 1.14 (read the exact
  value in `public/audio/<id>_dub_<lang>/speed.json`, the printout rounds). A clip over 1.14 gets
  its line shortened (same meaning), voiced again (delete that `.mp3` in `public/audio/<id>_<lang>/`,
  rerun `tools/voice_lessons.sh`) and fitted again. Extra commas add pauses: cut words instead.
- `pack` must list every language (`pack <id> hi te ta mr`), or the packed mp4 and the Drive copy
  lose the tracks left out. Check: `ffprobe` shows 4 audio + 4 subtitle streams.

### Dub render status (PC, 7 Nov 2026)
- All 26 English dub videos are rendered. On the PC they live in the second checkout
  `D:\AIL\Website\voice-replacer-dub\course_video_indic\out\dub\<Comp>_video.mp4`; this
  checkout's `out/dub/` holds hard links to them (`cp -l`, no extra disk), so `fit_dub.py`
  works here. Never render them again.
- **All 26 packed with 4 tracks: Hindi, Telugu, Tamil, Marathi** (audio + soft subtitles), in
  `final/dub/<Comp>.mp4` + Drive `FFIQ_indic/final/dub/` (+ separate `<Comp>_<lang>.m4a/.srt`).
  Marathi was added 6–7 Nov 2026 on the PC; every Marathi clip is at or below 1.14 speed.
- Kannada (`kn`, code `kan`): all 26 packed as `pack <id> hi te ta mr kn` (10 Nov 2026),
  so every `final/dub/<Comp>.mp4` now has 5 audio + 5 subtitle streams.
- Next language: translate + voice, then `fit_dub.py fit/track <id> <lang>` and
  `pack <id> hi te ta mr <lang>` (all languages, every time).
- PC TODO: the English voice track (English clips are only on the PC, see above).

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

## Pronunciation (31 Oct 2026)
- `narration/pronounce.py`: one voice-only respelling list per language (`PRON`), shared by
  every lesson; each module's say() ends with `return pronounce.fix(text, LANG)` (new modules too).
  Hindi so far: ज़रूरी→जरूरी, जाना-पहचाना→जाना पेहचाना, विज़ुअल→"visual" (the user's picks).
- English terms stay in each module's `SPOKEN` native-script forms (एस-ओ-पी, गेम्बा). The user
  heard English-letter forms (S-O-P, A-three) in Swara's voice and said the old way is better.
  `LATIN_OK` lists the few words voiced in English letters (lint allows only those).
- Before voicing a language: `python tools/say_words.py all_<lang>` -> `out/pron_test/<lang>_words.mp3`
  + `.txt` (every English term / PRON word in a real sentence, numbered). For Hindi the
  user marks bad numbers. For every other language the user can't judge (6 Nov 2026): Claude
  checks the sample with Whisper (see `docs/LANGUAGES_PLAN.md`); fix them in `pronounce.py`.
- After a `pronounce.py` change: `python tools/revoice.py all_<lang>` (or module names; `--dry`
  lists) re-voices ONLY clips whose spoken text changed (`public/audio/<id>/spoken.json`).
- Stay on free edge-tts voices (the user declined paid voices, 31 Oct 2026). The videos must
  sound fluent: the viewers are professionals.

## Two machines
See `docs/WORKPLAN.md`: PC edits/voices/commits and renders; the laptop only renders.
Exceptions: all Telugu work is done (and committed) on the laptop since 2 Nov 2026, and the
laptop renders the dub videos. Laptop Telugu audio is copied to Drive `FFIQ_sync/audio/<id>_te/`.
On the laptop, give `tools/run_awake.py` Git Bash's full path
(`C:/Users/PrashantMarathe-AIL/AppData/Local/Programs/Git/usr/bin/bash.exe`): plain `bash` is WSL.
`tools/jobs.ps1` (queue), `tools/worker.ps1` (render + `tools/validate_video.py` + copy to final),
`tools/pc_publish.ps1` (audio -> Drive `FFIQ_sync`). Every video is validated before `final/`.

## Render checklist
Standard: `python tools/run_awake.py bash scripts/render_lesson.sh hindi <Comp> ...` does steps 1–3 (Edge
browser, concurrency 1, keeps the PC awake, copies to `final/hindi/` and Drive). Each render is
retried up to 3 times: Edge sometimes fails to start right after a long render ("Getting
compositions" -> `[object Object]`), which used to stop the whole queue. Manual:
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
python tools/translate_lesson.py dump gemba_hi       # numbered strings to translate (then: build gemba_hi te <file>)
bash tools/voice_lessons.sh gemba_te ...             # voice many lessons (watchdog), then level + sync
python tools/make_dub.py                             # English dub lessons -> src/dub/
python tools/run_awake.py bash scripts/render_dub.sh "hi te"   # English videos + language tracks -> final/dub + Drive
python tools/fit_dub.py all zd hi te                 # one lesson's tracks again (video already rendered)
```
