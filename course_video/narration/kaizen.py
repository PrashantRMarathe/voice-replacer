"""Kaizen lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Suresh,
a line leader in monitor assembly, whose team removes two needless flips of
every monitor through a small, tested Kaizen, then turns it into a daily habit.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/kaizen.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py kaizen  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "kz"
NAME = "kaizen"

LETTERS = ["PDCA", "SDCA", "ECRS", "SOP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. Kaizen as spelled (KYE-zen, confirmed);
# TAKT = "tact".
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return re.sub(r"\bTAKT\b", "tact", text)


INTRO_SCRIPT = (
    "Every monitor on Suresh's line was flipped over twice. Face down, then face up again. "
    "Nobody asked why. It had always been done that way. Sound familiar? In this lesson, "
    "you'll learn Kaizen, continuous improvement. You'll see how small, tested changes, made "
    "by the people doing the work, add up to big results. We'll follow Suresh, a line leader "
    "in monitor assembly."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Kaizen is a daily habit, not a one-off event. Test small, "
    "measure honestly, and check nothing else got worse. And standardize every gain, so it "
    "becomes the starting point for the next one. Here's your action for this week. Ask one "
    "operator what makes their job difficult, and test one small fix. Great work completing "
    "this lesson. Next, you'll learn Low Cost Automation."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Kaizen Means",
        "points": [("Change for the better", "change for the better"),
                   ("Many small, disciplined changes", "many small changes"),
                   ("Made by the people closest to the work", "made by the people")],
        "example": "Suresh's line: two flips of every monitor, every unit, every shift.",
        "example_cue": "On Suresh's line",
        "script": "Kaizen is a Japanese word that means change for the better. In a factory, it means "
                  "continuous improvement through many small changes. They're made by the people "
                  "closest to the work, every day. Not one big project, once a year. On Suresh's line, "
                  "every monitor was flipped twice, on every shift. That's thousands of heavy lifts a "
                  "week. So what makes an improvement a Kaizen?",
    },
    {
        "key": "p02", "num": 2, "title": "What Makes It Kaizen",
        "points": [("Continuous and people-driven", "It's continuous"),
                   ("Starts at the gemba", "It starts at the gemba"),
                   ("Low cost first, backed by data", "It tries low-cost"),
                   ("Ends in a new standard", "And it ends")],
        "example": "Each improved standard is the baseline for the next Kaizen.",
        "example_cue": "Then the cycle",
        "script": "A few things set it apart. It's continuous, and driven by people, not just "
                  "engineers. It starts at the gemba, with what you actually see. It tries low-cost "
                  "ideas first, and checks the results with data. And it ends in a new standard, the "
                  "best method you know today. Then the cycle starts again, from that new baseline. "
                  "What mindset does that need?",
    },
    {
        "key": "p03", "num": 3, "title": "The Kaizen Mindset",
        "points": [("Every process can improve", "Every process can"),
                   ("Problems are for learning, not blame", "Problems are"),
                   ("Creativity before capital", "creativity before capital")],
        "example": "“We've always flipped it” is exactly the sentence Kaizen questions.",
        "example_cue": "We've always",
        "script": "It starts with a belief. Every process can improve, even a good one. Problems are "
                  "chances to learn, not reasons to blame someone. Go and see before you decide. And "
                  "use creativity before capital. A tape mark often beats a new machine. We've always "
                  "done it that way is exactly the sentence Kaizen questions. When did you last hear it "
                  "on your line?",
    },
    {
        "key": "p04", "num": 4, "title": "Types of Kaizen",
        "points": [("Daily Kaizen: minutes to days", "Daily Kaizen"),
                   ("Point Kaizen: one specific loss", "Point Kaizen"),
                   ("Kaizen event: three to five days", "A Kaizen event"),
                   ("System Kaizen: end-to-end flow", "System Kaizen")],
        "example": "The double flip: a point Kaizen, owned by Suresh's own team.",
        "example_cue": "The double flip",
        "script": "Kaizen comes in different sizes. Daily Kaizen is small and local, like moving a tool "
                  "closer. Point Kaizen targets one specific loss, in hours or days. A Kaizen event "
                  "brings a cross-functional team together for three to five days. System Kaizen fixes "
                  "flow across departments, over weeks. The double flip was a point Kaizen, owned by "
                  "Suresh's own team. Which size fits your biggest pain?",
    },
    {
        "key": "p05", "num": 5, "title": "Kaizen Runs on PDCA",
        "points": [("Plan: observe, define, find the cause", "Plan means"),
                   ("Do: a small, safe trial", "Do means"),
                   ("Check: compare with the baseline", "Check means"),
                   ("Act: standardize, or learn and repeat", "Act means")],
        "example": "SDCA holds the standard. PDCA improves it.",
        "example_cue": "Its twin",
        "script": "Every Kaizen follows PDCA. Plan means observe, define the gap, and find the cause. Do "
                  "means a small, safe trial. Check means comparing the result with your baseline and "
                  "target. Act means standardizing it, or learning and trying again. Its twin is SDCA, "
                  "which holds the standard steady. Strong teams switch between the two. Without PDCA, "
                  "an idea is just an untested change. Where do you start?",
    },
    {
        "key": "p06", "num": 6, "title": "See It at the Gemba",
        "points": [("Watch the work as it really is", "Watch the work"),
                   ("Count walking, reaching, flipping", "Count the walking"),
                   ("Ask what makes the job hard", "Ask the operators")],
        "example": "Flip face down to fit the stand, flip face up to test. Two lifts of a 6 kg monitor.",
        "example_cue": "Suresh's team saw",
        "script": "At the gemba, of course. Watch the work as it really is, not as the SOP says it is. "
                  "Count the walking, reaching, searching and lifting. Ask the operators what makes their "
                  "job hard. Suresh's team saw it straight away. Each monitor went face down to fit the "
                  "stand, then face up again for the test. Two lifts of a six kilo monitor, every time. "
                  "What would you write down?",
    },
    {
        "key": "p07", "num": 7, "title": "Define the Problem",
        "points": [("Symptom, then the facts", "Start with the symptom"),
                   ("Measure the loss", "Measure the loss"),
                   ("A target with a deadline", "Set a target")],
        "example": "Cycle 38 s vs 35 s TAKT. 2 flips per unit. 15 panel scratches per 1,000.",
        "example_cue": "Suresh's facts",
        "script": "Start with the symptom. The line missed its hourly target. Then get the facts. "
                  "Measure the loss, and keep facts apart from opinions. Suresh's facts were clear. "
                  "Cycle time was thirty-eight seconds, against a TAKT of thirty-five. Every flip risked "
                  "a scratch, and fifteen panels in a thousand were scratched. Set a target with a "
                  "deadline, and leave the solution out. What would you aim for?",
    },
    {
        "key": "p08", "num": 8, "title": "Generate Ideas",
        "points": [("Ask the operators first", "Ask the operators"),
                   ("Use ECRS", "Use ECRS"),
                   ("Look at other lines", "Look at other lines")],
        "example": "Leela, an operator: “Why not fit the stand while the monitor's still in its tray?”",
        "example_cue": "Leela, an operator",
        "script": "Now generate ideas, and plenty of them. Ask the operators first. What makes this job "
                  "difficult? What would remove one step? Use ECRS, eliminate, combine, rearrange and "
                  "simplify. Look at other lines, and other industries too. Leela, an operator on the "
                  "night shift, had the best idea. Why not fit the stand while the monitor is still face "
                  "down, in its tray? Why hadn't anyone asked her before?",
    },
    {
        "key": "p09", "num": 9, "title": "Choose the Idea",
        "points": [("Safety and quality are gates", "Safety and quality"),
                   ("Score impact, ease, cost, speed", "Then score"),
                   ("It must fix a verified cause", "And the idea must")],
        "example": "Leela's idea: high on impact, ease and cost. It won.",
        "example_cue": "Leela's idea",
        "script": "Pick with a simple scorecard. Safety and quality are gates. Fail them, and the idea is "
                  "out, whatever its score. Then score impact, ease, cost and speed, with agreed weights. "
                  "And the idea must address a cause you've verified. It should be simple enough for "
                  "everyone to follow. Leela's idea scored high on impact, ease and cost. It won easily. "
                  "How should you try it?",
    },
    {
        "key": "p10", "num": 10, "title": "Trial It Small",
        "points": [("A hypothesis and a scope", "Write a hypothesis"),
                   ("Same measures as the baseline", "Measure it the same way"),
                   ("Watch the people, not just the numbers", "Watch the operators")],
        "example": "One station, one shift: re-sequenced steps and a foam pad in the tray. Cost: almost nothing.",
        "example_cue": "Suresh's trial",
        "script": "Small and safe, first. Write a hypothesis. If we fit the stand in the tray, both "
                  "flips disappear. Set the scope, a station and a shift. Measure it the same way you "
                  "measured the baseline. Watch the operators, not just the numbers. Suresh's trial ran "
                  "on one station, for one shift. It used a re-sequenced job and a foam pad in the tray. "
                  "It cost almost nothing. What happened?",
    },
    {
        "key": "p11", "num": 11, "title": "Check the Results",
        "points": [("Cycle time: 38 s down to 33 s", "Cycle time fell"),
                   ("Flips per unit: 2 down to 0", "Both flips"),
                   ("Scratches: 15 down to 3 per 1,000", "Scratches fell"),
                   ("Nothing else got worse", "nothing else got worse")],
        "example": "Balanced rule: the target improves, and safety, quality and delivery don't suffer.",
        "example_cue": "That's the balanced rule",
        "script": "Cycle time fell to thirty-three seconds, now inside TAKT. Both flips disappeared. "
                  "Scratches fell from fifteen to three per thousand. And the team checked that nothing "
                  "else got worse. Test results, safety and the next station all held. Operators said their backs felt the difference by lunchtime. That's the "
                  "balanced rule. Improving one number while hurting another isn't Kaizen. But how do you "
                  "know it'll last?",
    },
    {
        "key": "p12", "num": 12, "title": "Measure Honestly",
        "points": [("Same definitions, before and after", "Use the same definitions"),
                   ("Count good output, not gross", "Count good output"),
                   ("Check again at 30, 60, 90 days", "check again")],
        "example": "Day 30: still 33 s. Day 90: still 33 s, and 3 scratches per 1,000.",
        "example_cue": "Suresh checked",
        "script": "Measure it honestly. Use the same definitions before and after. Count good output, not "
                  "gross output. Show the actual change, not just a percentage. And check that "
                  "something else, like an easier model mix, didn't cause it. Then check again at "
                  "thirty, sixty and ninety days. Suresh checked at day thirty, and again at ninety. "
                  "Still thirty-three seconds. What locks it in?",
    },
    {
        "key": "p13", "num": 13, "title": "Standardize the Gain",
        "points": [("Update the SOP and standard work", "Update the SOP"),
                   ("Train everyone, remove the old way", "Train every operator"),
                   ("Name an owner and audit it", "Name an owner")],
        "example": "The old flip instructions were removed from every station the same week.",
        "example_cue": "Suresh removed",
        "script": "A Kaizen isn't finished until it's the standard. Update the SOP and standard work. "
                  "Train every operator, and confirm they understand. Remove the old method, so nobody "
                  "drifts back. Name an owner, and audit it. Suresh removed the old flip instructions "
                  "from every station, the same week. The new method became the baseline. And the "
                  "baseline is where the next Kaizen starts. How do you keep ideas coming?",
    },
    {
        "key": "p14", "num": 14, "title": "Make It a Habit",
        "points": [("A visible idea board", "A visible idea board"),
                   ("Quick replies to every idea", "Reply to every idea"),
                   ("Recognize the people", "Recognize")],
        "example": "Suresh's team: 40 ideas in 3 months, 27 tested, 19 standardized.",
        "example_cue": "In three months",
        "script": "Make Kaizen a daily habit. A visible idea board helps people see their ideas matter. "
                  "Reply to every idea within a week, even when the answer is no. Recognize the people, "
                  "not just the savings. And review the pipeline every week. In three months, Suresh's "
                  "team logged forty ideas. They tested twenty-seven, and standardized nineteen. What "
                  "would happen on your line?",
    },
    {
        "key": "p15", "num": 15, "title": "Start Tomorrow",
        "points": [("Pick one recurring pain", "Pick one recurring pain"),
                   ("Watch ten cycles, talk to the team", "Watch ten cycles"),
                   ("Test the smallest safe fix", "test the smallest")],
        "example": "Kaizen = small improvements × disciplined repetition × ownership.",
        "example_cue": "Small improvements",
        "script": "Here's how to start tomorrow. Pick one recurring pain on your line. Watch ten cycles, "
                  "and measure the loss. Talk to the people who do the work, and set one measurable "
                  "target. Then test the smallest safe fix you can. If it works, standardize it. Small "
                  "improvements, repeated with discipline, by people who own them. That's how ordinary "
                  "lines become great ones. Who will you ask first?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Change for the better", "icon": "chartUp", "with": 0},
        {"label": "Small steps", "icon": "sequence", "with": 1},
        {"label": "By the team", "icon": "person", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 2, "icon": "weight", "label": "flips of every monitor",
                 "unit": "every unit, every shift", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Continuous", "icon": "sequence", "with": 0},
        {"label": "Gemba-based", "icon": "walk", "with": 1},
        {"label": "Low cost, data", "icon": "scale", "with": 2},
        {"label": "New standard", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p03": {"type": "versus", "items": [
        {"label": "“We've always done it”", "sub": "Accept the loss", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "“Every process can improve”", "sub": "Kaizen", "icon": "check", "tone": "good", "with": 0}]},
    "p04": {"type": "ladder", "top": "BIGGEST", "bottom": "SMALLEST", "items": [
        {"label": "System Kaizen", "sub": "Weeks", "icon": "stack", "with": 3},
        {"label": "Kaizen event", "sub": "3–5 days", "icon": "calendar", "with": 2},
        {"label": "Point Kaizen", "sub": "Hours to days", "icon": "pin", "with": 1},
        {"label": "Daily Kaizen", "sub": "Minutes", "icon": "hand", "with": 0}]},
    "p05": {"type": "flow", "items": [
        {"label": "Plan", "icon": "clipboard", "with": 0},
        {"label": "Do", "icon": "wrench", "with": 1},
        {"label": "Check", "icon": "search", "with": 2},
        {"label": "Act", "icon": "check", "tone": "good", "with": 3}]},
    "p06": {"type": "flow", "items": [
        {"label": "Face down: fit stand", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Face up: test", "icon": "weight", "tone": "bad", "with": "example"},
        {"label": "Two 6 kg lifts", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p07": {"type": "bars", "label": "TAKT", "value": 35, "suffix": " s", "with": "example", "items": [
        {"label": "Cycle time", "value": 38, "tone": "bad", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Ask operators", "icon": "person", "with": 0},
        {"label": "ECRS", "icon": "key", "with": 1},
        {"label": "Other lines", "icon": "search", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Flip twice", "sub": "Today", "icon": "weight", "tone": "bad", "with": "example"},
            {"label": "Fit stand in the tray", "sub": "Leela's idea", "icon": "check", "tone": "good", "with": "example"}]}},
    "p09": {"type": "icons", "with": "example", "items": [
        {"label": "Robot arm", "sub": "Score 2.4", "icon": "gear", "with": "example"},
        {"label": "Lifting aid", "sub": "Score 3.6", "icon": "weight", "with": "example"},
        {"label": "Leela's idea", "sub": "Score 4.7 of 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p10": {"type": "doc", "items": [
        {"label": "Hypothesis: both flips disappear", "icon": "key", "with": 0},
        {"label": "Scope: one station, one shift", "icon": "pin", "with": 0},
        {"label": "Same measures as baseline", "icon": "scale", "with": 1},
        {"label": "Foam pad + new sequence", "icon": "shape", "with": "example"}]},
    "p11": {"type": "compare", "before": {"label": "Before", "value": 15}, "after": {"label": "Trial", "value": 3},
            "unit": "panel scratches per 1,000 monitors", "note": "Cycle 38 s → 33 s · flips 2 → 0", "with": 2},
    "p12": {"type": "timeline", "items": [
        {"label": "Baseline", "sub": "Before", "icon": "clipboard", "with": 0},
        {"label": "Still 33 s", "sub": "Day 30", "icon": "check", "with": "example"},
        {"label": "Still 33 s", "sub": "Day 90", "icon": "check", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Update SOP", "icon": "clipboard", "with": 0},
        {"label": "Train, remove old way", "icon": "person", "with": 1},
        {"label": "Owner and audit", "icon": "search", "tone": "good", "with": 2}]},
    "p14": {"type": "bars", "label": "", "note": "Suresh's team, first three months", "with": "example", "items": [
        {"label": "Ideas", "value": 40, "with": "example"},
        {"label": "Tested", "value": 27, "with": "example"},
        {"label": "Standardized", "value": 19, "tone": "good", "with": "example"}]},
    "p15": {"type": "steps", "items": [
        {"label": "One recurring pain", "with": 0},
        {"label": "Ten cycles, talk to the team", "with": 1},
        {"label": "Smallest safe fix", "with": 2},
        {"label": "Standardize", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which is the best Kaizen problem statement?",
        "options": ["“We need a robot arm on the monitor line”",
                    "“Cycle time is 38 s vs a 35 s TAKT, with 2 flips per unit; reach 35 s in 4 weeks”",
                    "“Operators are too slow”"],
        "correct": 1,
        "explanation": "A good statement has the measured gap, the observed loss and a target with a deadline, without naming a solution or blaming people.",
        "q_script": "Quick check. Which of these is the best Kaizen problem statement? Take a few seconds.",
        "a_script": "It's the second one. It has the measured gap, the observed loss, and a target with "
                    "a deadline. The others are a solution and a blame.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A trial cuts cycle time by 4 seconds, but operators report shoulder strain. What now?",
        "options": ["Standardize it: the target improved",
                    "Treat it as not yet successful: adapt the method and re-test",
                    "Rotate operators every hour and keep it"],
        "correct": 1,
        "explanation": "The balanced rule: a Kaizen succeeds only if safety, quality and people don't suffer. Strain means the method needs changing before it becomes the standard.",
        "q_script": "One more, and this one's a scenario. A trial cuts cycle time by four seconds. But "
                    "operators report shoulder strain. What should the team do? Have a think.",
        "a_script": "It isn't a success yet. Adapt the method and test again. A Kaizen only counts when "
                    "safety and people don't pay for the gain.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
