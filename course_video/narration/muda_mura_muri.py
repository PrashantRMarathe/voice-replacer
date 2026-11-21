"""Muda, Mura, Muri (the 3M) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Sanjay,
a line supervisor on a CCTV camera assembly line that misses its hourly plan.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/muda_mura_muri.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py muda_mura_muri  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "mm"
NAME = "muda_mura_muri"

LETTERS = ["CCTV", "WIP", "FPY", "SMED", "TPM", "UPH", "OEE", "SOP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = text.replace("TIMWOODS", "Tim Woods").replace("TAKT", "tact")
    return re.sub(r"\b3M\b", "three M", text)


INTRO_SCRIPT = (
    "Six o'clock. The shift ends in one hour, and Sanjay's line is forty cameras behind. "
    "Everyone is rushing. Mistakes pile up at test. Tomorrow, it happens again. Sound "
    "familiar? In this lesson, you'll learn the 3M of Lean: Muda, Mura and Muri. You'll "
    "see how waste, unevenness and overburden feed each other. And we'll follow Sanjay, "
    "a line supervisor on a CCTV camera line, as he breaks that cycle."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Muda is waste, Mura is unevenness, and Muri is "
    "overburden. They feed each other, so improve them together. And the goal is stable "
    "flow, not people working faster. Here's your action for this week. Walk one product "
    "through your line, and tag one example of each M. Great work completing this "
    "lesson. Next, you'll learn Next Inspection, protecting the process after yours."
)

# One story thread: Sanjay's CCTV camera assembly line. Big work-order releases,
# WIP waves before test, walking for parts, end-of-shift rush and overtime.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Meet the 3M",
        "points": [("Muda: waste — no value for the customer", "Muda is waste"),
                   ("Mura: unevenness — load swings up and down", "Mura is unevenness"),
                   ("Muri: overburden — beyond safe capacity", "Muri is overburden")],
        "example": "Sanjay's line, in one hour: operators wait for kits (Muda), output swings (Mura), then everyone rushes (Muri).",
        "example_cue": "On Sanjay's line",
        "script": "Here's the core idea. Lean looks for three enemies of good flow. Muda is "
                  "waste, work that adds no value for your customer. Mura is unevenness, a load "
                  "that swings up and down. Muri is overburden, asking people or machines for "
                  "more than they can safely give. On Sanjay's line, you can see all three in one "
                  "hour. Operators wait for kits, output swings, and then everyone rushes. So "
                  "which one should you attack first?",
    },
    {
        "key": "p02", "num": 2, "title": "How the 3M Connect",
        "points": [("You can't fix them one at a time", "You can't fix them"),
                   ("Mura creates Muri, Muri creates Muda", "Mura often creates Muri"),
                   ("Chase only the waste and it comes back", "If you only chase")],
        "example": "Monday's huge batch (Mura) → operators and tester rushed (Muri) → defects, rework, overtime (Muda).",
        "example_cue": "Sanjay's planner released",
        "script": "Here's the surprise. You can't fix them one at a time. Mura often creates "
                  "Muri, and Muri creates Muda. Sanjay's planner released a huge batch on Monday "
                  "morning. That's Mura. To catch up, operators hurried and the tester never "
                  "rested. That's Muri. Then came defects, rework and overtime. That's Muda. If "
                  "you only chase the waste, it comes straight back. So let's look closely at "
                  "each one, starting with waste.",
    },
    {
        "key": "p03", "num": 3, "title": "Muda: The Value Test",
        "points": [("Does it change the product the customer needs?", "Does this step change"),
                   ("Is it done right the first time?", "Is it done right"),
                   ("Would the customer pay for it?", "Would the customer happily"),
                   ("If not — challenge it", "If the answer is no")],
        "example": "Fitting the lens adds value. Walking to fetch labels, waiting for a kit and testing twice do not.",
        "example_cue": "On Sanjay's line, fitting",
        "script": "How do you spot waste? Use a simple value test. Does this step change the "
                  "product in a way your customer needs? Is it done right the first time? Would "
                  "the customer happily pay for it? If the answer is no, challenge it. On "
                  "Sanjay's line, fitting the lens adds value. Walking to fetch labels doesn't. "
                  "Neither does waiting for a kit, or testing a camera twice. But can you "
                  "remove every step that fails the test?",
    },
    {
        "key": "p04", "num": 4, "title": "Necessary vs Pure Waste",
        "points": [("Type 1: needed today — simplify it", "Some steps add no value"),
                   ("Type 2: pure waste — remove it", "Type two is pure waste"),
                   ("Never call a person waste", "Never call a person waste")],
        "example": "Type 1: a required safety check. Type 2: typing the same serial into two systems.",
        "example_cue": "A required safety check",
        "script": "Not always. Some steps add no value, but you still need them today. A "
                  "required safety check is one. That's type one waste. Simplify it, or redesign "
                  "so it's no longer needed. Type two is pure waste, like typing the same serial "
                  "into two systems. Remove it. And here's a rule you must keep. Never call a "
                  "person waste. Waste lives in the process. Your job is to make the work easier "
                  "and safer. So what does waste look like?",
    },
    {
        "key": "p05", "num": 5, "title": "The 8 Wastes: TIMWOODS",
        "points": [("Transport · Inventory · Motion · Waiting", "Transport, inventory"),
                   ("Overproduction · Over-processing", "Overproduction and over-processing"),
                   ("Defects · unused Skills", "Defects, and unused skills"),
                   ("Waste walk: follow one product", "Sanjay did a waste walk")],
        "example": "Sanjay's waste walk: 3 kit waits in 2 hours, long walks for labels, a wall of WIP before test.",
        "example_cue": "Three waits for kits",
        "script": "Remember the eight wastes with one word, TIMWOODS. Transport, inventory, "
                  "motion and waiting. Overproduction and over-processing. Defects, and unused "
                  "skills. Sanjay did a waste walk. He followed one camera from kitting to "
                  "packing, and wrote down what he saw. Three waits for kits in two hours. Long "
                  "walks for labels. And a wall of WIP in front of test. Which of those eight "
                  "would you find first on your line?",
    },
    {
        "key": "p06", "num": 6, "title": "Mura: Unevenness",
        "points": [("Big batches, then nothing", "Big batches arrive"),
                   ("Material in fits and starts", "Material comes in fits"),
                   ("Same job, different methods", "Two operators do"),
                   ("Averages hide the peaks and valleys", "The average looks fine")],
        "example": "Sanjay's hourly board: 60, then 105, then 70. The average looks fine; the line doesn't.",
        "example_cue": "Look at Sanjay's hourly board",
        "script": "Now, Mura. It's unevenness in demand, workload or flow. Big batches arrive, "
                  "then nothing. Material comes in fits and starts. Two operators do the same job "
                  "in different ways. Look at Sanjay's hourly board. Sixty, then one hundred and "
                  "five, then seventy. The average looks fine. But your line doesn't live in "
                  "averages. It lives in those peaks and valleys. And peaks put pressure on "
                  "someone. Who do you think pays?",
    },
    {
        "key": "p07", "num": 7, "title": "Muri: Overburden",
        "points": [("People: lifting, reaches, alarms, too little training", "For people, it's heavy"),
                   ("Machines: past rated load, skipped maintenance", "For machines, it's running"),
                   ("Leads to fatigue, errors, breakdowns", "Muri leads to fatigue")],
        "example": "An operator reaches above shoulder height 120 times an hour; the tester runs through every break.",
        "example_cue": "One of Sanjay's operators",
        "script": "People and machines pay. That's Muri, overburden. For people, it's heavy "
                  "lifting, awkward reaches, too many alarms, or too little training. For "
                  "machines, it's running past their rated load, and skipping maintenance to hit "
                  "output. One of Sanjay's operators reaches above her shoulder a hundred and "
                  "twenty times an hour. And the tester runs straight through every break. Muri "
                  "leads to fatigue, errors and breakdowns. So how do the three combine?",
    },
    {
        "key": "p08", "num": 8, "title": "When All Three Collide",
        "points": [("4 hours of demand in one release", "Four hours of demand"),
                   ("Stations built ahead — WIP piled up", "The first stations built ahead"),
                   ("Test became the bottleneck", "Test became the bottleneck"),
                   ("Overtime, rushing, defects, rework", "Supervisors added people")],
        "example": "Looked like 'low test capacity'. Really: uneven release (Mura) + rushing (Muri) + rework (Muda).",
        "example_cue": "It looked like a test capacity",
        "script": "Here's what happened on Monday. Four hours of demand arrived in one release. "
                  "The first stations built ahead, and WIP piled up. Test became the bottleneck. "
                  "Supervisors added people and overtime. Operators hurried, defects rose, and "
                  "rework loaded test even more. It looked like a test capacity problem. But you "
                  "can see all three Ms in that story. So how do you find them on your own line?",
    },
    {
        "key": "p09", "num": 9, "title": "Finding 3M at the Gemba",
        "points": [("Watch before you change anything", "watch before you change"),
                   ("Record times, waits, walks, WIP, rework", "Record cycle times"),
                   ("Ask operators what's hard", "Then ask the operators"),
                   ("Check the data before choosing a fix", "Then check the data")],
        "example": "Sanjay tagged each finding Muda, Mura or Muri. A 20-minute kit wait got two tags: waste and unevenness.",
        "example_cue": "Sanjay tagged each finding",
        "script": "Go to the gemba, and watch before you change anything. Pick one product "
                  "family, and follow it. Record cycle times, waiting, walking, WIP and rework. "
                  "Then ask the operators what makes the job hard, uneven or unsafe. They "
                  "usually know. Sanjay tagged each finding as Muda, Mura or Muri. Some got two "
                  "tags. A twenty-minute kit wait is both waste and unevenness. Then check the "
                  "data before you choose a fix.",
    },
    {
        "key": "p10", "num": 10, "title": "Tools to Remove Muda",
        "points": [("5S: less searching and walking", "Five S cuts"),
                   ("Standard work: the best, safest method", "Standard work sets"),
                   ("Poka Yoke: stop errors at the source", "Poka Yoke stops errors"),
                   ("SMED and TPM: changeovers, reliability", "SMED cuts changeover"),
                   ("Root cause analysis: no repeat defects", "Root cause analysis stops"),
                   ("Don't automate a waste", "Don't automate a waste")],
        "example": "Labels and screws moved to racks at each station: walking dropped from 40 m to 8 m.",
        "example_cue": "Sanjay moved labels",
        "script": "Let's start removing waste. Five S cuts searching and walking. Standard work "
                  "sets the best, safest method. Poka Yoke stops errors at the source. SMED cuts "
                  "changeover time, and TPM keeps machines reliable. Root cause analysis stops "
                  "repeat defects. Sanjay moved labels and screws to racks at each station. "
                  "Walking dropped from forty meters to eight. One warning, though. Don't "
                  "automate a waste. You'll just make it faster.",
    },
    {
        "key": "p11", "num": 11, "title": "Tools to Level Mura",
        "points": [("Heijunka: level volume and mix", "Heijunka levels"),
                   ("TAKT links your pace to demand", "TAKT time links"),
                   ("Release every pitch, not in waves", "releases work every pitch"),
                   ("Pull and first-in, first-out lanes", "Pull signals")],
        "example": "TAKT = 27,000 s ÷ 450 cameras = one camera every 60 seconds.",
        "example_cue": "Sanjay's shift has",
        "script": "Next, smooth the flow. Heijunka levels both volume and mix. TAKT time links "
                  "your pace to customer demand. Sanjay's shift has twenty-seven thousand "
                  "seconds of working time. The customer needs four hundred and fifty cameras. That's one "
                  "camera every sixty seconds. So he now releases work every pitch, not in "
                  "waves. Pull signals and first-in, first-out lanes keep it steady. TAKT is a "
                  "rhythm, not a whip. So how do you protect your people?",
    },
    {
        "key": "p12", "num": 12, "title": "Tools to Relieve Muri",
        "points": [("Balance each station to TAKT", "Balance each station"),
                   ("Reaches and lifts in a safe zone", "Keep reaches"),
                   ("Fixtures where hands hold parts", "Add fixtures"),
                   ("Respect machine limits and maintenance", "Respect machine limits")],
        "example": "A fixture now holds the camera during screwing; the high bin moved down into easy reach.",
        "example_cue": "Sanjay added a fixture",
        "script": "Design the work so it fits people and machines. Balance each station to "
                  "TAKT, using real cycle times. Keep reaches and lifts in a safe zone. Add "
                  "fixtures and jigs where hands are holding parts. Respect machine limits, and "
                  "never skip maintenance to protect output. Sanjay added a fixture that holds "
                  "the camera during screwing. The high bin moved down into easy reach. Never "
                  "plan for a hundred percent utilization. So how do you put it all together?",
    },
    {
        "key": "p13", "num": 13, "title": "An 8-Step 3M Method",
        "points": [("Define, then observe at the gemba", "Define the problem"),
                   ("Classify into the three Ms", "Classify what you see"),
                   ("Measure a baseline, find root causes", "Measure a baseline"),
                   ("Test small changes with PDCA", "Test small changes"),
                   ("Standardize, keep auditing", "When a change works")],
        "example": "Sanjay's baseline: hourly output swinging widely, 2.5 hours of overtime a day.",
        "example_cue": "Sanjay's baseline was clear",
        "script": "Use a simple eight-step method. Define the problem, then observe at the "
                  "gemba. Classify what you see into the three Ms. Measure a baseline, then find "
                  "the root causes. Test small changes with Plan, Do, Check, Act. When a change "
                  "works, make it the new standard, and keep auditing it. Sanjay's baseline was "
                  "clear. Hourly output swung widely, and overtime ran two and a half hours a "
                  "day. Now, let's see his results.",
    },
    {
        "key": "p14", "num": 14, "title": "Case Study: CCTV Line",
        "points": [("Smaller, steady releases + first-in, first-out lane", "Smaller, steady releases"),
                   ("Parts and labels at the point of use", "Parts and labels"),
                   ("Release matched to test capacity", "Work released to match"),
                   ("Hourly board, problems raised early", "And an hourly board")],
        "example": "After 6 weeks: hourly swing almost gone, overtime close to zero, first pass yield up to 98%.",
        "example_cue": "After six weeks",
        "script": "Here's what Sanjay changed. Smaller, steady releases, with a first-in, "
                  "first-out lane before test. Parts and labels at the point of use. Work "
                  "released to match test capacity. And an hourly board, so problems are raised "
                  "early, not at six o'clock. After six weeks, the hourly swing almost "
                  "disappeared. Overtime fell close to zero. First pass yield rose to ninety-eight "
                  "percent. Notice he didn't ask anyone to work faster. So how do you prove it lasts?",
    },
    {
        "key": "p15", "num": 15, "title": "KPIs & Sustaining",
        "points": [("Flow: lead time, WIP", "For flow"),
                   ("Mura: hourly output range", "For Mura"),
                   ("Quality: FPY, rework", "For quality"),
                   ("Muri: overtime, ergonomic risk", "For Muri")],
        "example": "Units per hour up, but quality down and overtime up? You've only moved the loss.",
        "example_cue": "If units per hour",
        "script": "Measure all three Ms, not just output. For flow, track lead time and WIP. For "
                  "Mura, track the hourly output range, not only the average. For quality, "
                  "track first pass yield and rework. For Muri, watch overtime and ergonomic "
                  "risks. And never chase one number alone. If units per hour go up, but quality "
                  "falls and overtime climbs, you've only moved the loss. Keep reviewing it at "
                  "the gemba, every week.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Muda", "sub": "Waste: waiting for kits", "icon": "trash", "tone": "bad"},
        {"label": "Mura", "sub": "Unevenness: output swings", "icon": "wave", "tone": "bad"},
        {"label": "Muri", "sub": "Overburden: everyone rushes", "icon": "weight", "tone": "bad"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Mura", "sub": "A huge Monday batch", "icon": "wave", "tone": "bad", "with": 1},
        {"label": "Muri", "sub": "Rushing; the tester never rests", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Muda", "sub": "Defects, rework, overtime", "icon": "trash", "tone": "bad", "with": "example"}]},
    "p03": {"type": "versus", "items": [
        {"label": "Walking for labels", "sub": "No value (nor waiting, testing twice)", "icon": "walk", "with": "example"},
        {"label": "Fitting the lens", "sub": "Adds value", "icon": "camera", "with": "example"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Type 1: simplify", "sub": "A required safety check", "icon": "shield"},
        {"label": "Type 2: remove", "sub": "One serial typed twice", "icon": "cross", "tone": "bad"},
        {"label": "People are never waste", "sub": "Waste lives in the process", "icon": "person", "tone": "good"}]},
    "p05": {"type": "steps", "items": [
        {"label": "Transport", "sub": "T", "with": 0}, {"label": "Inventory", "sub": "I", "with": 0},
        {"label": "Motion", "sub": "M", "with": 0}, {"label": "Waiting", "sub": "W", "with": 0},
        {"label": "Overproduction", "sub": "O", "with": 1}, {"label": "Over-processing", "sub": "O", "with": 1},
        {"label": "Defects", "sub": "D", "with": 2}, {"label": "Unused skills", "sub": "S", "with": 2}]},
    "p06": {"type": "bars", "label": "Average", "note": "looks fine, hides the swings", "unit": "Sanjay's hourly board: cameras per hour", "items": [
        {"label": "Hour 1", "value": 60, "with": "example"},
        {"label": "Hour 2", "value": 105, "tone": "bad", "with": "example"},
        {"label": "Hour 3", "value": 70, "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "People", "sub": "Lifting, reaches, alarms", "icon": "person", "tone": "bad", "with": 0},
        {"label": "Machines", "sub": "Past rated load", "icon": "gear", "tone": "bad", "with": 1}],
        "then": {"type": "stat", "value": 120, "icon": "hand", "label": "reaches above shoulder height",
                 "unit": "every hour, for one operator", "with": "example"}},
    "p08": {"type": "flow", "items": [
        {"label": "4 hours of demand at once", "icon": "wave", "tone": "bad"},
        {"label": "WIP piles up", "icon": "stack", "tone": "bad"},
        {"label": "Test becomes the bottleneck", "icon": "test", "tone": "bad"},
        {"label": "Overtime, rushing, rework", "icon": "clock", "tone": "bad"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Watch first", "icon": "search"}, {"label": "Record it", "icon": "clipboard"},
        {"label": "Ask operators", "icon": "person"}, {"label": "Check the data", "icon": "chartUp"}]},
    "p10": {"type": "icons", "items": [
        {"label": "5S", "icon": "tray", "with": 0}, {"label": "Standard work", "icon": "clipboard", "with": 1},
        {"label": "Poka Yoke", "icon": "key", "with": 2}, {"label": "SMED + TPM", "icon": "wrench", "with": 3},
        {"label": "Root cause", "icon": "search", "with": 4}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 40}, "after": {"label": "After", "value": 8},
                 "suffix": " m", "unit": "walking per camera", "note": "80% less walking", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Heijunka", "sub": "Level volume and mix", "icon": "sequence", "with": 0},
        {"label": "TAKT", "sub": "Pace set by demand", "icon": "clock", "with": 1}],
        "then": {"type": "stat", "value": 60, "suffix": " s", "icon": "camera", "label": "one camera every 60 seconds",
                 "unit": "27,000 s of work time ÷ 450 cameras", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Balance to TAKT", "icon": "scale"}, {"label": "Safe reach zone", "icon": "person"},
        {"label": "Fixtures and jigs", "icon": "wrench"}, {"label": "Machine limits", "icon": "gear"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Hands hold the camera", "sub": "High bin above the shoulder", "icon": "hand"},
            {"label": "A fixture holds it", "sub": "Bin moved into easy reach", "icon": "wrench"}]}},
    "p13": {"type": "steps", "items": [
        {"label": "Define", "with": 0}, {"label": "Observe", "with": 0}, {"label": "Classify 3M", "with": 1},
        {"label": "Measure", "with": 2}, {"label": "Find causes", "with": 2}, {"label": "Test (PDCA)", "with": 3},
        {"label": "Standardize", "with": 4}, {"label": "Audit", "with": 4}]},
    "p14": {"type": "flow", "items": [
        {"label": "Small, steady releases", "icon": "sequence", "tone": "good"},
        {"label": "Parts at point of use", "icon": "tray", "tone": "good"},
        {"label": "Release = test capacity", "icon": "test", "tone": "good"},
        {"label": "Hourly board", "icon": "chartUp", "tone": "good"}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "first pass yield after 6 weeks",
                 "unit": "Overtime close to zero. Nobody worked faster.", "with": "example"}},
    "p15": {"type": "icons", "items": [
        {"label": "Flow", "sub": "Lead time, WIP", "icon": "clock"},
        {"label": "Mura", "sub": "Hourly range", "icon": "wave"},
        {"label": "Quality", "sub": "FPY, rework", "icon": "check"},
        {"label": "Muri", "sub": "Overtime, ergonomics", "icon": "weight"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Hourly output on a line reads 60, 105, 70, 110. Which M does this show most clearly?",
        "options": ["Muda — waste", "Mura — unevenness", "Muri — overburden"],
        "correct": 1,
        "explanation": "Output swinging hour to hour is Mura: unevenness in load and flow. Left alone, it usually creates Muri (rushing) and then Muda (defects, overtime).",
        "q_script": "Quick check. A line's hourly output keeps swinging, between sixty and one "
                    "hundred and ten. Which M does that show most clearly? Take a few seconds.",
        "a_script": "It's Mura, unevenness. The load swings from hour to hour. Left alone, it "
                    "usually creates rushing, and then waste.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A supervisor hits the daily plan by adding two hours of overtime every day. What should the team do FIRST?",
        "options": ["Ask operators to work faster", "Add more overtime to build a buffer",
                    "Observe the flow and find the Mura and Muri behind the shortfall",
                    "Buy another tester"],
        "correct": 2,
        "explanation": "Overtime hides the problem. Go to the gemba and find the unevenness and overburden causing the loss, then level and rebalance. Speed-ups, buffers or new machines just move the loss.",
        "q_script": "One more, and this one's a scenario. A supervisor hits the plan every day by "
                    "adding two hours of overtime. What should the team do first? Have a think.",
        "a_script": "Go and observe the flow first. Find the unevenness and overburden behind "
                    "the shortfall, then level and rebalance. Overtime only hides the problem.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
