import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/dt_es/words.json";

// Spanish version of DesignThinkingEs (same design and polish as the English lesson).
// All data comes from narration/design_thinking_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "Resuelve el problema correcto, con las personas que hacen el trabajo",
  outroLine: "Observa. Define. Prueba en pequeño.",
  outroSub: "Design Thinking — primero las personas, siempre la evidencia",
};

// Same polish as English DesignThinking; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "errores de etiqueta en cada 1,000 bombas",
    sub: "La primera idea: una impresora más rápida y cara. Nadie les había preguntado a los empacadores.", until: "En esta lección",
  },
  recap: {
    problem: "Errores de etiqueta en el empaque de bombas de infusión", before: 12, after: 2, unit: "por cada 1,000 bombas",
    takeaways: [
      { text: "Empieza con las personas; observa antes de decidir", cue: "Empieza con las personas" },
      { text: "Define la necesidad, sin una solución dentro", cue: "Define la necesidad" },
      { text: "Prueba en pequeño: resultados y uso real", cue: "Y prueba en pequeño" },
    ],
    action: { text: "Observa diez ciclos de un trabajo difícil, y habla con tres personas que lo hacen.", cue: "Esta es tu acción" },
    next: { letter: "E", title: "Elimination of Waste", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_ES_DURATION = PLAN.total;

export const DesignThinkingEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
