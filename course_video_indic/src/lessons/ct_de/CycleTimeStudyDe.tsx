import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/ct_de/words.json";

// German version of CycleTimeStudyDe (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "Die echte Arbeit messen, den echten Engpass finden",
  outroLine: "Definieren. Messen. Methode verbessern.",
  outroSub: "Cycle Time Study — Belege vor Tempo",
};

// Same polish as English CycleTimeStudy; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "Sekunden: jede Station schien schnell genug",
    sub: "Trotzdem verfehlte die Monitorlinie ihr Stundenziel, Schicht um Schicht.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Display-Teststation langsamer als der TAKT", before: 28, after: 23, unit: "Sekunden pro Monitor an Station C", fixedLabel: "Jetzt innerhalb des TAKT",
    takeaways: [
      { text: "Zuerst die Grenze festlegen", cue: "Legen Sie zuerst die Grenze fest" },
      { text: "Auf die Streuung schauen, nicht nur auf den Durchschnitt", cue: "Schauen Sie auf die Streuung" },
      { text: "Methode verbessern, nie Qualitätsprüfungen auslassen", cue: "Und verbessern Sie die Methode" },
    ],
    action: { text: "Messen Sie zehn Zyklen an einer Station, und vergleichen Sie den längsten mit dem TAKT.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "D", title: "Design Thinking", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_DE_DURATION = PLAN.total;

export const CycleTimeStudyDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
