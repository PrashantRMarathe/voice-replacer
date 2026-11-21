import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/pk_fr/words.json";

// French version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "Rendre la mauvaise action impossible",
  outroLine: "Éliminer. Empêcher. Détecter.",
  outroSub: "Poka Yoke — sortir la mémoire de la qualité",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_FR_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "enregistreurs partis avec une vis manquante",
    sub: "L'opératrice était compétente, et attentive. Simplement humaine.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Enregistreurs partis avec une vis manquante", before: 18, after: 1, unit: "pour 10 000 unités",
    takeaways: [
      { text: "Les erreurs sont prévisibles : éliminez-les dès la conception", cue: "Les erreurs sont prévisibles" },
      { text: "Prévenir, puis détecter, puis avertir", cue: "Préférez la prévention" },
      { text: "Testez chaque dispositif avec de mauvais échantillons", cue: "Et testez chaque dispositif" },
    ],
    action: { text: "Trouvez un contrôle qui repose sur la mémoire, et esquissez un Poka Yoke pour lui.", cue: "Voici votre action" },
    next: { letter: "Q", title: "QRQC", cue: "Ensuite, vous découvrirez le QRQC" },
  },
};

export const PokaYokeFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
