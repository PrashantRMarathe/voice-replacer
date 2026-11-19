import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/hc_fr/words.json";

// French version of HanchoFr (same design and polish as the English lesson).
// All data comes from narration/hancho_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "Le leadership sur le terrain, chaque heure de chaque équipe",
  outroLine: "Dirigez au Gemba. Faites grandir les personnes.",
  outroSub: "Hancho — rétablir les standards, s'améliorer chaque jour",
};

// Same polish as English Hancho; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV de moins par heure, pendant toute une équipe",
    sub: "Personne ne l'a remarqué avant le rapport du lendemain matin.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Écart de production après un changement de modèle", before: 98, after: 120, unit: "TV par heure",
    fixedLabel: "Rattrapé dans la même équipe",
    takeaways: [
      { text: "Dirigez depuis le Gemba : standard face au réel", cue: "Dirigez depuis le Gemba" },
      { text: "Rendez les écarts visibles chaque heure ; réagissez dans la même équipe", cue: "Rendez chaque écart visible" },
      { text: "Faites grandir les personnes, pour que la ligne ne dépende pas de vous", cue: "Et faites grandir vos équipes" },
    ],
    action: { text: "Écrivez votre propre travail standard de responsable, pour une équipe.", cue: "Voici votre action" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_FR_DURATION = PLAN.total;

export const HanchoFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
