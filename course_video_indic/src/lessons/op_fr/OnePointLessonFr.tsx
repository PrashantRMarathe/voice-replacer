import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/op_fr/words.json";

// French version of OnePointLessonFr (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "Un sujet. Un point clair. Une meilleure action.",
  outroLine: "Simple. Visuelle. Juste.",
  outroSub: "One Point Lesson — bien enseigner un point",
};

// Same polish as English OnePointLesson; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "connecteur monté à l'envers, et fissuré",
    sub: "L'équipe de jour connaissait l'astuce. Personne ne l'avait partagée.", until: "Dans cette leçon",
  },
  recap: {
    problem: "L'équipe de nuit fissurait des connecteurs", before: 14, after: 1, unit: "connecteurs fissurés par semaine",
    takeaways: [
      { text: "Un sujet, un point, un visuel fort", cue: "Un sujet" },
      { text: "Enseignez au Gemba, puis observez le travail", cue: "Enseignez-la au Gemba" },
      { text: "Gardez-la conforme au standard en vigueur", cue: "Et maîtrisez-la" },
    ],
    action: { text: "Choisissez une erreur qui se répète, et rédigez un brouillon de One Point Lesson pour elle.", cue: "Voici votre action" },
    next: { letter: "P", title: "Poka Yoke", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_FR_DURATION = PLAN.total;

export const OnePointLessonFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
