import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/bd_de/words.json";

// German version of BurnDownChartDe (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "Die Restarbeit sehen, vor dem Termin",
  outroLine: "Die Linie planen. Die Lücke verfolgen. Heute handeln.",
  outroSub: "Burn Down Chart — keine Überraschungen mehr am Freitag",
};

// Same polish as English BurnDownChart; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "Router verpassten den Lkw",
    sub: "Niemand sah es kommen, bis Freitagnachmittag.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Fehlende Router beim Versand", before: 80, after: 0, unit: "Router zu wenig",
    takeaways: [
      { text: "Zuerst die Ideallinie zeichnen; nie neu zeichnen", cue: "Zeichnen Sie zuerst die Ideallinie" },
      { text: "Nur fertige und gute Arbeit zählen", cue: "Zählen Sie nur Arbeit" },
      { text: "Über der Ideallinie? Am selben Tag handeln, mit einem Verantwortlichen", cue: "Und wenn die Linie" },
    ],
    action: { text: "Wählen Sie eine Arbeit mit Termin, und zeichnen Sie ihr Diagramm vor der morgigen Schicht.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "C", title: "Cycle Time Study", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_DE_DURATION = PLAN.total;

export const BurnDownChartDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
