import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/a3_de/words.json";

// German version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "Die ganze Problemgeschichte auf einer Seite",
  outroLine: "Die Lücke sehen. Die Ursache beweisen. Sichern.",
  outroSub: "A3 — besser denken, auf einem Bogen",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_DE_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "Server fielen beim ersten Boot-Test durch",
    sub: "In vier Wochen. Erster Lösungsvorschlag: zwei Prüfer mehr.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Server, die beim ersten Boot-Test durchfallen", before: 48, after: 16, unit: "pro 1.000 Server", fixedLabel: "Ziel erreicht: von 48 gesunken",
    takeaways: [
      { text: "Beginnen Sie mit einer messbaren Lücke", cue: "Beginnen Sie mit einer messbaren" },
      { text: "Hingehen und schauen; jede Ursache beweisen", cue: "Gehen Sie hin und schauen Sie" },
      { text: "Nur standardisieren, was der Pilot bewiesen hat", cue: "Und standardisieren Sie nur" },
    ],
    action: { text: "Wählen Sie ein wiederkehrendes Problem, und schreiben Sie seine Problembeschreibung auf einen A3-Bogen.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "B", title: "Burn Down Chart", cue: "Als Nächstes lernen Sie" },
  },
};

export const A3ProblemSolvingDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
