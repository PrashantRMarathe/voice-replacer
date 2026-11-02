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
import words from "../../captions/hc_ta/words.json";

// Tamil version of HanchoTa (same design and polish as the English lesson).
// All data comes from narration/hancho_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "ஷாப்-ஃப்ளோர் தலைமை, ஒவ்வொரு ஷிஃப்ட்டின் ஒவ்வொரு மணி நேரமும்",
  outroLine: "Gemba-வில் வழிநடத்துங்கள். மக்களைத் தயார் செய்யுங்கள்.",
  outroSub: "Hancho — ஸ்டாண்டர்டை மீட்டெடுங்கள், ஒவ்வொரு நாளும் மேம்படுத்துங்கள்",
};

// Same polish as English Hancho; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV மணி நேரத்துக்குக் குறைவு, ஒரு முழு ஷிஃப்ட்",
    sub: "அடுத்த நாள் காலை ரிப்போர்ட் வரை யாருக்கும் தெரியவில்லை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "மாடல் சேஞ்சுக்குப் பிறகு அவுட்புட் இடைவெளி", before: 98, after: 120, unit: "மணி நேரத்துக்கு TV",
    fixedLabel: "அதே ஷிஃப்ட்டில் மீட்பு",
    takeaways: [
      { text: "Gemba-விலிருந்து வழிநடத்துங்கள்: ஸ்டாண்டர்ட், உண்மை", cue: "Gemba-விலிருந்து வழிநடத்துங்கள்" },
      { text: "இடைவெளியை மணி நேரத்துக்குக் காட்டுங்கள்; அதே ஷிஃப்ட்டில் நடவடிக்கை", cue: "ஒவ்வொரு இடைவெளியையும்" },
      { text: "மக்களைத் தயார் செய்யுங்கள், லைன் உங்களை நம்பி இருக்காமல்", cue: "உங்கள் மக்களைத்" },
    ],
    action: { text: "ஒரு ஷிஃப்ட்டுக்கு உங்கள் லீடர் ஸ்டாண்டர்ட் வொர்க்கை எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_TA_DURATION = PLAN.total;

export const HanchoTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
