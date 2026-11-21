import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/zd_es/words.json";

// Spanish version of ZeroDefectsEs (same design and polish as the English lesson).
// All data comes from narration/zero_defects_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "Previene los defectos — no solo los inspecciones",
  outroLine: "Previene. Mide. Mejora.",
  outroSub: "Zero Defects — integrado en la gestión diaria",
};

// Same polish as English ZeroDefects; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "teléfonos de regreso a retrabajo",
    sub: "Un conector, mal asentado. Pasó todas las revisiones visuales.", until: "En esta lección",
  },
  recap: {
    problem: "Fallas de carga por un conector mal asentado", before: 1200, after: 200,
    unit: "teléfonos con falla, de 40,000", fixedLabel: "Difícil de repetir: 83% menos",
    takeaways: [
      { text: "Previene los defectos, no solo los inspecciones", cue: "Previene los defectos" },
      { text: "Mide con honestidad, con definiciones claras", cue: "Mide con honestidad" },
      { text: "Corrige el sistema, no a la persona", cue: "Y cuando algo falle" },
    ],
    action: { text: "Elige un defecto que sigue regresando, y pregúntate cómo hacerlo imposible.", cue: "Esta es tu acción" },
    next: { letter: "Z", title: "Zero Defects", kicker: "LECCIÓN COMPLETA", cue: "Nos vemos en la siguiente" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_ES_DURATION = PLAN.total;

export const ZeroDefectsEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
