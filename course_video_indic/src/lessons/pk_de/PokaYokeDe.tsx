import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/pk_de/words.json";

// German version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "Die falsche Handlung unmöglich machen",
  outroLine: "Beseitigen. Verhindern. Erkennen.",
  outroSub: "Poka Yoke — das Gedächtnis aus der Qualität nehmen",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_DE_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "Rekorder mit fehlender Schraube ausgeliefert",
    sub: "Die Werkerin war geschickt und sorgfältig. Einfach ein Mensch.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Rekorder mit fehlender Schraube ausgeliefert", before: 18, after: 1, unit: "pro 10.000 Einheiten",
    takeaways: [
      { text: "Fehler sind vorhersehbar: konstruieren Sie sie heraus", cue: "Fehler sind vorhersehbar" },
      { text: "Verhindern, dann erkennen, dann warnen", cue: "Vermeiden ist besser" },
      { text: "Prüfen Sie jede Vorrichtung mit schlechten Mustern", cue: "Und prüfen Sie jede" },
    ],
    action: { text: "Suchen Sie eine Prüfung, die auf dem Gedächtnis beruht, und skizzieren Sie ein Poka Yoke dafür.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "Q", title: "QRQC", cue: "Als Nächstes lernen Sie QRQC kennen" },
  },
};

export const PokaYokeDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
