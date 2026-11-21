import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/up_fr/words.json";

// French version of UniformProductionFr (same design and polish as the English lesson).
// All data comes from narration/uniform_production_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "Lisser le volume et le mix pour un flux régulier et fiable",
  outroLine: "Lisser. Séquencer. Stabiliser.",
  outroSub: "Uniform Production — un rythme régulier que votre ligne peut tenir",
};

// Same polish as English UniformProduction; cues are phrases from the French intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "téléphones le lundi. Presque rien le mardi.",
    sub: "Mercredi, le banc de test est noyé.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Un planning très chaotique", before: 0, after: 6000, unit: "bonnes unités par jour, chaque jour",
    fixedLabel: "Un rythme régulier et lissé",
    takeaways: [
      { text: "Lissez à la fois le volume et le mix", cue: "Lissez à la fois le volume" },
      { text: "Vérifiez d'abord les goulots et les changements de série", cue: "Vérifiez les goulots" },
      { text: "Un plan visible, des règles de changement claires", cue: "Et rendez le plan visible" },
    ],
    action: { text: "Trouvez un produit fabriqué en gros lot, et esquissez un schéma plus petit qui se répète.", cue: "Voici votre action" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "Ensuite, vous allez cartographier" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_FR_DURATION = PLAN.total;

export const UniformProductionFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
