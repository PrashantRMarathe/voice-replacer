import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/fm_es/words.json";

// Spanish version of FMEAEs (same design and polish as the English lesson).
// All data comes from narration/fmea_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "Análisis de modos de falla y sus efectos: piensa antes de la falla",
  outroLine: "Encadénalo. Califícalo. Prevénlo.",
  outroSub: "FMEA — un plan vivo, no un formato",
};

// Same polish as English FMEA; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "radios para exteriores regresaron llenos de agua",
    sub: "Faltaba el empaque en dos, torcido en cuatro. Todos pasaron la inspección final.", until: "En esta lección",
  },
  recap: {
    problem: "Riesgo del empaque en el radio 5G para exteriores", before: 240, after: 32, unit: "número de prioridad de riesgo",
    fixedLabel: "Riesgo reducido, comprobado en una prueba",
    takeaways: [
      { text: "Efecto → modo de falla → causa controlable", cue: "Construye una cadena clara" },
      { text: "Califica con evidencia; el criterio sobre los números", cue: "Califica con evidencia" },
      { text: "Previene primero, compruébalo, luego recalifica", cue: "Y prefiere la prevención" },
    ],
    action: { text: "Elige un paso crítico, y escribe su cadena de falla con tu equipo.", cue: "Esta es tu acción" },
    next: { letter: "G", title: "Gemba", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_ES_DURATION = PLAN.total;

export const FMEAEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
