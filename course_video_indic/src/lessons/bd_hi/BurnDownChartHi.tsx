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
import words from "../../captions/bd_hi/words.json";

// hi version of BurnDownChartHi (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "डेडलाइन से पहले बचा काम देखें",
  outroLine: "लाइन तय करें। गैप देखें। आज कदम उठाएँ।",
  outroSub: "Burn Down Chart — अब शुक्रवार के झटके नहीं",
};

// Same polish as English BurnDownChart; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "राउटर ट्रक से छूट गए",
    sub: "शुक्रवार दोपहर तक किसी को अंदाज़ा तक नहीं था।", until: "इस लेसन में",
  },
  recap: {
    problem: "डिस्पैच पर कम पड़े राउटर", before: 80, after: 0, unit: "राउटर कम",
    takeaways: [
      { text: "पहले आइडियल लाइन; उसे दोबारा कभी नहीं", cue: "पहले आइडियल लाइन" },
      { text: "सिर्फ़ पूरा और अच्छा काम गिनें", cue: "सिर्फ़ वही काम" },
      { text: "आइडियल से ऊपर? उसी दिन कदम, ओनर के साथ", cue: "और जब लाइन" },
    ],
    action: { text: "डेडलाइन वाला एक काम चुनें, और कल की शिफ़्ट से पहले उसका बर्न-डाउन बनाएँ।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "C", title: "Cycle Time Study", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_HI_DURATION = PLAN.total;

export const BurnDownChartHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
