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
import words from "../../captions/ew_hi/words.json";

// hi version of EliminationOfWasteHi (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "जिसके लिए ग्राहक पैसे न दे, उसे हटाएँ",
  outroLine: "देखें। वजह हटाएँ। साबित करें।",
  outroSub: "Elimination of Waste — ज़्यादा वैल्यू, कम मेहनत",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "साउंडबार का हर महीने रीवर्क",
    sub: "हर एक ठीक करने में ₹42। किसी ने कभी इसे जोड़ा ही नहीं था।", until: "इस लेसन में",
  },
  recap: {
    problem: "भनभनाते स्पीकर तार से रीवर्क होते साउंडबार", before: 1500, after: 300, unit: "रीवर्क प्रति महीना", fixedLabel: "रीवर्क 80% घटा",
    takeaways: [
      { text: "वेस्ट: जिसके ग्राहक पैसे न दे", cue: "वेस्ट वह सब" },
      { text: "इसे Gemba पर तथ्यों से ढूँढें", cue: "इसे Gemba पर" },
      { text: "वजह हटाएँ, साबित करें, टिकाएँ", cue: "और वजह हटाएँ" },
    ],
    action: { text: "तीस मिनट अपनी लाइन पर चलें, और तीन वेस्ट तथ्यों के रूप में लिखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "F", title: "FMEA", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_HI_DURATION = PLAN.total;

export const EliminationOfWasteHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
