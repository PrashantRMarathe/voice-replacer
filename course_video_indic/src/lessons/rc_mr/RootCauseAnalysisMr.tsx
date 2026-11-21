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
import words from "../../captions/rc_mr/words.json";

// Marathi version of RootCauseAnalysisMr (same design and polish as the English lesson).
// All data comes from narration/root_cause_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "लक्षणापासून सिद्ध करता येईल अशा कारणापर्यंत",
  outroLine: "व्याख्या करा. तपासा. रोखा.",
  outroSub: "Root Cause Analysis — सिद्ध करा, मग दुरुस्त करा",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "कॅमेरे एका सकाळी फोकस टेस्टमध्ये फेल",
    sub: "तीन लोक, तीन वेगळी उत्तरं.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "चेंजओव्हरनंतर फोकसमध्ये फेल कॅमेरे", before: 60, after: 12, unit: "डिफेक्ट प्रति 20,000 कॅमेरे",
    takeaways: [
      { text: "धारदार व्याख्या, ग्राहकाला वाचवा", cue: "समस्येची धारदार" },
      { text: "तपासेपर्यंत प्रत्येक कारण हायपोथिसिस", cue: "प्रत्येक कारण" },
      { text: "का घडलं आणि का निसटलं, दोन्ही दुरुस्त करा", cue: "आणि दोन्ही दुरुस्त" },
    ],
    action: { text: "एक बंद झालेली समस्या घ्या, आणि तिचं रूट कॉज कधी तपासलं गेलं होतं का ते पाहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_MR_DURATION = PLAN.total;

export const RootCauseAnalysisMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
