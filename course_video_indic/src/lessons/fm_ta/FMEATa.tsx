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
import words from "../../captions/fm_ta/words.json";

// Tamil version of FMEATa (same design and polish as the English lesson).
// All data comes from narration/fmea_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "ஃபெயிலியர் மோட் அண்ட் எஃபெக்ட்ஸ் அனாலிசிஸ்: ஃபெயிலியருக்கு முன் யோசியுங்கள்",
  outroLine: "சங்கிலியை உருவாக்குங்கள். ஸ்கோர் கொடுங்கள். தடுங்கள்.",
  outroSub: "FMEA — ஒரு உயிருள்ள பிளான், ஃபார்ம் அல்ல",
};

// Same polish as English FMEA; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "அவுட்டோர் ரேடியோக்கள் தண்ணீர் நிறைந்து திரும்பின",
    sub: "இரண்டில் கேஸ்கெட் இல்லை, நான்கில் மடங்கியது. எல்லாம் ஃபைனல் இன்ஸ்பெக்ஷனில் தேறியவை.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "அவுட்டோர் 5G ரேடியோவில் கேஸ்கெட் ரிஸ்க்", before: 240, after: 32, unit: "ரிஸ்க் பிரையாரிட்டி நம்பர்",
    fixedLabel: "ரிஸ்க் குறைந்தது, ட்ரையலில் நிரூபணம்",
    takeaways: [
      { text: "பாதிப்பு → ஃபெயிலியர் மோட் → கட்டுப்படுத்தக்கூடிய காரணம்", cue: "ஒரு தெளிவான" },
      { text: "ஆதாரத்துடன் ஸ்கோர்; எண்ணுக்கு மேலே புரிதல்", cue: "ஆதாரத்துடன் ஸ்கோர்" },
      { text: "முதலில் தடுப்பு, நிரூபியுங்கள், பிறகு மீண்டும் ஸ்கோர்", cue: "தடுப்பைத் தேர்ந்தெடுங்கள்" },
    ],
    action: { text: "ஒரு முக்கியமான படியைத் தேர்ந்தெடுத்து, உங்கள் டீமுடன் அதன் ஃபெயிலியர் சங்கிலியை எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "G", title: "Gemba", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_TA_DURATION = PLAN.total;

export const FMEATa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
