import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/fm_fr/words.json";

// French version of FMEAFr (same design and polish as the English lesson).
// All data comes from narration/fmea_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "Analyse des modes de défaillance et de leurs effets : réfléchir avant la défaillance",
  outroLine: "Enchaînez. Notez. Prévenez.",
  outroSub: "FMEA — un plan vivant, pas un formulaire",
};

// Same polish as English FMEA; cues are phrases from the French intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "radios extérieures revenues pleines d'eau",
    sub: "Joint manquant sur deux, tordu sur quatre. Toutes avaient passé l'inspection finale.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Risque du joint sur la radio 5G extérieure", before: 240, after: 32, unit: "indice de priorité du risque",
    fixedLabel: "Risque réduit, prouvé par un essai",
    takeaways: [
      { text: "Effet → mode de défaillance → cause maîtrisable", cue: "Construisez une chaîne claire" },
      { text: "Notez avec des preuves ; le jugement avant les chiffres", cue: "Notez avec des preuves" },
      { text: "Prévenez d'abord, prouvez-le, puis renotez", cue: "Et préférez la prévention" },
    ],
    action: { text: "Choisissez une étape critique, et écrivez sa chaîne de défaillance avec votre équipe.", cue: "Voici votre action" },
    next: { letter: "G", title: "Gemba", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_FR_DURATION = PLAN.total;

export const FMEAFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
