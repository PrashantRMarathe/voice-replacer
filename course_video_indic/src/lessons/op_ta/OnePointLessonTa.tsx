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
import words from "../../captions/op_ta/words.json";

// Tamil version of OnePointLessonTa (same design and polish as the English lesson).
// All data comes from narration/one_point_lesson_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "op_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ONE POINT LESSON",
  title: "One Point Lesson",
  subtitle: "ஒரு தலைப்பு. ஒரு தெளிவான பாயிண்ட். ஒரு சிறந்த வேலை.",
  outroLine: "எளிமை. விஷுவல். சரி.",
  outroSub: "One Point Lesson — ஒரு பாயிண்ட்டை நன்றாகக் கற்றுக்கொடுங்கள்",
};

// Same polish as English OnePointLesson; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "கனெக்டர் தலைகீழாகப் பொருந்தி உடைந்தது",
    sub: "டே ஷிஃப்ட்டுக்கு முறை தெரியும். யாரும் சொல்லவில்லை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "நைட் ஷிஃப்ட்டில் உடையும் கனெக்டர்கள்", before: 14, after: 1, unit: "வாரத்துக்கு உடைந்த கனெக்டர்கள்",
    takeaways: [
      { text: "ஒரு தலைப்பு, ஒரு பாயிண்ட், ஒரு வலுவான விஷுவல்", cue: "ஒரு தலைப்பு" },
      { text: "Gemba-வில் கற்றுக்கொடுங்கள், பிறகு வேலையைப் பாருங்கள்", cue: "இதை Gemba-வில்" },
      { text: "இதை இப்போதைய ஸ்டாண்டர்டுடன் பொருத்தி வையுங்கள்", cue: "இதைக் கண்ட்ரோலில்" },
    ],
    action: { text: "திரும்பத் திரும்ப நடக்கும் ஒரு தவறைத் தேர்ந்தெடுத்து, அதற்கு One Point Lesson டிராஃப்ட் எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "P", title: "Poka Yoke", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ONE_POINT_LESSON_TA_DURATION = PLAN.total;

export const OnePointLessonTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
