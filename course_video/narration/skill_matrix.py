"""Skill Training Matrix lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Vikram,
a cell leader on a network-camera cell with four operators (Asha, Bala,
Chitra, Deepa), who learns his "fully trained" cell has a single point of failure.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/skill_matrix.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py skill_matrix  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "sk"
NAME = "skill_matrix"

LETTERS = ["SOP", "ESD", "OJT", "OPL", "SMT", "SKU", "HR", "PPE"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return text.replace("TAKT", "tact")


INTRO_SCRIPT = (
    "Monday morning. Bala calls in sick. He's the only person who can set up lens focus. "
    "By ten o'clock, the whole camera cell has stopped. Sound familiar? In this lesson, "
    "you'll learn the Skill Training Matrix. You'll see who can really do which job, where "
    "the gaps are, and how to close them. We'll follow Vikram, a cell leader, as he "
    "builds one for his team."
)
OUTRO_SCRIPT = (
    "So, three things to remember. A skill matrix shows demonstrated ability, not "
    "attendance. Count qualified backups for every critical job, on every shift. And keep "
    "it live, with evidence behind every rating. Here's your action for this week. List "
    "your three most critical stations, and count the qualified people for each. Great "
    "work completing this lesson. Next, you'll learn TAKT time, the beat of your line."
)

# One story thread: Vikram's network-camera cell. Operators Asha, Bala, Chitra,
# Deepa; skills ESD, PCB assembly, lens focus, test, packing; L0-L4, L3 = qualified.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What a Skill Matrix Is",
        "points": [("Who can do which job, and how well", "who can do"),
                   ("The proven level for each person", "It shows the proven level"),
                   ("The gaps", "And it shows the gaps"),
                   ("Not an attendance sheet", "It is not an attendance sheet")],
        "example": "Vikram's cell: board assembly, lens focus, test and packing — with approved backups for each.",
        "example_cue": "Vikram's cell has",
        "script": "Here's the core idea. A Skill Training Matrix is a visual record of who can do "
                  "which job, and how well. It shows the proven level for each person, on each "
                  "operation. And it shows the gaps. It is not an attendance sheet, or a list of "
                  "courses. Vikram's cell has board assembly, lens focus, test and packing. His "
                  "matrix shows the approved backups for each. Why does that matter so much on "
                  "your line?",
    },
    {
        "key": "p02", "num": 2, "title": "Why It Matters",
        "points": [("Plan staffing, cover absences, balance", "Supervisors use it"),
                   ("Confirm competence on critical steps", "Quality uses it"),
                   ("A clear path to grow", "And people see")],
        "example": "Skilled at feeder setup ≠ authorized to release a program. Two different skills.",
        "example_cue": "A technician might be skilled",
        "script": "Because it links your people to your results. Supervisors use it to plan "
                  "staffing, cover absences, and balance the line. Quality uses it to confirm "
                  "who's competent on critical steps. And people see a clear path to grow. Here's "
                  "a subtle point. A technician might be skilled at feeder setup, but not "
                  "authorized to release a program. Those are two different skills. Which three "
                  "stations would hurt most if their only expert was absent?",
    },
    {
        "key": "p03", "num": 3, "title": "Matrix Structure",
        "points": [("Rows: people", "People go in the rows"),
                   ("Columns: skills", "Skills go in the columns"),
                   ("Each cell: level + last assessed", "Each cell shows"),
                   ("Each skill linked to its SOP", "Each skill links"),
                   ("Don't lump tasks into one skill", "Never lump different tasks")],
        "example": "Production keeps it current; trainers assess; Quality validates the critical skills.",
        "example_cue": "Production keeps the matrix",
        "script": "The layout is simple. People go in the rows. Skills go in the columns. Each "
                  "cell shows the person's level, and when it was last assessed. Each skill links "
                  "to its SOP, and shows how critical it is. Production keeps the matrix up to "
                  "date. Trainers assess, and Quality validates the critical skills. And here's a "
                  "rule. Never lump different tasks into one skill, just to make the chart look "
                  "full. So what do the levels mean?",
    },
    {
        "key": "p04", "num": 4, "title": "Proficiency Levels L0–L4",
        "points": [("L0 not trained", "Level zero means"),
                   ("L1 understands safety and sequence", "Level one means"),
                   ("L2 works under supervision", "Level two means"),
                   ("L3 qualified to work alone", "Level three means"),
                   ("L4 trains others, troubleshoots", "Level four means")],
        "example": "A level isn't a permit: machine and safety authorization are recorded separately.",
        "example_cue": "But a level isn't a permit",
        "script": "Use a five-level scale. Level zero means not trained. Level one means you "
                  "understand the safety, sequence and main risks. Level two means you can do it "
                  "under supervision. Level three means you're qualified to work alone, within "
                  "cycle time and quality limits. Level four means you can train others and "
                  "troubleshoot. But a level isn't a permit. Machine and safety authorization "
                  "are recorded separately. Which skills come first?",
    },
    {
        "key": "p05", "num": 5, "title": "Find the Critical Skills",
        "points": [("Map every step and its SOP", "List every step"),
                   ("Flag safety, quality, customer impact", "Then flag the skills"),
                   ("Rate impact, difficulty, backups", "Rate the impact"),
                   ("Minimum qualified headcount per shift", "set a minimum qualified")],
        "example": "Vikram's cell: lens focus and firmware flashing rank highest; carton handling ranks lower.",
        "example_cue": "In Vikram's cell",
        "script": "Start with your process map. List every step, and the SOP that governs it. "
                  "Then flag the skills where a mistake hits safety, quality or the customer. "
                  "Rate the impact, how hard the skill is to learn, and how many backups you "
                  "have. In Vikram's cell, lens focus and firmware flashing rank highest. A wrong "
                  "setting there reaches the customer. Carton handling ranks lower. For each "
                  "critical skill, set a minimum qualified headcount per shift.",
    },
    {
        "key": "p06", "num": 6, "title": "Assessing Real Skill",
        "points": [("Brief theory check", "Check theory briefly"),
                   ("Watch real cycles + one abnormal situation", "Observe several real cycles"),
                   ("Record date, assessor, results", "Record the date")],
        "example": "A test operator passed the theory but kept missing failed serial scans — she stays at level two.",
        "example_cue": "One of Vikram's test operators",
        "script": "Now, how do you know someone is really at level three? You test what they can "
                  "actually do. Check theory briefly, then watch the practical work. Observe "
                  "several real cycles, and at least one abnormal situation. Record the date, the "
                  "assessor and the results. One of Vikram's test operators passed the theory "
                  "easily. But she kept missing failed serial scans. So she stays at level two "
                  "for now. When should you reassess?",
    },
    {
        "key": "p07", "num": 7, "title": "Training Needs & Gaps",
        "points": [("Reassess after absence or changes", "Reassess after"),
                   ("Need = required level − proven level", "A need is the gap"),
                   ("Count qualified people vs positions", "Count your qualified people"),
                   ("Find single points of failure", "Look hard for single")],
        "example": "Vikram's shift needs 4 qualified firmware operators and has 2: a gap of 2.",
        "example_cue": "Vikram's shift needs",
        "script": "Reassess after a long absence, a process change or repeated defects. Then work "
                  "out your training needs. A need is the gap between the level you require and "
                  "the level that's proven. Count your qualified people against the positions "
                  "you must fill. Vikram's shift needs four qualified firmware operators. He has "
                  "two. That's a gap of two. Look hard for single points of failure, like Bala "
                  "on lens focus. How do you close the gap?",
    },
    {
        "key": "p08", "num": 8, "title": "Training Methods",
        "points": [("Structured on-the-job training", "structured on-the-job training"),
                   ("Independent assessor checks the result", "An independent assessor"),
                   ("Dojo: safe practice off the line", "A Dojo is"),
                   ("One Point Lessons for key points", "One Point Lessons reinforce")],
        "example": "Vikram's packing Dojo uses wrong labels and missing accessories on purpose.",
        "example_cue": "Vikram's packing Dojo",
        "script": "Train your people with structured on-the-job training. The trainer prepares, demonstrates at "
                  "standard pace, and then the learner practices with feedback. An independent "
                  "assessor checks the result. A Dojo is a training area off the line, where "
                  "people can practice safely. Vikram's packing Dojo uses wrong labels and "
                  "missing accessories on purpose. One Point Lessons reinforce single key "
                  "points. And remember to teach the reaction to problems, not just the normal "
                  "steps.",
    },
    {
        "key": "p09", "num": 9, "title": "The 90-Day Training Plan",
        "points": [("Days 1–30: map, define levels, assess", "In the first thirty days"),
                   ("Days 31–60: train the critical gaps", "In the next thirty"),
                   ("Days 61–90: certify backups, scale up", "In the last thirty")],
        "example": "Vikram's first priority: get a second lens focus expert qualified.",
        "example_cue": "Vikram's first priority",
        "script": "Every training plan needs owners, dates and a clear result. Here's a ninety-day "
                  "version. In the first thirty days, map the skills, define the levels, and "
                  "assess where you are. In the next thirty, train the critical gaps, and verify "
                  "people moving to level three. In the last thirty, certify backups and scale "
                  "up. Vikram's first priority was obvious. Get a second lens focus expert "
                  "qualified. What would yours be?",
    },
    {
        "key": "p10", "num": 10, "title": "Matrix KPIs",
        "points": [("Qualification coverage", "Qualification coverage asks"),
                   ("Skill attainment", "Skill attainment tracks"),
                   ("Cross-training rate", "Cross-training rate counts"),
                   ("Expired qualifications", "count expired qualifications")],
        "example": "18 of 24 critical positions covered = 75%. Calculate it per shift.",
        "example_cue": "Vikram has eighteen",
        "script": "Measure your real resilience, not training hours. Qualification coverage asks how "
                  "many required positions have a qualified person. Skill attainment tracks the "
                  "planned upgrades that are verified. Cross-training rate counts people "
                  "qualified on two or more jobs. And count expired qualifications. Vikram has "
                  "eighteen of twenty-four critical positions covered. That's seventy-five "
                  "percent. Calculate it per shift, because one person can't cover two stations "
                  "at once.",
    },
    {
        "key": "p11", "num": 11, "title": "Worked Example: Vikram's Cell",
        "points": [("Asha: board assembly L4", "Asha is a level four"),
                   ("Chitra now joins Bala: lens focus L3", "Chitra has now joined"),
                   ("Chitra, Deepa: test L3+", "Chitra and Deepa are"),
                   ("Next priority: another focus backup", "So what's the next")],
        "example": "Focus + test at once: Bala on focus, Deepa on test. Chitra can't do both.",
        "example_cue": "So who covers focus",
        "script": "Here's Vikram's matrix after ninety days. Asha is a level four on board assembly. "
                  "Chitra has now joined Bala at level three on lens focus. Chitra and Deepa are qualified on "
                  "test. So who covers focus and test at the same time? Bala on focus, and Deepa "
                  "on test. Chitra can't do both at once. If Bala is absent, Chitra must move to "
                  "focus. So what's the next training priority? Another lens focus backup.",
    },
    {
        "key": "p12", "num": 12, "title": "Link to Quality & Safety",
        "points": [("Level + authorization + SOP training", "only when three things"),
                   ("Each skill tied to its SOP revision", "Tie each skill"),
                   ("Process change → reassess", "When the process changes"),
                   ("Training never replaces process design", "training never replaces")],
        "example": "Vikram's firmware technician was L3 on the old recipe — the new one changed critical steps, so he was reassessed.",
        "example_cue": "Vikram's firmware technician",
        "script": "A skill matrix is a quality safeguard. Someone should work alone on a "
                  "critical step only when three things are current. Their level, their "
                  "authorization, and their SOP training. Tie each skill to its SOP revision. When the process "
                  "changes, reassess. Vikram's firmware technician was level three on the old "
                  "recipe. The new one changed critical steps, so he was reassessed. And "
                  "remember, training never replaces good process design. Can software help?",
    },
    {
        "key": "p13", "num": 13, "title": "Digital Matrix & Visual Board",
        "points": [("Unique codes for people and skills", "Use unique codes"),
                   ("Audit trail of every change", "keep an audit trail"),
                   ("Reminders for expiring qualifications", "Set reminders"),
                   ("No self-approval of critical skills", "Never let anyone approve")],
        "example": "Vikram's dashboard warns him when an authorization is about to expire.",
        "example_cue": "Vikram's dashboard warns",
        "script": "Yes, if the data is trustworthy. A digital matrix links assessments, SOP "
                  "revisions and shift plans. Use unique codes for people and skills, and keep "
                  "an audit trail of every change. Set reminders for expiring qualifications. "
                  "Never let anyone approve their own critical skill. Vikram's dashboard warns "
                  "him when an authorization is about to expire. And here's an audit question. "
                  "Can you show the evidence behind any level three rating?",
    },
    {
        "key": "p14", "num": 14, "title": "Governance & Review",
        "points": [("Daily: qualified staffing at start-up", "Every day"),
                   ("Weekly: gaps, cross-training, overdue", "Every week"),
                   ("Monthly: coverage, people leaving", "Every month"),
                   ("Quarterly: assessor consistency", "Every quarter")],
        "example": "Seniority and attendance don't equal qualification.",
        "example_cue": "Seniority and attendance",
        "script": "Keep the matrix alive with a steady review rhythm. Every day, check that "
                  "critical stations are staffed by qualified people at start-up. Every week, "
                  "review gaps, cross-training and overdue assessments. Every month, look at "
                  "coverage and the risk of people leaving. Every quarter, check that assessors "
                  "rate consistently. And update levels when ability really changes, not on a "
                  "calendar. Seniority and attendance don't equal qualification. Ready to build "
                  "yours?",
    },
    {
        "key": "p15", "num": 15, "title": "Templates & Audit",
        "points": [("Matrix: skill, SOP rev, level, expiry", "The matrix holds"),
                   ("Assessment form: theory, cycles, safety", "The assessment form"),
                   ("A training plan for each gap", "Each gap gets"),
                   ("Audit cells against real work", "Then audit it")],
        "example": "Another supervisor should see who is qualified today, at a glance.",
        "example_cue": "Another supervisor should see",
        "script": "Use a controlled template for your matrix. The matrix holds each person, skill, SOP revision, "
                  "level, assessment date and expiry. The assessment form records theory, "
                  "observed cycles, safety checks and the result. Each gap gets a training plan. "
                  "Then audit it. Pick a few cells, and check the evidence against real work on "
                  "the floor. Another supervisor should see who is qualified today, at a glance. "
                  "It's a live control system, not decoration.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Who does which job", "icon": "person"}, {"label": "Proven level", "icon": "check"},
        {"label": "The gaps", "icon": "warning", "tone": "bad"},
        {"label": "Not attendance", "icon": "cross", "tone": "bad"}]},
    "p02": {"type": "icons", "items": [
        {"label": "Staffing, absences", "icon": "calendar"},
        {"label": "Competence on critical steps", "icon": "shield"},
        {"label": "A path to grow", "icon": "chartUp", "tone": "good"}]},
    "p03": {"type": "matrix", "cols": ["Lens", "Fasten", "Test", "Pack"], "note": "Illustration: each cell is a proven level", "items": [
        {"label": "Person A", "cells": [3, 4, 2, None], "with": 0},
        {"label": "Person B", "cells": [1, 3, 3, 2], "with": 1},
        {"label": "Person C", "cells": [None, 2, 4, 3], "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Not trained", "sub": "L0"}, {"label": "Understands", "sub": "L1"},
        {"label": "Supervised", "sub": "L2"}, {"label": "Works alone", "sub": "L3"},
        {"label": "Trains others", "sub": "L4"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Map every step + SOP", "icon": "clipboard"},
        {"label": "Flag safety, quality, customer", "icon": "warning"},
        {"label": "Rate impact, difficulty, backups", "icon": "scale"},
        {"label": "Minimum qualified per shift", "icon": "person", "tone": "good"}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Lens focus", "sub": "Highest risk", "icon": "camera", "tone": "bad", "with": "example"},
            {"label": "Firmware flashing", "sub": "Highest risk", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "Carton handling", "sub": "Lower", "icon": "box", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Brief theory check", "icon": "clipboard", "with": 0},
        {"label": "Real cycles + one abnormal", "icon": "search", "with": 1},
        {"label": "Date, assessor, result", "icon": "calendar", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Theory: passed", "icon": "clipboard", "tone": "good", "with": "example"},
            {"label": "Real work: missed failed scans", "icon": "search", "tone": "bad", "with": "example"},
            {"label": "She stays at level 2", "icon": "person", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Reassess after changes", "icon": "sequence", "with": 0},
        {"label": "Need = required − proven", "icon": "count", "with": 1}],
        "then": {"type": "bars", "label": "", "note": "A gap of 2", "unit": "qualified firmware operators per shift", "with": "example", "items": [
            {"label": "Needed", "value": 4, "with": "example"},
            {"label": "Have", "value": 2, "tone": "bad", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "On-the-job training", "icon": "person"}, {"label": "Independent assessor", "icon": "shield"},
        {"label": "Dojo", "sub": "Safe practice off the line", "icon": "tray"}, {"label": "One Point Lessons", "icon": "clipboard"}]},
    "p09": {"type": "timeline", "items": [
        {"label": "Map skills, define levels, assess", "sub": "Days 1–30", "icon": "clipboard"},
        {"label": "Train the critical gaps", "sub": "31–60", "icon": "person"},
        {"label": "Certify backups, scale up", "sub": "61–90", "icon": "check"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Qualification coverage", "icon": "count"}, {"label": "Skill attainment", "icon": "chartUp"},
        {"label": "Cross-training rate", "icon": "sequence"}, {"label": "Expired qualifications", "icon": "clock", "tone": "bad"}],
        "then": {"type": "stat", "value": 75, "suffix": "%", "icon": "person", "label": "of critical positions covered",
                 "unit": "18 of 24: calculate it per shift", "with": "example"}},
    "p11": {"type": "matrix", "cols": ["Board", "Focus", "Test"], "note": "After 90 days. Focus + test at once: Bala and Deepa. Next: another focus backup.", "items": [
        {"label": "Asha", "cells": [4, None, None], "with": 0},
        {"label": "Bala", "cells": [None, 3, None], "with": 1},
        {"label": "Chitra", "cells": [None, 3, 3], "with": 1},
        {"label": "Deepa", "cells": [None, None, 3], "with": 2}]},
    "p12": {"type": "icons", "items": [
        {"label": "Level", "icon": "person", "with": 0}, {"label": "Authorization", "icon": "key", "with": 0},
        {"label": "SOP training", "icon": "clipboard", "with": 0},
        {"label": "Process change: reassess", "icon": "sequence", "with": 2}]},
    "p13": {"type": "icons", "items": [
        {"label": "Unique codes", "icon": "barcode"}, {"label": "Audit trail", "icon": "sequence"},
        {"label": "Expiry reminders", "icon": "clock"}, {"label": "No self-approval", "icon": "cross", "tone": "bad"}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Qualified staffing at start-up", "sub": "Daily", "icon": "person"},
        {"label": "Gaps, cross-training, overdue", "sub": "Weekly", "icon": "calendar"},
        {"label": "Coverage, people leaving", "sub": "Monthly", "icon": "chartUp"},
        {"label": "Assessor consistency", "sub": "Quarterly", "icon": "scale"}]},
    "p15": {"type": "doc", "items": [
        {"label": "Skill matrix · Cell 2 · Rev C", "icon": "label", "with": 0},
        {"label": "Skill · SOP rev · level · expiry", "icon": "clipboard", "with": 0},
        {"label": "Assessment: theory, cycles, safety", "icon": "test", "with": 1},
        {"label": "A training plan for each gap", "icon": "calendar", "with": 2},
        {"label": "Audited against real work", "icon": "search", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "An operator has finished the training course but hasn't been assessed yet. Can they be counted as L3?",
        "options": ["Yes — the course is complete", "No — L3 needs demonstrated, assessed performance",
                    "Yes, if they've worked there a long time"],
        "correct": 1,
        "explanation": "Attendance and seniority aren't competence. Level 3 means independent performance proven by an assessment with evidence.",
        "q_script": "Quick check. An operator has finished the training course, but hasn't been "
                    "assessed yet. Can they be counted as level three? Take a few seconds.",
        "a_script": "No. Level three needs performance that's been assessed and proven. Attending "
                    "a course isn't the same as being qualified.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Only one person on the shift is qualified on lens focus, and output depends on it. What should the cell leader do FIRST?",
        "options": ["Train everyone on every skill", "Qualify a backup for lens focus as the top priority",
                    "Ask the expert never to take leave", "Train low-risk skills first because they're quicker"],
        "correct": 1,
        "explanation": "A single-point dependency on a critical skill is the biggest risk. Prioritize qualifying a backup there, then widen cross-training.",
        "q_script": "One more, and this one's a scenario. Only one person on the shift is "
                    "qualified on lens focus, and the whole cell depends on it. What should the "
                    "cell leader do first? Have a think.",
        "a_script": "Qualify a backup on lens focus first. A single point of failure on a "
                    "critical skill is the biggest risk. Then widen cross-training.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
