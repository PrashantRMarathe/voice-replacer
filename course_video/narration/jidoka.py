"""Jidoka lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Anjali,
a process engineer on a patient monitor line, turning an automatic adhesive
dispenser that kept running with a half-blocked nozzle into a Jidoka station
that detects, stops, calls and contains.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/jidoka.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py jidoka  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "jd"
NAME = "jidoka"

LETTERS = ["FPY", "SOP", "PFMEA"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. Jidoka, Andon as spelled (voiced since
# Zero Defects); Sakichi = "Sah-kee-chee".
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return re.sub(r"\bSakichi\b", "Sah-kee-chee", text)


INTRO_SCRIPT = (
    "The dispenser ran perfectly all night. Except its nozzle was half blocked. By morning, "
    "a hundred and forty patient monitors had a thin seal. Sound familiar? In this lesson, "
    "you'll learn Jidoka, automation with a human touch. You'll see how to make a process "
    "spot a problem, stop itself, and call for help, before defects pile up. We'll follow "
    "Anjali, a process engineer on a patient monitor line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Define normal first, so the process knows what abnormal "
    "looks like. Detect, stop and contain at the source, and never pass a defect on. And "
    "treat every stop as a lesson, fixing the root cause so it doesn't repeat. Here's your "
    "action for this week. Pick one automatic process, and write down what should make it "
    "stop. Great work completing this lesson. Next, you'll learn Kaizen."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Jidoka Is",
        "points": [("Detect an abnormality", "detects an abnormal"),
                   ("Stop or contain", "stops or contains"),
                   ("Correct, then prevent", "Then people correct")],
        "example": "Anjali's dispenser seals the front bezel of every patient monitor.",
        "example_cue": "Anjali's challenge",
        "script": "Jidoka is often called automation with a human touch. It means a process that "
                  "detects an abnormal condition by itself. It stops or contains the work, so no "
                  "defect moves on. Then people correct it, and prevent it from happening again. "
                  "Anjali's challenge was an adhesive dispenser. It seals the front bezel of every "
                  "patient monitor. So what changes when you add Jidoka?",
    },
    {
        "key": "p02", "num": 2, "title": "Without and With Jidoka",
        "points": [("Defects travel vs caught at source", "Without Jidoka, a defect"),
                   ("Hesitation vs clear stop rules", "people hesitate"),
                   ("Inspection vs built-in quality", "quality depends")],
        "example": "Without it: 140 thin seals, found at leak test the next morning.",
        "example_cue": "Without it",
        "script": "Without Jidoka, a defect can travel through many stations before anyone sees it. "
                  "People hesitate to stop, because nobody said they could. Sorting becomes routine, "
                  "and quality depends on final inspection. With Jidoka, it's caught near the source. "
                  "The stop rules are clear, and quality is built into the process. Without it, Anjali "
                  "found a hundred and forty thin seals the next morning. Where did this idea begin?",
    },
    {
        "key": "p03", "num": 3, "title": "Where It Came From",
        "points": [("Sakichi Toyoda's automatic loom", "It goes back to"),
                   ("It stopped when a thread broke", "stopped itself"),
                   ("One of the two pillars of TPS", "two pillars")],
        "example": "Just-in-Time moves material well. Jidoka makes sure it doesn't move defects well.",
        "example_cue": "Here's the link",
        "script": "It goes back to Sakichi Toyoda's automatic loom. The clever part wasn't the speed. "
                  "The loom stopped itself whenever a thread broke, instead of weaving bad cloth. That "
                  "idea became one of the two pillars of the Toyota Production System. Here's the link. "
                  "Just-in-time moves material efficiently. Jidoka makes sure you don't move defects "
                  "efficiently. Does that mean fewer people?",
    },
    {
        "key": "p04", "num": 4, "title": "People Still Matter",
        "points": [("Machines watch, people think", "Machines do the watching"),
                   ("One person can run several machines", "one person can"),
                   ("Judgment, repair, improvement", "on judgment")],
        "example": "Anjali's operator used to stare at the bead all shift. Now she runs two stations.",
        "example_cue": "Anjali's operator",
        "script": "No. Jidoka doesn't remove people. Machines do the watching, and people do the "
                  "thinking. Because the machine signals when it needs help, one person can look after "
                  "several machines. Their time goes on judgment, repair, standards and improvement. "
                  "Anjali's operator used to stare at the adhesive bead all shift. Now she runs two "
                  "stations, and solves problems. How does the cycle work?",
    },
    {
        "key": "p05", "num": 5, "title": "Step 1: Detect",
        "points": [("Define normal first", "define normal"),
                   ("Then sense the deviation", "sense when"),
                   ("Sensors, checks, tests, monitors", "Sensors, vision")],
        "example": "Normal bead: 2.0 to 2.4 mm wide, no gaps.",
        "example_cue": "For Anjali",
        "script": "The cycle has four steps. Detect, stop, correct and prevent. Detection needs one "
                  "thing first. You must define normal. You can't sense abnormal until you know what "
                  "good looks like. Then you sense when the process drifts from it. Sensors, vision, "
                  "tests, torque monitors and operator checks can all do it. For Anjali, normal was a "
                  "bead two to two point four millimetres wide, with no gaps. What comes next?",
    },
    {
        "key": "p06", "num": 6, "title": "Steps 2 to 4: Stop, Correct, Prevent",
        "points": [("Stop or contain to match the risk", "Stop or contain"),
                   ("Correct: restore the standard", "Correct means"),
                   ("Prevent: remove the root cause", "Prevent means")],
        "example": "Correcting isn't the same as preventing. A cleaned nozzle can block again.",
        "example_cue": "Remember this",
        "script": "Stop or contain, in a way that matches the risk. That might be a machine stop, a "
                  "station lock, a held unit, or a blocked transaction. Correct means restoring the "
                  "approved standard, and finding the affected product. Prevent means removing the root "
                  "cause, and updating the standard. Remember this. Correcting isn't preventing. A "
                  "cleaned nozzle can block again tomorrow. So how is this different from automation?",
    },
    {
        "key": "p07", "num": 7, "title": "Jidoka vs Plain Automation",
        "points": [("Automation does the work", "Plain automation"),
                   ("Jidoka also judges the work", "Jidoka adds"),
                   ("Fast machines make fast defects", "a fast machine")],
        "example": "Anjali's dispenser: fully automatic, but blind. It kept dispensing all night.",
        "example_cue": "Anjali's dispenser",
        "script": "Plain automation does the work. Jidoka adds judgment about the work. A normal machine "
                  "keeps running, unless something physically jams. A Jidoka machine stops when it sees "
                  "a defined abnormality, and calls a person. And here's the danger. A fast machine "
                  "makes defects fast. Anjali's dispenser was fully automatic, but blind. It dispensed "
                  "thin beads all night. What principles should guide you?",
    },
    {
        "key": "p08", "num": 8, "title": "Core Principles",
        "points": [("No defect forward", "No defect forward"),
                   ("No abnormality hidden", "No abnormality hidden"),
                   ("No repeat accepted without action", "No repeat problem")],
        "example": "Three questions: what's normal? How do we detect a deviation? What happens next?",
        "example_cue": "Ask three questions",
        "script": "Remember three short rules. No defect forward. No abnormality hidden. No repeat "
                  "problem accepted without action. Use machine detection and human judgment together. "
                  "And never just restart without learning something. Every stop should leave the process a little stronger. Ask three questions about any "
                  "process. What's normal? How will we detect a deviation? And exactly what happens "
                  "after detection? Can you answer them for your line?",
    },
    {
        "key": "p09", "num": 9, "title": "Andon",
        "points": [("Green: normal", "Green means"),
                   ("Yellow: help needed", "Yellow means"),
                   ("Red: stop, contain, escalate", "Red means")],
        "example": "Anjali's rule: the team leader answers a yellow within two minutes.",
        "example_cue": "On Anjali's line",
        "script": "Andon makes problems visible, with lights, sounds or screens. Green means normal, so "
                  "keep working to standard. Yellow means help is needed, and a leader comes quickly. "
                  "Red means a critical abnormality. Stop safely, contain, and escalate. Then find the "
                  "last known good unit. On Anjali's line, the team leader answers any yellow within two "
                  "minutes. How fast does help reach your line?",
    },
    {
        "key": "p10", "num": 10, "title": "An Andon Culture",
        "points": [("A call is useful information", "A genuine Andon call"),
                   ("Never punish a stop", "Never punish"),
                   ("Calls may rise at first", "calls often rise")],
        "example": "Andon calls doubled in month one, then halved by month three.",
        "example_cue": "On Anjali's line",
        "script": "Andon only works if people trust it. A genuine Andon call is useful information, not "
                  "a nuisance. Never punish a stop, or people will hide problems to protect output. And "
                  "expect a surprise. When problems become visible, calls often rise at first. On "
                  "Anjali's line, Andon calls doubled in the first month. By month three, they'd halved, "
                  "because causes were being fixed. Would your team call?",
    },
    {
        "key": "p11", "num": 11, "title": "Strongest Controls First",
        "points": [("Eliminate, or prevent by design", "First, eliminate"),
                   ("Detect and stop immediately", "Next, detect"),
                   ("Warnings and inspection last", "Warnings come")],
        "example": "Good poka yoke: simple, close to the source, hard to bypass, easy to challenge-test.",
        "example_cue": "A good poka yoke",
        "script": "Use the strongest control you can. First, eliminate the chance of error, or prevent "
                  "it by design. Next, detect the error and stop immediately. Warnings come after that, "
                  "and downstream inspection only as an extra defense. A good poka yoke is simple, close "
                  "to the source, and hard to bypass. And it's easy to challenge-test every shift. So "
                  "what did Anjali build?",
    },
    {
        "key": "p12", "num": 12, "title": "Anjali's Jidoka Station",
        "points": [("A sensor measures every bead", "measures every bead"),
                   ("Out of limits: dispenser stops", "the dispenser stops"),
                   ("Andon, and hold to the last good unit", "Andon calls")],
        "example": "First real stop: one monitor affected, not 140.",
        "example_cue": "Its first real stop",
        "script": "She added a vision sensor that measures every bead, right after dispensing. If the "
                  "width falls outside limits, the dispenser stops, and the unit is held. Andon calls the "
                  "team leader. Everything since the last good unit is checked. Its first real stop came "
                  "two weeks later. One monitor was affected, not a hundred and forty. But why did the "
                  "nozzle block?",
    },
    {
        "key": "p13", "num": 13, "title": "Root Cause After the Stop",
        "points": [("Stopping reveals; analysis improves", "Stopping reveals"),
                   ("Ask why, with evidence", "Why did the nozzle"),
                   ("Fix it, then standardize", "So she added")],
        "example": "Adhesive cured in the nozzle during breaks. No purge step in the standard.",
        "example_cue": "Adhesive cured",
        "script": "Stopping reveals a problem. Root cause analysis turns it into an improvement. Why did "
                  "the nozzle block? Adhesive cured inside it during breaks. Why? There was no purge step "
                  "after a pause. Why? The standard never covered breaks. So she added an automatic "
                  "purge after any pause, and a pressure monitor. The PFMEA and SOP were updated too. "
                  "How would you measure success?",
    },
    {
        "key": "p14", "num": 14, "title": "Measure the Right Things",
        "points": [("First pass yield and escapes", "Watch first pass yield"),
                   ("Andon response time", "Andon response time"),
                   ("Repeat abnormalities", "repeat abnormalities")],
        "example": "First pass yield: 97.5% → 99.0%. Escapes: zero in 90 days.",
        "example_cue": "Anjali's results",
        "script": "Measure response and recurrence, not just the number of stops. Watch first pass yield, "
                  "and escapes to the customer. Track Andon response time, from the call to help "
                  "arriving. And watch repeat abnormalities. They should fall over time. Anjali's results "
                  "were clear. First pass yield rose by one and a half points, to ninety-nine percent. "
                  "Not one seal escaped in ninety days. Who makes it all work?",
    },
    {
        "key": "p15", "num": 15, "title": "Roles and Your Roadmap",
        "points": [("Operators detect, call and stop", "Operators detect"),
                   ("Leaders respond and restore", "Leaders respond"),
                   ("A 30-60-90 day rollout", "Roll it out")],
        "example": "Days 0–30: define abnormal. 31–60: detect and train. 61–90: fix top repeats.",
        "example_cue": "In the first thirty days",
        "script": "Everyone has a role. Operators detect, call, stop and give facts. Leaders respond fast, "
                  "and restore the standard. Maintenance keeps sensors and interlocks working, and "
                  "management protects the right to stop. Roll it out in ninety days. In the first "
                  "thirty days, define abnormal and pick a pilot. Then build detection and train. "
                  "Finally, fix the top repeat causes. Where will you start?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "flow", "items": [
        {"label": "Detect", "icon": "sensor", "with": 0},
        {"label": "Stop", "icon": "lock", "with": 1},
        {"label": "Correct", "icon": "wrench", "with": 2},
        {"label": "Prevent", "icon": "shield", "tone": "good", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Without Jidoka", "sub": "Defects travel, found later", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "With Jidoka", "sub": "Caught at the source", "icon": "check", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 140, "icon": "warning", "label": "thin seals by morning",
                 "unit": "found at leak test", "with": "example"}},
    "p03": {"type": "timeline", "items": [
        {"label": "Loom stops on a broken thread", "sub": "Early 1900s", "icon": "gear", "with": 0},
        {"label": "Pillar of TPS", "sub": "TPS", "icon": "stack", "with": 2},
        {"label": "No defects moved on", "sub": "Today", "icon": "shield", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Watching one machine", "sub": "All shift", "icon": "search", "tone": "bad", "with": 0},
        {"label": "Running two stations", "sub": "And solving problems", "icon": "person", "tone": "good", "with": "example"}]},
    "p05": {"type": "icons", "items": [
        {"label": "Define normal", "icon": "clipboard", "with": 0},
        {"label": "Sense the drift", "icon": "sensor", "with": 1},
        {"label": "Tests, monitors", "icon": "test", "with": 2}],
        "then": {"type": "stat", "value": 2.0, "decimals": 1, "suffix": "–2.4 mm", "icon": "pin", "label": "normal bead width",
                 "unit": "no gaps", "with": "example"}},
    "p06": {"type": "steps", "items": [
        {"label": "Stop or contain", "with": 0},
        {"label": "Correct", "with": 1},
        {"label": "Prevent", "with": 2}]},
    "p07": {"type": "versus", "items": [
        {"label": "Plain automation", "sub": "Kept dispensing all night", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Jidoka", "sub": "Stops and calls", "icon": "sensor", "tone": "good", "with": 1}]},
    "p08": {"type": "icons", "items": [
        {"label": "No defect forward", "icon": "lock", "with": 0},
        {"label": "No abnormality hidden", "icon": "search", "with": 1},
        {"label": "No repeat without action", "icon": "key", "tone": "good", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Green: normal", "sub": "Keep to standard", "icon": "check", "tone": "good", "with": 0},
        {"label": "Yellow: help", "sub": "Leader comes fast", "icon": "person", "with": 1},
        {"label": "Red: stop", "sub": "Contain, escalate", "icon": "warning", "tone": "bad", "with": 2}]},
    "p10": {"type": "bars", "label": "", "note": "Andon calls per week", "with": 2, "items": [
        {"label": "Before", "value": 10, "with": 2},
        {"label": "Month 1", "value": 20, "with": "example"},
        {"label": "Month 3", "value": 10, "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "STRONGEST", "bottom": "WEAKEST", "items": [
        {"label": "Eliminate or prevent", "icon": "shape", "with": 0},
        {"label": "Detect and stop", "icon": "sensor", "with": 1},
        {"label": "Warn", "icon": "warning", "with": 2},
        {"label": "Inspect later", "icon": "search", "with": 2}]},
    "p12": {"type": "flow", "items": [
        {"label": "Sensor checks every bead", "icon": "sensor", "with": 0},
        {"label": "Dispenser stops", "icon": "lock", "with": 1},
        {"label": "Andon, hold to last good", "icon": "warning", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 140}, "after": {"label": "With Jidoka", "value": 1},
                 "unit": "monitors affected per nozzle problem", "with": "example"}},
    "p13": {"type": "steps", "items": [
        {"label": "Nozzle blocked", "with": 1},
        {"label": "Adhesive cured in breaks", "with": "example"},
        {"label": "No purge step", "with": "example"},
        {"label": "Auto-purge + pressure monitor", "with": 2}]},
    "p14": {"type": "compare", "before": {"label": "Before", "value": 97.5}, "after": {"label": "After", "value": 99.0},
            "decimals": 1, "suffix": "%", "unit": "first pass yield", "note": "Zero escapes in 90 days", "with": "example"},
    "p15": {"type": "timeline", "items": [
        {"label": "Define abnormal, pilot", "sub": "Days 0–30", "icon": "clipboard", "with": 2},
        {"label": "Detect, train", "sub": "31–60", "icon": "sensor", "with": 2},
        {"label": "Fix top repeats", "sub": "61–90", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "What makes Jidoka different from ordinary automation?",
        "options": ["It runs faster",
                    "It detects a defined abnormality, stops, and calls a person",
                    "It needs no people at all"],
        "correct": 1,
        "explanation": "Automation does the work; Jidoka also judges it. It stops on a defined abnormality and signals for human help, so defects don't multiply.",
        "q_script": "Quick check. What makes Jidoka different from ordinary automation? Take a few seconds.",
        "a_script": "It's the second one. It detects a defined abnormality, stops itself, and calls a "
                    "person. So defects don't multiply.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "An operator sees an abnormal seal, but the line is behind target. What should she do?",
        "options": ["Keep going and report it at the end of the shift",
                    "Call Andon and hold the unit, as the stop rules say",
                    "Fix it quietly herself and carry on"],
        "correct": 1,
        "explanation": "No defect forward, no abnormality hidden. Calling Andon and holding the unit protects the customer, even when output is behind.",
        "q_script": "One more, and this one's a scenario. An operator sees an abnormal seal, but the "
                    "line is behind target. What should she do? Have a think.",
        "a_script": "Call Andon, and hold the unit, just as the stop rules say. No defect forward, and "
                    "no abnormality hidden, even when output is behind.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
