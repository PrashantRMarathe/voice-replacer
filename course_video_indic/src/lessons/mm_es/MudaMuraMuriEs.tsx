import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/mm_es/words.json";

// Spanish version of MudaMuraMuriEs (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "Desperdicio, disparidad y sobrecarga — mejora las tres",
  outroLine: "Nivela. Protege. Elimina.",
  outroSub: "Las 3M — flujo estable, no gente más rápida",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "cámaras atrás, una hora antes de que termine el turno",
    sub: "Todos corren. Los errores se acumulan en la prueba.", until: "En esta lección",
  },
  recap: {
    problem: "La línea de Sanjay terminaba tarde cada día", before: 150, after: 0, unit: "minutos de horas extra al día",
    takeaways: [
      { text: "Muda desperdicio, Mura disparidad, Muri sobrecarga", cue: "Muda es desperdicio" },
      { text: "Se alimentan entre sí: mejóralas juntas", cue: "Se alimentan entre sí" },
      { text: "Flujo estable, no gente más rápida", cue: "Y la meta es" },
    ],
    action: { text: "Sigue un producto por tu línea, y marca un ejemplo de cada M.", cue: "Esta es tu acción" },
    next: { letter: "N", title: "Next Inspection", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_ES_DURATION = PLAN.total;

export const MudaMuraMuriEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
