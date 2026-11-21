import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/up_de/words.json";

// German version of UniformProductionDe (same design and polish as the English lesson).
// All data comes from narration/uniform_production_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "Menge und Mix glätten, für einen stetigen, verlässlichen Fluss",
  outroLine: "Glätten. Ordnen. Stabilisieren.",
  outroSub: "Uniform Production: ein stetiges Tempo, das Ihre Linie hält",
};

// Same polish as English UniformProduction; cues are phrases from the German intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "Handys am Montag. Fast keine am Dienstag.",
    sub: "Am Mittwoch ertrinkt der Prüfplatz.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Ein sehr holpriger Plan", before: 0, after: 6000, unit: "gute Einheiten am Tag, jeden Tag",
    fixedLabel: "Ein stetiges, glattes Tempo",
    takeaways: [
      { text: "Menge und Mix glätten", cue: "Glätten Sie Menge" },
      { text: "Zuerst Engpässe und Umrüstungen prüfen", cue: "Prüfen Sie Engpässe" },
      { text: "Ein sichtbarer Plan, klare Änderungsregeln", cue: "Und machen Sie den Plan" },
    ],
    action: { text: "Suchen Sie ein Produkt aus großer Charge, und skizzieren Sie ein kleineres, wiederholtes Muster.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "Als Nächstes bilden Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_DE_DURATION = PLAN.total;

export const UniformProductionDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
