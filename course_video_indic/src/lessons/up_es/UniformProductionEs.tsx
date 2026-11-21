import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/up_es/words.json";

// Spanish version of UniformProductionEs (same design and polish as the English lesson).
// All data comes from narration/uniform_production_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "Nivela el volumen y la mezcla para un flujo estable y confiable",
  outroLine: "Nivela. Ordena. Estabiliza.",
  outroSub: "Uniform Production — un ritmo estable que tu línea puede sostener",
};

// Same polish as English UniformProduction; cues are phrases from the Spanish intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "teléfonos el lunes. Casi nada el martes.",
    sub: "Para el miércoles, el banco de prueba se ahoga.", until: "En esta lección",
  },
  recap: {
    problem: "Un programa muy disparejo", before: 0, after: 6000, unit: "unidades buenas al día, todos los días",
    fixedLabel: "Un ritmo estable y nivelado",
    takeaways: [
      { text: "Nivela el volumen y la mezcla", cue: "Nivela el volumen" },
      { text: "Revisa primero los cuellos de botella y los cambios de modelo", cue: "Revisa los cuellos de botella" },
      { text: "Un plan visible, reglas claras de cambio", cue: "Y haz visible el plan" },
    ],
    action: { text: "Busca un producto que armas en un lote grande, y dibuja un patrón más pequeño que se repita.", cue: "Esta es tu acción" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "Ahora vas a mapear" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_ES_DURATION = PLAN.total;

export const UniformProductionEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
