import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/bd_es/words.json";

// Spanish version of BurnDownChartEs (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "Ve el trabajo que falta, antes de la fecha límite",
  outroLine: "Planea la línea. Sigue la brecha. Actúa hoy.",
  outroSub: "Burn Down Chart — no más sorpresas el viernes",
};

// Same polish as English BurnDownChart; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "routers no alcanzaron el camión",
    sub: "Nadie lo vio venir, hasta el viernes en la tarde.", until: "En esta lección",
  },
  recap: {
    problem: "Routers faltantes en el embarque", before: 80, after: 0, unit: "routers de menos",
    takeaways: [
      { text: "Dibuja primero la línea ideal; nunca la redibujes", cue: "Dibuja primero la línea ideal" },
      { text: "Cuenta solo el trabajo completo y bueno", cue: "Cuenta solo el trabajo" },
      { text: "¿Arriba de la ideal? Actúa ese día, con un responsable", cue: "Y cuando la línea" },
    ],
    action: { text: "Elige un trabajo con fecha límite, y dibuja su gráfica antes del turno de mañana.", cue: "Esta es tu acción" },
    next: { letter: "C", title: "Cycle Time Study", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_ES_DURATION = PLAN.total;

export const BurnDownChartEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
