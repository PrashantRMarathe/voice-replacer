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
import words from "../../captions/vs_hi/words.json";

// Hindi version of ValueStreamMappingHi (same design and polish as the English lesson).
// All data comes from narration/value_stream_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "ऑर्डर से डिलीवरी तक, पूरा फ़्लो देखें",
  outroLine: "देखें। मापें। फ़्लो बनाएँ।",
  outroSub: "Value Stream Mapping — इंतज़ार ढूँढें, फ़्लो डिज़ाइन करें",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "मिनट, एक सेट-टॉप बॉक्स बनाने और टेस्ट करने में",
    sub: "फिर भी ग्राहक तक पहुँचने में लगभग चार दिन।", until: "इस लेसन में",
  },
  recap: {
    problem: "मिनटों के काम के लिए दिनों का इंतज़ार", before: 4200, after: 2100, unit: "तीन बफ़र में इंतज़ार करती यूनिट",
    fixedLabel: "फ़्यूचर स्टेट: आधा इंतज़ार",
    takeaways: [
      { text: "असली मटीरियल + जानकारी फ़्लो का नक्शा", cue: "असली फ़्लो का नक्शा" },
      { text: "लीड टाइम इंतज़ार में छिपा है, काम में नहीं", cue: "आपका ज़्यादातर लीड" },
      { text: "स्टॉक घटाने से पहले फ़्यूचर स्टेट साबित करें", cue: "और कोई भी स्टॉक" },
    ],
    action: { text: "एक प्रोडक्ट फ़ैमिली के साथ डिस्पैच से उल्टा चलें, और हर ढेर गिनें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_HI_DURATION = PLAN.total;

export const ValueStreamMappingHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
