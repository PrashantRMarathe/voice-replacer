import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/yz_es/words.json";

// Spanish version of YamazumiEs (same design and polish as the English lesson).
// All data comes from narration/yamazumi_es.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_es",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "Balancea la línea contra el TAKT — con datos reales",
  outroLine: "Mide. Apila. Balancea.",
  outroSub: "Yamazumi — un flujo que se sostiene, por diseño",
};

// Same polish as English Yamazumi; cues are phrases from the Spanish intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "operadores esperando, mientras uno está enterrado en tornillos",
    sub: "Nadie es flojo. El trabajo simplemente está apilado de forma dispareja.", until: "En esta lección",
  },
  recap: {
    problem: "Estación B arriba del TAKT", before: 35, after: 30, unit: "segundos de trabajo en la estación B",
    fixedLabel: "De vuelta en el TAKT",
    takeaways: [
      { text: "Mide el trabajo real, no el mejor caso", cue: "Mide el trabajo real" },
      { text: "Apílalo contra el TAKT para ver los montones", cue: "Apílalo contra el TAKT" },
      { text: "Rebalancea sin arriesgar la seguridad ni la calidad", cue: "Y rebalancea con cuidado" },
    ],
    action: { text: "Mide una estación de tu línea, y dibuja su barra contra el TAKT.", cue: "Tu acción esta semana" },
    next: { letter: "Z", title: "Zero Defects", cue: "Nos vemos en la siguiente" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_ES_DURATION = PLAN.total;

export const YamazumiEs: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("es");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
