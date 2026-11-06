import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/zd/words.json";

// All data comes from narration/zero_defects.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "zd",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "Prevent defects — don't just inspect them",
  outroLine: "Prevent. Measure. Improve.",
  outroSub: "Zero Defects — built into daily management",
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
// Z is the last letter, so the end card says "lesson complete", not a next lesson.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "phones back for rework",
    sub: "One connector, seated badly. It passed every visual check.", until: "In this lesson",
  },
  recap: {
    problem: "Charging failures from a badly seated connector", before: 1200, after: 200,
    unit: "phones failing, out of 40,000", fixedLabel: "Made hard to repeat: 83% fewer",
    takeaways: [
      { text: "Prevent defects, don't just inspect", cue: "Prevent defects" },
      { text: "Measure honestly, with clear definitions", cue: "Measure honestly" },
      { text: "Fix the system, not the person", cue: "And when something fails" },
    ],
    action: { text: "Pick one defect that keeps coming back, and ask how to make it impossible.", cue: "Here's your action" },
    next: { letter: "Z", title: "Zero Defects", kicker: "LESSON COMPLETE", cue: "See you in the next one" },
  },
};

export const ZeroDefects: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
