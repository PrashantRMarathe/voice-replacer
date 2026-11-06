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
import words from "../../captions/ik_hi/words.json";

// hi version of IshikawaHi (same design and polish as the English lesson).
// All data comes from narration/ishikawa_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "फ़िशबोन से खुलकर खोजें, फिर वजह साबित करें",
  outroLine: "खुलकर खोजें। सटीक साबित करें।",
  outroSub: "Ishikawa — परखने तक हर हड्डी एक अनुमान",
};

// Same polish as English Ishikawa; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "स्विच प्रति 1,000 पोर्ट टेस्ट में फ़ेल",
    sub: "5 से बढ़कर। मीटिंग का जवाब: नया टेस्टर खरीदो।", until: "इस लेसन में",
  },
  recap: {
    problem: "स्विच लाइन पर पोर्ट-लिंक फ़ेल्योर", before: 32, after: 4, unit: "प्रति 1,000 स्विच",
    fixedLabel: "दोनों वजहें ठीक",
    takeaways: [
      { text: "सिर पर धारदार, मापने लायक असर", cue: "सिर पर एक" },
      { text: "6M में खुलकर खोजें, बिना दोष", cue: "छह एम में" },
      { text: "साबित होने तक हर हड्डी अनुमान", cue: "और हर हड्डी" },
    ],
    action: { text: "बार-बार आने वाली एक समस्या का फ़िशबोन बनाएँ, और परखने के लिए तीन वजहें चुनें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "J", title: "Jidoka", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_HI_DURATION = PLAN.total;

export const IshikawaHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
