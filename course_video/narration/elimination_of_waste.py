"""Elimination of Waste lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Deepak,
a production manager on a soundbar line (home audio), running a waste walk
and removing the rework caused by a rattling speaker wire. M (Muda, Mura,
Muri) teaches the eight wastes in depth; this lesson is about the value test,
finding waste with facts, and proving the gain.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/elimination_of_waste.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py elimination_of_waste  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "ew"
NAME = "elimination_of_waste"

LETTERS = ["ECRS", "FPY", "SOP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. TIMWOODS = "Tim Woods".
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return text.replace("TIMWOODS", "Tim-Woods")  # one token, so captions map


INTRO_SCRIPT = (
    "Every month, fifteen hundred soundbars went back for rework. Each one cost forty-two "
    "rupees to fix. Nobody had ever added it up. Sound familiar? In this lesson, you'll "
    "learn Elimination of Waste. You'll see how to spot work your customer won't pay for, "
    "remove its cause, and prove the gain. We'll follow Deepak, a production manager on a "
    "soundbar line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Waste is anything your customer wouldn't pay for, but "
    "never your safety or quality checks. Find it with facts at the gemba, not opinions. "
    "And remove the cause, then prove the gain and hold it. Here's your action for this "
    "week. Walk your line for thirty minutes, and write down three wastes as facts. Great "
    "work completing this lesson. Next, you'll learn F-M-E-A, failure mode and effects analysis."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Waste Really Is",
        "points": [("Uses resources, adds no customer value", "Waste is any activity"),
                   ("Not one-time cost cutting", "It isn't a one-time"),
                   ("Remove the cause, prevent it returning", "remove its root cause")],
        "example": "Deepak's line: 1,500 soundbars reworked every month.",
        "example_cue": "On Deepak's line",
        "script": "Let's start with a definition. Waste is any activity that uses time, space, material "
                  "or effort, but adds no value for your customer. Eliminating it isn't a one-time cost "
                  "cutting drive. You find the waste, remove its root cause, and stop it coming back. On "
                  "Deepak's line, fifteen hundred soundbars were reworked every month. So how do you "
                  "decide what's value, and what's waste?",
    },
    {
        "key": "p02", "num": 2, "title": "The Value Test",
        "points": [("Changes the product", "It changes the product"),
                   ("The customer would pay for it", "The customer would pay"),
                   ("Done right, the first time", "It's done right"),
                   ("Else: necessary, or pure waste", "Everything else")],
        "example": "Fitting the speaker: value. Re-fitting it after a rattle: pure waste.",
        "example_cue": "Fitting the speaker",
        "script": "Use a simple value test. An activity adds value only when three things are true. "
                  "It changes the product. The customer would pay for that change. And it's done right, "
                  "the first time. Everything else is either necessary, like a legal check, or pure "
                  "waste. Fitting the speaker is value. Re-fitting it after a rattle is pure waste. How "
                  "much of your day passes that test?",
    },
    {
        "key": "p03", "num": 3, "title": "Why It Matters",
        "points": [("Faster flow, shorter lead time", "Work flows faster"),
                   ("Fewer defects and less rework", "Fewer defects"),
                   ("Capacity released, no new spend", "You free up people"),
                   ("Ideas from the people doing the work", "your people get")],
        "example": "Deepak's target: free capacity for a new model, without adding a shift.",
        "example_cue": "Deepak needed",
        "script": "Why bother? Because waste hides your capacity. Remove it, and work flows faster, so "
                  "lead time shrinks. Fewer defects means less rework and fewer returns. You free up "
                  "people, machines, space and cash, without new investment. And your people get to "
                  "use their ideas. Deepak needed room for a new soundbar model, without adding a shift. "
                  "Where would your spare capacity come from?",
    },
    {
        "key": "p04", "num": 4, "title": "Three Guardrails",
        "points": [("Safety and quality checks aren't waste", "Never call a safety"),
                   ("Don't push waste onto someone else", "Don't push waste"),
                   ("People are never the waste", "people are never")],
        "example": "The final audio test stays. It protects the customer.",
        "example_cue": "On Deepak's line",
        "script": "Before you start cutting, three guardrails. Never call a safety or quality check "
                  "waste, unless a risk review approves it. Don't push waste onto another shift, a "
                  "supplier or your customer. Moving it isn't removing it. And people are never the "
                  "waste. Unused skill is. On Deepak's line, the final audio test stays. It protects "
                  "every customer. So which wastes do you look for?",
    },
    {
        "key": "p05", "num": 5, "title": "The Eight Wastes",
        "points": [("Transport, inventory, motion, waiting", "Transport, inventory"),
                   ("Overproduction, overprocessing", "overproduction"),
                   ("Defects, unused skills", "defects and unused skills")],
        "example": "Remember them as TIMWOODS.",
        "example_cue": "Remember them as",
        "script": "Lean groups waste into eight types. You'll meet them again in the Muda lesson. Transport, "
                  "inventory, motion and waiting. Then overproduction, and overprocessing, which means "
                  "doing more than the customer needs. Finally, defects and unused skills. Remember them "
                  "as TIMWOODS. Every one of them hides somewhere on every line, including yours. The real skill isn't naming them. It's seeing them on your own line. So "
                  "how do you look?",
    },
    {
        "key": "p06", "num": 6, "title": "The Waste Walk",
        "points": [("Go to the gemba during normal work", "Go to the gemba"),
                   ("Record facts, never blame", "Write down facts"),
                   ("Where, what, how long, how often", "Note where it happened")],
        "example": "Fact: “Four operators waited 12 minutes for missing grilles.” Opinion: “Stores is always late.”",
        "example_cue": "Compare these two",
        "script": "Do a waste walk. Go to the gemba during normal production, not during a visit. Write "
                  "down facts, and never blame a person. Note where it happened, what product, how long "
                  "and how often. Watch the people, the parts and the paperwork. Compare these two. Four operators waited twelve minutes for missing "
                  "grilles. Or, stores is always late. Only the first tells you where to look, and how big it is. Which one can you actually fix?",
    },
    {
        "key": "p07", "num": 7, "title": "What Deepak Found",
        "points": [("Waiting for late kits", "Operators waited"),
                   ("Reaching and walking for tools", "reached and walked"),
                   ("A duplicate barcode scan", "the same barcode"),
                   ("Rework: buzzing soundbars", "the biggest")],
        "example": "Rework was the biggest: 1,500 buzzing soundbars a month.",
        "example_cue": "the biggest",
        "script": "In one hour, Deepak's team filled a page. Operators waited for kits that arrived "
                  "late. They reached and walked for screwdrivers at every cycle. Packing scanned the "
                  "same barcode twice, in two different systems. But the biggest was rework. Fifteen "
                  "hundred soundbars a month failed the buzz test, and went back to the repair bench. "
                  "How do you measure how much time is really value?",
    },
    {
        "key": "p08", "num": 8, "title": "Measure the Flow",
        "points": [("Flow efficiency = value time ÷ lead time", "Flow efficiency is"),
                   ("18 min of value in 240 min", "eighteen minutes"),
                   ("Only 7.5% of the time adds value", "seven and a half")],
        "example": "A soundbar spends 4 hours in the plant. Only 18 minutes change it.",
        "example_cue": "A soundbar spends",
        "script": "Put a number on it. Flow efficiency is value-added time, divided by total lead time. "
                  "A soundbar spends four hours inside Deepak's plant. Only eighteen minutes of that "
                  "actually changes it. That's a flow efficiency of seven and a half percent. Everything "
                  "else is waiting, moving, checking or fixing. Don't panic. That's normal at the "
                  "start. But which waste do you attack first?",
    },
    {
        "key": "p09", "num": 9, "title": "Find the Root Cause",
        "points": [("Pareto: pick the biggest loss", "Use a Pareto"),
                   ("Ask why, with evidence", "Then ask why"),
                   ("Fix the cause, not the symptom", "Fix the cause")],
        "example": "Root cause: no fixed route for the speaker wire, so it touched the cone.",
        "example_cue": "The wire had",
        "script": "Use a Pareto, and pick the biggest loss first. For Deepak, that was rework. Then ask "
                  "why, with evidence. Why did soundbars buzz? A speaker wire touched the cone. Why? The "
                  "wire had no fixed route, so every operator placed it differently. That's a process "
                  "cause, not a careless person. Fix the cause, not the symptom. So what countermeasure "
                  "would you choose?",
    },
    {
        "key": "p10", "num": 10, "title": "Countermeasures: ECRS",
        "points": [("Eliminate the unnecessary", "Eliminate what"),
                   ("Combine tasks or checks", "Combine tasks"),
                   ("Rearrange sequence or layout", "Rearrange"),
                   ("Simplify what's left", "Simplify")],
        "example": "A wire-routing clip, kit carts at the line, one scan instead of two.",
        "example_cue": "Deepak's team chose",
        "script": "Think ECRS. Eliminate what isn't needed. Combine tasks or checks that belong together. "
                  "Rearrange the sequence or the layout. Simplify what's left, and make it visual. "
                  "Deepak's team chose three changes. A small clip that routes the speaker wire one way "
                  "only. Kit carts delivered to the line every hour. And one scan at packing instead of "
                  "two. Which E-C-R-S letter fits each one?",
    },
    {
        "key": "p11", "num": 11, "title": "The Cost of Defects",
        "points": [("Internal: scrap, rework, retest", "Internal failures"),
                   ("External: returns, warranty, freight", "External failures"),
                   ("Every repair hides more waste", "every repair")],
        "example": "Rework: ₹42 per soundbar, 1,500 a month.",
        "example_cue": "Each rework",
        "script": "Defects are the most expensive waste. Internal failures mean scrap, rework, retest "
                  "and stopped lines. External failures mean returns, warranty claims and urgent freight. "
                  "And every repair hides more waste, like handling, waiting and paperwork. A buzzing "
                  "soundbar was opened, re-routed, retested and logged again. Each rework "
                  "on Deepak's line cost forty-two rupees. With fifteen hundred a month, it added up "
                  "fast. So did the clip work?",
    },
    {
        "key": "p12", "num": 12, "title": "The Results",
        "points": [("Rework: 1,500 down to 300 a month", "Rework fell"),
                   ("First pass yield up to 99%", "First pass yield"),
                   ("Reaching for tools: 22 s down to 13 s", "reaching for tools")],
        "example": "Same people, same shift. Room for the new model.",
        "example_cue": "Same people",
        "script": "It did, after a four-week trial. Rework fell from fifteen hundred to three hundred "
                  "soundbars a month. First pass yield rose to ninety-nine percent. With kit carts and "
                  "tools at hand, reaching for tools dropped from twenty-two seconds to thirteen per "
                  "cycle. Same people, same shift, and now there's room for the new model. But what "
                  "was it worth in money?",
    },
    {
        "key": "p13", "num": 13, "title": "Proving the Money",
        "points": [("Savings = avoided cost − cost of the fix", "Savings are"),
                   ("Separate hard savings from capacity", "Keep hard savings"),
                   ("Finance confirms the numbers", "Finance should confirm")],
        "example": "1,200 fewer reworks × ₹42 × 12 months ≈ ₹6 lakh. Minus ₹1.2 lakh for the fix: ≈ ₹4.8 lakh net.",
        "example_cue": "Twelve hundred fewer",
        "script": "Savings are the cost you avoid, minus what the fix cost. Twelve hundred fewer reworks "
                  "a month, at forty-two rupees, over a year. That's about six lakh rupees. The clips, "
                  "carts and system change cost about one point two lakh. So the first-year net benefit "
                  "is about four point eight lakh. Keep hard savings separate from freed capacity. And "
                  "Finance should confirm the numbers. How do you make it stick?",
    },
    {
        "key": "p14", "num": 14, "title": "Make It Stick",
        "points": [("Update SOP, layout, training", "Update the SOP"),
                   ("Daily board: target, actual, gap, action", "A daily board"),
                   ("Audit at 7, 30 and 90 days", "Audit at seven")],
        "example": "Deepak's day-30 audit: one shift had stopped using the clip. Fixed the same day.",
        "example_cue": "At day thirty",
        "script": "Make the new way the normal way. Update the SOP, the layout and the training. A daily "
                  "board shows the target, the actual, the gap and the action, with an owner. Audit at "
                  "seven, thirty and ninety days, because drift is quiet. At day thirty, one shift had "
                  "stopped using the clip. Deepak's team found it, and fixed it the same day. Would "
                  "your audit have caught that?",
    },
    {
        "key": "p15", "num": 15, "title": "Your 30-Day Plan",
        "points": [("Days 1–7: pick a product, walk, map", "In the first week"),
                   ("Days 8–18: Pareto, root cause, pilot", "Over the next eleven days"),
                   ("Days 19–30: measure, standardize, audit", "In the last twelve days")],
        "example": "Then share it: other lines copy what worked, after checking it fits.",
        "example_cue": "Then share",
        "script": "Here's a thirty-day plan you can start now. In the first week, pick one product "
                  "family, walk the gemba, and map the flow. Over the next eleven days, use a Pareto, find "
                  "the root cause, and run a small pilot. In the last twelve days, measure the result, "
                  "update the standard, and audit it. Then share it, so other lines copy what worked. "
                  "Which product will you walk first?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "No customer value", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "Not one-off cuts", "icon": "calendar", "with": 1},
        {"label": "Remove the cause", "icon": "key", "tone": "good", "with": 2}],
        "then": {"type": "stat", "value": 1500, "icon": "wave", "label": "soundbars reworked every month",
                 "unit": "Deepak's line", "with": "example"}},
    "p02": {"type": "steps", "items": [
        {"label": "Changes the product", "with": 0},
        {"label": "Customer would pay", "with": 1},
        {"label": "Right first time", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Re-fit after a rattle", "sub": "Pure waste", "icon": "wrench", "tone": "bad", "with": "example"},
            {"label": "Fit the speaker", "sub": "Value", "icon": "wave", "tone": "good", "with": "example"}]}},
    "p03": {"type": "icons", "items": [
        {"label": "Faster flow", "icon": "chartDown", "with": 0},
        {"label": "Fewer defects", "icon": "check", "with": 1},
        {"label": "Capacity freed", "icon": "box", "with": 2},
        {"label": "People's ideas", "icon": "person", "tone": "good", "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Keep safety & quality checks", "icon": "shield", "tone": "good", "with": 0},
        {"label": "Don't shift waste", "icon": "sequence", "with": 1},
        {"label": "People aren't waste", "icon": "person", "with": 2}]},
    "p05": {"type": "icons", "items": [
        {"label": "Transport", "icon": "sequence", "with": 0},
        {"label": "Inventory", "icon": "stack", "with": 0},
        {"label": "Motion", "icon": "walk", "with": 0},
        {"label": "Waiting", "icon": "clock", "with": 0},
        {"label": "Overproduction", "icon": "box", "with": 1},
        {"label": "Overprocessing", "icon": "gear", "with": 1},
        {"label": "Defects", "icon": "cross", "with": 2},
        {"label": "Unused skills", "icon": "person", "with": 2}]},
    "p06": {"type": "flow", "items": [
        {"label": "Normal production", "icon": "walk", "with": 0},
        {"label": "Facts, no blame", "icon": "clipboard", "with": 1},
        {"label": "Where · how long · how often", "icon": "clock", "with": 2}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "“Stores is always late”", "sub": "Opinion", "icon": "cross", "tone": "bad", "with": "example"},
            {"label": "“4 waited 12 min for grilles”", "sub": "Fact", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Late kits", "icon": "clock", "tone": "bad", "with": 0},
        {"label": "Reaching for tools", "icon": "walk", "tone": "bad", "with": 1},
        {"label": "Double scan", "icon": "barcode", "tone": "bad", "with": 2},
        {"label": "Buzzing soundbars", "icon": "wave", "tone": "bad", "with": 3}]},
    "p08": {"type": "compare", "before": {"label": "Lead time", "value": 240}, "after": {"label": "Value-added", "value": 18},
            "unit": "minutes per soundbar", "note": "Flow efficiency 7.5%", "with": 1},
    "p09": {"type": "steps", "items": [
        {"label": "Soundbars buzz", "with": 1},
        {"label": "Wire touches the cone", "with": 1},
        {"label": "No fixed wire route", "with": "example"}]},
    "p10": {"type": "steps", "items": [
        {"label": "Eliminate", "with": 0}, {"label": "Combine", "with": 1},
        {"label": "Rearrange", "with": 2}, {"label": "Simplify", "with": 3}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Wire-routing clip", "icon": "shape", "tone": "good", "with": "example"},
            {"label": "Hourly kit carts", "icon": "box", "with": "example"},
            {"label": "One scan, not two", "icon": "barcode", "with": "example"}]}},
    "p11": {"type": "icons", "items": [
        {"label": "Internal", "sub": "Scrap, rework, retest", "icon": "trash", "tone": "bad", "with": 0},
        {"label": "External", "sub": "Returns, warranty", "icon": "box", "tone": "bad", "with": 1},
        {"label": "Hidden", "sub": "Handling, waiting, paperwork", "icon": "clock", "tone": "bad", "with": 2}],
        "then": {"type": "stat", "value": 42, "prefix": "₹", "icon": "wrench", "label": "per rework",
                 "unit": "1,500 reworks a month", "with": "example"}},
    "p12": {"type": "compare", "before": {"label": "Before", "value": 1500}, "after": {"label": "After", "value": 300},
            "unit": "soundbars reworked a month", "note": "FPY 99% · tool reach 22 s → 13 s", "with": 0},
    "p13": {"type": "stat", "value": 4.8, "decimals": 1, "prefix": "₹", "suffix": " lakh", "icon": "chartUp",
            "label": "net benefit, first year", "unit": "₹6 lakh avoided − ₹1.2 lakh for the fix", "with": "example"},
    "p14": {"type": "timeline", "items": [
        {"label": "Standard updated", "sub": "Day 0", "icon": "clipboard", "with": 0},
        {"label": "Audit", "sub": "Day 7", "icon": "search", "with": 2},
        {"label": "Drift caught", "sub": "Day 30", "icon": "warning", "with": "example"},
        {"label": "Audit", "sub": "Day 90", "icon": "check", "tone": "good", "with": 2}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Walk and map", "sub": "Days 1–7", "icon": "walk", "with": 0},
        {"label": "Cause and pilot", "sub": "Days 8–18", "icon": "search", "with": 1},
        {"label": "Prove and hold", "sub": "Days 19–30", "icon": "check", "tone": "good", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A product spends 300 minutes in the plant, but only 30 minutes change it. What is the flow efficiency?",
        "options": ["10%", "30%", "90%"],
        "correct": 0,
        "explanation": "Flow efficiency = value-added time ÷ total lead time = 30 ÷ 300 = 10%. The other 90% is waiting, moving, checking or fixing.",
        "q_script": "Quick check. A product spends three hundred minutes in the plant. Only thirty "
                    "minutes actually change it. What's the flow efficiency? Take a few seconds.",
        "a_script": "It's ten percent. Divide the value-added time by the total lead time. The rest is "
                    "waiting, moving, checking or fixing.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "To cut cycle time, a team proposes removing the final audio test. What should happen?",
        "options": ["Remove it: tests don't change the product",
                    "Keep it unless a risk review approves, and cut the defects it catches",
                    "Move the test to the customer's site"],
        "correct": 1,
        "explanation": "Required quality checks aren't waste to cut on a whim. Keep the test unless a risk review approves a change, and attack the defects behind it. Moving it to the customer only shifts the waste.",
        "q_script": "One more, and this one's a scenario. To cut cycle time, a team wants to remove "
                    "the final audio test. What should happen? Have a think.",
        "a_script": "Keep the test, unless a risk review approves a change. Then attack the defects it "
                    "catches. Moving it to the customer only shifts the waste.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
