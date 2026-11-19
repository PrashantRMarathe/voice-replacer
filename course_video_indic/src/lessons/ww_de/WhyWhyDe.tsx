import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ww_de/words.json";

// German version of WhyWhyDe (same design and polish as the English lesson).
// All data comes from narration/why_why_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "An der bequemen Antwort vorbei zu einer beweisbaren Ursache",
  outroLine: "Definieren. Beweisen. Vorbeugen.",
  outroSub: "Why–Why: die Ursache beheben, nicht die Person",
};

// Same polish as English WhyWhy; cues are phrases from the German intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "Handys fielen im Endtest beim Laden durch",
    sub: "Erste Antwort: Bedienfehler. Zwei Tage später passierte es wieder.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Ladefehler an Linie 2", before: 50, after: 15, unit: "Ladefehler, gleiche Menge",
    fixedLabel: "Grundursache behoben: 70 % weniger",
    takeaways: [
      { text: "Zuerst ein scharfes Problem, dann eingrenzen", cue: "Beginnen Sie mit einem scharfen Problem" },
      { text: "Belege für jedes Warum, dann testen", cue: "Stützen Sie jedes Warum" },
      { text: "Beheben, wie es entstand und warum es durchrutschte", cue: "Und beheben Sie beides" },
    ],
    action: { text: "Nehmen Sie einen Wiederholfehler, und schreiben Sie seine 5W2H-Beschreibung.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "X", title: "X-Matrix", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_DE_DURATION = PLAN.total;

export const WhyWhyDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
