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
import words from "../../captions/kz_hi/words.json";

// hi version of KaizenHi (same design and polish as the English lesson).
// All data comes from narration/kaizen_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "छोटे बदलाव, हर दिन, काम करने वाले लोगों से",
  outroLine: "देखें। छोटा आज़माएँ। स्टैंडर्ड बनाएँ। दोहराएँ।",
  outroSub: "Kaizen — आज का सबसे अच्छा तरीका, कल की बेसलाइन",
};

// Same polish as English Kaizen; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "बार हर मॉनिटर पलटा जाता",
    sub: "मुँह नीचे, फिर मुँह ऊपर। हमेशा से ऐसा ही होता आया था।", until: "इस लेसन में",
  },
  recap: {
    problem: "मॉनिटर पलटने से पैनल स्क्रैच", before: 15, after: 3, unit: "स्क्रैच प्रति 1,000 मॉनिटर",
    fixedLabel: "90 दिन पर भी टिका",
    takeaways: [
      { text: "Kaizen रोज़ की आदत है", cue: "Kaizen रोज़ की" },
      { text: "छोटा परखें; जाँचें कि कुछ और न बिगड़े", cue: "छोटे स्तर पर" },
      { text: "हर फ़ायदे का स्टैंडर्ड बनाएँ", cue: "और हर फ़ायदे" },
    ],
    action: { text: "एक ऑपरेटर से पूछें कि उसके काम में मुश्किल क्या है, और एक छोटा हल परखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "L", title: "Low Cost Automation", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_HI_DURATION = PLAN.total;

export const KaizenHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
