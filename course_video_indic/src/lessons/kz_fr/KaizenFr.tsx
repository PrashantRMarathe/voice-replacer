import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/kz_fr/words.json";

// French version of KaizenFr (same design and polish as the English lesson).
// All data comes from narration/kaizen_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "De petits changements, chaque jour, par les personnes qui font le travail",
  outroLine: "Observer. Essayer en petit. Standardiser. Recommencer.",
  outroSub: "Kaizen — la meilleure méthode d'aujourd'hui est la base de demain",
};

// Same polish as English Kaizen; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "retournements de chaque moniteur",
    sub: "Face en bas, puis face en haut. On avait toujours fait comme ça.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Dalles rayées par le retournement des moniteurs", before: 15, after: 3, unit: "rayures pour 1 000 moniteurs",
    fixedLabel: "Tenu à 90 jours",
    takeaways: [
      { text: "Le Kaizen est une habitude quotidienne", cue: "Le Kaizen est une habitude quotidienne" },
      { text: "Testez en petit ; vérifiez que rien d'autre ne s'est dégradé", cue: "Testez en petit" },
      { text: "Standardisez chaque gain", cue: "Et standardisez chaque gain" },
    ],
    action: { text: "Demandez à un opérateur ce qui rend son travail difficile, et testez une petite solution.", cue: "Voici votre action" },
    next: { letter: "L", title: "Low Cost Automation", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_FR_DURATION = PLAN.total;

export const KaizenFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
