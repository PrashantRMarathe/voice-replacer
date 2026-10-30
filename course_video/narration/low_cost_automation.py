"""Low Cost Automation lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Gaurav,
a process engineer on a Bluetooth speaker line, replacing mallet-seated
grilles with a simple, safe pneumatic press, after simplifying the job first.
L's outro points to M (Muda, Mura, Muri), the start of the second half.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/low_cost_automation.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py low_cost_automation  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "lc"
NAME = "low_cost_automation"

LETTERS = ["LCA", "ECRS", "PLC", "SOP", "UPH"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    return re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)


INTRO_SCRIPT = (
    "Every speaker grille on Gaurav's line was seated with a rubber mallet. Four hundred taps "
    "an hour, per operator. Sore wrists, and loose grilles rattling at test. Sound familiar? "
    "In this lesson, you'll learn Low Cost Automation. You'll see how simple, safe devices "
    "can remove repetitive work and errors, without buying a full robot line. We'll follow "
    "Gaurav, a process engineer on a Bluetooth speaker line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Simplify first, and never automate waste. Choose the "
    "simplest safe solution that does the job, with safety as the first gate. And prove the "
    "real benefit, then maintain it like any other machine. Here's your action for this week. "
    "Find one repetitive motion on your line, and ask whether it can be eliminated before it's "
    "automated. Great work completing this lesson. Next, you'll learn Muda, Mura and Muri."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Low Cost Automation Is",
        "points": [("Simple, reliable, economical devices", "simple, reliable"),
                   ("Remove repetitive work and errors", "to remove repetitive"),
                   ("No full automation needed", "without jumping")],
        "example": "Gaurav's target: grille seating, done by hand with a rubber mallet.",
        "example_cue": "Gaurav's target",
        "script": "Low Cost Automation, or LCA, means using simple, reliable and economical devices. "
                  "You use them to remove repetitive work, prevent errors and improve safety. And you do "
                  "it without jumping straight to a fully automated line. Think clamps, guides, sensors "
                  "and small air cylinders. Gaurav's target was grille seating, still done by hand with "
                  "a rubber mallet. What ideas guide LCA?",
    },
    {
        "key": "p02", "num": 2, "title": "The Core Philosophy",
        "points": [("Automate the need, not the complexity", "Automate the need"),
                   ("Simplify before automating", "Simplify before"),
                   ("Keep people in the loop", "Keep people"),
                   ("Measure it, maintain it", "And measure")],
        "example": "A fancy robot was quoted at ₹18 lakh. Gaurav asked: what does the job really need?",
        "example_cue": "A robot was quoted",
        "script": "A few ideas guide every good LCA. Automate the need, not the complexity. Start from "
                  "the problem, and the function you require. Simplify before you automate anything. "
                  "Keep people in the loop, so abnormalities stay visible. And measure the benefit, then "
                  "maintain it. A robot was quoted at eighteen lakh rupees. Gaurav asked one question. "
                  "What does this job really need?",
    },
    {
        "key": "p03", "num": 3, "title": "When LCA Makes Sense",
        "points": [("Frequent, repetitive motions", "repeated every cycle"),
                   ("Ergonomic or safety risk", "hurts people"),
                   ("Steps missed or done the wrong way", "steps get missed"),
                   ("Bottleneck, but no case for a robot", "a bottleneck")],
        "example": "Grille seating: every cycle, wrist strain, and uneven seating. All four boxes ticked.",
        "example_cue": "Grille seating ticked",
        "script": "LCA makes sense when a motion is repeated every cycle, many times a shift. When the "
                  "work hurts people, or creates a safety risk. When steps get missed, reversed or "
                  "misplaced. And when there's a bottleneck, but full automation isn't worth the money. "
                  "It also suits products with uncertain volume. Grille seating ticked every box. But "
                  "what must low cost never mean?",
    },
    {
        "key": "p04", "num": 4, "title": "Low Cost, Never Low Safety",
        "points": [("Safety is the first design gate", "Safety is the first"),
                   ("Guards, stops, risk assessment", "Guards, emergency stops"),
                   ("A normal sensor isn't a safety device", "an ordinary sensor")],
        "example": "Gaurav's rule: no device runs until the safety team signs the risk assessment.",
        "example_cue": "Gaurav's rule",
        "script": "Low cost must never mean low safety, or poor engineering. Safety is the first design "
                  "gate, before cost or speed. Guards, emergency stops, risk assessment and electrical "
                  "standards all still apply. And remember, an ordinary sensor or controller isn't "
                  "automatically a safety device. Gaurav's rule was simple. No device runs until the "
                  "safety team signs the risk assessment. What kinds of LCA exist?",
    },
    {
        "key": "p05", "num": 5, "title": "Levels of LCA",
        "points": [("Mechanical: gravity, springs, guides", "Mechanical assists"),
                   ("Pneumatic: clamps, presses, grippers", "Pneumatic assists"),
                   ("Sensors and simple controls", "Sensors detect"),
                   ("Pick the lowest level that works", "Pick the lowest")],
        "example": "Manual → assisted → semi-automatic → automatic.",
        "example_cue": "Think of a ladder",
        "script": "There are several levels. Mechanical assists use gravity, springs, levers and guides, "
                  "with no power at all. Pneumatic assists use small air cylinders to clamp or press. "
                  "Sensors detect presence, position or sequence, and simple controls run the steps. Think "
                  "of a ladder, from manual to fully automatic. Pick the lowest level that safely meets "
                  "your need. Where do you begin?",
    },
    {
        "key": "p06", "num": 6, "title": "The LCA Method",
        "points": [("Observe and measure", "Observe the real job"),
                   ("Simplify, then define the function", "simplify it"),
                   ("Concept, risk review, prototype", "sketch a concept"),
                   ("Validate, standardize, replicate", "validate it")],
        "example": "Gaurav's baseline: 28 s cycle, 18 loose grilles per 1,000 speakers.",
        "example_cue": "Gaurav's baseline",
        "script": "Follow a clear method. Observe the real job, and measure the time, motion, defects and "
                  "risk. Then simplify it, and define exactly what function the device must perform. "
                  "Next, sketch a concept, review its risks, and build a prototype. Finally, validate it, "
                  "standardize it, and copy it where it fits. Gaurav's baseline was a twenty-eight second "
                  "cycle, and eighteen loose grilles per thousand. What comes first?",
    },
    {
        "key": "p07", "num": 7, "title": "ECRS Before Automation",
        "points": [("Eliminate, combine, rearrange, simplify", "Eliminate, combine"),
                   ("Only then automate", "Only then"),
                   ("Automated waste is still waste", "Automated waste")],
        "example": "Gaurav eliminated a separate tap-test step: the new press would confirm seating itself.",
        "example_cue": "Gaurav found",
        "script": "Simplify first, with ECRS. Eliminate, combine, rearrange and simplify. Only then "
                  "automate what's left. Why? Because automated waste is still waste. It's just faster, "
                  "more expensive, and harder to change later. Gaurav found one step to eliminate before "
                  "anything else. Operators tapped every grille again, just to check it. A well-designed "
                  "press could confirm seating by itself. What did he see at the gemba?",
    },
    {
        "key": "p08", "num": 8, "title": "Gaurav's Opportunity",
        "points": [("Repeated motion every cycle", "the same motion"),
                   ("Uneven force, uneven seating", "uneven force"),
                   ("Wrist strain, every shift", "wrist strain")],
        "example": "Loose grilles: 18 per 1,000 speakers, all found at the rattle test.",
        "example_cue": "Loose grilles",
        "script": "At the gemba, he saw the same motion, every cycle. Pick up the mallet, tap around the "
                  "grille, check it, put the mallet down. Each operator used uneven force, so seating "
                  "varied. Some grilles sat loose, and rattled at test. And operators reported wrist "
                  "strain by mid-shift. Loose grilles ran at eighteen per thousand speakers. Which "
                  "technology would you choose?",
    },
    {
        "key": "p09", "num": 9, "title": "Choose Simple Technology",
        "points": [("Match technology to the function", "Choose by function"),
                   ("Fewest parts, standard parts", "Use the fewest parts"),
                   ("Easy to clean, adjust and fix", "Make it easy")],
        "example": "Gaurav's choice: a small air cylinder, a locating nest and one presence sensor.",
        "example_cue": "Gaurav chose",
        "script": "Choose by function, not because something looks advanced. Think about accuracy, cycle "
                  "time, the environment, and who will maintain it. Use the fewest parts, and standard "
                  "parts where you can. Make it easy to clean, adjust and repair. And make its status "
                  "obvious at a glance. Gaurav chose a small air cylinder, a locating nest and one "
                  "presence sensor. How do you make that safe?",
    },
    {
        "key": "p10", "num": 10, "title": "Design It Safe",
        "points": [("Find pinch points and stored energy", "Look for pinch points"),
                   ("Guards and two-hand start", "Add guards"),
                   ("Safe stop, safe restart", "After a stop")],
        "example": "A two-hand start keeps both hands out of the press zone. Air pressure releases on stop.",
        "example_cue": "Gaurav's press",
        "script": "Look for pinch points, crushing, moving parts, and stored air pressure. Add guards, and "
                  "a start method that keeps hands away from danger. After a stop or air loss, the device "
                  "must return to a safe state, not restart by itself. Gaurav's press uses a two-hand "
                  "start, so both hands stay clear. Air pressure releases on any stop. Would your current "
                  "fixtures pass that test?",
    },
    {
        "key": "p11", "num": 11, "title": "Gaurav's Press",
        "points": [("Nest locates the speaker", "A nest locates"),
                   ("Sensor confirms the grille is present", "A sensor confirms"),
                   ("Controlled force, OK or not-OK lamp", "controlled force")],
        "example": "No grille, no press. Wrong position, no press. Seated: green lamp.",
        "example_cue": "No grille",
        "script": "Here's what he built. A nest locates the speaker the same way every time. A sensor "
                  "confirms the grille is present and positioned. Then the cylinder presses with "
                  "controlled force, and a lamp shows okay or not okay. No grille, no press. Wrong position, "
                  "no press. Seated correctly, green light. The operator loads and unloads, and the "
                  "press does the rest. How much faster was it?",
    },
    {
        "key": "p12", "num": 12, "title": "Count the Real Gain",
        "points": [("Cycle time: 28 s down to 22 s", "Cycle time fell"),
                   ("Theoretical output: about 35 more an hour", "about thirty-five"),
                   ("Include stops and recovery", "Include loading")],
        "example": "Real-world check: two short jams a shift, one minute each. The gain held.",
        "example_cue": "Gaurav measured",
        "script": "Cycle time fell from twenty-eight seconds to twenty-two. In theory, that's about "
                  "thirty-five more speakers an hour. But don't trust theory alone. A fast station that keeps stopping can slow the whole line. Include loading, "
                  "unloading, minor stops, jams and fault recovery. Gaurav measured real production for "
                  "two weeks. There were two short jams a shift, about a minute each. The gain held. "
                  "But was it worth the money?",
    },
    {
        "key": "p13", "num": 13, "title": "Cost and Payback",
        "points": [("Total cost of ownership", "Count the total cost"),
                   ("Net benefit, validated", "Count only benefits"),
                   ("Payback = investment ÷ monthly benefit", "Payback is")],
        "example": "₹1.2 lakh invested ÷ ₹30,000 net benefit a month = 4-month payback.",
        "example_cue": "Gaurav's press cost",
        "script": "Count the total cost of ownership. That's design, parts, installation, training, air, "
                  "spares and maintenance. Count only benefits you can validate, like less rework and "
                  "freed labour time. Payback is the investment, divided by the monthly net benefit. "
                  "Gaurav's press cost one point two lakh rupees. It saved thirty thousand a month. That's "
                  "a four month payback. How do you keep it running?",
    },
    {
        "key": "p14", "num": 14, "title": "Validate and Maintain",
        "points": [("Trial all models and shifts", "Trial it"),
                   ("Preventive maintenance and spares", "Give it a maintenance plan"),
                   ("Clear fault codes and recovery", "Write clear fault")],
        "example": "Loose grilles: 18 → 2 per 1,000. Wrist complaints: none in 60 days.",
        "example_cue": "Loose grilles fell",
        "script": "Trial it across models and shifts, before you call it done. Check safety, quality, "
                  "speed, reliability and how easily operators recover from a fault. Give it a maintenance "
                  "plan, critical spares, and sensor checks. Write clear fault codes, so technicians fix "
                  "it fast. Loose grilles fell from eighteen to two per thousand. And no wrist complaints "
                  "in sixty days. What mistakes should you avoid?",
    },
    {
        "key": "p15", "num": 15, "title": "Mistakes and Your Next Step",
        "points": [("Automating a process you don't understand", "Automating a process"),
                   ("Choosing technology first", "Choosing the technology"),
                   ("Forgetting maintenance and spares", "Forgetting")],
        "example": "Gaurav's press now runs on three lines, copied after checking each one fits.",
        "example_cue": "Gaurav's press now",
        "script": "Watch for common mistakes. Automating a process you don't understand. Choosing the "
                  "technology before defining the problem. Forgetting maintenance, spares and fault "
                  "recovery. Claiming theoretical savings you never validated. And ignoring what "
                  "operators tell you. And not updating the standards afterwards. Gaurav's press now runs on three lines, copied only after checking "
                  "each one fits. Which repetitive job will you look at first?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Simple devices", "icon": "gear", "with": 0},
        {"label": "Less repetition, fewer errors", "icon": "check", "with": 1},
        {"label": "No full robot line", "icon": "scale", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 400, "icon": "hand", "label": "mallet taps an hour",
                 "unit": "per operator", "with": "example"}},
    "p02": {"type": "icons", "items": [
        {"label": "Need, not complexity", "icon": "key", "with": 0},
        {"label": "Simplify first", "icon": "shape", "with": 1},
        {"label": "People in the loop", "icon": "person", "with": 2},
        {"label": "Measure, maintain", "icon": "wrench", "tone": "good", "with": 3}]},
    "p03": {"type": "icons", "items": [
        {"label": "Repetitive", "icon": "sequence", "with": 0},
        {"label": "Ergonomic risk", "icon": "warning", "with": 1},
        {"label": "Missed steps", "icon": "cross", "with": 2},
        {"label": "Bottleneck", "icon": "clock", "with": 3}]},
    "p04": {"type": "flow", "items": [
        {"label": "Safety gate first", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Guards, e-stops, risk review", "icon": "lock", "with": 1},
        {"label": "Signed before it runs", "icon": "clipboard", "with": "example"}]},
    "p05": {"type": "ladder", "top": "AUTOMATIC", "bottom": "MANUAL", "items": [
        {"label": "Sensors and simple controls", "icon": "sensor", "with": 2},
        {"label": "Pneumatic assist", "icon": "gear", "with": 1},
        {"label": "Mechanical assist", "icon": "shape", "with": 0},
        {"label": "Manual", "icon": "hand", "with": 3}]},
    "p06": {"type": "steps", "items": [
        {"label": "Observe, measure", "with": 0}, {"label": "Simplify, define", "with": 1},
        {"label": "Concept, risk, prototype", "with": 2}, {"label": "Validate, standardize, copy", "with": 3}]},
    "p07": {"type": "steps", "items": [
        {"label": "Eliminate", "with": 0}, {"label": "Combine", "with": 0},
        {"label": "Rearrange", "with": 0}, {"label": "Simplify", "with": 0},
        {"label": "Then automate", "with": 1}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Re-tap every grille", "sub": "Eliminated", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Press confirms seating", "sub": "Built in", "icon": "check", "tone": "good", "with": "example"}]}},
    "p08": {"type": "flow", "items": [
        {"label": "Same motion every cycle", "icon": "hand", "tone": "bad", "with": 0},
        {"label": "Uneven force", "icon": "scale", "tone": "bad", "with": 1},
        {"label": "Wrist strain", "icon": "warning", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 18, "icon": "wave", "label": "loose grilles per 1,000",
                 "unit": "found at the rattle test", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "Air cylinder", "icon": "gear", "with": "example"},
        {"label": "Locating nest", "icon": "shape", "with": "example"},
        {"label": "Presence sensor", "icon": "sensor", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Pinch points", "icon": "warning", "tone": "bad", "with": 0},
        {"label": "Two-hand start", "icon": "hand", "with": 1},
        {"label": "Air released on stop", "icon": "lock", "tone": "good", "with": 2}]},
    "p11": {"type": "flow", "items": [
        {"label": "Nest locates", "icon": "shape", "with": 0},
        {"label": "Sensor confirms", "icon": "sensor", "with": 1},
        {"label": "Controlled press", "icon": "gear", "with": 2},
        {"label": "Green: seated", "icon": "check", "tone": "good", "with": "example"}]},
    "p12": {"type": "compare", "before": {"label": "Mallet", "value": 28}, "after": {"label": "Press", "value": 22},
            "suffix": " s", "unit": "cycle time per speaker", "note": "About 35 more an hour, in theory", "with": 0},
    "p13": {"type": "bars", "label": "", "note": "Savings so far, ₹ thousand: paid back in month 4", "with": "example", "items": [
        {"label": "Month 1", "value": 30, "with": "example"},
        {"label": "Month 2", "value": 60, "with": "example"},
        {"label": "Month 3", "value": 90, "with": "example"},
        {"label": "Month 4", "value": 120, "tone": "good", "with": "example"}]},
    "p14": {"type": "compare", "before": {"label": "Mallet", "value": 18}, "after": {"label": "Press", "value": 2},
            "unit": "loose grilles per 1,000 speakers", "note": "No wrist complaints in 60 days", "with": "example"},
    "p15": {"type": "icons", "items": [
        {"label": "Automating the unknown", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Technology first", "icon": "gear", "tone": "bad", "with": 1},
        {"label": "No spares, no PM", "icon": "wrench", "tone": "bad", "with": 2},
        {"label": "Copied to 3 lines", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Before adding any automation to a manual step, what should you do first?",
        "options": ["Buy the fastest machine available",
                    "Simplify it with ECRS, and eliminate waste",
                    "Ask operators to work faster"],
        "correct": 1,
        "explanation": "Simplify first: eliminate, combine, rearrange and simplify. Automated waste is still waste, just faster and harder to change.",
        "q_script": "Quick check. Before you automate a manual step, what should you do first? Take a "
                    "few seconds.",
        "a_script": "Simplify it with ECRS, and eliminate the waste. Automated waste is still waste, "
                    "just faster and harder to change.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A new LCA station saves 6 seconds on paper, but jams ten times a shift. What should the team do?",
        "options": ["Roll it out: the cycle time is better",
                    "Measure real output with the stops, and fix reliability first",
                    "Remove the sensor so it jams less"],
        "correct": 1,
        "explanation": "Theoretical cycle time isn't real capacity. Include jams and recovery, fix reliability, and only then roll it out. Removing a sensor would weaken quality control.",
        "q_script": "One more, and this one's a scenario. A new station saves six seconds on paper. But "
                    "it jams ten times a shift. What should the team do? Have a think.",
        "a_script": "Measure the real output, including the stops, and fix reliability first. Theory "
                    "isn't capacity, and removing the sensor would only weaken quality.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
