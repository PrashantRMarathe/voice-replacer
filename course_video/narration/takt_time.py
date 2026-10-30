"""TAKT Time lesson DATA: 15 pages + 2 quizzes + intro/outro.

Follows the script style guide (docs/PLAYBOOK.md §4b). Story thread: Rohan,
a planning engineer at a network-camera plant that must ship 7,200 good
cameras a day across three shifts (TAKT 10 s), and a final-test constraint.

VOICE-ONLY. The pipeline (edge-tts bootstrap, clone import, timings,
captions, quizzes) lives in lesson_lib.py:

  python narration/takt_time.py                voice MISSING clips (bootstrap)
  python narration/import_clones.py takt_time  import the cloned voice
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lesson_lib  # noqa: E402

ID = "tt"
NAME = "takt_time"

LETTERS = ["UPH", "UPPH", "WIP", "FPY", "SOP", "SMED"]


# Pronunciation fixes for the voice only (PLAYBOOK §4b rule 12); on-screen text
# and captions keep the proper spelling. TAKT = "tact" (confirmed).
def say(text: str) -> str:
    text = re.sub(r"\b(" + "|".join(LETTERS) + r")(s?)\b",
                  lambda m: "-".join(m.group(1)) + m.group(2), text)
    text = text.replace("TAKT", "tact")
    return re.sub(r"\bHeijunka\b", "Hay-joon-kah", text)


INTRO_SCRIPT = (
    "Every machine on Rohan's camera line looked busy. Upstream stations were racing. Yet "
    "dispatch kept missing the truck. How can a busy line still be late? In this lesson, "
    "you'll learn TAKT time, the beat your customer sets. You'll see how to calculate it "
    "correctly, and use it to balance, staff and run your line. We'll follow Rohan, a "
    "planning engineer at a camera plant."
)
OUTRO_SCRIPT = (
    "So, three things to remember. TAKT is net available time divided by customer demand. "
    "It's the pace you need, not the time a station actually takes. And plan for real "
    "losses, like downtime and yield, not theoretical speed. Here's your action for this "
    "week. Calculate the TAKT for one of your lines, and compare it with your slowest "
    "station. Great work completing this lesson. Next, you'll learn Uniform Production."
)

# One story thread: Rohan's network-camera plant. 7,200 good cameras/day, 1,200 net
# minutes/day over three shifts -> TAKT 10 s; final test 18 s per unit is the constraint.
# Each page: title, 2-4 on-screen points (text, cue = the phrase in the script where
# the box appears), a worked example (+ example_cue) and the spoken script.
PAGES = [
    {
        "key": "p01", "num": 1, "title": "What TAKT Time Is",
        "points": [("Takt: German for beat, or rhythm", "TAKT comes from"),
                   ("The pace that meets customer demand", "It's the pace"),
                   ("TAKT = net available time ÷ demand", "Divide your net")],
        "example": "420 net minutes ÷ 840 cameras = one camera every 30 seconds.",
        "example_cue": "Say a shift has",
        "script": "Here's the core idea. TAKT comes from the German word for beat, or rhythm. "
                  "It's the pace at which you must finish units to meet customer demand. The "
                  "formula is simple. Divide your net available time by the demand. Say a shift "
                  "has four hundred and twenty minutes. The customer needs eight hundred and "
                  "forty cameras. That's one camera every thirty seconds. Is that the time an "
                  "operator actually takes? No.",
    },
    {
        "key": "p02", "num": 2, "title": "Why TAKT Matters",
        "points": [("Links your customer to the shop floor", "TAKT connects your customer"),
                   ("No shared pace → overproduction, WIP", "Without a shared pace"),
                   ("Plan staffing, balance work, pace materials", "TAKT helps you plan")],
        "example": "Rohan's assembly built 1,000 cameras ahead of test. Utilization looked great; the trucks still left late.",
        "example_cue": "His assembly built",
        "script": "TAKT connects your customer to the shop floor. Without a shared pace, early "
                  "stations overproduce, and WIP piles up. Shortages hide, and dispatch becomes "
                  "a scramble. That's exactly what happened to Rohan. His assembly built a "
                  "thousand cameras ahead of test. Utilization looked great. But the trucks "
                  "still left late. TAKT helps you plan staffing, balance work, and pace "
                  "materials. But first, you need the right numbers. Where do you start?",
    },
    {
        "key": "p03", "num": 3, "title": "Net Available Time",
        "points": [("Start with shift length", "Take your shift length"),
                   ("Subtract planned breaks, meetings, cleaning", "Then subtract planned"),
                   ("Don't subtract random downtime here", "don't subtract random downtime"),
                   ("Write down your assumptions", "write down your assumptions")],
        "example": "480 min shift − breaks − a short meeting = 430 net minutes.",
        "example_cue": "An eight-hour shift",
        "script": "Start with net available time. Take your shift length. Then subtract planned "
                  "breaks, meetings and planned cleaning. An eight-hour shift is four hundred and "
                  "eighty minutes. Take off breaks and a short meeting, and you get four hundred "
                  "and thirty. But don't subtract random downtime here. That's a loss you handle "
                  "when you check capacity. Be consistent, and write down your assumptions. What "
                  "about the other half of the formula?",
    },
    {
        "key": "p04", "num": 4, "title": "Customer Demand",
        "points": [("Demand and time: same period", "The demand must cover"),
                   ("Good units needed, not units started", "Use the good units"),
                   ("Mixed models: check each one", "On a mixed-model line"),
                   ("Recalculate when demand or shifts change", "recalculate whenever")],
        "example": "Daily demand with one shift's time = nonsense.",
        "example_cue": "Mixing daily demand",
        "script": "The demand must cover the same period as your time. If you use daily demand, "
                  "use daily net time too. Mixing daily demand with one shift's time gives you "
                  "nonsense. Use the good units your customer needs, not the units you start. On "
                  "a mixed-model line, the total TAKT is a guide. But each model still needs its "
                  "own capacity check. And recalculate whenever demand or shifts change. So how "
                  "is TAKT different from cycle time?",
    },
    {
        "key": "p05", "num": 5, "title": "TAKT vs Cycle vs Lead Time",
        "points": [("TAKT: the pace you need", "TAKT is the pace you need"),
                   ("Cycle time: what a station takes", "Cycle time is"),
                   ("Lead time: the whole journey", "Lead time is"),
                   ("Cycle > TAKT = can't keep up", "If your cycle time")],
        "example": "One of Rohan's lines: final test 38 s vs TAKT 30 s. It needed improvement, or a second tester.",
        "example_cue": "On one of Rohan's lines",
        "script": "Here's the most common mix-up. TAKT is the pace you need. Cycle time is what a "
                  "station actually takes, measured on the floor. Lead time is the whole journey, "
                  "including waiting and moving. If your cycle time is longer than TAKT, that "
                  "station can't keep up. On one of Rohan's lines, final test took thirty-eight seconds, against a "
                  "TAKT of thirty. It needed improvement, or a second tester. Always define your "
                  "start and end points first.",
    },
    {
        "key": "p06", "num": 6, "title": "Pitch, UPH and UPPH",
        "points": [("UPH: the hourly rate you need", "Units per hour"),
                   ("Pitch: time to fill one pack", "Pitch is"),
                   ("UPPH: good output per person-hour", "UPPH measures"),
                   ("Theory isn't output", "theory isn't output")],
        "example": "TAKT 24 s → 150 units an hour. Pack of 20 → a pitch of 8 minutes.",
        "example_cue": "With a TAKT of",
        "script": "TAKT links to a few other useful numbers. Units per hour, or UPH, is the hourly "
                  "rate you need. Pitch is the time to fill one standard pack. With a TAKT of "
                  "twenty-four seconds, you need a hundred and fifty units an hour. A pack of "
                  "twenty gives a pitch of eight minutes. UPPH measures good output per person "
                  "hour. But remember, theory isn't output. Real throughput depends on uptime and "
                  "yield. So how do you balance the work?",
    },
    {
        "key": "p07", "num": 7, "title": "Balancing with Yamazumi",
        "points": [("Time each work element", "Break each job"),
                   ("Stack each operator's work as a bar", "Stack each operator's"),
                   ("Draw the TAKT line across", "Then draw the TAKT line"),
                   ("Move or redesign within safety & skill", "So you move or redesign")],
        "example": "TAKT 40 s: Operator A has 52 s of work, Operator B only 25 s.",
        "example_cue": "On one of Rohan's cells",
        "script": "You use a Yamazumi chart. Break each job into repeatable work elements, and "
                  "time them. Stack each operator's work as a bar. Then draw the TAKT line "
                  "across. Any bar above the line is overloaded. On one of Rohan's cells, TAKT "
                  "was forty seconds. Operator A had fifty-two seconds of work. Operator B had "
                  "only twenty-five. So you move or redesign tasks, within safety and skill "
                  "limits. How many people do you need?",
    },
    {
        "key": "p08", "num": 8, "title": "Minimum Operators",
        "points": [("Work content ÷ TAKT, round up", "Divide the total manual"),
                   ("A starting point only", "treat that as a starting point"),
                   ("Use a stable time study", "Use a stable time study")],
        "example": "310 s of work ÷ 40 s TAKT = 7.75 → at least 8 operators.",
        "example_cue": "Rohan's cell had",
        "script": "Here's a quick estimate. Divide the total manual work content by TAKT, then "
                  "round up. Rohan's cell had three hundred and ten seconds of work per camera. "
                  "With a TAKT of forty, that's seven point seven five. So you need at least eight "
                  "operators. But treat that as a starting point. Walking, replenishment, quality "
                  "checks and skill levels all matter. Use a stable time study, not one best-case "
                  "cycle. What limits your output?",
    },
    {
        "key": "p09", "num": 9, "title": "Bottlenecks & Parallel Stations",
        "points": [("The bottleneck limits good output", "It's the step that limits"),
                   ("Capacity = 3,600 ÷ cycle time", "One station's hourly capacity"),
                   ("Apply uptime and first pass yield", "Apply uptime"),
                   ("Evidence before buying a machine", "Check the evidence")],
        "example": "Two testers at 50 s = 144 attempts an hour → about 127 good units after uptime and yield.",
        "example_cue": "Two testers at fifty",
        "script": "The bottleneck does. It's the step that limits your good output. One station's "
                  "hourly capacity is thirty-six hundred seconds, divided by its cycle time. "
                  "Two testers at fifty seconds each give a hundred and forty-four attempts an "
                  "hour. But testers stop, and some units fail. Apply uptime and first pass "
                  "yield, and you get about a hundred and twenty-seven good units. Check the "
                  "evidence before you buy another machine. What about mixed models?",
    },
    {
        "key": "p10", "num": 10, "title": "Mixed Models & Heijunka",
        "points": [("One TAKT doesn't fit every model", "A single TAKT"),
                   ("Check each model's station times", "So check each model's"),
                   ("Heijunka: level volume and mix", "Use Heijunka"),
                   ("SMED: cut changeover losses", "use SMED")],
        "example": "60% Model A, 40% Model B with a longer test: schedule all the Bs together and test drowns.",
        "example_cue": "Say sixty percent",
        "script": "A single TAKT doesn't guarantee every model fits. Say sixty percent of Rohan's "
                  "demand is Model A, and forty percent is Model B. Model B needs a longer test. "
                  "If the plan schedules all the Bs together, test drowns, even though the "
                  "average looks fine. So check each model's station times. Use Heijunka to "
                  "level the volume and the mix. And use SMED to cut your changeover losses. "
                  "What about materials?",
    },
    {
        "key": "p11", "num": 11, "title": "Material Flow & Kanban",
        "points": [("TAKT sets the material rhythm", "TAKT also sets"),
                   ("Kanban: lead time, container size", "Kanban quantities"),
                   ("WIP limits between processes", "Set WIP limits"),
                   ("Don't release work just to stay busy", "Don't release new work")],
        "example": "TAKT 30 s, tote of 40 → lasts 20 minutes; replenishment must beat that.",
        "example_cue": "With a thirty-second TAKT",
        "script": "TAKT also sets the rhythm for material. With a thirty-second TAKT, a tote of "
                  "forty parts lasts twenty minutes. So replenishment must arrive before it "
                  "runs out, with some protection for variation. Kanban quantities also depend "
                  "on lead time and container size. Set WIP limits between processes. And here's "
                  "a hard rule. Don't release new work orders just to keep every station busy. "
                  "So how do you run the day?",
    },
    {
        "key": "p12", "num": 12, "title": "Hourly Plan vs Actual",
        "points": [("Planned = net seconds ÷ TAKT", "Planned units equal"),
                   ("Compare actual with plan", "Say you make"),
                   ("Record why: downtime, rejects, material", "Now record why"),
                   ("Don't blame operator speed", "Don't blame every shortfall")],
        "example": "TAKT 30 s → 120 planned an hour. Made 108 = 90%, a gap of 12.",
        "example_cue": "With a thirty-second TAKT",
        "script": "Use an hourly plan versus actual board. Planned units equal the net seconds "
                  "in the hour, divided by TAKT. With a thirty-second TAKT, you plan a hundred "
                  "and twenty good cameras. Say you make a hundred and eight. That's ninety "
                  "percent, and a gap of twelve. Now record why. Downtime, rejects, material, or "
                  "staffing. Don't blame every shortfall on operator speed. Ready for Rohan's "
                  "full case?",
    },
    {
        "key": "p13", "num": 13, "title": "Case Study: Camera Plant",
        "points": [("7,200 good cameras a day, 1,200 net min", "Rohan's plant must ship"),
                   ("TAKT = 10 seconds", "So TAKT is ten seconds"),
                   ("Test takes 18 s — the constraint", "But test takes"),
                   ("Two testers ≈ 353 good/hour vs 360", "Two testers give")],
        "example": "2 testers = 400 attempts/hour on paper → ≈ 353 good with real uptime and yield. Target: 360.",
        "example_cue": "With real uptime",
        "script": "Rohan's plant must ship seven thousand two hundred good cameras a day. It has "
                  "twelve hundred net minutes, across three shifts. So TAKT is ten seconds. The "
                  "lens and assembly stations are faster than that. But test takes eighteen "
                  "seconds. Two testers give four hundred attempts an hour on paper. With real "
                  "uptime and yield, that's about three hundred and fifty-three good units. The "
                  "target is three sixty. What would you do?",
    },
    {
        "key": "p14", "num": 14, "title": "Common Mistakes",
        "points": [("DO use approved demand & net time", "Do use approved demand"),
                   ("DO update TAKT when things change", "Do update TAKT"),
                   ("DON'T confuse it with cycle time", "Don't confuse it"),
                   ("DON'T skip tests, steps or breaks", "never chase speed")],
        "example": "Rohan improved tester uptime and trimmed the test cycle before buying a third tester.",
        "example_cue": "Rohan improved tester uptime",
        "script": "Rohan improved tester uptime, and trimmed the test cycle, before buying a "
                  "third tester. Now, watch for common mistakes. Do use approved demand and the "
                  "correct net time. Do update TAKT when demand or shifts change. Don't confuse "
                  "it with cycle time. Don't use gross shift hours. And never chase speed by "
                  "skipping tests, SOP steps or breaks. Can your leaders explain the numbers "
                  "behind the TAKT on your board?",
    },
    {
        "key": "p15", "num": 15, "title": "90-Day Roadmap",
        "points": [("Days 1–30: demand, net time, cycle times", "In the first thirty days"),
                   ("Days 31–60: Yamazumi, hourly boards", "In the next thirty"),
                   ("Days 61–90: verify output & yield, scale", "In the last thirty"),
                   ("Aim: reliable good output", "Remember the goal")],
        "example": "Reliable good output at the customer's pace — not keeping every station busy.",
        "example_cue": "It's reliable good output",
        "script": "Start with one representative line in your plant. In the first thirty days, collect demand, "
                  "net time and real cycle times, and map the current balance. In the next "
                  "thirty, pilot Yamazumi, standard work and hourly boards. Tackle the "
                  "bottleneck. In the last thirty, verify output and yield, train backups, and "
                  "scale up. Remember the goal. It's reliable good output at the customer's "
                  "pace. Not keeping every station busy.",
    },
]

# The picture beside each page's boxes (src/components/PageVisual.tsx). Items
# appear with their box: `with` = box index or "example".
VISUALS = {
    "p01": {"type": "icons", "items": [
        {"label": "Takt = beat", "icon": "wave", "with": 0}, {"label": "The pace demand sets", "icon": "clock", "with": 1},
        {"label": "Net time ÷ demand", "icon": "count", "with": 2}],
        "then": {"type": "stat", "value": 30, "suffix": " s", "icon": "camera", "label": "one camera every 30 seconds",
                 "unit": "420 net minutes ÷ 840 cameras", "with": "example"}},
    "p02": {"type": "versus", "items": [
        {"label": "1,000 built ahead of test", "sub": "Busy stations, late trucks", "icon": "stack", "with": "example"},
        {"label": "One shared pace", "sub": "Staffing, balance, materials", "icon": "clock", "with": 2}]},
    "p03": {"type": "flow", "items": [
        {"label": "480 min shift", "icon": "clock", "with": 0},
        {"label": "− breaks, meeting, cleaning", "icon": "calendar", "with": 1},
        {"label": "= 430 net minutes", "sub": "Random downtime is not taken off here", "icon": "check", "tone": "good", "with": "example"}]},
    "p04": {"type": "versus", "items": [
        {"label": "Daily demand ÷ one shift", "sub": "Gives nonsense", "icon": "cross", "with": "example"},
        {"label": "Same period for both", "sub": "Good units, not units started", "icon": "calendar", "with": 0}]},
    "p05": {"type": "icons", "items": [
        {"label": "TAKT", "sub": "The pace you need", "icon": "clock", "with": 0},
        {"label": "Cycle time", "sub": "What a station takes", "icon": "gear", "with": 1},
        {"label": "Lead time", "sub": "The whole journey", "icon": "sequence", "with": 2}],
        "then": {"type": "bars", "label": "", "note": "Test can't keep up: improve it, or add a tester", "unit": "seconds per camera", "with": "example", "items": [
            {"label": "TAKT", "value": 30, "tone": "good", "with": "example"},
            {"label": "Final test", "value": 38, "tone": "bad", "with": "example"}]}},
    "p06": {"type": "icons", "items": [
        {"label": "UPH", "sub": "Hourly rate needed", "icon": "chartUp", "with": 0},
        {"label": "Pitch", "sub": "Time to fill a pack", "icon": "box", "with": 1},
        {"label": "UPPH", "sub": "Good output per person-hour", "icon": "person", "with": 2}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "TAKT 24 s", "icon": "clock", "with": "example"},
            {"label": "= 150 units an hour", "icon": "chartUp", "with": "example"},
            {"label": "Pack of 20 = pitch of 8 min", "icon": "box", "tone": "good", "with": "example"}]}},
    "p07": {"type": "icons", "items": [
        {"label": "Time each element", "icon": "clock"}, {"label": "Stack each operator", "icon": "stack"},
        {"label": "Draw the TAKT line", "icon": "sequence"}, {"label": "Move work, safely", "icon": "person"}],
        "then": {"type": "bars", "label": "TAKT", "value": 40, "suffix": " s", "note": "A is overloaded", "unit": "seconds of work per operator", "with": "example", "items": [
            {"label": "Operator A", "value": 52, "tone": "bad", "with": "example"},
            {"label": "Operator B", "value": 25, "with": "example"}]}},
    "p08": {"type": "icons", "items": [
        {"label": "Work ÷ TAKT, round up", "icon": "count", "with": 0},
        {"label": "A starting point", "icon": "sequence", "with": 1},
        {"label": "Stable time study", "icon": "clock", "with": 2}],
        "then": {"type": "stat", "value": 8, "icon": "person", "label": "operators, at least",
                 "unit": "310 s of work ÷ 40 s TAKT = 7.75, rounded up", "with": "example"}},
    "p09": {"type": "icons", "items": [
        {"label": "The bottleneck", "icon": "warning", "tone": "bad"}, {"label": "3,600 ÷ cycle time", "icon": "count"},
        {"label": "Uptime × yield", "icon": "chartUp"}, {"label": "Evidence first", "icon": "search"}],
        "then": {"type": "flow", "with": "example", "items": [
            {"label": "2 testers at 50 s", "icon": "test", "with": "example"},
            {"label": "144 attempts an hour", "icon": "count", "with": "example"},
            {"label": "≈ 127 good after uptime, yield", "icon": "check", "tone": "good", "with": "example"}]}},
    "p10": {"type": "versus", "items": [
        {"label": "All the Bs together", "sub": "Test drowns", "icon": "stack", "with": "example"},
        {"label": "Level the mix", "sub": "Heijunka + SMED", "icon": "sequence", "with": 2}]},
    "p11": {"type": "stat", "value": 20, "suffix": " min", "icon": "box", "label": "a tote of 40 parts lasts",
            "unit": "at a 30 s TAKT: replenishment must beat it", "with": "example"},
    "p12": {"type": "bars", "label": "", "note": "90%: a gap of 12. Record why.", "unit": "good cameras in one hour, TAKT 30 s", "items": [
        {"label": "Planned", "value": 120, "with": "example"},
        {"label": "Made", "value": 108, "tone": "bad", "with": "example"}]},
    "p13": {"type": "stat", "value": 10, "suffix": " s", "icon": "clock", "label": "TAKT for 7,200 good cameras a day",
            "unit": "1,200 net minutes ÷ 7,200 cameras", "with": 1,
            "then": {"type": "bars", "label": "Target", "value": 360, "unit": "good cameras an hour, two testers", "with": 3, "items": [
                {"label": "On paper", "value": 400, "with": 3},
                {"label": "Real", "value": 353, "tone": "bad", "with": 3}]}},
    "p14": {"type": "icons", "items": [
        {"label": "Approved demand + net time", "icon": "check", "tone": "good"},
        {"label": "Update when things change", "icon": "sequence", "tone": "good"},
        {"label": "Not cycle time", "icon": "cross", "tone": "bad"},
        {"label": "Never skip tests or breaks", "icon": "warning", "tone": "bad"}]},
    "p15": {"type": "timeline", "items": [
        {"label": "Demand, net time, cycle times", "sub": "Days 1–30", "icon": "clipboard", "with": 0},
        {"label": "Yamazumi, hourly boards", "sub": "31–60", "icon": "stack", "with": 1},
        {"label": "Verify output and yield, scale", "sub": "61–90", "icon": "chartUp", "with": 2}]},
}
for _p in PAGES:
    _p["visual"] = VISUALS[_p["key"]]

# Two quick-check quizzes. `after` = page key this quiz follows in the timeline.
QUIZZES = [
    {
        "key": "quiz1", "num": 1, "after": "p08",
        "question": "A shift has 25,200 net seconds and the customer needs 840 units. What is the TAKT time?",
        "options": ["20 seconds", "30 seconds", "40 seconds"],
        "correct": 1,
        "explanation": "TAKT = net available time ÷ demand = 25,200 ÷ 840 = 30 seconds per unit.",
        "q_script": "Quick check. A shift has twenty-five thousand two hundred net seconds. The "
                    "customer needs eight hundred and forty units. What's the TAKT time? Take a "
                    "few seconds.",
        "a_script": "It's thirty seconds. TAKT is net available time divided by demand. So one "
                    "unit every thirty seconds.",
    },
    {
        "key": "quiz2", "num": 2, "after": "p15",
        "question": "Final test takes 38 s per unit, but TAKT is 30 s. A manager says: \"Tell the testers to go faster.\" What should the team do FIRST?",
        "options": ["Skip part of the test to save time", "Analyze the test station's losses and capacity",
                    "Build extra stock upstream", "Recalculate TAKT using gross shift time"],
        "correct": 1,
        "explanation": "A cycle time above TAKT is a capacity problem. Study the station's losses, cycle and uptime, then improve or add verified capacity. Skipping tests or hiding it with stock creates new problems.",
        "q_script": "One more, and this one's a scenario. Final test takes thirty-eight seconds, "
                    "but TAKT is thirty. A manager says, tell the testers to go faster. What "
                    "should the team do first? Have a think.",
        "a_script": "Analyze the test station first. Study its losses, cycle and uptime, then "
                    "improve it, or add proven capacity. Skipping tests or building stock only "
                    "creates new problems.",
    },
]


if __name__ == "__main__":
    lesson_lib.main(sys.modules[__name__])
