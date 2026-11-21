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
import words from "../../captions/bd_ta/words.json";

// Tamil version of BurnDownChartTa (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "டெட்லைனுக்கு முன் மீதி வேலையைப் பாருங்கள்",
  outroLine: "லைனை வரையுங்கள். இடைவெளியைப் பாருங்கள். இன்றே நடவடிக்கை எடுங்கள்.",
  outroSub: "Burn Down Chart — இனி வெள்ளிக்கிழமை அதிர்ச்சிகள் இல்லை",
};

// Same polish as English BurnDownChart; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "ரௌட்டர்கள் டிரக்கைத் தவறவிட்டன",
    sub: "வெள்ளிக்கிழமை மதியம் வரை யாருக்கும் தெரியவே இல்லை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "டிஸ்பாட்சில் குறைந்த ரௌட்டர்கள்", before: 80, after: 0, unit: "ரௌட்டர்கள் குறைவு",
    takeaways: [
      { text: "முதலில் ஐடியல் லைன்; அதை மீண்டும் ஒருபோதும் இல்லை", cue: "முதலில் ஐடியல் லைனை" },
      { text: "முடிந்த நல்ல வேலையை மட்டும் எண்ணுங்கள்", cue: "உண்மையில் முடிந்த" },
      { text: "ஐடியலுக்கு மேலே? அதே நாளில் நடவடிக்கை, ஓனருடன்", cue: "லைன் ஐடியலுக்கு மேலே" },
    ],
    action: { text: "டெட்லைன் உள்ள ஒரு வேலையைத் தேர்ந்தெடுத்து, நாளைய ஷிஃப்ட்டுக்கு முன் அதன் பர்ன்-டவுனை வரையுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "C", title: "Cycle Time Study", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_TA_DURATION = PLAN.total;

export const BurnDownChartTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
