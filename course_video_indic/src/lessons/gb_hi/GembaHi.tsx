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
import words from "../../captions/gb_hi/words.json";

// Hindi version of GembaHi (same design and polish as the English lesson).
// All data comes from narration/gemba_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "असली जगह, असली चीज़, असली तथ्य",
  outroLine: "जाएँ। देखें। पक्का करें।",
  outroSub: "Gemba, Genbutsu, Genjitsu — फ़ैसले से पहले तथ्य",
};

// Same polish as English Gemba; cues are phrases from the Hindi intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× ईयरबड फ़ेल्योर, शिफ़्ट B पर",
    sub: "प्लान: शिफ़्ट B को दोबारा ट्रेनिंग। किसी ने एक फ़ेल ईयरबड तक नहीं देखा।", until: "इस लेसन में",
  },
  recap: {
    problem: "ऑडियो टेस्ट में फ़ेल होते ईयरबड", before: 20, after: 8, unit: "प्रति 1,000 ईयरबड फ़ेल्योर",
    fixedLabel: "वजह पर ठीक किया",
    takeaways: [
      { text: "असली जगह पर जाएँ; असली साइकिल देखें", cue: "असली जगह पर जाएँ" },
      { text: "असली चीज़ हाथ में लें; अच्छी से तुलना करें", cue: "असली चीज़ हाथ" },
      { text: "असली तथ्य परखें, भाजक के साथ", cue: "और असली तथ्य" },
    ],
    action: { text: "बार-बार आने वाली एक समस्या लें, और तीस मिनट की 3G विज़िट करें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "H", title: "Hancho", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_HI_DURATION = PLAN.total;

export const GembaHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
