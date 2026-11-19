import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ni_es/words.json";

// Spanish version of NextInspectionEs (same design and polish as the English lesson).
// All data comes from narration/next_inspection_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "El siguiente proceso es mi cliente",
  outroLine: "No hagas. No pases. No aceptes.",
  outroSub: "Next Inspection — protege al siguiente proceso",
};

// Same polish as English NextInspection; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "conector flojo en la estación tres",
    sub: "Nadie lo notó. Luego un cliente abrió la caja.", until: "En esta lección",
  },
  recap: {
    problem: "Defectos que se escapan a estaciones posteriores", before: 18, after: 3, unit: "fugas por semana",
    takeaways: [
      { text: "No hagas, no pases, no aceptes", cue: "No hagas" },
      { text: "Revisa temprano, y reacciona rápido", cue: "Revisa los puntos críticos" },
      { text: "Sigue moviendo los controles hacia el inicio", cue: "Y sigue moviendo" },
    ],
    action: { text: "Elige una entrega, y anota lo que el siguiente proceso necesita de ella.", cue: "Esta es tu acción" },
    next: { letter: "O", title: "One Point Lesson", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_ES_DURATION = PLAN.total;

export const NextInspectionEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
