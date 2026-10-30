"""One Point Lesson (OPL) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Ravi,
a shift supervisor on a video-recorder box-build line, turning hard-won
lessons into one-page, visual training at the workstation.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/one_point_lesson.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py one_point_lesson  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "op"
NAME = "one_point_lesson"

LETTERS = ["OPL", "SOP", "PCB", "AOI", "ESD", "TPM", "FMEA", "LPA", "FPY"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    return re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)


INTRO_SCRIPT = (
    "Night shift. A new operator fits a connector the wrong way, and cracks it. The day "
    "shift knew the trick. Nobody had shared it. Sound familiar? In this lesson, you'll "
    "learn the One Point Lesson. It's a one-page, visual way to teach one thing well, "
    "right at the workstation. We'll follow Ravi, a shift supervisor on a video recorder "
    "line, as he builds his first ones."
)
OUTRO_SCRIPT = (
    "So, three things to remember. One topic, one clear point, and a strong visual. Teach "
    "it at the gemba, and confirm it by watching the work. And control it, so it always "
    "matches the current standard. Here's your action for this week. Pick one mistake "
    "that keeps repeating, and draft a One Point Lesson for it. Great work completing "
    "this lesson. Next, you'll learn Poka Yoke, mistake-proofing."
)

# One story thread: Ravi's NVR box-build line, night shift vs day shift skill gap.
# First OPL: correct connector insertion. Others: screw sequence, label check.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What a One Point Lesson Is",
        "points": [("One thing, on one page", "teaches one thing on one"),
                   ("Short: learned in minutes", "It's short"),
                   ("Visual: good and bad examples", "It's visual"),
                   ("Taught at the workplace", "it's taught right at the workplace")],
        "example": "Ravi's first OPL, connector insertion: the right grip, the wrong grip, and the click to listen for.",
        "example_cue": "Ravi's first one",
        "script": "Here's the core idea. A One Point Lesson, or OPL, teaches one thing on one "
                  "page. It's short, so you learn it in a few minutes. It's visual, with photos "
                  "and clear good and bad examples. And it's taught right at the workplace. "
                  "Ravi's first one covered connector insertion. One photo of the right grip, one "
                  "of the wrong grip, and the click to listen for. What do you think it should "
                  "never replace?",
    },
    {
        "key": "p02", "num": 2, "title": "What an OPL Is Not",
        "points": [("Never replaces your SOP", "An OPL never replaces"),
                   ("No big topic squeezed onto one page", "It doesn't squeeze"),
                   ("Reinforces one critical point", "it reinforces one critical point")],
        "example": "Ravi's connector lesson sits beside the SOP and points to the exact step it supports.",
        "example_cue": "Ravi's connector lesson",
        "script": "An OPL never replaces your SOP. It isn't a work instruction, a full "
                  "specification, or a certification. It doesn't squeeze a big topic onto one "
                  "crowded page either. Instead, it reinforces one critical point, so people "
                  "remember it. Ravi's connector lesson sits right beside the SOP. It points to "
                  "the exact step it supports. So the standard stays the master, and the OPL "
                  "makes it stick. Why is that worth the effort?",
    },
    {
        "key": "p03", "num": 3, "title": "Why OPLs Pay Off",
        "points": [("Closes skill gaps between shifts", "OPLs close skill gaps"),
                   ("New people learn faster", "New people learn faster"),
                   ("Lessons from defects shared quickly", "Lessons from defects"),
                   ("Skilled operators become trainers", "your skilled operators")],
        "example": "Night shift cracked 14 connectors a week; day shift cracked 2. Same SOP, different know-how.",
        "example_cue": "Ravi's night shift cracked",
        "script": "OPLs close skill gaps between people and shifts. Ravi's night shift cracked "
                  "fourteen connectors a week. Day shift cracked two. Same SOP, but different "
                  "know-how. A One Point Lesson spreads that know-how in minutes. New people "
                  "learn faster. Lessons from defects and breakdowns get shared quickly. And your "
                  "skilled operators become trainers, which builds real ownership. The payback "
                  "shows up in quality, safety and cost. So which kinds can you make?",
    },
    {
        "key": "p04", "num": 4, "title": "Types of OPL",
        "points": [("Basic knowledge, e.g. ESD handling", "A basic knowledge lesson"),
                   ("Problem: defect, cause and fix", "A problem lesson"),
                   ("Improvement: a better method from Kaizen", "An improvement lesson"),
                   ("Safety · Quality · Maintenance", "Then there are safety")],
        "example": "Ravi's cracked-connector lesson is a problem type.",
        "example_cue": "Ravi's cracked connector lesson",
        "script": "There are six common types. A basic knowledge lesson teaches something "
                  "everyone must know, like ESD handling. A problem lesson explains a defect, its "
                  "cause and its fix. An improvement lesson shares a better method from a Kaizen. "
                  "Then there are safety, quality and maintenance lessons. Ravi's cracked "
                  "connector lesson is a problem type. Names may differ at your site. The rule "
                  "doesn't. One clear point. So when should you make one?",
    },
    {
        "key": "p05", "num": 5, "title": "When to Create One",
        "points": [("A repeat defect just solved", "A repeat defect has just"),
                   ("New product, machine or jig", "A new product"),
                   ("A step keeps being misunderstood", "A step in the SOP"),
                   ("A near miss or a skilled person's trick", "A near miss")],
        "example": "Ravi's trigger: the cause of the cracked connectors was found — now the fix had to reach every shift.",
        "example_cue": "For Ravi, the trigger",
        "script": "Make one when a small piece of knowledge can change behaviour. A repeat "
                  "defect has just been solved. A new product, machine or jig arrives. A step in "
                  "the SOP keeps being misunderstood. A near miss reveals a gap. Or a skilled "
                  "person knows a trick nobody else does. For Ravi, the trigger was clear. The "
                  "cause of the cracked connectors was found. Now the fix had to reach every "
                  "shift. What goes on the page?",
    },
    {
        "key": "p06", "num": 6, "title": "Structure of a Good OPL",
        "points": [("Number, title, revision, date", "Start with a number"),
                   ("Why it matters + the one key point", "Then say why it matters"),
                   ("Visuals, steps, caution", "Add the visuals"),
                   ("Owner, approval, training record", "Finish with the owner")],
        "example": "The page should make sense at a glance — could your newest operator read it in a minute?",
        "example_cue": "The page should make sense",
        "script": "Every OPL follows the same layout, so people know where to look. Start with "
                  "a number, a short title, the revision and the date. Then say why it matters, "
                  "and state the one key point. Add the visuals and any simple steps. Include a "
                  "caution where there's a risk. Finish with the owner, the approval and the "
                  "training record. The page should make sense at a glance. Could your newest "
                  "operator read yours in a minute?",
    },
    {
        "key": "p07", "num": 7, "title": "How to Prepare It",
        "points": [("Define one learning objective", "defining one learning objective"),
                   ("Go to the gemba, verify the standard", "Then go to the gemba"),
                   ("Simple words, real photos, good vs bad", "Next, put it"),
                   ("Check, then approve", "Then have Quality")],
        "example": "Ravi photographed the real connector, at the real station.",
        "example_cue": "Ravi photographed",
        "script": "Start by defining one learning objective. Then go to the gemba, and watch "
                  "the real work. Verify the approved standard and the root cause. Next, put it "
                  "in simple words your operators use. Add real photos, arrows and good and bad "
                  "examples. Draft it on the standard template. Then have Quality or Engineering "
                  "check it, and approve it. Ravi photographed the real connector, at the real "
                  "station. Now, how do you make the visuals work?",
    },
    {
        "key": "p08", "num": 8, "title": "Visual Communication",
        "points": [("Real photos, arrows on the exact spot", "Use real photos"),
                   ("Good and bad side by side", "Put good and bad"),
                   ("Large text, plenty of space", "Use large text"),
                   ("Never use colour as the only signal", "never use colour")],
        "example": "Ravi's OPL shows a tick, a cross, and the words good and not good.",
        "example_cue": "Ravi added a tick",
        "script": "Visuals are the heart of an OPL. Your learner should get the point before "
                  "reading a single sentence. Use real photos, with arrows and circles on the "
                  "exact spot. Put good and bad side by side. Use large text and plenty of "
                  "space. Avoid long paragraphs and jargon. And never use colour as the only "
                  "signal. Ravi added a tick, a cross, and the words good and not good. So how "
                  "do you actually teach it?",
    },
    {
        "key": "p09", "num": 9, "title": "Delivering at the Gemba",
        "points": [("Explain why it matters", "Explain why it matters"),
                   ("Show, demonstrate, compare", "Show the real part"),
                   ("Ask questions, let them try", "Ask short questions"),
                   ("A signature alone proves nothing", "A signature alone")],
        "example": "Ravi teaches each lesson in 5 minutes at shift start, then watches every operator do it.",
        "example_cue": "Ravi teaches each lesson",
        "script": "Teach it where the work happens. Explain why it matters, in terms of "
                  "quality or safety. Show the real part. Demonstrate slowly, then compare good "
                  "and bad. Ask short questions to check understanding. Let the learner try it, "
                  "and correct mistakes on the spot. Ravi teaches each lesson in five minutes "
                  "at shift start. Then he watches every operator do it. A signature alone "
                  "proves nothing. Where else can OPLs help?",
    },
    {
        "key": "p10", "num": 10, "title": "OPLs for Box Build & Quality",
        "points": [("Boards: AOI false call vs real defect", "On boards"),
                   ("Assembly: screw sequence, connector locking", "At assembly"),
                   ("Test: firmware version check", "At test"),
                   ("Packing: label and accessory checks", "At packing")],
        "example": "Wrong PCB prevention: where to read the board number, how to match the model, what to do on a mismatch.",
        "example_cue": "Ravi's next lesson",
        "script": "Almost every process has a good OPL topic. On boards, teach how to tell an "
                  "AOI false call from a real defect. At assembly, teach the screw sequence and "
                  "connector locking. At test, teach the firmware version check. At packing, "
                  "teach label and accessory checks. Ravi's next lesson was wrong PCB "
                  "prevention. Where to read the board number, how to match the model, and what to "
                  "do on a mismatch. Which topic would help you most?",
    },
    {
        "key": "p11", "num": 11, "title": "OPLs and Other Lean Tools",
        "points": [("After a Kaizen: the new method", "After a Kaizen"),
                   ("After a Poka Yoke: what its alarm means", "After a Poka Yoke"),
                   ("5S standards and machine care", "It teaches five S"),
                   ("Lessons from root cause analysis", "It shares the lessons")],
        "example": "New fixture → an OPL on how to load it, and what the red light means.",
        "example_cue": "Ravi's team installed",
        "script": "OPLs help other Lean tools work on the floor. After a Kaizen, an OPL teaches "
                  "the new method. After a Poka Yoke goes in, it explains how the device works, "
                  "and what its alarm means. It teaches five S standards, and basic machine care "
                  "for TPM. It shares the lessons from root cause analysis. Ravi's team "
                  "installed a new fixture. Their OPL taught how to load it, and what the red "
                  "light means. But how do you keep OPLs correct?",
    },
    {
        "key": "p12", "num": 12, "title": "Control and Revisions",
        "points": [("Number, owner, approver", "Give it a unique number"),
                   ("Linked to the SOP it supports", "Link it to the SOP"),
                   ("Reviewed whenever anything changes", "Review it whenever"),
                   ("Old copies removed from the line", "And remove old copies")],
        "example": "When the connector supplier changed, Ravi revised the lesson and pulled every old copy.",
        "example_cue": "When Ravi's connector supplier",
        "script": "An OPL is a controlled document, even though it's short. Give it a unique "
                  "number, an owner and an approver. Link it to the SOP it supports. Review it "
                  "whenever the product, process or standard changes. And remove old copies "
                  "from the line. When Ravi's connector supplier changed, he revised the lesson, "
                  "and pulled every old copy. Here's the golden rule. An OPL must never "
                  "conflict with your current standard. So, did it work?",
    },
    {
        "key": "p13", "num": 13, "title": "Measuring Effectiveness",
        "points": [("Changed behaviour is the result", "Changed behaviour is"),
                   ("Check knowledge with questions", "So check knowledge"),
                   ("Watch the method days later", "Then watch the method"),
                   ("Track the targeted defect", "And track the defect")],
        "example": "Night shift: 14 cracked connectors a week → 1 a week, six weeks after the lesson.",
        "example_cue": "Ravi's night shift cracked",
        "script": "Here's the real test. Training completion is not the result. Changed "
                  "behaviour is. So check knowledge with a few questions. Then watch the method "
                  "at the gemba, days later. And track the defect you were targeting. Ravi's "
                  "night shift cracked fourteen connectors a week. Six weeks after the lesson, "
                  "they cracked one. If a problem continues, don't just retrain. Look at the "
                  "standard and the process too. What mistakes should you avoid?",
    },
    {
        "key": "p14", "num": 14, "title": "Common Mistakes",
        "points": [("Too much content → split it", "Too much content"),
                   ("Text only → add real photos", "Only text"),
                   ("Signature only → demonstrate and observe", "Training by signature"),
                   ("Old version on the wall → revision control", "An old version")],
        "example": "Ravi's first draft covered four topics. He split it into four lessons.",
        "example_cue": "Ravi's first draft",
        "script": "Watch for a few classic mistakes. Too much content on one page? Split it. "
                  "Only text, no pictures? Add real photos. Training by signature only? "
                  "Demonstrate, question and observe. An old version still on the wall? Use "
                  "revision control. No check that it worked? Track the defect. And never use "
                  "an OPL to blame someone. Ravi's first draft covered four topics. He split it "
                  "into four lessons. Ready to roll yours out?",
    },
    {
        "key": "p15", "num": 15, "title": "Roadmap & Creator Checklist",
        "points": [("Plan template, numbering, approval", "Plan your template"),
                   ("Pilot on the biggest defects or risks", "Pilot a few lessons"),
                   ("Train the trainers, use at the gemba", "Train supervisors"),
                   ("Measure the effect, build a library", "Measure the effect")],
        "example": "Before release, ask: Is it correct? Is the point obvious?",
        "example_cue": "Before you release any lesson",
        "script": "Roll it out in simple phases. Plan your template, numbering and approval "
                  "flow. Pilot a few lessons on your biggest defects or safety risks. Train "
                  "supervisors and skilled operators to teach them. Then use them at shift "
                  "meetings and at the gemba. Measure the effect, and build a controlled "
                  "library. Before you release any lesson, ask yourself. Is it correct? Is the "
                  "point obvious? Teach one point well, and keep it current.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "One thing", "icon": "check"}, {"label": "Minutes to learn", "icon": "clock"},
        {"label": "Visual", "icon": "camera"}, {"label": "At the workplace", "icon": "wrench"}]},
    "p02": {"type": "versus", "items": [
        {"label": "Replacing the SOP", "sub": "or cramming a big topic", "icon": "cross", "with": 0},
        {"label": "Beside the SOP", "sub": "Points to the exact step", "icon": "clipboard", "with": 2}]},
    "p03": {"type": "compare", "before": {"label": "Night shift", "value": 14}, "after": {"label": "Day shift", "value": 2},
            "unit": "cracked connectors a week", "note": "Same SOP, different know-how", "with": "example"},
    "p04": {"type": "icons", "items": [
        {"label": "Basic knowledge", "icon": "chip", "with": 0}, {"label": "Problem", "icon": "warning", "with": 1},
        {"label": "Improvement", "icon": "chartUp", "with": 2}, {"label": "Safety", "icon": "shield", "with": 3},
        {"label": "Quality", "icon": "check", "with": 3}, {"label": "Maintenance", "icon": "wrench", "with": 3}]},
    "p05": {"type": "icons", "items": [
        {"label": "Repeat defect solved", "icon": "check"}, {"label": "New product or jig", "icon": "box"},
        {"label": "Misunderstood step", "icon": "search"}, {"label": "Near miss, or a trick", "icon": "warning"}]},
    "p06": {"type": "doc", "items": [
        {"label": "OPL-012 · Connector insertion · Rev B", "icon": "label", "with": 0},
        {"label": "Key point: push until it clicks", "icon": "key", "with": 1},
        {"label": "", "icon": "goodbad", "with": 2},
        {"label": "Caution: never force it", "icon": "warning", "with": 2},
        {"label": "Owner · approved · trained", "icon": "person", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "One learning objective", "icon": "search"},
        {"label": "Go to the gemba", "sub": "Verify the standard", "icon": "walk"},
        {"label": "Simple words, real photos", "icon": "camera"},
        {"label": "Check, then approve", "icon": "check", "tone": "good"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Real photos, arrows", "icon": "camera", "with": 0},
        {"label": "Good and bad side by side", "icon": "shape", "with": 1},
        {"label": "Large text, space", "icon": "label", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Colour only", "sub": "Not everyone sees it", "icon": "warning"},
            {"label": "Tick, cross + words", "sub": "Good / not good", "icon": "check"}]}},
    "p09": {"type": "flow", "items": [
        {"label": "Explain why it matters", "icon": "person"},
        {"label": "Show, demonstrate, compare", "icon": "camera"},
        {"label": "Ask, then let them try", "icon": "hand"},
        {"label": "A signature proves nothing", "icon": "cross", "tone": "bad"}]},
    "p10": {"type": "flow", "items": [
        {"label": "Boards", "sub": "AOI false call vs real defect", "icon": "chip"},
        {"label": "Assembly", "sub": "Screw sequence, connector locking", "icon": "screw"},
        {"label": "Test", "sub": "Firmware version check", "icon": "test"},
        {"label": "Packing", "sub": "Label and accessories", "icon": "label"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Kaizen", "icon": "chartUp"}, {"label": "Poka Yoke", "icon": "key"},
        {"label": "5S + TPM", "icon": "tray"}, {"label": "Root cause", "icon": "search"}]},
    "p12": {"type": "flow", "items": [
        {"label": "Number, owner, approver", "icon": "label"},
        {"label": "Linked to its SOP", "icon": "clipboard"},
        {"label": "Reviewed on every change", "icon": "sequence"},
        {"label": "Old copies removed", "icon": "trash", "tone": "good"}]},
    "p13": {"type": "icons", "items": [
        {"label": "Changed behaviour", "icon": "person", "with": 0},
        {"label": "A few questions", "icon": "search", "with": 1},
        {"label": "Watch, days later", "icon": "clock", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 14}, "after": {"label": "6 weeks after", "value": 1},
                 "unit": "cracked connectors a week, night shift", "note": "The lesson changed behaviour", "with": "example"}},
    "p14": {"type": "icons", "items": [
        {"label": "Too much?", "sub": "Split it", "icon": "stack"},
        {"label": "Text only?", "sub": "Add real photos", "icon": "camera"},
        {"label": "Signature only?", "sub": "Observe the work", "icon": "hand"},
        {"label": "Old version?", "sub": "Revision control", "icon": "sequence"}]},
    "p15": {"type": "steps", "items": [
        {"label": "Template + numbering", "with": 0}, {"label": "Pilot on big defects", "with": 1},
        {"label": "Train the trainers", "with": 2}, {"label": "Use at the gemba", "with": 2},
        {"label": "Measure the effect", "with": 3}, {"label": "Build a library", "with": 3}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A draft OPL covers connector insertion, screw torque, label checks and ESD on one page. What's the problem?",
        "options": ["It needs more text", "It has too many points — split it into separate OPLs",
                    "It should be in colour only"],
        "correct": 1,
        "explanation": "An OPL teaches ONE point. Four topics on one page dilute the message — make four focused OPLs instead.",
        "q_script": "Quick check. A draft lesson covers connector insertion, screw torque, label "
                    "checks and ESD, all on one page. What's the problem? Take a few seconds.",
        "a_script": "It has too many points. A One Point Lesson teaches one thing. Split it into "
                    "four focused lessons.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Everyone signed the OPL two weeks ago, but the same defect is back. What should the supervisor do FIRST?",
        "options": ["Make everyone sign it again", "Observe the work and check the standard, method and lesson",
                    "Blame the operators who signed", "Remove the OPL from the line"],
        "correct": 1,
        "explanation": "Signatures don't prove learning. Go and observe: is the method followed, is the standard right, is the OPL clear? Then fix the cause.",
        "q_script": "One more, and this one's a scenario. Everyone signed the lesson two weeks "
                    "ago, but the same defect is back. What should the supervisor do first? Have a think.",
        "a_script": "Go and observe the work. Check the method, the standard and the lesson "
                    "itself. A signature doesn't prove learning, so find the real cause.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
