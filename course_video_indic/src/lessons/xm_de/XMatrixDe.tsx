import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/xm_de/words.json";

// German version of XMatrixDe (same design and polish as the English lesson).
// All data comes from narration/x_matrix_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Strategie in Handeln verwandeln, mit Hoshin Kanri",
  outroLine: "Ausrichten. Umsetzen. Prüfen.",
  outroSub: "X-Matrix: Strategie, die Sie wirklich umsetzen",
};

// Same polish as English XMatrix; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "Verbesserungsprojekte, jedes Team beschäftigt",
    sub: "Und doch rutschte die Lieferung, Quartal für Quartal.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Ein volles Portfolio, rutschende Lieferung", before: 40, after: 3, unit: "Projekte, jedes mit einem Ziel und einem KPI verknüpft",
    fixedLabel: "Fokussiertes Portfolio",
    takeaways: [
      { text: "Wenige echte Prioritäten, keine Wunschliste", cue: "Wählen Sie wenige echte Prioritäten" },
      { text: "Ziel → Projekt → KPI → ein Eigentümer", cue: "Verbinden Sie jedes Ziel" },
      { text: "Ehrlich prüfen: die Zahlen müssen sich bewegen", cue: "Und prüfen Sie ehrlich" },
    ],
    action: { text: "Schreiben Sie ein Ziel für Ihren Bereich als Ergebnis, nicht als Tätigkeit.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "Y", title: "Yamazumi", cue: "Bis zum nächsten Mal" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_DE_DURATION = PLAN.total;

export const XMatrixDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
