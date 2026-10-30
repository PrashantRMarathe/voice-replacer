"""Ishikawa Diagram lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Nikhil,
a quality engineer on a network switch line, using a fishbone to widen the
search for rising port-test failures, then proving two causes that coexisted
(worn test cables and a drifting press-fit height).

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/ishikawa.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py ishikawa  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "ik"
NAME = "ishikawa"

LETTERS = ["MES", "SOP", "PFMEA", "ESD"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. Ishikawa as spelled (ee-shee-KAH-wah,
# confirmed in Root Cause Analysis); Kaoru = "KAH-oh-roo".
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return re.sub(r"\bKaoru\b", "Kah-oh-roo", text)


INTRO_SCRIPT = (
    "Port-test failures on the switch line jumped six times in one week. The first meeting "
    "lasted two hours. It ended with one decision. Buy a new tester. Sound familiar? In this "
    "lesson, you'll learn the Ishikawa diagram, also called the fishbone. You'll see how to "
    "search for causes widely, then prove the real ones before you spend a rupee. We'll "
    "follow Nikhil, a quality engineer on a network switch line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Start with a sharp, measurable effect at the head. Search "
    "widely across the six M's, without blame. And treat every bone as a guess until evidence "
    "proves it. Here's your action for this week. Draw a fishbone for one recurring problem, "
    "and pick the three causes you'll test first. Great work completing this lesson. Next, "
    "you'll learn Jidoka."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What a Fishbone Is",
        "points": [("One problem at the head", "One problem sits"),
                   ("Possible causes on the bones", "possible causes"),
                   ("A team thinking tool", "It's a team tool")],
        "example": "Nikhil's problem: network switches failing the port-link test.",
        "example_cue": "Nikhil's problem",
        "script": "An Ishikawa diagram looks like the skeleton of a fish. One problem sits at the head. "
                  "All the possible causes branch off the bones, sorted into families. It's a team tool, "
                  "so everyone can see the whole search on one page. It stops you jumping to the first "
                  "idea. Nikhil's problem was network switches failing the port-link test. Where did "
                  "this tool come from?",
    },
    {
        "key": "p02", "num": 2, "title": "Origins, and Its Limits",
        "points": [("Kaoru Ishikawa, quality pioneer", "Kaoru Ishikawa"),
                   ("One of seven basic quality tools", "seven basic quality tools"),
                   ("Shows possible causes, proves nothing", "it doesn't prove")],
        "example": "Buying a new tester was a guess. The fishbone would make it one guess among many.",
        "example_cue": "Buying a new tester",
        "script": "It was made popular by Kaoru Ishikawa, a Japanese quality expert. It's one of the "
                  "seven basic quality tools. But here's the key thing. It shows possible causes, and it "
                  "doesn't prove any of them. Proof comes later, from observation, measurement and "
                  "trials. Buying a new tester was just a guess. The fishbone would make it one guess "
                  "among many. So what does the fish look like?",
    },
    {
        "key": "p03", "num": 3, "title": "Anatomy of the Fish",
        "points": [("Head: the effect", "The head is"),
                   ("Spine and major bones: cause families", "The spine links"),
                   ("Minor bones: specific causes", "Minor bones hold")],
        "example": "Write a cause as “suspected” until it's proven.",
        "example_cue": "Nikhil's rule",
        "script": "Read it from left to right. The head is the effect, the problem you want to solve. "
                  "The spine links everything to it. The major bones are cause families, like machine or "
                  "method. Minor bones hold specific possible causes, and smaller bones go deeper still. "
                  "Nikhil's rule was simple. Every cause is suspected, until it's proven. What goes in "
                  "the head?",
    },
    {
        "key": "p04", "num": 4, "title": "A Sharp Effect",
        "points": [("What, where, when, how much", "Say what is failing"),
                   ("A baseline and a denominator", "Add a baseline"),
                   ("One defect mode at a time", "Keep it to one")],
        "example": "“Port-link failures on switch Line 3 rose from 5 to 32 per 1,000 this week.”",
        "example_cue": "Nikhil wrote",
        "script": "A vague head gives you a vague fish. Quality is bad helps nobody. Say what is failing, "
                  "where, when, and how much. Add a baseline, and a clear denominator. Keep it to one "
                  "defect mode at a time. Nikhil wrote one sentence. Port-link failures on switch line "
                  "three rose from five to thirty-two per thousand this week. Can you see how much "
                  "sharper that is?",
    },
    {
        "key": "p05", "num": 5, "title": "The 6M: People, Machine, Method",
        "points": [("People: skill, workload, handover", "People covers"),
                   ("Machine: wear, settings, maintenance", "Machine covers"),
                   ("Method: sequence, SOP, changeover", "Method covers")],
        "example": "Use the families as prompts, not rigid boxes.",
        "example_cue": "Use them as prompts",
        "script": "Most teams use six families, called the six M's. People covers skill, training, "
                  "workload and handovers. Machine covers fixture wear, settings, maintenance and "
                  "software. Method covers the sequence, the SOP, changeovers and setup checks. For each family, ask your team one question. Could this explain our effect? Use them "
                  "as prompts, not rigid boxes. One cause can touch two families. And the other three "
                  "M's?",
    },
    {
        "key": "p06", "num": 6, "title": "Material, Measurement, Environment",
        "points": [("Material: supplier, lot, handling", "Material covers"),
                   ("Measurement: gauges, test limits, false rejects", "Measurement covers"),
                   ("Environment: ESD, humidity, dust, heat", "Environment covers")],
        "example": "Measurement is the one teams forget. Is the tester itself telling the truth?",
        "example_cue": "Measurement is the one",
        "script": "Material covers supplier variation, the wrong lot, and damage in handling. Measurement "
                  "covers gauges, test limits, calibration and false rejects. Environment covers ESD, "
                  "humidity, dust, light and heat. Measurement is the one teams forget most. Is the "
                  "tester itself telling you the truth? Keep that question in mind. A worn test fixture can fail good units all day long. Before you draw, "
                  "what should you collect?",
    },
    {
        "key": "p07", "num": 7, "title": "Collect Evidence First",
        "points": [("A Pareto of defect types", "a Pareto"),
                   ("Split by shift, lot, station, tester", "Split the data"),
                   ("Compare good units with bad", "Compare good units")],
        "example": "Failures clustered on two of the four test stations.",
        "example_cue": "Nikhil's first split",
        "script": "Bring some data into the room. Start with a Pareto of defect types, so you work on "
                  "the biggest one. Split the data by shift, lot, station and tester. Compare good units "
                  "with bad ones, side by side. Nikhil's first split was a surprise. Most failures came "
                  "from just two of the four test stations. What would you suspect, from that alone?",
    },
    {
        "key": "p08", "num": 8, "title": "Build It: Eight Steps",
        "points": [("Define the effect, gather the team", "Define the effect"),
                   ("Draw the bones, brainstorm, no blame", "Draw the head"),
                   ("Ask why, merge, prioritize", "Ask why could this"),
                   ("Assign owners to test causes", "Assign an owner")],
        "example": "Nikhil's team: production, quality, test, maintenance and stores.",
        "example_cue": "Nikhil's team",
        "script": "Build it in eight steps. Define the effect, and gather a cross-functional team. Draw "
                  "the head, the spine and the families. Brainstorm causes with no debate and no blame. "
                  "Ask why could this happen, to go deeper. Merge duplicates, and prioritize with data. "
                  "Assign an owner to test each cause. Nikhil's team mixed production, quality, test, "
                  "maintenance and stores. Why include stores?",
    },
    {
        "key": "p09", "num": 9, "title": "Nikhil's Fishbone",
        "points": [("Machine: press-fit height drift", "Machine had"),
                   ("Measurement: worn test cables", "Measurement had"),
                   ("Material, method, people, environment", "Other bones")],
        "example": "Twenty-three possible causes in forty minutes.",
        "example_cue": "In forty minutes",
        "script": "Because material problems often start in stores. Here's what the team found. Machine "
                  "had a press-fit tool whose stop height might drift. Measurement had loopback test "
                  "cables, plugged in thousands of times. Other bones held a new port supplier lot, a "
                  "missing engagement check, a temporary crew and ESD records. In forty minutes, they "
                  "had twenty-three possible causes. Which do you test first?",
    },
    {
        "key": "p10", "num": 10, "title": "Fishbone, Then Five Whys",
        "points": [("Fishbone goes wide", "The fishbone goes wide"),
                   ("Five whys goes deep", "Five whys goes deep"),
                   ("Never stop at operator error", "never stop")],
        "example": "Why worn cables? No change limit. Why? Cables weren't in the maintenance plan.",
        "example_cue": "Take the test cables",
        "script": "Use two tools together. The fishbone goes wide, to find candidates. Five whys goes "
                  "deep, down one chosen path. Take the test cables. Why were they worn? Nobody replaced "
                  "them. Why? They weren't in any maintenance plan. And never stop at operator error. "
                  "Ask what made the error possible. But a convincing chain still isn't proof. How do "
                  "you prove a cause?",
    },
    {
        "key": "p11", "num": 11, "title": "Prove It: The Evidence Ladder",
        "points": [("Observe it at the gemba", "Observe the condition"),
                   ("Trace and measure", "Trace failures"),
                   ("Experiment, then replicate", "Run a controlled")],
        "example": "Votes don't count. A single good trial isn't proof either.",
        "example_cue": "Votes don't count",
        "script": "Climb an evidence ladder. Observe the condition at the gemba. Trace failures to lots, "
                  "shifts, stations and equipment. Measure with calibrated tools. Run a controlled "
                  "experiment, changing one factor at a time. Then replicate it, to show the effect "
                  "really goes away. Votes don't count as evidence. And a single good trial isn't proof "
                  "either. So what did Nikhil prove?",
    },
    {
        "key": "p12", "num": 12, "title": "Two Causes, Both Real",
        "points": [("Worn cables: false failures", "New cables cut"),
                   ("Press height drift: real failures", "the press-fit stop"),
                   ("Causes can coexist", "Two causes")],
        "example": "Retest with new cables: 6 of 10 'failed' switches passed. The other 4 had shallow ports.",
        "example_cue": "He retested",
        "script": "He retested ten failed switches, with brand new cables. Six of them passed. New cables "
                  "cut the false failures straight away. The other four really failed. Their ports sat "
                  "shallow, because the press-fit stop had drifted. Two causes, both real, at the same "
                  "time. That happens more often than you'd think. Fixing only one would leave half the problem. A new tester would have fixed neither. So what actions would you take?",
    },
    {
        "key": "p13", "num": 13, "title": "Strong Corrective Actions",
        "points": [("Design it out before retraining", "Design the cause out"),
                   ("Locks, interlocks, counters", "Use locks"),
                   ("Update SOP, PFMEA, control plan", "update the SOP")],
        "example": "Cable insertion counter with a change limit. Press height check and lock at every shift start.",
        "example_cue": "Nikhil's team added",
        "script": "Design the cause out, before you rely on reminders or retraining. Use locks, "
                  "interlocks, counters and fixtures. Then update the SOP, the PFMEA, the control plan "
                  "and the training, together. Nikhil's team added an insertion counter to every test "
                  "cable, with a change limit. And the press height was checked and locked at every "
                  "shift start. How would you know it worked?",
    },
    {
        "key": "p14", "num": 14, "title": "Prove It Worked",
        "points": [("Set the target before you start", "Set your target"),
                   ("A fixed window and sample size", "a fixed window"),
                   ("32 → 4 per 1,000, held for 30 days", "Failures fell")],
        "example": "Zero false failures from worn cables, over 30 production days.",
        "example_cue": "And not one",
        "script": "Set your target before the change, not after you see the results. Decide a fixed "
                  "window and a sample size. Nikhil chose thirty production days. He also challenged the counter with a worn cable, to prove it blocked use. Failures fell from "
                  "thirty-two per thousand to four, and stayed there. And not one false failure came from "
                  "a worn cable. The tester budget went back into the drawer. What mistakes should you "
                  "avoid?",
    },
    {
        "key": "p15", "num": 15, "title": "Mistakes and Best Practices",
        "points": [("Vague effects and mixed defects", "A vague effect"),
                   ("Missing functions in the room", "Leaving out"),
                   ("No validation after the session", "Stopping after")],
        "example": "Keep rejected causes on the chart, with the evidence that ruled them out.",
        "example_cue": "Keep rejected causes",
        "script": "Watch for a few mistakes. A vague effect, or several defects mixed together. Leaving "
                  "out maintenance, test or stores. Writing operator carelessness instead of looking at "
                  "the system. Stopping after the brainstorm, with no tests and no owners. Keep rejected "
                  "causes on the chart, with the evidence that ruled them out. Your next team will thank "
                  "you. Which mistake have you seen?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Possible causes", "icon": "search", "with": 1},
        {"label": "Cause families", "icon": "stack", "with": 1},
        {"label": "The problem", "sub": "At the head", "icon": "warning", "tone": "bad", "with": 0}]},
    "p02": {"type": "versus", "items": [
        {"label": "Proof", "sub": "Not from the fishbone", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Possible causes", "sub": "What it shows", "icon": "search", "tone": "good", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Head", "sub": "The effect", "icon": "warning", "with": 0},
        {"label": "Major bones", "sub": "Cause families", "icon": "stack", "with": 1},
        {"label": "Minor bones", "sub": "Specific causes", "icon": "search", "with": 2}]},
    "p04": {"type": "versus", "items": [
        {"label": "“Quality is bad”", "sub": "Vague", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "5 → 32 per 1,000", "sub": "Line 3, port-link, this week", "icon": "check", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "People", "icon": "person", "with": 0},
        {"label": "Machine", "icon": "gear", "with": 1},
        {"label": "Method", "icon": "clipboard", "with": 2}]},
    "p06": {"type": "icons", "items": [
        {"label": "Material", "icon": "box", "with": 0},
        {"label": "Measurement", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Environment", "icon": "wave", "with": 2}]},
    "p07": {"type": "bars", "label": "", "note": "Port-link failures by test station", "with": "example", "items": [
        {"label": "T1", "value": 14, "tone": "bad", "with": "example"},
        {"label": "T2", "value": 3, "with": "example"},
        {"label": "T3", "value": 12, "tone": "bad", "with": "example"},
        {"label": "T4", "value": 3, "with": "example"}]},
    "p08": {"type": "steps", "items": [
        {"label": "Define, team", "with": 0}, {"label": "Draw, brainstorm", "with": 1},
        {"label": "Why? Merge, rank", "with": 2}, {"label": "Owners test", "with": 3}]},
    "p09": {"type": "icons", "items": [
        {"label": "Machine", "sub": "Press height drift", "icon": "gear", "with": 0},
        {"label": "Measurement", "sub": "Worn test cables", "icon": "scale", "with": 1},
        {"label": "Material", "sub": "New port lot", "icon": "box", "with": 2},
        {"label": "Method", "sub": "No engagement check", "icon": "clipboard", "with": 2},
        {"label": "People", "sub": "Temporary crew", "icon": "person", "with": 2},
        {"label": "Environment", "sub": "ESD records", "icon": "wave", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "search", "label": "possible causes in 40 minutes",
                 "unit": "every one still a guess", "with": "example"}},
    "p10": {"type": "steps", "items": [
        {"label": "Cables worn", "with": "example"},
        {"label": "Never replaced", "with": "example"},
        {"label": "Not in the maintenance plan", "with": "example"}]},
    "p11": {"type": "ladder", "top": "STRONGEST", "bottom": "WEAKEST", "items": [
        {"label": "Replicate", "icon": "check", "with": 2},
        {"label": "Experiment", "icon": "test", "with": 2},
        {"label": "Trace and measure", "icon": "scale", "with": 1},
        {"label": "Observe", "icon": "search", "with": 0}]},
    "p12": {"type": "bars", "label": "", "note": "10 failed switches retested with new cables: 6 passed, 4 had shallow ports", "with": "example", "items": [
        {"label": "False fails", "value": 6, "with": "example"},
        {"label": "Real fails", "value": 4, "tone": "bad", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Cable insertion counter", "icon": "count", "with": "example"},
        {"label": "Press height lock", "icon": "lock", "with": "example"},
        {"label": "SOP, PFMEA, control plan", "icon": "clipboard", "tone": "good", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Before", "value": 32}, "after": {"label": "After", "value": 4},
            "unit": "port-link failures per 1,000 switches", "note": "Held for 30 production days", "with": 2},
    "p15": {"type": "icons", "items": [
        {"label": "Vague effect", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Missing functions", "icon": "person", "tone": "bad", "with": 1},
        {"label": "No validation", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Keep rejected causes", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which is the best effect to put at the head of a fishbone?",
        "options": ["“Quality problems on the switch line”",
                    "“Port-link failures on Line 3 rose from 5 to 32 per 1,000 this week”",
                    "“The tester is bad”"],
        "correct": 1,
        "explanation": "A good head names one defect, the place, the period and the size, with a baseline. “The tester is bad” is already a cause.",
        "q_script": "Quick check. Which of these is the best effect to put at the head of a fishbone? "
                    "Take a few seconds.",
        "a_script": "It's the second one. It names one defect, the place, the period and the size. The "
                    "last one is already a cause.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "After brainstorming, the team votes “operator carelessness” as the top cause. What next?",
        "options": ["Retrain the operators: the team agreed",
                    "Ask what made the error possible, and test causes with evidence",
                    "Add a warning sign at the station"],
        "correct": 1,
        "explanation": "A vote isn't evidence, and carelessness isn't a controllable cause. Ask which process condition made the error possible, then prove it.",
        "q_script": "One more, and this one's a scenario. After brainstorming, the team votes operator "
                    "carelessness as the top cause. What should happen next? Have a think.",
        "a_script": "Ask what made the error possible, and test each cause with evidence. A vote isn't "
                    "proof, and carelessness isn't a cause you can control.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
