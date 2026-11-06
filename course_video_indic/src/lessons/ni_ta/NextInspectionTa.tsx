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
import words from "../../captions/ni_ta/words.json";

// Tamil version of NextInspectionTa (same design and polish as the English lesson).
// All data comes from narration/next_inspection_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ni_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "NEXT INSPECTION",
  title: "Next Inspection",
  subtitle: "அடுத்த ப்ராசஸ் என் கஸ்டமர்",
  outroLine: "உருவாக்காதீர்கள். அனுப்பாதீர்கள். ஏற்காதீர்கள்.",
  outroSub: "Next Inspection — அடுத்த ப்ராசஸைக் காப்பாற்றுங்கள்",
};

// Same polish as English NextInspection; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "warning", label: "தளர்ந்த கனெக்டர், ஸ்டேஷன் மூன்றில்",
    sub: "யாரும் கவனிக்கவில்லை. பிறகு ஒரு கஸ்டமர் பெட்டியைத் திறந்தார்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "அடுத்த ஸ்டேஷன்களுக்கு வெளியேறும் டிஃபெக்ட்கள்", before: 18, after: 3, unit: "வாரத்துக்கு எஸ்கேப்",
    takeaways: [
      { text: "உருவாக்காதீர்கள், அனுப்பாதீர்கள், ஏற்காதீர்கள்", cue: "டிஃபெக்ட்டை உருவாக்காதீர்கள்" },
      { text: "விரைவாகச் சரிபாருங்கள், வேகமாக நடவடிக்கை", cue: "முக்கியமான பாயிண்ட்களை" },
      { text: "கண்ட்ரோல்களை மேல்நோக்கி நகர்த்திக்கொண்டே இருங்கள்", cue: "உங்கள் கண்ட்ரோல்களை" },
    ],
    action: { text: "ஒரு ஹேண்ட்ஆஃபைத் தேர்ந்தெடுத்து, அடுத்த ப்ராசஸுக்கு அதிலிருந்து என்ன தேவை என்று எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "O", title: "One Point Lesson", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const NEXT_INSPECTION_TA_DURATION = PLAN.total;

export const NextInspectionTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
