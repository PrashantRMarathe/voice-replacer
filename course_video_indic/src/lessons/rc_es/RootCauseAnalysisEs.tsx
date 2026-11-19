import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/rc_es/words.json";

// Spanish version of RootCauseAnalysisEs (same design and polish as the English lesson).
// All data comes from narration/root_cause_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "Del síntoma a una causa que puedas comprobar",
  outroLine: "Define. Prueba. Previene.",
  outroSub: "Root Cause Analysis — compruébalo, luego corrígelo",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "cámaras fallaron la prueba de enfoque en una mañana",
    sub: "Tres personas, tres respuestas distintas.", until: "En esta lección",
  },
  recap: {
    problem: "Cámaras que fallan el enfoque tras un cambio de modelo", before: 60, after: 12, unit: "defectos por cada 20,000 cámaras",
    takeaways: [
      { text: "Defínelo con precisión, protege al cliente", cue: "Define el problema con precisión" },
      { text: "Cada causa es una hipótesis hasta probarla", cue: "Trata cada causa" },
      { text: "Corrige por qué pasó, y por qué se escapó", cue: "Y corrige por qué pasó" },
    ],
    action: { text: "Toma un problema cerrado, y revisa si su causa raíz se probó alguna vez.", cue: "Esta es tu acción" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_ES_DURATION = PLAN.total;

export const RootCauseAnalysisEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
