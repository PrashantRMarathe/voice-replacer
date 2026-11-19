import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ik_fr/words.json";

// French version of IshikawaFr (same design and polish as the English lesson).
// All data comes from narration/ishikawa_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "Chercher large avec l'arête de poisson, puis prouver la cause",
  outroLine: "Cherchez large. Prouvez précis.",
  outroSub: "Ishikawa — chaque arête est une supposition tant qu'elle n'est pas testée",
};

// Same polish as English Ishikawa; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "switchs pour 1 000 échouent au test de ports",
    sub: "Contre 5 avant. La réponse de la réunion : acheter un nouveau testeur.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Échecs de liaison des ports sur la ligne de switchs", before: 32, after: 4, unit: "pour 1 000 switchs",
    fixedLabel: "Les deux causes corrigées",
    takeaways: [
      { text: "Un effet précis et mesurable dans la tête", cue: "Mettez un effet précis" },
      { text: "Cherchez largement dans les 6M, sans reproche", cue: "Cherchez largement" },
      { text: "Chaque arête est une supposition tant qu'elle n'est pas prouvée", cue: "Et traitez chaque arête" },
    ],
    action: { text: "Dessinez une arête de poisson pour un problème récurrent, et choisissez trois causes à tester.", cue: "Voici votre action" },
    next: { letter: "J", title: "Jidoka", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_FR_DURATION = PLAN.total;

export const IshikawaFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
