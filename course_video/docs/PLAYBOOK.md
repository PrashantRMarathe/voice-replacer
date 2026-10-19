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
- Inside each Sequence add: the scene, `<Audio src={narr("<scene>.mp3")} />`,
  `<Audio src={sfx("whoosh")} />`, and `{Cap(words)}` (captions toggle).
- Add `<Audio src={narr("music.mp3")} volume={0.16} loop />` at the top.
- Add the `captions` prop (default true) so a Dub variant can turn it off.
- Export `FIVES_DURATION` = total frames.

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

## 5. Voice, captions, music, SFX
- **Voice:** `en-US-ChristopherNeural`, `rate="-6%"` (edge-tts). Change `VOICE`
  for a different narrator. Good alternates: `en-IN-NeerjaNeural` (Indian female),
  `en-IN-PrabhatNeural` (Indian male), `en-US-AriaNeural`.
- **Captions:** generated from word timings; `Captions.tsx` highlights the active
  word. If you change the voice, regenerate word timings so captions stay in sync.
- **Music/SFX:** regenerate with `make_music.py` / `make_sfx.py` (numpy,
  royalty-free — no license risk). Keep music quiet.

---

## 6. Changing / cloning the voice (dubbing)
Two ways:
1. **Simplest swap:** change `VOICE` in the generator, regenerate, re-render.
2. **Cloned voice:** dub the **voice stem** (`narration.wav`), not the mixed
   video — then mix the new voice with the music+SFX stem and mux onto the
   no-caption video. Full steps in `DUB_WORKFLOW.md`.
   ⚠️ If you dub the whole mixed video with the Colab dub tool, its Demucs step
   can DROP the quiet music. Fix: layer the music stem back under the result
   (ffmpeg `amix`). Prefer dubbing the stem to avoid this.

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
