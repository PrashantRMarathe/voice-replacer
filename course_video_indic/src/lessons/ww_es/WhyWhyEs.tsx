import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ww_es/words.json";

// Spanish version of WhyWhyEs (same design and polish as the English lesson).
// All data comes from narration/why_why_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "Ve más allá de la respuesta fácil hasta una causa que puedas comprobar",
  outroLine: "Define. Comprueba. Previene.",
  outroSub: "Why–Why — corrige la causa, no a la persona",
};

// Same polish as English WhyWhy; cues are phrases from the Spanish intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "teléfonos fallaron la carga en la prueba final",
    sub: "Primera respuesta: error del operador. Dos días después, volvió a pasar.", until: "En esta lección",
  },
  recap: {
    problem: "Fallas de carga en la Línea 2", before: 50, after: 15, unit: "defectos de carga, mismo volumen",
    fixedLabel: "Causa raíz corregida: 70% menos",
    takeaways: [
      { text: "Primero un problema preciso, luego contener", cue: "Empieza con un problema preciso" },
      { text: "Evidencia para cada porqué, luego pruébalo", cue: "Respalda cada porqué" },
      { text: "Corrige cómo pasó y por qué se escapó", cue: "Y corrige cómo pasó" },
    ],
    action: { text: "Toma un defecto repetido, y escribe su planteamiento 5W2H.", cue: "Esta es tu acción" },
    next: { letter: "X", title: "X-Matrix", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_ES_DURATION = PLAN.total;

export const WhyWhyEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
