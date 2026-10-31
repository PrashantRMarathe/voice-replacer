import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/kz/words.json";

// All data comes from narration/kaizen.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "kz",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "Small changes, every day, by the people doing the work",
  outroLine: "See. Try small. Standardize. Repeat.",
  outroSub: "Kaizen — today's best method is tomorrow's baseline",
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
export const KAIZEN_POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "flips of every monitor",
    sub: "Face down, then face up. It had always been done that way.", until: "In this lesson",
  },
  recap: {
    problem: "Panel scratches from flipping monitors", before: 15, after: 3, unit: "scratches per 1,000 monitors",
    fixedLabel: "Held at 90 days",
    takeaways: [
      { text: "Kaizen is a daily habit", cue: "Kaizen is a daily habit" },
      { text: "Test small; check nothing else got worse", cue: "Test small" },
      { text: "Standardize every gain", cue: "And standardize every gain" },
    ],
    action: { text: "Ask one operator what makes their job difficult, and test one small fix.", cue: "Here's your action" },
    next: { letter: "L", title: "Low Cost Automation", cue: "Next, you'll learn" },
  },
};

export const Kaizen: React.FC<{ captions?: boolean }> = ({ captions = true }) => (
  <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
    polish={{ ...KAIZEN_POLISH, sound: captions }} />
);
