import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/gb_de/words.json";

// German version of GembaDe (same design and polish as the English lesson).
// All data comes from narration/gemba_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "Echter Ort, echtes Ding, echte Fakten",
  outroLine: "Hingehen. Sehen. Bestätigen.",
  outroSub: "Gemba, Genbutsu, Genjitsu — Fakten vor Entscheidungen",
};

// Same polish as English Gemba; cues are phrases from the German intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× die Ohrhörer-Fehler in Schicht B",
    sub: "Der Plan: Schicht B neu schulen. Niemand hatte einen defekten Ohrhörer angesehen.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Ohrhörer fallen beim Audiotest durch", before: 20, after: 8, unit: "Fehler pro 1.000 Ohrhörer",
    fixedLabel: "An der Ursache behoben",
    takeaways: [
      { text: "An den echten Ort gehen; echte Zyklen beobachten", cue: "Gehen Sie an den echten Ort" },
      { text: "Das echte Ding halten; mit einem guten vergleichen", cue: "Nehmen Sie das echte Ding" },
      { text: "Die echten Fakten prüfen, mit Nenner", cue: "Und prüfen Sie die echten Fakten" },
    ],
    action: { text: "Nehmen Sie ein wiederkehrendes Problem, und machen Sie einen dreißigminütigen 3G-Besuch.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "H", title: "Hancho", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_DE_DURATION = PLAN.total;

export const GembaDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
