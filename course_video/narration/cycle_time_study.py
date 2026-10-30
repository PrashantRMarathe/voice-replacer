"""Cycle Time Study lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Imran,
a process engineer on a monitor assembly line, timing the display-test
station that the report said was fast enough.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/cycle_time_study.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py cycle_time_study  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "ct"
NAME = "cycle_time_study"

LETTERS = ["UPH", "FPY", "ECRS", "SOP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. TAKT = "tact".
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return re.sub(r"\bTAKT\b", "tact", text)


INTRO_SCRIPT = (
    "The report said every station was faster than twenty-four seconds. Yet the monitor line "
    "missed its hourly target, shift after shift. So whose numbers were wrong? Sound "
    "familiar? In this lesson, you'll learn the Cycle Time Study. You'll see how to time a "
    "station properly, find the real bottleneck, and fix it without pushing people faster. "
    "We'll follow Imran, a process engineer on a monitor assembly line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Define the boundary first, or your numbers can't be "
    "compared. Look at the spread, not just the average. And fix the method at the "
    "bottleneck, never by skipping quality checks. Here's your action for this week. Time ten "
    "cycles at one station, and compare the longest one with TAKT. Great work completing this "
    "lesson. Next, you'll learn Design Thinking."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Cycle Time Is",
        "points": [("Time between completed units", "the time between"),
                   ("At a defined boundary", "at a boundary you define"),
                   ("Under stated conditions", "under conditions you state")],
        "example": "The report said station C took 21 seconds. Imran's stopwatch said 28.",
        "example_cue": "The report said",
        "script": "Let's start with a clear definition. Cycle time is the time between one completed "
                  "unit and the next. It's measured at a boundary you define, under conditions you "
                  "state. Sounds simple, right? Here's why it isn't. The report said the display-test "
                  "station took twenty-one seconds. Imran stood there with a stopwatch, and measured "
                  "twenty-eight. Both numbers were honest. So how can they both be true?",
    },
    {
        "key": "p02", "num": 2, "title": "Boundaries Matter",
        "points": [("Manual time: hands-on work", "Manual time is"),
                   ("Machine time: test, dispense, cure", "Machine time is"),
                   ("Station cycle: the real repeat interval", "The station cycle"),
                   ("Same boundary, or no comparison", "If two teams")],
        "example": "21 seconds came from old standard times. 28 seconds was the real unit-to-unit interval.",
        "example_cue": "The report used",
        "script": "Because they measured different things. Manual time is the hands-on work, like "
                  "fastening and connecting. Machine time is automatic, like a test or a cure. The "
                  "station cycle is the real repeat interval, with any overlap. You can't just add them "
                  "up. The report used old standard times, with no retries or waiting. Imran timed one "
                  "finished monitor to the next. If "
                  "two teams use different boundaries, their numbers can't be compared. So which number "
                  "matters to your customer?",
    },
    {
        "key": "p03", "num": 3, "title": "Cycle Time vs TAKT, Lead Time, UPH",
        "points": [("Cycle time: how often you finish one", "Cycle time asks"),
                   ("TAKT: the pace demand needs", "TAKT asks"),
                   ("Lead time: order to finish, with waiting", "Lead time is"),
                   ("UPH: good units per hour", "U-P-H counts")],
        "example": "Imran's line: TAKT 24 seconds, so it needs 150 monitors an hour.",
        "example_cue": "On Imran's line",
        "script": "Four measures sound alike, but they answer different questions. Cycle time asks, "
                  "how often do you finish one? TAKT asks, what pace does demand need? Lead time is "
                  "the whole journey, from order to finish, including waiting. It can be days, even "
                  "when your cycle is seconds. U-P-H counts good units per hour. On Imran's line, "
                  "TAKT is twenty-four seconds. That's a hundred and fifty monitors an hour. Which "
                  "of these do you track?",
    },
    {
        "key": "p04", "num": 4, "title": "Comparing With TAKT",
        "points": [("Above TAKT: a capacity shortfall", "If cycle time is above"),
                   ("Equal to TAKT: no headroom", "If it's equal"),
                   ("Below TAKT: headroom, don't overproduce", "If it's below")],
        "example": "Station C at 28 seconds sits 4 seconds above a 24-second TAKT.",
        "example_cue": "Imran's display-test station",
        "script": "Now compare your cycle with TAKT. If cycle time is above TAKT, that station can't "
                  "keep up. You have a capacity shortfall. If it's equal, you've got no room for any "
                  "hiccup or downtime. If it's below, you have headroom. But don't use it to "
                  "overproduce. Imran's display-test station sat at twenty-eight seconds. That's four "
                  "seconds above TAKT, every single cycle. So how do you run a study you can trust?",
    },
    {
        "key": "p05", "num": 5, "title": "Preparing the Study",
        "points": [("A clear purpose and station", "Pick the station"),
                   ("Record the conditions", "Write down the conditions"),
                   ("Normal cycles only, delays logged", "Separate startup"),
                   ("Explain it to the operator", "And tell the operator")],
        "example": "Imran's goal: measure station C's repeat interval to check capacity against TAKT.",
        "example_cue": "Imran's goal was",
        "script": "A good study starts with a purpose. Pick the station, maybe a suspected bottleneck, "
                  "or one that varies a lot. Write down the conditions. That means the model, the "
                  "operator, the shift and the tools. Separate startup, changeover and rework from "
                  "normal cycles. And tell the operator why you're there. You're studying the process, "
                  "not judging them. Imran's goal was one sentence. Check station C against TAKT. "
                  "Ready to break the work down?",
    },
    {
        "key": "p06", "num": 6, "title": "Breaking Down the Elements",
        "points": [("Split work into visible elements", "Split the work"),
                   ("Clear start and finish for each", "Each element needs"),
                   ("Waiting recorded separately", "Record waiting separately"),
                   ("Never cut quality or safety checks", "Never remove")],
        "example": "Station C: load 5 s, scan label 3 s, display test 15 s, unload 4 s, waiting 1 s.",
        "example_cue": "Imran split station C",
        "script": "Split the work into small elements you can actually see. Each element needs a clear "
                  "start and finish, so nothing is counted twice. Record waiting separately from touch "
                  "time. Then sort each step as value-adding, necessary, or pure waste. Never remove a "
                  "required quality or safety check. Imran split station C into five parts. Load, scan "
                  "the label, display test, unload, and a little waiting. Where would you look first?",
    },
    {
        "key": "p07", "num": 7, "title": "The Stopwatch Sheet",
        "points": [("Time repeated cycles, not one", "Time many cycles"),
                   ("Average: 28 s. Range: 26 to 32 s", "The average was"),
                   ("Log every abnormal cycle", "Log every abnormal")],
        "example": "The longest cycle: 32 seconds, when the label scan failed twice.",
        "example_cue": "The longest cycle",
        "script": "Never trust one good-looking cycle. Time many cycles in a row. Imran timed ten. The "
                  "average was twenty-eight seconds. But the spread ran from twenty-six all the way to "
                  "thirty-two. Log every abnormal cycle, with its reason, not just the number. The "
                  "longest cycle came when the label scan failed twice. An average alone would have "
                  "hidden that. What's your longest cycle hiding?",
    },
    {
        "key": "p08", "num": 8, "title": "Calculating Capacity",
        "points": [("Hourly output = 3,600 ÷ cycle time", "Hourly output is"),
                   ("Station C: about 129 an hour", "At twenty-eight seconds"),
                   ("Stations needed = work content ÷ TAKT", "To find how many")],
        "example": "Demand needs 150 an hour. Station C makes about 129. That's the gap.",
        "example_cue": "Demand needs",
        "script": "Now turn time into capacity. Hourly output is the seconds in an hour, divided by "
                  "your cycle time. At twenty-eight seconds, station C makes about a hundred and "
                  "twenty-nine monitors an hour. Demand needs a hundred and fifty. That's the gap, in "
                  "plain numbers. To find how many stations you need, divide total work content by "
                  "TAKT, then round up. State every assumption. Does your plan use net time, after "
                  "breaks?",
    },
    {
        "key": "p09", "num": 9, "title": "Variation Matters",
        "points": [("Averages hide long cycles", "averages hide"),
                   ("Plot cycles in time order", "Plot your cycles"),
                   ("Never delete long cycles to look good", "Never delete"),
                   ("Report spread and % over TAKT", "Report the typical time")],
        "example": "Station C: 3 of 10 cycles ran 30 seconds or more.",
        "example_cue": "At station C",
        "script": "Here's a trap. Two stations can share an average, and behave very differently. "
                  "Averages hide the long cycles that build queues. So plot your cycles in time order. "
                  "Split them by model and shift before you pool them. Never delete long cycles just "
                  "to improve the average. Investigate them instead. Report the typical time, the "
                  "spread, and how often you go over TAKT. At station C, three cycles in ten ran "
                  "thirty seconds or more. Sound familiar?",
    },
    {
        "key": "p10", "num": 10, "title": "Finding the Bottleneck",
        "points": [("The slowest station sets the pace", "The slowest station"),
                   ("Look for queues before, idle after", "Look for a queue"),
                   ("Fix the constraint first", "Fix the constraint first")],
        "example": "Stations A 19 s, B 22 s, C 28 s, D 21 s. Station C caps the line.",
        "example_cue": "Imran timed all four",
        "script": "So which station really limits your line? The slowest station usually sets the "
                  "pace. Look for a queue building in front of it, and people waiting after it. Imran "
                  "timed all four stations. Stand and cover, board fit, display test and packing. Only "
                  "display test sat above TAKT. Fix the constraint first. Speeding up any other "
                  "station just piles up more work in progress. So why was station C slow?",
    },
    {
        "key": "p11", "num": 11, "title": "Why Is It Slow?",
        "points": [("Go and see: the real station", "Imran went to the gemba"),
                   ("Method, design, machine or waiting?", "A slow station can be"),
                   ("Check retries, alarms and timestamps", "He checked")],
        "example": "Label scan retries, and a serial label applied at the test station itself.",
        "example_cue": "He found two things",
        "script": "Imran went to the gemba, and watched the real station. A slow station can be a "
                  "method problem, a design problem, a slow machine, or simply waiting. Each needs a "
                  "different fix. He checked scan retries, alarm codes and test timestamps. He found "
                  "two things. Labels sat at an angle, so the scanner often missed. And the operator "
                  "also stuck on the serial label, right there, inside the cycle. What would you try?",
    },
    {
        "key": "p12", "num": 12, "title": "Improve the Method",
        "points": [("Eliminate, Combine, Rearrange, Simplify", "Think ECRS"),
                   ("Simple, low-cost fixes first", "Then look at"),
                   ("Never skip tests to save time", "But never cut a cycle")],
        "example": "A label guide straightens every label. The scanner reads first time.",
        "example_cue": "Imran added",
        "script": "Fix the method before you ask anyone to go faster. Think ECRS. Eliminate, combine, "
                  "rearrange and simplify. Then look at simple, low-cost fixes, like guides, feeders "
                  "and barcode checks. But never cut a cycle by skipping a test, a torque check or "
                  "E-S-D control. That's not improvement. Imran added a small label guide. Every label "
                  "now sits straight, and the scanner reads it first time. What about the serial label?",
    },
    {
        "key": "p13", "num": 13, "title": "Rebalancing the Line",
        "points": [("Move work to stations with spare time", "Move work to"),
                   ("Keep sequence, skills and checks", "Check the sequence"),
                   ("No new walking or ergonomic risk", "And make sure")],
        "example": "Serial label moved to station A: A 23 s, C 23 s. Every station now sits below TAKT.",
        "example_cue": "Imran moved the serial label",
        "script": "Next, rebalance the line. Move work to stations with spare time, but only if it's "
                  "safe. Check the sequence, the tools, the skills and the checks at the new station. "
                  "And make sure you don't add walking, strain or defect risk. Imran moved the serial "
                  "label to station A. Station A went to twenty-three seconds. Station C dropped to "
                  "twenty-three. Every station now sits below TAKT. Is that the end of the story?",
    },
    {
        "key": "p14", "num": 14, "title": "Prove It, Then Standardize",
        "points": [("Trial across shifts and models", "Run the trial"),
                   ("Compare spread, FPY and output", "Compare the spread"),
                   ("Update standard work and train", "update the standard work"),
                   ("Escalate drift fast", "Set a trigger")],
        "example": "Trigger: 3 cycles in a row over TAKT means the team leader checks the station.",
        "example_cue": "Imran's trigger",
        "script": "Not yet. A fast morning proves nothing. Run the trial across shifts and models. "
                  "Compare the spread, the first pass yield and the output, not just the average. If "
                  "quality holds, update the standard work and train every shift. Set a trigger, so "
                  "drift gets caught fast. Imran's trigger was simple. Three cycles in a row over "
                  "TAKT, and the team leader checks the station. Who would check yours?",
    },
    {
        "key": "p15", "num": 15, "title": "Your 30-Day Plan",
        "points": [("Week 1: define and baseline", "In week one"),
                   ("Week 2: find the bottleneck", "In week two"),
                   ("Week 3: trial one countermeasure", "In week three"),
                   ("Week 4: verify, standardize, train", "In week four")],
        "example": "Imran's line now meets 150 monitors an hour, with first pass yield unchanged.",
        "example_cue": "Imran's line now",
        "script": "Now it's your turn. Here's a simple thirty-day plan. In week one, define one "
                  "station's boundary, and time at least ten cycles. In week two, find the bottleneck "
                  "and its causes. In week three, trial one countermeasure. In week four, verify it, "
                  "update the SOP, and train. Imran's line now meets its hundred and fifty an hour, "
                  "and first pass yield didn't move. Which station will you time first?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Unit to unit", "icon": "sequence", "with": 0},
        {"label": "Defined boundary", "icon": "pin", "with": 1},
        {"label": "Stated conditions", "icon": "clipboard", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "21 s", "sub": "The report", "icon": "clipboard", "with": "example"},
            {"label": "28 s", "sub": "Imran's stopwatch", "icon": "clock", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Manual", "sub": "Hands-on work", "icon": "hand", "with": 0},
        {"label": "Machine", "sub": "Test, dispense, cure", "icon": "gear", "with": 1},
        {"label": "Station cycle", "sub": "Real repeat interval", "icon": "clock", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Old standard times", "sub": "21 seconds", "icon": "clipboard", "with": "example"},
            {"label": "Unit to unit", "sub": "28 seconds", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Cycle time", "sub": "How often you finish", "icon": "clock", "with": 0},
        {"label": "TAKT", "sub": "Pace demand needs", "icon": "wave", "with": 1},
        {"label": "Lead time", "sub": "Order to finish", "icon": "calendar", "with": 2},
        {"label": "UPH", "sub": "Good units per hour", "icon": "count", "with": 3}],
        "then": {"type": "stat", "value": 150, "icon": "count", "label": "monitors an hour needed",
                 "unit": "TAKT 24 seconds", "with": "example"}},
    "p04": {"type": "ladder", "top": "SHORTFALL", "bottom": "HEADROOM", "items": [
        {"label": "Above TAKT", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Equal to TAKT", "icon": "scale", "with": 1},
        {"label": "Below TAKT", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
            {"label": "Station C", "value": 28, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "flow", "items": [
        {"label": "Purpose and station", "icon": "pin", "with": 0},
        {"label": "Conditions", "icon": "clipboard", "with": 1},
        {"label": "Normal cycles only", "icon": "clock", "with": 2},
        {"label": "Explain to operator", "icon": "person", "tone": "good", "with": 3}]},
    "p06": {"type": "bars", "label": "", "note": "Station C elements: 28 s in total", "with": "example", "items": [
        {"label": "Load", "value": 5, "with": "example"},
        {"label": "Scan", "value": 3, "with": "example"},
        {"label": "Test", "value": 15, "with": "example"},
        {"label": "Unload", "value": 4, "with": "example"},
        {"label": "Wait", "value": 1, "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Ten cycles timed at station C (seconds)", "items": [
        {"label": "Fastest", "value": 26, "tone": "good", "with": 1},
        {"label": "Average", "value": 28, "with": 1},
        {"label": "Slowest", "value": 32, "tone": "bad", "with": "example"}]},
    "p08": {"type": "compare", "before": {"label": "Station C", "value": 129}, "after": {"label": "Demand", "value": 150},
            "unit": "monitors an hour", "note": "3,600 ÷ 28 ≈ 129", "with": 1},
    "p09": {"type": "icons", "items": [
        {"label": "Averages hide", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Time order", "icon": "chartUp", "with": 1},
        {"label": "Keep long cycles", "icon": "lock", "with": 2},
        {"label": "Spread, % over TAKT", "icon": "scale", "with": 3}],
        "then": {"type": "stat", "value": 3, "suffix": " of 10", "icon": "clock", "label": "cycles at 30 seconds or more",
                 "unit": "station C", "with": "example"}},
    "p10": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 19, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 28, "tone": "bad", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Method", "icon": "clipboard", "with": 1},
        {"label": "Design", "icon": "shape", "with": 1},
        {"label": "Machine", "icon": "gear", "with": 1},
        {"label": "Waiting", "icon": "clock", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Labels at an angle", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Scan retries", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Serial label inside the cycle", "icon": "sticker", "tone": "bad", "with": "example"}]}},
    "p12": {"type": "steps", "items": [
        {"label": "Eliminate", "with": 0}, {"label": "Combine", "with": 0},
        {"label": "Rearrange", "with": 0}, {"label": "Simplify", "with": 0}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Before", "sub": "Labels at an angle, scan retries", "icon": "barcode", "tone": "bad", "with": "example"},
            {"label": "Label guide", "sub": "Reads first time", "icon": "check", "tone": "good", "with": "example"}]}},
    "p13": {"type": "bars", "label": "TAKT", "value": 24, "suffix": " s", "with": "example", "items": [
        {"label": "A", "value": 23, "with": "example"},
        {"label": "B", "value": 22, "with": "example"},
        {"label": "C", "value": 23, "tone": "good", "with": "example"},
        {"label": "D", "value": 21, "with": "example"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Trial: shifts, models", "icon": "calendar", "with": 0},
        {"label": "Spread, FPY, output", "icon": "chartUp", "with": 1},
        {"label": "Standard work, training", "icon": "clipboard", "with": 2},
        {"label": "Trigger: 3 over TAKT", "icon": "warning", "tone": "good", "with": "example"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Define and baseline", "sub": "Week 1", "icon": "clock", "with": 0},
        {"label": "Bottleneck", "sub": "Week 2", "icon": "search", "with": 1},
        {"label": "Trial", "sub": "Week 3", "icon": "wrench", "with": 2},
        {"label": "Standardize", "sub": "Week 4", "icon": "check", "tone": "good", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A station's cycle time is 30 seconds. What is its theoretical output per hour?",
        "options": ["90 units", "120 units", "180 units"],
        "correct": 1,
        "explanation": "Hourly output = 3,600 ÷ cycle time = 3,600 ÷ 30 = 120 units an hour, before any losses.",
        "q_script": "Quick check. A station's cycle time is thirty seconds. What's its theoretical "
                    "output per hour? Take a few seconds.",
        "a_script": "It's a hundred and twenty. Divide the seconds in an hour by the cycle time, and "
                    "remember, that's before any losses.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "After a change, a station's cycle time drops from 28 to 22 seconds, but first pass yield falls. What now?",
        "options": ["Standardize it: the station is faster",
                    "Hold the change and find why quality dropped",
                    "Add a final inspector to catch the defects"],
        "correct": 1,
        "explanation": "A faster cycle that makes more defects isn't an improvement. Hold the change, find why yield fell, and only standardize once quality holds.",
        "q_script": "One more, and this one's a scenario. After a change, a station gets six seconds "
                    "faster. But first pass yield falls. What should the team do? Have a think.",
        "a_script": "Hold the change, and find out why quality dropped. A faster cycle that makes more "
                    "defects isn't an improvement at all.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
