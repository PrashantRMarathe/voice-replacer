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
import words from "../../captions/up_ta/words.json";

// Tamil version of UniformProductionTa (same design and polish as the English lesson).
// All data comes from narration/uniform_production_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "வால்யூம், மிக்ஸை லெவல் செய்யுங்கள், நிலையான, நம்பகமான ஃப்ளோவுக்கு",
  outroLine: "லெவல் செய்யுங்கள். வரிசைப்படுத்துங்கள். நிலைப்படுத்துங்கள்.",
  outroSub: "Uniform Production — உங்கள் லைன் தக்கவைக்கக்கூடிய வேகம்",
};

// Same polish as English UniformProduction; cues are phrases from the Tamil intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "ஃபோன்கள் திங்கட்கிழமை. செவ்வாய் ஏறக்குறைய ஒன்றுமில்லை.",
    sub: "புதனுக்குள், டெஸ்ட் பெஞ்ச் வேலையில் மூழ்கியிருக்கிறது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "மிகவும் மேடு பள்ளமான ஷெட்யூல்", before: 0, after: 6000, unit: "நல்ல யூனிட்கள் தினமும், ஒவ்வொரு நாளும்",
    fixedLabel: "ஒரு நிலையான, லெவல் வேகம்",
    takeaways: [
      { text: "வால்யூம், மிக்ஸ் இரண்டையும் லெவல் செய்யுங்கள்", cue: "வால்யூம், மிக்ஸ் இரண்டையும்" },
      { text: "முதலில் பாட்டில்நெக், சேஞ்ச்ஓவரைச் சரிபாருங்கள்", cue: "எந்த பேட்டர்னையும்" },
      { text: "கண்ணுக்குத் தெரியும் பிளான், மாற்றத்துக்கான தெளிவான விதிகள்", cue: "பிளானைக் கண்ணுக்குத்" },
    ],
    action: { text: "பெரிய பேட்ச்களில் செய்யும் ஒரு புராடக்ட்டைக் கண்டுபிடித்து, சிறிய, திரும்பும் பேட்டர்னை வரையுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "அடுத்து," },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_TA_DURATION = PLAN.total;

export const UniformProductionTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
