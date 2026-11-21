import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ct_es/words.json";

// Spanish version of CycleTimeStudyEs (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "Mide el trabajo real, encuentra el cuello de botella real",
  outroLine: "Define. Mide. Mejora el método.",
  outroSub: "Cycle Time Study — evidencia antes que velocidad",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "segundos: cada estación parecía bastante rápida",
    sub: "Aun así, la línea de monitores no cumplía su meta por hora, turno tras turno.", until: "En esta lección",
  },
  recap: {
    problem: "Estación de prueba de pantalla más lenta que el TAKT", before: 28, after: 23, unit: "segundos por monitor en la estación C", fixedLabel: "Ahora dentro del TAKT",
    takeaways: [
      { text: "Define primero el límite", cue: "Define primero el límite" },
      { text: "Mira la dispersión, no solo el promedio", cue: "Mira la dispersión" },
      { text: "Corrige el método, nunca te saltes revisiones de calidad", cue: "Y corrige el método" },
    ],
    action: { text: "Toma el tiempo de diez ciclos en una estación, y compara el más largo con el TAKT.", cue: "Esta es tu acción" },
    next: { letter: "D", title: "Design Thinking", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_ES_DURATION = PLAN.total;

export const CycleTimeStudyEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
