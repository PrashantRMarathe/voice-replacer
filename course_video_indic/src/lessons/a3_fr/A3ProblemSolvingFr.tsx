import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/a3_fr/words.json";

// French version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "Toute l'histoire du problème sur une page",
  outroLine: "Voyez l'écart. Prouvez la cause. Pérennisez.",
  outroSub: "A3 — mieux réfléchir, sur une seule feuille",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_FR_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "serveurs ont échoué à leur premier test de démarrage",
    sub: "En quatre semaines. Première solution proposée : deux contrôleurs de plus.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Serveurs échouant à leur premier test de démarrage", before: 48, after: 16, unit: "pour 1 000 serveurs", fixedLabel: "Cible atteinte : contre 48 avant",
    takeaways: [
      { text: "Partez d'un écart mesurable", cue: "Partez d'un écart mesurable" },
      { text: "Allez voir ; prouvez chaque cause", cue: "Allez voir" },
      { text: "Ne standardisez que ce que le pilote a prouvé", cue: "Et ne standardisez que" },
    ],
    action: { text: "Choisissez un problème récurrent, et écrivez son énoncé sur une feuille A3.", cue: "Voici votre action" },
    next: { letter: "B", title: "Burn Down Chart", cue: "Ensuite, vous découvrirez" },
  },
};

export const A3ProblemSolvingFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
