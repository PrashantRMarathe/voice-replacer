"""Full 9-minute '8 Wastes' lesson: content + narration generation.

This is the single source of truth for the long lesson. It:
  1. Holds every scene's on-screen content AND spoken script.
  2. Generates one narration mp3 per scene with Edge TTS.
  3. Measures each clip and writes timings.json (seconds per scene) and
     content.json (on-screen text per scene) into src/lessons/full/ so the
     Remotion composition stays perfectly in sync with the real audio.

Run:  python course_video/narration/full_lesson.py
Swap the voice later by changing VOICE, or replace the mp3s with your cloned
voice and re-run only the measuring step.
"""
import asyncio
import json
import subprocess
from pathlib import Path

import edge_tts

VOICE = "en-US-ChristopherNeural"
RATE = "-6%"

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "public" / "audio" / "full"
DATA = ROOT / "src" / "lessons" / "full"
AUDIO.mkdir(parents=True, exist_ok=True)
DATA.mkdir(parents=True, exist_ok=True)

# Each waste: letter, name, icon key, one-line definition, a factory example,
# and a "how to fix" line. The narration expands these conversationally.
WASTES = [
    {
        "l": "D", "name": "Defects", "icon": "Defect",
        "def": "Any work that has errors and must be fixed or scrapped.",
        "example": "A welded part fails inspection and goes back for rework.",
        "fix": "Build quality in at the source with checks and poka-yoke.",
        "script": "The first waste is Defects. A defect is any product or piece of "
                  "work that contains an error, and now has to be reworked, repaired, "
                  "or thrown away. Imagine a welded part that fails inspection and has "
                  "to go all the way back down the line to be fixed. That's lost "
                  "material, lost time, and lost money. The lean answer is to build "
                  "quality in at the source, so mistakes are caught and prevented, "
                  "not discovered at the very end.",
    },
    {
        "l": "O", "name": "Overproduction", "icon": "Overproduction",
        "def": "Making more, or sooner, than the customer actually needs.",
        "example": "Running a big batch 'to be efficient' that then sits in storage.",
        "fix": "Produce to real demand using pull and takt time.",
        "script": "The second waste is Overproduction, and many experts call this the "
                  "worst waste of all, because it hides every other one. "
                  "Overproduction means making more than the customer needs, or making "
                  "it far too early. Picture a team running a huge batch just to look "
                  "efficient, when that stock simply sits in storage for weeks. The fix "
                  "is to produce only to real demand, using pull systems and takt time "
                  "so you make exactly what is needed, when it is needed.",
    },
    {
        "l": "W", "name": "Waiting", "icon": "Waiting",
        "def": "Idle time when people or products wait for the next step.",
        "example": "An operator standing idle because the previous machine is slow.",
        "fix": "Balance the line so work flows evenly between steps.",
        "script": "The third waste is Waiting. This is the idle time when people, "
                  "machines, or products are simply standing still, waiting for the "
                  "next step to happen. Think of an operator standing with nothing to "
                  "do because the machine before them is running slow. Every second of "
                  "waiting adds cost but adds no value. We reduce it by balancing the "
                  "line, so that work flows smoothly and evenly from one step to the "
                  "next.",
    },
    {
        "l": "N", "name": "Non-utilized talent", "icon": "Talent",
        "def": "Failing to use people's skills, ideas, and experience.",
        "example": "Ignoring the operator who knows exactly how to fix a recurring jam.",
        "fix": "Involve everyone in improvement; listen to the front line.",
        "script": "The fourth waste is Non-utilized talent. This is the waste of "
                  "people, and it is often invisible. It happens when we fail to use "
                  "the skills, the ideas, and the experience of our own team. The "
                  "operator on the floor often knows exactly why a machine keeps "
                  "jamming, but nobody ever asks them. Lean culture flips this. We "
                  "involve everyone in improvement, and we truly listen to the people "
                  "closest to the work.",
    },
    {
        "l": "T", "name": "Transportation", "icon": "Transport",
        "def": "Unnecessary movement of materials and products.",
        "example": "Carrying parts across the factory and back between steps.",
        "fix": "Place steps close together so products travel less.",
        "script": "The fifth waste is Transportation. This is the unnecessary movement "
                  "of materials and products from one place to another. Every time a "
                  "part is carried across the factory and then carried back again, "
                  "you add handling, risk of damage, and delay, but no value for the "
                  "customer. The solution is thoughtful layout. When we place steps "
                  "close together in the right order, products travel far less.",
    },
    {
        "l": "I", "name": "Inventory", "icon": "Inventory",
        "def": "Excess raw material, work-in-progress, or finished goods.",
        "example": "Shelves full of stock that ties up cash and hides problems.",
        "fix": "Keep only what you need; let inventory flow, not pile up.",
        "script": "The sixth waste is Inventory. This is excess, more raw material, "
                  "more work in progress, or more finished goods than you actually "
                  "need right now. Those full shelves might feel safe, but they tie "
                  "up cash, they take up space, and worst of all, they hide problems "
                  "like defects and poor flow. The goal is to keep only what you need, "
                  "and let inventory flow through the process rather than pile up.",
    },
    {
        "l": "M", "name": "Motion", "icon": "Motion",
        "def": "Unnecessary movement of people at the workstation.",
        "example": "Reaching, bending, and searching for tools every single cycle.",
        "fix": "Organize the workspace with 5S so everything is within reach.",
        "script": "The seventh waste is Motion. Be careful, because this is different "
                  "from transportation. Motion is the unnecessary movement of people, "
                  "right at the workstation. It is the reaching, the bending, and the "
                  "constant searching for a tool that should already be within reach. "
                  "Repeated thousands of times a day, this quietly drains energy and "
                  "time. We fix it by organizing the workspace, often with 5S, so "
                  "everything has a place and is easy to grab.",
    },
    {
        "l": "E", "name": "Extra processing", "icon": "Processing",
        "def": "Doing more work than the customer actually values.",
        "example": "Polishing a surface that will never be seen or used.",
        "fix": "Do exactly what the customer needs, no more, no less.",
        "script": "The eighth and final waste is Extra processing. This is doing more "
                  "work than the customer actually needs or values. A classic example "
                  "is polishing a surface to a mirror finish, when that surface will "
                  "be hidden inside the product and never seen. It is effort that "
                  "feels productive, but adds no real value. The lean principle is "
                  "simple. Do exactly what the customer needs. No more, and no less.",
    },
]

INTRO = (
    "Welcome to this lesson on the eight wastes of lean manufacturing. "
    "In lean thinking, waste is anything that uses up time, money, or effort "
    "without adding value for the customer. And the surprising truth is that in "
    "most processes, the vast majority of activity is actually waste. "
    "Over the next few minutes, we'll walk through all eight types, one by one, "
    "with clear examples you can recognize in your own workplace. "
    "To make them easy to remember, we use a single word. Downtime. "
    "Each letter stands for one of the eight wastes."
)

VALUE = (
    "Before we name the wastes, let's understand what waste really means. "
    "Every activity in your process falls into one of three buckets. "
    "The first is value-added work. This is work the customer is happy to pay "
    "for, because it changes the product into what they want. "
    "The second is necessary non-value work. The customer wouldn't pay for it, "
    "but right now you can't avoid it, like a required safety inspection. "
    "And the third bucket is pure waste. Work that adds no value, and could be "
    "removed today. Here is the eye-opening part. In a typical process, "
    "value-added work is often less than five percent of the total time. "
    "Everything else is waiting, moving, fixing, and storing. "
    "Lean is the discipline of seeing that hidden waste, and removing it."
)

MMM = (
    "You'll also hear lean experts talk about three enemies, three Japanese "
    "words. Muda, Mura, and Muri. Muda means waste, the eight types we're about "
    "to learn. Mura means unevenness, the peaks and troughs in your workload "
    "that create chaos. And Muri means overburden, pushing people and machines "
    "beyond their healthy limits. The eight wastes we focus on today are Muda. "
    "But keep in mind that uneven flow and overburden are usually what create "
    "that waste in the first place."
)

SUMMARY = (
    "So let's bring it all together. Downtime. "
    "Defects. Overproduction. Waiting. Non-utilized talent. "
    "Transportation. Inventory. Motion. And extra processing. "
    "Once you can see these eight wastes, you can't unsee them. "
    "You'll start spotting them everywhere, in every process you touch."
)

OUTRO = (
    "And that is the foundation of lean. Your mission as a lean thinker is "
    "simple to say, and powerful in practice. Learn to see the waste, and then "
    "work every day to remove it. In the next lesson, we'll put this into "
    "action with one of the most practical tools in lean. The five S system. "
    "I'll see you there."
)


# One practical "how to spot it on the floor" line per waste, appended to each
# section's narration to add depth (and length) without feeling like padding.
SPOT = {
    "D": "To spot it, look for rework areas, scrap bins, and inspection stations. "
         "Wherever work gets redone, defects are hiding.",
    "O": "To spot it, look for stock made 'just in case', and batches produced "
         "long before anyone ordered them.",
    "W": "To spot it, watch for people standing idle, or products sitting in a "
         "queue with nothing happening to them.",
    "N": "To spot it, ask whether the best ideas on the floor are actually being "
         "heard, or quietly ignored.",
    "T": "To spot it, follow a single part through the process and count how far "
         "it really travels.",
    "I": "To spot it, look for full shelves, overflowing bins, and aisles packed "
         "with work in progress.",
    "M": "To spot it, watch one operator for a few minutes and count the reaching, "
         "bending, and searching.",
    "E": "To spot it, ask of every step, would the customer pay extra for this? "
         "If not, question why you do it.",
}


def scenes():
    yield ("intro", INTRO)
    yield ("value", VALUE)
    yield ("mmm", MMM)
    for w in WASTES:
        yield (f"waste_{w['l']}", w["script"] + " " + SPOT[w["l"]])
    yield ("summary", SUMMARY)
    yield ("outro", OUTRO)


async def generate():
    for key, text in scenes():
        mp3 = AUDIO / f"{key}.mp3"
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(mp3))
        print("  voiced", key)


def measure():
    timings = {}
    for key, _ in scenes():
        mp3 = AUDIO / f"{key}.mp3"
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(mp3)],
            capture_output=True, text=True, check=True)
        timings[key] = round(float(out.stdout.strip()), 3)
    (DATA / "timings.json").write_text(json.dumps(timings, indent=2), encoding="utf-8")
    content = {
        "wastes": [{k: w[k] for k in ("l", "name", "icon", "def", "example", "fix")}
                   for w in WASTES],
    }
    (DATA / "content.json").write_text(json.dumps(content, indent=2), encoding="utf-8")
    total = sum(timings.values())
    print(f"timings.json + content.json written. Narration total ~ {total:.1f}s "
          f"({total/60:.1f} min)")


if __name__ == "__main__":
    asyncio.run(generate())
    measure()
