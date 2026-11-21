import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ew_fr/words.json";

// French version of EliminationOfWasteFr (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "Supprimer ce que votre client ne paierait pas",
  outroLine: "Voyez-le. Supprimez la cause. Prouvez-le.",
  outroSub: "Elimination of Waste — plus de valeur, moins d'effort",
};

// Same polish as English EliminationOfWaste; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "barres de son retouchées chaque mois",
    sub: "₹42 chacune à réparer. Personne n'avait jamais fait le total.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Barres de son retouchées pour un fil de haut-parleur qui grésille", before: 1500, after: 300, unit: "retouches par mois", fixedLabel: "Retouches réduites de 80 %",
    takeaways: [
      { text: "Gaspillage : ce que le client ne paierait pas", cue: "Le gaspillage est tout" },
      { text: "Trouvez-le avec des faits au Gemba", cue: "Trouvez-le avec des faits au Gemba" },
      { text: "Supprimez la cause, prouvez-le, maintenez-le", cue: "Et supprimez la cause" },
    ],
    action: { text: "Parcourez votre ligne pendant trente minutes, et notez trois gaspillages sous forme de faits.", cue: "Voici votre action" },
    next: { letter: "F", title: "FMEA", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_FR_DURATION = PLAN.total;

export const EliminationOfWasteFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
