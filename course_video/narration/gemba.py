"""Gemba (3G: Gemba, Genbutsu, Genjitsu) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Manoj,
a production supervisor on a wireless earbuds line. The dashboard blamed
shift B for twice the audio-test failures; going to see the real place, the
real earbuds and the real facts found a wrong soldering tip instead.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/gemba.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py gemba  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "gb"
NAME = "gemba"

LETTERS = ["ESD", "MES"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. Genbutsu / Genjitsu = gen-BOO-tsu /
# gen-JEE-tsu (Gemba Academy's sound-alike guide); 3G = "three-G" (one token,
# so captions map word for word).
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = re.sub(r"\b3G\b", "three-G", text)
    text = re.sub(r"\bGenbutsu\b", "Gen-boot-sue", text)
    return re.sub(r"\bGenjitsu\b", "Gen-jeet-sue", text)


INTRO_SCRIPT = (
    "The dashboard said shift B was careless. Twice as many earbuds failed audio test as on "
    "shift A. The plan was simple. Retrain shift B. Nobody had looked at a single failed "
    "earbud. Sound familiar? In this lesson, you'll learn Gemba, and the 3G behind it. You'll "
    "see how to go to the real place, examine the real thing, and check the real facts. "
    "We'll follow Manoj, a production supervisor on a wireless earbuds line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Go to the real place, and watch real cycles before you "
    "decide. Hold the real thing, and compare it with a good one. And check the real facts, "
    "with counts, times and a denominator. Here's your action for this week. Take one "
    "recurring problem, and do a thirty-minute 3G visit. Great work completing this lesson. "
    "Next, you'll learn Hancho, leadership on the shop floor."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "Go and See",
        "points": [("Gemba: the real place", "Gemba means"),
                   ("Genbutsu: the real thing", "Genbutsu means"),
                   ("Genjitsu: the real facts", "Genjitsu means")],
        "example": "Manoj's rule: no decision on shift B until he'd held a failed earbud.",
        "example_cue": "Manoj made one rule",
        "script": "Lean has a simple habit. Go and see, before you decide. It comes as three Japanese "
                  "words, often called the 3G. Gemba means the real place, where the work happens. "
                  "Genbutsu means the real thing, like the failed part. Genjitsu means the real facts. "
                  "Manoj made one rule. No decision about shift B, until he'd held a failed earbud in "
                  "his hand. Why does that matter?",
    },
    {
        "key": "p02", "num": 2, "title": "Why Reports Aren't Enough",
        "points": [("Dashboards show symptoms", "Dashboards show"),
                   ("Reports hide the context", "Reports hide"),
                   ("Facts stop the blame", "And facts stop")],
        "example": "The dashboard showed shift B's failures. It didn't show why.",
        "example_cue": "Manoj's dashboard",
        "script": "Because reports only tell you part of the story. Dashboards show symptoms, not "
                  "causes. Reports hide the sequence, the workarounds and the context. A part, a "
                  "fixture or a workstation often shows evidence no spreadsheet can. And facts stop "
                  "the blame, and the money wasted on the wrong fix. Manoj's dashboard showed that "
                  "shift B failed more. It couldn't show why. So where do you start?",
    },
    {
        "key": "p03", "num": 3, "title": "3G in One View",
        "points": [("Where did it happen?", "Gemba asks"),
                   ("What exactly was affected?", "Genbutsu asks"),
                   ("What actually occurred?", "Genjitsu asks")],
        "example": "Line 2 · audio test · left earbud · 22 of 1,100 on shift B",
        "example_cue": "For Manoj",
        "script": "Think of each G as a question. Gemba asks, where did it happen? The line, the "
                  "station, the step. Genbutsu asks, what exactly was affected? The unit, the part, "
                  "the tool. Genjitsu asks, what actually occurred? Times, counts and measurements. "
                  "For Manoj, it was line two, the audio test, and the left earbud. Twenty-two "
                  "failures in eleven hundred, on shift B. So let's go to the place.",
    },
    {
        "key": "p04", "num": 4, "title": "Gemba: The Real Place",
        "points": [("Have a clear question", "Start with a clear question"),
                   ("Tell the area owner, wear the PPE", "Tell the area owner"),
                   ("Watch several full cycles", "Watch several"),
                   ("Compare with the standard", "Compare what you see")],
        "example": "Manoj's question: what's different at audio test on shift B?",
        "example_cue": "Manoj's question",
        "script": "Start with a clear question, and a target process. Tell the area owner you're "
                  "coming, and follow the P-P-E and E-S-D rules. Watch several full cycles, without "
                  "interfering. Compare what you see with the approved standard work. Then ask neutral "
                  "questions, and note any gap with its time and place. Manoj's question was short. "
                  "What's different at audio test on shift B? How should you behave there?",
    },
    {
        "key": "p05", "num": 5, "title": "Gemba Manners",
        "points": [("Not a surprise inspection", "isn't a surprise"),
                   ("Listen before suggesting", "Listen before"),
                   ("Never judge from one cycle", "never judge")],
        "example": "Manoj stayed through a full shift B hour, and asked: “What makes this job hard?”",
        "example_cue": "Manoj stayed",
        "script": "A gemba visit isn't a surprise inspection, or a hunt for someone to blame. Listen "
                  "before suggesting anything. Don't interrupt critical work. And never judge from one "
                  "cycle, because one cycle can mislead you. Manoj stayed for a full hour on shift B. "
                  "He asked one question. What makes this job hard for you? The answers surprised him. "
                  "But what should you hold in your hand?",
    },
    {
        "key": "p06", "num": 6, "title": "Genbutsu: The Real Thing",
        "points": [("The failed unit, the part, the tool", "That means the failed unit"),
                   ("Record model, lot, time, station", "Record the model"),
                   ("Compare bad with good", "Compare a bad unit")],
        "example": "Failed left earbuds: dull, grainy solder on the speaker wire. Good ones: bright and smooth.",
        "example_cue": "Manoj compared",
        "script": "Hold the real thing. That means the failed unit, the component, the fixture or the "
                  "tool. Record the model, lot, time and station before you touch it. Inspect it "
                  "without changing the evidence. Compare a bad unit with a good one, side by side, "
                  "under the same light. Manoj compared failed left earbuds with good ones. The failed "
                  "solder joints looked dull and grainy. What could cause that?",
    },
    {
        "key": "p07", "num": 7, "title": "Safety Comes First",
        "points": [("Never bypass an interlock", "Never bypass"),
                   ("Lockout before opening equipment", "Lock out"),
                   ("ESD handling for electronics", "handle electronics")],
        "example": "Manoj asked the technician to cool and lock out the iron before checking it.",
        "example_cue": "Manoj asked",
        "script": "One rule beats curiosity. Never bypass an interlock, or open live equipment, just to "
                  "see the real thing. Lock out first, and let a qualified person do it. Handle "
                  "electronics with E-S-D protection, or you'll create new defects while you "
                  "investigate. Manoj asked the technician to cool down and lock out the soldering "
                  "station before checking it. Safe evidence is good evidence. Now, what about the facts?",
    },
    {
        "key": "p08", "num": 8, "title": "Genjitsu: The Real Facts",
        "points": [("Facts, not opinions", "Replace opinions"),
                   ("Counts with a denominator", "Use counts"),
                   ("A signal isn't proof", "is a signal")],
        "example": "Shift B: 22 of 1,100 (2.0%). Shift A: 9 of 1,050 (0.9%).",
        "example_cue": "Shift B had",
        "script": "Replace opinions with facts. Testing is slow is an opinion. Median test time rose "
                  "from forty-six to sixty-one seconds is a fact. Use counts with a denominator, and "
                  "time stamps you can trust. Shift B had twenty-two failures in eleven hundred. Shift "
                  "A had nine in about a thousand. That difference is a signal to investigate. But is "
                  "it proof that shift B caused it?",
    },
    {
        "key": "p09", "num": 9, "title": "One Connected Investigation",
        "points": [("Define and contain first", "Define the problem"),
                   ("Place, thing, facts, together", "go to the place"),
                   ("Test causes before fixing", "Then test")],
        "example": "Manoj held suspect earbuds from shift B before anything else.",
        "example_cue": "Manoj held",
        "script": "No. So use the 3G as one connected investigation, not three boxes to tick. Define "
                  "the problem in numbers, and protect your customer first. Then go to the place, "
                  "inspect the thing, and gather the facts, together. Then test possible causes, "
                  "before you change anything permanently. Manoj held all suspect earbuds from shift B "
                  "first. Then he went back to the station. What did the place show him?",
    },
    {
        "key": "p10", "num": 10, "title": "What the Place Showed",
        "points": [("Same people, same method", "followed the same method"),
                   ("A different soldering tip", "the soldering tip"),
                   ("Changed on Monday night", "changed on Monday")],
        "example": "Shift B's iron had a smaller tip from the spares crib. Not the standard one.",
        "example_cue": "It had come",
        "script": "At first, nothing looked wrong. Shift B followed the same method as shift A, step "
                  "by step. Then Manoj looked closely at the soldering tip. It was smaller than the one "
                  "on shift A's station. It had been changed on Monday night. It had come from the "
                  "spares crib, and it wasn't the standard tip. Could a smaller tip make a weaker joint? "
                  "How would you find out?",
    },
    {
        "key": "p11", "num": 11, "title": "What the Facts Showed",
        "points": [("Failures by station and time", "Manoj mapped"),
                   ("Started right after the tip change", "started the shift"),
                   ("A controlled trial confirmed it", "Then a controlled trial")],
        "example": "Trial: standard tip 1 failure in 300. Smaller tip: 7 in 300.",
        "example_cue": "With the standard tip",
        "script": "Manoj mapped every failure by station, time and lot. They started the shift after "
                  "the tip change, and only at that one station. Then a controlled trial, approved by "
                  "engineering, tested both tips. With the standard tip, one earbud failed in three "
                  "hundred. With the smaller tip, seven failed. The smaller tip couldn't put enough heat "
                  "into the joint. Was shift B careless, after all?",
    },
    {
        "key": "p12", "num": 12, "title": "3G Feeds Root Cause",
        "points": [("Every why backed by evidence", "Every why"),
                   ("Never end at “operator error”", "Never end"),
                   ("Ask what made the error possible", "Ask what process")],
        "example": "Root cause: the spares crib stocked the wrong tip, and the standard didn't name it.",
        "example_cue": "Manoj's last why",
        "script": "No. The 3G gives your root-cause tools real evidence. With five whys, every why must "
                  "be backed by something you saw or measured. Never end at operator error, or more "
                  "training. Ask what process condition made the error possible. Manoj's last why was "
                  "clear. The spares crib stocked the wrong tip, and the standard didn't name the tip "
                  "type. So what did he change?",
    },
    {
        "key": "p13", "num": 13, "title": "Fix and Verify",
        "points": [("Correct tip, named on the standard", "named the tip"),
                   ("Tip check at every shift start", "a tip check"),
                   ("Verified over five shifts", "verified the result")],
        "example": "Shift B: 20 per 1,000 down to 8 per 1,000, level with shift A.",
        "example_cue": "Failures fell",
        "script": "The fix was simple. The standard now named the tip type, and the spares crib stocked "
                  "only the right one. A tip check joined the start-of-shift routine. Then he verified "
                  "the result over five full shifts, not one good hour. Shift B's failures fell from "
                  "twenty per thousand to eight, level with shift A. And shift B never needed retraining. How could you "
                  "make this a daily habit?",
    },
    {
        "key": "p14", "num": 14, "title": "The 30-Minute Gemba Walk",
        "points": [("Purpose and safety first", "review safety"),
                   ("Observe, then check the thing and data", "observe the process"),
                   ("Agree containment and an owner", "agree containment")],
        "example": "Manoj's question at every stop: “What's the standard, and what's actually happening?”",
        "example_cue": "Manoj's favourite",
        "script": "Make it standard work. In a thirty-minute walk, first review safety, the gap and "
                  "your purpose. Then observe the process at the point of work for ten minutes. "
                  "Inspect the affected item, and check the key data. Ask the team for causes, agree "
                  "containment, and name an owner with a date. Manoj's favourite question is simple. "
                  "What's the standard, and what's actually happening? What would you ask?",
    },
    {
        "key": "p15", "num": 15, "title": "Mistakes to Avoid",
        "points": [("Managing from the dashboard", "Managing only"),
                   ("Treating one sample as the truth", "Treating one sample"),
                   ("Closing after training", "Closing a problem")],
        "example": "Manoj now spends his first 30 minutes of every shift at the gemba.",
        "example_cue": "Manoj now",
        "script": "Watch for a few common mistakes. Managing only from the dashboard. Relying on "
                  "interviews, without holding the part. Treating one sample as the truth. Changing "
                  "settings during the investigation, and destroying the evidence. Closing a problem "
                  "after training, without checking it stopped. Manoj now spends the first thirty "
                  "minutes of every shift at the gemba. Could you do the same?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Gemba", "sub": "Real place", "icon": "walk", "with": 0},
        {"label": "Genbutsu", "sub": "Real thing", "icon": "wave", "with": 1},
        {"label": "Genjitsu", "sub": "Real facts", "icon": "search", "with": 2}]},
    "p02": {"type": "versus", "items": [
        {"label": "Dashboard", "sub": "Shows symptoms", "icon": "chartUp", "with": 0},
        {"label": "The real place", "sub": "Shows causes", "icon": "walk", "tone": "good", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "Where?", "sub": "Line 2, audio test", "icon": "pin", "with": 0},
        {"label": "What?", "sub": "Left earbud", "icon": "wave", "with": 1},
        {"label": "What occurred?", "sub": "22 of 1,100", "icon": "count", "with": 2}]},
    "p04": {"type": "steps", "items": [
        {"label": "Clear question", "with": 0}, {"label": "Owner, PPE, ESD", "with": 1},
        {"label": "Watch full cycles", "with": 2}, {"label": "Compare with standard", "with": 3}]},
    "p05": {"type": "versus", "items": [
        {"label": "Surprise inspection", "sub": "Hunting for blame", "icon": "cross", "tone": "bad", "with": 0},
        {"label": "Respectful visit", "sub": "“What makes this hard?”", "icon": "person", "tone": "good", "with": "example"}]},
    "p06": {"type": "versus", "items": [
        {"label": "Failed earbud", "sub": "Dull, grainy joint", "icon": "cross", "tone": "bad", "with": "example"},
        {"label": "Good earbud", "sub": "Bright, smooth joint", "icon": "check", "tone": "good", "with": "example"}]},
    "p07": {"type": "icons", "items": [
        {"label": "No bypassed interlocks", "icon": "lock", "with": 0},
        {"label": "Lockout first", "icon": "key", "with": 1},
        {"label": "ESD protection", "icon": "shield", "tone": "good", "with": 2}]},
    "p08": {"type": "bars", "label": "", "note": "Failures per 1,000 earbuds: a signal, not proof", "with": "example", "items": [
        {"label": "Shift A", "value": 9, "with": "example"},
        {"label": "Shift B", "value": 20, "tone": "bad", "with": "example"}]},
    "p09": {"type": "steps", "items": [
        {"label": "Define and contain", "with": 0},
        {"label": "Place", "with": 1}, {"label": "Thing", "with": 1}, {"label": "Facts", "with": 1},
        {"label": "Test causes", "with": 2}]},
    "p10": {"type": "versus", "items": [
        {"label": "Shift B tip", "sub": "Smaller, from the spares crib", "icon": "wrench", "tone": "bad", "with": 1},
        {"label": "Standard tip", "sub": "Shift A", "icon": "check", "tone": "good", "with": 1}]},
    "p11": {"type": "bars", "label": "", "note": "Controlled trial: failures in 300 earbuds", "with": "example", "items": [
        {"label": "Standard tip", "value": 1, "tone": "good", "with": "example"},
        {"label": "Smaller tip", "value": 7, "tone": "bad", "with": "example"}]},
    "p12": {"type": "steps", "items": [
        {"label": "Weak solder joints", "with": 0},
        {"label": "Smaller tip, too little heat", "with": 0},
        {"label": "Wrong tip in the spares crib", "with": "example"},
        {"label": "Tip type not on the standard", "with": "example"}]},
    "p13": {"type": "compare", "before": {"label": "Before", "value": 20}, "after": {"label": "After", "value": 8},
            "unit": "failures per 1,000 earbuds, shift B", "note": "Level with shift A, verified over 5 shifts", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Safety, gap, purpose", "sub": "0–5", "icon": "shield", "with": 0, "span": 5},
        {"label": "Observe", "sub": "5–15", "icon": "walk", "with": 1, "span": 10},
        {"label": "Thing and data", "sub": "15–22", "icon": "search", "with": 1, "span": 7},
        {"label": "Causes, owner", "sub": "22–30", "icon": "person", "tone": "good", "with": 2, "span": 8}]},
    "p15": {"type": "icons", "items": [
        {"label": "Dashboard only", "icon": "chartUp", "tone": "bad", "with": 0},
        {"label": "One sample", "icon": "count", "tone": "bad", "with": 1},
        {"label": "Closed after training", "icon": "clipboard", "tone": "bad", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "Which statement is a real fact (Genjitsu)?",
        "options": ["“Shift B is always careless.”",
                    "“The supplier caused it.”",
                    "“18 of 24 failures came from lot B.”"],
        "correct": 2,
        "explanation": "A fact has counts, a denominator and a scope you can check. The others are opinions, and the supplier claim is still unproven.",
        "q_script": "Quick check. Which of these statements is a real fact? Take a few seconds.",
        "a_script": "It's the last one. It has a count, a denominator and a scope you can check. The "
                    "other two are just opinions.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "The dashboard shows one shift with twice the defects. The manager wants to retrain that shift. What first?",
        "options": ["Retrain them today: the data is clear",
                    "Go to the station, hold the failed units, and check the facts",
                    "Swap the two shifts' operators"],
        "correct": 1,
        "explanation": "A difference between shifts is a signal, not proof. Go and see: the real place, the real thing and the real facts, before you decide on any fix.",
        "q_script": "One more, and this one's a scenario. The dashboard shows one shift with twice the "
                    "defects. The manager wants to retrain that shift. What should happen first? Have a think.",
        "a_script": "Go and see. Visit the station, hold the failed units, and check the facts. A "
                    "difference between shifts is a signal, not proof.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
