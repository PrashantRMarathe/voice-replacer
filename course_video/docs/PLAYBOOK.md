# 📘 Course Video PLAYBOOK

Everything needed to produce a new animated lesson for the **Factory Flow IQ**
Lean Manufacturing course, in the same style as Zero Defects and Yamazumi. A
new chat/session should read this top to bottom before building.

---

## 1. What we're making
Professional **animated explainer videos** (not photorealistic, not slides).
Style: dark navy background, teal accents, clean flat design, friendly female
guide character + PPE factory workers. Each lesson has:
- The user's **cloned narration voice**, plus a quiet music bed and soft card / quiz
  sounds on the normal version (the `...Dub` version is voice-only, see CLAUDE.md rule 4)
- **Sentence captions**: one clean line at a time, no per-word highlight
- **2 quick-check quizzes** (one mid-lesson, one before the outro)
- The **FFIQ brand mark** top-left
- Smooth scene transitions and animated layouts
- 1920×1080, 30 fps, MP4, plus a `...Dub` (no-caption) master and an `.srt`

Why this approach: it's **free**, fully controllable, repeatable across many
lessons, and accurate (text/data are always correct, unlike AI video).

---

## 2. Project map
```
course_video/
  src/
    theme.ts                  # DESIGN SYSTEM: colors, fonts, brand, fps/size
    Root.tsx                  # registers every composition (lesson + Dub)
    fonts.ts                  # loads Google fonts (Poppins, Inter)
    components/
      Background.tsx          # calm navy grid + faint particles
      BrandMark.tsx           # FFIQ badge, top-left (every lesson)
      Captions.tsx            # sentence-line captions from word timings
      Quiz.tsx                # QuizScene: question, think countdown, answer
      ui.tsx / icons.tsx      # RiseIn, GlowCard, line icons
      characters.tsx          # Guide / Worker (custom SVG, poses, PPE)
    scenes/Scene.tsx          # per-scene slide+scale+fade transition
    lessons/
      plan.ts                 # TIMELINE MATH: scene order, quiz placement,
                              #   durations, caption line splitting (pure TS,
                              #   shared by the video, SRT export and checks)
      shared/PageLesson.tsx   # Intro/Page/Outro scenes + the voice-only timeline
      zd/ZeroDefects.tsx      # a page lesson = data + titles (~35 lines)
      zd/{timings,content,quizzes}.json
      yz/Yamazumi.tsx         # same pattern
      EightWastes.tsx, full/  # older hand-built lessons
    captions/<id>/words.json  # {clipKey: [{w,s,e}]} per lesson
  public/audio/<id>/<key>.mp3 # narration clips (cloned voice)
  narration/
    lesson_lib.py             # PIPELINE: edge-tts bootstrap, clone import,
                              #   timings/content/quizzes/words, clone script
    zero_defects.py           # lesson DATA (scripts, pages, quizzes)
    yamazumi.py               # lesson DATA
    import_clones.py          # import cloned WAVs for any lesson (--realign)
    lint_scripts.py           # script style lint (part of npm run check)
    watch_drive.py            # Drive watcher: gate, import, render -> final/
  scripts/
    check.ts                  # pre-render checks (npm run check)
    srt.ts                    # .srt export (npm run srt)
    lessons.ts                # id -> composition registry for the scripts
  out/                        # renders, .srt, clone scripts (gitignored)
    voice_reference/          #   voice_reference_A.wav (approved voice)
  docs/PLAYBOOK.md            # this file (technical)
  docs/AUTOMATION.md          # user guide: the Drive pipeline, status, fixes
  docs/VOICE.md               # voice standard, batch checks, history
  docs/NEW_LESSON_CHECKLIST.md
../colab_clone_drive.ipynb    # STANDARD clone notebook (Drive, Run all)
../colab_clone_voice.ipynb    # backup clone notebook (manual upload)
../tts.py                     # voice engines (F5 + XTTS fallback)
```

---

## 3. Style rules (keep every lesson consistent)
- **Colors/fonts only from `src/theme.ts`.** Headings = Poppins, body = Inter.
  Accent = teal (`#2dd4bf`), danger/red for "waste", green for "good/value".
- **Backgrounds:** always `<Background />`; keep it calm (few faint particles).
- **Entrances:** wrap revealed elements in `<RiseIn delay={n}>`; stagger ~8–12
  frames. Wrap each scene in `<Scene>` for the transition.
- **Pacing:** scene length = narration clip + `PAD` (2.2 s), done by `plan.ts`.
- **Captions** sit bottom-center; keep characters far left/right.
- **Characters:** female guide in a blazer (host); workers in ESD coat + glasses
  + mask + cap. Tasteful and professional only. Poses:
  `pointing|crossed|resting|carrying|reaching`. Expressions:
  `smile|neutral|tired|concerned|surprised`.
- **Audio:** narration first. Normal version: quiet music bed + soft card / quiz
  sounds (polish layer), normalised to −14 LUFS. `...Dub` version: narration only.

---

## 4. How to make a NEW page lesson (step by step)
Say the new lesson is **5S System**, id `fs`, module `five_s`.

1. **Data:** copy `narration/zero_defects.py` → `narration/five_s.py`. Set
   `ID = "fs"`, `NAME = "five_s"`, write `INTRO_SCRIPT`, `OUTRO_SCRIPT`, the
   `PAGES` (title, 2–4 `points`, `example` + `example_cue`, spoken `script`; see
   §4c) and 2 `QUIZZES`
   (`after` = page key, on-screen `question/options/correct/explanation`, spoken
   `q_script`/`a_script`). Add `say()` only for pronunciation fixes.
2. **Bootstrap:** `python narration/five_s.py`. It voices any missing clip with
   edge-tts (never overwrites existing clips; `--force` re-voices all) and
   writes timings/content/quizzes/words plus `out/five_s.json`.
3. **Component:** copy `src/lessons/zd/ZeroDefects.tsx` → `src/lessons/fs/FiveS.tsx`;
   change the paths, `id`, `TEXT` titles and export names. For a custom visual
   on one page, pass `renderBlock={(b) => b.key === "p04" ? <MyScene/> : undefined}`.
4. **Register:** add `FiveS` and `FiveSDub` (`defaultProps={{ captions: false }}`)
   to `src/Root.tsx`, and `fs: "FiveS"` to `scripts/lessons.ts`.
5. **Check:** `npm run check` (types, audio, captions, quizzes, Root).
6. **Preview:** `npx remotion still FiveS out/fives_check.png --frame=120`.
7. **Queue the voice:** copy `out/five_s.json` to `G:/My Drive/FFIQ_voice/input/`
   and ask the user to **Run all** in `colab_clone_drive.ipynb` (§6a).
8. **The watcher does the rest:** quality gate, import, `npm run check`, SRT,
   render → `FFIQ_voice/final/FiveS.mp4`. Manual equivalent:
   `python narration/import_clones.py five_s <dir>`, then
   `npx remotion render FiveS out/five-s.mp4` and `npm run srt`.

---

## 4b. Script style guide (how the narration should sound)
The voice is a **teacher talking to one learner**, not a textbook read aloud.
On-screen bullets carry the facts; the narration explains *why* and *what it
looks like on the floor*. `npm run check` runs `narration/lint_scripts.py`,
which flags breaks of the measurable rules (marked **[lint]**).

1. **Hook first.** The intro opens with a problem, a cost or a moment, never
   "Welcome to this lesson on…" **[lint]**. Then say what the learner will be
   able to do.
   *"One connector, plugged in backwards, cost a line thirty-two thousand rupees…"*
2. **One story thread.** Follow one person, one line and one product through
   the lesson (e.g. *Priya's phone-assembly line*). Side lines are fine for
   contrast. On-screen examples use the same story.
3. **Talk to the learner.** Every page has "you"/"your" or a question **[lint]**.
   Aim for at least 2 "you"s and 1 question a page.
4. **Short spoken sentences.** At most 20 words each, one idea per
   sentence **[lint]**.
5. **Vary the rhythm.** Open pages with a story beat, a question, a surprising
   number or a common mistake. "For example" at most 3 times per lesson **[lint]**.
6. **Narrate, don't read the screen.** Say a number once and let the screen show
   the math. At most 5 number words in one sentence **[lint]**.
7. **Link the pages.** End most pages with a one-line bridge or question that
   leads into the next ("But what if people still slip?").
8. **Even pacing.** 65–80 words per page; lint flags under 60 or over 90 **[lint]**.
9. **Strong ending.** The outro gives 3 takeaways, one action for this week,
   and a pointer to the next lesson.
10. **Quizzes test thinking.** At least one scenario quiz ("What should the team
    do first?"), not only recall or arithmetic.
11. **Spoken forms.** Spell acronyms as letters ("P-P-M", "M-E-S"), write
    numbers as words in scripts, and use `say()` for pronunciation fixes.
12. **Unsure how a term is spoken? Look it up, then confirm.** For acronyms
    said as a word (TAKT, SMED, OEE…), Japanese Lean terms, product or company
    names: first search how practitioners pronounce it (Lean glossaries,
    dictionaries, training videos). If sources agree, use that and tell the user
    in the hand-off. If sources disagree or find nothing, ASK the user before
    making the clone file. A wrong guess costs a full re-clone. Put the confirmed form in
    the lesson's `say()`; on-screen text keeps the proper spelling. The script
    lint flags every ALL-CAPS word left in the spoken text **[lint]**.
    Confirmed so far:

    | Term | Spoken as | Lesson |
    |---|---|---|
    | TAKT | "tact" | Yamazumi |
    | OEE | "O-E-E", letter by letter (confirmed by the user) | all |
    | RACI | "ray-see" (written "racey" in `say()`; checked against RACI guides) | X-Matrix |
    | Heijunka | "hay-JOON-kah" (written "Hay-joon-kah"; sources split, chosen by the user) | Uniform Production |
    | Hoshin Kanri | "HOH-shin KAHN-ree" (written "Hoe-shin Kahn-ree"; confirmed by the user) | X-Matrix |
    | EPEI | letter by letter, "E-P-E-I" (confirmed by the user) | Uniform Production |
    | Muda, Mura, Muri, Gemba, Kanban, Kaizen | as spelled (MOO-dah, GEM-bah, KAHN-bahn, KYE-zen; confirmed) | all |
    | FIFO | avoided: say "first-in, first-out" | all |
    | Jidoka, Andon, Poka Yoke | as spelled (jee-DOH-kah, AHN-don, POH-kah YOH-keh; voiced since Zero Defects) | all |
    | TIMWOODS | "Tim Woods" (sources write it "TIM WOODS") | Muda, Mura, Muri |
    | QRQC | letter by letter, "Q-R-Q-C" (no vowels, no word form) | QRQC |
    | Ishikawa | as spelled, "ee-shee-KAH-wah" | Root Cause Analysis |
    | Shigeo Shingo | "Shee-gay-oh Shingo" | Poka Yoke |
    | Genbutsu | avoided (sources thin): say "the real parts" | QRQC |
    | Dojo | English word, "DOH-joh" | Skill Matrix |
    | OPL, RCA, DOE, MSA, LPA, CTQ, AOI, NVR, CCTV, UPH, UPPH, OJT, PCB, BOM, PLC | letter by letter | M to T |
    | PPM, DPMO, FPY, MES, SOP, SKU, ESD, ECRS, SMED, PFMEA (F-M-E-A), WIP | letter by letter ("P-P-M") | all |

13. **One set of numbers per story.** A number used on two pages must agree
    (demand per shift vs per day, a station's cycle time, a defect count). Work
    out every derived number (TAKT, capacity, %, payback, "a fifth") from the
    story's base numbers, and check the voice says what the screen shows.
14. **The story obeys the lesson.** Don't let the worked example break a rule
    the same lesson teaches (e.g. "equal to TAKT leaves no headroom", then
    balancing a station to exactly TAKT). Keep one cause per story thread.
15. **Technically true.** Check engineering claims you're not sure of
    (soldering, test, materials). A buyer from the industry spots them.
16. **Course order A→Z.** Never say "you met this in the X lesson" for a
    lesson that comes later. Each outro names the next letter's lesson; Z
    closes the whole course.
17. **A fresh case per lesson.** Don't reuse another lesson's case study or
    its numbers (e.g. the same "wrong spacer" story, the same "60 → 12, 80%,
    6-month payback").
18. **Terms with digits** (A3, 3G, 5G, 5W2H) need a `say()` fix too ("A-three");
    the lint flags any left in the spoken text **[lint]**.

Full A–Z review, 28 Oct 2026: these rules come from the errors it found in
C, E, G, P, S, U, V and W.

Reference lesson: `narration/zero_defects.py` (rewritten to this guide).

---

## 4c. On-screen boxes match the voice
Every box on a page must be something the narration actually says, and it
appears at the moment the voice says it.
- `points`: 2–4 `(text, cue)` pairs. `text` is the short on-screen line; `cue`
  is an exact phrase from the page `script` where that point is spoken. Don't
  pad to 4: if the narration covers 3 points, show 3 (2 or 3 sit in one row,
  4 as 2×2).
- `example` + `example_cue`: the example box shows the story beat the voice
  tells, and appears at its cue. Numbers on screen match the spoken numbers.
- `lesson_lib.page_content` turns each cue into a time (`at`, `exampleAt` in
  `content.json`) from the clip's word timings; `PageScene` reveals each box
  then and outlines the one being explained. Re-run after any edit:
  `python narration/import_clones.py <NAME> --realign` (no re-clone needed:
  the voice doesn't change).
- The script lint fails a page whose cue isn't in the script, whose points
  are out of spoken order, or that has fewer than 2 or more than 4 points;
  `npm run check` warns about any page whose boxes aren't synced.

---

## 5. Voice, captions, sound
- **Draft voice (timing scout only):** `en-US-ChristopherNeural`, `rate="-6%"`,
  edge-tts with `boundary="WordBoundary"` (in `lesson_lib.py`).
- **Final voice = CLONED** (see §6). This is the standard.
- **Captions:** `Captions.tsx` shows one line at a time. `plan.ts` `toLines()`
  splits sentences longer than ~72 characters at a comma near the middle
  (never after a little word like "a"/"the"). The `.srt` uses the same lines.
- **Caption sync (§6, "Caption sync"):** caption timing comes from the clip's real
  pauses, not an even spread, so each line changes when the voice does.
- **Audio (CLAUDE.md rule 4).** Normal version: narration + polish layer (music bed
  from `make_music.py`, card / quiz sounds from `make_demo_sfx.py`), then
  `ffmpeg -af loudnorm=I=-14:TP=-1.5:LRA=11`. `...Dub` version: narration only.
  `make_sfx.py` (whoosh/ding/pop) is legacy and unused.

---

## 6. Voice = CLONE-ONLY pipeline (the reliable way)
Do NOT use the full Colab dub tool on the finished video. It transcribes and
re-times (guesses), which caused **repeated sentences**. Instead the voice is
cloned clip by clip and imported. **Standard route: the Drive pipeline (§6a).**
The steps below are what it automates (and the manual fallback). The voice
standard, batch checks and history are in **`docs/VOICE.md`**.

1. **Clone script:** the generator writes `out/<NAME>.json` (`key` → spoken
   text, including `quizN_q` / `quizN_a`). Hand it to the user to upload. Course
   content stays OFF GitHub.
2. **Clone on Colab:** `colab_clone_drive.ipynb` (standard, reads Drive `input/`)
   or `colab_clone_voice.ipynb` (backup, manual upload). Engine **F5 1.1.22**,
   voice clip **`voice_reference_A.wav`** (see `docs/VOICE.md`). Both notebooks
   stop if F5 doesn't import or the engine isn't F5.
3. **Import:** `python narration/import_clones.py <NAME> [clones_dir]`. Converts
   to `public/audio/<ID>/<key>.mp3` at a fixed loudness (gain only, to
   `TARGET_LUFS` = −29, peaks ≤ −3 dB, matching the chosen voice), rewrites `timings.json` to the cloned
   durations, sizes each quiz's think countdown to its question clip, and
   times captions to the clip's REAL pauses (ffmpeg silencedetect: sentence
   ends snap to the nearest pause, then commas). `--realign` redoes only the
   captions from the current clips. A partial batch (e.g. only new quiz
   clips) is fine; clips without a WAV keep their current mp3.
4. **Render** the normal and `...Dub` compositions, then `npm run srt`.

### Caption sync: how it works
The cloned voice has no word timestamps, and spreading words evenly over a clip
drifts (measured: avg 0.5 s, worst 1.7 s late on Yamazumi), because the voice
pauses between sentences and changes pace. `aligned_word_times()` in
`lesson_lib.py` instead:
1. **Finds the real pauses** with ffmpeg `silencedetect` (−35 dB, ≥ 0.2 s).
2. **Matches sentence ends (`. ? !`) to pauses for the WHOLE clip at once**
   (`_match_sentence_ends`, dynamic programming): it picks the set of pauses that
   keeps the speaking pace between anchors closest to the clip's average, with a
   penalty for leaving a sentence unmatched or talking through a long pause.
   (The first version matched one sentence at a time; one miss shifted every
   later caption by ~2 s on Yamazumi pages 6, 8 and 14.)
3. **Snaps commas/semicolons/colons/dashes** to a remaining pause within 0.6 s,
   so split caption lines also change on time.
4. **Spreads the words between anchors** by character length.

Result: every sentence on a real pause (130/130 Zero Defects, 141/141
Yamazumi). A sentence the voice runs straight through has no pause; its caption
is placed by pace. Runs on every import; captions only:
`python narration/import_clones.py <NAME> --realign`.

---

## 6a. Automated pipeline (Google Drive)
The standard way to clone and render. Drive folder `G:/My Drive/FFIQ_voice/`
(Google Drive for desktop, folder set "Available offline"):

| Path | Role |
|---|---|
| `voice_reference_A.wav` | approved voice clip (md5 `b57f89e3…`) |
| `input/<NAME>.json` | clone scripts waiting (Claude copies `out/<NAME>.json` here) |
| `input/done/` | finished scripts |
| `output/<NAME>/*.wav` + `_DONE.json` | clones; `_DONE.json` = complete, with engine, F5 version, voice md5 |
| `output/_archive/` | earlier runs of a re-queued lesson |
| `final/<Comp>.mp4` + `.srt` | finished videos |
| `status.txt`, `watcher.log` | progress, readable on a phone |

1. Claude copies `out/<NAME>.json` to `input/`.
2. User opens `colab_clone_drive.ipynb` from GitHub → **Runtime → Run all**.
   Clips are saved one by one, so after a disconnect Run all resumes.
3. `python narration/watch_drive.py` (runs on the PC) sees `_DONE.json` and:
   quality gate (F5 not XTTS, approved voice md5, brightness ≤ 1050 Hz, pace
   85–180 wpm) → import → `npm run check` → SRT → render (1 retry) → `final/`.
   A failed gate writes `_HELD.json` (nothing imported); a later error writes
   `_FAILED.json`. Delete it to retry; `--force <NAME>` skips the gate.
4. **Failure handling in Colab:** each lesson runs in its own error guard. A
   lesson that raises writes `output/<NAME>/_ERROR.json` (clip + error + trace),
   stays in `input/`, and the run continues with the next lesson; the watcher
   shows it as FAILED. `_DONE.json` stores the script md5: a finished lesson
   whose script wasn't moved yet is just filed under `done/` (not re-cloned);
   a changed script archives the old run to `output/_archive/` and re-clones.

---

## 6b. Quizzes (required: 2 per lesson)
Defined in the lesson module's `QUIZZES`, placed by `after: "<page key>"`. Each
shows the question + options + `Think… N`, then highlights the correct option
with the explanation. **No sound effect.**
- **Narrated** (standard): when `quizN_q` and `quizN_a` clips exist, the question
  is read during the countdown and the answer plays on reveal.
- **Silent fallback:** before those clips are cloned, the quiz is a fixed 6 s
  think + 7 s hold. `npm run check` warns until they're imported.

---

## 7. Rendering options
- **Local:** `npx remotion render <Comp> out/x.mp4` (~30–40 min for a 10-min
  lesson). `remotion.config.ts` sets concurrency 2, a 120 s timeout and port
  3917, so no extra flags are needed. Keep the PC awake (the watcher does this
  while rendering; a closed lid still sleeps) and check the real exit code:
  piping through `tail` hides a failure.
- **Voice stem (for dubbing):** the audio is voice-only, so
  `npx remotion render <Comp>Dub out/<comp>-voice.wav --codec=wav` IS the clean
  narration stem, exactly on the timeline.
- **Colab (no good local GPU):** `colab_render.ipynb`. Use `--gl=angle` (or `swangle`).

---

## 8. Gotchas (learned the hard way)
- `react-peeps` / `react-open-peeps` are **broken on React 19**. Use the custom
  SVG characters.
- edge-tts default boundary is **SentenceBoundary**: pass `boundary="WordBoundary"`
  or you get zero word timings (handled in `lesson_lib.py`).
- Re-running a generator **never overwrites cloned clips** unless `--force`.
- `scripts/*.ts` run on Node's built-in TypeScript support (Node ≥ 22.6); they
  import `plan.ts`, so keep `plan.ts` free of React/Remotion imports.
- Give per-character SVG gradients unique ids (`React.useId()`), already
  handled in `characters.tsx`.
- **Port clash:** another dev server on :3000 (e.g. a Next.js app) answered
  Remotion's audio requests with 404s and killed a render mid-way. Remotion is
  pinned to port 3917 in `remotion.config.ts` (also concurrency 2, 120 s timeout).
- **Fonts:** `fonts.ts` loads only Poppins/Inter 400–700, normal, latin.
  Loading every variant (all weights, italics, subsets) times out renders with
  "Timeout … Fetching Poppins font". Add a weight there before using it.
- Captions drifting? Re-run `import_clones.py <NAME> --realign` (never go back
  to evenly spread `word_times()` for cloned clips).
- **PC sleep kills renders:** an overnight render died at 29% ("Session
  closed"). The watcher holds Windows awake while it works.
- **Colab notebooks:** Colab now runs Python 3.13. Shell lines (`!...`) need
  `echo`, not `print`. Install every voice package in ONE `pip` call, or pins
  like `transformers<5` get undone (this broke F5, see `docs/VOICE.md`). Use
  `raise RuntimeError` (not `SystemExit`) to stop **Run all**. `os.chdir('/content')`
  before cloning the repo so re-runs don't nest folders.
- **Before importing any clone batch**, check it's F5 (`docs/VOICE.md`): peaks
  at exactly 0 dBFS on every clip = XTTS. The watcher's gate does this.
- Don't commit `node_modules/` or `out/`.

---

## 9. Optional: photorealistic AI B-roll
Not the main style, but available: `AI_VIDEO_GUIDE.md` + `KLING_PROMPTS.md` +
`colab_ai_video.ipynb`. Costs money or needs a cloud GPU; text/data come out
wrong, so only use for background shots and overlay correct text with Remotion.
