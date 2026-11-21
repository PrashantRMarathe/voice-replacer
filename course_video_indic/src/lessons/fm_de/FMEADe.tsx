import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/fm_de/words.json";

// German version of FMEADe (same design and polish as the English lesson).
// All data comes from narration/fmea_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "Fehlermöglichkeits- und Einflussanalyse: denken vor dem Versagen",
  outroLine: "Verketten. Bewerten. Verhindern.",
  outroSub: "FMEA — ein lebender Plan, kein Formular",
};

// Same polish as English FMEA; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "Außengeräte kamen voller Wasser zurück",
    sub: "Dichtung fehlte bei zwei, verdreht bei vier. Alle bestanden die Endkontrolle.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Dichtungsrisiko am 5G-Außengerät", before: 240, after: 32, unit: "Risikoprioritätszahl",
    fixedLabel: "Risiko gesenkt, im Versuch bewiesen",
    takeaways: [
      { text: "Folge → Fehlerart → beherrschbare Ursache", cue: "Bauen Sie eine klare Kette" },
      { text: "Mit Belegen bewerten; Urteil vor Zahlen", cue: "Bewerten Sie mit Belegen" },
      { text: "Zuerst verhindern, beweisen, dann neu bewerten", cue: "Und bevorzugen Sie Vermeidung" },
    ],
    action: { text: "Wählen Sie einen kritischen Schritt, und schreiben Sie mit Ihrem Team seine Fehlerkette auf.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "G", title: "Gemba", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_DE_DURATION = PLAN.total;

export const FMEADe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
