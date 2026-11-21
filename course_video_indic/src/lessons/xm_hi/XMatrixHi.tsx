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
import words from "../../captions/xm_hi/words.json";

// Hindi version of XMatrixHi (same design and polish as the English lesson).
// All data comes from narration/x_matrix_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri से रणनीति को एक्शन में बदलें",
  outroLine: "जोड़ें। लागू करें। रिव्यू करें।",
  outroSub: "X-Matrix — ऐसी रणनीति, जिसे आप सच में लागू कर सकें",
};

// Same polish as English XMatrix; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "इम्प्रूवमेंट प्रोजेक्ट, हर टीम व्यस्त",
    sub: "फिर भी डिलीवरी हर तिमाही फिसलती रही।", until: "इस लेसन में",
  },
  recap: {
    problem: "व्यस्त पोर्टफ़ोलियो, फिसलती डिलीवरी", before: 40, after: 3, unit: "प्रोजेक्ट, हर एक किसी लक्ष्य और KPI से जुड़ा",
    fixedLabel: "फ़ोकस्ड पोर्टफ़ोलियो",
    takeaways: [
      { text: "कुछ असली प्राथमिकताएँ, इच्छाओं की सूची नहीं", cue: "कुछ असली प्राथमिकताएँ" },
      { text: "लक्ष्य → प्रोजेक्ट → KPI → एक ओनर", cue: "हर लक्ष्य को" },
      { text: "ईमानदार रिव्यू: नंबर हिलने चाहिए", cue: "और ईमानदारी से" },
    ],
    action: { text: "अपने एरिया के लिए एक उद्देश्य लिखें, नतीजे के रूप में, काम के रूप में नहीं।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "Y", title: "Yamazumi", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_HI_DURATION = PLAN.total;

export const XMatrixHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
