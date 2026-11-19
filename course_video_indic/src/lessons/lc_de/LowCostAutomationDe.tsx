import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/lc_de/words.json";

// German version of LowCostAutomationDe (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_de.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_de",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "Die einfachste sichere Vorrichtung, die die Arbeit macht",
  outroLine: "Vereinfachen. Den Bedarf automatisieren. Beweisen.",
  outroSub: "Low Cost Automation — nie geringe Sicherheit",
};

// Same polish as English LowCostAutomation; cues are phrases from the German intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "Hammerschläge pro Stunde, pro Werker",
    sub: "Schmerzende Handgelenke, und lockere Gitter, die beim Test klapperten.", until: "In dieser Lektion",
  },
  recap: {
    problem: "Lockere Lautsprechergitter durch Einsetzen mit dem Hammer", before: 18, after: 2, unit: "pro 1.000 Lautsprecher",
    fixedLabel: "Amortisiert in 4 Monaten",
    takeaways: [
      { text: "Zuerst vereinfachen; nie Verschwendung automatisieren", cue: "Vereinfachen Sie zuerst" },
      { text: "Einfachste sichere Lösung; Sicherheit als erste Hürde", cue: "Wählen Sie die einfachste" },
      { text: "Den echten Nutzen beweisen, dann warten", cue: "Und beweisen Sie den echten Nutzen" },
    ],
    action: { text: "Suchen Sie eine wiederholte Bewegung, und fragen Sie, ob sie wegfallen kann, bevor Sie sie automatisieren.", cue: "Ihre Aufgabe für diese Woche" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "Als Nächstes lernen Sie" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_DE_DURATION = PLAN.total;

export const LowCostAutomationDe: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  setUI("de");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
