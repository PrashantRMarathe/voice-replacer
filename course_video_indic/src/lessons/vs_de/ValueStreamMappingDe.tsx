import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/vs_de/words.json";

// German version of ValueStreamMappingDe (same design and polish as the English lesson).
// All data comes from narration/value_stream_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "Den ganzen Fluss sehen, vom Auftrag bis zur Lieferung",
  outroLine: "Sehen. Messen. Fließen.",
  outroSub: "Value Stream Mapping: das Warten finden, den Fluss gestalten",
};

// Same polish as English ValueStreamMapping; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "Minuten für Bau und Test einer Set-Top-Box",
    sub: "Und doch fast vier Tage bis zum Kunden.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Tage des Wartens für Minuten Arbeit", before: 4200, after: 2100, unit: "wartende Einheiten in drei Puffern",
    fixedLabel: "Soll-Zustand: halb so viel Warten",
    takeaways: [
      { text: "Den echten Material- und Informationsfluss abbilden", cue: "Bilden Sie den echten Fluss ab" },
      { text: "Die Durchlaufzeit steckt im Warten, nicht in der Arbeit", cue: "Der Großteil Ihrer Durchlaufzeit" },
      { text: "Den Soll-Zustand beweisen, bevor Bestand sinkt", cue: "Und gestalten Sie einen Soll-Zustand" },
    ],
    action: { text: "Gehen Sie eine Produktfamilie rückwärts vom Versand ab, und zählen Sie jeden Stapel.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_DE_DURATION = PLAN.total;

export const ValueStreamMappingDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
