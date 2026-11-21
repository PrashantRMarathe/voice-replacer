import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ew_de/words.json";

// German version of EliminationOfWasteDe (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "Beseitigen, was Ihr Kunde nicht bezahlen würde",
  outroLine: "Sehen. Ursache beseitigen. Beweisen.",
  outroSub: "Elimination of Waste — mehr Wert, weniger Aufwand",
};

// Same polish as English EliminationOfWaste; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "Soundbars jeden Monat nachgearbeitet",
    sub: "₹42 Reparatur pro Stück. Niemand hatte es je zusammengerechnet.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Soundbars wegen eines brummenden Lautsprecherkabels nachgearbeitet", before: 1500, after: 300, unit: "Nacharbeiten im Monat", fixedLabel: "Nacharbeit um 80 % gesenkt",
    takeaways: [
      { text: "Verschwendung: was der Kunde nicht bezahlen würde", cue: "Verschwendung ist alles" },
      { text: "Mit Fakten am Gemba finden", cue: "Finden Sie sie mit Fakten am Gemba" },
      { text: "Ursache beseitigen, beweisen, halten", cue: "Und beseitigen Sie die Ursache" },
    ],
    action: { text: "Gehen Sie dreißig Minuten Ihre Linie ab, und notieren Sie drei Verschwendungen als Fakten.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "F", title: "FMEA", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_DE_DURATION = PLAN.total;

export const EliminationOfWasteDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
