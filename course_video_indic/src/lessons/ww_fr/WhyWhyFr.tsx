import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ww_fr/words.json";

// French version of WhyWhyFr (same design and polish as the English lesson).
// All data comes from narration/why_why_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "Dépasser la réponse facile jusqu'à une cause que l'on peut prouver",
  outroLine: "Définir. Prouver. Prévenir.",
  outroSub: "Why–Why — corriger la cause, pas la personne",
};

// Same polish as English WhyWhy; cues are phrases from the French intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "téléphones ont échoué à la charge au test final",
    sub: "Première réponse : erreur de l'opérateur. Deux jours plus tard, c'est revenu.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Échecs de charge sur la ligne 2", before: 50, after: 15, unit: "défauts de charge, volume égal",
    fixedLabel: "Cause racine corrigée : 70 % de moins",
    takeaways: [
      { text: "D'abord un problème précis, puis confiner", cue: "Partez d'un problème précis" },
      { text: "Une preuve pour chaque pourquoi, puis le tester", cue: "Appuyez chaque pourquoi" },
      { text: "Corrigez comment c'est arrivé et pourquoi ça s'est échappé", cue: "Et corrigez à la fois" },
    ],
    action: { text: "Prenez un défaut répété, et écrivez son énoncé 5W2H.", cue: "Voici votre action" },
    next: { letter: "X", title: "X-Matrix", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_FR_DURATION = PLAN.total;

export const WhyWhyFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
