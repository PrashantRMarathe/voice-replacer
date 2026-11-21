import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ni_fr/words.json";

// French version of NextInspectionFr (same design and polish as the English lesson).
// All data comes from narration/next_inspection_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "Le processus suivant est mon client",
  outroLine: "Ne faites pas. Ne transmettez pas. N'acceptez pas.",
  outroSub: "Next Inspection — protéger le processus suivant",
};

// Same polish as English NextInspection; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "connecteur mal enfiché au poste trois",
    sub: "Personne ne l'a remarqué. Puis un client a ouvert le carton.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Des défauts qui s'échappent vers les postes suivants", before: 18, after: 3, unit: "fuites par semaine",
    takeaways: [
      { text: "Ne faites pas, ne transmettez pas, n'acceptez pas", cue: "Ne faites pas" },
      { text: "Contrôlez tôt, et réagissez vite", cue: "Contrôlez les points critiques" },
      { text: "Remontez les contrôles vers l'amont", cue: "Et continuez à remonter" },
    ],
    action: { text: "Choisissez un passage de relais, et notez ce dont le processus suivant a besoin.", cue: "Voici votre action" },
    next: { letter: "O", title: "One Point Lesson", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_FR_DURATION = PLAN.total;

export const NextInspectionFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
