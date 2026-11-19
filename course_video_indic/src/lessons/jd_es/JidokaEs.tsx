import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/jd_es/words.json";

// Spanish version of JidokaEs (same design and polish as the English lesson).
// All data comes from narration/jidoka_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "Automatización con toque humano",
  outroLine: "Velo. Detenlo. Resuélvelo.",
  outroSub: "Jidoka — ningún defecto avanza, ninguna anormalidad escondida",
};

// Same polish as English Jidoka; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "monitores de pacientes con un sello delgado",
    sub: "El dosificador trabajó perfecto toda la noche. Su boquilla estaba medio tapada.", until: "En esta lección",
  },
  recap: {
    problem: "Sellos delgados por una boquilla de adhesivo tapada", before: 140, after: 1, unit: "monitores afectados por problema de boquilla",
    fixedLabel: "Atrapado en el origen",
    takeaways: [
      { text: "Define primero lo normal", cue: "Define primero lo normal" },
      { text: "Detecta, detén, contén: ningún defecto avanza", cue: "Detecta, detén y contén" },
      { text: "Cada paro es una lección: corrige la causa raíz", cue: "Y trata cada paro" },
    ],
    action: { text: "Elige un proceso automático, y anota qué debería hacer que se detenga.", cue: "Esta es tu acción" },
    next: { letter: "K", title: "Kaizen", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_ES_DURATION = PLAN.total;

export const JidokaEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
