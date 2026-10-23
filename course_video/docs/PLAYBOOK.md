# 📘 Course Video PLAYBOOK

Everything needed to produce a new animated lesson for the Lean Manufacturing
course, in the same style as the 8 Wastes lesson. A new chat/session should read
this top to bottom before building.

---

## 1. What we're making
Professional **animated explainer videos** (not photorealistic, not slides).
Style: dark navy background, teal accents, clean flat design, friendly female
guide character + PPE factory workers acting out concepts. Each lesson has:
- Narration voice (free neural voice, swappable to a cloned voice)
- Word-synced "karaoke" captions
- Soft background music + subtle sound effects (whoosh/ding)
- Smooth scene transitions and animated diagrams
- 1920×1080, 30 fps, exported as MP4

Why this approach: it's **free**, fully controllable, repeatable across many
lessons, and accurate (text/data are always correct — unlike AI video).

---

## 2. Project map
```
course_video/
  src/
    theme.ts                  # DESIGN SYSTEM: colors, fonts, brand, fps/size
    Root.tsx                  # registers every composition (lesson)
    index.ts                  # entry (registerRoot)
    fonts.ts                  # loads Google fonts (Poppins, Inter)
    components/
      Background.tsx          # animated navy grid + particles backdrop
      ui.tsx                  # RiseIn (entrance), GlowCard (numbered card)
      icons.tsx               # custom SVG line-icons (draw-on animation)
      Captions.tsx            # karaoke captions from *.words.json
      characters.tsx          # Character/Guide/Worker (custom SVG, poses, PPE)
    scenes/
      Scene.tsx               # per-scene wrapper: slide+scale+fade transition
    lessons/
      EightWastes.tsx         # the short lesson (+ EightWastesDub via prop)
      CharacterSample.tsx     # character demo
      full/
        FullEightWastes.tsx   # the ~9-min lesson (data-driven deep dives)
        timings.json          # per-scene narration seconds (generated)
        content.json          # per-waste on-screen text (generated)
    captions/
      *.words.json            # word timings per scene (copied from public/audio)
  public/audio/
    *.mp3, *.words.json       # short-lesson narration + word timings
    full/*.mp3                # full-lesson narration
    music.mp3                 # background music bed
    sfx/whoosh|ding|pop.mp3   # sound effects
  narration/
    make_narration.py         # edge-tts voice + word timings (short lesson)
    full_lesson.py            # full lesson: content + voice + timings.json
    make_music.py             # generate music bed (numpy, royalty-free)
    make_sfx.py               # generate SFX (numpy)
  out/                        # rendered videos + stems (gitignored)
  CLAUDE.md                   # quick rules (auto-loaded)
  docs/PLAYBOOK.md            # this file
  docs/NEW_LESSON_CHECKLIST.md
  DUB_WORKFLOW.md             # clean dubbing with stems
  AI_VIDEO_GUIDE.md           # optional photorealistic B-roll (Colab/Kling)
  KLING_PROMPTS.md            # prompt pack for AI B-roll
  colab_render.ipynb          # render lessons on Colab
  colab_ai_video.ipynb        # generate AI B-roll on Colab
```

---

## 3. Style rules (keep every lesson consistent)
- **Colors/fonts only from `src/theme.ts`.** Headings = Poppins, body = Inter.
  Accent = teal (`#2dd4bf`), danger/red for "waste", green for "good/value".
- **Backgrounds:** always `<Background />` behind scenes; body bg = `theme.colors.bg`.
- **Entrances:** wrap revealed elements in `<RiseIn delay={n}>`; stagger items by
  ~8–12 frames. Wrap each scene in `<Scene>` for the transition.
- **Pacing:** scene length = narration length + a small pad (short scenes ~2.8s,
  deep-dive scenes ~3.6s). Keep motion going during holds (glow pulses, particles).
- **Captions** sit at the bottom center; keep characters to the far left/right so
  they don't overlap the caption bar.
- **Characters:** female guide in a blazer (host, intro + outro + reactions);
  workers in ESD coat + glasses + mask + cap act out each waste. Tasteful and
  professional only. Poses: `pointing|crossed|resting|carrying|reaching`.
  Expressions: `smile|neutral|tired|concerned|surprised`.
- **Sound:** one `whoosh` at each scene start; a `ding` on a key reveal; music bed
  at volume ~0.14–0.16; whoosh ~0.5, ding ~0.35.

---

## 4. How to make a NEW lesson (step by step)
Say the new lesson is **5S System**. Create `FiveS` (and `FiveSDub`).

### Step 1 — Write the narration script
Decide the scenes and write conversational narration per scene (short sentences,
contractions, "Let's look at…"). For a short lesson, 4–6 scenes. For a full
lesson, follow `narration/full_lesson.py`'s structure (one data entry per
section + intro/summary/outro).

### Step 2 — Generate the voice + word timings
Copy `narration/make_narration.py` to a new generator (or extend it) with your
scene texts. It MUST use `edge_tts.Communicate(text, VOICE, rate=RATE,
boundary="WordBoundary")` and write, per scene:
- `public/audio/<scene>.mp3`
- `public/audio/<scene>.words.json`  (list of `{w,s,e}`)
Then copy the `*.words.json` into `src/captions/` (they're imported there).
Run it: `python narration/make_fives.py`

### Step 3 — Measure durations
Note each clip's length (ffprobe, or print it in the script). Scene durations in
Remotion = `ceil(seconds*30) + pad_frames`.

### Step 4 — Build the lesson component
Copy `src/lessons/EightWastes.tsx` to `src/lessons/FiveS.tsx`. For each scene:
- Build the visual (reuse `GlowCard`, icons, diagrams, characters).
- Place scenes on a timeline with `<Sequence from={..} durationInFrames={..}>`.
- Inside each Sequence add: the scene, `<Audio src={narr("<scene>.mp3")} />`, and
  the sentence captions (behind the `captions` prop).
- **No music and no SFX `<Audio>`.** Narration voice only.
- Insert **2 quiz blocks** (`QuizScene`) — one mid-lesson, one before the outro.
- Add `<BrandMark />` at the top level (after the scenes).
- Add the `captions` prop (default true) so a Dub variant can turn it off.
- Export `FIVES_DURATION` = total frames (include the 2 `quizDuration(...)`).

### Step 5 — Register it
In `src/Root.tsx` add two `<Composition>`s: `FiveS` and `FiveSDub`
(`defaultProps={{ captions: false }}`), same fps/width/height.

### Step 6 — Preview & verify
`npx remotion studio` to scrub, or render a still:
`npx remotion still FiveS out/fives_check.png --frame=120`
Check layout, caption sync, character placement.

### Step 7 — Render
`npx remotion render FiveS out/5s-lesson.mp4`
(and `FiveSDub` for the dub master).

### Step 8 — (If dubbing) export stems
Build voice-only and music+SFX-only stems aligned to the timeline (see
`DUB_WORKFLOW.md` for the ffmpeg pattern), so the voice can be swapped without
losing music.

---

## 5. Voice, captions, sound
- **Draft voice (for timing):** `en-US-ChristopherNeural`, `rate="-6%"`
  (edge-tts, `boundary="WordBoundary"`). Used to scout timing / previews.
- **Final voice = CLONED** (see §6). This is the standard.
- **Captions:** `Captions.tsx` shows the **whole active sentence**, no per-word
  highlight (word-highlight looks desynced on approximate timings). Caption
  timings are written per scene as `src/captions/<lesson>/<key>.words.json`.
- **Pure voice-only.** No background music and NO sound effects (no whoosh, no
  ding). The only audio is the narration. `make_music.py` / `make_sfx.py` still
  exist but are not used.

---

## 6. Voice = CLONE-ONLY pipeline (the reliable way)
Do NOT use the full Colab dub tool on the finished video. It transcribes and
re-times (guesses), which caused **repeated sentences** and **lost music**.
Instead:

1. **Draft the script** → `scripts.json` per lesson (`key` → narration text).
   The generators also voice it with edge-tts to scout scene timing. Then hand
   the user a copy named `<lesson>.json` to upload (course content stays OFF
   GitHub — only the engine code is in the repo).
2. **Clone on Colab (`colab_clone_voice.ipynb`)** — the user uploads their voice
   clip and their lesson `.json` file(s) (many at once = batch). The notebook
   loads the voice model once and speaks each scene in the uploaded voice. No
   Whisper, no Demucs, no video upload, no lessons pulled from GitHub. Outputs
   `clones/<lesson>/<key>.wav`, one folder per lesson, in `clones.zip`.
3. **Import the clips** → convert to `public/audio/<lesson>/<key>.mp3`, measure
   each one, and **rewrite `timings.json`** to the cloned durations so every
   page's audio fits its own scene (no drift, no repeats — structurally
   impossible to cross pages).
4. **Caption timings:** spread each scene's words evenly across its cloned clip
   duration → `src/captions/<lesson>/<key>.words.json` (captions are shown
   per-sentence, so this stays well-synced per page).
5. **Render** the normal (captioned) and `...Dub` (no-caption) compositions.

This gives: cloned voice, perfect per-page sync, no repeats, no music to lose.

---

## 6b. Quizzes (required: 2 per lesson)
Use `QuizScene` from `src/components/Quiz.tsx`. Each quiz: `{num, question,
options[], correct, explanation, think}`. It shows the question + options, a
`Think… N` countdown (give time to think), then highlights the correct option
and shows the explanation (with a soft `ding`). Insert as blocks in the
composition: **one mid-lesson, one just before the outro** (see how
`ZeroDefects.tsx` inserts `quiz("quiz1", …)` and `quiz("quiz2", …)`). Quiz
blocks have a fixed duration (`quizDuration(FPS, think)`), no narration.

---

## 7. Rendering options
- **Local:** `npx remotion render <Comp> out/x.mp4`
- **Colab (no good local GPU):** `colab_render.ipynb` — installs Node + Chromium
  libs, clones the repo, renders, downloads. Use `--gl=angle` (or `swangle`).

---

## 8. Gotchas (learned the hard way)
- `react-peeps` / `react-open-peeps` — **broken on React 19**. Use the custom SVG
  characters instead.
- edge-tts default boundary is **SentenceBoundary** → pass `boundary="WordBoundary"`
  or you get zero word timings.
- `tsconfig.json` has `resolveJsonModule: true` so JSON (timings/content/words)
  can be imported.
- Gradient/`useId` collisions: give per-character SVG gradients unique ids
  (`React.useId()`), already handled in `characters.tsx`.
- Keep characters off the bottom-center so they don't overlap captions.
- Don't commit `node_modules/` or `out/`.

---

## 9. Optional: photorealistic AI B-roll
Not the main style, but available: `AI_VIDEO_GUIDE.md` + `KLING_PROMPTS.md` +
`colab_ai_video.ipynb`. Costs money or needs a cloud GPU; text/data come out
wrong, so only use for background shots and overlay correct text with Remotion.
