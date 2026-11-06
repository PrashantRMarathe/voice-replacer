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
import words from "../../captions/ni_hi/words.json";

// hi version of NextInspectionHi (same design and polish as the English lesson).
// All data comes from narration/next_inspection_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "अगला प्रोसेस मेरा ग्राहक है",
  outroLine: "न बनाएँ। न भेजें। न स्वीकारें।",
  outroSub: "Next Inspection — अगले प्रोसेस को बचाएँ",
};

// Same polish as English NextInspection; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "ढीला कनेक्टर, स्टेशन तीन पर",
    sub: "किसी ने ध्यान नहीं दिया। फिर एक ग्राहक ने बॉक्स खोला।", until: "इस लेसन में",
  },
  recap: {
    problem: "आगे के स्टेशन तक निकलते डिफ़ेक्ट", before: 18, after: 3, unit: "एस्केप हर हफ़्ते",
    takeaways: [
      { text: "न बनाएँ, न भेजें, न स्वीकारें", cue: "डिफ़ेक्ट न बनाएँ" },
      { text: "जल्दी जाँचें, तेज़ी से कदम उठाएँ", cue: "ज़रूरी पॉइंट जल्द" },
      { text: "कंट्रोल ऊपर की ओर ले जाते रहें", cue: "और अपने कंट्रोल" },
    ],
    action: { text: "एक हैंडऑफ़ चुनें, और लिखें कि अगले प्रोसेस को उससे क्या चाहिए।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "O", title: "One Point Lesson", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_HI_DURATION = PLAN.total;

export const NextInspectionHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
