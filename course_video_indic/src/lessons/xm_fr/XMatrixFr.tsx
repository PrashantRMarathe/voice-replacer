import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/xm_fr/words.json";

// French version of XMatrixFr (same design and polish as the English lesson).
// All data comes from narration/x_matrix_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Transformer la stratégie en action avec le Hoshin Kanri",
  outroLine: "Aligner. Déployer. Revoir.",
  outroSub: "X-Matrix — une stratégie que vous pouvez vraiment exécuter",
};

// Same polish as English XMatrix; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "projets d'amélioration, toutes les équipes occupées",
    sub: "Pourtant, la livraison glissait encore, trimestre après trimestre.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Un portefeuille chargé, une livraison qui glisse", before: 40, after: 3, unit: "projets, chacun relié à un objectif et un KPI",
    fixedLabel: "Portefeuille ciblé",
    takeaways: [
      { text: "Quelques vraies priorités, pas une liste de souhaits", cue: "Choisissez quelques vraies priorités" },
      { text: "Objectif → projet → KPI → un responsable", cue: "Reliez chaque objectif" },
      { text: "Revues honnêtes : les chiffres doivent bouger", cue: "Et faites des revues honnêtes" },
    ],
    action: { text: "Écrivez un objectif pour votre zone sous forme de résultat, pas d'activité.", cue: "Voici votre action" },
    next: { letter: "Y", title: "Yamazumi", cue: "À bientôt pour la suite" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_FR_DURATION = PLAN.total;

export const XMatrixFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
