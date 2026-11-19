import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/gb_es/words.json";

// Spanish version of GembaEs (same design and polish as the English lesson).
// All data comes from narration/gemba_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "Lugar real, cosa real, hechos reales",
  outroLine: "Ve. Observa. Confirma.",
  outroSub: "Gemba, Genbutsu, Genjitsu — hechos antes que decisiones",
};

// Same polish as English Gemba; cues are phrases from the Spanish intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× las fallas de audífonos en el turno B",
    sub: "El plan: volver a entrenar al turno B. Nadie había visto un audífono con falla.", until: "En esta lección",
  },
  recap: {
    problem: "Audífonos que fallan la prueba de audio", before: 20, after: 8, unit: "fallas por cada 1,000 audífonos",
    fixedLabel: "Corregido en la causa",
    takeaways: [
      { text: "Ve al lugar real; observa ciclos reales", cue: "Ve al lugar real" },
      { text: "Toma la cosa real; compárala con una buena", cue: "Toma la cosa real" },
      { text: "Revisa los hechos reales, con un denominador", cue: "Y revisa los hechos reales" },
    ],
    action: { text: "Toma un problema que se repite, y haz una visita 3G de treinta minutos.", cue: "Esta es tu acción" },
    next: { letter: "H", title: "Hancho", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_ES_DURATION = PLAN.total;

export const GembaEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
