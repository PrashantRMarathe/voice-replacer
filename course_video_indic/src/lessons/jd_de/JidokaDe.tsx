import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/jd_de/words.json";

// German version of JidokaDe (same design and polish as the English lesson).
// All data comes from narration/jidoka_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "Automatisierung mit menschlicher Note",
  outroLine: "Sehen. Stoppen. Lösen.",
  outroSub: "Jidoka — kein Fehler weitergegeben, keine Abweichung versteckt",
};

// Same polish as English Jidoka; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "Patientenmonitore mit zu dünner Dichtung",
    sub: "Der Dosierer lief die ganze Nacht perfekt. Seine Düse war halb verstopft.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Dünne Dichtungen durch eine verstopfte Klebstoffdüse", before: 140, after: 1, unit: "betroffene Monitore pro Düsenproblem",
    fixedLabel: "An der Quelle gefangen",
    takeaways: [
      { text: "Zuerst das Normale definieren", cue: "Definieren Sie zuerst das Normale" },
      { text: "Erkennen, stoppen, eindämmen: kein Fehler weitergegeben", cue: "Erkennen, stoppen und eindämmen Sie" },
      { text: "Jeder Stopp ist eine Lektion: Grundursache beheben", cue: "Und behandeln Sie jeden Stopp" },
    ],
    action: { text: "Wählen Sie einen automatischen Prozess, und notieren Sie, was ihn stoppen sollte.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "K", title: "Kaizen", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_DE_DURATION = PLAN.total;

export const JidokaDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
