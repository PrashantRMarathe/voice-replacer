"""QRQC (Quick Response Quality Control) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Farhan,
quality lead at a network-camera plant, when focus failures jump after a
lens fixture changeover on Line 4.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/qrqc.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py qrqc  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "qr"
NAME = "qrqc"

# QRQC has no vowels, so it can only be said letter by letter ("Q-R-Q-C").
LETTERS = ["QRQC", "WIP", "FPY", "MES", "SKU", "NVR", "FMEA", "SOP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return text.replace("5W2H", "five W two H")


INTRO_SCRIPT = (
    "Ten o'clock. Cameras start failing focus test. Someone resets the tester, and the "
    "line runs on. By noon, a full shift of suspect cameras is heading for the warehouse. "
    "Sound familiar? In this lesson, you'll learn QRQC, quick response quality control. "
    "You'll see how to react in minutes, protect your customer, and still find the real "
    "cause. We'll follow Farhan, a quality lead at a camera plant."
)
OUTRO_SCRIPT = (
    "So, three things to remember. React fast, but with evidence. Contain first, and "
    "reconcile every suspect unit. And close an issue only when the fix is proven in real "
    "production. Here's your action for this week. Write down the first thirty minutes of "
    "your reaction plan for one critical defect. Great work completing this lesson. Next, "
    "you'll go deeper into Root Cause Analysis."
)

# One story thread: Farhan's network-camera plant, Line 4. After a lens fixture
# changeover, 24 of 800 units fail focus (3.0% vs a 0.4% baseline).
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What QRQC Is",
        "points": [("Detect it and make it visible", "You detect it"),
                   ("Contain it to protect the customer", "You contain it"),
                   ("Find the cause with facts, prove the fix", "Then you find the cause"),
                   ("Speed never replaces evidence", "Speed matters")],
        "example": "Line 4: QRQC starts by isolating the work order — not by resetting the tester.",
        "example_cue": "On Farhan's Line four",
        "script": "Here's the core idea. QRQC stands for quick response quality control. It's a "
                  "disciplined way to react to a problem. You detect it and make it visible. You "
                  "contain it, to protect your customer. Then you find the cause with facts, and "
                  "prove the fix works. Speed matters, but it never replaces evidence. On "
                  "Farhan's Line four, QRQC starts by isolating the work order. Not by resetting "
                  "the tester. So what's behind this approach?",
    },
    {
        "key": "p02", "num": 2, "title": "Core Principles",
        "points": [("Real place, real parts", "Go to the real place"),
                   ("Verified facts, never blame", "Use verified facts"),
                   ("React at once to customer or safety risk", "React at once"),
                   ("Containment ≠ permanent fix", "And keep temporary containment")],
        "example": "Farhan's huddle starts with the failed camera on the table, next to its records.",
        "example_cue": "Farhan's huddle starts",
        "script": "QRQC grew up in automotive supplier quality. It rests on a few principles. "
                  "Go to the real place, and look at the real parts. Use verified facts, never "
                  "opinions or blame. React at once to any customer or safety risk. And keep "
                  "temporary containment separate from the permanent fix. Farhan's huddle starts "
                  "with the failed camera on the table, next to its records. What would you put "
                  "on your table?",
    },
    {
        "key": "p03", "num": 3, "title": "Three Escalation Levels",
        "points": [("Level 1: line or shift reacts", "At level one"),
                   ("Level 2: cross-functional team", "At level two"),
                   ("Level 3: plant leaders, customer", "At level three"),
                   ("Escalate at once: safety, repeat escape", "Escalate right away")],
        "example": "Your site sets the escalation timings, based on risk.",
        "example_cue": "Your site sets the timings",
        "script": "A good QRQC system has three levels. At level one, the line or shift detects "
                  "the problem, stops or segregates, and logs the evidence. At level two, a "
                  "cross-functional team investigates and acts. At level three, plant leaders "
                  "add resources, or talk to the customer. Escalate right away for safety, or a "
                  "repeat escape. Your site sets the timings, based on risk. So what happens in "
                  "the first few minutes?",
    },
    {
        "key": "p04", "num": 4, "title": "The First 30 Minutes",
        "points": [("0–5 min: detect, find station & lot, isolate", "In the first five minutes"),
                   ("Then: tell lead & Quality, keep samples", "Next, tell the shift lead"),
                   ("Then: find the last known good point", "Then find the last known good"),
                   ("By 30 min: quarantine, record, assign", "By thirty minutes")],
        "example": "Never restart a critical process on a verbal okay.",
        "example_cue": "never restart a critical process",
        "script": "The first half hour sets the tone. In the first five minutes, detect it, find "
                  "the station and lot, and stop or isolate the flow. Next, tell the shift lead "
                  "and Quality, and keep failed and good samples. Then find the last known good "
                  "point. By thirty minutes, quarantine the suspect stock, and record quantities "
                  "and owners. And never restart a critical process on a verbal okay. What would "
                  "your first call be?",
    },
    {
        "key": "p05", "num": 5, "title": "5W2H: Define the Problem",
        "points": [("What, where, when, who", "What failed, where"),
                   ("How detected, how many", "how it was detected"),
                   ("Confirmed rejects vs suspect population", "Separate confirmed rejects")],
        "example": "Line 4: 18 of 600 cameras failed focus between 10:00 and noon, right after a lens fixture changeover.",
        "example_cue": "On Line four, eighteen",
        "script": "A sharp problem statement stops you chasing the wrong thing. Use 5W2H. What "
                  "failed, where, when, who saw it, how it was detected, and how many. Separate "
                  "confirmed rejects from the suspect population. Here's Farhan's statement. On "
                  "Line four, eighteen of six hundred cameras failed focus, between ten and noon. "
                  "It started right after a lens fixture changeover. Notice how that already "
                  "points somewhere. But first, what about the suspect units?",
    },
    {
        "key": "p06", "num": 6, "title": "Containment & Reconciliation",
        "points": [("Find the suspect scope", "Find the suspect scope"),
                   ("Hold it: physically and in the system", "Hold that stock"),
                   ("Screen based on risk", "Screen it based on risk"),
                   ("Reconcile every unit", "Then reconcile every unit")],
        "example": "2,000 suspect cameras: screened good + failed + waiting must add up exactly. No unit may disappear.",
        "example_cue": "Farhan had two thousand",
        "script": "Containment is a barrier, not a cure. Find the suspect scope by serial "
                  "number, work order and shift. Hold that stock, both physically and in the "
                  "system. Screen it based on risk. Then reconcile every unit. Farhan had two "
                  "thousand suspect cameras. Most screened good, some failed, and the rest were "
                  "still waiting. The numbers must add up exactly. No unit may simply disappear. "
                  "So where does the team track all this?",
    },
    {
        "key": "p07", "num": 7, "title": "The QRQC Board & Huddle",
        "points": [("Risk, containment, cause, action, owner, date", "Each issue shows"),
                   ("Red open · amber verifying · green proven", "Use red for open"),
                   ("Bring real samples and trend charts", "Bring the real samples"),
                   ("Nothing 'done' without proof", "watch for meeting theatre")],
        "example": "Farhan's 15-minute huddle: new problems, then containment, then actions and escalations.",
        "example_cue": "Farhan runs a fifteen-minute",
        "script": "The QRQC board is your control centre. Each issue shows its risk, "
                  "containment, cause, action, owner and due date. Use red for open, amber for "
                  "verifying, and green only for proven closure. Farhan runs a fifteen-minute "
                  "huddle at the board each shift. New problems first, then containment, then "
                  "actions and escalations. Bring the real samples and trend charts. And watch "
                  "for meeting theatre. Is anything marked done without proof?",
    },
    {
        "key": "p08", "num": 8, "title": "Root Cause with Evidence",
        "points": [("Five whys = a hypothesis, not proof", "A five whys chain"),
                   ("Reproduce the failure safely", "Reproduce the failure"),
                   ("Brainstorm across the 6M", "Brainstorm causes across"),
                   ("Happened · escaped · system allowed", "Look for three causes")],
        "example": "A fishbone alone isn't enough: each competing idea has to be tested.",
        "example_cue": "Then test the competing ideas",
        "script": "Now find the root cause, with evidence. A five whys chain is a hypothesis, "
                  "not proof. Reproduce the failure safely if you can. Brainstorm causes across "
                  "people, machine, method, material, measurement and environment. Then test the "
                  "competing ideas. Look for three causes. Why it happened, why it escaped, and "
                  "what in the system allowed both. Can you see why a fishbone alone isn't "
                  "enough?",
    },
    {
        "key": "p09", "num": 9, "title": "Corrective Action & Change Control",
        "points": [("Fix how it happened and how it escaped", "Tackle both"),
                   ("Engineered controls over reminders", "Prefer engineered controls"),
                   ("Check cycle time, safety, false rejects", "Check the effect"),
                   ("Update FMEA, SOP, training", "Then update the FMEA")],
        "example": "A verbal 'check the fixture' became a scan: each fixture linked to its approved recipe.",
        "example_cue": "On Farhan's line",
        "script": "Now fix each verified cause. Tackle both how it happened, and how it escaped. "
                  "Prefer engineered controls, like keyed fixtures and scan interlocks, over "
                  "reminders. Check the effect on cycle time, safety and false rejects. Then "
                  "update the FMEA, the SOP and the training. On Farhan's line, a verbal "
                  "instruction to check the fixture became a scan. Each fixture is now linked to "
                  "its approved recipe. So when can you close it?",
    },
    {
        "key": "p10", "num": 10, "title": "Closure Criteria",
        "points": [("Installed ≠ proven", "Installing a fix"),
                   ("Challenge: good, bad, borderline parts", "challenge it with known good"),
                   ("Across shifts, models, changeovers", "Check it across shifts"),
                   ("Every suspect unit decided, then sign-off", "Make sure every suspect")],
        "example": "Farhan's rule: ten production days with no repeat before the board turns green.",
        "example_cue": "Farhan waits ten",
        "script": "Here's the trap. Installing a fix is not the same as proving it. To close, "
                  "challenge it with known good, known bad and borderline parts. Check it across "
                  "shifts, models and changeovers. Track recurrence and yield for a set period. "
                  "Make sure every suspect unit has a decision. Then Quality and the owner sign "
                  "off. Farhan waits ten production days with no repeat. Only then does the board "
                  "turn green. How do you measure all of this?",
    },
    {
        "key": "p11", "num": 11, "title": "QRQC KPIs",
        "points": [("Response time: detection → containment", "Response time runs"),
                   ("Containment coverage %", "Containment coverage is"),
                   ("First pass yield and defect rate", "Track first pass yield"),
                   ("On-time action closure", "measure on-time closure")],
        "example": "95% of suspect units found = not done: 5% are still out there.",
        "example_cue": "If you've found",
        "script": "Use a balanced set of measures. Response time runs from detection to the "
                  "first effective containment. Containment coverage is the share of suspect "
                  "units you've accounted for. Track first pass yield and the defect rate. And "
                  "measure on-time closure of actions. Here's a subtle one. If you've found "
                  "ninety-five percent of the suspect units, you're not nearly done. Five "
                  "percent are still out there. Ready for Farhan's case?",
    },
    {
        "key": "p12", "num": 12, "title": "Case Study: Focus Failure",
        "points": [("24 of 800 fail focus vs < 0.5% normal", "After the changeover"),
                   ("Hold work order + output since last good setup", "Farhan held the work order"),
                   ("Compare fixture, recipe, focus trend", "The team compared"),
                   ("Test the spacer hypothesis", "Their hypothesis was")],
        "example": "The wrong spacer reproduced the failure on controlled samples. Only then was it called the cause.",
        "example_cue": "So they tested it",
        "script": "Here's the full story. After the changeover, twenty-four of eight hundred "
                  "cameras failed focus. The normal rate was under half a percent. Farhan held "
                  "the work order, and everything since the last good setup. The team compared "
                  "fixture records, recipe versions and focus trends. Their hypothesis was a "
                  "wrong spacer. So they tested it on controlled samples, and it reproduced the "
                  "failure. Only then did they call it the cause. Would your team have waited?",
    },
    {
        "key": "p13", "num": 13, "title": "Case Study: Label Mismatch",
        "points": [("Carton label ≠ device inside", "A video recorder carton"),
                   ("Hold the pallet, match every serial", "The team held the pallet"),
                   ("Trace scans and printer jobs", "Then they traced"),
                   ("Force serial-to-SKU match, log bypasses", "So the fix forced")],
        "example": "Root cause: the MES match was switched off during a printer fault, and nobody logged it.",
        "example_cue": "The MES match had been",
        "script": "Here's a second case, from packing. A video recorder carton showed the wrong "
                  "SKU. The product inside worked perfectly. But the customer would still get "
                  "the wrong item. The team held the pallet, and matched every serial to its "
                  "label. Then they traced the scans and printer jobs. The MES match had been "
                  "switched off during a printer fault. Nobody logged it. So the fix forced a "
                  "serial-to-SKU match before printing, and logged every bypass. Would you have "
                  "looked there?",
    },
    {
        "key": "p14", "num": 14, "title": "90-Day Deployment",
        "points": [("Pilot one high-risk area first", "Start with one high-risk"),
                   ("Days 1–30: triggers, levels, board", "In the first thirty days"),
                   ("Days 31–60: train leaders, run huddles", "In the next thirty"),
                   ("Days 61–90: audit, link to FMEA, expand", "In the last thirty")],
        "example": "Roll out QRQC like an operating system, not a standalone form.",
        "example_cue": "roll out QRQC like an operating",
        "script": "Now, roll out QRQC like an operating system, not a standalone form. "
                  "Start with one high-risk pilot area, and get the method stable there. In the "
                  "first thirty days, set triggers, levels and the board. In the next thirty, "
                  "train your line leaders and run the huddles. In the last thirty, audit the "
                  "actions, link them to the FMEA, and expand to other lines. Who owns what?",
    },
    {
        "key": "p15", "num": 15, "title": "The Issue Record & Roles",
        "points": [("Plant head sponsors", "The plant head sponsors"),
                   ("Quality owns the method", "Quality owns the method"),
                   ("Production owns the reaction", "Production owns"),
                   ("Engineering owns the technical fixes", "And Engineering owns"),
                   ("One record for every issue", "Keep one record")],
        "example": "The test: could someone rebuild the whole event from your record alone?",
        "example_cue": "Could someone rebuild",
        "script": "The plant head sponsors it. Quality owns the method. Production owns the "
                  "immediate reaction. And Engineering owns the technical fixes. Keep one record "
                  "for every issue. It holds the problem, photos and suspect window. It holds "
                  "the containment and reconciliation, the causes, the actions and the proof. "
                  "Here's the test. Could someone rebuild the whole event from your record "
                  "alone? React quickly, but always close with evidence.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Detect, make it visible", "icon": "sensor", "with": 0},
        {"label": "Contain: protect the customer", "icon": "lock", "with": 1},
        {"label": "Cause with facts, prove the fix", "icon": "search", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Reset the tester", "sub": "and run on", "icon": "power"},
            {"label": "Isolate the work order", "sub": "QRQC starts here", "icon": "lock"}]}},
    "p02": {"type": "icons", "items": [
        {"label": "Real place, real parts", "icon": "walk"}, {"label": "Facts, never blame", "icon": "search"},
        {"label": "React at once", "icon": "warning"}, {"label": "Containment is not the fix", "icon": "lock"}]},
    "p03": {"type": "flow", "items": [
        {"label": "Level 1: line or shift", "sub": "Stop, segregate, log", "icon": "person", "with": 0},
        {"label": "Level 2: cross-functional team", "sub": "Investigate and act", "icon": "gear", "with": 1},
        {"label": "Level 3: plant leaders", "sub": "Resources, the customer", "icon": "shield", "with": 2}]},
    "p04": {"type": "timeline", "items": [
        {"label": "Detect, find station and lot, isolate", "sub": "0–5", "span": 5, "icon": "sensor"},
        {"label": "Tell the lead and Quality, keep samples", "sub": "Next", "span": 8, "icon": "person"},
        {"label": "Find the last known good point", "sub": "Then", "span": 7, "icon": "search"},
        {"label": "Quarantine, record, assign", "sub": "By 30", "span": 10, "icon": "lock"}]},
    "p05": {"type": "icons", "items": [
        {"label": "What, where, when, who", "icon": "search", "with": 0},
        {"label": "How detected, how many", "icon": "count", "with": 1},
        {"label": "Rejects vs suspects", "icon": "stack", "with": 2}],
        "then": {"type": "stat", "value": 18, "suffix": " of 600", "icon": "camera", "label": "cameras failed focus",
                 "unit": "10:00 to noon, right after a lens fixture changeover", "with": "example"}},
    "p06": {"type": "icons", "items": [
        {"label": "Find the scope", "icon": "search"}, {"label": "Hold it", "icon": "lock"},
        {"label": "Screen by risk", "icon": "test"}, {"label": "Reconcile", "icon": "count"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2,000 suspect cameras", "icon": "stack", "with": "example"},
            {"label": "Good + failed + waiting", "icon": "count", "with": "example"},
            {"label": "= 2,000: none missing", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Open", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Verifying", "icon": "clock", "with": 1},
        {"label": "Proven", "sub": "Only then: green", "icon": "check", "tone": "good", "with": 1}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "New problems", "icon": "warning", "with": "example"},
            {"label": "Containment", "icon": "lock", "with": "example"},
            {"label": "Actions, escalations", "icon": "sequence", "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "People", "icon": "person", "with": 2}, {"label": "Machine", "icon": "gear", "with": 2},
        {"label": "Method", "icon": "clipboard", "with": 2}, {"label": "Material", "icon": "box", "with": 2},
        {"label": "Measurement", "icon": "scale", "with": 2}, {"label": "Environment", "icon": "wave", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Happened + escaped", "icon": "search"}, {"label": "Engineered controls", "icon": "key"},
        {"label": "Cycle time, safety", "icon": "clock"}, {"label": "FMEA, SOP, training", "icon": "clipboard"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "“Check the fixture”", "sub": "A verbal reminder", "icon": "person"},
            {"label": "Fixture scan", "sub": "Linked to its approved recipe", "icon": "barcode"}]}},
    "p10": {"type": "icons", "items": [
        {"label": "Installed is not proven", "icon": "cross", "tone": "bad"}, {"label": "Challenge it", "icon": "test"},
        {"label": "Across shifts, models", "icon": "sequence"}, {"label": "Every unit decided", "icon": "check"}],
        "then": {"type": "stat", "value": 10, "suffix": " days", "icon": "calendar", "label": "of production with no repeat",
                 "unit": "before the board turns green", "with": "example"}},
    "p11": {"type": "icons", "items": [
        {"label": "Response time", "icon": "clock"}, {"label": "Containment coverage", "icon": "count"},
        {"label": "Yield, defect rate", "icon": "chartUp"}, {"label": "On-time closure", "icon": "calendar"}],
        "then": {"type": "stat", "value": 5, "suffix": "%", "icon": "warning", "label": "of suspect units still out there",
                 "unit": "Finding 95% is not done", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "24 of 800 fail focus", "sub": "Normal: under 0.5%", "icon": "camera", "tone": "bad", "with": 0},
        {"label": "Hold since the last good setup", "icon": "lock", "with": 1},
        {"label": "Compare fixture, recipe, trend", "icon": "search", "with": 2},
        {"label": "Wrong spacer reproduced it", "sub": "Only then: the cause", "icon": "test", "tone": "good", "with": "example"}]},
    "p13": {"type": "flow", "items": [
        {"label": "Carton label ≠ device", "icon": "label", "tone": "bad", "with": 0},
        {"label": "Hold the pallet, match serials", "icon": "lock", "with": 1},
        {"label": "MES match switched off", "sub": "During a printer fault, not logged", "icon": "warning", "tone": "bad", "with": "example"},
        {"label": "Forced serial-to-SKU match", "sub": "Every bypass logged", "icon": "barcode", "tone": "good", "with": 3}]},
    "p14": {"type": "timeline", "items": [
        {"label": "Triggers, levels, board", "sub": "Days 1–30", "icon": "clipboard", "with": 1},
        {"label": "Train leaders, run huddles", "sub": "31–60", "icon": "person", "with": 2},
        {"label": "Audit, link to FMEA, expand", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Plant head", "sub": "Sponsors", "icon": "person"}, {"label": "Quality", "sub": "The method", "icon": "shield"},
        {"label": "Production", "sub": "The reaction", "icon": "wrench"}, {"label": "Engineering", "sub": "The fixes", "icon": "gear"},
        {"label": "One record", "sub": "Every issue", "icon": "clipboard"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p07",
        "question": "1,900 of 2,000 suspect units have been found and screened. Is containment complete?",
        "options": ["Yes — 95% is good enough", "No — 100 suspect units are still unaccounted for",
                    "Yes, if the fix is installed"],
        "correct": 1,
        "explanation": "Containment coverage of 95% means 5% of the suspect population is still out there. Containment is complete only when every unit is accounted for.",
        "q_script": "Quick check. Nineteen hundred of two thousand suspect units have been found "
                    "and screened. Is containment complete? Take a few seconds.",
        "a_script": "No. One hundred suspect units are still unaccounted for. Containment is "
                    "complete only when every unit is found.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Focus failures jump at test right after a fixture changeover. The tester is reset and passes. What should happen FIRST?",
        "options": ["Keep running — the tester passed", "Isolate units since the last good setup and record the evidence",
                    "Change the fixture back and say nothing", "Wait for the end-of-day meeting"],
        "correct": 1,
        "explanation": "Protect the customer first: hold everything since the last verified setup, keep samples and records, then investigate. Resetting the tester hides the abnormality.",
        "q_script": "One more, and this one's a scenario. Focus failures jump right after a "
                    "fixture changeover. Someone resets the tester, and it passes. What should "
                    "happen first? Have a think.",
        "a_script": "Isolate every unit since the last good setup, and record the evidence. Then "
                    "investigate. Resetting the tester only hides the problem.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
