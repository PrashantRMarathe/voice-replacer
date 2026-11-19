import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/tt_es/words.json";

// Spanish version of TaktTimeEs (same design and polish as the English lesson).
// All data comes from narration/takt_time_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "El compás que marca tu cliente",
  outroLine: "Mide. Balancea. Fluye.",
  outroSub: "TAKT Time — el ritmo del cliente",
};

// Same polish as English TaktTime; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "cámaras armadas antes de la prueba",
    sub: "Cada estación ocupada. El camión igual salió tarde.", until: "En esta lección",
  },
  recap: {
    problem: "Una línea ocupada, que igual pierde el camión", before: 0, after: 10, unit: "segundos: el compás para 7,200 cámaras al día",
    fixedLabel: "El ritmo al que todos trabajan",
    takeaways: [
      { text: "TAKT = tiempo neto disponible ÷ demanda", cue: "El TAKT es el tiempo neto disponible" },
      { text: "El ritmo que necesitas, no el tiempo de una estación", cue: "Es el ritmo" },
      { text: "Planea con pérdidas reales, no con teoría", cue: "Y planea con las pérdidas reales" },
    ],
    action: { text: "Calcula el TAKT de una línea, y compáralo con tu estación más lenta.", cue: "Esta es tu acción" },
    next: { letter: "U", title: "Uniform Production", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_ES_DURATION = PLAN.total;

export const TaktTimeEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
