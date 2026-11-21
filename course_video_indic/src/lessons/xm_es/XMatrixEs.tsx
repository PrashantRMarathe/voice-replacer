import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/xm_es/words.json";

// Spanish version of XMatrixEs (same design and polish as the English lesson).
// All data comes from narration/x_matrix_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Convierte la estrategia en acción con Hoshin Kanri",
  outroLine: "Alinea. Despliega. Revisa.",
  outroSub: "X-Matrix — una estrategia que de verdad puedes ejecutar",
};

// Same polish as English XMatrix; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "proyectos de mejora, todos los equipos ocupados",
    sub: "Aun así, la entrega seguía fallando, trimestre tras trimestre.", until: "En esta lección",
  },
  recap: {
    problem: "Un portafolio ocupado, entregas que fallan", before: 40, after: 3, unit: "proyectos, cada uno ligado a una meta y un KPI",
    fixedLabel: "Portafolio enfocado",
    takeaways: [
      { text: "Unas pocas prioridades reales, no una lista de deseos", cue: "Elige unas pocas prioridades reales" },
      { text: "Meta → proyecto → KPI → un responsable", cue: "Liga cada meta" },
      { text: "Revisa con honestidad: los números deben moverse", cue: "Y revisa con honestidad" },
    ],
    action: { text: "Escribe un objetivo para tu área como un resultado, no como una actividad.", cue: "Esta es tu acción" },
    next: { letter: "Y", title: "Yamazumi", cue: "Nos vemos en la siguiente" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_ES_DURATION = PLAN.total;

export const XMatrixEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
