import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/qr_de/words.json";

// German version of QrqcDe (same design and polish as the English lesson).
// All data comes from narration/qrqc_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "In Minuten reagieren, mit Belegen abschließen",
  outroLine: "Erkennen. Eingrenzen. Beweisen.",
  outroSub: "QRQC: schnelle Reaktion, echte Belege",
};

// Same polish as English QRQC; cues are phrases from the German intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "Kameras bis Mittag im Fokustest durchgefallen",
    sub: "Jemand setzte den Tester zurück, und die Linie lief weiter.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Verdächtige Kameras auf dem Weg ins Lager", before: 2000, after: 0, unit: "verdächtige Kameras nicht erfasst",
    takeaways: [
      { text: "Schnell reagieren, aber mit Belegen", cue: "Reagieren Sie schnell" },
      { text: "Zuerst eingrenzen, jede Einheit abgleichen", cue: "Grenzen Sie zuerst ein" },
      { text: "Erst schließen, wenn die Lösung bewiesen ist", cue: "Und schließen Sie ein Problem" },
    ],
    action: { text: "Die ersten 30 Minuten Ihres Reaktionsplans für einen kritischen Fehler aufschreiben.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "Als Nächstes vertiefen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_DE_DURATION = PLAN.total;

export const QrqcDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
