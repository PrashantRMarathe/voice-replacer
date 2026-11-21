"""Zero Defects lesson DATA: 15 pages + 2 quizzes + intro/outro.

Reference lesson for the script style guide (docs/PLAYBOOK.md §4b): hook
intro, one story thread (Priya's phone-assembly line), short spoken sentences,
talks to the learner, pages linked by a bridge line, 3-takeaway outro.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/zero_defects.py                 voice MISSING clips (bootstrap)
  python narration/import_clones.py zero_defects   import the cloned voice
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "zd"
NAME = "zero_defects"

INTRO_SCRIPT = (
    "One connector, seated badly. It passed every visual check. Then four hundred "
    "phones came back for rework. Sound familiar? In this lesson, you'll learn Zero "
    "Defects. You'll see how to measure quality honestly, and how to make mistakes "
    "like that impossible. We'll follow Priya, a line engineer on a mobile phone "
    "assembly line, as she does exactly that."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Prevent defects, don't just inspect for them. "
    "Measure honestly, with clear definitions. And when something fails, fix the "
    "system, not the person. Here's your action for this week. Pick one defect that "
    "keeps coming back on your line, and ask how to make it impossible. Great work "
    "completing this lesson, and the whole course, from A to Z. Now go and make one "
    "improvement on your line."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Meaning & Philosophy",
        "points": [("Every defect is preventable", "treats every defect as preventable"),
                   ("Right the first time", "You aim to get"),
                   ("Design and control the process", "By designing and controlling"),
                   ("A discipline, not a promise", "It's a discipline")],
        "example": "Priya's line: a station now confirms the connector is seated before electrical test.",
        "example_cue": "On Priya's line",
        "script": "Here's the core idea. Zero Defects treats every defect as preventable, not as "
                  "a normal cost of doing business. You aim to get each unit right the first time. "
                  "How? By designing and controlling the process well. It's a discipline, not a "
                  "promise that nothing ever goes wrong. On Priya's line, a station now confirms "
                  "the connector is seated before electrical test. So where did this idea come from?",
    },
    {
        "key": "p02", "num": 2, "title": "History & Business Value",
        "points": [("Crosby, 1960s: quality = meeting requirements", "Philip Crosby made"),
                   ("Lean adds built-in quality & mistake-proofing", "Modern Lean adds"),
                   ("Fix the system, not the person", "you fix the system"),
                   ("Leaders remove barriers; operators stop & react", "Leaders remove the barriers")],
        "example": "To win leaders' support, you need to show the money.",
        "example_cue": "But to win that support",
        "script": "Philip Crosby made Zero Defects famous in the nineteen sixties. His definition "
                  "is simple. Quality means meeting clearly defined requirements. Modern Lean adds "
                  "built-in quality, standard work and mistake-proofing. Here's the key shift. When "
                  "a defect happens, you fix the system, not blame the person. Leaders remove the "
                  "barriers, and operators are trusted to stop and react. But to win that support, "
                  "you need to show the money.",
    },
    {
        "key": "p03", "num": 3, "title": "Cost of Poor Quality",
        "points": [("Internal failure: scrap, rework, retest", "Internal failures include"),
                   ("External failure: warranty, returns", "External failures include"),
                   ("Hidden: delays, handling, lost capacity", "Then come the hidden costs"),
                   ("Prevention costs far less", "Prevention costs far less")],
        "example": "Priya's line: 400 reworked phones = ₹32,000 of direct rework — before a single late shipment.",
        "example_cue": "Last month, Priya's line",
        "script": "Poor quality costs more than you think. Internal failures include scrap, rework "
                  "and retest. External failures include warranty claims and returns. Then come the "
                  "hidden costs, like delays, extra handling and lost capacity. Last month, Priya's "
                  "line reworked four hundred phones. That's thirty-two thousand rupees of direct "
                  "rework, before a single late shipment. Prevention costs far less. So how do you "
                  "measure where quality is lost?",
    },
    {
        "key": "p04", "num": 4, "title": "FTR, FPY & RTY",
        "points": [("First Time Right: no correction at all", "First Time Right means"),
                   ("First Pass Yield: pass a step first time", "First Pass Yield is"),
                   ("Rolled Throughput Yield: multiply every step", "Rolled Throughput Yield multiplies")],
        "example": "Three stages at 98% each give only about 94% together.",
        "example_cue": "Three stages at ninety-eight",
        "script": "Start with three yield measures. First Time Right means meeting requirements "
                  "with no correction at all. First Pass Yield is the share of units that pass a "
                  "step the first time. Rolled Throughput Yield multiplies the yields of every step. "
                  "Here's the trap. Three stages at ninety-eight percent each sounds great. "
                  "Together, they give only about ninety-four percent. Which step on your line "
                  "quietly drags the total down?",
    },
    {
        "key": "p05", "num": 5, "title": "PPM, DPMO & Targets",
        "points": [("PPM: defective units per million", "P-P-M counts"),
                   ("DPMO: defects per million opportunities", "D-P-M-O counts"),
                   ("Report sample size and scope", "Always report your sample"),
                   ("Never compare PPM with DPMO", "And never compare")],
        "example": "Priya found 25 bad phones in 50,000 = 500 PPM.",
        "example_cue": "Priya found twenty-five",
        "script": "Defect rates need a precise denominator. P-P-M counts defective units per "
                  "million. D-P-M-O counts defects per million opportunities. So you must define "
                  "the opportunities on each unit first. Priya found twenty-five bad phones in "
                  "fifty thousand. That's five hundred P-P-M. Always report your sample size and "
                  "scope. And never compare a P-P-M with a D-P-M-O. Now, how do you stop defects "
                  "being made at all?",
    },
    {
        "key": "p06", "num": 6, "title": "Quality at Source",
        "points": [("Every operation owns its output", "every operation owns"),
                   ("Next station = your customer", "Treat the next station"),
                   ("Check inputs and setup, follow the SOP", "Check your inputs"),
                   ("Wrong? Stop, segregate, escalate", "If something looks wrong")],
        "example": "Set-top box line: operators check the thermal pad and screw torque before a unit moves on.",
        "example_cue": "On the set-top box line",
        "script": "Quality at source means every operation owns its own output. Treat the next "
                  "station as your customer. Check your inputs and setup first, then follow the "
                  "current S-O-P. If something looks wrong, stop, segregate and escalate. Don't "
                  "pass it on. On the set-top box line next door, operators check the thermal pad "
                  "and screw torque before a unit moves on. Inspection later can't rescue an "
                  "unstable process. But what if people still slip?",
    },
    {
        "key": "p07", "num": 7, "title": "Poka Yoke",
        "points": [("Poka Yoke = mistake-proofing", "It means mistake-proofing"),
                   ("Make errors impossible, or catch them", "Shapes, interlocks and sensors"),
                   ("Prevention beats a warning label", "Prevention beats a warning"),
                   ("Challenge with good & bad samples", "Challenge each device")],
        "example": "Priya's battery-connector fixture only fits one way; the phone can't move on until the check is recorded.",
        "example_cue": "Priya added a battery",
        "script": "That's where Poka Yoke comes in. It means mistake-proofing. Shapes, interlocks "
                  "and sensors either make an error impossible, or catch it instantly. Prevention "
                  "beats a warning label, because warnings rely on memory. Priya added a battery "
                  "connector fixture that only fits one way. The phone can't move on until the "
                  "check is recorded. Challenge each device with good and bad samples, every shift. "
                  "So what happens when something still goes wrong?",
    },
    {
        "key": "p08", "num": 8, "title": "Jidoka, Andon & Response",
        "points": [("Jidoka: the process stops itself", "Jidoka means"),
                   ("Andon makes the problem visible", "An Andon signal"),
                   ("Clear stop criteria, a named owner", "You need clear stop criteria"),
                   ("Restart only when the cause is controlled", "you restart only when")],
        "example": "An audio tester flags repeated channel imbalance: the line stops and suspect units are held.",
        "example_cue": "Picture an audio tester",
        "script": "Jidoka means the process detects an abnormality and stops itself. An Andon "
                  "signal makes the problem visible, so the right people respond fast. You need "
                  "clear stop criteria, and a named owner for every Andon call. Picture an audio "
                  "tester flagging repeated channel imbalance. The line stops, and suspect units "
                  "are held. The fixture is checked, and you restart only when the cause is "
                  "controlled. Stopping isn't failure. Hiding the problem is.",
    },
    {
        "key": "p09", "num": 9, "title": "Standard Work & Audits",
        "points": [("Standard work: best, safest method", "With standard work"),
                   ("Verify the first unit after changeover", "verify the first unit"),
                   ("Layered audits confirm controls", "Then layered process audits"),
                   ("Audit controls, not paperwork", "Audit the controls")],
        "example": "Firmware release needs the approved image, a recipe match and a checksum.",
        "example_cue": "At a firmware station",
        "script": "Now, how do you keep good results stable? With standard work. That's the current "
                  "best and safest method, including checks, settings and traceability. Keep it "
                  "visible, and verify the first unit after every changeover. Then layered process "
                  "audits confirm your critical controls still work. Audit the controls, not the "
                  "paperwork. At a firmware station, release needs the approved image, a recipe "
                  "match and a checksum. But how stable is the process itself?",
    },
    {
        "key": "p10", "num": 10, "title": "SPC & Process Capability",
        "points": [("SPC: normal variation vs real signals", "It separates normal variation"),
                   ("Cp: spread vs specification", "C-p compares"),
                   ("Cpk: also checks centering", "C-p-k also checks"),
                   ("Only with a stable process & calibrated gauge", "Both only mean something")],
        "example": "Screw torque on Priya's line: tight, centered variation gives Cpk ≈ 1.33. That's capable.",
        "example_cue": "Take screw torque",
        "script": "Statistical Process Control answers that. It separates normal variation from "
                  "real signals that need action. C-p compares your process spread to the "
                  "specification. C-p-k also checks whether the process is centered. Both only "
                  "mean something when the process is stable and the gauge is calibrated. Take "
                  "screw torque on Priya's line. With tight, centered variation, C-p-k comes out "
                  "around one point three three. That's capable. But how do you see risks coming?",
    },
    {
        "key": "p11", "num": 11, "title": "PFMEA & Control Plans",
        "points": [("PFMEA: how each step can fail, and why", "It asks how each step"),
                   ("Control Plan turns it into real checks", "Then the Control Plan"),
                   ("Method · frequency · owner · reaction", "Each check has a method"),
                   ("Update both after real failures", "Update both whenever")],
        "example": "Missing insulation pad can cause a short → presence interlock + stop-and-hold rule.",
        "example_cue": "On an audio device",
        "script": "You use a Process F-M-E-A. It asks how each step can fail, why, and what "
                  "prevents or detects it. Then the Control Plan turns that into real checks. Each "
                  "check has a method, a frequency, an owner and a reaction. On an audio device, a "
                  "missing insulation pad can cause a short. So the F-M-E-A leads to a presence "
                  "interlock and a clear stop-and-hold rule. Update both whenever a real failure "
                  "teaches you something.",
    },
    {
        "key": "p12", "num": 12, "title": "Root Cause Analysis",
        "points": [("Define the problem precisely", "starts by defining"),
                   ("Contain suspect stock first", "Contain suspect stock"),
                   ("Facts, five whys, controlled tests", "Then use facts"),
                   ("Why did it happen? Why wasn't it stopped?", "Your fix must answer")],
        "example": "Priya's team traced their charging failures to loose connector seating.",
        "example_cue": "Priya's team traced",
        "script": "And failures will teach you, if you dig properly. Root Cause Analysis starts by "
                  "defining the problem precisely. Contain suspect stock first. Then use facts, "
                  "five whys and controlled tests, never assumptions. Your fix must answer two "
                  "questions. Why did the defect happen? And why didn't our controls stop it? "
                  "Priya's team traced their charging failures to loose connector seating. Let's "
                  "see what they did next.",
    },
    {
        "key": "p13", "num": 13, "title": "Case Study: Mobile Phone",
        "points": [("1,200 of 40,000 failed: 3%", "Twelve hundred of forty"),
                   ("Data split by lot, fixture, station, shift", "The team split the data"),
                   ("Keyed fixture + automatic seating check", "So they trialed"),
                   ("FMEA and SOP updated", "They updated the F-M-E-A")],
        "example": "Failures fell to 0.5% — an 83% reduction.",
        "example_cue": "Failures fell to half",
        "script": "Here's Priya's case. Twelve hundred of forty thousand phones failed the first "
                  "charging test. That's a three percent failure rate. The team split the data by "
                  "connector lot, fixture, station and shift. The pattern pointed to the fixture. "
                  "So they trialed a keyed fixture with an automatic seating check. Failures fell "
                  "to half a percent. That's an eighty-three percent reduction. And what made it "
                  "stick? They updated the F-M-E-A and the S-O-P.",
    },
    {
        "key": "p14", "num": 14, "title": "Set-Top Box & Audio",
        "points": [("Same thinking, tailored controls", "You just tailor the controls"),
                   ("Set-top box: firmware matched to SKU", "So match the firmware"),
                   ("Audio: keyed connectors, golden units", "Keyed connectors and golden-unit"),
                   ("Packing: serial matched to carton", "At packing")],
        "example": "Set-top box: firmware, power, labels. Audio: polarity, sealing, channel balance.",
        "example_cue": "Set-top box defects often",
        "script": "The same thinking works on every product family. You just tailor the controls. "
                  "Set-top box defects often involve firmware, power and labels. So match the "
                  "firmware to the S-K-U, and block wrong flashing. Audio devices fail on speaker "
                  "polarity, sealing and channel balance. Keyed connectors and golden-unit checks "
                  "handle those. At packing, the system matches each serial to its carton. What "
                  "would you protect first on your line?",
    },
    {
        "key": "p15", "num": 15, "title": "KPIs & 90-Day Roadmap",
        "points": [("Lagging: FPY, PPM, cost of poor quality", "Watch your lagging results"),
                   ("Leading: challenge tests, audit scores", "Also watch leading controls"),
                   ("Days 1–30: baseline and contain", "In the first thirty days"),
                   ("Days 31–60: root causes, pilot Poka Yoke", "In the next thirty"),
                   ("Days 61–90: verify gains, deploy everywhere", "In the last thirty")],
        "example": "Last 30 days: verify the gains and deploy them on every line.",
        "example_cue": "In the last thirty",
        "script": "Finally, make it part of daily management. Watch your lagging results, like "
                  "F-P-Y, P-P-M and the cost of poor quality. Also watch leading controls, like "
                  "interlock challenge tests and audit scores. Here's a simple ninety-day plan. In "
                  "the first thirty days, baseline and contain. In the next thirty, find root "
                  "causes and pilot Poka Yoke. In the last thirty, verify the gains and deploy "
                  "them on every line.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Every defect preventable", "icon": "shield", "with": 0},
        {"label": "Right the first time", "icon": "check", "tone": "good", "with": 1},
        {"label": "Design the process", "icon": "gear", "with": 2},
        {"label": "A discipline", "icon": "clipboard", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Connector seated?", "icon": "sensor", "with": "example"},
            {"label": "Then electrical test", "icon": "test", "tone": "good", "with": "example"}]}},
    "p02": {"type": "timeline", "items": [
        {"label": "Quality = meeting requirements", "sub": "Crosby, 1960s", "icon": "clipboard", "with": 0},
        {"label": "Built-in quality, mistake-proofing", "sub": "Modern Lean", "icon": "key", "with": 1},
        {"label": "Fix the system, not the person", "sub": "Today", "icon": "gear", "with": 2}]},
    "p03": {"type": "icons", "items": [
        {"label": "Internal", "sub": "Scrap, rework, retest", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "External", "sub": "Warranty, returns", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Hidden", "sub": "Delays, handling, capacity", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 32000, "prefix": "₹", "icon": "wrench", "label": "of direct rework",
                 "unit": "400 phones reworked in one month", "with": "example"}},
    "p04": {"type": "icons", "items": [
        {"label": "First Time Right", "sub": "No correction at all", "icon": "check", "with": 0},
        {"label": "First Pass Yield", "sub": "Pass a step first time", "icon": "test", "with": 1},
        {"label": "Rolled Throughput Yield", "sub": "Multiply every step", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "98% × 98% × 98% ≈ 94%", "suffix": "%", "with": "example", "items": [
            {"label": "Stage 1", "value": 98, "with": "example"},
            {"label": "Stage 2", "value": 98, "with": "example"},
            {"label": "Stage 3", "value": 98, "with": "example"},
            {"label": "Together", "value": 94, "tone": "bad", "with": "example"}]}},
    "p05": {"type": "versus", "items": [
        {"label": "PPM", "sub": "Defective units per million", "icon": "count", "with": 0},
        {"label": "DPMO", "sub": "Defects per million opportunities", "icon": "search", "with": 1}],
        "then": {"type": "stat", "value": 500, "suffix": " PPM", "icon": "count", "label": "25 bad phones in 50,000",
                 "unit": "Always report sample size and scope", "with": "example"}},
    "p06": {"type": "flow", "items": [
        {"label": "Own your output", "icon": "hand", "with": 0},
        {"label": "Next station = customer", "icon": "person", "with": 1},
        {"label": "Inputs, setup, SOP", "icon": "clipboard", "with": 2},
        {"label": "Stop, segregate, escalate", "icon": "warning", "tone": "bad", "with": 3}]},
    "p07": {"type": "ladder", "top": "STRONGEST", "bottom": "WEAKEST", "items": [
        {"label": "Make it impossible", "icon": "key", "with": 1},
        {"label": "Catch it instantly", "icon": "sensor", "with": 1},
        {"label": "Warning label", "icon": "warning", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Fixture fits one way", "icon": "shape", "with": "example"},
            {"label": "Check recorded", "icon": "clipboard", "with": "example"},
            {"label": "Only then the phone moves on", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Abnormality detected", "sub": "Jidoka", "icon": "sensor", "with": 0},
        {"label": "Andon: make it visible", "icon": "warning", "with": 1},
        {"label": "Stop, hold suspects", "icon": "lock", "tone": "bad", "with": "example"},
        {"label": "Restart when controlled", "icon": "check", "tone": "good", "with": 3}]},
    "p09": {"type": "doc", "items": [
        {"label": "Standard work · Firmware station", "icon": "label", "with": 0},
        {"label": "First unit verified after changeover", "icon": "check", "with": 1},
        {"label": "Approved image + recipe match", "icon": "chip", "with": "example"},
        {"label": "Checksum before release", "icon": "lock", "with": "example"},
        {"label": "Layered audit: controls, not paperwork", "icon": "search", "with": 3}]},
    "p10": {"type": "icons", "items": [
        {"label": "Noise vs real signal", "icon": "wave", "with": 0},
        {"label": "Cp: spread vs spec", "icon": "scale", "with": 1},
        {"label": "Cpk: centered too", "icon": "pin", "with": 2},
        {"label": "Stable process, calibrated gauge", "icon": "gear", "with": 3}],
        "then": {"type": "stat", "value": 1.33, "decimals": 2, "icon": "screw", "label": "Cpk on screw torque",
                 "unit": "Tight, centered variation: capable", "with": "example"}},
    "p11": {"type": "flow", "items": [
        {"label": "PFMEA: how it can fail", "icon": "search", "with": 0},
        {"label": "Control Plan: real checks", "icon": "clipboard", "with": 1},
        {"label": "Method · frequency · owner · reaction", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Missing insulation pad", "sub": "Can cause a short", "icon": "warning", "tone": "bad", "with": "example"},
            {"label": "Presence interlock", "icon": "sensor", "with": "example"},
            {"label": "Stop-and-hold rule", "icon": "lock", "tone": "good", "with": "example"}]}},
    "p12": {"type": "flow", "items": [
        {"label": "Define precisely", "icon": "clipboard", "with": 0},
        {"label": "Contain suspect stock", "icon": "lock", "with": 1},
        {"label": "Facts, five whys, tests", "icon": "test", "with": 2},
        {"label": "Why made? Why not stopped?", "icon": "search", "tone": "good", "with": 3}]},
    "p13": {"type": "stat", "value": 3, "suffix": "%", "icon": "power", "label": "failed the first charging test",
            "unit": "1,200 of 40,000 phones", "with": 0,
            "then": {"type": "compare", "before": {"label": "Before", "value": 3}, "after": {"label": "After", "value": 0.5},
                     "decimals": 1, "suffix": "%", "unit": "phones failing the first charging test",
                     "note": "An 83% reduction", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Set-top box", "sub": "Firmware matched to SKU", "icon": "chip", "with": 1},
        {"label": "Audio", "sub": "Keyed connectors, golden units", "icon": "wave", "with": 2},
        {"label": "Packing", "sub": "Serial matched to carton", "icon": "barcode", "with": 3}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Baseline and contain", "sub": "Days 1–30", "icon": "lock", "with": 2},
        {"label": "Root causes, pilot Poka Yoke", "sub": "31–60", "icon": "search", "with": 3},
        {"label": "Verify gains, deploy everywhere", "sub": "61–90", "icon": "chartUp", "with": 4}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "970 of 1,000 units pass the first test with no rework. What is the First Pass Yield?",
        "options": ["3%", "97%", "9.7 per unit"],
        "correct": 1,
        "explanation": "FPY = first-pass accepted ÷ total = 970 ÷ 1,000 = 97%. It counts only the units that passed the first time, with no rework.",
        "q_script": "Quick check. Nine hundred and seventy of a thousand units pass the first test, "
                    "with no rework. What's the First Pass Yield? Take a few seconds.",
        "a_script": "It's ninety-seven percent. First Pass Yield counts only the units that passed "
                    "the first time, divided by the total.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "An audio line finds reversed speaker polarity on 30 units this shift. What should the team do FIRST?",
        "options": ["Retrain the operator and carry on", "Stop, contain suspect units, then find the root cause",
                    "Add a warning label to the speaker", "Increase final inspection"],
        "correct": 1,
        "explanation": "Contain first: stop and hold suspect units back to the last good point. Then find the root cause and prevent it, e.g. with a keyed polarity connector. Blame, labels and extra inspection don't stop it recurring.",
        "q_script": "One more, and this one's a scenario. An audio line finds reversed speaker "
                    "polarity on thirty units this shift. What should the team do first? Have a think.",
        "a_script": "Stop and contain the suspect units first. Then find the root cause, and prevent "
                    "it, for example with a keyed polarity connector. Blame, labels and extra "
                    "inspection won't stop it coming back.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
