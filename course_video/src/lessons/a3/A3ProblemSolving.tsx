import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/a3/words.json";

// All data comes from narration/a3_problem_solving.py (+ import_clones.py for the
// cloned voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "a3",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "The whole problem story on one page",
  outroLine: "See the gap. Prove the cause. Sustain.",
  outroSub: "A3 — better thinking, on one sheet",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const A3_PROBLEM_SOLVING_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "servers failed their first boot test",
    sub: "In four weeks. The first fix proposed: two more inspectors.", until: "In this lesson",
  },
  recap: {
    problem: "Servers failing their first boot test", before: 48, after: 16, unit: "per 1,000 servers", fixedLabel: "Target met: down from 48",
    takeaways: [
      { text: "Start with a measurable gap", cue: "Start with a measurable" },
      { text: "Go and see; prove every cause", cue: "Go and see" },
      { text: "Standardize only what the pilot proved", cue: "And standardize only" },
    ],
    action: { text: "Pick one repeating problem, and write its problem statement on an A3.", cue: "Here's your action" },
    next: { letter: "B", title: "Burn Down Chart", cue: "Next, you'll learn" },
  },
};

export const A3ProblemSolving: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...A3_PROBLEM_SOLVING_POLISH, sound: captions }} />
);
