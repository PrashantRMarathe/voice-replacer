import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/tt_de/words.json";

// German version of TaktTimeDe (same design and polish as the English lesson).
// All data comes from narration/takt_time_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "Der Takt, den Ihr Kunde vorgibt",
  outroLine: "Messen. Abstimmen. Fließen.",
  outroSub: "TAKT Time: das Tempo des Kunden",
};

// Same polish as English TaktTime; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "Kameras vor dem Test auf Vorrat gebaut",
    sub: "Jede Station beschäftigt. Der Lkw fuhr trotzdem zu spät.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Eine beschäftigte Linie verpasst den Lkw", before: 0, after: 10, unit: "Sekunden: der Takt für 7.200 Kameras pro Tag",
    fixedLabel: "Das Tempo, nach dem alle arbeiten",
    takeaways: [
      { text: "TAKT = netto verfügbare Zeit ÷ Bedarf", cue: "TAKT ist die netto verfügbare" },
      { text: "Das nötige Tempo, nicht die Zeit einer Station", cue: "Es ist das nötige Tempo" },
      { text: "Mit echten Verlusten planen, nicht mit Theorie", cue: "Und planen Sie mit echten" },
    ],
    action: { text: "Berechnen Sie den TAKT für eine Linie, und vergleichen Sie ihn mit Ihrer langsamsten Station.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "U", title: "Uniform Production", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_DE_DURATION = PLAN.total;

export const TaktTimeDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
