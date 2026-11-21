import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/qr_es/words.json";

// Spanish version of QrqcEs (same design and polish as the English lesson).
// All data comes from narration/qrqc_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "Reacciona en minutos — cierra con evidencia",
  outroLine: "Detecta. Contén. Comprueba.",
  outroSub: "QRQC — reacción rápida, evidencia real",
};

// Same polish as English QRQC; cues are phrases from the Spanish intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "cámaras fallando la prueba de enfoque para el mediodía",
    sub: "Alguien reinició el probador, y la línea siguió.", until: "En esta lección",
  },
  recap: {
    problem: "Cámaras sospechosas camino al almacén", before: 2000, after: 0, unit: "cámaras sospechosas sin ubicar",
    takeaways: [
      { text: "Reacciona rápido, pero con evidencia", cue: "Reacciona rápido" },
      { text: "Primero contén, cuadra cada unidad", cue: "Primero contén" },
      { text: "Cierra solo cuando la solución esté comprobada", cue: "Y cierra un problema" },
    ],
    action: { text: "Escribe los primeros 30 minutos de tu plan de reacción para un defecto crítico.", cue: "Esta es tu acción" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "Ahora profundizarás" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_ES_DURATION = PLAN.total;

export const QrqcEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
