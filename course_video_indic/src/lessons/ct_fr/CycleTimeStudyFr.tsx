import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ct_fr/words.json";

// French version of CycleTimeStudyFr (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "Mesurer le vrai travail, trouver le vrai goulot",
  outroLine: "Définir. Mesurer. Améliorer la méthode.",
  outroSub: "Cycle Time Study — des preuves avant la vitesse",
};

// Same polish as English CycleTimeStudy; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "secondes : chaque poste semblait assez rapide",
    sub: "Pourtant, la ligne de moniteurs ratait son objectif horaire, équipe après équipe.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Poste de test d'écran plus lent que le TAKT", before: 28, after: 23, unit: "secondes par moniteur au poste C", fixedLabel: "Maintenant dans le TAKT",
    takeaways: [
      { text: "Définissez d'abord la limite", cue: "Définissez d'abord la limite" },
      { text: "Regardez la dispersion, pas seulement la moyenne", cue: "Regardez la dispersion" },
      { text: "Corrigez la méthode, ne sautez jamais les contrôles qualité", cue: "Et corrigez la méthode" },
    ],
    action: { text: "Chronométrez dix cycles sur un poste, et comparez le plus long au TAKT.", cue: "Voici votre action" },
    next: { letter: "D", title: "Design Thinking", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_FR_DURATION = PLAN.total;

export const CycleTimeStudyFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
