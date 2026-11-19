import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/op_es/words.json";

// Spanish version of OnePointLessonEs (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "Un tema. Un punto claro. Una acción mejor.",
  outroLine: "Simple. Visual. Correcta.",
  outroSub: "One Point Lesson — enseña bien un punto",
};

// Same polish as English OnePointLesson; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "conector colocado al revés, y estrellado",
    sub: "El turno de día conocía el truco. Nadie lo había compartido.", until: "En esta lección",
  },
  recap: {
    problem: "El turno de noche estrellaba conectores", before: 14, after: 1, unit: "conectores estrellados por semana",
    takeaways: [
      { text: "Un tema, un punto, un buen apoyo visual", cue: "Un tema" },
      { text: "Enseña en el Gemba, luego observa el trabajo", cue: "Enséñala en el Gemba" },
      { text: "Que coincida con el estándar vigente", cue: "Y contrólala" },
    ],
    action: { text: "Elige un error que se sigue repitiendo, y haz un borrador de una One Point Lesson para él.", cue: "Esta es tu acción" },
    next: { letter: "P", title: "Poka Yoke", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_ES_DURATION = PLAN.total;

export const OnePointLessonEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
