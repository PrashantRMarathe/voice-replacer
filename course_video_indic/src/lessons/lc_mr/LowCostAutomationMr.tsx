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
import words from "../../captions/lc_mr/words.json";

// Marathi version of LowCostAutomationMr (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "काम करणारं सर्वात सोपं सुरक्षित डिव्हाइस",
  outroLine: "सोपं करा. गरज ऑटोमेट करा. सिद्ध करा.",
  outroSub: "Low Cost Automation — कधीही कमी सेफ्टी नाही",
};

// Same polish as English LowCostAutomation; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "मॅलेटचे ठोके तासाला, प्रत्येक ऑपरेटर",
    sub: "दुखणारी मनगटं, आणि टेस्टवर खडखडणाऱ्या सैल ग्रिल.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "मॅलेटने बसवल्याने सैल स्पीकर ग्रिल", before: 18, after: 2, unit: "प्रति 1,000 स्पीकर",
    fixedLabel: "4 महिन्यांत वसुली",
    takeaways: [
      { text: "आधी सोपं करा; वेस्ट कधीच ऑटोमेट नाही", cue: "आधी सोपं करा" },
      { text: "सर्वात सोपा सुरक्षित उपाय; सेफ्टी पहिला गेट", cue: "काम करणारा सर्वात" },
      { text: "खरा फायदा सिद्ध करा, मग देखभाल", cue: "आणि खरा फायदा" },
    ],
    action: { text: "पुनरावृत्तीची एक हालचाल शोधा, आणि विचारा की ऑटोमेट करण्याआधी ती काढता येईल का.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_MR_DURATION = PLAN.total;

export const LowCostAutomationMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
