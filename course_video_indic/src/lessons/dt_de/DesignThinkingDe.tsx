import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/dt_de/words.json";

// German version of DesignThinkingDe (same design and polish as the English lesson).
// All data comes from narration/design_thinking_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "Das richtige Problem lösen, mit den Menschen, die die Arbeit machen",
  outroLine: "Beobachten. Definieren. Klein testen.",
  outroSub: "Design Thinking — zuerst die Menschen, immer Belege",
};

// Same polish as English DesignThinking; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "Etikettenfehler pro 1.000 Pumpen",
    sub: "Die erste Idee: ein teurer, schnellerer Drucker. Niemand hatte die Packer gefragt.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Etikettenfehler beim Verpacken von Infusionspumpen", before: 12, after: 2, unit: "pro 1.000 Pumpen",
    takeaways: [
      { text: "Bei den Menschen beginnen; beobachten, bevor Sie entscheiden", cue: "Beginnen Sie bei den Menschen" },
      { text: "Den Bedarf definieren, ohne Lösung darin", cue: "Definieren Sie den Bedarf" },
      { text: "Klein testen: Ergebnisse und echte Nutzung", cue: "Und testen Sie klein" },
    ],
    action: { text: "Beobachten Sie zehn Zyklen einer mühsamen Arbeit, und sprechen Sie mit drei Menschen, die sie machen.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "E", title: "Elimination of Waste", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_DE_DURATION = PLAN.total;

export const DesignThinkingDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
