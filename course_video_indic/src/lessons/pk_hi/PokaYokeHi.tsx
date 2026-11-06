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
import words from "../../captions/pk_hi/words.json";

// Hindi version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "गलत काम को असंभव बनाएँ",
  outroLine: "हटाएँ। रोकें। पकड़ें।",
  outroSub: "Poka Yoke — क्वालिटी को याददाश्त के भरोसे से बाहर निकालें",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_HI_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "रिकॉर्डर एक स्क्रू के बिना भेजे गए",
    sub: "ऑपरेटर कुशल और सावधान थी। बस इंसान।", until: "इस लेसन में",
  },
  recap: {
    problem: "रिकॉर्डर गायब स्क्रू के साथ भेजे गए", before: 18, after: 1, unit: "प्रति 10,000 यूनिट",
    takeaways: [
      { text: "गलतियों का अनुमान लगता है: उन्हें डिज़ाइन से हटाएँ", cue: "गलतियों का अनुमान" },
      { text: "पहले रोकें, फिर पकड़ें, फिर चेतावनी", cue: "चेतावनी से बेहतर" },
      { text: "हर डिवाइस को खराब सैंपल से परखें", cue: "और हर डिवाइस" },
    ],
    action: { text: "याददाश्त पर टिका एक चेक ढूँढें, और उसके लिए Poka Yoke का स्केच बनाएँ।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "Q", title: "QRQC", cue: "आगे, आप QRQC" },
  },
};

export const PokaYokeHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
