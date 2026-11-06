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
import words from "../../captions/qr_hi/words.json";

// Hindi version of QrqcHi (same design and polish as the English lesson).
// All data comes from narration/qrqc_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "मिनटों में कदम — सबूत के साथ बंद",
  outroLine: "पकड़ें। रोकें। साबित करें।",
  outroSub: "QRQC — तेज़ रिस्पॉन्स, असली सबूत",
};

// Same polish as English QRQC; cues are phrases from the Hindi intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "कैमरे दोपहर तक फ़ोकस टेस्ट में फ़ेल",
    sub: "किसी ने टेस्टर रीसेट किया, और लाइन चलती रही।", until: "इस लेसन में",
  },
  recap: {
    problem: "वेयरहाउस की ओर जाते शक वाले कैमरे", before: 2000, after: 0, unit: "शक वाले कैमरे बिना हिसाब",
    takeaways: [
      { text: "तेज़ी से कदम, पर सबूत के साथ", cue: "तेज़ी से कदम" },
      { text: "पहले कंटेनमेंट, हर यूनिट का हिसाब", cue: "पहले कंटेनमेंट" },
      { text: "हल साबित होने पर ही बंद करें", cue: "और किसी मुद्दे" },
    ],
    action: { text: "किसी एक गंभीर डिफ़ेक्ट के लिए अपने रिस्पॉन्स प्लान के पहले 30 मिनट लिखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_HI_DURATION = PLAN.total;

export const QrqcHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
