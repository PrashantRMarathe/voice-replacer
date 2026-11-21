import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ni_de/words.json";

// German version of NextInspectionDe (same design and polish as the English lesson).
// All data comes from narration/next_inspection_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "Der nächste Prozess ist mein Kunde",
  outroLine: "Nicht machen. Nicht weitergeben. Nicht annehmen.",
  outroSub: "Next Inspection: den nächsten Prozess schützen",
};

// Same polish as English NextInspection; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "lockerer Stecker an Station drei",
    sub: "Niemand bemerkte ihn. Dann öffnete ein Kunde den Karton.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Fehler, die zu späteren Stationen durchrutschen", before: 18, after: 3, unit: "Durchschlupfe pro Woche",
    takeaways: [
      { text: "Nicht machen, nicht weitergeben, nicht annehmen", cue: "Keinen Fehler machen" },
      { text: "Früh prüfen, schnell reagieren", cue: "Prüfen Sie kritische Punkte" },
      { text: "Kontrollen weiter nach vorn verlegen", cue: "Und verlegen Sie" },
    ],
    action: { text: "Wählen Sie eine Übergabe, und notieren Sie, was der nächste Prozess davon braucht.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "O", title: "One Point Lesson", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_DE_DURATION = PLAN.total;

export const NextInspectionDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
