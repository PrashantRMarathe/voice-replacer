import React from "react";
import { PageLesson, LessonText } from "../../lessons/shared/PageLesson";
import type { Polish } from "../../lessons/shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../../lessons/plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "./words.json";

// All data comes from narration/takt_time.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "tt",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "The beat your customer sets",
  outroLine: "Measure. Balance. Flow.",
  outroSub: "TAKT Time — the customer's pace",
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "cameras built ahead of test",
    sub: "Every station busy. The truck still left late.", until: "In this lesson",
  },
  recap: {
    problem: "A busy line, still missing the truck", before: 0, after: 10, unit: "seconds: the beat for 7,200 cameras a day",
    fixedLabel: "The pace everyone works to",
    takeaways: [
      { text: "TAKT = net available time ÷ demand", cue: "TAKT is net available" },
      { text: "The pace you need, not a station's time", cue: "It's the pace" },
      { text: "Plan for real losses, not theory", cue: "And plan for real" },
    ],
    action: { text: "Calculate the TAKT for one line, and compare it with your slowest station.", cue: "Here's your action" },
    next: { letter: "U", title: "Uniform Production", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const TaktTimeDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...POLISH, sound: true }} />
  );
};
