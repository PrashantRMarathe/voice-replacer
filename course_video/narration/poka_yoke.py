"""Poka Yoke (error proofing) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Divya,
a process engineer on a video-recorder (NVR) assembly line, replacing
reminders with designs that make the wrong action impossible.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/poka_yoke.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py poka_yoke  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "pk"
NAME = "poka_yoke"

LETTERS = ["NVR", "SMT", "MES", "SKU", "PLC", "FMEA", "SOP", "PPM", "FPY", "BOM"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return re.sub(r"\bShigeo\b", "Shee-gay-oh", text)


INTRO_SCRIPT = (
    "Eighteen video recorders shipped with a screw missing. The operator was skilled, and "
    "careful. She was simply human. Sound familiar? In this lesson, you'll learn Poka "
    "Yoke, or error proofing. You'll see how to design a process where the wrong action is "
    "impossible, or caught instantly. We'll follow Divya, a process engineer on an NVR "
    "assembly line, as she takes memory out of quality."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Errors are predictable, so design them out. Prefer "
    "prevention to detection, and detection to a warning. And challenge every device with "
    "bad samples, so you know it still works. Here's your action for this week. Find one "
    "check on your line that relies on memory, and sketch a Poka Yoke for it. Great work "
    "completing this lesson. Next, you'll learn Q-R-Q-C, quick response quality control."
)

# One story thread: Divya's NVR assembly line. Missing screws (18 per 10,000),
# reversed connectors, wrong firmware, wrong accessories at packing.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Poka Yoke Is",
        "points": [("Japanese for mistake-proofing", "Poka Yoke is Japanese"),
                   ("Don't rely on memory", "Don't rely on someone"),
                   ("Wrong action impossible, or seen instantly", "Design the process so")],
        "example": "Divya replaced a 'check orientation' sticker with a keyed connector. A sticker warns. A key prevents.",
        "example_cue": "Divya's line had a sticker",
        "script": "Here's the core idea. Poka Yoke is Japanese for mistake-proofing. Don't rely "
                  "on someone remembering to do the right thing. Design the process so the wrong "
                  "action can't happen, or shows up instantly. Divya's line had a sticker saying, "
                  "check the connector orientation. She replaced it with a keyed connector that "
                  "fits only one way. A sticker warns. A key prevents. So where did this idea "
                  "come from?",
    },
    {
        "key": "p02", "num": 2, "title": "Error vs Defect",
        "points": [("From the Toyota Production System", "Poka Yoke grew up"),
                   ("Error: the wrong action", "The error is the wrong action"),
                   ("Defect: the bad product that follows", "The defect is the bad product"),
                   ("Stop the error before it's a defect", "You stop the error")],
        "example": "End-of-line inspection finds problems after the labour and parts are spent.",
        "example_cue": "End-of-line inspection finds",
        "script": "Poka Yoke grew up in the Toyota Production System, through engineer Shigeo "
                  "Shingo. His key insight was simple. An error and a defect are different. The "
                  "error is the wrong action, like reversing a connector. The defect is the bad "
                  "product that follows. You stop the error before it becomes a defect. "
                  "End-of-line inspection finds problems after you've spent the labour and "
                  "parts. Why wait that long?",
    },
    {
        "key": "p03", "num": 3, "title": "The Control Hierarchy",
        "points": [("1 Eliminate: asymmetric locating pins", "Best, eliminate"),
                   ("2 Prevent: barcode interlock", "Next, prevent"),
                   ("3 Detect and stop: missing-screw sensor", "Then detect and stop"),
                   ("4 Warn: an alarm", "Weaker still"),
                   ("5 Inspect later — weakest", "Weakest, inspect later")],
        "example": "Choose controls by how reliably they stop errors — not by how easy they are to install.",
        "example_cue": "Choose controls by how reliably",
        "script": "Not all controls are equal. Here's the order of strength. Best, eliminate the "
                  "chance of error, with asymmetric locating pins. Next, prevent the wrong action, "
                  "like a barcode interlock. Then detect and stop, like a sensor that spots a "
                  "missing screw. Weaker still, a warning alarm. Weakest, inspect later. Choose "
                  "controls by how reliably they stop errors, not by how easy they are to "
                  "install. Which level are your checks today?",
    },
    {
        "key": "p04", "num": 4, "title": "Engineering Rules",
        "points": [("A positive pass signal, not 'no alarm'", "First, look for"),
                   ("Fail safe on power or sensor loss", "Second, the control must fail safe"),
                   ("Bypass: rare, logged, time-limited", "Third, make any bypass"),
                   ("Test it with wrong conditions", "Fourth, never claim")],
        "example": "Divya pulled the sensor cable during a trial. The fixture stayed locked.",
        "example_cue": "Divya pulled the sensor cable",
        "script": "Follow four engineering rules. First, look for a positive pass signal, not "
                  "just the absence of an alarm. Second, the control must fail safe. If power or "
                  "a sensor is lost, it stops. Third, make any bypass rare, logged and time "
                  "limited. Fourth, never claim it works until you've tested it with wrong "
                  "conditions. Divya pulled the sensor cable during a trial. The fixture stayed "
                  "locked. So what kinds of Poka Yoke exist?",
    },
    {
        "key": "p05", "num": 5, "title": "Three Methods",
        "points": [("Contact: shape, size, position", "The contact method"),
                   ("Fixed value: the right count", "The fixed value method"),
                   ("Motion step: the right sequence", "The motion step method")],
        "example": "Orientation problem → contact. Missing part → fixed value. Scan, program, test, label in order → motion step.",
        "example_cue": "Got an orientation problem",
        "script": "There are three classic methods. The contact method uses shape, size or "
                  "position to tell right from wrong. An asymmetric nest is one. The fixed value "
                  "method checks the count, like a counter that needs all six screws. The motion "
                  "step method checks the sequence. Scan, program, test, then label, in that "
                  "order. Each can prevent or detect. Got an orientation problem? Use contact. "
                  "A missing part? Use fixed value.",
    },
    {
        "key": "p06", "num": 6, "title": "Human Error Is Predictable",
        "points": [("Human errors are predictable", "Human errors are predictable"),
                   ("Skip, wrong part, reversed, out of order", "People skip steps"),
                   ("Ask what made it possible, not who", "So ask what made")],
        "example": "Wrong firmware → similar recipe names → model chosen by hand → MES scan not linked to the programmer.",
        "example_cue": "Divya traced wrong firmware",
        "script": "Human errors are predictable, so treat them as system risks. People skip "
                  "steps, pick the wrong part, reverse things, or do steps out of order. They "
                  "enter the wrong setting, or mix up labels. So ask what made the error "
                  "possible, not who made it. Divya traced wrong firmware to recipes with "
                  "similar names. The model was chosen by hand. The MES scan wasn't linked to "
                  "the programmer. Can you see the fix already?",
    },
    {
        "key": "p07", "num": 7, "title": "An 8-Step Design Method",
        "points": [("Define, observe, measure, find the cause", "Define the defect"),
                   ("Choose the simplest robust idea", "Choose the simplest"),
                   ("Prototype and challenge with bad parts", "Build a prototype"),
                   ("Update the SOP, train, monitor", "Then update the SOP")],
        "example": "Agree success before installing: wrong parts rejected, good parts pass, pace still holds.",
        "example_cue": "Before you install anything",
        "script": "Use a cross-functional team, and work in eight steps. Define the defect. "
                  "Observe the real operation, and find where the error happens. Measure the "
                  "baseline, and find the cause. Choose the simplest robust idea. Build a "
                  "prototype, and challenge it with good and bad parts. Then update the SOP, "
                  "train, and keep monitoring. Before you install anything, agree what success "
                  "looks like. Wrong parts rejected, good parts pass, and your pace still holds.",
    },
    {
        "key": "p08", "num": 8, "title": "Assembly Applications",
        "points": [("Torque signal linked to the work order", "She linked the screwdriver's"),
                   ("Fixture releases only when every screw is good", "The fixture only releases"),
                   ("Keyed connectors, gasket sensor", "She also added keyed")],
        "example": "Missing screws: 18 in 10,000 → 1 in 10,000, about 94% fewer.",
        "example_cue": "Missing screws fell",
        "script": "Now let's go to Divya's assembly line. Her missing screws were the big one. "
                  "She linked the screwdriver's torque signal to the work order. The fixture "
                  "only releases when every screw has a good result. A magnetic tray couldn't "
                  "prove that. Missing screws fell from eighteen in ten thousand to one. That's "
                  "about ninety-four percent fewer. She also added keyed connectors, and a "
                  "gasket sensor before closing. What about the boards inside?",
    },
    {
        "key": "p09", "num": 9, "title": "SMT and Test Applications",
        "points": [("Every feeder reel scanned against the BOM", "So scan every feeder"),
                   ("Program version checked before start", "Check the program version"),
                   ("Serial bound to model, firmware, pass record", "At test, bind each"),
                   ("Network drop must never 'pass'", "And make sure a network drop")],
        "example": "Divya's tester can't print a label without a pass record for that serial.",
        "example_cue": "Divya's tester can't print",
        "script": "On the board line, wrong settings can make thousands of defects fast. So scan "
                  "every feeder reel against the bill of materials. Check the program version "
                  "before the machine starts. At test, bind each serial number to its model, "
                  "firmware and pass record. Divya's tester can't print a label without that "
                  "record. And make sure a network drop can never create a false pass. Have you "
                  "tested yours that way?",
    },
    {
        "key": "p10", "num": 10, "title": "Packing and Dispatch",
        "points": [("Serial scan + carton label match", "So scan the serial"),
                   ("Accessories counted before closing", "count accessories"),
                   ("Weight checks have blind spots", "Weight checks help"),
                   ("Barcodes can be defeated", "a barcode isn't automatically")],
        "example": "A wrong adapter weighed the same as the right one — a shaped kit tray caught it.",
        "example_cue": "Divya found a wrong adapter",
        "script": "A perfect product can still become a complaint at packing. So scan the "
                  "serial, match the carton label, and count accessories before the box closes. "
                  "Weight checks help, but they have blind spots. Divya found a wrong adapter "
                  "that weighed the same as the right one. A shaped kit tray caught it instead. "
                  "And remember, a barcode isn't automatically error-proof. Duplicate labels and "
                  "manual overrides can defeat it. So should every fix be expensive?",
    },
    {
        "key": "p11", "num": 11, "title": "Low-Cost & Safe",
        "points": [("Simple: pins, guides, switches, trays", "Pins, guides, limit switches"),
                   ("Never create a pinch point", "A device must never"),
                   ("Quality sensors aren't safety systems", "an ordinary quality sensor"),
                   ("Plan cleaning and calibration", "Plan its cleaning")],
        "example": "Divya's best device cost ₹1,200: two pins that stop the rear panel going on upside down.",
        "example_cue": "Divya's best device cost",
        "script": "Not at all. Many of the best Poka Yokes are simple. Pins, guides, limit "
                  "switches, count trays and go, no-go gauges. Divya's best device cost twelve "
                  "hundred rupees. Two pins that stop the rear panel going on upside down. But "
                  "keep safety first. A device must never create a pinch point. And an ordinary "
                  "quality sensor is not a safety system. Plan its cleaning and calibration too. "
                  "So how do you make it stick?",
    },
    {
        "key": "p12", "num": 12, "title": "FMEA, Control Plan & Audits",
        "points": [("FMEA: link to the failure mode", "In the FMEA"),
                   ("Control plan: method and reaction", "In the control plan"),
                   ("Standard work: pass signal, who resets", "In standard work"),
                   ("Audit with a known bad sample", "Feed it a known bad sample")],
        "example": "Divya feeds every device a known bad sample, every shift.",
        "example_cue": "Divya does that every shift",
        "script": "Build every device into your quality system. In the FMEA, link it to the "
                  "failure mode it controls. In the control plan, write the method and the "
                  "reaction. In standard work, show what a pass looks like, and who can reset "
                  "the device. Then audit it. Don't just check the device exists. Feed it a known "
                  "bad sample, and confirm it rejects it. Divya does that every shift. How do "
                  "you measure the benefit?",
    },
    {
        "key": "p13", "num": 13, "title": "KPIs & Savings",
        "points": [("Defect PPM and escapes down", "Defect P-P-M"),
                   ("First pass yield up", "First pass yield should rise"),
                   ("Watch false rejects", "And watch false rejects")],
        "example": "60,000 units/month, defects cut from 0.8% to 0.2% ≈ ₹65,000 saved a month, minus running cost.",
        "example_cue": "Divya's line makes",
        "script": "Measure the result, and the health of your device. Defect P-P-M and customer "
                  "escapes should fall. First pass yield should rise. And watch false rejects. A "
                  "sensor that keeps rejecting good units invites people to bypass it. Divya's "
                  "line makes sixty thousand units a month. Cutting defects from almost one "
                  "percent to a quarter of that saves about sixty-five thousand rupees a month. "
                  "Then subtract your running cost.",
    },
    {
        "key": "p14", "num": 14, "title": "90-Day Roadmap",
        "points": [("Weeks 1–2: top failure modes + baseline", "In the first two weeks"),
                   ("Weeks 3–4: design options, agree logic", "Over the next two weeks"),
                   ("Month 2: pilot one station", "In the second month"),
                   ("Month 3: document, train, copy", "In the last month")],
        "example": "Test every wrong condition you know during the pilot.",
        "example_cue": "test every wrong condition",
        "script": "Here's a simple ninety-day plan. In the first two weeks, pick your top "
                  "failure modes from Pareto and the FMEA, and set a baseline. Over the next "
                  "two weeks, design options and agree the logic. In the second month, pilot on "
                  "one station, and test every wrong condition you know. In the last month, "
                  "update the documents, train people, and then copy it to other lines. Who "
                  "owns each part of that?",
    },
    {
        "key": "p15", "num": 15, "title": "Release Checklist",
        "points": [("Failure mode clear, with a baseline", "Is the failure mode clear"),
                   ("Safety and ergonomics reviewed", "Were safety and ergonomics"),
                   ("Bad samples tested on every model", "Was it tested"),
                   ("Power loss, offline, bypass handled", "Does it handle power loss")],
        "example": "Production owns the station. Engineering designs it. Quality challenge-tests it.",
        "example_cue": "Production owns the station",
        "script": "Production owns the station. Engineering designs it, and Quality challenge "
                  "tests it. Before you release any device, run a final checklist. Is the "
                  "failure mode clear, with a baseline? Were safety and ergonomics reviewed? Was "
                  "it tested with bad samples on every model? Does it handle power loss, offline "
                  "mode and bypass? The best Poka Yoke makes the right action natural, and the "
                  "wrong one impossible.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "A sticker warns", "sub": "'Check orientation'", "icon": "sticker", "with": "example"},
        {"label": "A key prevents", "sub": "Fits only one way", "icon": "key", "with": "example"}]},
    "p02": {"type": "flow", "stop": {"after": 0, "label": "STOP HERE", "with": 3}, "items": [
        {"label": "Error", "sub": "The wrong action", "icon": "hand", "tone": "bad", "with": 1},
        {"label": "Defect", "sub": "The bad product", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Found at end of line", "sub": "Labour and parts already spent", "icon": "search", "tone": "bad", "with": "example"}]},
    "p03": {"type": "ladder", "items": [
        {"label": "Eliminate", "icon": "pin"}, {"label": "Prevent", "icon": "barcode"},
        {"label": "Detect and stop", "icon": "sensor"}, {"label": "Warn", "icon": "warning"},
        {"label": "Inspect later", "icon": "search"}]},
    "p04": {"type": "icons", "items": [
        {"label": "Positive pass", "icon": "check"}, {"label": "Fail safe", "icon": "power"},
        {"label": "Bypass logged", "icon": "lock"}, {"label": "Test wrong cases", "icon": "test"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Contact", "sub": "Shape, size, position", "icon": "shape"},
        {"label": "Fixed value", "sub": "The right count", "icon": "count"},
        {"label": "Motion step", "sub": "The right order", "icon": "sequence"}]},
    "p06": {"type": "flow", "items": [
        {"label": "Similar recipe names", "icon": "sticker", "tone": "bad", "with": 2},
        {"label": "Model chosen by hand", "icon": "hand", "tone": "bad", "with": 2},
        {"label": "Wrong firmware", "icon": "chip", "tone": "bad", "with": 2},
        {"label": "Fix: link the MES scan", "sub": "to the programmer", "icon": "barcode", "tone": "good", "with": "example"}]},
    "p07": {"type": "steps", "items": [
        {"label": "Define", "with": 0}, {"label": "Observe", "with": 0},
        {"label": "Measure", "with": 0}, {"label": "Find the cause", "with": 0},
        {"label": "Choose an idea", "with": 1}, {"label": "Prototype", "with": 2},
        {"label": "Challenge it", "with": 2}, {"label": "Standardise", "with": 3}]},
    "p08": {"type": "assembly", "label": "Divya's NVR line: the fixture counts every screw",
            "then": {"type": "compare", "before": {"label": "Before", "value": 18}, "after": {"label": "After", "value": 1},
                     "unit": "missing screws per 10,000 units", "note": "about 94% fewer"}},
    "p09": {"type": "flow", "stop": {"after": 2, "label": "NO PASS, NO LABEL", "with": "example"}, "items": [
        {"label": "Reel scanned vs BOM", "icon": "barcode", "with": 0},
        {"label": "Program version checked", "icon": "chip", "with": 1},
        {"label": "Pass record per serial", "icon": "test", "with": 2},
        {"label": "Label prints", "icon": "label", "tone": "good", "with": "example"}]},
    "p10": {"type": "versus", "items": [
        {"label": "Weight check", "sub": "Wrong adapter, same weight", "icon": "scale", "with": "example"},
        {"label": "Shaped kit tray", "sub": "Wrong adapter can't fit", "icon": "tray", "with": "example"}]},
    "p11": {"type": "stat", "value": 1200, "prefix": "₹", "icon": "pin", "label": "Two locating pins",
            "unit": "No more rear panels fitted upside down"},
    "p12": {"type": "flow", "items": [
        {"label": "FMEA", "sub": "The failure mode", "icon": "clipboard"},
        {"label": "Control plan", "sub": "Method and reaction", "icon": "shield"},
        {"label": "Standard work", "sub": "Pass signal, who resets", "icon": "person"},
        {"label": "Audit", "sub": "A known bad sample", "icon": "test", "tone": "good"}]},
    "p13": {"type": "compare", "before": {"label": "Before", "value": 0.8}, "after": {"label": "After", "value": 0.2},
            "suffix": "%", "decimals": 1, "unit": "defect rate, 60,000 units a month", "note": "≈ ₹65,000 saved a month"},
    "p14": {"type": "timeline", "items": [
        {"label": "Failure modes + baseline", "sub": "W1–2", "span": 2, "icon": "search"},
        {"label": "Design options, agree logic", "sub": "W3–4", "span": 2, "icon": "gear"},
        {"label": "Pilot one station", "sub": "Month 2", "span": 4, "icon": "test"},
        {"label": "Document, train, copy", "sub": "Month 3", "span": 4, "icon": "clipboard"}]},
    "p15": {"type": "icons", "items": [
        {"label": "Production", "sub": "Owns the station", "icon": "person", "with": "example"},
        {"label": "Engineering", "sub": "Designs it", "icon": "gear", "with": "example"},
        {"label": "Quality", "sub": "Challenge-tests it", "icon": "shield", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A fixture won't release until it counts all six screws. Which Poka Yoke method is this?",
        "options": ["Contact method", "Fixed-value method", "Motion-step method"],
        "correct": 1,
        "explanation": "It confirms the correct count, so it's the fixed-value method. Contact checks shape or position; motion-step checks sequence.",
        "q_script": "Quick check. A fixture won't release until it counts all six screws. Which "
                    "Poka Yoke method is that? Take a few seconds.",
        "a_script": "It's the fixed value method. It confirms the correct count. Contact checks "
                    "shape, and motion step checks the sequence.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A new gasket sensor rejects so many good units that operators start bypassing it. What should the team do FIRST?",
        "options": ["Remove the sensor", "Discipline the operators",
                    "Control the bypass and fix the false rejects with verified samples",
                    "Add a reminder sign"],
        "correct": 2,
        "explanation": "False rejects invite bypass. Lock down the bypass, then improve positioning, lighting or thresholds using known good and bad samples, and track the false-reject rate.",
        "q_script": "One more, and this one's a scenario. A new gasket sensor rejects so many good "
                    "units that operators start bypassing it. What should the team do first? Have a think.",
        "a_script": "Control the bypass, then fix the false rejects. Improve the sensor setup, "
                    "using known good and bad samples. False rejects invite people to bypass a device.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
