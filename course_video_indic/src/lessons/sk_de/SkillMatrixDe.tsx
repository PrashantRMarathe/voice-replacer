import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/sk_de/words.json";

// German version of SkillMatrixDe (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "Wer welche Arbeit wirklich kann, und wo die Lücken sind",
  outroLine: "Bewerten. Schulen. Abdecken.",
  outroSub: "Skill Matrix: eine lebende Kompetenzsteuerung",
};

// Same polish as English SkillMatrix; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "Person kann den Linsenfokus einrichten",
    sub: "Bala meldete sich krank. Um zehn stand die ganze Zelle.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Ein Experte für Linsenfokus, und er war krank", before: 1, after: 2, unit: "qualifizierte Experten für Linsenfokus",
    takeaways: [
      { text: "Nachgewiesenes Können, nicht Anwesenheit", cue: "Eine Qualifikationsmatrix zeigt" },
      { text: "Qualifizierte Vertretungen zählen, jede Schicht", cue: "Zählen Sie qualifizierte Vertretungen" },
      { text: "Lebendig halten, mit Belegen", cue: "Und halten Sie sie lebendig" },
    ],
    action: { text: "Listen Sie Ihre drei kritischsten Stationen, und zählen Sie die Qualifizierten für jede.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "T", title: "TAKT Time", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_DE_DURATION = PLAN.total;

export const SkillMatrixDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
