"""Hancho (shop-floor leadership) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Sunita,
newly appointed Hancho (team leader) on an LED TV assembly line, running the
daily leadership cycle and recovering an output drop within the same shift.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/hancho.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py hancho  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "hc"
NAME = "hancho"

LETTERS = ["SOP", "OJT", "FPY", "LED", "TV"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. Hancho (班長, hanchō) = "HAHN-cho", like
# the English "honcho" (Merriam-Webster, Alphadictionary); one token, so captions map.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = re.sub(r"\bTAKT\b", "tact", text)
    return re.sub(r"\bHancho\b", "Hahn-cho", text)


INTRO_SCRIPT = (
    "Last month, the line ran twenty TVs an hour short, for a whole shift. Nobody noticed "
    "until the next morning's report. By then, the loss was history. Sound familiar? In this "
    "lesson, you'll learn Hancho, leadership right on the shop floor. You'll see how a team "
    "leader spots a gap in the first hour, and fixes it before the shift ends. We'll follow "
    "Sunita, a new Hancho on an LED TV line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Lead from the gemba, comparing the standard with what's "
    "actually happening. Make every gap visible, every hour, and react the same shift. And "
    "build your people, so the line doesn't depend on you. Here's your action for this week. "
    "Write your own leader standard work, for one shift. Great work completing this lesson. "
    "Next, you'll learn the Ishikawa diagram."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What a Hancho Is",
        "points": [("Japanese for team leader", "is Japanese for"),
                   ("A leadership system, not a tool", "It isn't a tool"),
                   ("Leads where the value is made", "who leads right")],
        "example": "Sunita: twelve operators, one LED TV line, every shift's results.",
        "example_cue": "Sunita leads",
        "script": "Hancho is Japanese for team leader, or first-line leader. It isn't a tool you fill "
                  "in. It's a leadership system, built around one person who leads right where the "
                  "value is made. Close to the operators, close to the process, and close to the "
                  "problems. Sunita leads twelve operators on an LED TV line. She owns the results of "
                  "every shift. So how does a Hancho think?",
    },
    {
        "key": "p02", "num": 2, "title": "The Hancho Mindset",
        "points": [("What's the standard? What's actual?", "What's the standard"),
                   ("Where's the gap, and why?", "Where's the gap"),
                   ("Act now, then stop it repeating", "What do we do right now")],
        "example": "Sunita keeps these questions on a card in her pocket.",
        "example_cue": "Sunita keeps",
        "script": "A Hancho asks the same questions, every time. What's the standard? What's actually "
                  "happening? Where's the gap, and what caused it? What do we do right now, and what "
                  "must change so it never repeats? Notice there's no blame in any of them. Just "
                  "standard, actual, gap and action. Sunita keeps these questions on a small card in "
                  "her pocket. Why does a line need this role?",
    },
    {
        "key": "p03", "num": 3, "title": "Why Lines Need a Hancho",
        "points": [("Small gaps grow when leaders are far away", "When leaders are far"),
                   ("Faster response, clear ownership", "A Hancho means"),
                   ("Daily kaizen, not just projects", "And improvement happens")],
        "example": "Last month: a 20-TV-an-hour gap, found the next morning.",
        "example_cue": "Remember last",
        "script": "When leaders are far from the process, small gaps grow. A loose fixture becomes "
                  "downtime. A few defects become a customer complaint. A Hancho means faster response, "
                  "and clear ownership on every shift. Standards get followed, because someone checks. "
                  "And improvement happens every day, not just in special projects. Remember last "
                  "month's gap, found the next morning? What exactly does a Hancho own?",
    },
    {
        "key": "p04", "num": 4, "title": "What a Hancho Owns",
        "points": [("Safety and quality", "Safety comes first"),
                   ("Delivery and cost", "Delivery means"),
                   ("People and the process", "And people")],
        "example": "Sunita's rule: solve it, call support, or escalate. Know which.",
        "example_cue": "Sunita learned",
        "script": "A Hancho owns six areas. Safety comes first, then quality, by protecting the "
                  "standard and containing defects. Delivery means tracking plan against actual, every "
                  "hour. Cost means cutting scrap, rework and downtime. And people, and the process, "
                  "through training, standard work and line readiness. Sunita learned one more thing. "
                  "Know when to solve it, when to call support, and when to escalate. How does her day "
                  "start?",
    },
    {
        "key": "p05", "num": 5, "title": "Before the Shift Starts",
        "points": [("Pre-shift readiness check", "First, readiness"),
                   ("A short team briefing", "Then a short briefing"),
                   ("Start-up and first-piece checks", "Then start-up checks")],
        "example": "Today's briefing: a model change to the 43-inch TV at 10 o'clock.",
        "example_cue": "Today's briefing",
        "script": "Sunita's day starts before the line does. First, readiness. Are the people, "
                  "materials, machines, tools and documents ready? Then a short briefing. The target, "
                  "quality alerts, safety points, and what the last shift learned. Then start-up "
                  "checks, including the first piece. Today's briefing had one big point. A model "
                  "change to the forty-three inch TV at ten o'clock. What happens once the line runs?",
    },
    {
        "key": "p06", "num": 6, "title": "During and After the Shift",
        "points": [("Hourly plan vs actual", "Every hour"),
                   ("React to every abnormality", "She reacts"),
                   ("Coach at the process", "She coaches"),
                   ("A factual handover", "At the end")],
        "example": "Handover note: open issues, WIP, quality status, actions and owners.",
        "example_cue": "Her handover",
        "script": "Every hour, she compares plan with actual. Output, first pass yield, downtime and "
                  "work in progress. She reacts to every abnormality, and records it. She coaches "
                  "operators at the process, not in a meeting room. At the end, she hands over to the "
                  "next shift with facts, not memories. Her handover covers open issues, quality status, "
                  "actions and owners. Where does she spend most of her time?",
    },
    {
        "key": "p07", "num": 7, "title": "Leading at the Gemba",
        "points": [("Watch the real process and product", "She watches"),
                   ("Talk with the operator", "She talks"),
                   ("Ask questions, don't just give answers", "She asks questions")],
        "example": "“What should be happening? What's actually happening? What changed?”",
        "example_cue": "Her favorite three",
        "script": "At the gemba, not at a desk. She watches the real process and the real product. She "
                  "talks with the operator who does the work. She compares the actual method with the "
                  "standard. And she asks questions that build thinking, instead of handing out every "
                  "answer. Her favorite three are simple. What should be happening? What's actually "
                  "happening? And what changed? Which would you ask first?",
    },
    {
        "key": "p08", "num": 8, "title": "Leader Standard Work",
        "points": [("Checks by frequency", "lists her checks"),
                   ("Sequence, cycle time, quality points", "She checks"),
                   ("Latest SOP at every station", "And the latest SOP")],
        "example": "Sunita's list: start of shift, every hour, every model change, end of shift.",
        "example_cue": "Her list runs",
        "script": "A Hancho needs standard work too. Leader standard work lists her checks, by how often "
                  "they happen. She checks the work sequence, the cycle time against TAKT, and the "
                  "quality points. She checks tools and fixtures are right. And the latest SOP must be "
                  "at every station, and understood. Her list runs at the start of shift, every hour, "
                  "every model change, and at the end. What would yours include?",
    },
    {
        "key": "p09", "num": 9, "title": "Visual Management",
        "points": [("Plan vs actual, every hour", "Plan against actual"),
                   ("Quality, downtime, open actions", "First pass yield"),
                   ("See, react, record, follow up", "Every red number")],
        "example": "10 to 11 a.m.: plan 120 TVs, actual 98. Red.",
        "example_cue": "At eleven o'clock",
        "script": "Make the line readable at a glance. Plan against actual, every hour. First pass "
                  "yield, top defects, downtime reasons, and open actions with owners. But a board isn't "
                  "decoration. Every red number must trigger a response. See it, react, record it, and "
                  "follow up. At eleven o'clock, Sunita's board turned red. Plan, a hundred and twenty "
                  "TVs. Actual, ninety-eight. What should she do first?",
    },
    {
        "key": "p10", "num": 10, "title": "Abnormality Response",
        "points": [("Detect, contain, call", "Detect the gap"),
                   ("Correct and confirm", "Correct the process"),
                   ("Prevent and share", "Then prevent it")],
        "example": "Level 1: team fixes it. Level 2: call support. Level 3: escalate to management.",
        "example_cue": "There are three levels",
        "script": "Follow a clear response. Detect the gap, contain it to protect the customer, and "
                  "call the right support. Correct the process, and confirm the output is good again. "
                  "Then prevent it, and share what you learned. There are three levels. Level one, the "
                  "team fixes it. Level two, call quality, engineering or maintenance. Level three, "
                  "safety or customer risk, escalate now. Which level was Sunita's?",
    },
    {
        "key": "p11", "num": 11, "title": "Sunita's Red Hour",
        "points": [("Output: 98 against 120 an hour", "Output had dropped"),
                   ("First pass yield: 98.5% to 95.8%", "First pass yield"),
                   ("Work piling up before test", "And work was piling")],
        "example": "It started right after the 10 o'clock model change.",
        "example_cue": "It all started",
        "script": "Here's what she saw. Output had dropped to ninety-eight TVs an hour, against a plan "
                  "of a hundred and twenty. First pass yield had fallen by almost three "
                  "points. And work was piling up in front of the test station. Three numbers, all moving the wrong way. "
                  "It all started right after the ten o'clock model change. Would you go to the test "
                  "station first?",
    },
    {
        "key": "p12", "num": 12, "title": "Contain, Then Go and See",
        "points": [("Hold the suspect TVs", "she held"),
                   ("Find the bottleneck station", "found the bottleneck"),
                   ("Compare method with standard", "compared the method")],
        "example": "Station 6: on the new model, the panel cable took a new path, and operators bent it by hand.",
        "example_cue": "At station six",
        "script": "Not yet. First, she held every suspect TV since ten o'clock. Customer protected. Then "
                  "she walked the line, and found the bottleneck before test. She compared the method "
                  "with the standard, at each station. At station six, the new model's panel cable took "
                  "a different path. The fixture still guided the old path. So operators bent the cable "
                  "by hand, and some didn't seat. Was this level one?",
    },
    {
        "key": "p13", "num": 13, "title": "Call, Correct, Confirm",
        "points": [("Level 2: call engineering", "She called engineering"),
                   ("Correct the fixture, update the SOP", "adjusted the cable guide"),
                   ("Confirm over several cycles", "confirmed it")],
        "example": "By 1 p.m.: 120 TVs an hour, first pass yield 98.6%.",
        "example_cue": "By one o'clock",
        "script": "It was level two. She called engineering, with facts, photos and the failed units. "
                  "Engineering adjusted the cable guide for the new model, and the SOP was updated. "
                  "Sunita confirmed it over several cycles, not just one good TV. By one o'clock, the "
                  "line was back to a hundred and twenty an hour. First pass yield was ninety-eight "
                  "point six. Who made sure every shift knew?",
    },
    {
        "key": "p14", "num": 14, "title": "Building People",
        "points": [("Explain, show, practice, verify", "Explain, demonstrate"),
                   ("Certify critical skills", "Certify critical skills"),
                   ("Cross-train for cover", "Cross-train")],
        "example": "Sunita trained two operators on the new cable routing before the night shift.",
        "example_cue": "Sunita trained",
        "script": "A Hancho builds capability, not dependency. Use a simple training rhythm. Explain, "
                  "demonstrate, let them practice, then verify. Certify critical skills before anyone "
                  "works alone. Cross-train, so one absence can't stop the line. And coach problem "
                  "solving, not just the job. Sunita trained two operators on the new cable routing, "
                  "before the night shift started. Could your line run without you?",
    },
    {
        "key": "p15", "num": 15, "title": "Measure It, Then Start",
        "points": [("KPIs hourly, daily, weekly", "Review output"),
                   ("Audit to coach, not to blame", "Audit to coach"),
                   ("A 30-day plan", "Here's a thirty-day plan")],
        "example": "Week 1 roles · week 2 hourly board · week 3 skills · week 4 audit and review.",
        "example_cue": "Here's a thirty-day plan",
        "script": "Measure both results and discipline. Review output and downtime hourly, quality "
                  "daily, and skills and kaizen weekly. A green number without discipline won't last. "
                  "Audit to coach your team, not to catch people out. Here's a thirty-day plan. Week "
                  "one, define roles and leader standard work. Week two, launch the hourly board. Week "
                  "three, skills and coaching. Week four, audit and review. Which week will you start?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Team leader", "sub": "班長", "icon": "person", "with": 0},
        {"label": "A system", "icon": "gear", "with": 1},
        {"label": "At the gemba", "icon": "walk", "tone": "good", "with": 2}]},
    "p02": {"type": "steps", "items": [
        {"label": "Standard?", "with": 0}, {"label": "Actual?", "with": 0},
        {"label": "Gap and cause?", "with": 1}, {"label": "Act and prevent", "with": 2}]},
    "p03": {"type": "versus", "items": [
        {"label": "Leader far away", "sub": "Gap found next morning", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Hancho on the line", "sub": "Gap found this hour", "icon": "person", "tone": "good", "with": 1}]},
    "p04": {"type": "icons", "items": [
        {"label": "Safety", "icon": "shield", "with": 0},
        {"label": "Quality", "icon": "check", "with": 0},
        {"label": "Delivery", "icon": "calendar", "with": 1},
        {"label": "Cost", "icon": "scale", "with": 1},
        {"label": "People", "icon": "person", "with": 2},
        {"label": "Process", "icon": "clipboard", "with": 2}]},
    "p05": {"type": "flow", "items": [
        {"label": "Readiness", "sub": "People, material, tools", "icon": "clipboard", "with": 0},
        {"label": "Briefing", "sub": "Target, alerts, learning", "icon": "person", "with": 1},
        {"label": "Start-up checks", "sub": "First piece", "icon": "check", "tone": "good", "with": 2}]},
    "p06": {"type": "timeline", "items": [
        {"label": "Plan vs actual", "sub": "Hourly", "icon": "clock", "with": 0},
        {"label": "React, coach", "sub": "All shift", "icon": "hand", "with": 1},
        {"label": "Handover", "sub": "End of shift", "icon": "clipboard", "tone": "good", "with": 3}]},
    "p07": {"type": "icons", "items": [
        {"label": "Watch", "icon": "search", "with": 0},
        {"label": "Talk", "icon": "person", "with": 1},
        {"label": "Ask, don't tell", "icon": "key", "tone": "good", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "Start of shift: readiness", "icon": "calendar", "with": "example"},
        {"label": "Hourly: plan vs actual", "icon": "clock", "with": "example"},
        {"label": "Model change: first piece", "icon": "check", "with": "example"},
        {"label": "End of shift: handover", "icon": "clipboard", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "10–11 a.m.: plan vs actual", "with": "example", "items": [
        {"label": "Plan", "value": 120, "tone": "good", "with": "example"},
        {"label": "Actual", "value": 98, "tone": "bad", "with": "example"}]},
    "p10": {"type": "ladder", "top": "LEVEL 3", "bottom": "LEVEL 1", "items": [
        {"label": "Safety or customer risk: escalate now", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Call support functions", "icon": "person", "with": "example"},
        {"label": "Team restores the standard", "icon": "hand", "tone": "good", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "98 vs 120 an hour", "icon": "chartDown", "tone": "bad", "with": 0},
        {"label": "FPY 98.5% → 95.8%", "icon": "test", "tone": "bad", "with": 1},
        {"label": "WIP before test", "icon": "stack", "tone": "bad", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Hold suspect TVs", "icon": "lock", "with": 0},
        {"label": "Find the bottleneck", "icon": "search", "with": 1},
        {"label": "Station 6: cable path changed", "icon": "wrench", "tone": "bad", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "11 a.m.", "value": 98}, "after": {"label": "1 p.m.", "value": 120},
            "unit": "TVs an hour", "note": "First pass yield back to 98.6%", "with": "example"},
    "p14": {"type": "steps", "items": [
        {"label": "Explain", "with": 0}, {"label": "Demonstrate", "with": 0},
        {"label": "Practice", "with": 0}, {"label": "Verify", "with": 1}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Roles, leader standard work", "sub": "Week 1", "icon": "clipboard", "with": 2},
        {"label": "Hourly board", "sub": "Week 2", "icon": "chartUp", "with": 2},
        {"label": "Skills, coaching", "sub": "Week 3", "icon": "person", "with": 2},
        {"label": "Audit, review", "sub": "Week 4", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A Hancho's job is mainly to…",
        "options": ["Fill in the shift report at the end of the day",
                    "Lead at the gemba: keep the standard, react to gaps, develop people",
                    "Do the hardest station personally, every shift"],
        "correct": 1,
        "explanation": "A Hancho leads where the value is made: protecting the standard, responding to abnormalities fast and building the team's capability. Reports and covering stations aren't the core of the role.",
        "q_script": "Quick check. What's a Hancho's main job? Take a few seconds.",
        "a_script": "It's the second one. Lead at the gemba. Keep the standard, react to gaps, and "
                    "develop your people.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "The hourly board turns red and suspect units may have a safety risk. Which response level?",
        "options": ["Level 1: the team fixes it quietly",
                    "Level 2: call maintenance when they're free",
                    "Level 3: contain and escalate to management immediately"],
        "correct": 2,
        "explanation": "Safety or customer risk is level 3: contain the units and escalate immediately. Don't wait to see if the team can handle it.",
        "q_script": "One more, and this one's a scenario. The hourly board turns red, and suspect units "
                    "may carry a safety risk. Which response level is it? Have a think.",
        "a_script": "It's level three. Contain the units, and escalate to management right away. Safety "
                    "risk never waits.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
