import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/rc_de/words.json";

// German version of RootCauseAnalysisDe (same design and polish as the English lesson).
// All data comes from narration/root_cause_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "Vom Symptom zu einer beweisbaren Ursache",
  outroLine: "Definieren. Testen. Vorbeugen.",
  outroSub: "Root Cause Analysis: erst beweisen, dann beheben",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "Kameras an einem Vormittag im Fokustest durchgefallen",
    sub: "Drei Leute, drei verschiedene Antworten.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Kameras fallen nach einem Wechsel im Fokus durch", before: 60, after: 12, unit: "Fehler pro 20.000 Kameras",
    takeaways: [
      { text: "Scharf definieren, den Kunden schützen", cue: "Definieren Sie das Problem scharf" },
      { text: "Jede Ursache ist eine Hypothese, bis sie getestet ist", cue: "Behandeln Sie jede Ursache" },
      { text: "Beheben, warum es entstand und warum es durchrutschte", cue: "Und beheben Sie beides" },
    ],
    action: { text: "Nehmen Sie ein abgeschlossenes Problem, und prüfen Sie, ob seine Grundursache je getestet wurde.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_DE_DURATION = PLAN.total;

export const RootCauseAnalysisDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
