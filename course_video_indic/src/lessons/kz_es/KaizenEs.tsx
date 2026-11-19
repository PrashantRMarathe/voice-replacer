import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/kz_es/words.json";

// Spanish version of KaizenEs (same design and polish as the English lesson).
// All data comes from narration/kaizen_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "Cambios pequeños, cada día, por las personas que hacen el trabajo",
  outroLine: "Observa. Prueba en pequeño. Estandariza. Repite.",
  outroSub: "Kaizen — el mejor método de hoy es la base de mañana",
};

// Same polish as English Kaizen; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "volteos de cada monitor",
    sub: "Boca abajo, luego boca arriba. Siempre se había hecho así.", until: "En esta lección",
  },
  recap: {
    problem: "Rayones de panel por voltear monitores", before: 15, after: 3, unit: "rayones por cada 1,000 monitores",
    fixedLabel: "Se sostuvo a los 90 días",
    takeaways: [
      { text: "El Kaizen es un hábito diario", cue: "El Kaizen es un hábito diario" },
      { text: "Prueba en pequeño; revisa que nada más empeoró", cue: "Prueba en pequeño" },
      { text: "Estandariza cada ganancia", cue: "Y estandariza cada ganancia" },
    ],
    action: { text: "Pregúntale a un operador qué hace difícil su trabajo, y prueba una solución pequeña.", cue: "Esta es tu acción" },
    next: { letter: "L", title: "Low Cost Automation", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_ES_DURATION = PLAN.total;

export const KaizenEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
