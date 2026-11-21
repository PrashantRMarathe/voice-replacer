import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ik_es/words.json";

// Spanish version of IshikawaEs (same design and polish as the English lesson).
// All data comes from narration/ishikawa_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "Busca a lo ancho con la espina de pescado, luego comprueba la causa",
  outroLine: "Busca a lo ancho. Comprueba a fondo.",
  outroSub: "Ishikawa — cada espina es una suposición hasta probarla",
};

// Same polish as English Ishikawa; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "switches por cada 1,000 fallan la prueba de puertos",
    sub: "Antes eran 5. La respuesta de la junta: comprar un probador nuevo.", until: "En esta lección",
  },
  recap: {
    problem: "Fallas de enlace de puertos en la línea de switches", before: 32, after: 4, unit: "por cada 1,000 switches",
    fixedLabel: "Las dos causas corregidas",
    takeaways: [
      { text: "Un efecto preciso y medible en la cabeza", cue: "Empieza con un efecto preciso" },
      { text: "Busca a lo ancho en las 6M, sin culpar", cue: "Busca a lo ancho" },
      { text: "Cada espina es una suposición hasta comprobarla", cue: "Y trata cada espina" },
    ],
    action: { text: "Dibuja una espina de pescado para un problema que se repite, y elige tres causas para probar.", cue: "Esta es tu acción" },
    next: { letter: "J", title: "Jidoka", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_ES_DURATION = PLAN.total;

export const IshikawaEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
