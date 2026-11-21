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
import words from "../../captions/ik_ta/words.json";

// Tamil version of IshikawaTa (same design and polish as the English lesson).
// All data comes from narration/ishikawa_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "ஃபிஷ்போனால் பரந்த அளவில் தேடுங்கள், பிறகு காரணத்தை நிரூபியுங்கள்",
  outroLine: "பரந்த அளவில் தேடுங்கள். துல்லியமாக நிரூபியுங்கள்.",
  outroSub: "Ishikawa — சோதிக்கும் வரை ஒவ்வொரு எலும்பும் ஊகம்",
};

// Same polish as English Ishikawa; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "சுவிட்ச்கள் 1,000-க்கு போர்ட் டெஸ்ட்டில் ஃபெயில்",
    sub: "5-இலிருந்து உயர்வு. மீட்டிங்கின் பதில்: புதிய டெஸ்டர் வாங்குங்கள்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "சுவிட்ச் லைனில் போர்ட்-லிங்க் ஃபெயிலியர்கள்", before: 32, after: 4, unit: "1,000 சுவிட்ச்களுக்கு",
    fixedLabel: "இரண்டு காரணங்களும் சரியானவை",
    takeaways: [
      { text: "தலையில் கூர்மையான, அளவிடக்கூடிய பாதிப்பு", cue: "தலையில் ஒரு" },
      { text: "6M-இல் பரந்த அளவில் தேடுங்கள், குற்றச்சாட்டு இல்லாமல்", cue: "ஆறு எம்-களில்" },
      { text: "நிரூபிக்கும் வரை ஒவ்வொரு எலும்பும் ஊகம்", cue: "ஆதாரம் நிரூபிக்கும்" },
    ],
    action: { text: "திரும்ப வரும் ஒரு பிரச்சனையின் ஃபிஷ்போனை வரைந்து, சோதிக்க மூன்று காரணங்களைத் தேர்ந்தெடுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "J", title: "Jidoka", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_TA_DURATION = PLAN.total;

export const IshikawaTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
