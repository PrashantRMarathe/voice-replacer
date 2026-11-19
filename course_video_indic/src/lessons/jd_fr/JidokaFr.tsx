import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/jd_fr/words.json";

// French version of JidokaFr (same design and polish as the English lesson).
// All data comes from narration/jidoka_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "L'automatisation à visage humain",
  outroLine: "Voyez-le. Arrêtez-le. Résolvez-le.",
  outroSub: "Jidoka — aucun défaut transmis, aucune anomalie cachée",
};

// Same polish as English Jidoka; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "moniteurs patient avec un joint trop fin",
    sub: "Le doseur a parfaitement tourné toute la nuit. Sa buse était à moitié bouchée.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Joints trop fins dus à une buse de colle bouchée", before: 140, after: 1, unit: "moniteurs touchés par problème de buse",
    fixedLabel: "Attrapé à la source",
    takeaways: [
      { text: "Définissez d'abord le normal", cue: "Définissez d'abord le normal" },
      { text: "Détecter, arrêter, confiner : aucun défaut transmis", cue: "Détectez, arrêtez et confinez" },
      { text: "Chaque arrêt est une leçon : corrigez la cause racine", cue: "Et traitez chaque arrêt" },
    ],
    action: { text: "Choisissez un processus automatique, et notez ce qui devrait le faire s'arrêter.", cue: "Voici votre action" },
    next: { letter: "K", title: "Kaizen", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_FR_DURATION = PLAN.total;

export const JidokaFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
