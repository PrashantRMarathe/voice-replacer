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
import words from "../../captions/ww_ta/words.json";

// Tamil version of WhyWhyTa (same design and polish as the English lesson).
// All data comes from narration/why_why_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ww_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "WHY–WHY ANALYSIS",
  title: "Why–Why Analysis",
  subtitle: "எளிய பதிலைத் தாண்டி, நிரூபிக்கக்கூடிய காரணம் வரை",
  outroLine: "வரையறுங்கள். நிரூபியுங்கள். தடுங்கள்.",
  outroSub: "Why–Why — காரணத்தைச் சரிசெய்யுங்கள், நபரை அல்ல",
};

// Same polish as English WhyWhy; cues are phrases from the Tamil intro/outro.
// recap uses the page-12 numbers (50 → 15, 70%), not the English polish's 60 → 12;
// hook.value is 21 (the intro count), not the English polish's 24.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 21, icon: "power", label: "ஃபோன்கள் ஃபைனல் டெஸ்ட்டில் சார்ஜிங்கில் ஃபெயில்",
    sub: "முதல் பதில்: ஆபரேட்டர் தவறு. இரண்டு நாட்களுக்குப் பிறகு, மீண்டும் அதே நடந்தது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "லைன் 2-இல் சார்ஜிங் ஃபெயிலியர்", before: 50, after: 15, unit: "சார்ஜிங் டிஃபெக்ட்கள், அதே வால்யூம்",
    fixedLabel: "ரூட் காஸ் சரி: 70% குறைவு",
    takeaways: [
      { text: "முதலில் கூர்மையான பிரச்சனை, பிறகு கன்டெய்ன்மென்ட்", cue: "கூர்மையான பிரச்சனையுடன்" },
      { text: "ஒவ்வொரு ஏன் பின்னாலும் ஆதாரம், பிறகு சோதியுங்கள்", cue: "ஒவ்வொரு ஏன்" },
      { text: "எப்படி நடந்தது, ஏன் வெளியேறியது, இரண்டையும் சரிசெய்யுங்கள்", cue: "இரண்டையும் சரிசெய்யுங்கள்" },
    ],
    action: { text: "திரும்பத் திரும்ப நடக்கும் ஒரு டிஃபெக்ட்டை எடுத்து, அதன் 5W2H ஸ்டேட்மென்ட்டை எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "X", title: "X-Matrix", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const WHY_WHY_TA_DURATION = PLAN.total;

export const WhyWhyTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
