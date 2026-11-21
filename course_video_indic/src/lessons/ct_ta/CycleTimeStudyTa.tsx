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
import words from "../../captions/ct_ta/words.json";

// Tamil version of CycleTimeStudyTa (same design and polish as the English lesson).
// All data comes from narration/cycle_time_study_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ct_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "CYCLE TIME STUDY",
  title: "Cycle Time Study",
  subtitle: "உண்மையான வேலையை அளவிடுங்கள், உண்மையான பாட்டில்நெக்கைக் கண்டுபிடியுங்கள்",
  outroLine: "வரையறை. அளவீடு. முறையில் மேம்பாடு.",
  outroSub: "Cycle Time Study — வேகத்துக்கு முன் ஆதாரம்",
};

// Same polish as English CycleTimeStudy; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "clock", label: "வினாடிகள்: ஒவ்வொரு ஸ்டேஷனும் போதுமான வேகமாகத் தெரிந்தது",
    sub: "ஆனாலும் மானிட்டர் லைன் ஷிஃப்ட்டுக்கு ஷிஃப்ட் மணி நேர டார்கெட்டைத் தவறவிட்டது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "டிஸ்பிளே-டெஸ்ட் ஸ்டேஷன் TAKT-ஐ விட மெதுவு", before: 28, after: 23, unit: "மானிட்டருக்கு வினாடிகள், ஸ்டேஷன் C-யில்", fixedLabel: "இப்போது TAKT-க்குள்",
    takeaways: [
      { text: "முதலில் எல்லையை நிர்ணயியுங்கள்", cue: "முதலில் எல்லையை" },
      { text: "சராசரி மட்டுமல்ல, பரவலையும் பாருங்கள்", cue: "சராசரி மட்டுமல்ல" },
      { text: "முறையைச் சரிசெய்யுங்கள், குவாலிட்டி செக்கை ஒருபோதும் விடாதீர்கள்", cue: "பாட்டில்நெக்கில் முறையைச்" },
    ],
    action: { text: "ஒரு ஸ்டேஷனில் பத்து சைக்கிள்களை அளந்து, மிக நீளமானதை TAKT உடன் ஒப்பிடுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "D", title: "Design Thinking", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const CYCLE_TIME_STUDY_TA_DURATION = PLAN.total;

export const CycleTimeStudyTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
