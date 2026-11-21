import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ik_de/words.json";

// German version of IshikawaDe (same design and polish as the English lesson).
// All data comes from narration/ishikawa_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "Breit suchen mit der Fischgräte, dann die Ursache beweisen",
  outroLine: "Breit suchen. Gezielt beweisen.",
  outroSub: "Ishikawa — jede Gräte ist eine Vermutung, bis sie getestet ist",
};

// Same polish as English Ishikawa; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "Switches pro 1.000 fallen beim Port-Test durch",
    sub: "Vorher 5. Die Antwort des Meetings: einen neuen Tester kaufen.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Port-Link-Fehler an der Switch-Linie", before: 32, after: 4, unit: "pro 1.000 Switches",
    fixedLabel: "Beide Ursachen behoben",
    takeaways: [
      { text: "Eine scharfe, messbare Wirkung im Kopf", cue: "Setzen Sie eine scharfe" },
      { text: "Breit über die 6M suchen, ohne Schuld", cue: "Suchen Sie breit" },
      { text: "Jede Gräte ist eine Vermutung, bis sie bewiesen ist", cue: "Und behandeln Sie jede Gräte" },
    ],
    action: { text: "Zeichnen Sie eine Fischgräte für ein wiederkehrendes Problem, und wählen Sie drei Ursachen zum Testen.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "J", title: "Jidoka", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_DE_DURATION = PLAN.total;

export const IshikawaDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
