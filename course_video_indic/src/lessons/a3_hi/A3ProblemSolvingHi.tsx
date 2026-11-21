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
import words from "../../captions/a3_hi/words.json";

// Hindi version of A3 Problem Solving (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "समस्या की पूरी कहानी, एक पेज पर",
  outroLine: "गैप देखें। वजह साबित करें। टिकाएँ।",
  outroSub: "A3 — बेहतर सोच, एक शीट पर",
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_HI_DURATION = PLAN.total;

// Same polish as English A3ProblemSolving; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "सर्वर अपने पहले बूट टेस्ट में फ़ेल",
    sub: "चार हफ़्तों में। पहला सुझाया हल: दो और इंस्पेक्टर।", until: "इस लेसन में",
  },
  recap: {
    problem: "पहले बूट टेस्ट में फ़ेल होते सर्वर", before: 48, after: 16, unit: "प्रति 1,000 सर्वर", fixedLabel: "टारगेट पूरा: 48 से नीचे",
    takeaways: [
      { text: "एक मापने लायक गैप से शुरू करें", cue: "शुरुआत एक मापने" },
      { text: "जाकर देखें; हर वजह साबित करें", cue: "जाकर देखें" },
      { text: "सिर्फ़ पायलट में साबित चीज़ का स्टैंडर्ड", cue: "और सिर्फ़ वही" },
    ],
    action: { text: "बार-बार आने वाली एक समस्या चुनें, और उसका प्रॉब्लम स्टेटमेंट A3 पर लिखें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "B", title: "Burn Down Chart", cue: "आगे, आप" },
  },
};

export const A3ProblemSolvingHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
