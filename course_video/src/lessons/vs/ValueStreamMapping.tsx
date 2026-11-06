import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/vs/words.json";

// All data comes from narration/value_stream.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "vs",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "See the whole flow, from order to delivery",
  outroLine: "See. Measure. Flow.",
  outroSub: "Value Stream Mapping — find the waiting, design the flow",
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "minutes to build and test a set-top box",
    sub: "Yet almost four days to reach the customer.", until: "In this lesson",
  },
  recap: {
    problem: "Days of waiting for minutes of work", before: 4200, after: 2100, unit: "units waiting across three buffers",
    fixedLabel: "Future state: half the waiting",
    takeaways: [
      { text: "Map the real material + information flow", cue: "Map the real flow" },
      { text: "Lead time hides in waiting, not work", cue: "Most of your lead time" },
      { text: "Prove the future state before cutting stock", cue: "And design a future" },
    ],
    action: { text: "Walk one product family backwards from dispatch, and count every pile you pass.", cue: "Here's your action" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "Next, you'll learn" },
  },
};

export const ValueStreamMapping: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
