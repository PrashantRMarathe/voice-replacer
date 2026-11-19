import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/gb_fr/words.json";

// French version of GembaFr (same design and polish as the English lesson).
// All data comes from narration/gemba_fr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_fr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "Lieu réel, chose réelle, faits réels",
  outroLine: "Allez. Voyez. Confirmez.",
  outroSub: "Gemba, Genbutsu, Genjitsu — les faits avant les décisions",
};

// Same polish as English Gemba; cues are phrases from the French intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× les défaillances d'écouteurs dans l'équipe B",
    sub: "Le plan : reformer l'équipe B. Personne n'avait regardé un écouteur défaillant.", until: "Dans cette leçon",
  },
  recap: {
    problem: "Écouteurs échouant au test audio", before: 20, after: 8, unit: "défaillances pour 1 000 écouteurs",
    fixedLabel: "Corrigé à la cause",
    takeaways: [
      { text: "Allez au lieu réel ; observez de vrais cycles", cue: "Allez au lieu réel" },
      { text: "Prenez la chose réelle ; comparez-la à une bonne", cue: "Prenez la chose réelle" },
      { text: "Vérifiez les faits réels, avec un dénominateur", cue: "Et vérifiez les faits réels" },
    ],
    action: { text: "Prenez un problème récurrent, et faites une visite 3G de trente minutes.", cue: "Voici votre action" },
    next: { letter: "H", title: "Hancho", cue: "Ensuite, vous découvrirez" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_FR_DURATION = PLAN.total;

export const GembaFr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("fr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
