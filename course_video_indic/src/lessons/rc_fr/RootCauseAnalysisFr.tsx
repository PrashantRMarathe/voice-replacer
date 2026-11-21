import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/rc_fr/words.json";

// French version of RootCauseAnalysisFr (same design and polish as the English lesson).
// All data comes from narration/root_cause_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "Du symptôme à une cause que vous pouvez prouver",
  outroLine: "Définir. Tester. Prévenir.",
  outroSub: "Root Cause Analysis — le prouver, puis le corriger",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "caméras ont échoué au test de mise au point en une matinée",
    sub: "Trois personnes, trois réponses différentes.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Caméras échouant à la mise au point après un changement de série", before: 60, after: 12, unit: "défauts pour 20 000 caméras",
    takeaways: [
      { text: "Définissez-le avec précision, protégez le client", cue: "Définissez le problème avec précision" },
      { text: "Chaque cause est une hypothèse tant qu'elle n'est pas testée", cue: "Traitez chaque cause" },
      { text: "Corrigez pourquoi c'est arrivé, et pourquoi ça s'est échappé", cue: "Et corrigez à la fois" },
    ],
    action: { text: "Prenez un problème clôturé, et vérifiez si sa cause racine a été testée.", cue: "Voici votre action" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_FR_DURATION = PLAN.total;

export const RootCauseAnalysisFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
