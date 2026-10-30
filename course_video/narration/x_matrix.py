"""X-Matrix / Hoshin Kanri lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Arjun,
operations head at an electronics plant (phones, set-top boxes, audio devices),
turning a busy project portfolio into a focused one.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/x_matrix.py                     voice MISSING clips (bootstrap)
  python narration/import_clones.py x_matrix       import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "xm"
NAME = "x_matrix"

LETTERS = ["KPI", "BOM", "SMED", "IT"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12, confirmed by the
# user); on-screen text and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = re.sub(r"\bRACI\b", "racey", text)
    return re.sub(r"\bHoshin Kanri\b", "Hoe-shin Kahn-ree", text)


INTRO_SCRIPT = (
    "Forty improvement projects. Every team busy. Yet delivery still slipped, quarter "
    "after quarter. Sound familiar? In this lesson, you'll learn the X-Matrix, the "
    "one-page heart of Hoshin Kanri. You'll see how to link a few big goals to the "
    "projects and numbers that prove them. We'll follow Arjun, operations head at an "
    "electronics plant, as he turns a busy portfolio into a focused one."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Pick a few real priorities, not a wish list. Link "
    "every goal to a project, a KPI, and one owner. And review honestly, because the "
    "numbers must move, not just the chart. Here's your action for this week. Write one "
    "objective for your area as an outcome, not an activity. Great work completing this "
    "lesson. Next, you'll learn Yamazumi, balancing the work on your line."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "X-Matrix & Hoshin Kanri",
        "points": [("Your whole strategy on one page", "puts your whole strategy"),
                   ("Objectives → goals → projects → targets → owners", "It links long-term objectives"),
                   ("A short list of real actions", "Its job is to turn"),
                   ("Not a chart for the wall", "It's not a colorful chart")],
        "example": "Arjun wants reliable delivery and fewer defects. Can he trace that goal to work on the floor?",
        "example_cue": "Arjun wants reliable delivery",
        "script": "Here's the core idea. The X-Matrix puts your whole strategy on one page. It links "
                  "long-term objectives, this year's goals, improvement projects, measurable "
                  "targets, and the owners behind them. Its job is to turn strategy into a short "
                  "list of real actions. It's not a colorful chart to hang on a wall. Arjun wants "
                  "reliable delivery and fewer defects. Can he trace that goal all the way to work "
                  "on the floor? First, where does the method come from?",
    },
    {
        "key": "p02", "num": 2, "title": "Origins & Alignment",
        "points": [("Hoshin Kanri: direction management", "Roughly, it means"),
                   ("Aligns direction with daily work", "It aligns where"),
                   ("Limit priorities to what you can resource", "So limit your priorities"),
                   ("Two-way, not top-down", "And keep the conversation")],
        "example": "Arjun's site ran dozens of local Kaizens — only a few truly helped customer delivery.",
        "example_cue": "His site ran dozens",
        "script": "Hoshin Kanri is a Japanese approach. Roughly, it means direction management. It "
                  "aligns where you're heading with what you actually do every day. The X-Matrix is "
                  "simply the picture of that alignment. Here's the trap Arjun found. His site ran "
                  "dozens of local Kaizens. Only a few truly helped customer delivery. So limit "
                  "your priorities to what you can resource. And keep the conversation two-way, "
                  "not top-down. Now, what goes on the page?",
    },
    {
        "key": "p03", "num": 3, "title": "Four Core Quadrants",
        "points": [("Breakthrough objectives: 3–5 years", "First, breakthrough objectives"),
                   ("Annual objectives: this year", "Second, annual objectives"),
                   ("Improvement projects", "Third, improvement projects"),
                   ("KPIs and targets: the proof", "Fourth, KPIs and targets")],
        "example": "Arjun's chain runs from world-class quality down to one yield target.",
        "example_cue": "Arjun's chain runs",
        "script": "A typical X-Matrix has four linked parts. First, breakthrough objectives, three "
                  "to five years out. Second, annual objectives, the progress you need this year. "
                  "Third, improvement projects, the work that changes performance. Fourth, KPIs "
                  "and targets, the proof it's working. Owners sit alongside, in a responsibility "
                  "grid. Layouts vary by template, so always add a legend. Arjun's chain runs from "
                  "world-class quality down to one yield target. Let's start at the top.",
    },
    {
        "key": "p04", "num": 4, "title": "Breakthrough Objectives",
        "points": [("A few big outcomes: 3 to 5", "Pick three to five"),
                   ("Result, horizon, today's baseline", "State the result"),
                   ("Check for goals that fight", "And check for goals")],
        "example": "Arjun's outcome: cut customer returns by two thirds, while output grows.",
        "example_cue": "Arjun wrote one clear outcome",
        "script": "Breakthrough objectives name a few big outcomes, beyond normal day-to-day "
                  "improvement. Pick three to five, not a wish list. State the result, the time "
                  "horizon, and today's baseline. And check for goals that fight each other, like "
                  "speed against safety. Arjun wrote one clear outcome. Cut customer returns by "
                  "two thirds, while output grows. Notice it's a result, not an activity. You can "
                  "measure it. So how do you break that into this year?",
    },
    {
        "key": "p05", "num": 5, "title": "Annual Objectives",
        "points": [("Measurable results for this year", "Annual objectives turn"),
                   ("Baseline, target, period, data source", "Define the baseline"),
                   ("Catchball: test feasibility together", "Then use catchball")],
        "example": "Year one: part of the returns drop, agreed after studying field failures.",
        "example_cue": "For year one",
        "script": "Annual objectives turn that direction into results you can measure this year. "
                  "Don't just hand out round percentages. Define the baseline, the target, the "
                  "period, and the data source. Keep the list short. Then use catchball. That's "
                  "the back-and-forth where teams test whether a target is really feasible. For "
                  "year one, Arjun aims for part of the drop, not all of it. His teams agreed it "
                  "after studying field failures. So which projects will get you there?",
    },
    {
        "key": "p06", "num": 6, "title": "Improvement Projects",
        "points": [("Problem, scope, owner, milestones, check", "A good one has"),
                   ("More inspection rarely = breakthrough", "Adding more inspection"),
                   ("Choose on evidence: impact vs effort", "Choose projects on evidence")],
        "example": "A barcode-to-BOM interlock blocks wrong components — success claimed only when tests and defect data agree.",
        "example_cue": "On Arjun's phone line",
        "script": "Projects are the changes that move your annual targets. A good one has a problem "
                  "statement, a scope, an owner, milestones, and a way to verify results. Here's a "
                  "common mistake. Adding more inspection rarely delivers a breakthrough. Choose "
                  "projects on evidence, and weigh impact against effort, cost, and risk. On "
                  "Arjun's phone line, a barcode-to-BOM interlock blocks wrong components. But he "
                  "only claims success when tests and defect data agree. How will you know it's "
                  "working?",
    },
    {
        "key": "p07", "num": 7, "title": "Leading & Lagging KPIs",
        "points": [("Lagging: results already got", "Lagging indicators measure"),
                   ("Leading: conditions that predict them", "Leading indicators measure"),
                   ("Define denominator and data source", "Define each one's denominator"),
                   ("Don't reward redefined numbers", "And never reward")],
        "example": "On Arjun's line, 98% of units pass first time.",
        "example_cue": "On Arjun's line",
        "script": "That's the job of KPIs. Lagging indicators measure results you've already got, "
                  "like first-pass yield, returns, and on-time delivery. Leading indicators measure "
                  "the conditions that predict them, like audits, setup checks, and training. You "
                  "need both. Define each one's denominator and data source. And never reward a "
                  "number that only improved because someone changed its definition. On Arjun's "
                  "line, ninety-eight percent of units pass first time. But how strongly does each "
                  "project drive each number?",
    },
    {
        "key": "p08", "num": 8, "title": "Correlation Strength",
        "points": [("Symbols show link strength", "The matrix uses symbols"),
                   ("Agree the legend first", "agree your legend first"),
                   ("Score the link, not importance", "Score the link"),
                   ("Look for gaps and over-claims", "Then look for gaps")],
        "example": "Arjun's fixture interlock strongly cuts wrong parts — and barely touches energy use.",
        "example_cue": "Arjun's fixture interlock",
        "script": "The matrix uses symbols to show how strongly two items are linked. Often a "
                  "filled circle means strong, and an open circle means moderate. No convention is "
                  "universal, so agree your legend first. Score the link, not how important the "
                  "item feels. Then look for gaps. Is there an annual goal with no project behind "
                  "it? Is there a project claiming to help everything? Arjun's fixture interlock "
                  "strongly cuts wrong parts. It barely touches energy use. So who makes sure it "
                  "happens?",
    },
    {
        "key": "p09", "num": 9, "title": "Ownership & Catchball",
        "points": [("One accountable owner each", "Give every objective"),
                   ("Name supporting teams", "Name the supporting teams"),
                   ("RACI: responsible, accountable, consulted, informed", "Who's responsible"),
                   ("Owner needs budget and authority", "Make sure your owner")],
        "example": "Set-top box test automation: Engineering, Production, Quality and IT help — one project leader stays accountable.",
        "example_cue": "On Arjun's set-top box",
        "script": "Goals fail when ownership is fuzzy. Give every objective and project one "
                  "accountable owner. Name the supporting teams too. That's the idea behind RACI. "
                  "Who's responsible, who's accountable, who's consulted, and who's informed? Make "
                  "sure your owner has the budget and authority to remove barriers. On Arjun's "
                  "set-top box test automation, Engineering, Production, Quality, and IT all help. "
                  "But one project leader stays accountable. If it stalls, you know who to ask.",
    },
    {
        "key": "p10", "num": 10, "title": "Construction Workshop",
        "points": [("Gather evidence first", "Before the workshop"),
                   ("Scope, baseline, objectives, outcomes", "Agree the scope"),
                   ("High-impact projects, each with a KPI", "Pick high-impact projects"),
                   ("Score links, assign owners, set reviews", "Finally, score the links")],
        "example": "In Arjun's workshop, three departments linked projects to one delivery target.",
        "example_cue": "In Arjun's workshop",
        "script": "Build the matrix from strategy down to real work. Before the workshop, gather "
                  "evidence on customers, performance, capacity, and cost. Then take it step by "
                  "step. Agree the scope and baseline. Choose a few breakthrough objectives. Define "
                  "this year's outcomes. Pick high-impact projects, and give each a KPI. Finally, "
                  "score the links, assign owners, and set a review rhythm. In Arjun's workshop, "
                  "three departments linked projects to one delivery target. What does your "
                  "finished matrix look like?",
    },
    {
        "key": "p11", "num": 11, "title": "Worked Example",
        "points": [("Delivery 90% → 98%", "on-time delivery goes"),
                   ("First-pass yield → 99%", "First-pass yield climbs"),
                   ("Changeover 50 → 20 minutes", "Changeover drops"),
                   ("Planning, Quality, Engineering own one each", "Planning owns delivery")],
        "example": "Projects: a readiness dashboard, a barcode interlock and a SMED pilot.",
        "example_cue": "The projects are",
        "script": "Here's Arjun's finished matrix. The numbers are training assumptions. His "
                  "breakthroughs are reliable delivery, defect prevention, and flexible capacity. "
                  "This year, on-time delivery goes from ninety to ninety-eight percent. First-pass "
                  "yield climbs to ninety-nine. Changeover drops from fifty minutes to twenty. The "
                  "projects are a readiness dashboard, a barcode interlock, and a SMED pilot. "
                  "Planning owns delivery, Quality owns yield, and Engineering owns changeover. Can "
                  "you see each line of sight?",
    },
    {
        "key": "p12", "num": 12, "title": "Review Cadence — PDCA",
        "points": [("A living tool: Plan, Do, Check, Act", "Review it with Plan"),
                   ("Daily / weekly: exceptions, milestones", "Daily and weekly"),
                   ("Monthly: KPI trends and risks", "Monthly, review"),
                   ("Quarterly: still supports strategy?", "Quarterly, ask")],
        "example": "Yield stalled even after training — so Arjun checked whether the process control really changed.",
        "example_cue": "Yield stalled",
        "script": "The X-Matrix is a living tool, not a poster. Review it with Plan, Do, Check, "
                  "Act. Compare results with targets, find the causes of gaps, and adapt. Daily and "
                  "weekly, track exceptions and milestones. Monthly, review KPI trends and risks. "
                  "Quarterly, ask whether each project still supports the strategy. Here's what "
                  "Arjun learned. Yield stalled even after training was finished. So he checked "
                  "whether the process control had really changed. What traps should you avoid?",
    },
    {
        "key": "p13", "num": 13, "title": "Do's & Don'ts",
        "points": [("A few measurable outcomes, clear owners", "So do keep a few"),
                   ("Check causal links and resources", "Do check the causal links"),
                   ("Not everything 'strongly linked'", "don't mark every project"),
                   ("Finished project ≠ delivered benefit", "Don't treat a finished project")],
        "example": "One project was marked complete, yet complaints held steady.",
        "example_cue": "One of Arjun's projects",
        "script": "A matrix turns into dead paperwork fast. Too many goals, vague words, and "
                  "unchecked links will do it. So do keep a few measurable outcomes with clear "
                  "owners. Do check the causal links and the resources behind them. But don't mark "
                  "every project as strongly linked to every KPI. Don't treat a finished project "
                  "as a delivered benefit. And never quietly rewrite a baseline. One of Arjun's "
                  "projects was marked complete, yet complaints held steady. How would you prove "
                  "real value?",
    },
    {
        "key": "p14", "num": 14, "title": "Cost–Benefit Math",
        "points": [("On-time delivery = on time ÷ total due", "On-time delivery is"),
                   ("Relative drop = drop ÷ old rate", "A relative reduction is"),
                   ("Payback = investment ÷ monthly savings", "Payback is")],
        "example": "Defects 2% → 1.2% sounds small — it's a 40% relative drop. The interlock pays back in 6 months.",
        "example_cue": "Defects falling from two",
        "script": "Benefits need consistent formulas, or nobody will trust them. On-time delivery "
                  "is on-time shipments over total due. A relative reduction is the drop divided "
                  "by the old rate. Payback is the investment divided by verified monthly savings. "
                  "Here's a trap you'll meet. Defects falling from two percent to one point two "
                  "sounds small. It's actually a forty percent relative drop. And Arjun's "
                  "interlock pays back in six months. So how do you start tomorrow?",
    },
    {
        "key": "p15", "num": 15, "title": "90-Day Roadmap",
        "points": [("Days 1–30: baselines, draft matrix", "In the first thirty days"),
                   ("Days 31–60: catchball, projects, owners", "In the next thirty"),
                   ("Days 61–90: check links, review, audit", "In the last thirty")],
        "example": "What outcome? Which target? Which project? Which KPI? Who owns the result?",
        "example_cue": "What outcome matters",
        "script": "Start with a pilot, and build the review habit before you spread it everywhere. "
                  "In the first thirty days, collect baselines and draft the matrix. In the next "
                  "thirty, run catchball, approve projects, and assign owners. In the last thirty, "
                  "check the links, review the gaps, and audit the result. Then ask your five "
                  "questions. What outcome matters? Which target supports it? Which project "
                  "changes the process? Which KPI proves it? And who owns the result?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Long-term objectives", "icon": "chartUp", "with": 1},
        {"label": "This year's goals", "icon": "calendar", "with": 1},
        {"label": "Improvement projects", "icon": "wrench", "with": 1},
        {"label": "Targets and owners", "icon": "person", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Direction management", "icon": "sequence", "with": 0},
        {"label": "Strategy meets daily work", "icon": "calendar", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Dozens of local Kaizens", "sub": "Few helped delivery", "icon": "stack", "with": "example"},
            {"label": "A few resourced priorities", "sub": "Two-way, not top-down", "icon": "key", "with": 2}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Breakthrough", "sub": "3–5 years", "icon": "chartUp", "with": 0},
        {"label": "Annual", "sub": "This year", "icon": "calendar", "with": 1},
        {"label": "Projects", "sub": "The work", "icon": "wrench", "with": 2},
        {"label": "KPIs & targets", "sub": "The proof", "icon": "check", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "3 to 5 big outcomes", "icon": "key", "with": 0},
        {"label": "Result, horizon, baseline", "icon": "clipboard", "with": 1},
        {"label": "Goals that fight", "sub": "Speed vs safety", "icon": "scale", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 2, "suffix": "/3", "icon": "chartDown", "label": "fewer customer returns",
                 "unit": "While output grows: a result, not an activity", "with": "example"}},
    "p05": {"type": "doc", "items": [
        {"label": "Annual objective · Year 1", "icon": "label", "with": 0},
        {"label": "Baseline · target · period", "icon": "clipboard", "with": 1},
        {"label": "Data source named", "icon": "search", "with": 1},
        {"label": "Catchball: is it feasible?", "icon": "sequence", "with": 2},
        {"label": "Agreed from field failures", "icon": "check", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Problem, scope, owner", "icon": "clipboard", "with": 0},
        {"label": "More inspection", "sub": "Rarely a breakthrough", "icon": "search", "tone": "bad", "with": 1},
        {"label": "Impact vs effort", "icon": "scale", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Scan the part barcode", "icon": "barcode", "with": "example"},
            {"label": "Check against the BOM", "icon": "clipboard", "with": "example"},
            {"label": "Wrong part? Blocked", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p07": {"type": "versus", "items": [
        {"label": "Lagging", "sub": "Yield, returns, delivery", "icon": "chartUp", "with": 0},
        {"label": "Leading", "sub": "Audits, setups, training", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 98, "suffix": "%", "icon": "check", "label": "pass first time",
                 "unit": "First-pass yield on Arjun's line", "with": "example"}},
    "p08": {"type": "matrix", "prefix": "check", "cols": ["Wrong parts", "Yield", "Energy"],
            "note": "Score the link, not the importance", "items": [
        {"label": "Interlock", "cells": [3, 3, None], "with": "example"},
        {"label": "SMED pilot", "cells": [None, None, 3], "with": "example"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Responsible", "icon": "wrench", "with": 2},
        {"label": "Accountable", "sub": "One owner", "icon": "person", "tone": "good", "with": 0},
        {"label": "Consulted", "icon": "search", "with": 2},
        {"label": "Informed", "icon": "clipboard", "with": 2}]},
    "p10": {"type": "steps", "items": [
        {"label": "Evidence", "with": 0}, {"label": "Scope, baseline", "with": 1},
        {"label": "Objectives", "with": 1}, {"label": "Projects + KPI", "with": 2},
        {"label": "Links, owners", "with": 3}, {"label": "Review rhythm", "with": 3}]},
    "p11": {"type": "compare", "before": {"label": "Today", "value": 90}, "after": {"label": "This year", "value": 98},
            "suffix": "%", "unit": "on-time delivery", "note": "Planning owns it", "with": 0,
            "then": {"type": "icons", "with": "example", "items": [
                {"label": "Readiness dashboard", "sub": "Delivery", "icon": "chartUp", "with": "example"},
                {"label": "Barcode interlock", "sub": "Yield to 99%", "icon": "barcode", "with": "example"},
                {"label": "SMED pilot", "sub": "Changeover 50 → 20 min", "icon": "clock", "with": "example"}]}},
    "p12": {"type": "timeline", "items": [
        {"label": "Exceptions, milestones", "sub": "Daily / weekly", "icon": "calendar", "with": 1},
        {"label": "KPI trends, risks", "sub": "Monthly", "icon": "chartUp", "with": 2},
        {"label": "Still on strategy?", "sub": "Quarterly", "icon": "search", "with": 3}]},
    "p13": {"type": "icons", "items": [
        {"label": "Few outcomes, clear owners", "icon": "person", "tone": "good", "with": 0},
        {"label": "Check links + resources", "icon": "check", "tone": "good", "with": 1},
        {"label": "Everything 'strong'", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Finished ≠ delivered", "icon": "warning", "tone": "bad", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Before", "value": 2}, "after": {"label": "After", "value": 1.2},
            "decimals": 1, "suffix": "%", "unit": "defect rate", "note": "A 40% relative drop · 6-month payback", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Baselines, draft matrix", "sub": "Days 1–30", "icon": "clipboard", "with": 0},
        {"label": "Catchball, projects, owners", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Check links, review, audit", "sub": "61–90", "icon": "search", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which of these belongs in the KPIs / targets dimension, not the breakthrough objectives?",
        "options": ["Become world-class in product quality", "Raise first-pass yield to 99% this year", "Delight every customer"],
        "correct": 1,
        "explanation": "A target is measurable, with a number and a date. The others are directional objectives, not measures.",
        "q_script": "Quick check. Which of these belongs in the KPIs and targets, rather than the "
                    "breakthrough objectives? Take a few seconds.",
        "a_script": "Raise first-pass yield to ninety-nine percent this year. A target carries a "
                    "number and a date. The other two are directions, not measures.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Arjun's annual on-time delivery goal has no project linked to it. What should he do FIRST?",
        "options": ["Mark a strong link to the nearest project", "Find or launch a project that can move delivery — or rethink the goal",
                    "Leave it; the KPI will improve on its own"],
        "correct": 1,
        "explanation": "A goal with no supporting project is a gap. Close it with real work, or revise the goal; never fill the box with a link that has no mechanism.",
        "q_script": "One more, and this one's a scenario. Arjun's annual delivery goal has no "
                    "project linked to it. What should he do first? Have a think.",
        "a_script": "Find or launch a project that can really move delivery, or rethink the goal. "
                    "Drawing a link with no real mechanism just hides the gap.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
