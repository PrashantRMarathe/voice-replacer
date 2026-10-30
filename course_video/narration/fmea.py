"""FMEA lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Asha,
a quality engineer at a telecom plant, running a Process FMEA on the housing
gasket of an outdoor 5G small-cell radio after units came back with water inside.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/fmea.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py fmea  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "fm"
NAME = "fmea"

LETTERS = ["FMEA", "PFMEA", "RPN", "SOP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. FMEA letter by letter; 5G = "five-G".
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return re.sub(r"\b5G\b", "five-G", text)


INTRO_SCRIPT = (
    "Six outdoor radio units came back from the field, full of water. In two, the gasket "
    "was missing. In four, it was twisted. Every one had passed final inspection. Sound "
    "familiar? In this lesson, you'll learn FMEA, failure mode and effects analysis. You'll "
    "see how to find risks before they reach a customer, and act on the biggest ones first. "
    "We'll follow Asha, a quality engineer at a telecom plant."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Build a clear chain, from effect to failure mode to a "
    "cause you can control. Score with evidence, and never let the number replace judgement. "
    "And prefer prevention, then prove it works before you rescore. Here's your action for "
    "this week. Pick one critical step, and write its failure chain with your team. Great "
    "work completing this lesson. Next, you'll learn Gemba, the real place."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What FMEA Is",
        "points": [("How could it fail, and why?", "It asks how"),
                   ("What would the effect be?", "what the effect"),
                   ("Act before it reaches the customer", "Then you act")],
        "example": "Asha's target: the housing gasket on an outdoor 5G small cell.",
        "example_cue": "Asha's target",
        "script": "FMEA is a team method for thinking before failure happens. It asks how a product or "
                  "process could fail, and why. It asks what the effect would be, and what controls you "
                  "have today. Then you act, before the failure ever reaches your customer. That's "
                  "built-in quality, not inspection. Asha's target was the housing gasket on an outdoor "
                  "5G small cell. So what words do you need?",
    },
    {
        "key": "p02", "num": 2, "title": "The Key Words",
        "points": [("Failure mode: how it fails", "A failure mode"),
                   ("Effect: what the customer suffers", "The effect"),
                   ("Cause: why it could happen", "The cause"),
                   ("Control and action", "A control")],
        "example": "Mode: gasket twisted. Effect: water inside. Cause: no seating check.",
        "example_cue": "For Asha",
        "script": "Learn five words. A failure mode is how the requirement fails. The effect is what "
                  "happens to the next process, or the customer. The cause is why it could happen. A "
                  "control prevents the cause, or detects the failure. And an action reduces the risk. "
                  "For Asha, the mode was a twisted gasket. The effect was water inside. Can you guess "
                  "the cause?",
    },
    {
        "key": "p03", "num": 3, "title": "Types of FMEA",
        "points": [("System and design FMEA", "System and design"),
                   ("Process FMEA: manufacturing steps", "A Process FMEA"),
                   ("Clear start and end boundaries", "Set clear boundaries")],
        "example": "Asha's scope: from gasket pick-up to the sealed, tested housing.",
        "example_cue": "Asha's scope",
        "script": "There are a few types. System and design FMEA look at the product and how its parts "
                  "work together. Machinery FMEA looks at equipment. A Process FMEA looks at your "
                  "manufacturing steps, and that's the one most Lean teams use. Set clear boundaries, "
                  "so the job stays manageable. Asha's scope ran from picking the gasket up, to a "
                  "sealed, tested housing. When should you build one?",
    },
    {
        "key": "p04", "num": 4, "title": "When to Start or Update",
        "points": [("New product or process", "a new product"),
                   ("Any change: material, tool, layout", "any change"),
                   ("After a complaint or escape", "after a complaint")],
        "example": "Asha updated hers the day the six wet radios came back.",
        "example_cue": "Asha updated",
        "script": "Start one for a new product or a new process. Update it after any change. That "
                  "includes material, equipment, software, tooling, layout or method. And update it "
                  "after a complaint, or whenever you learn a control isn't working. An FMEA that's two "
                  "years old describes a factory that no longer exists. Asha updated hers the day the "
                  "wet radios came back. Who builds it?",
    },
    {
        "key": "p05", "num": 5, "title": "The Team and the Inputs",
        "points": [("A cross-functional team", "Bring production"),
                   ("Experienced operators", "operators who know"),
                   ("Flow chart, data, work instructions", "Bring the inputs"),
                   ("Visit the gemba before scoring", "go to the gemba")],
        "example": "At the gemba, Asha saw two gasket sizes sharing one bin.",
        "example_cue": "At the gemba",
        "script": "Bring production, engineering, quality, maintenance and test. Include experienced "
                  "operators who know the real work. Bring the inputs too. A process flow, defect data, "
                  "work instructions and lessons learned. Then go to the gemba before you score anything. "
                  "Compare the written method with what really happens. At the gemba, Asha saw two gasket "
                  "sizes sharing one bin. What would you write down?",
    },
    {
        "key": "p06", "num": 6, "title": "The Seven Steps",
        "points": [("Plan, structure, function", "Plan the scope"),
                   ("Failure analysis", "analyze the failures"),
                   ("Risk analysis", "rate the risk"),
                   ("Optimize and document", "take action")],
        "example": "Asha's team: one requirement and one failure chain at a time.",
        "example_cue": "Asha's team",
        "script": "The method has seven steps. Plan the scope, map the structure, and write what each "
                  "step must achieve. Then analyze the failures, and rate the risk. Finally, take action, "
                  "and document what changed. A simple rule keeps meetings sane. Asha's team worked on "
                  "one requirement and one failure chain at a time. So what does a good requirement look "
                  "like?",
    },
    {
        "key": "p07", "num": 7, "title": "Write Clear Functions",
        "points": [("An action verb plus a requirement", "a verb, plus"),
                   ("Measurable, not vague", "measurable")],
        "example": "Weak: “Fit gasket.” Strong: “Place the correct gasket fully in the groove, with no twist or damage.”",
        "example_cue": "Compare these",
        "script": "Write each function as a verb, plus a requirement you can check. Make it measurable, "
                  "not vague. Assemble correctly tells nobody anything. Compare these. Fit gasket. Or, "
                  "place the correct gasket fully in the groove, with no twist or damage. The second one "
                  "tells you exactly how it can fail. Missing, wrong size, not seated, or twisted. Can you "
                  "rewrite one of your own steps that way?",
    },
    {
        "key": "p08", "num": 8, "title": "The Failure Chain",
        "points": [("Effect: water ingress, field failure", "The effect is"),
                   ("Mode: gasket missing or twisted", "The failure mode is"),
                   ("Cause: something you can control", "The cause must")],
        "example": "Cause: two gasket sizes in one bin, and no check that it's seated.",
        "example_cue": "Asha's causes were",
        "script": "Now link the chain. The effect is water ingress, and a radio failing on a pole. The "
                  "failure mode is a gasket that's missing, or twisted. The cause must be something you "
                  "can actually control. Never write carelessness or human error. Asha's causes were "
                  "specific. Two gasket sizes shared one bin. And nothing checked that the gasket was "
                  "seated. Now you can design a fix. But which risk comes first?",
    },
    {
        "key": "p09", "num": 9, "title": "Severity, Occurrence, Detection",
        "points": [("Severity: how bad the effect is", "Severity rates"),
                   ("Occurrence: how often the cause happens", "Occurrence rates"),
                   ("Detection: how likely we catch it", "Detection rates"),
                   ("Every score needs evidence", "Back every score")],
        "example": "Gasket risk: Severity 8, Occurrence 5, Detection 6.",
        "example_cue": "Asha's team scored",
        "script": "You rate three things, usually from one to ten. Severity rates how bad the effect is. "
                  "Occurrence rates how often the cause happens, with today's prevention. Detection rates "
                  "how likely you are to catch it before it escapes. Here, ten means you probably won't. "
                  "Back every score with data, not feelings. Asha's team scored the gasket eight, five "
                  "and six. What does that add up to?",
    },
    {
        "key": "p10", "num": 10, "title": "Risk Priority Number",
        "points": [("RPN = Severity × Occurrence × Detection", "The Risk Priority Number"),
                   ("8 × 5 × 6 = 240", "That's two hundred"),
                   ("A guide, not a verdict", "But treat it")],
        "example": "Gasket RPN: 240, the highest on Asha's sheet.",
        "example_cue": "It was the highest",
        "script": "The Risk Priority Number multiplies the three scores together. For the gasket, eight "
                  "times five times six. That's two hundred and forty. It was the highest number on "
                  "Asha's sheet. But treat it as a guide, not a verdict. Different scores can give the "
                  "same RPN. And teams can be tempted to nudge scores to pass a limit. So what should "
                  "you look at as well?",
    },
    {
        "key": "p11", "num": 11, "title": "Severity Comes First",
        "points": [("High severity needs action anyway", "a high severity"),
                   ("High, medium, low action priority", "Many teams now use"),
                   ("Ask: is prevention or detection weak?", "And always ask")],
        "example": "A safety risk with RPN 90 can matter more than a cosmetic one at 200.",
        "example_cue": "A safety risk",
        "script": "Look at severity first. A high severity needs action, even when its RPN looks "
                  "moderate. Many teams now use action priority, rated high, medium or low. High means "
                  "act, or formally explain why you can't. And always ask which control is weak, "
                  "prevention or detection. A safety risk scoring ninety can matter more than a cosmetic "
                  "one scoring two hundred. Do you agree?",
    },
    {
        "key": "p12", "num": 12, "title": "Prevention vs Detection",
        "points": [("Prevention: stop the cause happening", "Prevention controls"),
                   ("Detection: catch it before release", "Detection controls"),
                   ("Automatic beats human judgement", "automatic beats")],
        "example": "Asha's only control: a final visual check. Detection, and a weak one.",
        "example_cue": "Asha's only control",
        "script": "Know which kind of control you have. Prevention controls stop the cause happening, "
                  "like a keyed part or a recipe lock. Detection controls catch the failure before "
                  "release, like a sensor or a test. Ask whether each one checks every unit, and whether "
                  "it can be bypassed. And automatic beats human judgement, almost every time. Asha's "
                  "only control was a final visual check. Detection, and a weak one. What would you add?",
    },
    {
        "key": "p13", "num": 13, "title": "Choose Strong Actions",
        "points": [("Eliminate the cause", "First, eliminate"),
                   ("Prevent it: lock, key, interlock", "Next, prevent"),
                   ("Improve detection", "Then improve detection"),
                   ("Training and checklists last", "Training and checklists")],
        "example": "Asha's actions: one gasket per keyed tray, a groove fixture, a presence sensor and a leak test.",
        "example_cue": "Asha chose",
        "script": "Some actions are stronger than others. First, eliminate the cause by design, if you "
                  "can. Next, prevent it, with a lock, a key or an interlock. Then reduce variation. Then "
                  "improve detection with an automatic check. Training and checklists come last, when "
                  "nothing stronger is possible. Asha chose a keyed tray with one gasket size, a groove "
                  "fixture, a presence sensor, and a leak test. Did it work?",
    },
    {
        "key": "p14", "num": 14, "title": "Verify, Then Rescore",
        "points": [("Prove it under real conditions", "Prove it works"),
                   ("Severity stays 8: same effect", "Severity stayed"),
                   ("Occurrence 5 → 2, Detection 6 → 2", "Occurrence fell"),
                   ("RPN 240 → 32", "The RPN fell")],
        "example": "Proof first: the sensor caught every bad sample in a 500-unit trial.",
        "example_cue": "Asha's proof",
        "script": "Never rescore just because you bought a sensor. Prove it works under real conditions "
                  "first. Asha's proof came from a five-hundred-unit trial. The sensor caught every bad "
                  "sample. Severity stayed at eight, because water inside is still just as bad. "
                  "Occurrence fell to two, and detection fell to two. The RPN fell from two hundred and "
                  "forty to thirty-two. Is the job finished now?",
    },
    {
        "key": "p15", "num": 15, "title": "Keep It Alive",
        "points": [("Update control plan, SOP, training", "Update the control plan"),
                   ("Review high risks every week", "Review open high risks"),
                   ("Copy lessons to similar products", "Copy what you learned")],
        "example": "Asha's team copied the keyed tray to two other outdoor units.",
        "example_cue": "Asha's team copied",
        "script": "Not quite. An FMEA is a living document, not a form to file. Update the control plan, "
                  "the SOP, the training and the audits. Review open high risks every week, and the whole "
                  "sheet after any complaint. Copy what you learned to similar products. Asha's team "
                  "copied the keyed tray to two other outdoor units. And no wet radio has come back "
                  "since. Where will you start yours?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "How could it fail?", "icon": "search", "with": 0},
        {"label": "What's the effect?", "icon": "warning", "with": 1},
        {"label": "Act first", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Failure mode", "sub": "How it fails", "icon": "cross", "with": 0},
        {"label": "Effect", "sub": "What it causes", "icon": "warning", "with": 1},
        {"label": "Cause", "sub": "Why it happens", "icon": "search", "with": 2},
        {"label": "Control, action", "sub": "What stops it", "icon": "shield", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "System", "icon": "stack", "with": 0},
        {"label": "Design", "icon": "shape", "with": 0},
        {"label": "Process", "icon": "sequence", "tone": "good", "with": 1},
        {"label": "Boundaries", "icon": "pin", "with": 2}]},
    "p04": {"type": "icons", "items": [
        {"label": "New product or process", "icon": "box", "with": 0},
        {"label": "Any change", "icon": "gear", "with": 1},
        {"label": "Complaint or escape", "icon": "warning", "tone": "bad", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Cross-functional", "icon": "person", "with": 0},
        {"label": "Operators", "icon": "hand", "with": 1},
        {"label": "Data and flow", "icon": "clipboard", "with": 2},
        {"label": "Gemba first", "icon": "walk", "tone": "good", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Plan", "with": 0}, {"label": "Structure", "with": 0},
        {"label": "Function", "with": 0}, {"label": "Failure", "with": 1},
        {"label": "Risk", "with": 2}, {"label": "Optimize", "with": 3},
        {"label": "Document", "with": 3}]},
    "p07": {"type": "versus", "items": [
        {"label": "“Fit gasket”", "sub": "Vague", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "“Correct gasket, fully seated, no twist”", "sub": "Measurable", "icon": "check", "tone": "good", "with": "example"}]},
    "p08": {"type": "flow", "items": [
        {"label": "Effect", "sub": "Water ingress", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Failure mode", "sub": "Missing or twisted", "icon": "cross", "tone": "bad", "with": 1},
        {"label": "Cause", "sub": "Mixed bin, no seating check", "icon": "search", "with": "example"}]},
    "p09": {"type": "bars", "label": "", "note": "Severity · Occurrence · Detection, 1 to 10", "with": "example", "items": [
        {"label": "Sev.", "value": 8, "tone": "bad", "with": "example"},
        {"label": "Occ.", "value": 5, "with": "example"},
        {"label": "Det.", "value": 6, "with": "example"}]},
    "p10": {"type": "stat", "value": 240, "icon": "warning", "label": "RPN for the gasket",
            "unit": "8 × 5 × 6", "with": 1},
    "p11": {"type": "ladder", "top": "HIGH", "bottom": "LOW", "items": [
        {"label": "Act, or justify why not", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Review and improve", "icon": "search", "with": 1},
        {"label": "Maintain and monitor", "icon": "check", "tone": "good", "with": 1}]},
    "p12": {"type": "versus", "items": [
        {"label": "Detection", "sub": "Final visual check", "icon": "search", "with": 1},
        {"label": "Prevention", "sub": "Stop the cause", "icon": "key", "tone": "good", "with": 0}]},
    "p13": {"type": "ladder", "top": "STRONGEST", "bottom": "WEAKEST", "items": [
        {"label": "Eliminate by design", "icon": "shape", "with": 0},
        {"label": "Prevent: key, lock", "icon": "key", "with": 1},
        {"label": "Detect automatically", "icon": "sensor", "with": 2},
        {"label": "Train, checklist", "icon": "clipboard", "with": 3}]},
    "p14": {"type": "compare", "before": {"label": "Before", "value": 240}, "after": {"label": "After", "value": 32},
            "unit": "RPN for the gasket", "note": "Occurrence 5 → 2 · Detection 6 → 2", "with": 3},
    "p15": {"type": "flow", "items": [
        {"label": "Control plan, SOP", "icon": "clipboard", "with": 0},
        {"label": "Weekly risk review", "icon": "calendar", "with": 1},
        {"label": "Copy to similar units", "icon": "sequence", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which is a useful FMEA cause?",
        "options": ["Operator carelessness",
                    "Two gasket sizes share one bin at the station",
                    "Water gets inside the radio"],
        "correct": 1,
        "explanation": "A useful cause is a specific condition you can control. Carelessness is blame, and water inside is the effect.",
        "q_script": "Quick check. Which of these is a useful cause, for an FMEA? Take a few seconds.",
        "a_script": "It's the second one. It's a specific condition you can control. Carelessness is "
                    "just blame, and water inside is the effect.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "After adding a sensor and a leak test, the team wants to cut Severity from 8 to 4. Is that right?",
        "options": ["Yes: the risk is lower now",
                    "No: Severity changes only if the effect changes",
                    "Yes, if the RPN stays under 100"],
        "correct": 1,
        "explanation": "Severity rates the effect. Water inside a radio is just as bad as before. The new controls lower Occurrence and Detection, not Severity.",
        "q_script": "One more, and this one's a scenario. After adding a sensor and a leak test, the "
                    "team wants to cut severity from eight to four. Is that right? Have a think.",
        "a_script": "No. Severity rates the effect, and water inside is just as bad as before. The new "
                    "controls lower occurrence and detection instead.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
