import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/mm_fr/words.json";

// French version of MudaMuraMuriFr (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "Gaspillage, irrégularité et surcharge — améliorez les trois",
  outroLine: "Lisser. Protéger. Supprimer.",
  outroSub: "Les 3M — un flux stable, pas des gens plus rapides",
};

// Same polish as English MudaMuraMuri; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "caméras de retard, une heure avant la fin de l'équipe",
    sub: "Tout le monde se précipite. Les erreurs s'accumulent au test.", until: "Dans cette leçon",
  },
  recap: {
    problem: "La ligne de Sanjay finissait en retard chaque jour", before: 150, after: 0, unit: "minutes d'heures supplémentaires par jour",
    takeaways: [
      { text: "Muda gaspillage, Mura irrégularité, Muri surcharge", cue: "Muda, c'est le gaspillage" },
      { text: "Ils s'alimentent : améliorez-les ensemble", cue: "Ils s'alimentent les uns les autres" },
      { text: "Un flux stable, pas des gens plus rapides", cue: "Et l'objectif est" },
    ],
    action: { text: "Suivez un produit le long de votre ligne, et repérez un exemple de chaque M.", cue: "Voici votre action" },
    next: { letter: "N", title: "Next Inspection", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_FR_DURATION = PLAN.total;

export const MudaMuraMuriFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
