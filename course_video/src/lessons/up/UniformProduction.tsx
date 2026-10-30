import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/up/words.json";

// All data comes from narration/uniform_production.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "up",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "Level volume and mix for a steady, reliable flow",
  outroLine: "Level. Sequence. Stabilize.",
  outroSub: "Uniform Production — a steady pace your line can keep",
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "phones on Monday. Almost none on Tuesday.",
    sub: "By Wednesday, the test bench is drowning.", until: "In this lesson",
  },
  recap: {
    problem: "A very bumpy schedule", before: 0, after: 2400, unit: "good units a day, every day",
    fixedLabel: "A steady, level pace",
    takeaways: [
      { text: "Level both volume and mix", cue: "Level both volume" },
      { text: "Check bottlenecks and changeovers first", cue: "Check bottlenecks" },
      { text: "A visible plan, clear change rules", cue: "And make the plan" },
    ],
    action: { text: "Find one product built in a big batch, and sketch a smaller, repeating pattern.", cue: "Here's your action" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "Next, you'll map" },
  },
};

export const UniformProduction: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
