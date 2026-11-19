import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/bd_fr/words.json";

// French version of BurnDownChartFr (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "Voir le travail restant, avant l'échéance",
  outroLine: "Tracez la ligne. Suivez l'écart. Agissez aujourd'hui.",
  outroSub: "Burn Down Chart — fini les surprises du vendredi",
};

// Same polish as English BurnDownChart; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "routeurs ont raté le camion",
    sub: "Personne ne l'a vu venir, jusqu'au vendredi après-midi.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Routeurs manquants à l'expédition", before: 80, after: 0, unit: "routeurs en moins",
    takeaways: [
      { text: "Tracez d'abord la ligne idéale ; ne la redessinez jamais", cue: "Tracez d'abord la ligne idéale" },
      { text: "Ne comptez que le travail terminé et bon", cue: "Ne comptez que le travail" },
      { text: "Au-dessus de l'idéal ? Agissez le jour même, avec un responsable", cue: "Et quand la ligne" },
    ],
    action: { text: "Choisissez un travail avec une échéance, et tracez son graphique avant l'équipe de demain.", cue: "Voici votre action" },
    next: { letter: "C", title: "Cycle Time Study", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_FR_DURATION = PLAN.total;

export const BurnDownChartFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
