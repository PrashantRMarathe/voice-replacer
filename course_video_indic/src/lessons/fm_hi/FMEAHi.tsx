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
import words from "../../captions/fm_hi/words.json";

// hi version of FMEAHi (same design and polish as the English lesson).
// All data comes from narration/fmea_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "फ़ेल्योर मोड एंड इफ़ेक्ट्स एनालिसिस: फ़ेल्योर से पहले सोचें",
  outroLine: "चेन बनाएँ। स्कोर दें। रोकें।",
  outroSub: "FMEA — एक जीवित प्लान, फ़ॉर्म नहीं",
};

// Same polish as English FMEA; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "आउटडोर रेडियो पानी से भरकर लौटे",
    sub: "दो में गैस्केट गायब, चार में मुड़ा। सब फ़ाइनल इंस्पेक्शन में पास थे।", until: "इस लेसन में",
  },
  recap: {
    problem: "आउटडोर 5G रेडियो पर गैस्केट का जोखिम", before: 240, after: 32, unit: "रिस्क प्रायोरिटी नंबर",
    fixedLabel: "जोखिम घटा, ट्रायल में साबित",
    takeaways: [
      { text: "असर → फ़ेल्योर मोड → कंट्रोल होने वाली वजह", cue: "एक साफ़ चेन" },
      { text: "सबूत से स्कोर; नंबर से ऊपर समझ", cue: "सबूत के साथ" },
      { text: "पहले रोकथाम, साबित करें, फिर दोबारा स्कोर", cue: "और रोकथाम को" },
    ],
    action: { text: "एक ज़रूरी कदम चुनें, और अपनी टीम के साथ उसकी फ़ेल्योर चेन लिखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "G", title: "Gemba", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_HI_DURATION = PLAN.total;

export const FMEAHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
