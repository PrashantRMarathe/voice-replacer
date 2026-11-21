"""Design Thinking lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Pooja,
an improvement engineer at a medical devices plant, fixing label errors and
lost time at the infusion-pump packing station by starting with the packers.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/design_thinking.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py design_thinking  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "dt"
NAME = "design_thinking"

LETTERS = ["SCAMPER"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. SCAMPER is said as the word "scamper";
# TAKT = "tact".
def say(text: str) -> str:
    text = re.sub(r"\bSCAMPER\b", "Scamper", text)
    text = re.sub(r"\bA3\b", "A-three", text)
    return re.sub(r"\bTAKT\b", "tact", text)


INTRO_SCRIPT = (
    "The packing line kept missing its target. Wrong labels kept slipping through. The "
    "first idea was a faster printer, for a lot of money. Nobody had asked the packers. "
    "Sound familiar? In this lesson, you'll learn Design Thinking. You'll see how to "
    "understand the people doing the work, solve the right problem, and test ideas cheaply. "
    "We'll follow Pooja, an improvement engineer at a medical devices plant."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Start with the people doing the work, and watch before "
    "you decide. Define the need without hiding a solution inside it. And test small, "
    "measuring both results and whether people really use it. Here's your action for this "
    "week. Watch ten cycles of one painful job, and talk to three people who do it. Great "
    "work completing this lesson. Next, you'll learn Elimination of Waste."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Design Thinking Is",
        "points": [("Start with the people in the process", "starts with the people"),
                   ("Empathize, define, ideate", "You empathize"),
                   ("Prototype and test, then repeat", "Then you prototype")],
        "example": "Pooja's packing station: infusion pumps, labels, and packers nobody had asked.",
        "example_cue": "Pooja's challenge",
        "script": "Design Thinking is a way of solving problems that starts with the people in the "
                  "process. The ones who do the work, support it, or receive it. You empathize, by "
                  "watching real work. You define the real need, and ideate many options. Then you "
                  "prototype something small, test it, and learn. And you repeat. Pooja's challenge "
                  "was the infusion pump packing station. So how does this fit with Lean?",
    },
    {
        "key": "p02", "num": 2, "title": "Design Thinking and Lean",
        "points": [("It doesn't replace Lean tools", "It doesn't replace"),
                   ("It finds the right problem first", "It helps you find"),
                   ("People adopt what they help design", "people adopt")],
        "example": "Last year's new packing method lasted two weeks. The packers went back to the old way.",
        "example_cue": "Last year",
        "script": "It doesn't replace A3, Kaizen or Poka Yoke. It helps you find the right problem "
                  "before you pick one of them. Lean removes waste. Design Thinking makes sure the "
                  "change fits real people and real work. And here's the bonus. People adopt what they "
                  "helped design. Last year, a new packing method lasted two weeks. Then the packers "
                  "quietly went back to the old way. Why do you think that happened?",
    },
    {
        "key": "p03", "num": 3, "title": "Working Principles",
        "points": [("Observe without assuming", "Watch without assuming"),
                   ("Separate facts from opinions", "Separate facts"),
                   ("Prototype small before big changes", "Try ideas small"),
                   ("Measure results and acceptance", "Measure both")],
        "example": "Pooja's rule: “Show me” before “tell me”.",
        "example_cue": "Pooja's rule",
        "script": "A few principles keep you honest. Watch without assuming you already know the "
                  "answer. Separate facts from opinions, and from proposed solutions. Treat operators "
                  "and support teams as your users. Try ideas small, before you change the whole "
                  "process. Measure both the results and whether people actually accept the change. "
                  "Pooja's rule was simple. Show me, before tell me. Which of these do you skip most "
                  "often?",
    },
    {
        "key": "p04", "num": 4, "title": "What It Prevents",
        "points": [("Automating a broken process", "Automating a broken"),
                   ("Fixing only the visible symptom", "Fixing only"),
                   ("Solutions people can't follow", "Forcing a solution"),
                   ("Big spending before testing", "Spending big")],
        "example": "The faster printer: a big spend, on a problem nobody had checked.",
        "example_cue": "The faster printer",
        "script": "Why bother? Because it prevents some expensive mistakes. Automating a broken "
                  "process you don't really understand. Fixing only the visible symptom. Forcing a "
                  "solution that people can't follow on a busy shift. And spending big, before testing "
                  "a single assumption. The faster printer was a perfect example. A big spend, on a "
                  "problem nobody had checked. So what are the steps you'll follow?",
    },
    {
        "key": "p05", "num": 5, "title": "Five Stages, One Loop",
        "points": [("Empathize · Define · Ideate", "Empathize asks"),
                   ("Prototype · Test", "Prototype asks"),
                   ("Desirable, feasible, viable", "A good answer is"),
                   ("Move on with evidence, not meetings", "Move to the next stage")],
        "example": "Pooja's gate: no ideas until she had real observations and a baseline.",
        "example_cue": "Pooja set one gate",
        "script": "There are five stages, and you can loop back. Empathize asks what users experience. "
                  "Define asks which problem matters most. Ideate asks what could solve it. Prototype "
                  "asks how it might work. Test asks whether it creates value. A good answer is "
                  "desirable, feasible and viable. Move to the next stage with evidence, not because a "
                  "meeting ended. Pooja set one gate. No ideas without observations. Ready to watch?",
    },
    {
        "key": "p06", "num": 6, "title": "Empathize at the Gemba",
        "points": [("Observe across shifts", "Watch several cycles"),
                   ("Interview after you observe", "Then ask open questions"),
                   ("Shadow one role end to end", "Shadow one person"),
                   ("Empathy map: say, think, do, feel", "An empathy map")],
        "example": "Pooja watched ten cycles on each shift, then spoke with five packers.",
        "example_cue": "Pooja watched",
        "script": "Empathy starts at the gemba. Watch several cycles, on normal and busy shifts. Then "
                  "ask open questions, after you've seen the work. Shadow one person through the whole "
                  "job, to see the handoffs. An empathy map helps you sort it all. What do they say, "
                  "think, do and feel? Pooja watched ten cycles on each shift. Then she spoke with five "
                  "packers. What do you think she saw?",
    },
    {
        "key": "p07", "num": 7, "title": "What Pooja Saw",
        "points": [("Walking to fetch labels", "packers walked"),
                   ("Two look-alike labels side by side", "Two labels that looked"),
                   ("Waiting for the printer", "the printer sometimes")],
        "example": "“I'm not slow. I'm searching.” A packer, on the night shift.",
        "example_cue": "One packer said",
        "script": "Not slow packers. The packers walked to a shared rack to fetch every label. Two "
                  "labels that looked almost the same sat side by side. And the printer sometimes "
                  "paused, so they waited. One packer said it perfectly. I'm not slow. I'm searching. "
                  "Notice what's missing? Nobody blamed anyone. These are facts about the work, not "
                  "the people. How would you turn them into a problem worth solving?",
    },
    {
        "key": "p08", "num": 8, "title": "Define the Need",
        "points": [("User · need · insight", "user, a need"),
                   ("No solution inside the statement", "It doesn't name"),
                   ("A baseline you can measure", "Add a baseline")],
        "example": "Packers need the right label at hand, because look-alike labels and walking cause errors. Now: 52 s vs 45 s TAKT, 12 errors per 1,000.",
        "example_cue": "Pooja wrote",
        "script": "Now define the need. A good statement names a user, a need and an insight. It "
                  "doesn't name the solution. Pooja wrote one sentence. Packers need the right label "
                  "right at hand, because look-alike labels and walking cause errors. Add a baseline. "
                  "The station took fifty-two seconds, against a TAKT of forty-five. And twelve "
                  "pumps in every thousand had a label error. Can you spot the printer anywhere in "
                  "that statement?",
    },
    {
        "key": "p09", "num": 9, "title": "Ideate: Go Wide First",
        "points": [("Brainwrite before you discuss", "Brainwriting"),
                   ("Ask “How might we…?”", "How might we"),
                   ("SCAMPER and the waste lens", "Try SCAMPER")],
        "example": "Pooja's team: 23 ideas in 30 minutes, from packers, quality and stores.",
        "example_cue": "Pooja's team",
        "script": "Now go wide, before you choose. Brainwriting means everyone writes ideas alone, "
                  "before the group talks. That way, the loudest voice doesn't win. Ask how might we "
                  "questions, to turn limits into chances. Try SCAMPER, or look through the eight "
                  "wastes. Pooja's team wrote twenty-three ideas in thirty minutes. Packers, quality "
                  "and stores all joined in. How do you pick just one?",
    },
    {
        "key": "p10", "num": 10, "title": "Select With a Scorecard",
        "points": [("Weight each criterion", "Weight each criterion"),
                   ("Rate each concept, add the scores", "Rate every concept"),
                   ("Safety and quality are gates", "safety and quality")],
        "example": "Label slots + scan check: 4.15. New printer at the station: 4.10.",
        "example_cue": "The top two",
        "script": "Use a simple scorecard. Weight each criterion, like quality, user acceptance, impact, "
                  "feasibility and cost. Rate every concept, from one to five. Multiply and add. But "
                  "safety and quality aren't just scores. They're gates. Fail one, and the idea is out. "
                  "The top two were close. Model-specific label slots with a scan check, and a new "
                  "printer at the station. The slots won, just. What would you test first?",
    },
    {
        "key": "p11", "num": 11, "title": "Prototype Small and Cheap",
        "points": [("Paper, cardboard or tape first", "Start with paper"),
                   ("One station before the line", "Try one station"),
                   ("Hours, not months", "measured in hours")],
        "example": "Cardboard label slots, one per model, taped beside the packer.",
        "example_cue": "Pooja's first prototype",
        "script": "Make the idea real, as cheaply as you can. Start with paper, cardboard or tape on "
                  "the floor. Try one station before the whole line. A good prototype is measured in "
                  "hours, not months. Pooja's first prototype was cardboard. One label slot per model, "
                  "taped right beside the packer, with the scanner at hand. It cost almost nothing. "
                  "But how would she know if it worked?",
    },
    {
        "key": "p12", "num": 12, "title": "Plan the Test",
        "points": [("A clear hypothesis", "Write a hypothesis"),
                   ("Scope, metrics and comparison", "Set the scope"),
                   ("A decision rule agreed up front", "Agree a decision rule")],
        "example": "Hypothesis: label slots + scan check bring cycle time inside TAKT and cut label errors by at least 75%.",
        "example_cue": "Pooja's hypothesis",
        "script": "Plan the test before you start it. Write a hypothesis. If we change this, we expect "
                  "that. Set the scope, the measures, and what you'll compare against. Agree a decision "
                  "rule up front. Adopt, adapt or stop. Pooja's hypothesis was clear. The slots and a "
                  "scan check would bring cycle time inside TAKT. And label errors would fall by at "
                  "least three quarters. What do you think happened?",
    },
    {
        "key": "p13", "num": 13, "title": "The Results",
        "points": [("Cycle time: 52 s down to 44 s", "Cycle time fell"),
                   ("Good pumps per shift: 500 up to 610", "Good pumps per shift"),
                   ("Label errors: 12 down to 2 per 1,000", "Label errors fell"),
                   ("Walking: 4 m down to 1.2 m", "Walking dropped")],
        "example": "18 of 20 packers used the new method: 90% adoption.",
        "example_cue": "Eighteen of twenty",
        "script": "The trial worked, mostly. Cycle time fell from fifty-two to forty-four seconds. "
                  "That's now inside TAKT. Good pumps per shift rose from five hundred to six hundred "
                  "and ten. Label errors fell from twelve to two per thousand. Walking dropped by more "
                  "than half. And eighteen of twenty packers used the new method. That's ninety percent. "
                  "So, should Pooja roll it out tomorrow?",
    },
    {
        "key": "p14", "num": 14, "title": "Adapt Before You Roll Out",
        "points": [("Not 100% adoption? Find out why", "Two packers"),
                   ("Simplify the hard step, test again", "simplified that step"),
                   ("Check other factors didn't cause it", "And check that")],
        "example": "The two packers were left-handed. The slots were on the right. Mirror the layout.",
        "example_cue": "It turned out",
        "script": "Not yet. Two packers didn't follow the method. So she asked them why. It turned out "
                  "they worked left-handed, and the slots were on the right. She simplified that step, "
                  "with a mirrored layout, and tested again. And check that other factors didn't cause "
                  "the gain, like an easier model mix or extra staff. Only then do you standardize. "
                  "How would you measure success?",
    },
    {
        "key": "p15", "num": 15, "title": "Measure, Standardize, Start",
        "points": [("Outcome, process, adoption, balance", "Measure the outcome"),
                   ("Standardize, train, review at 30/60/90", "Then standardize"),
                   ("Start tomorrow: 10 cycles, 3 people", "Start tomorrow")],
        "example": "Pooja's 90-day review: errors held at 2 per 1,000, adoption at 100%.",
        "example_cue": "At ninety days",
        "script": "Measure the outcome, the process, adoption and balance. Did anything else get worse, "
                  "like safety or cost? Then standardize, train every shift, and review at thirty, sixty "
                  "and ninety days. At ninety days, Pooja's errors held at two per thousand, and every "
                  "packer used the method. Start tomorrow. Watch ten cycles of one painful job, talk to "
                  "three people, and write one need.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "steps", "items": [
        {"label": "Empathize", "with": 1}, {"label": "Define", "with": 1},
        {"label": "Ideate", "with": 1}, {"label": "Prototype", "with": 2},
        {"label": "Test", "with": 2}]},
    "p02": {"type": "icons", "items": [
        {"label": "Lean tools stay", "icon": "wrench", "with": 0},
        {"label": "Right problem first", "icon": "search", "with": 1},
        {"label": "Owned by the users", "icon": "hand", "tone": "good", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Imposed method", "sub": "Gone in two weeks", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "Co-designed method", "sub": "People keep it", "icon": "check", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Observe", "icon": "search", "with": 0},
        {"label": "Facts first", "icon": "clipboard", "with": 1},
        {"label": "Small trials", "icon": "shape", "with": 2},
        {"label": "Acceptance", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Automating a mess", "icon": "gear", "tone": "bad", "with": 0},
        {"label": "Symptom only", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Can't be followed", "icon": "cross", "tone": "bad", "with": 2},
        {"label": "Big spend, no test", "icon": "trash", "tone": "bad", "with": 3}]},
    "p05": {"type": "steps", "items": [
        {"label": "Empathize", "with": 0}, {"label": "Define", "with": 0},
        {"label": "Ideate", "with": 0}, {"label": "Prototype", "with": 1},
        {"label": "Test", "with": 1}],
        "then": {"type": "icons", "with": 2, "items": [
            {"label": "Desirable", "sub": "Users need it", "icon": "person", "with": 2},
            {"label": "Feasible", "sub": "We can do it", "icon": "wrench", "with": 2},
            {"label": "Viable", "sub": "Worth the cost", "icon": "scale", "tone": "good", "with": 2}]}},
    "p06": {"type": "icons", "items": [
        {"label": "Observe", "icon": "search", "with": 0},
        {"label": "Interview", "icon": "person", "with": 1},
        {"label": "Shadow", "icon": "walk", "with": 2},
        {"label": "Say · think · do · feel", "icon": "clipboard", "with": 3}]},
    "p07": {"type": "flow", "items": [
        {"label": "Walk to the rack", "icon": "walk", "tone": "bad", "with": 0},
        {"label": "Look-alike labels", "icon": "label", "tone": "bad", "with": 1},
        {"label": "Wait for the printer", "icon": "clock", "tone": "bad", "with": 2}]},
    "p08": {"type": "doc", "items": [
        {"label": "User: the packers", "icon": "person", "with": 0},
        {"label": "Need: the right label at hand", "icon": "label", "with": "example"},
        {"label": "Insight: look-alikes and walking", "icon": "search", "with": "example"},
        {"label": "Baseline: 52 s vs 45 s, 12 per 1,000", "icon": "chartUp", "with": 2}]},
    "p09": {"type": "icons", "items": [
        {"label": "Brainwriting", "icon": "clipboard", "with": 0},
        {"label": "How might we…?", "icon": "key", "with": 1},
        {"label": "SCAMPER, 8 wastes", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 23, "icon": "key", "label": "ideas in 30 minutes",
                 "unit": "packers, quality and stores", "with": "example"}},
    "p10": {"type": "versus", "items": [
        {"label": "New printer", "sub": "Score 4.10 of 5", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Label slots + scan check", "sub": "Score 4.15 of 5", "icon": "check", "tone": "good", "with": "example"}]},
    "p11": {"type": "ladder", "top": "CHEAPEST", "bottom": "BIGGEST", "items": [
        {"label": "Paper, cardboard, tape", "icon": "shape", "with": 0},
        {"label": "One-station pilot", "icon": "pin", "with": 1},
        {"label": "Line trial", "icon": "sequence", "with": 1}],
        "then": {"type": "stat", "value": 1, "suffix": " slot per model", "icon": "label", "label": "cardboard, taped by the packer",
                 "unit": "scanner within reach", "with": "example"}},
    "p12": {"type": "flow", "items": [
        {"label": "Hypothesis", "icon": "key", "with": 0},
        {"label": "Scope and metrics", "icon": "clipboard", "with": 1},
        {"label": "Adopt · adapt · stop", "icon": "scale", "tone": "good", "with": 2}]},
    "p13": {"type": "compare", "before": {"label": "Before", "value": 12}, "after": {"label": "Trial", "value": 2},
            "unit": "label errors per 1,000 pumps", "note": "Cycle 52 s → 44 s · 500 → 610 good pumps", "with": 2,
            "then": {"type": "stat", "value": 90, "suffix": "%", "icon": "person", "label": "adoption",
                     "unit": "18 of 20 packers", "with": "example"}},
    "p14": {"type": "flow", "items": [
        {"label": "Ask why", "icon": "person", "with": 0},
        {"label": "Mirror the layout", "icon": "shape", "with": 1},
        {"label": "Check the model mix", "icon": "search", "with": 2},
        {"label": "Then standardize", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Standardize, train", "sub": "Day 0", "icon": "clipboard", "with": 1},
        {"label": "Review", "sub": "30 · 60", "icon": "search", "with": 1},
        {"label": "Errors held at 2", "sub": "90 days", "icon": "check", "tone": "good", "with": "example"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which is the best Design Thinking challenge statement?",
        "options": ["We need a faster label printer at packing",
                    "Packers need the right label at hand, because look-alike labels and walking cause errors",
                    "Packers must be more careful with labels"],
        "correct": 1,
        "explanation": "It names the user, the need and the insight, without choosing a solution or blaming anyone. The others are a solution and a blame.",
        "q_script": "Quick check. Which of these is the best challenge statement? Take a few seconds.",
        "a_script": "It's the second one. It names the user, the need and the insight. The first one "
                    "is already a solution, and the last one is just blame.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A pilot cuts cycle time, but only 6 of 10 operators use the new method. What next?",
        "options": ["Roll it out: the numbers improved",
                    "Ask the other four why, simplify, and test again",
                    "Make it mandatory and audit daily"],
        "correct": 1,
        "explanation": "Low adoption is evidence too. Find out what makes the method hard for those users, improve it, and re-test before you standardize.",
        "q_script": "One more, and this one's a scenario. A pilot cuts cycle time. But only six of ten "
                    "operators use the new method. What should the team do? Have a think.",
        "a_script": "Ask the other four why, simplify the hard part, and test again. Low adoption is "
                    "evidence too, so treat it like any other result.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
