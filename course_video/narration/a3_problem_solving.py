"""A3 Problem Solving lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Karthik,
a test engineer on a server assembly line, writing his first A3 about servers
failing their first boot test (a memory module not fully seated after a
chassis change).

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/a3_problem_solving.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py a3_problem_solving  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "a3"
NAME = "a3_problem_solving"

LETTERS = ["MES", "SOP", "PDCA"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. A3 = "A-three"; Genbutsu / Genjitsu
# = gen-BOO-tsu / gen-JEE-tsu (Gemba Academy's sound-alike guide).
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = re.sub(r"\bA3\b", "A-three", text)
    text = re.sub(r"\b3G\b", "three-G", text)
    text = re.sub(r"\bGenbutsu\b", "Gen-boot-sue", text)
    return re.sub(r"\bGenjitsu\b", "Gen-jeet-sue", text)


INTRO_SCRIPT = (
    "Five hundred and seventy-six servers failed their first boot test in four weeks. "
    "The first fix proposed? Add two more inspectors. Sound familiar? In this lesson, "
    "you'll learn A3 problem solving. You'll see how to tell a whole problem story on "
    "one page, from the real gap to a proven fix. We'll follow Karthik, a test engineer "
    "on a server assembly line, as he writes his first A3."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Start with a measurable gap, never a cause or a "
    "solution. Go and see, and prove every cause with evidence. And standardize only "
    "what your pilot really proved. Here's your action for this week. Pick one repeating "
    "problem, and write its problem statement on an A3 sheet. Great work completing this "
    "lesson. Next, you'll learn the Burn Down Chart, tracking work against time."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What an A3 Is",
        "points": [("Named after the A3 paper size", "An A3 is named"),
                   ("The whole problem story on one page", "It tells a whole"),
                   ("Define, find causes, test, sustain", "You define the problem"),
                   ("Visual, and built as a team", "It's visual")],
        "example": "Karthik's report said “operators are careless”. His manager handed back one blank A3 sheet.",
        "example_cue": "His report said",
        "script": "An A3 is named after a paper size. It tells a whole problem story on one page. "
                  "You define the problem, find its real causes, test fixes and keep the results. "
                  "It's visual, and you build it as a team. Here's how Karthik met his first one. "
                  "His report said operators are careless. His manager handed it back, with one "
                  "blank A3 sheet. So what really counts as a problem?",
    },
    {
        "key": "p02", "num": 2, "title": "Problems Are Gaps",
        "points": [("A problem is a measurable gap", "A problem is a gap"),
                   ("Don't jump from complaint to solution", "A3 stops you jumping"),
                   ("A gap can be measured and investigated", "You can measure a gap")],
        "example": "“Operators are careless” is blame. “Boot failures rose to 4.8%” is a gap.",
        "example_cue": "Compare two statements",
        "script": "Here's the key idea. A problem is a gap, between what's happening and the "
                  "standard you need. A3 stops you jumping from a complaint straight to a solution. "
                  "Compare two statements. Operators are careless is blame. Boot failures rose "
                  "to four point eight percent. That's a gap. You can measure a gap. "
                  "You can investigate it, too. Which kind of statement do you hear most on your floor?",
    },
    {
        "key": "p03", "num": 3, "title": "Where A3 Fits: PDCA",
        "points": [("Problems that keep coming back", "Use it for problems"),
                   ("Problems teams must solve together", "It shines when"),
                   ("Built on Plan · Do · Check · Act", "it follows PDCA")],
        "example": "Karthik's boot failures: repeated, costly and cross-functional.",
        "example_cue": "Karthik's boot failures",
        "script": "Where does A3 fit? Use it for problems that keep coming back. Repeated defects, "
                  "downtime, shortages and missed output are good candidates. It shines when "
                  "Production, Quality and Engineering must solve something together. And underneath, "
                  "it follows PDCA. You plan, then do a small pilot. You check the results against "
                  "the target. Then you act, by standardizing or rethinking. Karthik's boot failures "
                  "fit perfectly. So what goes on your sheet?",
    },
    {
        "key": "p04", "num": 4, "title": "Anatomy of an A3",
        "points": [("Left: background, current condition, target", "The left side"),
                   ("Root-cause analysis: why the gap exists", "Root-cause analysis explains"),
                   ("Right: countermeasures, plan, follow-up", "The right side"),
                   ("Each panel answers one question", "Each panel answers")],
        "example": "Karthik's sheet: seven panels, one page, read left to right.",
        "example_cue": "Karthik's sheet has",
        "script": "Picture the sheet. The left side tells the story so far. Background says why it "
                  "matters now. Current condition shows what's really happening. Target says what "
                  "result, by when. Root-cause analysis explains why the gap exists. The right side "
                  "moves to action, with countermeasures, a plan and follow-up. Each panel answers "
                  "one question. Karthik's sheet has seven panels, read left to right. Could you "
                  "name the question behind each one?",
    },
    {
        "key": "p05", "num": 5, "title": "The Problem Statement",
        "points": [("Name the gap, never a cause", "names the gap"),
                   ("Line · product · period · measure", "Name the line"),
                   ("Clear denominator, same definitions", "Use one clear denominator"),
                   ("No blame, no solution", "There's no blame")],
        "example": "Line 2, last month: 4.8% of 12,000 servers failed first boot test, vs a 1.5% reference.",
        "example_cue": "Here's Karthik's version",
        "script": "Now, the hardest panel to get right. A good problem statement names the gap, but "
                  "never claims a cause. Name the line, the product, the period and the measure. "
                  "Use one clear denominator and the same definitions. Here's Karthik's version. Over "
                  "the last month on Line Two, first boot-test failures averaged four point eight percent. "
                  "The reference was one point five, across twelve thousand servers. Notice what's "
                  "missing? There's no blame, and no solution.",
    },
    {
        "key": "p06", "num": 6, "title": "Go and See: the 3G",
        "points": [("Gemba: the real place", "Gemba is the real place"),
                   ("Genbutsu: the real things", "Genbutsu means"),
                   ("Genjitsu: the real facts", "Genjitsu means")],
        "example": "7 of 10 failed servers at the bench: a memory module sitting slightly raised.",
        "example_cue": "Karthik pulled ten",
        "script": "Before you open a spreadsheet, go and see. Lean calls it the 3G. Gemba is the "
                  "real place, so you stand at the test station. Genbutsu means the real things, "
                  "like failed servers, fixtures and test logs. Genjitsu means the real facts, which "
                  "you check yourself. Karthik pulled ten failed servers onto the bench. In seven of "
                  "them, a memory module sat slightly raised. Would a report ever have shown him that?",
    },
    {
        "key": "p07", "num": 7, "title": "Data You Can Trust",
        "points": [("One clear definition", "starts with a clear definition"),
                   ("Count unique units: retests can't hide failures", "Why unique?"),
                   ("Check timestamps, serials, calibration", "Are the timestamps right"),
                   ("Line log matches the MES", "Does the line log")],
        "example": "First-pass failure rate = unique servers failing their first valid test ÷ unique servers tested.",
        "example_cue": "First-pass failure rate is",
        "script": "Good data starts with a clear definition. Karthik's rule was simple. First-pass "
                  "failure rate is unique servers failing their first valid test, divided by unique "
                  "servers tested. Why unique? Because retests can hide failures, or count one server "
                  "twice. Then check the data itself. Are the timestamps right, and every serial "
                  "number unique? Is the tester calibrated? Does the line log match the MES? Only "
                  "then can you trust your chart.",
    },
    {
        "key": "p08", "num": 8, "title": "Seeing the Gap",
        "points": [("Weekly trend: rising every week", "weekly trend climbed"),
                   ("About 400 extra failures", "That's nearly four hundred"),
                   ("Pareto: sort failures by mode", "Then a Pareto chart")],
        "example": "Memory not detected: 288 of 576 failures, half of the total.",
        "example_cue": "Memory not detected",
        "script": "So what did the chart show? Karthik's weekly trend climbed every single week. "
                  "By week four, it reached five and a half percent. At the reference rate, you'd expect about "
                  "one hundred and eighty failures. He had five hundred and seventy-six. That's "
                  "nearly four hundred extra. Then a Pareto chart split them by failure mode. Memory "
                  "not detected was half of them. The gap is clear, but it doesn't prove a cause. "
                  "Where would you start?",
    },
    {
        "key": "p09", "num": 9, "title": "Target & Scope",
        "points": [("Target: 2% or less within 6 weeks", "Karthik's was clear"),
                   ("Guardrails: test time, retests, escapes", "Add guardrails too"),
                   ("Scope: what's in, what's out", "Then fix the scope")],
        "example": "Out of scope: loosening the test limits to look better.",
        "example_cue": "Loosening the test limits",
        "script": "Next, set a target you can actually test. Karthik's was clear. Cut first boot-test "
                  "failures on Line Two to two percent or less, within six weeks. Add guardrails too, "
                  "like test time, retest rate and escaped defects. They make sure you don't win by "
                  "cheating. Then fix the scope. Memory failures on Line Two are in. Loosening the "
                  "test limits is out. Can you see why that matters?",
    },
    {
        "key": "p10", "num": 10, "title": "Exploring Causes: Ishikawa",
        "points": [("Think broadly first", "think broadly"),
                   ("Six M's: people, machine, method…", "It sorts possible causes"),
                   ("Every branch is a guess until checked", "Every branch is only")],
        "example": "Is insertion trained? Has the chassis changed? Does latching vary by lot?",
        "example_cue": "Karthik's team asked",
        "script": "Now, why is the gap there? First, think broadly with an Ishikawa diagram. It sorts "
                  "possible causes into six M's. People, machine, method, material, measurement and "
                  "environment. Karthik's team asked questions in each one. Is the insertion method "
                  "trained? Has the chassis changed? Does module latching vary by lot? But be careful. "
                  "Every branch is only a guess until you check it. So how do you narrow it down?",
    },
    {
        "key": "p11", "num": 11, "title": "Root Cause: Five Whys",
        "points": [("Ask why, step by step", "go deep with five whys"),
                   ("End at a process cause you can fix", "That's a process cause"),
                   ("A chain isn't proof: test it", "But a chain")],
        "example": "Root cause: work instructions weren't reviewed when the chassis changed.",
        "example_cue": "Work instructions weren't reviewed",
        "script": "Then go deep with five whys. Why did servers fail boot test? A memory module wasn't "
                  "fully seated. Why? The latch closed before the module was fully down. Why? The new "
                  "chassis left less room to press straight. Why wasn't the method changed? Work "
                  "instructions weren't reviewed when the chassis changed. That's a process cause you "
                  "can fix. But a chain isn't proof. Karthik pressed modules at an angle, and the "
                  "fault appeared every time.",
    },
    {
        "key": "p12", "num": 12, "title": "Countermeasures & Containment",
        "points": [("Break the verified cause", "break the cause"),
                   ("Judge: effect, risk, cost, sustain", "Judge each one"),
                   ("Contain now, fix for good", "Meanwhile, contain")],
        "example": "Insertion guide · latch check · work-instruction review on every chassis change",
        "example_cue": "Karthik's team picked three",
        "script": "Now choose countermeasures that break the cause. Karthik's team picked three. An "
                  "insertion guide that keeps the module straight. A latch check before the server "
                  "leaves the station. And a work-instruction review on every chassis change. Judge "
                  "each one on effect, risk, cost and how easy it is to sustain. Meanwhile, contain. "
                  "Suspect servers were held and rechecked. Containment protects your customer, but "
                  "it isn't the fix.",
    },
    {
        "key": "p13", "num": 13, "title": "Plan & Owners",
        "points": [("One owner, a due date, evidence", "your plan names one owner"),
                   ("Weeks 1–2: confirm cause, pilot", "Test engineering confirms"),
                   ("Weeks 3–4: update SOP, train every shift", "Maintenance and production"),
                   ("Weeks 5–6: verify the results", "Quality verifies")],
        "example": "Stuck? Escalate with the exact blocker and the decision you need.",
        "example_cue": "Stuck?",
        "script": "An action without an owner rarely happens. So your plan names one owner, a due date "
                  "and the evidence for each action. Test engineering confirms the cause in week one. "
                  "Process engineering pilots the insertion guide in week two. Maintenance and "
                  "production update the SOP and train every shift by week four. Quality verifies the "
                  "results in weeks five and six. Stuck? Escalate with the exact blocker. So how do "
                  "you know it worked?",
    },
    {
        "key": "p14", "num": 14, "title": "Pilot & Check",
        "points": [("Same product mix as the baseline", "with the same product mix"),
                   ("4.8% down to 1.6%: target met", "Failures dropped"),
                   ("Guardrails checked too", "he checked the guardrails"),
                   ("Missed? Revisit the cause, not the target", "If it hadn't")],
        "example": "Pilot: 48 failures in 3,000 servers = 1.6%.",
        "example_cue": "Karthik ran it",
        "script": "A pilot is an experiment, not an announcement. Karthik ran it on three thousand "
                  "servers, with the same product mix as the baseline. Failures dropped "
                  "to one point six percent. Target met. But he checked the guardrails "
                  "too. Test time held steady, and no other failure mode grew. Did it hold on every "
                  "shift? Yes. If it hadn't, you'd revisit the cause, never quietly change the target.",
    },
    {
        "key": "p15", "num": 15, "title": "Sustain & Your 30-Day A3",
        "points": [("Update SOP, checklist, training", "Update the SOP"),
                   ("Shift-start check; review at 30/60/90 days", "Add a latch check"),
                   ("Copy only to lines that truly match", "Copy it to other lines"),
                   ("Your own A3 in 30 days", "Now it's your turn")],
        "example": "Days 1–5: one real problem, baseline at the gemba. Day 20: causes and pilot. Day 30: present your A3.",
        "example_cue": "In the first five days",
        "script": "Finally, make the new way the normal way. Update the SOP, the checklist and the "
                  "training. Add a latch check at every shift start, and review the trend at thirty, "
                  "sixty and ninety days. Copy it to other lines only after checking they really "
                  "match. Now it's your turn. In the first five days, pick one real problem and check "
                  "its baseline at the gemba. By day twenty, verify causes and run a pilot. By day "
                  "thirty, present your A3.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "A3 paper size", "icon": "label", "with": 0},
        {"label": "One-page story", "icon": "clipboard", "with": 1},
        {"label": "Causes, tests, results", "icon": "search", "with": 2},
        {"label": "Built as a team", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "“Operators are careless”", "sub": "Karthik's first report", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "One blank A3 sheet", "sub": "His manager's answer", "icon": "clipboard", "tone": "good", "with": "example"}]}},
    "p02": {"type": "versus", "items": [
        {"label": "Blame", "sub": "“Operators are careless”", "icon": "person", "tone": "bad", "with": "example"},
        {"label": "Gap", "sub": "Boot failures up to 4.8%", "icon": "chartUp", "tone": "good", "with": "example"}]},
    "p03": {"type": "icons", "items": [
        {"label": "Repeated defects", "icon": "warning", "with": 0},
        {"label": "Downtime, shortages", "icon": "clock", "with": 0},
        {"label": "Cross-functional", "icon": "person", "with": 1}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Plan", "icon": "clipboard", "with": 2},
            {"label": "Do", "sub": "Small pilot", "icon": "wrench", "with": 2},
            {"label": "Check", "sub": "Against target", "icon": "search", "with": 2},
            {"label": "Act", "sub": "Standardize", "icon": "check", "tone": "good", "with": 2}]}},
    "p04": {"type": "doc", "items": [
        {"label": "Background · why now", "icon": "label", "with": 0},
        {"label": "Current condition · target", "icon": "chartUp", "with": 0},
        {"label": "Root cause · why the gap", "icon": "search", "with": 1},
        {"label": "Countermeasures · plan", "icon": "wrench", "with": 2},
        {"label": "Follow-up · did it work?", "icon": "check", "with": 2}]},
    "p05": {"type": "versus", "items": [
        {"label": "Weak", "sub": "“Quality is poor everywhere”", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Precise", "sub": "Line 2 · last month · 4.8% vs 1.5%", "icon": "check", "tone": "good", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Real place", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Real things", "icon": "chip", "with": 1},
        {"label": "Genjitsu", "sub": "Real facts", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 7, "suffix": " of 10", "icon": "chip", "label": "failed servers on the bench",
                 "unit": "a memory module sitting slightly raised", "with": "example"}},
    "p07": {"type": "flow", "items": [
        {"label": "Clear definition", "icon": "clipboard", "with": 0},
        {"label": "Unique servers", "icon": "count", "with": 1},
        {"label": "Timestamps, serials", "icon": "barcode", "with": 2},
        {"label": "Log matches MES", "icon": "check", "tone": "good", "with": 3}]},
    "p08": {"type": "bars", "label": "", "note": "First boot-test failures per 1,000 servers, by week", "items": [
        {"label": "W1", "value": 41, "with": 0},
        {"label": "W2", "value": 46, "with": 0},
        {"label": "W3", "value": 50, "with": 0},
        {"label": "W4", "value": 55, "tone": "bad", "with": 0}],
        "then": {"type": "bars", "label": "", "note": "Failure modes: 576 first-pass failures", "with": 2, "items": [
            {"label": "Memory", "value": 288, "tone": "bad", "with": 2},
            {"label": "Fan", "value": 144, "with": 2},
            {"label": "Network", "value": 86, "with": 2},
            {"label": "Other", "value": 58, "with": 2}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Target", "sub": "≤ 2% in 6 weeks", "icon": "pin", "tone": "good", "with": 0},
        {"label": "Guardrails", "sub": "Test time, retests, escapes", "icon": "shield", "with": 1}],
        "then": {"type": "versus", "with": 2, "items": [
            {"label": "Out of scope", "sub": "Loosening test limits", "icon": "cross", "tone": "bad", "with": 2},
            {"label": "In scope", "sub": "Memory failures, Line 2", "icon": "check", "tone": "good", "with": 2}]}},
    "p10": {"type": "icons", "items": [
        {"label": "People", "icon": "person", "with": 1},
        {"label": "Machine", "icon": "gear", "with": 1},
        {"label": "Method", "icon": "clipboard", "with": 1},
        {"label": "Material", "icon": "box", "with": 1},
        {"label": "Measurement", "icon": "scale", "with": 1},
        {"label": "Environment", "icon": "wave", "with": 1}]},
    "p11": {"type": "steps", "items": [
        {"label": "Module not fully seated", "with": 0},
        {"label": "Latch closed too early", "with": 0},
        {"label": "Less room in new chassis", "with": 0},
        {"label": "Instructions not reviewed", "with": "example"}],
        "then": {"type": "stat", "value": 100, "suffix": "%", "icon": "test", "label": "fault reproduced",
                 "unit": "pressing modules at an angle", "with": 2}},
    "p12": {"type": "flow", "items": [
        {"label": "Insertion guide", "icon": "shape", "with": "example"},
        {"label": "Latch check", "icon": "sensor", "with": "example"},
        {"label": "Review on chassis change", "icon": "clipboard", "tone": "good", "with": "example"}],
        "then": {"type": "flow", "with": 2, "items": [
            {"label": "Containment", "sub": "Protects the customer now", "icon": "lock", "with": 2},
            {"label": "Countermeasure", "sub": "Removes the cause for good", "icon": "key", "tone": "good", "with": 2}]}},
    "p13": {"type": "timeline", "items": [
        {"label": "Confirm cause, pilot", "sub": "Weeks 1–2", "icon": "test", "with": 1},
        {"label": "Update SOP, train", "sub": "Weeks 3–4", "icon": "clipboard", "with": 2},
        {"label": "Verify results", "sub": "Weeks 5–6", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Baseline", "value": 4.8}, "after": {"label": "Pilot", "value": 1.6},
            "decimals": 1, "suffix": "%", "unit": "servers failing first boot test",
            "note": "Target ≤ 2%: met", "with": 1},
    "p15": {"type": "timeline", "items": [
        {"label": "One real problem, baseline", "sub": "Days 1–5", "icon": "walk", "with": "example"},
        {"label": "Causes and pilot", "sub": "By day 20", "icon": "search", "with": "example"},
        {"label": "Present your A3", "sub": "Day 30", "icon": "clipboard", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which is the best A3 problem statement?",
        "options": ["Operators are careless when fitting memory",
                    "Line 2 first boot-test failures averaged 4.8% vs 1.5% over 4 weeks",
                    "We need two more inspectors at test"],
        "correct": 1,
        "explanation": "It names the line, period and measure, with a reference, and claims no cause. The others are a blame and a solution.",
        "q_script": "Quick check. Which of these is the best A3 problem statement? Take a few seconds.",
        "a_script": "It's the second one. It names the line, the period and the measure, and it doesn't "
                    "claim a cause. The others are a blame and a solution.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Karthik's pilot meets the target, but the retest rate doubles. What should he do?",
        "options": ["Standardize anyway: the target is met",
                    "Investigate the guardrail before standardizing",
                    "Raise the target to 3% to be safe"],
        "correct": 1,
        "explanation": "A guardrail moved, so the change may be hiding failures in retests instead of removing them. Understand it before you standardize.",
        "q_script": "One more, and this one's a scenario. Karthik's pilot meets the target, but the "
                    "retest rate doubles. What should he do? Have a think.",
        "a_script": "Investigate before you standardize. A guardrail has moved, so the fix may be "
                    "hiding failures, not removing them.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
