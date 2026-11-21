import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/lc_fr/words.json";

// French version of LowCostAutomationFr (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "Le dispositif sûr le plus simple qui fait le travail",
  outroLine: "Simplifier. Automatiser le besoin. Le prouver.",
  outroSub: "Low Cost Automation — jamais basse sécurité",
};

// Same polish as English LowCostAutomation; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "coups de maillet par heure, par opérateur",
    sub: "Des poignets douloureux, et des grilles mal fixées qui vibraient au test.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Grilles d'enceinte mal fixées au maillet", before: 18, after: 2, unit: "pour 1 000 enceintes",
    fixedLabel: "Rentabilisé en 4 mois",
    takeaways: [
      { text: "Simplifiez d'abord ; n'automatisez jamais le gaspillage", cue: "Simplifiez d'abord" },
      { text: "La solution sûre la plus simple ; la sécurité comme premier filtre", cue: "Choisissez la solution sûre la plus simple" },
      { text: "Prouvez le bénéfice réel, puis entretenez-la", cue: "Et prouvez le bénéfice réel" },
    ],
    action: { text: "Trouvez un mouvement répétitif, et demandez-vous s'il peut être éliminé avant d'être automatisé.", cue: "Voici votre action" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_FR_DURATION = PLAN.total;

export const LowCostAutomationFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
