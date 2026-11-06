import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/rc/words.json";

// All data comes from narration/root_cause.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "rc",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "From symptom to a cause you can prove",
  outroLine: "Define. Test. Prevent.",
  outroSub: "Root Cause Analysis — prove it, then fix it",
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "cameras failed focus test in one morning",
    sub: "Three people, three different answers.", until: "In this lesson",
  },
  recap: {
    problem: "Cameras failing focus after a changeover", before: 60, after: 12, unit: "defects per 20,000 cameras",
    takeaways: [
      { text: "Define it sharply, protect the customer", cue: "Define the problem sharply" },
      { text: "Every cause is a hypothesis until tested", cue: "Treat every cause" },
      { text: "Fix why it happened, and why it escaped", cue: "And fix both" },
    ],
    action: { text: "Take one closed problem, and check whether its root cause was ever tested.", cue: "Here's your action" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "Next, you'll learn" },
  },
};

export const RootCauseAnalysis: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...POLISH, sound: captions }} />
);
