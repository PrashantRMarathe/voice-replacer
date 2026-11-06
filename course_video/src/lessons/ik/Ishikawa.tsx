import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ik/words.json";

// All data comes from narration/ishikawa.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "ik",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "Search wide with the fishbone, then prove the cause",
  outroLine: "Search wide. Prove narrow.",
  outroSub: "Ishikawa — every bone is a guess until tested",
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const ISHIKAWA_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "switches per 1,000 failing port test",
    sub: "Up from 5. The meeting's answer: buy a new tester.", until: "In this lesson",
  },
  recap: {
    problem: "Port-link failures on the switch line", before: 32, after: 4, unit: "per 1,000 switches",
    fixedLabel: "Both causes fixed",
    takeaways: [
      { text: "A sharp, measurable effect at the head", cue: "Start with a sharp" },
      { text: "Search widely across the 6M, no blame", cue: "Search widely" },
      { text: "Every bone is a guess until proven", cue: "And treat every bone" },
    ],
    action: { text: "Draw a fishbone for one recurring problem, and pick three causes to test.", cue: "Here's your action" },
    next: { letter: "J", title: "Jidoka", cue: "Next, you'll learn" },
  },
};

export const Ishikawa: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...ISHIKAWA_POLISH, sound: captions }} />
);
