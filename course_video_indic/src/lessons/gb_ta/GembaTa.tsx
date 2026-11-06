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
import words from "../../captions/gb_ta/words.json";

// Tamil version of GembaTa (same design and polish as the English lesson).
// All data comes from narration/gemba_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "gb_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "GEMBA · 3G",
  title: "Gemba",
  subtitle: "உண்மையான இடம், உண்மையான பொருள், உண்மையான தகவல்கள்",
  outroLine: "போங்கள். பாருங்கள். உறுதிசெய்யுங்கள்.",
  outroSub: "Gemba, Genbutsu, Genjitsu — முடிவுக்கு முன் உண்மைகள்",
};

// Same polish as English Gemba; cues are phrases from the Tamil intro/outro.
// recap.after is 8 (the page-13 result), not the English polish's 5.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "wave", label: "× இயர்பட் ஃபெயிலியர்கள், ஷிஃப்ட் B-யில்",
    sub: "பிளான்: ஷிஃப்ட் B-க்கு மீண்டும் பயிற்சி. யாரும் ஒரு ஃபெயில் ஆன இயர்பட்டைக் கூடப் பார்க்கவில்லை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "ஆடியோ டெஸ்ட்டில் ஃபெயில் ஆகும் இயர்பட்கள்", before: 20, after: 8, unit: "1,000 இயர்பட்களுக்கு ஃபெயிலியர்கள்",
    fixedLabel: "காரணத்தில் சரிசெய்யப்பட்டது",
    takeaways: [
      { text: "உண்மையான இடத்துக்குப் போங்கள்; உண்மையான சைக்கிள்களைப் பாருங்கள்", cue: "உண்மையான இடத்துக்குப் போங்கள்" },
      { text: "உண்மையான பொருளைக் கையில் எடுங்கள்; நல்லதுடன் ஒப்பிடுங்கள்", cue: "உண்மையான பொருளைக் கையில்" },
      { text: "உண்மையான தகவல்களைச் சோதியுங்கள், வகுத்தியுடன்", cue: "உண்மையான தகவல்களைச் சோதியுங்கள்" },
    ],
    action: { text: "திரும்பத் திரும்ப வரும் ஒரு பிரச்சனையை எடுத்து, முப்பது நிமிட 3G விசிட் செய்யுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "H", title: "Hancho", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const GEMBA_TA_DURATION = PLAN.total;

export const GembaTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
