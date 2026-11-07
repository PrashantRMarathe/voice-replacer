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
import words from "../../captions/ik_mr/words.json";

// Marathi version of IshikawaMr (same design and polish as the English lesson).
// All data comes from narration/ishikawa_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "फिशबोनने मोकळेपणाने शोधा, मग कारण सिद्ध करा",
  outroLine: "मोकळेपणाने शोधा. नेमकं सिद्ध करा.",
  outroSub: "Ishikawa — तपासेपर्यंत प्रत्येक हाड एक अंदाज",
};

// Same polish as English Ishikawa; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "स्विच प्रति 1,000 पोर्ट टेस्टमध्ये फेल",
    sub: "5 वरून वाढून. मीटिंगचं उत्तर: नवा टेस्टर घ्या.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "स्विच लाइनवर पोर्ट-लिंक फेल्युअर", before: 32, after: 4, unit: "प्रति 1,000 स्विच",
    fixedLabel: "दोन्ही कारणं दुरुस्त",
    takeaways: [
      { text: "डोक्यावर धारदार, मोजता येणारा परिणाम", cue: "डोक्यावर एका" },
      { text: "6M मध्ये मोकळेपणाने शोधा, दोषाशिवाय", cue: "सहा एममध्ये" },
      { text: "सिद्ध होईपर्यंत प्रत्येक हाड अंदाज", cue: "आणि प्रत्येक हाड" },
    ],
    action: { text: "वारंवार येणाऱ्या एका समस्येचा फिशबोन बनवा, आणि तपासायला तीन कारणं निवडा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "J", title: "Jidoka", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_MR_DURATION = PLAN.total;

export const IshikawaMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
