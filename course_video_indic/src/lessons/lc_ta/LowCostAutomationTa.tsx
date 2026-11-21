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
import words from "../../captions/lc_ta/words.json";

// Tamil version of LowCostAutomationTa (same design and polish as the English lesson).
// All data comes from narration/low_cost_automation_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "lc_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "LOW COST AUTOMATION",
  title: "Low Cost Automation",
  subtitle: "வேலையை முடிக்கும் மிக எளிய பாதுகாப்பான சாதனம்",
  outroLine: "எளிதாக்குங்கள். தேவையை ஆட்டோமேட் செய்யுங்கள். நிரூபியுங்கள்.",
  outroSub: "Low Cost Automation — ஒருபோதும் குறைந்த சேஃப்டி அல்ல",
};

// Same polish as English LowCostAutomation; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "hand", label: "மேலட் அடிகள் மணி நேரத்துக்கு, ஒவ்வொரு ஆபரேட்டரும்",
    sub: "வலிக்கும் மணிக்கட்டுகள், டெஸ்ட்டில் கடகடக்கும் தளர்ந்த கிரில்கள்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "மேலட்டால் அமர்த்தியதால் தளர்ந்த ஸ்பீக்கர் கிரில்கள்", before: 18, after: 2, unit: "1,000 ஸ்பீக்கர்களுக்கு",
    fixedLabel: "4 மாதங்களில் மீட்பு",
    takeaways: [
      { text: "முதலில் எளிதாக்குங்கள்; வேஸ்ட்டை ஒருபோதும் ஆட்டோமேட் செய்யாதீர்கள்", cue: "முதலில் எளிதாக்குங்கள்" },
      { text: "மிக எளிய பாதுகாப்பான தீர்வு; சேஃப்டி முதல் கேட்", cue: "வேலையை முடிக்கும்" },
      { text: "உண்மையான லாபத்தை நிரூபியுங்கள், பிறகு பராமரியுங்கள்", cue: "உண்மையான லாபத்தை" },
    ],
    action: { text: "திரும்பத் திரும்ப வரும் ஒரு அசைவைக் கண்டுபிடித்து, ஆட்டோமேட் செய்யும் முன் அதை நீக்க முடியுமா என்று கேளுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "M", title: "Muda, Mura, Muri", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const LOW_COST_AUTOMATION_TA_DURATION = PLAN.total;

export const LowCostAutomationTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
