"""Burn Down Chart lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Sneha,
a production supervisor on a Wi-Fi router line, clearing 1,000 routers of
work in progress in five days before the dispatch truck, with a burn-down chart.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/burn_down_chart.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py burn_down_chart  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "bd"
NAME = "burn_down_chart"

LETTERS = ["RF"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    return re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)


INTRO_SCRIPT = (
    "Last month, the truck left with eighty routers missing. Nobody saw it coming, until "
    "Friday afternoon. Sound familiar? In this lesson, you'll learn the Burn Down Chart. "
    "You'll see how to track the work that's left. You'll spot a delay on day two, not "
    "day five, and recover in time. We'll follow Sneha, a production supervisor on a Wi-Fi "
    "router line, as she makes sure it never happens again."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Draw the ideal line first, and never redraw it to look "
    "better. Count only work that's truly complete and good. And when the line rises above "
    "ideal, act that same day, with an owner. Here's your action for this week. Pick one job "
    "with a deadline, and draw its burn-down chart before tomorrow's shift. Great work "
    "completing this lesson. Next, you'll learn the Cycle Time Study."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What a Burn-Down Shows",
        "points": [("Work left vs time available", "how much work is left"),
                   ("Up: work remaining. Across: time", "The vertical axis"),
                   ("The line falls toward zero", "the line should fall")],
        "example": "Sneha's chart: a whiteboard beside the line, visible to every shift.",
        "example_cue": "Sneha draws hers",
        "script": "Here's the idea. A burn-down chart shows how much work is left, against the time "
                  "you have. The vertical axis is work remaining. The horizontal axis is time. As "
                  "your team finishes work, the line should fall toward zero. That's it. Simple, but "
                  "powerful. Sneha draws hers on a whiteboard beside the line, so every shift can see "
                  "it. So why does Lean love such a simple chart?",
    },
    {
        "key": "p02", "num": 2, "title": "Why Lean Uses It",
        "points": [("A target becomes a visible path", "turns a target into a path"),
                   ("See a gap while it's small", "You see a gap"),
                   ("Focus on the constraint", "focus your people")],
        "example": "Last month: only a due date. The gap showed up on Friday afternoon.",
        "example_cue": "Last month, Sneha",
        "script": "Because it turns a target into a path you can see. A due date alone tells you "
                  "nothing, until it's missed. A burn-down shows you every day whether you're on "
                  "track. You see a gap while it's still small. And you can focus your people on the "
                  "one constraint that's stopping closure. Last month, Sneha only had a due date. She "
                  "found the gap on Friday. What would two extra days have been worth to you?",
    },
    {
        "key": "p03", "num": 3, "title": "What It's For",
        "points": [("Remaining work visible to everyone", "makes the remaining work visible"),
                   ("Actual progress vs required pace", "It compares real progress"),
                   ("Catch delays early", "It catches delays early"),
                   ("Recovery backed by facts", "backs your recovery actions")],
        "example": "The goal: every planned unit reaches zero by the due date.",
        "example_cue": "The goal is simple",
        "script": "So what does a burn-down actually do for you? It makes the remaining work visible "
                  "to the whole team, not just the planner. It compares real progress with the pace "
                  "you need. It catches delays early, while recovery is still cheap. And it backs your "
                  "recovery actions with facts, not feelings. The goal is simple. Every planned unit "
                  "reaches zero by the due date. Let's look at what's on the chart.",
    },
    {
        "key": "p04", "num": 4, "title": "The Five Elements",
        "points": [("Axes: work remaining, time", "The vertical axis"),
                   ("Ideal line: the pace you need", "The ideal line"),
                   ("Actual line: what really happened", "The actual line"),
                   ("Gap: actual minus ideal", "the gap is")],
        "example": "Sneha tracks routers still waiting to finish, day by day.",
        "example_cue": "Sneha tracks routers",
        "script": "A burn-down has five parts. The vertical axis is work remaining, in units, defects, "
                  "actions or hours. The horizontal axis is time, in shifts, days or weeks. The ideal "
                  "line is the pace you need. The actual line is what really happened. And the gap is "
                  "the distance between them. Sneha tracks routers still waiting to finish, day by "
                  "day. Which unit would you count on your line?",
    },
    {
        "key": "p05", "num": 5, "title": "Sneha's Challenge",
        "points": [("1,000 routers in work in progress", "One thousand routers"),
                   ("5 working days to the truck", "The truck leaves"),
                   ("Remaining = planned − completed", "Remaining work equals")],
        "example": "Day 0: nothing completed, 1,000 routers remaining.",
        "example_cue": "On day zero",
        "script": "Here's Sneha's challenge this month. One thousand routers are stuck in work in "
                  "progress. They still need final test and packing, and only good units count. The "
                  "truck leaves in five working days. The math starts simple. Remaining work equals "
                  "total planned work, minus what you've completed so far. On day zero, nothing is "
                  "done, so all one thousand remain. Can you guess the pace she needs each day?",
    },
    {
        "key": "p06", "num": 6, "title": "The Ideal Burn Rate",
        "points": [("Rate = total work ÷ periods", "total work divided"),
                   ("1,000 ÷ 5 = 200 a day", "Two hundred a day"),
                   ("Draw it first, never redraw it", "Draw it before")],
        "example": "Ideal line: 1,000 → 800 → 600 → 400 → 200 → 0",
        "example_cue": "So her ideal line",
        "script": "The ideal burn rate is total work divided by the periods you have. For Sneha, "
                  "that's one thousand routers over five days. Two hundred a day. So her ideal line "
                  "falls to zero in five equal steps. That straight line is her plan. Draw it before "
                  "work starts, and never redraw it to look better. If you move the plan, you hide "
                  "the gap. Now, what happened after two days?",
    },
    {
        "key": "p07", "num": 7, "title": "Day Two: Finding the Gap",
        "points": [("Completed: 320", "Her team has completed"),
                   ("Remaining: 680. Ideal: 600", "So six hundred and eighty"),
                   ("Gap: 80 behind plan", "The gap is"),
                   ("Three days to recover, quality intact", "She has three days")],
        "example": "Spotted on Tuesday, not Friday.",
        "example_cue": "she knows on Tuesday",
        "script": "At the end of day two, Sneha updates her chart. Her team has completed three "
                  "hundred and twenty routers. So six hundred and eighty remain. But her ideal line "
                  "says six hundred should remain. The gap is eighty routers behind plan. Is that a "
                  "disaster? No, but it's a signal. She has three days to recover it, without cutting "
                  "corners on quality. And she knows on Tuesday, not Friday.",
    },
    {
        "key": "p08", "num": 8, "title": "Reading the Lines",
        "points": [("Above ideal: behind. Find the constraint", "actual line sits above"),
                   ("Below ideal: ahead. Confirm quality", "If it sits below"),
                   ("Ahead with bad units isn't ahead", "Being ahead with bad")],
        "example": "Sneha's line sits above the ideal. What's stopping routers from finishing?",
        "example_cue": "Sneha's line was above",
        "script": "So how do you read the lines? If the actual line sits above the ideal, more work "
                  "remains than planned. Find the constraint, and assign a recovery action. If it sits "
                  "below, you're ahead. Great, but confirm quality, and sustain the pace. Being ahead "
                  "with bad units isn't being ahead at all. Sneha's line was above. So her question was "
                  "simple. What's stopping routers from finishing? What would you check first?",
    },
    {
        "key": "p09", "num": 9, "title": "Flat Lines & Reaching Zero",
        "points": [("Flat line: nothing closed", "A flat line means"),
                   ("Check stoppage, owner, data", "So check for a stoppage"),
                   ("At zero: verify, then close", "when the line reaches zero")],
        "example": "Wednesday: Sneha's line went flat for a whole shift.",
        "example_cue": "On Wednesday",
        "script": "Two more patterns matter. A flat line means nothing closed. Either work stopped, or "
                  "nobody updated the chart. Sometimes both. So check for a stoppage, check the owner, "
                  "and check the data. And when the line reaches zero? Don't just celebrate. Verify "
                  "that every unit meets the acceptance criteria, then formally close it. On Wednesday, "
                  "Sneha's line went flat for a whole shift. Can you guess why?",
    },
    {
        "key": "p10", "num": 10, "title": "The Daily Review",
        "points": [("Update and compare", "Update, by recording"),
                   ("Explain the main cause", "Explain the main cause"),
                   ("Act: an owner and a due time", "Act, with an owner"),
                   ("Confirm at the next update", "Then confirm")],
        "example": "Sneha runs the review in 10 minutes, at the start of every shift.",
        "example_cue": "Sneha runs this",
        "script": "Before we find out, here's the habit that catches it. A chart only helps if you "
                  "review it the same way every day. Update, by recording what's completed and recalculating what's left. Compare "
                  "actual with ideal. Explain the main cause of any bad gap. Act, with an owner and a "
                  "due time. Then confirm, at the next update, that the line is bending back. Sneha "
                  "runs this in ten minutes, at the start of every shift. Could you?",
    },
    {
        "key": "p11", "num": 11, "title": "Sneha's Recovery",
        "points": [("Constraint: one RF tester down", "One RF test station"),
                   ("Second tester, priority staffing", "A technician brought"),
                   ("One named owner updates the chart", "She named one owner")],
        "example": "Friday: zero routers remaining, a few hours before the truck.",
        "example_cue": "By Friday",
        "script": "So here's what Wednesday's flat line meant. One RF test station was down for "
                  "calibration. Routers piled up in front of it. And nobody updated the chart, because "
                  "nobody was named to. Sneha fixed both. A technician brought a second tester online, "
                  "and test got priority staffing. She named one owner to update the chart at a fixed "
                  "time. By Friday, the line touched zero, a few hours before the truck. Where else "
                  "could you use this?",
    },
    {
        "key": "p12", "num": 12, "title": "Where to Use It",
        "points": [("A clear start, a clear finish, a deadline", "whenever work has"),
                   ("Production: work in progress, recovery", "Clear work in progress"),
                   ("Quality: critical defects to zero", "Close every critical"),
                   ("Maintenance and kaizen actions", "Finish open maintenance")],
        "example": "Sneha's quality team now burns down open defects to zero before shipment.",
        "example_cue": "Sneha's quality team",
        "script": "Burn-downs aren't just for production. Use one whenever work has a clear starting "
                  "quantity, a clear finish, and a deadline. Clear work in progress before a changeover. "
                  "Recover a shortfall before the dispatch cut-off. Close every critical defect before "
                  "shipment. Finish open maintenance actions, or kaizen tasks, before a review. Sneha's "
                  "quality team now burns down open defects too. What has a deadline on your floor "
                  "this week?",
    },
    {
        "key": "p13", "num": 13, "title": "Honest Data",
        "points": [("One unit, a frozen starting quantity", "Use one unit"),
                   ("Define “complete” before you start", "Define exactly when"),
                   ("Count only good output", "count only output")],
        "example": "Routers waiting for retest: not counted as complete.",
        "example_cue": "On Thursday",
        "script": "A chart is only as honest as its data. Use one unit of measure all the way through. "
                  "Freeze the starting quantity, unless a scope change is approved. Define exactly when "
                  "something counts as complete. And count only output that meets quality. On Thursday, "
                  "Sneha's team wanted to count routers waiting for retest. She said no. Half-done isn't "
                  "done, and a failed unit isn't done either. Would you have counted them?",
    },
    {
        "key": "p14", "num": 14, "title": "Common Mistakes",
        "points": [("Changing the starting quantity", "Changing the starting quantity"),
                   ("Late or irregular updates", "Late updates"),
                   ("Counting partial or rejected units", "Counting partial work"),
                   ("A chart with no actions", "A chart with no actions")],
        "example": "Sneha logs approved scope changes in a separate box beside her chart.",
        "example_cue": "Sneha logs approved",
        "script": "Watch for a few common mistakes. Changing the starting quantity hides the original "
                  "gap. Late updates mean you react after the delay has grown. Counting partial work, "
                  "or rejected units, makes progress look better than it is. And a chart with no "
                  "actions is just a report. Sneha logs approved scope changes in a separate box beside "
                  "her chart. The original gap stays visible. Which mistake have you seen before?",
    },
    {
        "key": "p15", "num": 15, "title": "Strengths, Limits & Checklist",
        "points": [("Simple, fast, an early warning", "A burn-down is simple"),
                   ("Won't find the root cause by itself", "it won't explain"),
                   ("Define, confirm, calculate, name an owner", "here's your checklist"),
                   ("Update, act, close only at zero", "Then update")],
        "example": "Sneha pins this checklist beside every new chart.",
        "example_cue": "Sneha pins this",
        "script": "So what's the verdict? A burn-down is simple, quick to read, and it warns you before "
                  "the due date. But it won't explain the root cause by itself. And it depends on "
                  "honest, timely updates. So here's your checklist. Define the work, and what complete "
                  "means. Confirm the starting quantity and the date. Calculate the ideal rate, and name "
                  "an owner. Then update, act, and close only at zero. Sneha pins this checklist beside "
                  "every new chart.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Work left", "icon": "stack", "with": 0},
        {"label": "Time available", "icon": "clock", "with": 1},
        {"label": "Falls to zero", "icon": "chartDown", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Only a due date", "sub": "Gap found on Friday", "icon": "calendar", "tone": "bad", "with": "example"},
        {"label": "A burn-down", "sub": "Gap seen while it's small", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p03": {"type": "icons", "items": [
        {"label": "Visible to all", "icon": "search", "with": 0},
        {"label": "Actual vs pace", "icon": "scale", "with": 1},
        {"label": "Early warning", "icon": "warning", "with": 2},
        {"label": "Facts, not feelings", "icon": "clipboard", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Work remaining", "sub": "Vertical axis", "icon": "stack", "with": 0},
        {"label": "Time", "sub": "Horizontal axis", "icon": "calendar", "with": 0},
        {"label": "Ideal line", "icon": "chartDown", "with": 1},
        {"label": "Actual line", "icon": "pin", "with": 2},
        {"label": "Gap", "icon": "scale", "tone": "bad", "with": 3}]},
    "p05": {"type": "stat", "value": 1000, "icon": "box", "label": "routers in work in progress",
            "unit": "5 working days to the truck", "with": 0},
    "p06": {"type": "bars", "label": "", "note": "Ideal line: 200 fewer routers each day", "with": "example", "items": [
        {"label": "Day 0", "value": 1000, "with": "example"},
        {"label": "Day 1", "value": 800, "with": "example"},
        {"label": "Day 2", "value": 600, "with": "example"},
        {"label": "Day 3", "value": 400, "with": "example"},
        {"label": "Day 4", "value": 200, "with": "example"},
        {"label": "Day 5", "value": 0, "tone": "good", "with": "example"}]},
    "p07": {"type": "bars", "label": "", "note": "Routers remaining, end of day 2: 80 behind plan", "items": [
        {"label": "Ideal", "value": 600, "tone": "good", "with": 1},
        {"label": "Actual", "value": 680, "tone": "bad", "with": 1}]},
    "p08": {"type": "versus", "items": [
        {"label": "Above ideal", "sub": "Behind: find the constraint", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "Below ideal", "sub": "Ahead: confirm quality", "icon": "chartDown", "tone": "good", "with": 1}]},
    "p09": {"type": "flow", "items": [
        {"label": "Flat line", "sub": "Nothing closed", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Stoppage? Owner? Data?", "icon": "search", "with": 1},
        {"label": "At zero: verify, close", "icon": "check", "tone": "good", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Update", "with": 0}, {"label": "Compare", "with": 0},
        {"label": "Explain", "with": 1}, {"label": "Act", "with": 2},
        {"label": "Confirm", "with": 3}]},
    "p11": {"type": "flow", "items": [
        {"label": "RF tester down", "icon": "test", "tone": "bad", "with": 0},
        {"label": "Second tester online", "icon": "wrench", "with": 1},
        {"label": "One chart owner", "icon": "person", "with": 2}],
        "then": {"type": "stat", "value": 0, "icon": "check", "label": "routers remaining on Friday",
                 "unit": "a few hours before the truck", "with": "example"}},
    "p12": {"type": "icons", "items": [
        {"label": "Work in progress", "icon": "box", "with": 1},
        {"label": "Shortfall recovery", "icon": "chartUp", "with": 1},
        {"label": "Critical defects", "icon": "warning", "with": 2},
        {"label": "Maintenance, kaizen", "icon": "wrench", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "One unit, frozen start", "icon": "lock", "with": 0},
        {"label": "“Complete” defined", "icon": "clipboard", "with": 1},
        {"label": "Good output only", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Waiting for retest", "sub": "Not complete", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Passed and packed", "sub": "Counts", "icon": "check", "tone": "good", "with": "example"}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Moved start quantity", "icon": "stack", "tone": "bad", "with": 0},
        {"label": "Late updates", "icon": "clock", "tone": "bad", "with": 1},
        {"label": "Partial or rejected", "icon": "trash", "tone": "bad", "with": 2},
        {"label": "No actions", "icon": "cross", "tone": "bad", "with": 3}]},
    "p15": {"type": "doc", "items": [
        {"label": "Define the work and “complete”", "icon": "clipboard", "with": 2},
        {"label": "Confirm start quantity and date", "icon": "calendar", "with": 2},
        {"label": "Ideal rate, one owner", "icon": "person", "with": 2},
        {"label": "Update, act, close only at zero", "icon": "check", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "800 units must be cleared in 4 days. After day 2, 340 are done. Where is the team?",
        "options": ["60 units ahead of plan", "60 units behind plan", "Exactly on plan"],
        "correct": 1,
        "explanation": "Ideal remaining at day 2 = 800 − 2 × 200 = 400. Actual remaining = 800 − 340 = 460. 460 − 400 = 60 behind plan.",
        "q_script": "Quick check. Eight hundred units must be cleared in four days. After day two, "
                    "three hundred and forty are done. Where is the team? Take a few seconds.",
        "a_script": "They're sixty units behind. Four hundred should remain, but four hundred and "
                    "sixty still do. The actual line sits above the ideal.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A defect burn-down has been flat for two days. What should the team check first?",
        "options": ["Nothing: a flat line means things are stable",
                    "Whether work stopped, who owns it, and whether the data was updated",
                    "Redraw the ideal line to match reality"],
        "correct": 1,
        "explanation": "A flat line means nothing closed. Check for a stoppage, the owner and the data. Redrawing the ideal line only hides the gap.",
        "q_script": "One more, and this one's a scenario. A defect burn-down has been flat for two "
                    "days. What should the team check first? Have a think.",
        "a_script": "Check whether work stopped, who owns it, and whether anyone updated the data. "
                    "Redrawing the ideal line would only hide the gap.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
