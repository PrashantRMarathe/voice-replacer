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
import words from "../../captions/up_hi/words.json";

// Hindi version of UniformProductionHi (same design and polish as the English lesson).
// All data comes from narration/uniform_production_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "वॉल्यूम और मिक्स लेवल करें, स्थिर और भरोसेमंद फ़्लो के लिए",
  outroLine: "लेवल करें। क्रम तय करें। स्थिर बनाएँ।",
  outroSub: "Uniform Production — ऐसी रफ़्तार, जो आपकी लाइन बनाए रख सके",
};

// Same polish as English UniformProduction; cues are phrases from the Hindi intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "फ़ोन सोमवार को। मंगलवार को लगभग कुछ नहीं।",
    sub: "बुधवार तक, टेस्ट बेंच काम में डूबी है।", until: "इस लेसन में",
  },
  recap: {
    problem: "एक बहुत उबड़-खाबड़ शेड्यूल", before: 0, after: 6000, unit: "अच्छी यूनिट रोज़, हर दिन",
    fixedLabel: "एक स्थिर, लेवल रफ़्तार",
    takeaways: [
      { text: "वॉल्यूम और मिक्स, दोनों लेवल करें", cue: "वॉल्यूम और मिक्स, दोनों" },
      { text: "पहले बॉटलनेक और चेंजओवर जाँचें", cue: "किसी पैटर्न पर" },
      { text: "दिखने वाला प्लान, बदलाव के साफ़ नियम", cue: "और प्लान को" },
    ],
    action: { text: "बड़े बैच में बनने वाला एक प्रोडक्ट ढूँढें, और छोटे, दोहराए पैटर्न का स्केच बनाएँ।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_HI_DURATION = PLAN.total;

export const UniformProductionHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
