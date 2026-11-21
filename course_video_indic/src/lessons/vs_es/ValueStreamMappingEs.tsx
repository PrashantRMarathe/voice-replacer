import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/vs_es/words.json";

// Spanish version of ValueStreamMappingEs (same design and polish as the English lesson).
// All data comes from narration/value_stream_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "Ve todo el flujo, del pedido a la entrega",
  outroLine: "Observa. Mide. Fluye.",
  outroSub: "Value Stream Mapping — encuentra las esperas, diseña el flujo",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "minutos para armar y probar un decodificador",
    sub: "Aun así, casi cuatro días para llegar al cliente.", until: "En esta lección",
  },
  recap: {
    problem: "Días de espera por minutos de trabajo", before: 4200, after: 2100, unit: "unidades esperando en tres colchones",
    fixedLabel: "Estado futuro: la mitad de la espera",
    takeaways: [
      { text: "Mapea el flujo real de material + información", cue: "Mapea el flujo real" },
      { text: "El tiempo de entrega se esconde en la espera, no en el trabajo", cue: "La mayor parte de tu tiempo de entrega" },
      { text: "Comprueba el estado futuro antes de recortar inventario", cue: "Y diseña un estado futuro" },
    ],
    action: { text: "Recorre una familia de productos hacia atrás desde embarques, y cuenta cada montón que pases.", cue: "Esta es tu acción" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_ES_DURATION = PLAN.total;

export const ValueStreamMappingEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
