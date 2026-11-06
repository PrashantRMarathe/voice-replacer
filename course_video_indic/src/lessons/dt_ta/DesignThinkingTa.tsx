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
import words from "../../captions/dt_ta/words.json";

// Tamil version of DesignThinkingTa (same design and polish as the English lesson).
// All data comes from narration/design_thinking_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "dt_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "DESIGN THINKING",
  title: "Design Thinking",
  subtitle: "சரியான பிரச்சனையைத் தீர்க்கவும், வேலை செய்பவர்களுடன்",
  outroLine: "பாருங்கள். வரையறுங்கள். சிறியதாகச் சோதியுங்கள்.",
  outroSub: "Design Thinking — முதலில் மக்கள், எப்போதும் ஆதாரம்",
};

// Same polish as English DesignThinking; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 12, icon: "label", label: "1,000 பம்ப்களுக்கு லேபிள் தவறுகள்",
    sub: "முதல் யோசனை: விலையுயர்ந்த வேகமான பிரிண்டர். பேக்கர்களிடம் யாரும் கேட்கவே இல்லை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "இன்ஃப்யூஷன் பம்ப் பேக்கிங்கில் லேபிள் தவறுகள்", before: 12, after: 2, unit: "1,000 பம்ப்களுக்கு",
    takeaways: [
      { text: "மக்களிடமிருந்து தொடங்குங்கள்; முடிவெடுக்கும் முன் பாருங்கள்", cue: "வேலை செய்பவர்களிடமிருந்து" },
      { text: "தேவையை வரையறுங்கள், அதில் தீர்வு இல்லாமல்", cue: "தேவையை அதில்" },
      { text: "சிறியதாகச் சோதியுங்கள்: முடிவுகளும் உண்மையான பயன்பாடும்", cue: "சிறிய அளவில்" },
    ],
    action: { text: "சிரமமான ஒரு வேலையின் பத்து சைக்கிள்களைப் பாருங்கள், அதைச் செய்யும் மூன்று பேரிடம் பேசுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "E", title: "Elimination of Waste", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const DESIGN_THINKING_TA_DURATION = PLAN.total;

export const DesignThinkingTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
