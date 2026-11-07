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
import words from "../../captions/a3_mr/words.json";

// Marathi version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "समस्येची पूर्ण कहाणी, एका पानावर",
  outroLine: "गॅप पाहा. कारण सिद्ध करा. टिकवा.",
  outroSub: "A3 — चांगला विचार, एका शीटवर",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_MR_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "सर्व्हर पहिल्या बूट टेस्टमध्ये फेल",
    sub: "चार आठवड्यांत. पहिला सुचवलेला उपाय: आणखी दोन इन्स्पेक्टर.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "पहिल्या बूट टेस्टमध्ये फेल होणारे सर्व्हर", before: 48, after: 16, unit: "प्रति 1,000 सर्व्हर", fixedLabel: "टार्गेट पूर्ण: 48 च्या खाली",
    takeaways: [
      { text: "एका मोजता येणाऱ्या गॅपने सुरू करा", cue: "सुरुवात एका मोजता" },
      { text: "जाऊन पाहा; प्रत्येक कारण सिद्ध करा", cue: "जाऊन पाहा" },
      { text: "फक्त पायलटमध्ये सिद्ध झालेल्याचं स्टँडर्ड", cue: "आणि फक्त तेच" },
    ],
    action: { text: "वारंवार येणारी एक समस्या निवडा, आणि तिचं प्रॉब्लेम स्टेटमेंट A3 वर लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "B", title: "Burn Down Chart", cue: "पुढे, तुम्ही" },
  },
};

export const A3ProblemSolvingMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
