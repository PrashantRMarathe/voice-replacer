import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/mm_de/words.json";

// German version of MudaMuraMuriDe (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "Verschwendung, Unausgeglichenheit und Überlastung: alle drei verbessern",
  outroLine: "Glätten. Schützen. Beseitigen.",
  outroSub: "Die 3M: stabiler Fluss, nicht schnellere Menschen",
};

// Same polish as English MudaMuraMuri; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "Kameras im Rückstand, eine Stunde vor Schichtende",
    sub: "Alle hetzen. Am Test häufen sich Fehler.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Sanjays Linie war jeden Tag zu spät", before: 150, after: 0, unit: "Minuten Überstunden pro Tag",
    takeaways: [
      { text: "Muda Verschwendung, Mura Unausgeglichenheit, Muri Überlastung", cue: "Muda ist Verschwendung" },
      { text: "Sie nähren einander: gemeinsam verbessern", cue: "Sie nähren einander" },
      { text: "Stabiler Fluss, nicht schnellere Menschen", cue: "Und das Ziel ist" },
    ],
    action: { text: "Begleiten Sie ein Produkt durch Ihre Linie, und markieren Sie ein Beispiel für jedes M.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "N", title: "Next Inspection", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_DE_DURATION = PLAN.total;

export const MudaMuraMuriDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
