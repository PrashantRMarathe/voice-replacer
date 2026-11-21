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
import words from "../../captions/a3_ta/words.json";

// Tamil version of A3ProblemSolvingTa (same design and polish as the English lesson).
// All data comes from narration/a3_problem_solving_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "a3_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "A3 PROBLEM SOLVING",
  title: "A3 Problem Solving",
  subtitle: "முழுப் பிரச்சனைக் கதை, ஒரே பக்கத்தில்",
  outroLine: "இடைவெளியைப் பாருங்கள். காரணத்தை நிரூபியுங்கள். நிலைநிறுத்துங்கள்.",
  outroSub: "A3 — சிறந்த சிந்தனை, ஒரே ஷீட்டில்",
};

// Same polish as English A3ProblemSolving; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 576, icon: "chip", label: "சர்வர்கள் முதல் பூட் டெஸ்டில் ஃபெயில்",
    sub: "நான்கு வாரங்களில். முதல் யோசனை: இன்னும் இரண்டு இன்ஸ்பெக்டர்கள்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "முதல் பூட் டெஸ்டில் ஃபெயில் ஆகும் சர்வர்கள்", before: 48, after: 16, unit: "1,000 சர்வர்களுக்கு", fixedLabel: "டார்கெட் அடைந்தது: 48-க்குக் கீழே",
    takeaways: [
      { text: "அளக்கக்கூடிய இடைவெளியுடன் தொடங்குங்கள்", cue: "முதலில் அளக்கக்கூடிய" },
      { text: "நேரில் பாருங்கள்; ஒவ்வொரு காரணத்தையும் நிரூபியுங்கள்", cue: "நேரில் போய்ப்" },
      { text: "பைலட் நிரூபித்ததை மட்டும் ஸ்டாண்டர்டாக்குங்கள்", cue: "உங்கள் பைலட் உண்மையில்" },
    ],
    action: { text: "திரும்பத் திரும்ப வரும் ஒரு பிரச்சனையைத் தேர்ந்தெடுத்து, அதன் பிராப்ளம் ஸ்டேட்மென்டை A3-இல் எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "B", title: "Burn Down Chart", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const A3_PROBLEM_SOLVING_TA_DURATION = PLAN.total;

export const A3ProblemSolvingTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
