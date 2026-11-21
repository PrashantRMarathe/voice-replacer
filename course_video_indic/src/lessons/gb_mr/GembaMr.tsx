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
import words from "../../captions/gb_mr/words.json";

// Marathi version of GembaMr (same design and polish as the English lesson).
// All data comes from narration/gemba_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "खरी जागा, खरी वस्तू, खरी तथ्यं",
  outroLine: "जा. पाहा. पक्कं करा.",
  outroSub: "Gemba, Genbutsu, Genjitsu — निर्णयाआधी तथ्यं",
};

// Same polish as English Gemba; cues are phrases from the Marathi intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× इयरबड फेल्युअर, शिफ्ट B वर",
    sub: "प्लान: शिफ्ट B ला पुन्हा ट्रेनिंग. कोणी एक फेल इयरबडही पाहिला नाही.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "ऑडिओ टेस्टमध्ये फेल होणारे इयरबड", before: 20, after: 8, unit: "प्रति 1,000 इयरबड फेल्युअर",
    fixedLabel: "कारणावर दुरुस्त केलं",
    takeaways: [
      { text: "खऱ्या जागेवर जा; खरे सायकल पाहा", cue: "खऱ्या जागेवर जा" },
      { text: "खरी वस्तू हातात घ्या; चांगलीशी तुलना करा", cue: "खरी वस्तू हातात" },
      { text: "खरी तथ्यं पडताळा, भाजकासह", cue: "आणि खरी तथ्यं" },
    ],
    action: { text: "वारंवार येणारी एक समस्या घ्या, आणि तीस मिनिटांची 3G व्हिजिट करा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "H", title: "Hancho", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_MR_DURATION = PLAN.total;

export const GembaMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
