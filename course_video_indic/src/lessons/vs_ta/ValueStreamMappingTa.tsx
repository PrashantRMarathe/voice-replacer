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
import words from "../../captions/vs_ta/words.json";

// Tamil version of ValueStreamMappingTa (same design and polish as the English lesson).
// All data comes from narration/value_stream_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "ஆர்டர் முதல் டெலிவரி வரை, முழு ஃப்ளோவைப் பாருங்கள்",
  outroLine: "பாருங்கள். அளவிடுங்கள். ஃப்ளோவை உருவாக்குங்கள்.",
  outroSub: "Value Stream Mapping — காத்திருப்பைக் கண்டுபிடியுங்கள், ஃப்ளோவை டிசைன் செய்யுங்கள்",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "நிமிடங்கள், ஒரு செட்-டாப் பாக்ஸ் உருவாக்கி டெஸ்ட் செய்ய",
    sub: "ஆனாலும் கஸ்டமரை அடைய ஏறக்குறைய நான்கு நாட்கள்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "நிமிட வேலைக்கு நாட்கள் காத்திருப்பு", before: 4200, after: 2100, unit: "மூன்று பஃபர்களில் காத்திருக்கும் யூனிட்கள்",
    fixedLabel: "ஃப்யூச்சர் ஸ்டேட்: பாதிக் காத்திருப்பு",
    takeaways: [
      { text: "உண்மையான மெட்டீரியல் + தகவல் ஃப்ளோவின் மேப்", cue: "உண்மையான ஃப்ளோவின்" },
      { text: "லீட் டைம் காத்திருப்பில் மறைந்துள்ளது, வேலையில் அல்ல", cue: "உங்கள் பெரும்பாலான" },
      { text: "ஸ்டாக் குறைக்கும் முன் ஃப்யூச்சர் ஸ்டேட்டை நிரூபியுங்கள்", cue: "எந்த ஸ்டாக்கையும்" },
    ],
    action: { text: "ஒரு புராடக்ட் ஃபேமிலியுடன் டிஸ்பாட்சிலிருந்து பின்னோக்கி நடந்து, ஒவ்வொரு குவியலையும் எண்ணுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_TA_DURATION = PLAN.total;

export const ValueStreamMappingTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
