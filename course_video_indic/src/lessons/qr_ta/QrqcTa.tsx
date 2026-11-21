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
import words from "../../captions/qr_ta/words.json";

// Tamil version of QrqcTa (same design and polish as the English lesson).
// All data comes from narration/qrqc_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "நிமிடங்களில் நடவடிக்கை — ஆதாரத்துடன் மூடல்",
  outroLine: "பிடியுங்கள். நிறுத்துங்கள். நிரூபியுங்கள்.",
  outroSub: "QRQC — வேகமான பதில், உண்மையான ஆதாரம்",
};

// Same polish as English QRQC; cues are phrases from the Tamil intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "கேமராக்கள் மதியத்துக்குள் ஃபோகஸ் டெஸ்ட்டில் ஃபெயில்",
    sub: "யாரோ டெஸ்டரை ரீசெட் செய்தார்கள், லைன் ஓடிக்கொண்டே இருந்தது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "வேர்ஹவுஸை நோக்கிப் போகும் சந்தேகமான கேமராக்கள்", before: 2000, after: 0, unit: "கணக்கில் வராத சந்தேகமான கேமராக்கள்",
    takeaways: [
      { text: "வேகமாக நடவடிக்கை, ஆனால் ஆதாரத்துடன்", cue: "வேகமாக நடவடிக்கை" },
      { text: "முதலில் கன்டெய்ன்மென்ட், ஒவ்வொரு யூனிட்டின் கணக்கும்", cue: "முதலில் கன்டெய்ன்மென்ட்" },
      { text: "தீர்வு நிரூபித்த பிறகே மூடுங்கள்", cue: "தீர்வு உண்மையான" },
    ],
    action: { text: "ஒரு கடுமையான டிஃபெக்ட்டுக்கு உங்கள் ரெஸ்பான்ஸ் பிளானின் முதல் 30 நிமிடங்களை எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_TA_DURATION = PLAN.total;

export const QrqcTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
