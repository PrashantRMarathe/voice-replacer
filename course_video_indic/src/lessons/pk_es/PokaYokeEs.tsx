import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/pk_es/words.json";

// Spanish version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "Haz imposible la acción incorrecta",
  outroLine: "Eliminar. Prevenir. Detectar.",
  outroSub: "Poka Yoke — saca la memoria de la calidad",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_ES_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "grabadoras salieron sin un tornillo",
    sub: "La operadora era hábil y cuidadosa. Simplemente humana.", until: "En esta lección",
  },
  recap: {
    problem: "Grabadoras enviadas sin un tornillo", before: 18, after: 1, unit: "por cada 10,000 unidades",
    takeaways: [
      { text: "Los errores son predecibles: elimínalos desde el diseño", cue: "Los errores son predecibles" },
      { text: "Prevenir, luego detectar, luego advertir", cue: "Prefiere prevenir" },
      { text: "Pon a prueba cada dispositivo con muestras malas", cue: "Y pon a prueba" },
    ],
    action: { text: "Busca un chequeo que dependa de la memoria, y haz un boceto de un Poka Yoke para él.", cue: "Esta es tu acción" },
    next: { letter: "Q", title: "QRQC", cue: "Ahora aprenderás QRQC" },
  },
};

export const PokaYokeEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
