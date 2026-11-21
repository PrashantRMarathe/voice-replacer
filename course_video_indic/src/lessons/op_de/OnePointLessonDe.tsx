import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/op_de/words.json";

// German version of OnePointLessonDe (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "Ein Thema. Ein klarer Punkt. Eine bessere Handlung.",
  outroLine: "Einfach. Visuell. Korrekt.",
  outroSub: "One Point Lesson: einen Punkt gut lehren",
};

// Same polish as English OnePointLesson; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "Stecker falsch eingesetzt, und gebrochen",
    sub: "Die Tagschicht kannte den Trick. Niemand hatte ihn geteilt.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Nachtschicht bricht Stecker", before: 14, after: 1, unit: "gebrochene Stecker pro Woche",
    takeaways: [
      { text: "Ein Thema, ein Punkt, ein starkes Bild", cue: "Ein Thema" },
      { text: "Am Gemba lehren, dann die Arbeit beobachten", cue: "Lehren Sie sie am Gemba" },
      { text: "Passend zum aktuellen Standard halten", cue: "Und lenken Sie sie" },
    ],
    action: { text: "Wählen Sie einen Fehler, der sich wiederholt, und entwerfen Sie eine One Point Lesson dazu.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "P", title: "Poka Yoke", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_DE_DURATION = PLAN.total;

export const OnePointLessonDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
