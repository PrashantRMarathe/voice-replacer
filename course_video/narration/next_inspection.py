"""Next Inspection lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Anita,
a quality engineer on a security-camera assembly line, stopping defects from
travelling downstream to test and packing.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/next_inspection.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py next_inspection  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "ni"
NAME = "next_inspection"

LETTERS = ["CTQ", "SOP", "FPY", "PCB", "SMT", "AOI", "MES", "FMEA", "MSA", "LPA", "PPM"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    return re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)


INTRO_SCRIPT = (
    "One loose connector, at station three. Nobody noticed. It traveled through four more "
    "stations, final test and packing. Then a customer opened the box. Sound familiar? In "
    "this lesson, you'll learn Next Inspection. You'll see how every process can protect "
    "the next one, and catch defects where they start. We'll follow Anita, a quality "
    "engineer on a security camera line, as she does exactly that."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Don't make, don't pass, and don't accept a defect. "
    "Check critical points at the earliest place you can, and react fast. And keep moving "
    "your controls upstream, toward prevention. Here's your action for this week. Pick "
    "one hand-off on your line, and write down what the next process needs from it. "
    "Great work completing this lesson. Next, you'll learn the One Point Lesson."
)

# One story thread: Anita's security-camera line. Assembly -> firmware -> test ->
# packing. Loose connectors and wrong labels were escaping downstream.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Next Inspection Is",
        "points": [("Each process protects the next one", "each process protects"),
                   ("Confirm critical points before hand-off", "Before you hand work on"),
                   ("Don't make a defect", "Don't make a defect"),
                   ("Don't pass a defect", "Don't pass a defect"),
                   ("Don't accept a defect", "Don't accept a defect")],
        "example": "Anita's housing station now checks the connector lock first.",
        "example_cue": "On Anita's line",
        "script": "Here's the core idea. Next Inspection means each process protects the next "
                  "one. Before you hand work on, you confirm the critical points. And the "
                  "receiving station doesn't quietly accept a defect. It sends it straight back. "
                  "Three rules sum it up. Don't make a defect. Don't pass a defect. Don't accept "
                  "a defect. On Anita's line, the housing station now checks the connector lock "
                  "first. So why does this matter so much?",
    },
    {
        "key": "p02", "num": 2, "title": "Why Catch It Early",
        "points": [("Defects cost more at every step", "A defect gets more expensive"),
                   ("Early detection = fast feedback", "Early detection also"),
                   ("More inspection ≠ quality", "More inspection doesn't")],
        "example": "Loose connector: seconds to fix at assembly → open, repair, retest after test → a return at the customer.",
        "example_cue": "At assembly, a loose",
        "script": "A defect gets more expensive at every step it travels. At assembly, a loose "
                  "connector takes seconds to fix. After test, you open the housing, repair and "
                  "retest. At the customer, it's a return, and a hit to your name. Early "
                  "detection also gives fast feedback. The cause is still fresh, so it's easy to "
                  "find. But here's a warning. More inspection doesn't create quality. So "
                  "where should checks happen?",
    },
    {
        "key": "p03", "num": 3, "title": "Three Levels of Inspection",
        "points": [("Source: check the condition first", "Source inspection checks"),
                   ("Self: check your own output", "Self inspection means"),
                   ("Next process: check before accepting", "Next process inspection means")],
        "example": "Anita's line: a sensor checks orientation, the assembler confirms the lock, the tester confirms the model.",
        "example_cue": "On Anita's line",
        "script": "There are three levels. Source inspection checks the condition that could "
                  "create the defect, before it happens. Self inspection means you check your "
                  "own output, right where you made it. Next process inspection means the "
                  "receiving station checks before it accepts. On Anita's line, a sensor checks "
                  "orientation. The assembler confirms the lock. And the tester confirms the "
                  "model. Which level is strongest? The one closest to the source.",
    },
    {
        "key": "p04", "num": 4, "title": "The Next Process Is My Customer",
        "points": [("The next process is your customer", "The next process is your customer"),
                   ("Right product, quantity, quality, label, timing", "It needs the right product"),
                   ("Never knowingly pass an abnormal unit", "Never knowingly pass"),
                   ("Raise it through Andon", "Raise it through Andon")],
        "example": "Anita's assemblers asked the firmware team: what do you need from us?",
        "example_cue": "Anita's assemblers simply asked",
        "script": "Think of every hand-off as a sale. The next process is your customer. It "
                  "needs the right product, the right quantity and quality, and the right label "
                  "and timing. So follow the SOP, and confirm your critical points. Never knowingly "
                  "pass an abnormal unit. Raise it through Andon instead. Anita's assemblers "
                  "simply asked the firmware team, what do you need from us? Have you ever asked "
                  "your next process that question?",
    },
    {
        "key": "p05", "num": 5, "title": "Leaders Make It Real",
        "points": [("Leaders back anyone who stops for quality", "Leaders must back"),
                   ("Respond quickly when called", "They must respond"),
                   ("Record defects to learn, never to blame", "And defects must be recorded")],
        "example": "An operator stopped Anita's line for a cracked lens — her manager thanked her in front of the team.",
        "example_cue": "When an operator stopped",
        "script": "Here's what makes or breaks Next Inspection. Your leaders. If people get "
                  "pushed to keep running despite a problem, the checks become box-ticking. "
                  "Leaders must back anyone who stops for quality. They must respond quickly when "
                  "called. And defects must be recorded to learn, never to blame. When an "
                  "operator stopped Anita's line for a cracked lens, her manager thanked her in "
                  "front of the team. What would happen on your line?",
    },
    {
        "key": "p06", "num": 6, "title": "Choosing What to Inspect",
        "points": [("Choose checks by risk", "So choose by risk"),
                   ("Customer CTQ: function, safety, fit", "Start with what your customer"),
                   ("FMEA and repeat escapes", "Then look at your FMEA"),
                   ("Where can a wrong part or label slip in?", "Ask where a wrong part")],
        "example": "Anita chose four: connector lock, firmware version, housing seal and label.",
        "example_cue": "Anita chose four",
        "script": "You can't check everything with the same care. So choose by risk. Start with "
                  "what your customer feels, like function, safety and fit. Those are your CTQ "
                  "points. Then look at your FMEA, and at the defects that keep escaping. Ask "
                  "where a wrong part, setting or label could slip in. Anita chose four: "
                  "connector lock, firmware version, housing seal and label. For high risks, "
                  "prefer prevention over a visual check. So how do you build a good gate?",
    },
    {
        "key": "p07", "num": 7, "title": "Designing an Inspection Gate",
        "points": [("Define good and bad, with samples", "First, define what good"),
                   ("Choose the method", "Then choose the method"),
                   ("Set how often you check", "Set how often you check"),
                   ("Decide the reaction in advance", "And decide the reaction")],
        "example": "Anita's seal gate: boundary samples on the bench and a red bin for rejects.",
        "example_cue": "Anita's seal gate",
        "script": "A good gate is fast, clear and hard to skip. First, define what good and bad "
                  "look like, with boundary samples where you can. Then choose the method, a "
                  "gauge, a sensor, a scan or a visual check. Set how often you check. And decide "
                  "the reaction before a defect ever appears. Anita's seal gate has samples on "
                  "the bench, and a red bin for rejects. So what happens when the gate finds "
                  "something?",
    },
    {
        "key": "p08", "num": 8, "title": "The Reaction Plan",
        "points": [("Stop or signal with Andon", "Stop or signal"),
                   ("Identify defect, model, serial", "Identify the defect"),
                   ("Contain back to the last good unit", "Contain every unit"),
                   ("Correct, verify, prevent", "Correct the process")],
        "example": "Wrong firmware at test: every unit since the last good check was held.",
        "example_cue": "When Anita's tester found",
        "script": "You react, fast and in order. Stop or signal with Andon. Identify the defect, "
                  "the model and the serial. Contain every unit back to the last known good one. "
                  "Correct the process, and verify the first good unit before you restart. Then "
                  "find the root cause, and prevent it coming back. When Anita's tester found "
                  "wrong firmware, every unit since the last good check was held. A vague plan "
                  "means delay and mixed stock.",
    },
    {
        "key": "p09", "num": 9, "title": "Lean Tools That Help",
        "points": [("Poka Yoke stops the wrong part or step", "Poka Yoke stops"),
                   ("Jidoka and Andon stop and call help", "Jidoka and Andon"),
                   ("Standard work makes good and bad obvious", "Standard work and visual"),
                   ("FMEA defines risks, audits check controls", "Your FMEA defines")],
        "example": "Anita swapped a visual label check for a scan match — now the wrong label can't print.",
        "example_cue": "Anita swapped a visual",
        "script": "Next Inspection works best with other Lean tools. Poka Yoke stops the wrong "
                  "part or step from happening at all. Jidoka and Andon stop the line and call "
                  "for help. Standard work and visual standards make good and bad obvious. Your "
                  "FMEA defines the risks, and audits check the controls are really used. Anita "
                  "swapped a visual label check for a scan match. Now the wrong label simply "
                  "can't print. Where else could that work?",
    },
    {
        "key": "p10", "num": 10, "title": "Electronics Examples",
        "points": [("SMT: optical inspection, verified feeders", "At SMT"),
                   ("Assembly: barcode for the PCB, screw counter", "At assembly"),
                   ("Firmware: version interlock", "At firmware"),
                   ("Packing: weight check and scans", "At packing")],
        "example": "Each check sits right after the step it protects. Final inspection is the last safety net.",
        "example_cue": "Each check sits right after",
        "script": "Let's walk the line. At SMT, automatic optical inspection checks the boards, "
                  "and feeders are verified. At assembly, a barcode confirms the right PCB, and a "
                  "counter confirms every screw. At firmware, an interlock checks the version "
                  "before release. At packing, a weight check and scans catch a missing "
                  "accessory. Notice the pattern. Each check sits right after the step it "
                  "protects. And final inspection? It's your last safety net, not your quality "
                  "system.",
    },
    {
        "key": "p11", "num": 11, "title": "Quality at the Source",
        "points": [("Upstream builds to standard", "Upstream builds to standard"),
                   ("Downstream accepts only good output", "Downstream accepts"),
                   ("Problems go back to the station that made them", "Any problem goes straight back"),
                   ("Beware the inspection trap", "beware the inspection trap")],
        "example": "Anita's line once had an inspector after every station. She moved three into prevention projects.",
        "example_cue": "Anita's line once worked",
        "script": "Next Inspection supports quality at the source. Upstream builds to standard. "
                  "Downstream accepts only good output. Any problem goes straight back to the "
                  "station that made it, and the cause gets fixed. Now, beware the inspection "
                  "trap. Adding an inspector after every station costs a lot, and hides weak "
                  "processes. Anita's line once worked that way. She moved three inspectors into "
                  "prevention projects instead. Can you trust the checks that remain?",
    },
    {
        "key": "p12", "num": 12, "title": "Can You Trust the Check?",
        "points": [("False accepts let defects escape", "A false accept"),
                   ("False rejects invite bypassing", "A false reject"),
                   ("Clear definitions, photos, boundary samples", "So define defects clearly"),
                   ("Train the checkers", "Train the people who check"),
                   ("Calibrate gauges, run MSA", "Calibrate gauges"),
                   ("Control lighting and viewing distance", "Control the lighting")],
        "example": "Anita's two inspectors disagreed on one seal in five. Better samples fixed it.",
        "example_cue": "Anita's two inspectors",
        "script": "A check is only useful if you can trust it. A false accept lets a defect "
                  "escape. A false reject creates needless rework, and people start bypassing "
                  "the check. So define defects clearly, with photos and boundary samples. Train "
                  "the people who check. Calibrate gauges, and run a measurement study, called "
                  "MSA. Control the lighting and viewing distance. Anita's two inspectors "
                  "disagreed on one seal in five. Better samples fixed it. So how do you measure "
                  "success?",
    },
    {
        "key": "p13", "num": 13, "title": "KPIs for Next Inspection",
        "points": [("First pass yield up", "First pass yield should rise"),
                   ("Escape rate down", "The escape rate should fall"),
                   ("Rework, repeat defects, response time", "Watch your rework rate"),
                   ("False calls tracked", "And track false calls")],
        "example": "Yield rising while inspection effort falls = you're winning.",
        "example_cue": "If yield rises",
        "script": "Track a balanced set of numbers. First pass yield should rise. The escape "
                  "rate should fall. That's defects found downstream that should have been "
                  "caught earlier. Watch your rework rate and repeat defects. Measure detection "
                  "response time, from the signal to containment. And track false calls, so you "
                  "know your checks are reliable. If yield rises while inspection effort falls, "
                  "you're winning. Ready to see Anita's results?",
    },
    {
        "key": "p14", "num": 14, "title": "Case Study: Camera Line",
        "points": [("Hand-off checks at 4 risk points", "She put hand-off checks"),
                   ("Reaction plan posted at each gate", "Each gate got"),
                   ("Seal and label checks became interlocks", "The seal and label checks"),
                   ("Weekly escape review with the source", "And every week")],
        "example": "After 8 weeks: escapes 18 → 3 a week, rework more than halved, first pass yield 98.5%.",
        "example_cue": "After eight weeks",
        "script": "Here's what Anita did. She put hand-off checks at four risk points. Each gate "
                  "got a posted reaction plan. The seal and label checks became interlocks. And "
                  "every week, she reviewed each escape with the station that made it. After "
                  "eight weeks, escapes fell from eighteen a week to three. Rework dropped by "
                  "more than half. First pass yield climbed to ninety-eight and a half percent. "
                  "How would you roll this out?",
    },
    {
        "key": "p15", "num": 15, "title": "Roadmap & Daily Checklist",
        "points": [("Select by risk and Pareto, map the flow", "Select one product"),
                   ("Design checks with reaction plans", "Design the source"),
                   ("Pilot one line, compare before / after", "Pilot on one line"),
                   ("Standardize SOP, FMEA, training", "Then standardize")],
        "example": "Daily questions: Are the criteria visible? Can your operators explain the reaction plan?",
        "example_cue": "Every day, ask simple questions",
        "script": "Roll it out step by step. Select one product using risk and Pareto. Map the "
                  "flow, and list the critical points. Design the source, self and next process "
                  "checks, with reaction plans. Pilot on one line, and compare before and after. "
                  "Then standardize the SOP, the FMEA and the training. Every day, ask simple "
                  "questions. Are the criteria visible? Can your operators explain the reaction "
                  "plan? Protect the next process, every time.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Don't make", "sub": "a defect", "icon": "wrench", "with": 2},
        {"label": "Don't pass", "sub": "a defect", "icon": "lock", "with": 3},
        {"label": "Don't accept", "sub": "a defect", "icon": "shield", "with": 4}]},
    "p02": {"type": "flow", "items": [
        {"label": "At assembly", "sub": "Seconds to fix", "icon": "wrench", "tone": "good", "with": "example"},
        {"label": "After test", "sub": "Open, repair, retest", "icon": "test", "with": "example"},
        {"label": "At the customer", "sub": "A return, and a hit to your name", "icon": "box", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "top": "STRONGEST: CLOSEST TO THE SOURCE", "bottom": "LAST LINE OF DEFENSE", "items": [
        {"label": "Source", "icon": "sensor"}, {"label": "Self", "icon": "hand"},
        {"label": "Next process", "icon": "search"}]},
    "p04": {"type": "flow", "items": [
        {"label": "Your station", "sub": "Follow the SOP", "icon": "wrench", "with": 0},
        {"label": "Check the critical points", "sub": "Product, quantity, label, timing", "icon": "check", "with": 1},
        {"label": "Next process", "sub": "Your customer", "icon": "person", "tone": "good", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Back the stop", "icon": "shield"}, {"label": "Respond fast", "icon": "clock"},
        {"label": "Learn, never blame", "icon": "person", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "Customer CTQ", "sub": "Function, safety, fit", "icon": "person", "with": 1},
        {"label": "FMEA + escapes", "sub": "What keeps getting out", "icon": "clipboard", "with": 2},
        {"label": "Slip-in points", "sub": "Wrong part, setting, label", "icon": "label", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Connector lock", "icon": "lock", "with": "example"},
            {"label": "Firmware version", "icon": "chip", "with": "example"},
            {"label": "Housing seal", "icon": "shield", "with": "example"},
            {"label": "Label", "icon": "label", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Good vs bad samples", "icon": "shape"}, {"label": "The method", "icon": "sensor"},
        {"label": "How often", "icon": "clock"}, {"label": "The reaction", "icon": "warning"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Stop: Andon", "icon": "warning", "tone": "bad"},
        {"label": "Identify", "sub": "Defect, model, serial", "icon": "search"},
        {"label": "Contain", "sub": "Back to the last good unit", "icon": "lock"},
        {"label": "Correct, verify, prevent", "icon": "check", "tone": "good"}]},
    "p09": {"type": "icons", "items": [
        {"label": "Poka Yoke", "icon": "key"}, {"label": "Jidoka + Andon", "icon": "warning"},
        {"label": "Standard work", "icon": "clipboard"}, {"label": "FMEA + audits", "icon": "shield"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Visual label check", "sub": "Easy to miss", "icon": "search"},
            {"label": "Scan match", "sub": "The wrong label can't print", "icon": "barcode"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "SMT", "sub": "Optical inspection, verified feeders", "icon": "chip"},
        {"label": "Assembly", "sub": "PCB barcode, screw counter", "icon": "barcode"},
        {"label": "Firmware", "sub": "Version interlock", "icon": "lock"},
        {"label": "Packing", "sub": "Weight check and scans", "icon": "scale"}]},
    "p11": {"type": "flow", "items": [
        {"label": "Upstream builds to standard", "icon": "wrench", "with": 0},
        {"label": "Downstream accepts only good", "icon": "check", "with": 1},
        {"label": "Problems go back to the source", "icon": "sequence", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "An inspector after every station", "sub": "Costly; hides weak processes", "icon": "person"},
            {"label": "3 moved to prevention", "sub": "Quality at the source", "icon": "shield"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "False accept", "icon": "cross", "tone": "bad"}, {"label": "False reject", "icon": "warning", "tone": "bad"},
        {"label": "Clear definitions", "icon": "clipboard"}, {"label": "Trained checkers", "icon": "person"},
        {"label": "Calibrate, MSA", "icon": "gear"}, {"label": "Lighting", "icon": "sensor"}],
        "then": {"type": "stat", "value": 5, "prefix": "1 in ", "icon": "search", "label": "seals the two inspectors disagreed on",
                 "unit": "Better boundary samples fixed it", "with": "example"}},
    "p13": {"type": "icons", "items": [
        {"label": "First pass yield", "sub": "Up", "icon": "chartUp", "tone": "good"},
        {"label": "Escape rate", "sub": "Down", "icon": "chartDown", "tone": "good"},
        {"label": "Rework, response time", "icon": "clock"},
        {"label": "False calls", "icon": "warning"}]},
    "p14": {"type": "flow", "items": [
        {"label": "Checks at 4 risk points", "icon": "search", "tone": "good"},
        {"label": "Reaction plan at each gate", "icon": "clipboard", "tone": "good"},
        {"label": "Seal + label interlocks", "icon": "lock", "tone": "good"},
        {"label": "Weekly escape review", "icon": "calendar", "tone": "good"}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 18}, "after": {"label": "After 8 weeks", "value": 3},
                 "unit": "escapes a week", "note": "First pass yield 98.5%", "with": "example"}},
    "p15": {"type": "steps", "items": [
        {"label": "Select by risk", "with": 0}, {"label": "Map the flow", "with": 0},
        {"label": "Design checks", "with": 1}, {"label": "Pilot one line", "with": 2},
        {"label": "Standardize", "with": 3}, {"label": "Ask daily", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A sensor stops the wrong connector orientation before the part is fitted. Which level of inspection is this?",
        "options": ["Source inspection", "Self inspection", "Next-process inspection"],
        "correct": 0,
        "explanation": "It checks the condition that would create the defect, before it happens. That is source inspection — the strongest level.",
        "q_script": "Quick check. A sensor stops the wrong connector orientation before the part "
                    "is even fitted. Which level of inspection is that? Take a few seconds.",
        "a_script": "It's source inspection. It checks the condition before the defect can "
                    "happen. That's the strongest level.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Test keeps finding the same loose connector from assembly, so a manager adds an inspector after assembly. What's the better move?",
        "options": ["Add a second inspector to be safe", "Keep the inspector and also fix the cause at assembly",
                    "Remove all checks to save cost", "Ask test to stop reporting it"],
        "correct": 1,
        "explanation": "An extra inspector can contain the risk for now, but a repeat defect means the process must be fixed at the source — then the temporary check can be removed.",
        "q_script": "One more, and this one's a scenario. Test keeps finding the same loose "
                    "connector from assembly. A manager adds an inspector after assembly. What's "
                    "the better move? Have a think.",
        "a_script": "Keep the check for now, but fix the cause at assembly. A repeat defect means "
                    "the process needs improving at the source. Then the extra check can go.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
