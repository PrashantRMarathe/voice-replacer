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
import words from "../../captions/kz_ta/words.json";

// Tamil version of KaizenTa (same design and polish as the English lesson).
// All data comes from narration/kaizen_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "சிறிய மாற்றங்கள், ஒவ்வொரு நாளும், வேலை செய்பவர்களிடமிருந்து",
  outroLine: "பாருங்கள். சிறியதாக முயற்சியுங்கள். ஸ்டாண்டர்டாக்குங்கள். மீண்டும் செய்யுங்கள்.",
  outroSub: "Kaizen — இன்றைய சிறந்த முறை, நாளைய பேஸ்லைன்",
};

// Same polish as English Kaizen; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "முறை ஒவ்வொரு மானிட்டரும் புரட்டல்",
    sub: "முகம் கீழே, பிறகு முகம் மேலே. எப்போதும் அப்படித்தான் நடந்து வந்தது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "மானிட்டர் புரட்டலால் பேனல் கீறல்கள்", before: 15, after: 3, unit: "1,000 மானிட்டர்களுக்கு கீறல்கள்",
    fixedLabel: "90 நாட்களிலும் நிலைத்தது",
    takeaways: [
      { text: "Kaizen தினசரிப் பழக்கம்", cue: "Kaizen தினசரிப் பழக்கம்" },
      { text: "சிறியதாகச் சோதியுங்கள்; வேறு எதுவும் கெடவில்லை என்று பாருங்கள்", cue: "சிறிய அளவில்" },
      { text: "ஒவ்வொரு லாபத்தையும் ஸ்டாண்டர்டாக்குங்கள்", cue: "ஒவ்வொரு லாபத்தையும்" },
    ],
    action: { text: "ஒரு ஆபரேட்டரிடம் அவருடைய வேலையில் எது கடினம் என்று கேட்டு, ஒரு சிறிய தீர்வைச் சோதியுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "L", title: "Low Cost Automation", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_TA_DURATION = PLAN.total;

export const KaizenTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
