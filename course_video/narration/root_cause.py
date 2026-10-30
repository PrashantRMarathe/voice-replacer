"""Root Cause Analysis (RCA) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Lakshmi,
a quality engineer at a network-camera plant, investigating focus failures
on Line 3 after a changeover — and refusing to stop at the first plausible story.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/root_cause.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py root_cause  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "rc"
NAME = "root_cause"

LETTERS = ["RCA", "QRQC", "FMEA", "SOP", "MES", "SMT", "AOI", "FPY", "DOE", "SKU", "NVR", "PCB", "WIP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return text.replace("5W2H", "five W two H")


INTRO_SCRIPT = (
    "Thirty-six cameras failed focus test in one morning. Within an hour, three people had "
    "three different answers. The fixture. The lens. The tester. Who was right? In this "
    "lesson, you'll learn Root Cause Analysis. You'll see how to move from a symptom to a "
    "cause you can prove, and stop it for good. We'll follow Lakshmi, a quality engineer at "
    "a camera plant, as she finds out."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Define the problem sharply, and protect your customer "
    "first. Treat every cause as a hypothesis until a test proves it. And fix both why it "
    "happened, and why it escaped. Here's your action for this week. Take one closed "
    "problem, and check whether its root cause was ever actually tested. Great work "
    "completing this lesson. Next, you'll learn the Skill Training Matrix."
)

# One story thread: Lakshmi's network-camera plant. Line 3: 36 of 1,200 units fail
# focus after the 10:00 changeover (3.0% vs 0.5% baseline); Line 2 has no failures.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What RCA Is",
        "points": [("Symptom: what you observe", "The symptom is"),
                   ("Mechanism: how it happened", "The mechanism is"),
                   ("Root cause: controllable, with evidence", "The root cause is")],
        "example": "Blurry image = the symptom. A wrong spacer might be the cause — not confirmed until it's tested.",
        "example_cue": "On Lakshmi's line",
        "script": "Here's the core idea. Root Cause Analysis is an evidence-based investigation "
                  "into why something went wrong. It separates three things. The symptom is what "
                  "you observe. The mechanism is how it happened. The root cause is a condition "
                  "you can control, backed by evidence. On Lakshmi's line, a blurry image is the "
                  "symptom. A wrong spacer might be the cause. But nothing is confirmed until "
                  "it's tested. Where does this fit?",
    },
    {
        "key": "p02", "num": 2, "title": "RCA in the Quality System",
        "points": [("Detect a deviation", "First, you detect"),
                   ("Contain to protect the customer", "Then you contain it"),
                   ("Investigate with real data", "Next, you investigate"),
                   ("Correct, then verify over time", "You correct the verified")],
        "example": "A successful sort protects the customer — it doesn't prove the cause is gone.",
        "example_cue": "A successful sort protects",
        "script": "RCA is one link in a closed loop. First, you detect a deviation. Then you "
                  "contain it, to protect your customer. Next, you investigate with real data. "
                  "You correct the verified causes, and verify the result over time. It sits "
                  "alongside QRQC, the FMEA, control plans and Poka Yoke. And here's a key "
                  "point. A successful sort protects the customer. But does it prove the cause "
                  "is gone? Not at all.",
    },
    {
        "key": "p03", "num": 3, "title": "Define: 5W2H & Is / Is Not",
        "points": [("Sharp, measurable problem", "starts with a sharp"),
                   ("5W2H captures the facts", "Use 5W2H"),
                   ("Is / Is Not: where it occurs, and doesn't", "called Is, Is Not")],
        "example": "Line 3: 36 of 1,200 cameras failed focus after the 10:00 changeover. Line 2, another fixture: none.",
        "example_cue": "Lakshmi's statement was clear",
        "script": "Every good RCA starts with a sharp, measurable problem. Use 5W2H to capture "
                  "the facts. Then add a powerful comparison, called Is, Is Not. Where does the "
                  "problem occur, and where doesn't it? Lakshmi's statement was clear. On Line "
                  "three, thirty-six of twelve hundred cameras failed focus. It started after "
                  "the ten o'clock changeover. Line two, with a different fixture, had none. What "
                  "does that comparison tell you?",
    },
    {
        "key": "p04", "num": 4, "title": "Evidence & Traceability",
        "points": [("Gather evidence before changing settings", "gather the evidence"),
                   ("Keep failed and known-good samples", "Keep failed parts"),
                   ("Pull MES records, test logs, alarms", "Pull the MES records"),
                   ("Record every recent change", "Record every recent change"),
                   ("Check gauge calibration", "And confirm your gauges")],
        "example": "Lakshmi bagged ten failed and ten good cameras before anyone touched the fixture.",
        "example_cue": "Lakshmi bagged ten",
        "script": "It points at the changeover. But first, gather the evidence, before anyone "
                  "changes a setting. Keep failed parts and known-good samples. Pull the MES "
                  "records, test logs and machine alarms. Record every recent change, in "
                  "tooling, firmware, recipe and material lot. And confirm your gauges are "
                  "calibrated before trusting small differences. Lakshmi bagged ten failed and "
                  "ten good cameras. Could another engineer repeat your findings from your "
                  "evidence?",
    },
    {
        "key": "p05", "num": 5, "title": "Pareto: Pick Your Battle",
        "points": [("Rank by count, cost or risk", "Rank your defect types"),
                   ("Sort and add the running %", "Sort them"),
                   ("Split the top one by shift, station, supplier", "Then split the top one"),
                   ("Severe risks jump the queue", "A severe safety")],
        "example": "Wrong PCB 40 · missing screw 25 · focus 20 · label 10 · other 5 → top three = 85%.",
        "example_cue": "On Lakshmi's line, three",
        "script": "When you face many problems, Pareto helps you choose. Rank your defect types "
                  "by count, cost or risk. Sort them, and add up the running percentage. Often "
                  "a few causes make most of the loss. On Lakshmi's line, three defect types "
                  "made up eighty-five percent. Then split the top one by shift, station or "
                  "supplier. But one warning. A severe safety or customer risk jumps the queue, "
                  "whatever its rank. So how do you dig in?",
    },
    {
        "key": "p06", "num": 6, "title": "5 Why: Test the Chain",
        "points": [("Five isn't a rule", "Five isn't a rule"),
                   ("Evidence for every link", "Each link needs evidence"),
                   ("Branch when there's more than one cause", "Branch when"),
                   ("Never stop at 'operator error'", "never stop at operator error")],
        "example": "Missing screw → cycle finished without confirming it → torque signal not linked to MES.",
        "example_cue": "Take a missing screw",
        "script": "Use five whys, but treat it as a chain of claims to check. Five isn't a rule. "
                  "Each link needs evidence. Branch when there's more than one cause. And never "
                  "stop at operator error, or lack of training. Ask what in the work design "
                  "allowed it. Take a missing screw. The station let the cycle finish without "
                  "confirming the screw. Why? The torque signal wasn't linked to MES. A plausible "
                  "story isn't proof. Have you checked the logs?",
    },
    {
        "key": "p07", "num": 7, "title": "Fishbone & the 6M",
        "points": [("Fishbone = Ishikawa diagram", "The fishbone, or Ishikawa"),
                   ("People · machine · method", "People, machine, method"),
                   ("Material · measurement · environment", "material, measurement and environment"),
                   ("It doesn't prove which cause is true", "A fishbone doesn't prove")],
        "example": "Lakshmi's fishbone: fixture wear, wrong recipe, lens tolerance, tester repeatability, handling, heat.",
        "example_cue": "Lakshmi's team filled it in",
        "script": "The fishbone, or Ishikawa diagram, organizes your ideas. It has six "
                  "branches. People, machine, method, material, measurement and environment. "
                  "Lakshmi's team filled it in. Fixture wear, a wrong recipe, lens tolerance, "
                  "tester repeatability, handling, and heat. That's a great list of suspects. "
                  "But here's the key point. A fishbone doesn't prove which cause is true. For "
                  "each branch, you write the test that would confirm or reject it. What changed?",
    },
    {
        "key": "p08", "num": 8, "title": "Change Analysis & Fault Trees",
        "points": [("Change analysis: failing vs last stable", "That's change analysis"),
                   ("Fault tree: work back with AND / OR", "use a fault tree"),
                   ("Together ≠ cause", "Just because two things")],
        "example": "No picture escapes only if the firmware is wrong AND the interlock is missing.",
        "example_cue": "A video recorder escapes",
        "script": "That's change analysis. You compare the failing condition with the last "
                  "stable one, and list every change in between. For complex problems, use a "
                  "fault tree. It works backward from the failure, with and, or logic. A video "
                  "recorder escapes with no picture only if the firmware is wrong, and the "
                  "interlock is missing. But careful. Just because two things happened together "
                  "doesn't mean one caused the other. So how do you prove it?",
    },
    {
        "key": "p09", "num": 9, "title": "Test Your Hypothesis",
        "points": [("Write a prediction", "Write a prediction"),
                   ("One factor at a time, or a DOE", "Change one factor"),
                   ("Enough samples, repeated", "Use enough samples"),
                   ("Check the gauge first", "she checked the gauge first")],
        "example": "Approved vs suspect spacers, with the same camera, recipe and room.",
        "example_cue": "Lakshmi compared approved",
        "script": "Write a prediction. If the spacer is wrong, focus failures should rise. Then "
                  "test it. Change one factor at a time, or use a planned experiment, called a "
                  "DOE, when factors interact. Use enough samples, and repeat the trial. Lakshmi "
                  "compared approved and suspect spacers, with the same camera, recipe and room. "
                  "And she checked the gauge first. If your measurement varies a lot, even a "
                  "real difference can hide. Ready for the fix?",
    },
    {
        "key": "p10", "num": 10, "title": "Contain vs Correct vs Prevent",
        "points": [("Contain: protect the customer now", "Containment protects"),
                   ("Correct: remove the verified cause", "Corrective action removes"),
                   ("Prevent: spread to similar lines", "And preventive action"),
                   ("Fix the escape cause too", "Fix the escape cause")],
        "example": "Wrong board: scan the held stock → add an MES match → copy it to other variants.",
        "example_cue": "For a wrong board",
        "script": "Keep three actions apart. Containment protects your customer now. Corrective "
                  "action removes the verified cause. And preventive action spreads the lesson "
                  "to similar lines. Fix the escape cause too, with an interlock or a presence "
                  "check. For a wrong board, you scan the held stock. Then you add an MES "
                  "match, and copy it to other variants. One rule. Never release held stock just "
                  "because the fix was ordered. How do you make it last?",
    },
    {
        "key": "p11", "num": 11, "title": "Link to FMEA & Poka Yoke",
        "points": [("Link each cause to a failure mode", "Link each confirmed cause"),
                   ("Update the control plan", "Update the control plan"),
                   ("Validate Poka Yoke: good, bad, borderline", "Validate any Poka Yoke"),
                   ("Update SOP, training, audits", "Then update the SOP")],
        "example": "Ask: does the new control prevent the error, detect it, or only make it visible?",
        "example_cue": "Does the new control prevent",
        "script": "Feed what you learned back into the system. Link each confirmed cause to a "
                  "failure mode in your FMEA, and reassess the risk. Update the control plan, "
                  "with the method, the reaction and the owner. Validate any Poka Yoke with "
                  "known good, known bad and borderline parts. Then update the SOP, training "
                  "and audit questions. Ask yourself one question. Does the new control prevent "
                  "the error, detect it, or only make it visible?",
    },
    {
        "key": "p12", "num": 12, "title": "RCA Metrics",
        "points": [("Don't count closed forms as success", "Don't claim success"),
                   ("Defect rate ≠ first pass yield", "Track the defect rate"),
                   ("Track repeats after closure", "Track how often"),
                   ("Cost and payback", "What does it cost")],
        "example": "60 → 12 defects per 20,000: an 80% cut. ₹90,000 control saving ₹15,000/month = 6-month payback.",
        "example_cue": "A control that cuts defects",
        "script": "Measure both the quality of your investigations, and their business impact. "
                  "Don't claim success just because a form was closed. Track the defect rate, "
                  "and first pass yield, but never mix them up. Track how often problems come "
                  "back after closure. A control that cuts defects by eighty percent sounds "
                  "great. What does it cost, and how fast does it pay back? Lakshmi's paid back "
                  "in six months. Now, her full case.",
    },
    {
        "key": "p13", "num": 13, "title": "Case Study: Focus Failure",
        "points": [("Held every camera since the last good first-off", "Lakshmi held every camera"),
                   ("Four suspects: spacer, recipe, seating, tester", "Her team listed four"),
                   ("Measured, compared logs, cross-over test", "They measured the spacers"),
                   ("Keyed spacer + fixture scan linked to recipe", "The fix was a keyed spacer")],
        "example": "Swapping spacers moved the failures. Swapping testers didn't. That was the proof.",
        "example_cue": "Swapping spacers moved",
        "script": "Lakshmi held every camera since the last validated first-off unit. Her team "
                  "listed four suspects. Spacer thickness, a recipe mismatch, lens seating, and "
                  "tester drift. They measured the spacers, compared the logs, and ran a "
                  "cross-over test. Swapping spacers moved the failures. Swapping testers didn't. "
                  "Now they had proof. The fix was a keyed spacer, and a fixture scan linked to "
                  "the recipe. What evidence would you have needed?",
    },
    {
        "key": "p14", "num": 14, "title": "Two More Cases: SMT & Label",
        "points": [("Board line: wrong component placed", "On the board line"),
                   ("Fix: feeder interlock against the BOM", "The fix was a feeder"),
                   ("Packing: carton label ≠ device", "At packing"),
                   ("Fix: box can't close until all match", "That fix blocked")],
        "example": "Both fixes were challenge-tested before closure.",
        "example_cue": "Both fixes were",
        "script": "Two shorter cases show the same pattern. On the board line, a wrong component "
                  "was placed. The team compared the bill of materials, the feeder setup, the "
                  "reel barcode and AOI images. The fix was a feeder interlock against the bill. "
                  "At packing, a carton label didn't match the device. That fix blocked the box "
                  "from closing until serial, SKU and label all agreed. Both fixes were "
                  "challenge-tested. Could you prove every suspect unit was found?",
    },
    {
        "key": "p15", "num": 15, "title": "90-Day Deployment",
        "points": [("Days 1–30: triggers, roles, forms, pilots", "In the first thirty days"),
                   ("Days 31–60: train, investigate", "In the next thirty"),
                   ("Days 61–90: audit, update FMEA, expand", "In the last thirty"),
                   ("Closure: reconciled, verified, tested", "Before you close any problem")],
        "example": "Make RCA a routine, not a one-time workshop.",
        "example_cue": "Make RCA a routine",
        "script": "Make RCA a routine, not a one-time workshop. In the first thirty days, define "
                  "your triggers, roles, forms and pilot areas. In the next thirty, train teams, "
                  "and run real investigations. In the last thirty, audit the results, update "
                  "your FMEA and control plans, and expand. Before you close any problem, check "
                  "it. Is containment reconciled? Are the causes verified, and the actions "
                  "tested? Prove the cause, then prevent it.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Symptom", "sub": "A blurry image", "icon": "camera", "tone": "bad"},
        {"label": "Mechanism", "sub": "How it happened", "icon": "gear"},
        {"label": "Root cause", "sub": "A wrong spacer? Test it first", "icon": "search"}]},
    "p02": {"type": "flow", "items": [
        {"label": "Detect", "icon": "sensor"}, {"label": "Contain", "icon": "lock"},
        {"label": "Investigate with data", "icon": "search"},
        {"label": "Correct, verify over time", "icon": "check", "tone": "good"}]},
    "p03": {"type": "compare", "before": {"label": "Line 3", "value": 36}, "after": {"label": "Line 2", "value": 0},
            "unit": "focus failures after the changeover (Line 2 has another fixture)",
            "note": "Is / Is Not points at the fixture", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Evidence first", "icon": "search"}, {"label": "Failed + good samples", "icon": "box"},
        {"label": "Logs and alarms", "icon": "clipboard"}, {"label": "Recent changes", "icon": "sequence"},
        {"label": "Calibration", "icon": "scale"}]},
    "p05": {"type": "bars", "label": "", "note": "Top three = 85% of defects", "items": [
        {"label": "Wrong PCB", "value": 40, "tone": "bad", "with": "example"},
        {"label": "Missing screw", "value": 25, "tone": "bad", "with": "example"},
        {"label": "Focus", "value": 20, "tone": "bad", "with": "example"},
        {"label": "Label", "value": 10, "with": "example"},
        {"label": "Other", "value": 5, "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Five isn't a rule", "icon": "count"}, {"label": "Evidence per link", "icon": "search"},
        {"label": "Branch when needed", "icon": "sequence"}, {"label": "Never 'operator error'", "icon": "cross", "tone": "bad"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "A missing screw", "icon": "screw", "tone": "bad", "with": "example"},
            {"label": "Why? The cycle finished anyway", "icon": "sequence", "with": "example"},
            {"label": "Why? Torque not linked to MES", "icon": "chip", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "People", "sub": "Handling", "icon": "person", "with": 1},
        {"label": "Machine", "sub": "Fixture wear", "icon": "gear", "with": 1},
        {"label": "Method", "sub": "Wrong recipe", "icon": "clipboard", "with": 1},
        {"label": "Material", "sub": "Lens tolerance", "icon": "box", "with": 2},
        {"label": "Measurement", "sub": "Tester repeatability", "icon": "scale", "with": 2},
        {"label": "Environment", "sub": "Heat", "icon": "wave", "with": 2}]},
    "p08": {"type": "icons", "items": [
        {"label": "Change analysis", "sub": "Failing vs last stable", "icon": "sequence", "with": 0},
        {"label": "Fault tree", "sub": "AND / OR, worked backward", "icon": "gear", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Firmware is wrong", "icon": "chip", "tone": "bad", "with": "example"},
            {"label": "AND the interlock is missing", "icon": "lock", "tone": "bad", "with": "example"},
            {"label": "A no-picture unit escapes", "icon": "box", "tone": "bad", "with": "example"}]}},
    "p09": {"type": "icons", "items": [
        {"label": "Write a prediction", "icon": "clipboard"}, {"label": "One factor, or a DOE", "icon": "gear"},
        {"label": "Enough samples", "icon": "stack"}, {"label": "Check the gauge", "icon": "scale"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Suspect spacer", "sub": "Same camera, recipe, room", "icon": "shape"},
            {"label": "Approved spacer", "sub": "Same camera, recipe, room", "icon": "shape"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Contain", "sub": "Scan the held stock", "icon": "lock"},
        {"label": "Correct", "sub": "Add an MES match", "icon": "barcode"},
        {"label": "Prevent", "sub": "Copy it to other variants", "icon": "sequence", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "FMEA", "icon": "clipboard"}, {"label": "Control plan", "icon": "shield"},
        {"label": "Validate Poka Yoke", "icon": "test"}, {"label": "SOP, training, audits", "icon": "person"}],
        "then": {"type": "ladder", "top": "BEST", "bottom": "WEAKEST", "with": "example", "items": [
            {"label": "Prevents the error", "icon": "key", "with": "example"},
            {"label": "Detects it", "icon": "sensor", "with": "example"},
            {"label": "Only makes it visible", "icon": "search", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Closed form ≠ success", "icon": "cross", "tone": "bad"},
        {"label": "Defect rate vs FPY", "icon": "chartUp"},
        {"label": "Repeats after closure", "icon": "sequence"}, {"label": "Cost and payback", "icon": "calendar"}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 60}, "after": {"label": "After", "value": 12},
                 "unit": "defects per 20,000 cameras", "note": "80% fewer, 6-month payback", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Hold since the last good first-off", "icon": "lock"},
        {"label": "Four suspects listed", "icon": "search"},
        {"label": "Cross-over test", "sub": "Spacers moved it; testers didn't", "icon": "test"},
        {"label": "Keyed spacer + fixture scan", "icon": "key", "tone": "good"}]},
    "p14": {"type": "icons", "items": [
        {"label": "Wrong component", "sub": "Board line", "icon": "chip", "tone": "bad"},
        {"label": "Feeder interlock", "sub": "Checked against the BOM", "icon": "lock", "tone": "good"},
        {"label": "Label ≠ device", "sub": "Packing", "icon": "label", "tone": "bad"},
        {"label": "Box can't close", "sub": "Until all three match", "icon": "box", "tone": "good"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Triggers, roles, forms, pilots", "sub": "Days 1–30", "icon": "clipboard", "with": 0},
        {"label": "Train, run real investigations", "sub": "31–60", "icon": "person", "with": 1},
        {"label": "Audit, update FMEA, expand", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "A team's fishbone diagram lists six possible causes. What does it prove?",
        "options": ["The biggest branch is the root cause", "Nothing yet — each cause must be tested",
                    "All six causes are true"],
        "correct": 1,
        "explanation": "A fishbone organizes hypotheses. It proves nothing until each candidate is confirmed or rejected by a test.",
        "q_script": "Quick check. A team's fishbone diagram lists six possible causes. What "
                    "does it prove? Take a few seconds.",
        "a_script": "Nothing yet. A fishbone is a list of hypotheses. Each one must be tested "
                    "before you call it a cause.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A wrong-PCB defect is found. The new MES interlock has been ordered but isn't installed. Can the held WIP be released?",
        "options": ["Yes — the fix is on its way", "No — release only after screening and authorized disposition",
                    "Yes, if the operator is retrained", "Yes, if the next shift is told"],
        "correct": 1,
        "explanation": "Ordering a fix doesn't protect the customer. Held stock is released only after it's screened and dispositioned through the Quality process.",
        "q_script": "One more, and this one's a scenario. A wrong board defect is found. The new "
                    "interlock has been ordered, but isn't installed. Can the held stock be "
                    "released? Have a think.",
        "a_script": "No. Release it only after screening, and an authorized decision. Ordering a "
                    "fix doesn't protect your customer.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
