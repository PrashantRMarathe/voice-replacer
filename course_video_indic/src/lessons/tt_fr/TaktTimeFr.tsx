import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/tt_fr/words.json";

// French version of TaktTimeFr (same design and polish as the English lesson).
// All data comes from narration/takt_time_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "Le battement fixé par votre client",
  outroLine: "Mesurer. Équilibrer. Faire circuler.",
  outroSub: "TAKT Time — le rythme du client",
};

// Same polish as English TaktTime; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "caméras fabriquées avant le test",
    sub: "Chaque poste occupé. Le camion est quand même parti en retard.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Une ligne occupée, qui rate quand même le camion", before: 0, after: 10, unit: "secondes : le battement pour 7 200 caméras par jour",
    fixedLabel: "Le rythme sur lequel tout le monde travaille",
    takeaways: [
      { text: "TAKT = temps net disponible ÷ demande", cue: "Le TAKT est le temps net disponible" },
      { text: "Le rythme nécessaire, pas le temps d'un poste", cue: "C'est le rythme nécessaire" },
      { text: "Planifiez avec les pertes réelles, pas avec la théorie", cue: "Et planifiez avec les pertes réelles" },
    ],
    action: { text: "Calculez le TAKT d'une ligne, et comparez-le à votre poste le plus lent.", cue: "Voici votre action" },
    next: { letter: "U", title: "Uniform Production", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_FR_DURATION = PLAN.total;

export const TaktTimeFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
