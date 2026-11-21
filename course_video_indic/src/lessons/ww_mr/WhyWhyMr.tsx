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
import words from "../../captions/ww_mr/words.json";

// Marathi version of WhyWhyMr (same design and polish as the English lesson).
// All data comes from narration/why_why_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "सोप्या उत्तराच्या पलीकडे, सिद्ध करता येईल अशा कारणापर्यंत",
  outroLine: "व्याख्या करा. सिद्ध करा. रोखा.",
  outroSub: "Why–Why — कारण दुरुस्त करा, व्यक्ती नाही",
};

// Same polish as English WhyWhy; cues are phrases from the Marathi intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "फोन फायनल टेस्टमध्ये चार्जिंगमध्ये फेल",
    sub: "पहिलं उत्तर: ऑपरेटरची चूक. दोन दिवसांनी, पुन्हा तेच झालं.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "लाइन 2 वर चार्जिंग फेल्युअर", before: 50, after: 15, unit: "चार्जिंग डिफेक्ट, तोच व्हॉल्यूम",
    fixedLabel: "रूट कॉज दुरुस्त: 70% कमी",
    takeaways: [
      { text: "आधी धारदार समस्या, मग कंटेनमेंट", cue: "एका धारदार समस्येने" },
      { text: "प्रत्येक का चा पुरावा, मग तपासा", cue: "प्रत्येक का मागे" },
      { text: "कसं घडलं आणि का निसटलं, दोन्ही दुरुस्त करा", cue: "आणि दोन्ही दुरुस्त" },
    ],
    action: { text: "वारंवार होणारा एक डिफेक्ट घ्या, आणि त्याचं 5W2H स्टेटमेंट लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "X", title: "X-Matrix", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_MR_DURATION = PLAN.total;

export const WhyWhyMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
