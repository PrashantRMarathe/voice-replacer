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
import words from "../../captions/ew_ta/words.json";

// Tamil version of EliminationOfWasteTa (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "கஸ்டமர் பணம் கொடுக்காததை நீக்குங்கள்",
  outroLine: "பாருங்கள். காரணத்தை நீக்குங்கள். நிரூபியுங்கள்.",
  outroSub: "Elimination of Waste — அதிக மதிப்பு, குறைந்த உழைப்பு",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "சவுண்ட்பார்கள், மாதந்தோறும் ரீவொர்க்",
    sub: "ஒவ்வொன்றையும் சரிசெய்ய ₹42. யாரும் இதைக் கூட்டிப் பார்க்கவே இல்லை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "சத்தமிடும் ஸ்பீக்கர் வயரால் ரீவொர்க் ஆகும் சவுண்ட்பார்கள்", before: 1500, after: 300, unit: "மாதம் ரீவொர்க்", fixedLabel: "ரீவொர்க் 80% குறைந்தது",
    takeaways: [
      { text: "வேஸ்ட்: கஸ்டமர் பணம் கொடுக்காதது", cue: "வேஸ்ட் என்பது கஸ்டமர்" },
      { text: "இதை Gemba-வில் உண்மைகளால் கண்டுபிடியுங்கள்", cue: "இதை Gemba-வில்" },
      { text: "காரணத்தை நீக்குங்கள், நிரூபியுங்கள், நிலைநிறுத்துங்கள்", cue: "காரணத்தை நீக்குங்கள்" },
    ],
    action: { text: "முப்பது நிமிடங்கள் உங்கள் லைனில் நடந்து, மூன்று வேஸ்ட்களை உண்மைகளாக எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "F", title: "FMEA", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_TA_DURATION = PLAN.total;

export const EliminationOfWasteTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
