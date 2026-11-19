import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/dt_fr/words.json";

// French version of DesignThinkingFr (same design and polish as the English lesson).
// All data comes from narration/design_thinking_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "Résoudre le bon problème, avec les personnes qui font le travail",
  outroLine: "Observer. Définir. Tester en petit.",
  outroSub: "Design Thinking — d'abord les personnes, toujours des preuves",
};

// Same polish as English DesignThinking; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "erreurs d'étiquette pour 1 000 pompes",
    sub: "La première idée : une imprimante plus rapide et coûteuse. Personne n'avait demandé aux emballeurs.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Erreurs d'étiquette à l'emballage des pompes à perfusion", before: 12, after: 2, unit: "pour 1 000 pompes",
    takeaways: [
      { text: "Partez des personnes ; observez avant de décider", cue: "Partez des personnes" },
      { text: "Définissez le besoin, sans solution dedans", cue: "Définissez le besoin" },
      { text: "Testez en petit : résultats et usage réel", cue: "Et testez en petit" },
    ],
    action: { text: "Observez dix cycles d'un travail pénible, et parlez à trois personnes qui le font.", cue: "Voici votre action" },
    next: { letter: "E", title: "Elimination of Waste", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_FR_DURATION = PLAN.total;

export const DesignThinkingFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
