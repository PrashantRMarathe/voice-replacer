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
import words from "../../captions/tt_ta/words.json";

// Tamil version of TaktTimeTa (same design and polish as the English lesson).
// All data comes from narration/takt_time_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "tt_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "TAKT TIME",
  title: "TAKT Time",
  subtitle: "உங்கள் கஸ்டமர் நிர்ணயிக்கும் இதயத் துடிப்பு",
  outroLine: "அளவிடுங்கள். பேலன்ஸ் செய்யுங்கள். ஃப்ளோவை உருவாக்குங்கள்.",
  outroSub: "TAKT Time — கஸ்டமரின் வேகம்",
};

// Same polish as English TaktTime; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1000, icon: "stack", label: "கேமராக்கள் டெஸ்ட்டுக்கு முன்னால் செய்யப்பட்டன",
    sub: "ஒவ்வொரு ஸ்டேஷனும் பிஸி. டிரக் இன்னும் தாமதமாகப் போனது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "பிஸியான லைன், ஆனாலும் டிரக்கைத் தவறவிடுகிறது", before: 0, after: 10, unit: "வினாடிகள்: தினமும் 7,200 கேமராக்களின் துடிப்பு",
    fixedLabel: "எல்லோரும் நடக்கும் வேகம்",
    takeaways: [
      { text: "TAKT = நிகர கிடைக்கும் நேரம் ÷ டிமாண்ட்", cue: "TAKT என்பது" },
      { text: "தேவையான வேகம், ஸ்டேஷனின் நேரம் அல்ல", cue: "இது உங்களுக்குத்" },
      { text: "உண்மையான இழப்பால் பிளான், கோட்பாட்டால் அல்ல", cue: "உண்மையான இழப்புகளைக்" },
    ],
    action: { text: "ஒரு லைனின் TAKT-ஐக் கணக்கிட்டு, அதை உங்கள் மிக மெதுவான ஸ்டேஷனுடன் ஒப்பிடுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "U", title: "Uniform Production", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const TAKT_TIME_TA_DURATION = PLAN.total;

export const TaktTimeTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
