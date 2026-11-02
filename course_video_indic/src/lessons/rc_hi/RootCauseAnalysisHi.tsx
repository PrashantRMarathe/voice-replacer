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
import words from "../../captions/rc_hi/words.json";

// hi version of RootCauseAnalysisHi (same design and polish as the English lesson).
// All data comes from narration/root_cause_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "लक्षण से ऐसी वजह तक जिसे साबित कर सकें",
  outroLine: "परिभाषित करें। परखें। रोकें।",
  outroSub: "Root Cause Analysis — साबित करें, फिर ठीक करें",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "कैमरे एक सुबह में फ़ोकस टेस्ट में फ़ेल",
    sub: "तीन लोग, तीन अलग जवाब।", until: "इस लेसन में",
  },
  recap: {
    problem: "चेंजओवर के बाद फ़ोकस में फ़ेल कैमरे", before: 60, after: 12, unit: "डिफ़ेक्ट प्रति 20,000 कैमरे",
    takeaways: [
      { text: "धारदार परिभाषा, ग्राहक को बचाएँ", cue: "समस्या को धारदार" },
      { text: "परखने तक हर वजह हाइपोथीसिस", cue: "हर वजह को" },
      { text: "क्यों हुआ और क्यों निकला, दोनों ठीक करें", cue: "और दोनों ठीक" },
    ],
    action: { text: "एक बंद हुई समस्या लें, और जाँचें कि क्या उसका रूट कॉज़ कभी परखा गया था।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_HI_DURATION = PLAN.total;

export const RootCauseAnalysisHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
