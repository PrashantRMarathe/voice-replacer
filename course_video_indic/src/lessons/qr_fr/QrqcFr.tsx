import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/qr_fr/words.json";

// French version of QrqcFr (same design and polish as the English lesson).
// All data comes from narration/qrqc_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "Réagir en quelques minutes — clôturer avec des preuves",
  outroLine: "Détecter. Confiner. Prouver.",
  outroSub: "QRQC — réaction rapide, vraies preuves",
};

// Same polish as English QRQC; cues are phrases from the French intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "caméras échouant au test de mise au point à midi",
    sub: "Quelqu'un a réinitialisé le testeur, et la ligne a continué.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Caméras suspectes en route vers l'entrepôt", before: 2000, after: 0, unit: "caméras suspectes non retrouvées",
    takeaways: [
      { text: "Réagissez vite, mais avec des preuves", cue: "Réagissez vite" },
      { text: "Confinez d'abord, réconciliez chaque unité", cue: "Confinez d'abord" },
      { text: "Ne clôturez que quand la solution est prouvée", cue: "Et ne clôturez un problème" },
    ],
    action: { text: "Écrivez les 30 premières minutes de votre plan de réaction pour un défaut critique.", cue: "Voici votre action" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "Ensuite, vous approfondirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_FR_DURATION = PLAN.total;

export const QrqcFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
