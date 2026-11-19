import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/yz_fr/words.json";

// French version of YamazumiFr (same design and polish as the English lesson).
// All data comes from narration/yamazumi_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "Équilibrez la ligne face au TAKT — avec des données réelles",
  outroLine: "Mesurer. Empiler. Équilibrer.",
  outroSub: "Yamazumi — un flux qui tient, par conception",
};

// Same polish as English Yamazumi; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "opérateurs qui attendent, pendant qu'un seul croule sous les vis",
    sub: "Personne n'est paresseux. Le travail est simplement empilé de façon inégale.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Poste B au-dessus du TAKT", before: 35, after: 30, unit: "secondes de travail au poste B",
    fixedLabel: "De retour sous le TAKT",
    takeaways: [
      { text: "Mesurez le vrai travail, pas le meilleur cas", cue: "Mesurez le vrai travail" },
      { text: "Empilez-le face au TAKT pour voir les accumulations", cue: "Empilez-le face au TAKT" },
      { text: "Rééquilibrez sans risquer la sécurité ni la qualité", cue: "Et rééquilibrez avec soin" },
    ],
    action: { text: "Chronométrez un poste de votre ligne, et tracez sa barre face au TAKT.", cue: "Votre action cette semaine" },
    next: { letter: "Z", title: "Zero Defects", cue: "À bientôt pour la suite" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_FR_DURATION = PLAN.total;

export const YamazumiFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
