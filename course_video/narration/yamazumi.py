"""Yamazumi lesson DATA: 15 pages + 2 quizzes + intro/outro.

Written to the script style guide (docs/PLAYBOOK.md section 4b). Story thread:
Meera's four-operator set-top box cell.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/yamazumi.py                     voice MISSING clips (bootstrap)
  python narration/import_clones.py yamazumi   import the cloned voice
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "yz"
NAME = "yamazumi"

INTRO_SCRIPT = (
    "Every afternoon, Meera's set-top box cell falls behind. Three operators wait, "
    "while one is buried in screws. Nobody is lazy. The work is just stacked unevenly. "
    "In this lesson, you'll learn Yamazumi, a simple chart that shows exactly where "
    "work piles up. And you'll see how Meera rebalances her line with real data."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Measure the real work, not the best case. Stack "
    "it against TAKT to see where it piles up. And rebalance with care, never at the "
    "cost of safety or quality. Your action this week: time one station on your line, "
    "and draw its bar against TAKT. Great work completing this lesson. Next, you'll learn "
    "Zero Defects, the last lesson of the course."
)

# One story thread: Meera's four-operator set-top box cell, TAKT 30 s,
# stations A=22, B=35, C=27, D=20 s (104 s of work) -> rebalanced B=30, D=25.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Yamazumi Is",
        "points": [("A stacked bar chart of work per station", "It's a stacked bar chart"),
                   ("Japanese: 'piling up'", "The Japanese word means"),
                   ("Each bar: one operator's tasks", "Each bar stacks"),
                   ("Above the TAKT line = can't keep up", "Any bar above")],
        "example": "Meera's set-top box cell: four operators, four stacked bars, one TAKT line.",
        "example_cue": "Here's Meera's cell",
        "script": "So what is Yamazumi? It's a stacked bar chart of the work at each station. "
                  "The Japanese word means piling up. Each bar stacks one operator's tasks, in "
                  "seconds. A horizontal line marks TAKT time, the pace your customer needs. Any "
                  "bar above that line can't keep up. It turns your time studies into a balancing "
                  "conversation. Here's Meera's cell, with four operators. Can you spot the "
                  "problem already?",
    },
    {
        "key": "p02", "num": 2, "title": "Purpose & Benefits",
        "points": [("Imbalance, waiting, overload at a glance", "You see imbalance"),
                   ("Objective basis for staffing", "It gives you an objective"),
                   ("Shows where cross-training helps", "It also shows where"),
                   ("Never replaces engineering checks", "But Yamazumi never replaces")],
        "example": "One operator waits while another fights a long screw-fastening job — moving one small task could smooth the flow.",
        "example_cue": "In Meera's cell",
        "script": "Why bother? Because the chart makes problems visible. You see imbalance, "
                  "waiting and overload at a glance. It gives you an objective basis for staffing, "
                  "not gut feel. It also shows where cross-training would help. In Meera's cell, "
                  "one operator waits while another fights a long screw-fastening job. Moving one "
                  "small task could smooth the flow. But Yamazumi never replaces engineering "
                  "checks. First, you need three key times.",
    },
    {
        "key": "p03", "num": 3, "title": "TAKT, Cycle & Work Content",
        "points": [("TAKT: net time ÷ good units needed", "It's your net available time"),
                   ("Cycle time: how often a unit leaves", "Cycle time is"),
                   ("Work content: sum of manual tasks", "Work content is"),
                   ("Keep machine time separate", "Keep machine time separate")],
        "example": "420 net minutes ÷ 840 units = TAKT of 30 seconds. Station B needs 35.",
        "example_cue": "Meera has four hundred",
        "script": "First, TAKT time. It's your net available time divided by the good units the "
                  "customer needs. Cycle time is how often a unit actually leaves a station. Work "
                  "content is the sum of manual tasks on one unit. Keep machine time separate. "
                  "Meera has four hundred and twenty net minutes. Demand is eight hundred and forty "
                  "units. That's a TAKT of thirty seconds. Her Station B needs thirty-five. Can it "
                  "keep up alone?",
    },
    {
        "key": "p04", "num": 4, "title": "Chart Structure",
        "points": [("One bar per operator or station", "You draw one vertical bar"),
                   ("Seconds up the side, TAKT line across", "The vertical axis"),
                   ("Each block = a task, in order", "Each colored block"),
                   ("Colors show task types, not scores", "Colors show task types")],
        "example": "Station A stacks to 22 seconds; Station B reaches 35, well above the line.",
        "example_cue": "In Meera's chart",
        "script": "Now, let's build the chart. You draw one vertical bar per operator or station. "
                  "The vertical axis shows seconds. A horizontal line marks TAKT. Each colored "
                  "block is a task, stacked in standard-work order. Colors show task types, never "
                  "performance scores. Label every bar with its sample and shift. In Meera's chart, "
                  "Station A stacks to twenty-two seconds. Station B reaches thirty-five, well above "
                  "the line. So where do these numbers come from?",
    },
    {
        "key": "p05", "num": 5, "title": "Reliable Time Study",
        "points": [("Define where each task starts and ends", "Define where each task"),
                   ("Many cycles, across shifts", "Observe many cycles"),
                   ("Capture walking, stops, changeovers", "Capture walking"),
                   ("Separate machine from manual time", "Separate machine time")],
        "example": "Firmware flashing runs while the operator fastens screws, so Meera times each element separately.",
        "example_cue": "In Meera's cell",
        "script": "They come from real observation at the Gemba. Your chart is only as good as its "
                  "data. Define where each task starts and ends. Observe many cycles, across "
                  "shifts, not just the fastest one. Capture walking, minor stops and changeovers "
                  "too. Separate machine time from manual handling. In Meera's cell, firmware "
                  "flashing runs while the operator fastens screws. So she times each element "
                  "separately. What kinds of work will you find?",
    },
    {
        "key": "p06", "num": 6, "title": "Classifying the Work",
        "points": [("Value-added: what the customer wants", "Value-added work changes"),
                   ("Necessary non-value-added: checks, traceability", "Necessary non-value-added"),
                   ("Waste: searching, walking, waiting", "Waste is searching"),
                   ("ECRS — but keep quality & safety checks", "Challenge every step")],
        "example": "Meera's operator walks 5 seconds to fetch screws. Point-of-use bins remove that waste.",
        "example_cue": "Meera's operator walks",
        "script": "You'll find three kinds of work. Value-added work changes the product the way "
                  "the customer wants. Necessary non-value-added work covers required checks and "
                  "traceability. Waste is searching, walking and waiting. Challenge every step "
                  "with E-C-R-S: eliminate, combine, rearrange, simplify. But never remove a "
                  "required quality or safety check. Meera's operator walks five seconds to fetch "
                  "screws. Point-of-use bins remove that waste. Now you can map the current state.",
    },
    {
        "key": "p07", "num": 7, "title": "Building Current State",
        "points": [("Approved demand → TAKT", "Start with approved demand"),
                   ("One bar per station, TAKT line drawn", "Build one bar per station"),
                   ("Check the chart against reality", "Then walk the floor"),
                   ("A short bar ≠ spare capacity", "a short bar doesn't prove")],
        "example": "TAKT 30 s: A = 22, B = 35, C = 27, D = 20. B is 5 seconds over — the first priority.",
        "example_cue": "Here's Meera's current state",
        "script": "Start with approved demand, and calculate TAKT. Build one bar per station, "
                  "stack each task, and draw the TAKT line. Then walk the floor and check the "
                  "chart against reality. Here's Meera's current state. Station A runs twenty-two "
                  "seconds, and B runs thirty-five. C runs twenty-seven, and D runs twenty. "
                  "Station B is five seconds over TAKT. That's her first priority. And remember, "
                  "a short bar doesn't prove you have spare capacity.",
    },
    {
        "key": "p08", "num": 8, "title": "Line Balancing",
        "points": [("Move tasks or improve methods", "Balancing means moving"),
                   ("Not perfectly equal bars", "The goal isn't perfectly equal"),
                   ("Respect layout, sequence, skills, checks", "You must respect layout"),
                   ("Try ECRS before adding people", "Try E-C-R-S")],
        "example": "A 5-second labeling task moves from B to D: B = 30, D = 25. Then pilot and re-measure.",
        "example_cue": "Meera finds a five-second",
        "script": "Balancing means moving feasible tasks, or improving methods, so every station "
                  "can hold the pace. The goal isn't perfectly equal bars. You must respect "
                  "layout, task sequence, fixtures, skills and quality checks. Try E-C-R-S before "
                  "you add people. Meera finds a five-second labeling task that doesn't depend on "
                  "B's other work. She moves it to Station D. B drops to thirty, and D rises to "
                  "twenty-five. Then she pilots and re-measures.",
    },
    {
        "key": "p09", "num": 9, "title": "Manpower & Efficiency",
        "points": [("Manual work ÷ TAKT, round up", "Add up the manual work"),
                   ("Balance efficiency: work vs capacity", "Balance efficiency compares"),
                   ("A planning floor, not a promise", "Treat this as a planning floor"),
                   ("Prove output before cutting people", "Never cut operators")],
        "example": "104 seconds of work at a 30-second TAKT = 4 operators; efficiency about 87%.",
        "example_cue": "Meera's cell has one hundred",
        "script": "How many people do you really need? Add up the manual work, divide by TAKT, "
                  "and round up. Meera's cell has one hundred and four seconds of work. At a "
                  "thirty-second TAKT, that's four operators. Balance efficiency compares the "
                  "assigned work with the staffed capacity. Hers is about eighty-seven percent. "
                  "Treat this as a planning floor, not a promise. Never cut operators before good "
                  "output is proven, safely and consistently.",
    },
    {
        "key": "p10", "num": 10, "title": "Bottlenecks & Machines",
        "points": [("Not every long bar is an operator bottleneck", "Not every long bar"),
                   ("Shared machines need their own check", "Machines can run"),
                   ("Split manual, automatic, loading, waiting", "Split manual time"),
                   ("Adjust for uptime, changeovers, yield", "Then adjust for uptime")],
        "example": "Two audio testers: 160 units/hour on paper — about 140 good ones in reality.",
        "example_cue": "Look at the audio line's",
        "script": "Here's a common mistake. Not every long bar is an operator bottleneck. Machines "
                  "can run while people work, so shared equipment needs its own capacity check. "
                  "Split manual time, automatic cycle, loading and waiting. Then adjust for uptime, "
                  "changeovers and first-pass yield. Look at the audio line's two testers on screen. "
                  "On paper, they handle a hundred and sixty units an hour. In reality, it's about "
                  "one hundred and forty good ones. Would you have planned for that?",
    },
    {
        "key": "p11", "num": 11, "title": "Mixed-Model Lines",
        "points": [("One chart can hide trouble", "Then one chart can hide"),
                   ("Model-specific bars, worst case", "So use model-specific bars"),
                   ("Flexible, qualified staff", "Plan flexible, qualified staff"),
                   ("Heijunka and SMED smooth the mix", "And use Heijunka")],
        "example": "Averages 27 s across the mix, but 42 s on the audio model — a long batch piles up work fast.",
        "example_cue": "A station might average",
        "script": "What if your line builds several models? Then one chart can hide trouble. A "
                  "station might average twenty-seven seconds across the mix. But on the audio "
                  "model, it needs forty-two. Run a long batch of that model, and work piles up "
                  "fast. So use model-specific bars, and check the worst case. Plan flexible, "
                  "qualified staff. And use Heijunka and S-M-E-D to smooth the mix. So how do you "
                  "know a new balance really worked?",
    },
    {
        "key": "p12", "num": 12, "title": "KPIs & Verification",
        "points": [("A balanced chart is a hypothesis", "A balanced chart is only"),
                   ("Leading: standard-work adherence", "Watch leading measures"),
                   ("Lagging: good output, defects, UPPH", "Watch lagging ones"),
                   ("Check ergonomics with operators", "check ergonomics")],
        "example": "Plan attainment counts good units against the plan; first-pass yield counts units passing first time.",
        "example_cue": "Plan attainment counts",
        "script": "A balanced chart is only a hypothesis. You prove it with results. Watch leading "
                  "measures, like standard-work adherence. Watch lagging ones, like good output, "
                  "defects and units per person-hour. Keep your definitions consistent. On screen, "
                  "two measures look alike but mean different things. Plan attainment counts good "
                  "units against the plan. First-pass yield counts units that pass the first time. "
                  "And after any change, check ergonomics with your operators.",
    },
    {
        "key": "p13", "num": 13, "title": "Case: Set-Top Box Cell",
        "points": [("Before: B capped output near 103/hour", "Before, Station B capped"),
                   ("After: B down to 30 seconds", "After the pilot"),
                   ("About 116 good/hour vs 120 theoretical", "Output rose"),
                   ("Done only after two stable weeks", "She only called it done")],
        "example": "Short of 120 is normal: uptime and yield always cost something.",
        "example_cue": "And that's normal",
        "script": "Let's see how Meera's change played out. Before, Station B capped the cell near "
                  "one hundred and three units an hour. After the pilot, Station B dropped to "
                  "thirty seconds. Output rose to about one hundred and sixteen good units an "
                  "hour. That's short of the theoretical one hundred and twenty. And that's normal, "
                  "because uptime and yield always cost something. She only called it done after "
                  "two stable weeks. What would you check next?",
    },
    {
        "key": "p14", "num": 14, "title": "Do's & Don'ts",
        "points": [("Measure real work, keep data current", "Measure real work"),
                   ("Involve operators, Quality, Engineering", "Involve operators"),
                   ("Protect safety, ESD, testing, traceability", "Protect safety"),
                   ("No best-case times, no headcount cutting", "Don't use best-case")],
        "example": "Removing a barcode check looks like 6 seconds saved. It's not a balance — it's a traceability risk.",
        "example_cue": "Removing a barcode check",
        "script": "A few hard rules. Measure real work, and keep your data current. Involve "
                  "operators, Quality and Engineering. Protect safety, E-S-D, testing and "
                  "traceability. Don't use best-case cycle times. And don't turn Yamazumi into a "
                  "headcount-cutting tool, or people stop sharing real data. Here's a trap. "
                  "Removing a barcode check looks like six seconds saved. It's not a balance. It's "
                  "a traceability risk. Would your team spot it?",
    },
    {
        "key": "p15", "num": 15, "title": "90-Day Roadmap",
        "points": [("Days 1–30: pilot line, time studies, baseline", "In the first thirty days"),
                   ("Days 31–60: ECRS, rebalance, qualify", "In the next thirty"),
                   ("Days 61–90: verify, update SOPs, expand", "In the last thirty"),
                   ("Keep charts current", "Then keep your charts current")],
        "example": "An out-of-date chart is worse than no chart at all.",
        "example_cue": "An out-of-date chart",
        "script": "Ready to start? Here's a ninety-day plan. In the first thirty days, pick one "
                  "pilot line, collect demand and time studies, and build baseline charts. In the "
                  "next thirty, run E-C-R-S workshops, rebalance and qualify operators. In the last "
                  "thirty, verify yield and output, update the S-O-Ps, and expand to similar lines. "
                  "Then keep your charts current whenever demand, mix or staffing changes. An "
                  "out-of-date chart is worse than no chart at all.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example". Station bars use the
# current state from p07 (TAKT 30 s).
CURRENT = [("A", 22, None), ("B", 35, "bad"), ("C", 27, None), ("D", 20, None)]


def takt_bars(stations, note, unit, with_="example"):
    return {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": note, "unit": unit,
            "with": with_, "items": [{"label": f"Station {s}", "value": v, "tone": t, "with": with_}
                                     for s, v, t in stations]}


VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Stacked bars", "icon": "stack", "with": 0},
        {"label": "'Piling up'", "icon": "box", "with": 1},
        {"label": "One operator's tasks", "icon": "person", "with": 2},
        {"label": "Above TAKT: can't keep up", "icon": "warning", "tone": "bad", "with": 3}],
        "then": takt_bars(CURRENT, "B can't keep up", "Meera's cell: seconds of work per station")},
    "p02": {"type": "icons", "items": [
        {"label": "Imbalance at a glance", "icon": "search", "with": 0},
        {"label": "Staffing on facts", "icon": "person", "with": 1},
        {"label": "Where to cross-train", "icon": "sequence", "with": 2},
        {"label": "Engineering checks still needed", "icon": "wrench", "tone": "bad", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Long screw job", "sub": "Overloaded", "icon": "screw", "with": "example"},
            {"label": "Move one small task", "sub": "Smoother flow", "icon": "sequence", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "Net time ÷ good units", "icon": "clock", "with": 0},
        {"label": "Cycle time", "sub": "How often one leaves", "icon": "sequence", "with": 1},
        {"label": "Work content", "sub": "Sum of manual tasks", "icon": "hand", "with": 2},
        {"label": "Machine time", "sub": "Kept separate", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "clock", "label": "TAKT time",
                 "unit": "420 net minutes ÷ 840 units", "with": "example"}},
    "p04": takt_bars([("A", 22, None), ("B", 35, "bad")], "B is above the line",
                     "One bar per station, TAKT line across", with_=0),
    "p05": {"type": "flow", "items": [
        {"label": "Define start and end", "icon": "pin", "with": 0},
        {"label": "Many cycles, every shift", "icon": "clock", "with": 1},
        {"label": "Walking, stops, changeovers", "icon": "walk", "with": 2},
        {"label": "Machine apart from manual", "icon": "gear", "tone": "good", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Value-added", "icon": "check", "tone": "good", "with": 0},
        {"label": "Necessary: checks, traceability", "icon": "shield", "with": 1},
        {"label": "Waste: search, walk, wait", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "ECRS, keep the checks", "icon": "wrench", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Walk 5 s to fetch screws", "sub": "Waste", "icon": "walk", "with": "example"},
            {"label": "Point-of-use bins", "sub": "Walk removed", "icon": "tray", "with": "example"}]}},
    "p07": takt_bars(CURRENT, "B is 5 s over: first priority", "Meera's current state"),
    "p08": {"type": "icons", "items": [
        {"label": "Move tasks, improve methods", "icon": "sequence", "with": 0},
        {"label": "Not perfectly equal", "icon": "scale", "with": 1},
        {"label": "Layout, sequence, skills, checks", "icon": "clipboard", "with": 2},
        {"label": "ECRS before people", "icon": "person", "with": 3}],
        "then": takt_bars([("A", 22, None), ("B", 30, "good"), ("C", 27, None), ("D", 25, None)],
                          "5 s labeling moved B → D", "After the move: pilot, then re-measure")},
    "p09": {"type": "stat", "value": 4, "suffix": " operators", "icon": "person", "label": "104 s of work ÷ 30 s TAKT, rounded up",
            "unit": "Balance efficiency about 87%", "with": "example"},
    "p10": {"type": "icons", "items": [
        {"label": "Long bar ≠ operator problem", "icon": "person", "with": 0},
        {"label": "Shared machines", "icon": "gear", "with": 1},
        {"label": "Manual · auto · load · wait", "icon": "clock", "with": 2},
        {"label": "Uptime, changeovers, yield", "icon": "chartDown", "with": 3}],
        "then": {"type": "compare", "before": {"label": "On paper", "value": 160}, "after": {"label": "Good, real", "value": 140},
                 "unit": "units an hour, two audio testers", "note": "Plan for the real number", "with": "example"}},
    "p11": {"type": "bars", "label": "TAKT", "value": 30, "suffix": " s", "note": "The average hides it",
            "unit": "One station, seconds per unit", "with": "example", "items": [
        {"label": "Mix average", "value": 27, "with": "example"},
        {"label": "Audio model", "value": 42, "tone": "bad", "with": "example"}]},
    "p12": {"type": "icons", "items": [
        {"label": "A hypothesis to prove", "icon": "test", "with": 0},
        {"label": "Leading: standard work", "icon": "clipboard", "with": 1},
        {"label": "Lagging: output, defects, UPPH", "icon": "chartUp", "with": 2},
        {"label": "Ergonomics with operators", "icon": "person", "with": 3}]},
    "p13": {"type": "compare", "before": {"label": "Before", "value": 103}, "after": {"label": "After", "value": 116},
            "unit": "good units an hour (theory: 120)", "note": "Done after two stable weeks", "with": 2},
    "p14": {"type": "icons", "items": [
        {"label": "Real work, current data", "icon": "clock", "tone": "good", "with": 0},
        {"label": "Operators, Quality, Engineering", "icon": "person", "tone": "good", "with": 1},
        {"label": "Safety, ESD, tests, traceability", "icon": "shield", "tone": "good", "with": 2},
        {"label": "Best-case times, headcount cuts", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Pilot line, time studies, baseline", "sub": "Days 1–30", "icon": "clock", "with": 0},
        {"label": "ECRS, rebalance, qualify", "sub": "31–60", "icon": "sequence", "with": 1},
        {"label": "Verify, update SOPs, expand", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Station 4 runs 33 s against a 30-second TAKT; Station 1 runs 22 s. What should you try first?",
        "options": ["Ask station 4's operator to work faster",
                     "Move a feasible task from station 4 to station 1, or improve its method, then pilot and re-measure",
                     "Remove a quality check at station 4",
                     "Change the TAKT to 33 seconds"],
        "correct": 1,
        "explanation": "Balancing moves feasible work or improves the method. Pushing people, dropping checks or redefining TAKT hides the problem instead of fixing it.",
        "q_script": "Quick check, and it's a scenario. Station four runs thirty-three seconds against a "
                    "thirty-second TAKT. Station one runs twenty-two. What should you try first? Take a "
                    "few seconds.",
        "a_script": "Look for a feasible task to move from station four to station one, or improve its method. Then pilot "
                    "and re-measure. Pushing people or dropping checks isn't balancing.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "420 net minutes serve demand of 840 good units. What is the TAKT time?",
        "options": ["20 seconds per unit",
                     "30 seconds per unit",
                     "2 seconds per unit",
                     "60 seconds per unit"],
        "correct": 1,
        "explanation": "TAKT = net time ÷ demand = 420 × 60 ÷ 840 = 30 seconds per unit.",
        "q_script": "One more. Your line has four hundred and twenty net minutes. Demand is eight "
                    "hundred and forty good units. What's your TAKT time? Have a think.",
        "a_script": "It's thirty seconds per unit. Convert the minutes to seconds, then divide by "
                    "the demand.",
    },
]

# Spoken-only pronunciation fixes. The TTS reads "TAKT" (uppercase) as the
# letters T-A-K-T, so feed it a phonetic spelling that rhymes with "tact".
# On-screen text (content/quizzes/captions) keeps the proper "TAKT".
def say(text: str) -> str:
    return text.replace("TAKT", "tact")


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
