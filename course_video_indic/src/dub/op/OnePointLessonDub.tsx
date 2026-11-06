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

// All data comes from narration/one_point_lesson.py (+ import_clones.py for the cloned
// voice). The timeline (scene order, quiz placement, durations) is planLesson's.
const DATA: LessonData = {
  id: "op",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "One topic. One clear point. One better action.",
  outroLine: "Simple. Visual. Correct.",
  outroSub: "One Point Lesson — teach one point well",
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_DURATION = PLAN.total;

// Polish layer (shared/polish.tsx). The Dub version keeps it without sound.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "connector fitted the wrong way, and cracked",
    sub: "The day shift knew the trick. Nobody had shared it.", until: "In this lesson",
  },
  recap: {
    problem: "Night shift cracking connectors", before: 14, after: 1, unit: "cracked connectors a week",
    takeaways: [
      { text: "One topic, one point, one strong visual", cue: "One topic" },
      { text: "Teach at the gemba, then watch the work", cue: "Teach it at" },
      { text: "Keep it matching the current standard", cue: "And control it" },
    ],
    action: { text: "Pick one mistake that keeps repeating, and draft a One Point Lesson for it.", cue: "Here's your action" },
    next: { letter: "P", title: "Poka Yoke", cue: "Next, you'll learn" },
  },
};

// Dub version (made by tools/make_dub.py): English video, no captions, sound on;
// narration from public/audio/<voice>/, or none (music + effects) when voice is null.
export const OnePointLessonDub: React.FC<{ voice?: string | null }> = ({ voice = null }) => {
  setUI("en");
  const blocks = voice ? PLAN.blocks : PLAN.blocks.map((b) => ({ ...b, clips: [] }));
  return (
    <PageLesson data={{ ...DATA, id: voice ?? DATA.id }} blocks={blocks} text={TEXT} captions={false}
      polish={{ ...POLISH, sound: true }} />
  );
};
