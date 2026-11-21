import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/hc_de/words.json";

// German version of HanchoDe (same design and polish as the English lesson).
// All data comes from narration/hancho_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "Führung in der Fertigung, jede Stunde jeder Schicht",
  outroLine: "Am Gemba führen. Menschen entwickeln.",
  outroSub: "Hancho — Standards wiederherstellen, jeden Tag verbessern",
};

// Same polish as English Hancho; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV pro Stunde zu wenig, eine ganze Schicht lang",
    sub: "Niemand merkte es bis zum Bericht am nächsten Morgen.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Mengenlücke nach einem Modellwechsel", before: 98, after: 120, unit: "TV pro Stunde",
    fixedLabel: "In derselben Schicht aufgeholt",
    takeaways: [
      { text: "Vom Gemba aus führen: Standard gegen Ist", cue: "Führen Sie vom Gemba aus" },
      { text: "Lücken stündlich sichtbar machen; in derselben Schicht reagieren", cue: "Machen Sie jede Lücke sichtbar" },
      { text: "Menschen entwickeln, damit die Linie nicht von Ihnen abhängt", cue: "Und entwickeln Sie Ihre Leute" },
    ],
    action: { text: "Schreiben Sie Ihre eigene Führungs-Standardarbeit für eine Schicht.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_DE_DURATION = PLAN.total;

export const HanchoDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
