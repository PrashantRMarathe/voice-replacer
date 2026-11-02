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
import words from "../../captions/rc_ta/words.json";

// Tamil version of RootCauseAnalysisTa (same design and polish as the English lesson).
// All data comes from narration/root_cause_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "rc_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ROOT CAUSE ANALYSIS",
  title: "Root Cause Analysis",
  subtitle: "அறிகுறியிலிருந்து நிரூபிக்கக்கூடிய காரணம் வரை",
  outroLine: "வரையறுங்கள். சோதியுங்கள். தடுங்கள்.",
  outroSub: "Root Cause Analysis — நிரூபியுங்கள், பிறகு சரிசெய்யுங்கள்",
};

// Same polish as English RootCauseAnalysis; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 36, icon: "camera", label: "கேமராக்கள் ஒரே காலையில் ஃபோகஸ் டெஸ்ட்டில் ஃபெயில்",
    sub: "மூன்று பேர், மூன்று வெவ்வேறு பதில்கள்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "சேஞ்ச்ஓவருக்குப் பிறகு ஃபோகஸில் ஃபெயில் ஆகும் கேமராக்கள்", before: 60, after: 12, unit: "20,000 கேமராக்களுக்கு டிஃபெக்ட்கள்",
    takeaways: [
      { text: "கூர்மையான வரையறை, கஸ்டமரைக் காத்திடுங்கள்", cue: "பிரச்சனையைக் கூர்மையாக" },
      { text: "சோதிக்கும் வரை ஒவ்வொரு காரணமும் ஹைப்பாதிசிஸ்", cue: "டெஸ்ட் நிரூபிக்கும்" },
      { text: "ஏன் நடந்தது, ஏன் வெளியேறியது, இரண்டையும் சரிசெய்யுங்கள்", cue: "இரண்டையும் சரிசெய்யுங்கள்" },
    ],
    action: { text: "மூடிய ஒரு பிரச்சனையை எடுத்து, அதன் ரூட் காஸ் எப்போதாவது சோதிக்கப்பட்டதா என்று பாருங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "S", title: "Skill Training Matrix", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ROOT_CAUSE_ANALYSIS_TA_DURATION = PLAN.total;

export const RootCauseAnalysisTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
