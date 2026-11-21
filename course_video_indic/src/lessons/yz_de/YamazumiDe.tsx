import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/yz_de/words.json";

// German version of YamazumiDe (same design and polish as the English lesson).
// All data comes from narration/yamazumi_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "Die Linie gegen den TAKT abstimmen, mit echten Daten",
  outroLine: "Messen. Stapeln. Abstimmen.",
  outroSub: "Yamazumi: ein Fluss, der hält, durch Gestaltung",
};

// Same polish as English Yamazumi; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "Werker warten, während einer in Schrauben versinkt",
    sub: "Niemand ist faul. Die Arbeit ist nur ungleich gestapelt.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Station B über dem TAKT", before: 35, after: 30, unit: "Sekunden Arbeit an Station B",
    fixedLabel: "Wieder unter dem TAKT",
    takeaways: [
      { text: "Echte Arbeit messen, nicht den Bestfall", cue: "Messen Sie die echte Arbeit" },
      { text: "Gegen den TAKT stapeln, um Häufungen zu sehen", cue: "Stapeln Sie sie gegen den TAKT" },
      { text: "Neu abstimmen, ohne Sicherheit oder Qualität zu riskieren", cue: "Und stimmen Sie sorgfältig neu ab" },
    ],
    action: { text: "Messen Sie eine Station Ihrer Linie, und zeichnen Sie ihren Balken gegen den TAKT.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "Z", title: "Zero Defects", cue: "Bis zum nächsten Mal" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_DE_DURATION = PLAN.total;

export const YamazumiDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
