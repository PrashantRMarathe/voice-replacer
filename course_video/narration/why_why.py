"""Why-Why Analysis (5 Why) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Neha, a
quality engineer chasing charging failures on mobile phone Line 2.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/why_why.py                      voice MISSING clips (bootstrap)
  python narration/import_clones.py why_why        import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "ww"
NAME = "why_why"

LETTERS = ["FMEA", "SOP", "HDMI"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return text.replace("5W2H", "five W two H")


INTRO_SCRIPT = (
    "Twenty-one phones failed charging at final test. The first answer came fast. "
    "Operator error. Two days later, it happened again. Sound familiar? In this lesson, "
    "you'll learn Why-Why analysis, often called five whys. You'll see how to dig past "
    "the easy answer, to a cause you can prove and control. We'll follow Neha, a quality "
    "engineer on a mobile phone line, as she does exactly that."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Start with a sharp problem, and protect your customer "
    "first. Back every why with evidence, and test it before you call it the root cause. "
    "And fix both how it happened, and why it escaped. Here's your action for this week. "
    "Take one repeat defect, and write its 5W2H statement. Great work completing this "
    "lesson. Next, you'll learn the X-Matrix, linking strategy to action."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Why-Why Is",
        "points": [("Ask why, again and again, with facts", "Why-Why analysis means"),
                   ("Five isn't a rule", "but five isn't a rule"),
                   ("Stop at a cause you can prove & control", "You stop when")],
        "example": "Charging failure is the symptom: connector seating, board damage, fixture contact or tester setup could cause it.",
        "example_cue": "On Neha's line",
        "script": "Here's the core idea. Why-Why analysis means asking why a problem happened, "
                  "again and again, with facts behind every answer. It's often called five whys, "
                  "but five isn't a rule. You stop when you reach a cause you can prove and "
                  "control. On Neha's line, charging failure is the symptom. It could be connector "
                  "seating, board damage, fixture contact, or tester setup. None of those is the "
                  "root cause until it's tested. So how does this fit with other tools?",
    },
    {
        "key": "p02", "num": 2, "title": "Why-Why & Root Cause Analysis",
        "points": [("One tool inside root cause analysis", "Why-Why is one tool"),
                   ("Go to the real place, see the real product", "Go to the real place"),
                   ("What evidence supports this why?", "ask what evidence"),
                   ("Human action is a clue, not the answer", "And treat human action")],
        "example": "Missing screws on an audio line: 'operator forgot' wasn't enough — the team checked the feeder and sequence.",
        "example_cue": "When screws went missing",
        "script": "Why-Why is one tool inside root cause analysis. Fishbones, Pareto charts, and "
                  "experiments sit alongside it. It works best for a clear chain of cause and "
                  "effect. Go to the real place, and look at the real product. At every step, ask "
                  "what evidence supports this why. And treat human action as a clue, not the final "
                  "answer. When screws went missing on an audio line, operator forgot wasn't "
                  "enough. The team checked the feeder and the sequence. So where do you start?",
    },
    {
        "key": "p03", "num": 3, "title": "Step 1: Define with 5W2H",
        "points": [("A sharp problem statement", "Start with a sharp"),
                   ("5W2H: what, where, when, how found, how many", "Use 5W2H"),
                   ("Include the last known good", "Include the last known good")],
        "example": "Line 2: 21 of 700 phones (3%) failed charging after the 11:00 fixture change; the shift before ran under 0.5%.",
        "example_cue": "On Line two",
        "script": "Start with a sharp problem statement. A vague problem gets vague answers. Use "
                  "5W2H. What failed, where, when, how it was found, and how many. Include the last "
                  "known good condition. Here's Neha's statement. On Line two, twenty-one of seven "
                  "hundred phones failed charging. That's three percent, right after an eleven "
                  "o'clock fixture change. The shift before ran under half a percent. Notice how "
                  "much that tells you already. But what about the phones already built?",
    },
    {
        "key": "p04", "num": 4, "title": "Step 2: Contain First",
        "points": [("Protect your customer first", "protect your customer"),
                   ("Find the last known good point", "Find the last known good"),
                   ("Hold stock physically and in the system", "Hold that stock"),
                   ("Reconcile every unit", "Then reconcile every unit")],
        "example": "Sorting 100% protects the customer — it doesn't prove you've removed the cause.",
        "example_cue": "Sorting a hundred percent",
        "script": "Before you analyze, protect your customer. Containment limits risk while the "
                  "investigation runs. Find the last known good point, and every serial or lot "
                  "built since. Hold that stock physically, and in the system too. Then reconcile "
                  "every unit. Screened, failed, reworked, released, or pending. Neha held every "
                  "phone built since the fixture change. But here's a trap. Sorting a hundred "
                  "percent protects the customer. It doesn't prove you've removed the cause. So "
                  "what comes next?",
    },
    {
        "key": "p05", "num": 5, "title": "Step 3: Facts at the Gemba",
        "points": [("Compare failed vs known-good units", "compare failed units"),
                   ("Check settings, fixtures, versions, lots", "Check settings"),
                   ("Preserve evidence before adjusting", "Preserve the evidence"),
                   ("Saw · source · might mean", "Keep three columns")],
        "example": "Neha photographed and labeled each failed phone by serial, then pulled the tester and maintenance logs.",
        "example_cue": "Neha photographed",
        "script": "Your analysis is only as good as your evidence. Go to the gemba, and compare "
                  "failed units with known-good ones. Check settings, fixtures, calibration, "
                  "software versions, and supplier lots. Preserve the evidence before anyone "
                  "adjusts anything. Neha photographed and labeled each failed phone by serial "
                  "number. Then she pulled the tester logs and the maintenance records. Keep three "
                  "columns. What you saw, where it came from, and what it might mean. Now you're "
                  "ready to ask why.",
    },
    {
        "key": "p06", "num": 6, "title": "Step 4: Build the Chain",
        "points": [("Start from the observed event", "Write the observed event"),
                   ("Each arrow is a claim you can check", "Each arrow is a claim"),
                   ("Facts, not 'carelessness'", "Use specific facts"),
                   ("Branch when causes combine", "Branch the chain")],
        "example": "Wrong carton label → old print job → software allowed it → printer not linked to the scanned product.",
        "example_cue": "A wrong carton label",
        "script": "Write the observed event at the top. Ask why it happened. Then ask why that "
                  "condition existed. Each arrow is a claim you must be able to check. Ask why the "
                  "defect occurred, never who to blame. Use specific facts, not labels like "
                  "carelessness. Here's a packing example. A wrong carton label traced back to an "
                  "old print job. The software allowed it, because the printer wasn't linked to "
                  "the scanned product. Branch the chain whenever more than one cause contributed.",
    },
    {
        "key": "p07", "num": 7, "title": "Occurrence, Escape & System",
        "points": [("Occurrence: how the defect was made", "The occurrence cause"),
                   ("Escape: why nobody caught it", "The escape cause"),
                   ("System: why controls missed the risk", "And the system cause"),
                   ("Each needs its own fix", "Each one needs")],
        "example": "Fixture allows partial battery seating (occurrence); final test missed intermittent contact (escape).",
        "example_cue": "On Neha's line",
        "script": "A complete analysis usually has more than one chain. The occurrence cause "
                  "explains how the defect was made. The escape cause explains why nobody caught "
                  "it. And the system cause explains why your controls missed the risk in the first "
                  "place. On Neha's line, a fixture could allow partial battery seating. That's "
                  "occurrence. The final test didn't check intermittent contact. That's escape. "
                  "Each one needs its own fix. But what if there are many possible causes?",
    },
    {
        "key": "p08", "num": 8, "title": "Fishbone & Pareto",
        "points": [("Fishbone: 6 cause groups", "A fishbone diagram groups"),
                   ("Pareto: rank by frequency", "A Pareto chart ranks"),
                   ("Rare safety risks still matter", "But a rare safety risk"),
                   ("A fishbone is guesses, not proof", "a fishbone is a list")],
        "example": "Neha's top two defect types made up 65% of the total — that's where she focused first.",
        "example_cue": "Neha's top two",
        "script": "When many causes are possible, start wide. A fishbone diagram groups ideas "
                  "under people, machine, method, material, measurement, and environment. A Pareto "
                  "chart ranks defects by how often they happen. Neha's top two defect types made "
                  "up sixty-five percent of the total. That's where she focused first. But a rare "
                  "safety risk still matters, even with a low count. And remember, a fishbone is a "
                  "list of guesses, not proof. So how do you prove a cause?",
    },
    {
        "key": "p09", "num": 9, "title": "Prove the Cause",
        "points": [("Predict what should change", "Before the trial"),
                   ("Keep other factors fixed", "Keep other factors fixed"),
                   ("Test good and bad, across shifts", "Test both good and bad")],
        "example": "Good vs worn fixture pins, with the same parts: the failures followed the worn pins.",
        "example_cue": "Neha suspected",
        "script": "A logical chain isn't enough. You have to test it. Before the trial, write down "
                  "what should change if your cause is true. Keep other factors fixed, like "
                  "material lot and program version. Test both good and bad conditions, across "
                  "shifts. Neha suspected a worn fixture pin. She tried good pins and worn pins, "
                  "with the same parts. The failures followed the worn pins. What "
                  "would have proved her wrong? Failures that stayed with the good pins.",
    },
    {
        "key": "p10", "num": 10, "title": "Corrective Action & Poka Yoke",
        "points": [("Fix the cause, not the symptom", "Now fix the cause"),
                   ("Engineered prevention beats reminders", "Engineered prevention"),
                   ("Fix occurrence + independent escape check", "Fix the occurrence"),
                   ("Update FMEA, SOP, training", "Then update the FMEA")],
        "example": "Wrong audio labels: the printer now needs a matching serial scan first. Retraining relies on memory.",
        "example_cue": "For wrong labels",
        "script": "Now fix the cause, not just the symptom. Engineered prevention beats reminders. "
                  "Think keyed fixtures, barcode interlocks, and presence sensors. Fix the "
                  "occurrence, and add an independent check for the escape. Then update the FMEA, "
                  "the SOP, and the training. For wrong labels on audio devices, the printer now "
                  "needs a matching serial scan first. Why is retraining usually a weak fix? "
                  "Because it relies on memory, and memory fails. How do you know your fix worked?",
    },
    {
        "key": "p11", "num": 11, "title": "Verify & Close",
        "points": [("Finished ≠ proven", "Finishing an action"),
                   ("Challenge: good, bad, boundary samples", "Challenge the new control"),
                   ("Watch recurrence and yield", "Watch recurrence"),
                   ("No new downtime or false rejects", "Check you haven't")],
        "example": "Neha's closure rule: zero repeats over 10 production days, challenge tests passed, every suspect unit accounted for.",
        "example_cue": "Neha set a closure rule",
        "script": "Finishing an action isn't the same as proving it works. Challenge the new "
                  "control with known-good, known-bad, and boundary samples. Watch recurrence and "
                  "first-pass yield across shifts, models, and changeovers. Check you haven't "
                  "created new downtime or false rejects. Neha set a closure rule with her plant. "
                  "Zero repeats over ten production days, challenge tests passed, and every suspect "
                  "unit accounted for. Your plant should set its own rule. Then Quality signs it off.",
    },
    {
        "key": "p12", "num": 12, "title": "Why-Why KPIs",
        "points": [("Measure speed and results", "Measure both speed"),
                   ("Leading: fast containment, verified actions", "Leading measures"),
                   ("Lagging: defect rate, recurrence", "Lagging measures"),
                   ("Keep definitions stable", "Keep the definitions stable")],
        "example": "50 → 15 defects = a 70% drop. ₹1.2 lakh cost, ₹30,000 saved a month = 4-month payback.",
        "example_cue": "Neha's defects fell",
        "script": "Measure both speed and results. Leading measures include fast containment and "
                  "verified actions. Lagging measures include defect rate and recurrence. Keep the "
                  "definitions stable, so nobody improves a number by changing it. Neha's defects "
                  "fell from fifty to fifteen, on the same volume. That's a seventy percent drop. "
                  "Her fix cost one point two lakh rupees, and saves thirty thousand a month. So it "
                  "pays back in four months. Which of these does your team track today?",
    },
    {
        "key": "p13", "num": 13, "title": "Case Study: Charging Failure",
        "points": [("Phone or tester? Test that first", "Was the fault in the phone"),
                   ("Retested on a second tester: still failed", "She retested the failed phones"),
                   ("Worn pin on the assembly fixture", "The battery connector sat"),
                   ("Fix: new pins, life limits, setup check", "Her fix was")],
        "example": "The failed phones failed again on a second tester: the phones really were faulty.",
        "example_cue": "They failed there too",
        "script": "Here's how Neha's case came together. Was the fault in the phone, or in the "
                  "tester? She retested the failed phones on a second tester. They failed there "
                  "too, so the phones really were faulty. The chain went like this. The battery "
                  "connector sat half-seated, because a worn spring pin on the new assembly fixture "
                  "didn't press it fully home. It was worn because no replacement interval existed. Her fix was "
                  "new pins, life limits, and a setup check. Would you have checked the tester first?",
    },
    {
        "key": "p14", "num": 14, "title": "Set-Top Box & Audio",
        "points": [("Different products, different evidence", "Different products need"),
                   ("Set-top box: HDMI soldering, firmware, tester", "On a set-top box"),
                   ("Audio: trace kit, packing sequence, scans", "On an audio device"),
                   ("Deploy proven fixes to similar lines", "Once a fix is proven")],
        "example": "Missing remote: the kit skipped it, then the carton closed without a remote scan.",
        "example_cue": "The kit skipped the remote",
        "script": "Different products need different evidence. On a set-top box with no display, "
                  "you'd check the HDMI soldering, firmware, and tester settings. And you'd ask why "
                  "the end-of-line display check missed it. On an audio device missing its remote, "
                  "you'd trace the kit, the packing sequence, and the scans. The kit skipped the "
                  "remote. Then the carton closed without a remote scan. Once a fix is proven, "
                  "deploy it to similar lines too. Ready for the rollout plan?",
    },
    {
        "key": "p15", "num": 15, "title": "90-Day Deployment",
        "points": [("Pilot line + a few facilitators", "Start with one high-risk"),
                   ("Days 1–30: triggers, roles, templates", "In the first thirty days"),
                   ("Days 31–60: investigate, test hypotheses", "In the next thirty"),
                   ("Days 61–90: challenge, update, spread", "In the last thirty")],
        "example": "Audit for real samples and verified links — not neat forms.",
        "example_cue": "Audit for real samples",
        "script": "Make Why-Why part of daily management. Start with one high-risk pilot line, and "
                  "train a few facilitators. In the first thirty days, define triggers, roles, and "
                  "templates. In the next thirty, run real investigations and test your hypotheses. "
                  "In the last thirty, challenge-test the fixes, update controls, and spread the "
                  "lessons. Audit for real samples and verified links, not neat forms. Remember, "
                  "ask why until you can prove the cause. Then make it impossible to repeat.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Why?", "sub": "Backed by a fact", "icon": "search", "with": 0},
        {"label": "Why again?", "sub": "Five isn't a rule", "icon": "count", "with": 1},
        {"label": "A cause you can prove & control", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Connector seating", "icon": "pin", "with": "example"},
            {"label": "Board damage", "icon": "chip", "with": "example"},
            {"label": "Fixture contact", "icon": "wrench", "with": "example"},
            {"label": "Tester setup", "icon": "test", "with": "example"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Why-Why", "sub": "One tool of many", "icon": "search", "tone": "good", "with": 0},
        {"label": "Real place, real product", "icon": "walk", "with": 1},
        {"label": "Evidence for every why", "icon": "clipboard", "with": 2},
        {"label": "People are a clue", "icon": "person", "with": 3}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Operator forgot", "sub": "Not enough", "icon": "person", "with": "example"},
            {"label": "Check the feeder and sequence", "sub": "Facts", "icon": "search", "with": "example"}]}},
    "p03": {"type": "doc", "items": [
        {"label": "Problem statement · Line 2", "icon": "label", "with": 0},
        {"label": "What: charging failure at final test", "icon": "power", "with": 1},
        {"label": "When: after the 11:00 fixture change", "icon": "clock", "with": 1},
        {"label": "How many: 21 of 700 phones (3%)", "icon": "count", "with": 1},
        {"label": "Last known good: under 0.5%", "icon": "check", "with": 2}]},
    "p04": {"type": "flow", "items": [
        {"label": "Protect the customer", "icon": "shield", "with": 0},
        {"label": "Find the last known good", "icon": "search", "with": 1},
        {"label": "Hold stock: floor and system", "icon": "lock", "with": 2},
        {"label": "Reconcile every unit", "icon": "count", "tone": "good", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Failed vs known-good", "icon": "scale", "with": 0},
        {"label": "Settings, versions, lots", "icon": "gear", "with": 1},
        {"label": "Preserve the evidence", "icon": "camera", "with": 2},
        {"label": "Saw · source · meaning", "icon": "clipboard", "with": 3}]},
    "p06": {"type": "icons", "items": [
        {"label": "Start from the event", "icon": "search", "with": 0},
        {"label": "Each arrow: a claim to check", "icon": "check", "with": 1},
        {"label": "Facts, not labels", "icon": "cross", "tone": "bad", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Wrong carton label", "icon": "label", "tone": "bad", "with": "example"},
            {"label": "Old print job", "icon": "sequence", "with": "example"},
            {"label": "Software allowed it", "icon": "chip", "with": "example"},
            {"label": "Printer not linked to the scan", "icon": "barcode", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Occurrence", "sub": "How it was made", "icon": "wrench", "with": 0},
        {"label": "Escape", "sub": "Why nobody caught it", "icon": "search", "with": 1},
        {"label": "System", "sub": "Why controls missed it", "icon": "gear", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Fixture allows partial seating", "sub": "Occurrence", "icon": "pin", "tone": "bad", "with": "example"},
            {"label": "Final test misses intermittent contact", "sub": "Escape", "icon": "test", "tone": "bad", "with": "example"},
            {"label": "A fix for each", "icon": "check", "tone": "good", "with": 3}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Fishbone: 6 groups", "icon": "gear", "with": 0},
        {"label": "Pareto: rank by count", "icon": "chartUp", "with": 1},
        {"label": "Rare safety risks", "icon": "warning", "tone": "bad", "with": 2},
        {"label": "Guesses, not proof", "icon": "search", "with": 3}],
        "then": {"type": "bars", "label": "", "note": "Top two = 65% of defects", "with": "example", "items": [
            {"label": "Type 1", "value": 40, "tone": "bad", "with": "example"},
            {"label": "Type 2", "value": 25, "tone": "bad", "with": "example"},
            {"label": "Type 3", "value": 15, "with": "example"},
            {"label": "Type 4", "value": 12, "with": "example"},
            {"label": "Other", "value": 8, "with": "example"}]}},
    "p09": {"type": "steps", "items": [
        {"label": "Predict the change", "with": 0}, {"label": "Fix other factors", "with": 1},
        {"label": "Test good and bad", "with": 2}, {"label": "Across shifts", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Worn pins", "sub": "Failures followed", "icon": "pin", "with": "example"},
            {"label": "Good pins", "sub": "Same parts passed", "icon": "check", "with": "example"}]}},
    "p10": {"type": "ladder", "top": "STRONGEST", "bottom": "WEAKEST", "items": [
        {"label": "Keyed fixture, interlock", "icon": "key", "with": 1},
        {"label": "Presence sensor", "icon": "sensor", "with": 1},
        {"label": "Independent escape check", "icon": "search", "with": 2},
        {"label": "Retraining, reminders", "icon": "warning", "tone": "bad", "with": "example"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Known-good", "icon": "check", "tone": "good", "with": 1},
        {"label": "Known-bad", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Boundary samples", "icon": "scale", "with": 1},
        {"label": "Recurrence and yield", "icon": "chartUp", "with": 2}],
        "then": {"type": "doc", "with": "example", "items": [
            {"label": "Closure rule · Line 2", "icon": "label", "with": "example"},
            {"label": "Zero repeats in 10 production days", "icon": "calendar", "with": "example"},
            {"label": "Challenge tests passed", "icon": "test", "with": "example"},
            {"label": "Every suspect unit accounted for", "icon": "count", "with": "example"},
            {"label": "Quality signs it off", "icon": "person", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Speed and results", "icon": "clock", "with": 0},
        {"label": "Leading: fast containment", "icon": "shield", "with": 1},
        {"label": "Lagging: defects, repeats", "icon": "chartDown", "with": 2},
        {"label": "Stable definitions", "icon": "scale", "with": 3}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 50}, "after": {"label": "After", "value": 15},
                 "unit": "charging defects, same volume", "note": "A 70% drop · 4-month payback", "with": "example"}},
    "p13": {"type": "flow", "items": [
        {"label": "Phone or tester?", "icon": "search", "with": 0},
        {"label": "Second tester: still failed", "icon": "test", "with": 1},
        {"label": "Worn assembly-fixture pin, no replacement interval", "icon": "pin", "tone": "bad", "with": 2},
        {"label": "New pins, life limits, setup check", "icon": "check", "tone": "good", "with": 3}]},
    "p14": {"type": "icons", "items": [
        {"label": "Set-top box", "sub": "HDMI, firmware, tester", "icon": "chip", "with": 1},
        {"label": "Audio device", "sub": "Kit, sequence, scans", "icon": "wave", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Kit skipped the remote", "icon": "tray", "tone": "bad", "with": "example"},
            {"label": "Carton closed, no remote scan", "icon": "box", "tone": "bad", "with": "example"},
            {"label": "Spread the proven fix", "icon": "sequence", "tone": "good", "with": 3}]}},
    "p15": {"type": "timeline", "items": [
        {"label": "Triggers, roles, templates", "sub": "Days 1–30", "icon": "clipboard", "with": 1},
        {"label": "Investigate, test hypotheses", "sub": "31–60", "icon": "search", "with": 2},
        {"label": "Challenge, update, spread", "sub": "61–90", "icon": "chartUp", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "Final test didn't detect a half-seated battery connector. What kind of cause is that?",
        "options": ["Occurrence cause", "Escape cause", "System cause"],
        "correct": 1,
        "explanation": "The defect was made earlier (occurrence). The escape cause explains why the detection barrier — here, final test — didn't catch it.",
        "q_script": "Quick check. The final test didn't detect a half-seated battery connector. "
                    "What kind of cause is that? Take a few seconds.",
        "a_script": "It's an escape cause. The defect was made earlier. The escape explains why "
                    "our checks didn't catch it.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "30 cartons got wrong labels and someone says “operator error”. What should the team do FIRST?",
        "options": ["Retrain the operator and close it", "Contain suspect cartons, then ask why the process allowed it",
                    "Put a reminder sign at packing"],
        "correct": 1,
        "explanation": "Contain first, then find why the process allowed a wrong label at all. Retraining or a sign relies on memory, so it rarely stops a repeat.",
        "q_script": "One more, and this one's a scenario. Thirty cartons got wrong labels, and "
                    "someone says operator error. What should the team do first? Have a think.",
        "a_script": "Contain the suspect cartons first. Then ask why the process allowed a wrong "
                    "label at all. Retraining or a sign relies on memory, so it rarely stops a repeat.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
