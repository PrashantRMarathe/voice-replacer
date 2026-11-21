import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/vs_fr/words.json";

// French version of ValueStreamMappingFr (same design and polish as the English lesson).
// All data comes from narration/value_stream_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "Voir tout le flux, de la commande à la livraison",
  outroLine: "Voir. Mesurer. Faire circuler.",
  outroSub: "Value Stream Mapping — trouver l'attente, concevoir le flux",
};

// Same polish as English ValueStreamMapping; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "minutes pour fabriquer et tester un décodeur",
    sub: "Pourtant près de quatre jours pour arriver chez le client.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Des jours d'attente pour des minutes de travail", before: 4200, after: 2100, unit: "unités en attente dans trois stocks tampons",
    fixedLabel: "État futur : moitié moins d'attente",
    takeaways: [
      { text: "Cartographiez le flux réel de matière + information", cue: "Cartographiez le flux réel" },
      { text: "Le délai se cache dans l'attente, pas dans le travail", cue: "La plus grande partie de votre délai" },
      { text: "Prouvez l'état futur avant de réduire le stock", cue: "Et concevez un état futur" },
    ],
    action: { text: "Parcourez une famille de produits à rebours depuis l'expédition, et comptez chaque tas que vous croisez.", cue: "Voici votre action" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_FR_DURATION = PLAN.total;

export const ValueStreamMappingFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
