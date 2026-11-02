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
import words from "../../captions/lc_hi/words.json";

// hi version of LowCostAutomationHi (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "सबसे सरल सुरक्षित डिवाइस जो काम कर दे",
  outroLine: "आसान बनाएँ। ज़रूरत ऑटोमेट करें। साबित करें।",
  outroSub: "Low Cost Automation — कभी कम सेफ़्टी नहीं",
};

// Same polish as English LowCostAutomation; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "मैलेट की ठोक घंटे में, हर ऑपरेटर",
    sub: "दुखती कलाइयाँ, और टेस्ट पर खड़खड़ाती ढीली ग्रिल।", until: "इस लेसन में",
  },
  recap: {
    problem: "मैलेट से बैठाने पर ढीली स्पीकर ग्रिल", before: 18, after: 2, unit: "प्रति 1,000 स्पीकर",
    fixedLabel: "4 महीने में वसूली",
    takeaways: [
      { text: "पहले आसान बनाएँ; वेस्ट कभी ऑटोमेट नहीं", cue: "पहले आसान बनाएँ" },
      { text: "सबसे सरल सुरक्षित हल; सेफ़्टी पहला गेट", cue: "ऐसा सबसे सरल" },
      { text: "असली फ़ायदा साबित करें, फिर रखरखाव", cue: "और असली फ़ायदा" },
    ],
    action: { text: "दोहराव वाली एक हरकत ढूँढें, और पूछें कि क्या ऑटोमेट करने से पहले उसे हटाया जा सकता है।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_HI_DURATION = PLAN.total;

export const LowCostAutomationHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
