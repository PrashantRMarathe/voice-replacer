import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/zd_de/words.json";

// German version of ZeroDefectsDe (same design and polish as the English lesson).
// All data comes from narration/zero_defects_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "Fehler verhindern, nicht nur prüfen",
  outroLine: "Verhindern. Messen. Verbessern.",
  outroSub: "Zero Defects: in die tägliche Führung eingebaut",
};

// Same polish as English ZeroDefects; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "Handys zur Nacharbeit zurück",
    sub: "Ein Stecker, schlecht gesetzt. Er bestand jede Sichtprüfung.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Ladefehler durch einen schlecht gesetzten Stecker", before: 1200, after: 200,
    unit: "durchgefallene Handys, von 40.000", fixedLabel: "Schwer wiederholbar gemacht: 83 % weniger",
    takeaways: [
      { text: "Fehler verhindern, nicht nur prüfen", cue: "Verhindern Sie Fehler" },
      { text: "Ehrlich messen, mit klaren Definitionen", cue: "Messen Sie ehrlich" },
      { text: "Das System beheben, nicht die Person", cue: "Und wenn etwas schiefgeht" },
    ],
    action: { text: "Wählen Sie einen Fehler, der immer wiederkommt, und fragen Sie, wie Sie ihn unmöglich machen.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "Z", title: "Zero Defects", kicker: "LEKTION ABGESCHLOSSEN", cue: "Bis zum nächsten Mal" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_DE_DURATION = PLAN.total;

export const ZeroDefectsDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
