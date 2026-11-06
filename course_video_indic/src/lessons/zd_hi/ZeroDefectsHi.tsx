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
import words from "../../captions/zd_hi/words.json";

// Hindi version of ZeroDefectsHi (same design and polish as the English lesson).
// All data comes from narration/zero_defects_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "डिफ़ेक्ट रोकें — सिर्फ़ उनकी जाँच न करें",
  outroLine: "रोकें। मापें। सुधारें।",
  outroSub: "Zero Defects — रोज़ के मैनेजमेंट में शामिल",
};

// Same polish as English ZeroDefects; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "फ़ोन रीवर्क के लिए लौटे",
    sub: "एक कनेक्टर, गलत तरीके से बैठा। वह हर विज़ुअल चेक में पास हुआ।", until: "इस लेसन में",
  },
  recap: {
    problem: "गलत बैठे कनेक्टर से चार्जिंग फ़ेल्योर", before: 1200, after: 200,
    unit: "फ़ेल फ़ोन, 40,000 में से", fixedLabel: "दोहराना मुश्किल: 83% कम",
    takeaways: [
      { text: "डिफ़ेक्ट रोकें, सिर्फ़ जाँच नहीं", cue: "डिफ़ेक्ट रोकें" },
      { text: "साफ़ परिभाषाओं के साथ ईमानदारी से मापें", cue: "साफ़ परिभाषाओं के साथ" },
      { text: "सिस्टम ठीक करें, व्यक्ति को नहीं", cue: "और जब कुछ फ़ेल" },
    ],
    action: { text: "बार-बार लौटने वाला एक डिफ़ेक्ट चुनें, और पूछें कि उसे नामुमकिन कैसे बनाएँ।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "Z", title: "Zero Defects", kicker: "लेसन पूरा", cue: "अब जाइए" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_HI_DURATION = PLAN.total;

export const ZeroDefectsHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
