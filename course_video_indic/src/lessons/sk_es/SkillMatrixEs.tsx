import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/sk_es/words.json";

// Spanish version of SkillMatrixEs (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "Quién puede de verdad hacer cada trabajo — y dónde están las brechas",
  outroLine: "Evalúa. Entrena. Cubre.",
  outroSub: "Skill Matrix — un control vivo de la capacidad",
};

// Same polish as English SkillMatrix; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "persona que sabe ajustar el enfoque del lente",
    sub: "Bala se reportó enfermo. Para las diez, toda la celda estaba parada.", until: "En esta lección",
  },
  recap: {
    problem: "Un solo experto en enfoque del lente, y estaba enfermo", before: 1, after: 2, unit: "expertos calificados en enfoque del lente",
    takeaways: [
      { text: "Capacidad demostrada, no asistencia", cue: "Una matriz de habilidades muestra" },
      { text: "Cuenta los respaldos calificados, en cada turno", cue: "Cuenta los respaldos calificados" },
      { text: "Mantenla viva, con evidencia", cue: "Y mantenla viva" },
    ],
    action: { text: "Enlista tus tres estaciones más críticas, y cuenta las personas calificadas para cada una.", cue: "Esta es tu acción" },
    next: { letter: "T", title: "TAKT Time", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_ES_DURATION = PLAN.total;

export const SkillMatrixEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
