"""Uniform Production (Heijunka) lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Kavya, a
production planner on a shared line building phones, set-top boxes and audio
devices.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/uniform_production.py           voice MISSING clips (bootstrap)
  python narration/import_clones.py uniform_production   import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "up"
NAME = "uniform_production"

LETTERS = ["EPEI", "SMED", "WIP"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12, confirmed by the
# user); on-screen text and captions keep the proper spelling.
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = text.replace("TAKT", "tact")
    return re.sub(r"\bHeijunka\b", "Hay-joon-kah", text)


INTRO_SCRIPT = (
    "Monday, three thousand phones. Tuesday, almost nothing. By Wednesday, the test "
    "bench is drowning and the overtime bill is climbing. Sound familiar? In this "
    "lesson, you'll learn uniform production. You'll see how to level "
    "volume and mix, so your line runs at a steady pace it can actually keep. We'll "
    "follow Kavya, a production planner at an electronics plant, as she calms a very "
    "bumpy schedule."
)
OUTRO_SCRIPT = (
    "So, three things to remember. Level both volume and mix, to match real demand. "
    "Check bottlenecks and changeovers before you trust a pattern. And make the plan "
    "visible, with clear rules for when things change. Here's your action for this "
    "week. Find one product you build in a big batch, and sketch a smaller, repeating "
    "pattern. Great work completing this lesson. Next, you'll map your whole value stream."
)

# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What Uniform Production Means",
        "points": [("Leveling — Heijunka", "Uniform production means leveling"),
                   ("Smooth volume and mix", "You smooth both"),
                   ("A steady release pattern", "Irregular orders become"),
                   ("Match real demand, not equal amounts", "But leveling doesn't mean")],
        "example": "Kavya's plant builds phones, boxes and audio devices — in small, repeating sequences, not all phones first.",
        "example_cue": "Kavya's plant builds",
        "script": "Here's the core idea. Uniform production means leveling. Lean calls it "
                  "Heijunka. You smooth both the volume and the mix of what you build, over a set "
                  "period. Irregular orders become a steady release pattern your line can actually "
                  "hit. But leveling doesn't mean "
                  "making equal amounts of everything. It means matching the mix and rate to real "
                  "demand. Kavya's plant builds phones, set-top boxes, and audio devices. Instead "
                  "of all phones first, she plans small, repeating sequences. Why does that matter?",
    },
    {
        "key": "p02", "num": 2, "title": "Why Leveling Matters",
        "points": [("Demand never arrives evenly", "Demand almost never arrives"),
                   ("Chasing spikes: overtime, stock, shaky quality", "If you chase every spike"),
                   ("Leveling smooths within a planning window", "Leveling smooths your releases"),
                   ("You still need some buffer", "you'll still need some buffer")],
        "example": "A big phone order landed on Monday. Kavya spread it across the week, as the delivery date allowed.",
        "example_cue": "Last week, a big phone order",
        "script": "Demand almost never arrives evenly. If you chase every spike, you get "
                  "overtime, piles of finished stock, rushed suppliers, and shaky quality. "
                  "Leveling smooths your releases within an agreed planning window. It won't "
                  "erase demand swings, and you'll still need some buffer. Last week, a big phone "
                  "order landed on Monday. Kavya didn't build it all that day. She spread it "
                  "across the week, because the delivery date allowed it. So what exactly goes "
                  "wrong when work is uneven?",
    },
    {
        "key": "p03", "num": 3, "title": "Mura, Muri & Muda",
        "points": [("Mura: unevenness", "Mura is unevenness"),
                   ("Muri: overburden", "Muri is overburden"),
                   ("Muda: waste", "Muda is waste")],
        "example": "Tester handles ~2,000 units a day; assembly released over 3,000 for test in one day — a queue piled up.",
        "example_cue": "Kavya's functional tester",
        "script": "Lean names three linked problems. Mura is unevenness. Muri is overburden. "
                  "Muda is waste. Here's how they connect. Uneven releases create peaks. Peaks "
                  "overload your people and machines. And overload breeds defects, waiting, and "
                  "extra inventory. Kavya's functional tester handles about two thousand units a "
                  "day. Last month, assembly released over three thousand for testing in one day. Assembly hit "
                  "its plan, but a queue piled up at test. Can you spot that chain on your own line?",
    },
    {
        "key": "p04", "num": 4, "title": "Volume Leveling",
        "points": [("Spread output across a horizon", "Volume leveling spreads"),
                   ("Net demand = demand + end stock − stock", "First, work out net demand"),
                   ("Divide by production days", "Then divide by the production days"),
                   ("Check materials, yield, uptime, staff", "Check materials")],
        "example": "30,000 units of net need over 5 days = a steady 6,000 good units a day.",
        "example_cue": "Kavya's net need",
        "script": "Start with volume. Volume leveling spreads your planned output across a "
                  "sensible horizon. First, work out net demand. That's customer demand, plus the "
                  "stock you want to end with, minus usable stock on hand. Then divide by the "
                  "production days available. Kavya's net need this week is thirty thousand units, "
                  "over five days. That's a steady six thousand good units a day. "
                  "But can your line really hold that? Check materials, yield, uptime, and "
                  "staffing first.",
    },
    {
        "key": "p05", "num": 5, "title": "Mix Leveling",
        "points": [("Small repeating patterns that follow demand", "Mix leveling repeats"),
                   ("Ratio from demand", "That's a three, two, one ratio"),
                   ("Check changeovers, fixtures, parts", "You must check changeovers")],
        "example": "3,000 phones, 2,000 boxes, 1,000 audio → 3 : 2 : 1 → Phone–Box–Phone–Audio–Box–Phone.",
        "example_cue": "Kavya needs three thousand",
        "script": "Now the mix. Mix leveling repeats your products in small patterns that follow "
                  "demand, instead of one big batch each. Kavya needs three thousand phones, two "
                  "thousand boxes, and a thousand audio devices. That's a three, two, one ratio. "
                  "So a six-unit pattern might run phone, box, phone, audio, box, phone. But here's "
                  "the catch. A neat pattern on paper isn't automatically buildable. You must check "
                  "changeovers, fixtures, and parts first. So how fast should the pattern run?",
    },
    {
        "key": "p06", "num": 6, "title": "TAKT Time & Pitch",
        "points": [("TAKT: the pace the customer demands", "TAKT is the pace"),
                   ("Net time ÷ good units required", "Divide your net available"),
                   ("Pitch: time to release one batch", "Pitch is the time"),
                   ("Average TAKT ≠ every model keeps up", "An average TAKT doesn't")],
        "example": "A unit every 4.2 seconds → a 100-unit pitch of 7 minutes.",
        "example_cue": "Kavya's shift needs",
        "script": "That's where TAKT comes in. TAKT is the pace your customer demands. Divide your "
                  "net available time by the good units required. Leveling then sets the practical "
                  "order of releases at that pace. Pitch is the time to release one batch, often a "
                  "hundred units. Kavya's shift needs a unit every four point two seconds. So a "
                  "hundred-unit pitch is seven minutes. But careful. An average TAKT doesn't prove "
                  "every model can keep up. How do you show the plan to the floor?",
    },
    {
        "key": "p07", "num": 7, "title": "The Leveling Box",
        "points": [("A visual schedule", "It's a visual schedule"),
                   ("Time slots across, products down", "Time slots run"),
                   ("Cards: what to release, how many", "Cards in each slot"),
                   ("Misses and shortages visible", "Missed slots")],
        "example": "Every 30 minutes Kavya's board releases the next lot; kits are prepared in that order.",
        "example_cue": "Every thirty minutes",
        "script": "With a leveling box. It's a visual schedule. Time slots run across the columns, "
                  "and products run down the rows. Cards in each slot show what to release, and "
                  "how many. Every thirty minutes, Kavya's board releases the next lot. Kits are "
                  "prepared in that order, not by convenience. Missed slots and shortages become "
                  "obvious at a glance. Here's a quick test for your line. Can an operator see the "
                  "next release, and who to call, without asking anyone?",
    },
    {
        "key": "p08", "num": 8, "title": "EPEI & Changeover",
        "points": [("Small patterns = more changeovers", "Small patterns mean"),
                   ("EPEI: every part every interval", "EPEI measures"),
                   ("SMED: setup outside stopped time", "That's why SMED matters")],
        "example": "6 daily changeovers: 20 → 8 minutes = 72 minutes back every day.",
        "example_cue": "Kavya's six daily changeovers",
        "script": "Small patterns mean more changeovers. EPEI measures how often you make every "
                  "part. It stands for every part every interval. Kavya builds each family once a "
                  "day, so her EPEI is one day. Building each twice a shift responds faster, but "
                  "doubles the changeovers. That's why SMED matters. You move setup work outside "
                  "the stopped time. Kavya's six daily changeovers dropped from twenty minutes to "
                  "eight. That's seventy-two minutes back every day. Where does your line lose time?",
    },
    {
        "key": "p09", "num": 9, "title": "Bottlenecks & Mixed Models",
        "points": [("Leveling can't beat a capacity limit", "Leveling can't overcome"),
                   ("Load stations from the actual mix", "You need to load every station"),
                   ("Don't block the slowest model", "And if she schedules")],
        "example": "40% of units need a 12-second test = about 340 tests/hour vs one tester's ~300. Add a second tester.",
        "example_cue": "Forty percent of units",
        "script": "Here's a hard truth. Leveling can't overcome a real capacity limit. You need to "
                  "load every station from the actual mix, not the average. Kavya checked her test "
                  "area. Forty percent of units need a twelve-second test. That's about three hundred "
                  "and forty tests an hour. One tester gives about three hundred, even before losses. "
                  "So she needs a second tester, whatever the sequence. And if she schedules the "
                  "slowest model in one long block, the tester drowns. Do you know your slowest model?",
    },
    {
        "key": "p10", "num": 10, "title": "Kanban & WIP Control",
        "points": [("Kanban: what to replenish, when", "Kanban signals tell"),
                   ("Standard containers, first-in, first-out lanes", "Standard containers"),
                   ("WIP limits stop overproduction", "WIP limits stop"),
                   ("Kitting matched to pitch and mix", "Match your kitting")],
        "example": "A set-top box kit was short — the team logged it and followed the approved reschedule rule.",
        "example_cue": "Last Tuesday",
        "script": "A level schedule needs steady materials. Kanban signals tell the stores what to "
                  "replenish, and when. Standard containers and first-in, first-out lanes stop the "
                  "line from starving. WIP limits stop upstream from overproducing. Match your "
                  "kitting rhythm to the pitch and the mix. Last Tuesday, a set-top box kit was "
                  "short. Kavya's team didn't quietly swap in a different part. They logged it, "
                  "and followed the approved reschedule rule. What would your team do?",
    },
    {
        "key": "p11", "num": 11, "title": "Handling Demand Changes",
        "points": [("A frozen near-term window", "So you need a planning horizon"),
                   ("Floor rescheduling causes chaos", "Constant rescheduling"),
                   ("Decide who approves changes", "Decide who can approve")],
        "example": "500 audio devices wanted early: Kavya checked due dates, stock, parts and test capacity first.",
        "example_cue": "One morning, a customer",
        "script": "Demand will still change. So you need a planning horizon, and a near-term "
                  "window that's frozen or tightly controlled. Constant rescheduling on the floor "
                  "causes chaos. Decide who can approve a sequence change, and why. One morning, a "
                  "customer asked for five hundred audio devices early. Kavya didn't just jump the "
                  "queue. She checked due dates, finished stock, components, and test capacity "
                  "first. Then she changed the next release slots. Who approves changes on your line?",
    },
    {
        "key": "p12", "num": 12, "title": "Leveling KPIs",
        "points": [("Track output and stability together", "Track output and stability"),
                   ("Schedule adherence", "Schedule adherence compares"),
                   ("WIP days", "WIP days shows"),
                   ("Plus FPY, downtime, overtime", "Add first-pass yield")],
        "example": "95% of scheduled units done. 12,000 units of WIP = 2 days of output.",
        "example_cue": "Kavya's line finished",
        "script": "How do you know leveling is working? Track output and stability together. "
                  "Schedule adherence compares what you completed with what you planned. Kavya's "
                  "line finished ninety-five percent of its scheduled units. WIP days shows how "
                  "long work waits. Her twelve thousand units of WIP is two days of output. "
                  "Add first-pass yield, downtime, and overtime too. Otherwise you might improve "
                  "adherence and quietly hurt quality. Which numbers does your team review each day?",
    },
    {
        "key": "p13", "num": 13, "title": "Case Study: Shared Line",
        "points": [("Mix 3 : 2 : 1, TAKT 4.2 s", "The mix is three"),
                   ("60-unit pattern: 30 · 20 · 10", "She tries a sixty-unit"),
                   ("Check routing, tooling, test limits", "But first she checks"),
                   ("Faster changeovers, no shortcuts", "She sped up changeovers")],
        "example": "One pattern about every four minutes in theory — but her setups were too slow for that pace.",
        "example_cue": "In theory, that's one pattern",
        "script": "Let's put it together on Kavya's shared line. The mix is three to two to one. "
                  "The average TAKT is four point two seconds. She tries a sixty-unit pattern. "
                  "Thirty phones, twenty boxes, and ten audio devices. In theory, that's one pattern "
                  "about every four minutes. But first she checks routing, shared tooling, and each "
                  "product's test limits. Her setups turned out too slow for that pace. So what did "
                  "she do? She sped up changeovers, rather than forcing unsafe shortcuts. Would you?",
    },
    {
        "key": "p14", "num": 14, "title": "Common Mistakes",
        "points": [("Leveling on gross time", "Leveling on gross time"),
                   ("Equal quantities for an unequal mix", "Forcing equal quantities"),
                   ("More output than the line can make", "Scheduling more good output"),
                   ("Skipping first-off checks to catch up", "never skip first-off checks")],
        "example": "Firmware testers down while the board called for boxes: more WIP only moves the bottleneck. Escalate.",
        "example_cue": "One day, Kavya's board",
        "script": "A plan can look level on paper while the floor stays chaotic. Watch for these "
                  "mistakes. Leveling on gross time, and ignoring breaks and losses. Forcing equal "
                  "quantities when your customer's mix isn't equal. Scheduling more good output than "
                  "your line can really make. One day, Kavya's board called for set-top boxes, but "
                  "the firmware testers were down. Releasing more work would only move the "
                  "bottleneck. So she escalated and updated the plan. And never skip first-off "
                  "checks to catch up.",
    },
    {
        "key": "p15", "num": 15, "title": "90-Day Roadmap",
        "points": [("One family, one horizon", "Start small"),
                   ("Days 1–30: demand, mix, TAKT, setups", "In the first thirty days"),
                   ("Days 31–60: pilot board, kitting, changeovers", "In the next thirty"),
                   ("Days 61–90: verify, standardize, expand", "In the last thirty")],
        "example": "Planning sets releases, Production builds, Engineering checks capacity, Quality protects controls, Materials keeps kits ready.",
        "example_cue": "Planning sets releases",
        "script": "Start small, with one product family and one planning horizon. In the first "
                  "thirty days, map demand, mix, TAKT, bottlenecks, and setups. In the next thirty, "
                  "pilot your leveling board, kitting rhythm, and quicker changeovers. In the last "
                  "thirty, verify yield, adherence, and delivery. Then standardize and expand. Give "
                  "everyone a clear role. Planning sets releases, Production builds, and Engineering "
                  "checks capacity. Quality protects controls, and Materials keeps kits ready. Who "
                  "would own your pilot?",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "versus", "items": [
        {"label": "All phones first", "sub": "Then boxes, then audio", "icon": "stack", "with": 1},
        {"label": "Small repeating sequences", "sub": "Matched to real demand", "icon": "sequence", "with": "example"}]},
    "p02": {"type": "icons", "items": [
        {"label": "Demand is uneven", "icon": "wave"}, {"label": "Chasing spikes", "sub": "Overtime, stock", "icon": "clock", "tone": "bad"},
        {"label": "Level the releases", "icon": "sequence"}, {"label": "Some buffer", "icon": "box"}],
        "then": {"type": "versus", "with": "example", "items": [
            {"label": "Build it all Monday", "sub": "Overtime, rushed test", "icon": "stack"},
            {"label": "Spread across the week", "sub": "Due date allowed it", "icon": "calendar"}]}},
    "p03": {"type": "flow", "items": [
        {"label": "Mura", "sub": "Uneven releases make peaks", "icon": "wave", "tone": "bad", "with": 0},
        {"label": "Muri", "sub": "Peaks overload people, machines", "icon": "weight", "tone": "bad", "with": 1},
        {"label": "Muda", "sub": "Defects, waiting, inventory", "icon": "trash", "tone": "bad", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "A queue piles up at test", "unit": "units in one day", "with": "example", "items": [
            {"label": "Tester can do", "value": 2000, "tone": "good", "with": "example"},
            {"label": "Released", "value": 3200, "tone": "bad", "with": "example"}]}},
    "p04": {"type": "icons", "items": [
        {"label": "A sensible horizon", "icon": "calendar"}, {"label": "Net demand", "icon": "count"},
        {"label": "÷ production days", "icon": "sequence"}, {"label": "Check it can hold", "icon": "search"}],
        "then": {"type": "stat", "value": 6000, "icon": "chartUp", "label": "good units a day, every day",
                 "unit": "30,000 units of net need ÷ 5 days", "with": "example"}},
    "p05": {"type": "steps", "items": [
        {"label": "Phone", "sub": "P", "with": "example"}, {"label": "Box", "sub": "B", "with": "example"},
        {"label": "Phone", "sub": "P", "with": "example"}, {"label": "Audio", "sub": "A", "with": "example"},
        {"label": "Box", "sub": "B", "with": "example"}, {"label": "Phone", "sub": "P", "with": "example"}]},
    "p06": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "The customer's pace", "icon": "clock", "with": 0},
        {"label": "Net time ÷ good units", "icon": "count", "with": 1},
        {"label": "Pitch", "sub": "Time to release one batch", "icon": "box", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "One unit every 4.2 s", "icon": "clock", "with": "example"},
            {"label": "× a 100-unit batch", "icon": "box", "with": "example"},
            {"label": "= a 7-minute pitch", "icon": "check", "tone": "good", "with": "example"}]}},
    "p07": {"type": "doc", "items": [
        {"label": "Leveling box · shared line", "icon": "calendar", "with": 0},
        {"label": "08:00  Phone · Box · Phone", "icon": "sequence", "with": 1},
        {"label": "08:30  Audio · Box · Phone", "icon": "sequence", "with": 1},
        {"label": "09:00  Next lot: kits ready", "icon": "box", "with": 2},
        {"label": "Missed slot? Visible at once", "icon": "warning", "with": 3}]},
    "p08": {"type": "icons", "items": [
        {"label": "More changeovers", "icon": "sequence", "with": 0},
        {"label": "EPEI", "sub": "Every part every interval", "icon": "calendar", "with": 1},
        {"label": "SMED", "sub": "Setup outside stopped time", "icon": "wrench", "with": 2}],
        "then": {"type": "compare", "before": {"label": "Before", "value": 20}, "after": {"label": "After SMED", "value": 8},
                 "suffix": " min", "unit": "per changeover, six a day", "note": "72 minutes back every day", "with": "example"}},
    "p09": {"type": "bars", "label": "One tester", "value": 300, "note": "short even before losses: add a second tester", "unit": "tests an hour (40% of units need a 12 s test)", "items": [
        {"label": "Tests needed", "value": 343, "tone": "bad", "with": "example"}]},
    "p10": {"type": "icons", "items": [
        {"label": "Kanban signals", "icon": "label"}, {"label": "FIFO lanes", "icon": "sequence"},
        {"label": "WIP limits", "icon": "stack"}, {"label": "Kitting to the pitch", "icon": "tray"}]},
    "p11": {"type": "icons", "items": [
        {"label": "A frozen window", "icon": "lock", "with": 0},
        {"label": "Floor rescheduling", "sub": "Causes chaos", "icon": "warning", "tone": "bad", "with": 1},
        {"label": "Who approves", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "500 audio wanted early", "icon": "box", "with": "example"},
            {"label": "Check dates, stock, parts, test", "icon": "search", "with": "example"},
            {"label": "Then change the next slots", "icon": "sequence", "tone": "good", "with": "example"}]}},
    "p12": {"type": "icons", "items": [
        {"label": "Output + stability", "icon": "chartUp"}, {"label": "Schedule adherence", "icon": "check"},
        {"label": "WIP days", "icon": "clock"}, {"label": "FPY, downtime, overtime", "icon": "shield"}],
        "then": {"type": "stat", "value": 95, "suffix": "%", "icon": "check", "label": "of scheduled units completed",
                 "unit": "12,000 units of WIP = 2 days of output", "with": "example"}},
    "p13": {"type": "stat", "value": 4.2, "decimals": 1, "suffix": " s", "icon": "clock", "label": "average TAKT, mix 3 : 2 : 1",
            "unit": "phones : set-top boxes : audio", "with": 0,
            "then": {"type": "bars", "label": "", "note": "One pattern about every 4 minutes", "unit": "units in a 60-unit pattern", "with": 1, "items": [
                {"label": "Phones", "value": 30, "with": 1}, {"label": "Boxes", "value": 20, "with": 1},
                {"label": "Audio", "value": 10, "with": 1}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Gross time", "icon": "clock", "tone": "bad"}, {"label": "Equal quantities", "icon": "scale", "tone": "bad"},
        {"label": "Over-planning", "icon": "stack", "tone": "bad"}, {"label": "Skipping first-off", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Demand, mix, TAKT, setups", "sub": "Days 1–30", "icon": "clipboard", "with": 1},
        {"label": "Pilot board, kitting, changeovers", "sub": "31–60", "icon": "calendar", "with": 2},
        {"label": "Verify, standardize, expand", "sub": "61–90", "icon": "chartUp", "with": 3}],
        "then": {"type": "icons", "with": "example", "items": [
            {"label": "Planning", "icon": "calendar", "with": "example"}, {"label": "Production", "icon": "wrench", "with": "example"},
            {"label": "Engineering", "icon": "gear", "with": "example"}, {"label": "Quality", "icon": "shield", "with": "example"},
            {"label": "Materials", "icon": "box", "with": "example"}]}},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p06",
        "question": "Kavya needs 3,000 phones, 2,000 boxes and 1,000 audio devices. Which sequence is mix-leveled?",
        "options": ["All phones, then all boxes, then all audio", "Phone–Box–Phone–Audio–Box–Phone, repeated",
                    "One of each product, in turn"],
        "correct": 1,
        "explanation": "The repeating pattern follows the 3 : 2 : 1 demand ratio. Big batches create peaks; equal quantities ignore the real mix.",
        "q_script": "Quick check. Kavya needs three thousand phones, two thousand boxes, and a "
                    "thousand audio devices. Which sequence is mix-leveled? Take a few seconds.",
        "a_script": "The repeating pattern. Phone, box, phone, audio, box, phone. It follows the "
                    "demand ratio. Equal quantities would ignore the real mix.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "A customer suddenly wants 500 audio devices early. What should Kavya do FIRST?",
        "options": ["Insert them in the very next slot", "Check due dates, stock, parts and test capacity, then change the slots",
                    "Refuse — the schedule is frozen", "Add overtime and build them all today"],
        "correct": 1,
        "explanation": "Check the impact first, then change the next release slots using the agreed rules. Jumping the queue blindly, or refusing outright, both cause trouble.",
        "q_script": "One more, and this one's a scenario. A customer suddenly wants five hundred "
                    "audio devices early. What should Kavya do first? Have a think.",
        "a_script": "Check the impact first. Due dates, finished stock, components, and test "
                    "capacity. Then change the next release slots, using the agreed rules. Jumping "
                    "the queue blindly, or refusing outright, both cause trouble.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
