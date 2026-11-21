import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/a3_es/words.json";

// Spanish version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "Toda la historia del problema en una hoja",
  outroLine: "Ve la brecha. Prueba la causa. Sostén.",
  outroSub: "A3 — pensar mejor, en una sola hoja",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_ES_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "servidores fallaron su primera prueba de arranque",
    sub: "En cuatro semanas. La primera solución propuesta: dos inspectores más.", until: "En esta lección",
  },
  recap: {
    problem: "Servidores que fallan su primera prueba de arranque", before: 48, after: 16, unit: "por cada 1,000 servidores", fixedLabel: "Meta cumplida: bajó de 48",
    takeaways: [
      { text: "Empieza con una brecha medible", cue: "Empieza con una brecha medible" },
      { text: "Ve a ver; prueba cada causa", cue: "Ve a ver" },
      { text: "Estandariza solo lo que el piloto comprobó", cue: "Y estandariza solo" },
    ],
    action: { text: "Elige un problema que se repite, y escribe su planteamiento en una hoja A3.", cue: "Esta es tu acción" },
    next: { letter: "B", title: "Burn Down Chart", cue: "Ahora aprenderás" },
  },
};

export const A3ProblemSolvingEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
