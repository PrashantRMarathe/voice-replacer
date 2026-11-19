import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ew_es/words.json";

// Spanish version of EliminationOfWasteEs (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "Elimina lo que tu cliente no pagaría",
  outroLine: "Velo. Elimina la causa. Compruébalo.",
  outroSub: "Elimination of Waste — más valor, menos esfuerzo",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "barras de sonido retrabajadas cada mes",
    sub: "₹42 corregir cada una. Nadie lo había sumado nunca.", until: "En esta lección",
  },
  recap: {
    problem: "Barras de sonido retrabajadas por un cable de bocina que zumba", before: 1500, after: 300, unit: "retrabajos al mes", fixedLabel: "Retrabajo reducido 80%",
    takeaways: [
      { text: "Desperdicio: lo que el cliente no pagaría", cue: "El desperdicio es todo" },
      { text: "Encuéntralo con hechos en el Gemba", cue: "Encuéntralo con hechos en el Gemba" },
      { text: "Elimina la causa, compruébala, sostenla", cue: "Y elimina la causa" },
    ],
    action: { text: "Recorre tu línea durante treinta minutos, y anota tres desperdicios como hechos.", cue: "Esta es tu acción" },
    next: { letter: "F", title: "FMEA", cue: "Ahora aprenderás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_ES_DURATION = PLAN.total;

export const EliminationOfWasteEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
