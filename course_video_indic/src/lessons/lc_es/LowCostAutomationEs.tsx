import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/lc_es/words.json";

// Spanish version of LowCostAutomationEs (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "El dispositivo seguro más simple que hace el trabajo",
  outroLine: "Simplifica. Automatiza la necesidad. Compruébalo.",
  outroSub: "Low Cost Automation — nunca baja seguridad",
};

// Same polish as English LowCostAutomation; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "golpes de mazo por hora, por operador",
    sub: "Muñecas adoloridas, y rejillas flojas que vibraban en la prueba.", until: "En esta lección",
  },
  recap: {
    problem: "Rejillas de bocina flojas por asentarlas con mazo", before: 18, after: 2, unit: "por cada 1,000 bocinas",
    fixedLabel: "Recuperado en 4 meses",
    takeaways: [
      { text: "Primero simplifica; nunca automatices el desperdicio", cue: "Primero simplifica" },
      { text: "La solución segura más simple; la seguridad es el primer filtro", cue: "Elige la solución segura más simple" },
      { text: "Comprueba el beneficio real, luego dale mantenimiento", cue: "Y comprueba el beneficio real" },
    ],
    action: { text: "Busca un movimiento repetitivo, y pregúntate si se puede eliminar antes de automatizarlo.", cue: "Esta es tu acción" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_ES_DURATION = PLAN.total;

export const LowCostAutomationEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
