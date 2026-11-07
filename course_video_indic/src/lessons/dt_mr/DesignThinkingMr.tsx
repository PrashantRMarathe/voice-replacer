import React from "react";
import { PageLesson, LessonText } from "../shared/PageLesson";
import type { Polish } from "../shared/polish";
import { planLesson, LessonData, Page, Quiz, Word } from "../plan";
import { fps } from "../../theme";
import { ensureIndicFont } from "../../indicFonts";
import { setUI } from "../../ui";
import timings from "./timings.json";
import content from "./content.json";
import quizzes from "./quizzes.json";
import words from "../../captions/dt_mr/words.json";

// Marathi version of DesignThinkingMr (same design and polish as the English lesson).
// All data comes from narration/design_thinking_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "योग्य समस्या सोडवा, काम करणाऱ्यांसोबत",
  outroLine: "पाहा. व्याख्या करा. छोटं तपासा.",
  outroSub: "Design Thinking — आधी लोक, नेहमी पुरावा",
};

// Same polish as English DesignThinking; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "प्रत्येक 1,000 पंपांमागे लेबल चुका",
    sub: "पहिली कल्पना: एक महागडा जलद प्रिंटर. पॅकर्सना कोणी विचारलंच नाही.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "इन्फ्युजन पंप पॅकिंगवर लेबल चुका", before: 12, after: 2, unit: "प्रति 1,000 पंप",
    takeaways: [
      { text: "लोकांपासून सुरुवात; निर्णयाआधी पाहा", cue: "काम करणाऱ्या लोकांपासून" },
      { text: "गरजेची व्याख्या, तिच्यात उपाय नाही", cue: "गरजेची व्याख्या अशी" },
      { text: "छोटं तपासा: निकाल आणि खरा वापर", cue: "आणि छोट्या प्रमाणात" },
    ],
    action: { text: "एखाद्या त्रासदायक कामाचे दहा सायकल पाहा, आणि ते करणाऱ्या तीन लोकांशी बोला.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "E", title: "Elimination of Waste", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_MR_DURATION = PLAN.total;

export const DesignThinkingMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
