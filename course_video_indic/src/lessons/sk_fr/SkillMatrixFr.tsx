import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/sk_fr/words.json";

// French version of SkillMatrixFr (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "Qui peut vraiment faire quel travail — et où sont les écarts",
  outroLine: "Évaluer. Former. Couvrir.",
  outroSub: "Skill Matrix — une maîtrise vivante des compétences",
};

// Same polish as English SkillMatrix; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "personne capable de régler la mise au point des objectifs",
    sub: "Bala était malade. À dix heures, toute la cellule était à l'arrêt.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Un seul expert en mise au point, et il était malade", before: 1, after: 2, unit: "experts qualifiés en mise au point des objectifs",
    takeaways: [
      { text: "Capacité démontrée, pas présence", cue: "Une matrice de compétences montre" },
      { text: "Comptez les remplaçants qualifiés, dans chaque équipe", cue: "Comptez les remplaçants qualifiés" },
      { text: "Gardez-la vivante, avec des preuves", cue: "Et gardez-la vivante" },
    ],
    action: { text: "Listez vos trois postes les plus critiques, et comptez les personnes qualifiées pour chacun.", cue: "Voici votre action" },
    next: { letter: "T", title: "TAKT Time", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_FR_DURATION = PLAN.total;

export const SkillMatrixFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
