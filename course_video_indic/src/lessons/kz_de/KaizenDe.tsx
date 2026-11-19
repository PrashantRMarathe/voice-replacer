import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/kz_de/words.json";

// German version of KaizenDe (same design and polish as the English lesson).
// All data comes from narration/kaizen_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "Kleine Änderungen, jeden Tag, von den Menschen an der Arbeit",
  outroLine: "Sehen. Klein testen. Standardisieren. Wiederholen.",
  outroSub: "Kaizen — die beste Methode von heute ist die Basis von morgen",
};

// Same polish as English Kaizen; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "Wendungen pro Monitor",
    sub: "Bildschirm nach unten, dann nach oben. Man hatte es immer so gemacht.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Verkratzte Panels durch das Wenden von Monitoren", before: 15, after: 3, unit: "Kratzer pro 1.000 Monitore",
    fixedLabel: "Nach 90 Tagen gehalten",
    takeaways: [
      { text: "Kaizen ist eine tägliche Gewohnheit", cue: "Kaizen ist eine tägliche Gewohnheit" },
      { text: "Klein testen; prüfen, dass nichts schlechter wurde", cue: "Testen Sie klein" },
      { text: "Jeden Gewinn standardisieren", cue: "Und standardisieren Sie jeden Gewinn" },
    ],
    action: { text: "Fragen Sie einen Werker, was seine Arbeit schwer macht, und testen Sie eine kleine Lösung.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "L", title: "Low Cost Automation", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_DE_DURATION = PLAN.total;

export const KaizenDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
