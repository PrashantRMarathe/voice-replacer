import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/dt/words.json";

// All data comes from narration/design_thinking.py (+ import_clones.py for the
// cloned voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "dt",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "Solve the right problem, with the people who do the work",
  outroLine: "Observe. Define. Test small.",
  outroSub: "Design Thinking — people first, evidence always",
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const DESIGN_THINKING_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "label errors in every 1,000 pumps",
    sub: "The first idea: a costly faster printer. Nobody had asked the packers.", until: "In this lesson",
  },
  recap: {
    problem: "Label errors at infusion-pump packing", before: 12, after: 2, unit: "per 1,000 pumps",
    takeaways: [
      { text: "Start with the people; watch before you decide", cue: "Start with the people" },
      { text: "Define the need, with no solution inside", cue: "Define the need" },
      { text: "Test small: results and real use", cue: "And test small" },
    ],
    action: { text: "Watch ten cycles of one painful job, and talk to three people who do it.", cue: "Here's your action" },
    next: { letter: "E", title: "Elimination of Waste", cue: "Next, you'll learn" },
  },
};

export const DesignThinking: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...DESIGN_THINKING_POLISH, sound: captions }} />
);
