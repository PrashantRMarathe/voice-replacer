import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/zd_fr/words.json";

// French version of ZeroDefectsFr (same design and polish as the English lesson).
// All data comes from narration/zero_defects_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "Prévenir les défauts — ne pas seulement les inspecter",
  outroLine: "Prévenir. Mesurer. Améliorer.",
  outroSub: "Zero Defects — intégré au management quotidien",
};

// Same polish as English ZeroDefects; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "téléphones revenus en retouche",
    sub: "Un connecteur, mal enfoncé. Il a passé tous les contrôles visuels.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Échecs de charge dus à un connecteur mal enfoncé", before: 1200, after: 200,
    unit: "téléphones en échec, sur 40 000", fixedLabel: "Rendu difficile à répéter : 83 % de moins",
    takeaways: [
      { text: "Prévenez les défauts, ne vous contentez pas d'inspecter", cue: "Prévenez les défauts" },
      { text: "Mesurez honnêtement, avec des définitions claires", cue: "Mesurez honnêtement" },
      { text: "Corrigez le système, pas la personne", cue: "Et quand quelque chose échoue" },
    ],
    action: { text: "Choisissez un défaut qui revient sans cesse, et demandez-vous comment le rendre impossible.", cue: "Voici votre action" },
    next: { letter: "Z", title: "Zero Defects", kicker: "LEÇON TERMINÉE", cue: "À bientôt pour la suite" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_FR_DURATION = PLAN.total;

export const ZeroDefectsFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
