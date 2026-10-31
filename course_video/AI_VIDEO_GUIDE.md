# AI Factory Video — Colab Workflow

Make Flow/Veo-style realistic footage **for free**, on your own, using a Colab GPU.
Your PC has no NVIDIA GPU, so the heavy model runs on Google Colab (same as your
voice tool).

## What each side does
- **You:** run the Colab notebook, generate the clips, download `clips.zip`.
- **Claude:** stitch the clips + add your narration voice, music, correct text
  overlays (the 8 waste names/titles — because AI video spells text wrong),
  captions, transitions, and export the finished 1080p lesson.

## Steps
1. Upload **`colab_ai_video.ipynb`** to [Google Colab](https://colab.research.google.com).
2. In Colab: **Runtime → Change runtime type → GPU** (T4 works; L4/A100 = faster, nicer).
3. Run the cells top to bottom:
   - Cell 1: shows your GPU
   - Cell 2: installs libraries (~2–3 min)
   - Cell 3: loads the free **LTX-Video** model
   - Cell 4: the **prompt pack** (9 cinematic factory shots for the 8 Wastes) — edit if you like
   - Cell 5: generates all clips into `clips/` (~a few min each)
   - Cell 6: optional — generate one custom shot
   - Cell 7: zips + downloads `clips.zip`
4. Send me `clips.zip`. I assemble the final video.

## Honest expectations
- Each clip is **~5 seconds** → we stitch many together.
- Quality is **good but a step below** Google Flow/Veo.
- **Ignore any text the AI draws** — it's gibberish. I overlay the correct text.
- Free Colab (T4) works; if a clip runs out of memory, lower `num_frames` in Cell 5.
- Want higher quality later? On an A100 we can swap LTX-Video for **Wan 2.2** — same notebook structure.

## If you'd rather not run Colab
Tell me and I'll instead write a **Google Flow prompt pack** (paid, but highest
quality, zero setup) — same assembly step on my side afterwards.
