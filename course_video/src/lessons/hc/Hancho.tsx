import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/hc/words.json";

// All data comes from narration/hancho.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "hc",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "Shop-floor leadership, every hour of every shift",
  outroLine: "Lead at the gemba. Develop people.",
  outroSub: "Hancho — restore standards, improve every day",
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const HANCHO_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TVs an hour short, for a whole shift",
    sub: "Nobody noticed until the next morning's report.", until: "In this lesson",
  },
  recap: {
    problem: "Output gap after a model change", before: 98, after: 120, unit: "TVs an hour",
    fixedLabel: "Recovered in the same shift",
    takeaways: [
      { text: "Lead from the gemba: standard vs actual", cue: "Lead from the gemba" },
      { text: "Make gaps visible hourly; react the same shift", cue: "Make every gap visible" },
      { text: "Build people, so the line doesn't depend on you", cue: "And build your people" },
    ],
    action: { text: "Write your own leader standard work, for one shift.", cue: "Here's your action" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "Next, you'll learn" },
  },
};

export const Hancho: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...HANCHO_POLISH, sound: captions }} />
);
