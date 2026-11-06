"""Value Stream Mapping lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Rahul, an
improvement engineer mapping his plant's set-top box line.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/value_stream.py                 voice MISSING clips (bootstrap)
  python narration/import_clones.py value_stream   import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "vs"
NAME = "value_stream"

LETTERS = ["VSM", "WIP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    return text.replace("TAKT", "tact")


INTRO_SCRIPT = (
    "A set-top box takes fifteen minutes to build and test. Yet it takes almost four "
    "days to reach the customer. Where does all that time go? In this lesson, you'll "
    "learn Value Stream Mapping. You'll see how to draw the real flow of material and "
    "information. Then you'll find the waiting, and design a better future state. We'll follow "
    "Rahul, an improvement engineer, as he maps his plant's set-top box line."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Map the real flow, of both material and information. "
    "Most of your lead time hides in waiting, not in work. And design a future state you "
    "can prove, before you cut any stock. Here's your action for this week. Walk one "
    "product family backwards from dispatch, and count every pile you pass. Great work "
    "completing this lesson. Next, you'll learn Why-Why analysis, to find the real causes."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What a VSM Shows",
        "points": [("One product family, order to delivery", "shows the whole journey"),
                   ("Material and the information driving it", "It includes the material"),
                   ("Value-added work, waiting, inventory", "It shows value-added work"),
                   ("A shared picture of reality", "It's a shared picture")],
        "example": "Rahul follows a set-top box from incoming boards to dispatch — including planning signals and warehouse release.",
        "example_cue": "Rahul follows a set-top box",
        "script": "Here's the core idea. A value stream map shows the whole journey of one product "
                  "family, from customer order to delivery. It includes the material, and the "
                  "information that drives it. It shows value-added work, waiting, piles of "
                  "inventory, and slow signals. It's a shared picture of reality, not a decorative "
                  "flowchart. Rahul follows a set-top box from incoming boards to dispatch. He "
                  "includes planning signals and warehouse release, not just the line. So what "
                  "counts as value for you?",
    },
    {
        "key": "p02", "num": 2, "title": "Value, Flow & Waste",
        "points": [("Value: what the customer would pay for", "Value is what your customer"),
                   ("Needed today, but no value", "Some work adds no value"),
                   ("Pure waste: waiting, transport, rework", "Then there's pure waste")],
        "example": "Rahul's box: 15 minutes built and tested vs 2 days waiting for material release.",
        "example_cue": "Rahul's box spends",
        "script": "Value is what your customer would happily pay for. It changes the product's "
                  "form, fit, or function, right the first time. Some work adds no value but is "
                  "still needed today, like mandatory inspection. Then there's pure waste, like "
                  "waiting, transport, and rework. Rahul's box spends fifteen minutes being built "
                  "and tested. It spends two days waiting for material release. Which would you "
                  "attack first? Seconds of assembly, or days of waiting?",
    },
    {
        "key": "p03", "num": 3, "title": "Product Families & Scope",
        "points": [("Don't map everything at once", "Don't map everything"),
                   ("Family: same steps and equipment", "A product family is"),
                   ("Products × processes grid", "Build a simple grid"),
                   ("Group products that share a route", "Then group the products")],
        "example": "Phones and audio devices share packing but test very differently — so they get separate maps.",
        "example_cue": "Rahul noticed phones",
        "script": "Don't map everything at once. A product family is a group of items that follow "
                  "mostly the same steps and equipment. Mixing unrelated products hides variation, "
                  "and the averages start lying. Build a simple grid, with products down the side "
                  "and processes across the top. Then group the products that share a route. Rahul "
                  "noticed phones and audio devices share packing, but test very differently. So "
                  "they get separate maps. Which family would you map first?",
    },
    {
        "key": "p04", "num": 4, "title": "Symbols & Conventions",
        "points": [("Factory icons: customer and supplier", "Factory icons show"),
                   ("Process boxes + data boxes", "Process boxes show"),
                   ("Triangles: inventory waiting", "Triangles show"),
                   ("Material vs information arrows", "Solid arrows carry")],
        "example": "Kaizen bursts mark ideas; a timeline splits processing from waiting. Always add a legend.",
        "example_cue": "Kaizen bursts mark",
        "script": "Value stream maps use a simple visual language. Factory icons show your customer "
                  "and supplier. Process boxes show operations, with data boxes underneath for cycle "
                  "time, changeover, uptime, and yield. Triangles show inventory waiting. Solid "
                  "arrows carry material, and thinner arrows carry information. Kaizen bursts mark "
                  "ideas for improvement. A timeline along the bottom splits processing from "
                  "waiting. Symbols vary between companies, so always add a legend. Ready to "
                  "collect real data?",
    },
    {
        "key": "p05", "num": 5, "title": "Gemba Walk & Data",
        "points": [("Start at the gemba", "Mapping starts at the gemba"),
                   ("Walk from dispatch back to supplier", "Walk from dispatch"),
                   ("Time real cycles yourself", "Time real cycles"),
                   ("Count WIP at every buffer", "Count the WIP")],
        "example": "Rahul's system showed one number for test WIP, his physical count another. He reconciled them before any math.",
        "example_cue": "Rahul's system showed",
        "script": "Mapping starts at the gemba, where the work actually happens. Walk from dispatch "
                  "back toward the supplier. You'll see the real queues, and whether material is "
                  "pulled or pushed. Time real cycles yourself, several times, instead of trusting "
                  "standard times. Count the WIP at every buffer. Rahul's system showed one number "
                  "for test WIP. His physical count showed another. He reconciled them before doing "
                  "any math. Next, how fast does your customer need you to go?",
    },
    {
        "key": "p06", "num": 6, "title": "Customer Demand & TAKT",
        "points": [("TAKT: the pace your customer needs", "TAKT sets the pace"),
                   ("Net time ÷ good units, same period", "Divide your net available"),
                   ("Compare every station against it", "Now compare every station")],
        "example": "1,200 good boxes in one shift → TAKT 21 seconds, about 170 an hour. A 24-second station can't keep up alone.",
        "example_cue": "Rahul's line runs",
        "script": "TAKT sets the pace your customer needs. Divide your net available time by the "
                  "good units demanded, over the same period. Net time leaves out planned breaks "
                  "and stoppages. Rahul's line runs one shift, and needs twelve hundred good boxes a "
                  "day. That gives a TAKT of twenty-one seconds a unit, or about a hundred and "
                  "seventy an hour. Now compare every station against it. One station runs at "
                  "twenty-four seconds. What does that mean for you? It "
                  "can't keep up, unless a second station runs in parallel.",
    },
    {
        "key": "p07", "num": 7, "title": "The Current-State Map",
        "points": [("Demand on the right, work upstream", "Put customer demand"),
                   ("Data under each box", "Add the data"),
                   ("Draw the information flow", "Then draw the information flow"),
                   ("Check it with your operators", "Finally, ask your operators")],
        "example": "Planning released weekly batches; test could only handle a daily rate — boxes piled up in between.",
        "example_cue": "Rahul's map revealed",
        "script": "Now draw the current state. Put customer demand on the right, then work upstream "
                  "through each process and buffer. Add the data under each box. Then draw the "
                  "information flow. Forecasts, daily schedules, work orders, and Kanban signals. "
                  "Rahul's map revealed a mismatch. Planning released weekly batches to assembly, "
                  "but test could only handle a daily rate. So semi-finished boxes piled up in "
                  "between. Finally, ask your operators. Do the arrows match a normal day?",
    },
    {
        "key": "p08", "num": 8, "title": "Lead Time & Inventory",
        "points": [("Timeline: working vs waiting", "The timeline separates"),
                   ("Waiting = buffer ÷ daily demand", "To estimate waiting"),
                   ("Value-added ratio: a signal, not proof", "That tiny share")],
        "example": "Three buffers at 1,200 a day = 3.5 days of waiting vs 15 minutes of processing.",
        "example_cue": "Rahul has three buffers",
        "script": "The timeline separates working time from waiting time. To estimate waiting, "
                  "divide the inventory at each buffer by daily demand. Rahul has three buffers, "
                  "and demand of twelve hundred a day. Together, they hold three and a half days "
                  "of waiting. The actual processing adds up to just fifteen minutes. Can you see "
                  "the gap? That tiny share is the value-added ratio. Treat it as a signal, not "
                  "proof that all waiting can vanish. So why is that stock there?",
    },
    {
        "key": "p09", "num": 9, "title": "Constraints & Causes",
        "points": [("A map shows where, not why", "A map tells you"),
                   ("Long queues, expediting, rework loops", "Look for long queues"),
                   ("Dig deeper: Pareto, five whys, fishbone", "Then dig deeper")],
        "example": "2,000 boxes waiting at test: too few testers, downtime, firmware or batch releases? Check before buying.",
        "example_cue": "Rahul found two thousand",
        "script": "A map tells you where to look, not why it happens. Look for long queues, "
                  "frequent expediting, and rework loops. Then dig deeper with Pareto charts, five "
                  "whys, or a fishbone. Rahul found two thousand boxes waiting at test. Was it too "
                  "few testers? Downtime? Unstable firmware? Or big batch releases? Each one needs "
                  "a different fix. So he checked the data before anyone bought a new tester. What "
                  "would you check first?",
    },
    {
        "key": "p10", "num": 10, "title": "Future State: Flow & Pull",
        "points": [("Continuous flow at or below TAKT", "Use continuous flow"),
                   ("Capped first-in, first-out lanes", "use a first-in, first-out lane"),
                   ("Supermarket with pull signals", "use a supermarket"),
                   ("One pacemaker process", "Then pick one pacemaker")],
        "example": "Rahul's design: assembly and packing share a capped lane; boards are pulled from a supermarket.",
        "example_cue": "In Rahul's design",
        "script": "Now design the future state. It must be better, and also realistic. Use "
                  "continuous flow wherever steps can run at or below TAKT. Where they can't, use a "
                  "first-in, first-out lane with a hard cap. Where flow can't connect at all, use a "
                  "supermarket with pull signals. Then pick one pacemaker, the single process you "
                  "schedule. In Rahul's design, assembly and packing share a capped lane. Boards "
                  "are pulled from a supermarket. Where could your line flow?",
    },
    {
        "key": "p11", "num": 11, "title": "Pitch, Kanban & Refill",
        "points": [("Pitch = TAKT × pack quantity", "Pitch is the rhythm"),
                   ("Kanban size: lead time and demand", "Kanban sizes depend"),
                   ("Prove replenishment before cutting stock", "Prove replenishment works")],
        "example": "Packs of 20 → a 7-minute pitch. A kit lasts 6 minutes but a refill takes 12: more kits, or a faster refill.",
        "example_cue": "Rahul's packs hold",
        "script": "Leveling makes pull signals predictable. Pitch is the rhythm for moving one "
                  "standard pack. It's TAKT times the pack quantity. Rahul's packs hold twenty "
                  "boxes, so his pitch is seven minutes. Kanban sizes depend on replenishment lead "
                  "time and demand. One kit lasts six minutes, but a refill takes twelve. So he "
                  "needs more kits, or a faster refill. Here's the rule for you. Prove "
                  "replenishment works before you cut any stock. Ready for the whole case?",
    },
    {
        "key": "p12", "num": 12, "title": "Worked Case Study",
        "points": [("1,200 boxes a day; 4,200 waiting", "Demand is twelve hundred"),
                   ("3.5 days of queue time", "That's three and a half days"),
                   ("Future state: buffers halved", "His future state halves"),
                   ("Validate capacity, material, quality first", "Can test capacity")],
        "example": "Queue time falls to under two days — a 50% cut. But he doesn't flip the switch yet.",
        "example_cue": "Queue time falls",
        "script": "Here's Rahul's case, with training numbers. Demand is twelve hundred boxes a "
                  "day. Today, forty-two hundred units wait across three buffers. That's three and "
                  "a half days of queue time. His future state halves every buffer, to twenty-one "
                  "hundred units. Queue time falls to under two days. That's a fifty percent cut. "
                  "But he doesn't flip the switch yet. Can test capacity, material delivery, and "
                  "quality controls cope with less buffer? How would you check?",
    },
    {
        "key": "p13", "num": 13, "title": "KPIs & Real Benefits",
        "points": [("Measure the whole flow", "Measure the whole flow"),
                   ("Lead time, WIP, delivery, FPY", "Track lead time"),
                   ("Baseline, then verify for weeks", "Set a baseline"),
                   ("Watch for stock that just moved", "Watch for stock")],
        "example": "Lower WIP frees about ₹31 lakh of inventory — cash released once, not profit every year.",
        "example_cue": "Rahul's lower WIP",
        "script": "Measure the whole flow, not just station speed. Track lead time, WIP, on-time "
                  "delivery, and first-pass yield. Set a baseline, then verify over several "
                  "representative weeks. Watch for stock that simply moved somewhere else. Here's "
                  "a money trap. Rahul's lower WIP frees about thirty-one lakh rupees of inventory. "
                  "That's cash released once. It isn't thirty-one lakh of profit every year. Would "
                  "your finance team spot the difference? Report it honestly.",
    },
    {
        "key": "p14", "num": 14, "title": "Governance & 90 Days",
        "points": [("Every function has a role", "Value stream improvement needs"),
                   ("Days 1–30: pick family, map current", "In the first thirty days"),
                   ("Days 31–60: design future, pilot pull", "In the next thirty"),
                   ("Days 61–90: stabilize, audit, scale", "In the last thirty")],
        "example": "Rahul fixed the test bottleneck before cutting its buffer — otherwise the line starves.",
        "example_cue": "Rahul fixed the test bottleneck",
        "script": "Value stream improvement needs every function. Planning owns the schedule logic. "
                  "Production owns flow, Quality owns controls, and Materials owns replenishment. "
                  "Management removes barriers. In the first thirty days, pick the family and map "
                  "the current state. In the next thirty, design the future state and pilot pull "
                  "changes. In the last thirty, stabilize, audit, and scale. Rahul fixed the test "
                  "bottleneck before cutting its buffer. Otherwise, the line starves. What would "
                  "your first pilot be?",
    },
    {
        "key": "p15", "num": 15, "title": "Do's, Don'ts & Template",
        "points": [("Update when demand or routing changes", "Update it when"),
                   ("Map real flow, involve operators", "So do map the real flow"),
                   ("Cycle time ≠ lead time", "don't confuse cycle time"),
                   ("Check capacity before removing buffers", "don't remove buffers")],
        "example": "A map with only process boxes isn't a value stream map. It's just a flowchart.",
        "example_cue": "A map with only process boxes",
        "script": "A good map is a living decision tool. Update it when demand, routing, or major "
                  "constraints change. So do map the real flow, with consistent units, and involve "
                  "your operators. Do show rework paths and planning signals. But don't confuse "
                  "cycle time with lead time. Don't call a one-time cash release a yearly saving. "
                  "And don't remove buffers before you've checked capacity and replenishment. A map "
                  "with only process boxes isn't a value stream map. It's just a flowchart.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "One product family", "icon": "box"}, {"label": "Material + information", "icon": "sequence"},
        {"label": "Work vs waiting", "icon": "clock"}, {"label": "A shared picture", "icon": "person"}]},
    "p02": {"type": "versus", "items": [
        {"label": "2 days waiting", "sub": "for material release", "icon": "clock", "with": "example"},
        {"label": "15 minutes of real work", "sub": "built and tested", "icon": "wrench", "with": "example"}]},
    "p03": {"type": "matrix", "prefix": "check", "cols": ["Assembly", "Phone test", "Audio test", "Packing"],
            "note": "Same packing, different test: separate maps", "items": [
        {"label": "Phones", "cells": [3, 3, None, 3], "with": 2},
        {"label": "Audio", "cells": [3, None, 3, 3], "with": 3}]},
    "p04": {"type": "icons", "items": [
        {"label": "Customer, supplier", "icon": "box"}, {"label": "Process + data boxes", "icon": "clipboard"},
        {"label": "Triangles: inventory", "icon": "stack"}, {"label": "Material vs information", "icon": "sequence"}]},
    "p05": {"type": "flow", "items": [
        {"label": "Go to the gemba", "icon": "walk"},
        {"label": "Walk back from dispatch", "icon": "sequence"},
        {"label": "Time real cycles", "icon": "clock"},
        {"label": "Count every buffer", "sub": "Reconcile with the system", "icon": "count", "tone": "good"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "The customer's pace", "icon": "clock", "with": 0},
        {"label": "Net time ÷ good units", "icon": "count", "with": 1},
        {"label": "Compare every station", "icon": "scale", "with": 2}],
        "then": {"type": "bars", "label": "TAKT", "value": 21, "suffix": " s", "note": "can't keep up alone",
                 "unit": "1,200 good boxes a shift ≈ 170 an hour", "with": "example", "items": [
            {"label": "One station", "value": 24, "tone": "bad", "with": "example"}]}},
    "p07": {"type": "flow", "items": [
        {"label": "Planning: weekly batches", "icon": "calendar", "with": "example"},
        {"label": "Boxes pile up", "sub": "Semi-finished, waiting", "icon": "stack", "tone": "bad", "with": "example"},
        {"label": "Test: a daily rate", "icon": "test", "with": "example"}]},
    "p08": {"type": "icons", "items": [
        {"label": "Working vs waiting", "icon": "clock", "with": 0},
        {"label": "Buffer ÷ daily demand", "icon": "count", "with": 1},
        {"label": "Value-added ratio", "sub": "A signal, not proof", "icon": "search", "with": 2}],
        "then": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " days", "icon": "clock", "label": "of waiting",
                 "unit": "vs just 15 minutes of processing", "with": "example"}},
    "p09": {"type": "flow", "items": [
        {"label": "A map shows where, not why", "icon": "search", "with": 0},
        {"label": "Queues, expediting, rework", "icon": "stack", "with": 1},
        {"label": "Pareto, five whys, fishbone", "icon": "gear", "with": 2}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Too few testers?", "icon": "test", "with": "example"},
            {"label": "Downtime?", "icon": "clock", "with": "example"},
            {"label": "Firmware?", "icon": "chip", "with": "example"},
            {"label": "Batch releases?", "icon": "stack", "with": "example"}]}},
    "p10": {"type": "flow", "items": [
        {"label": "Boards pulled from a supermarket", "icon": "tray"},
        {"label": "Assembly", "icon": "wrench"},
        {"label": "A capped FIFO lane", "icon": "sequence"},
        {"label": "Packing: the pacemaker", "icon": "box", "tone": "good"}]},
    "p11": {"type": "icons", "items": [
        {"label": "Pitch = TAKT × pack", "icon": "count", "with": 0},
        {"label": "Kanban size", "icon": "label", "with": 1},
        {"label": "Prove the refill", "icon": "check", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "Packs of 20: a 7-minute pitch", "icon": "box", "with": "example"},
            {"label": "A kit lasts 6 min; a refill takes 12", "icon": "clock", "tone": "bad", "with": "example"},
            {"label": "More kits, or a faster refill", "icon": "check", "tone": "good", "with": "example"}]}},
    "p12": {"type": "stat", "value": 3.5, "decimals": 1, "suffix": " days", "icon": "clock", "label": "of queue time today",
            "unit": "4,200 units waiting ÷ 1,200 a day", "with": 1,
            "then": {"type": "compare", "before": {"label": "Today", "value": 4200}, "after": {"label": "Future state", "value": 2100},
                     "unit": "units waiting across three buffers", "note": "Queue time cut by half (planned)", "with": 2}},
    "p13": {"type": "icons", "items": [
        {"label": "The whole flow", "icon": "sequence"}, {"label": "Lead time, WIP, delivery, FPY", "icon": "chartUp"},
        {"label": "Baseline, then weeks", "icon": "calendar"}, {"label": "Stock that just moved", "icon": "stack", "tone": "bad"}],
        "then": {"type": "stat", "value": 31, "prefix": "₹", "suffix": " lakh", "icon": "box", "label": "of inventory freed",
                 "unit": "Cash released once: not profit every year", "with": "example"}},
    "p14": {"type": "timeline", "items": [
        {"label": "Pick the family, map current", "sub": "Days 1–30", "icon": "search", "with": 1},
        {"label": "Design future, pilot pull", "sub": "31–60", "icon": "sequence", "with": 2},
        {"label": "Stabilize, audit, scale", "sub": "61–90", "icon": "chartUp", "with": 3}]},
    "p15": {"type": "icons", "items": [
        {"label": "Update when things change", "icon": "sequence", "tone": "good"},
        {"label": "Real flow, with operators", "icon": "person", "tone": "good"},
        {"label": "Cycle ≠ lead time", "icon": "cross", "tone": "bad"},
        {"label": "Capacity before cutting buffers", "icon": "warning", "tone": "bad"}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A buffer holds 2,400 units and demand is 1,200 a day. How many days of inventory is that?",
        "options": ["Half a day", "2 days", "1,200 days"],
        "correct": 1,
        "explanation": "Inventory days = units waiting ÷ daily demand = 2,400 ÷ 1,200 = 2 days.",
        "q_script": "Quick check. A buffer holds twenty-four hundred units, and demand is twelve "
                    "hundred a day. How many days of inventory is that? Take a few seconds.",
        "a_script": "Two days. Divide the units waiting by the daily demand. The buffer holds "
                    "exactly two days of output.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Rahul finds 2,000 boxes waiting at test. What should the team do FIRST?",
        "options": ["Buy another tester right away", "Confirm the cause: capacity, downtime, firmware or batch release",
                    "Cut the buffer in half to force flow"],
        "correct": 1,
        "explanation": "A map shows where to look, not why. Confirm the mechanism first; buying a tester or cutting the buffer blindly may fix nothing, or starve the line.",
        "q_script": "One more, and this one's a scenario. Rahul finds two thousand boxes waiting "
                    "at test. What should the team do first? Have a think.",
        "a_script": "Confirm the cause first. It could be capacity, downtime, firmware, or big "
                    "batch releases. Buying a tester or cutting the buffer blindly may fix nothing, "
                    "or starve the line.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
