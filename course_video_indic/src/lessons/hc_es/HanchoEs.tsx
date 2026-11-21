import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/hc_es/words.json";

// Spanish version of HanchoEs (same design and polish as the English lesson).
// All data comes from narration/hancho_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "Liderazgo en el piso, cada hora de cada turno",
  outroLine: "Dirige en el Gemba. Desarrolla a las personas.",
  outroSub: "Hancho — restablecer estándares, mejorar cada día",
};

// Same polish as English Hancho; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV menos por hora, durante todo un turno",
    sub: "Nadie lo notó hasta el reporte de la mañana siguiente.", until: "En esta lección",
  },
  recap: {
    problem: "Brecha de producción tras un cambio de modelo", before: 98, after: 120, unit: "TV por hora",
    fixedLabel: "Recuperado en el mismo turno",
    takeaways: [
      { text: "Dirige desde el Gemba: estándar contra real", cue: "Dirige desde el Gemba" },
      { text: "Haz visibles las brechas cada hora; reacciona en el mismo turno", cue: "Haz visible cada brecha" },
      { text: "Desarrolla a las personas, para que la línea no dependa de ti", cue: "Y desarrolla a tu gente" },
    ],
    action: { text: "Escribe tu propio trabajo estándar de líder, para un turno.", cue: "Esta es tu acción" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_ES_DURATION = PLAN.total;

export const HanchoEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
