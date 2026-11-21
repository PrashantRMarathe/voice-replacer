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
import words from "../../captions/xm_ta/words.json";

// Tamil version of XMatrixTa (same design and polish as the English lesson).
// All data comes from narration/x_matrix_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "xm_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "X-MATRIX",
  title: "The X-Matrix",
  subtitle: "Hoshin Kanri மூலம் உத்தியை ஆக்ஷனாக மாற்றுங்கள்",
  outroLine: "இணையுங்கள். செயல்படுத்துங்கள். ரிவ்யூ செய்யுங்கள்.",
  outroSub: "X-Matrix — நீங்கள் உண்மையில் செயல்படுத்தக்கூடிய உத்தி",
};

// Same polish as English XMatrix; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "stack", label: "இம்ப்ரூவ்மென்ட் புராஜெக்ட்கள், ஒவ்வொரு டீமும் பிஸி",
    sub: "ஆனாலும் டெலிவரி ஒவ்வொரு காலாண்டும் நழுவிக்கொண்டே இருந்தது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "பிஸியான போர்ட்ஃபோலியோ, நழுவும் டெலிவரி", before: 40, after: 3, unit: "புராஜெக்ட்கள், ஒவ்வொன்றும் ஒரு இலக்கு, KPI-யுடன் இணைந்தது",
    fixedLabel: "ஃபோகஸ்டு போர்ட்ஃபோலியோ",
    takeaways: [
      { text: "சில உண்மையான முன்னுரிமைகள், விருப்பப் பட்டியல் அல்ல", cue: "சில உண்மையான" },
      { text: "இலக்கு → புராஜெக்ட் → KPI → ஒரு ஓனர்", cue: "ஒவ்வொரு இலக்கையும்" },
      { text: "நேர்மையான ரிவ்யூ: எண்கள் நகர வேண்டும்", cue: "நேர்மையாக ரிவ்யூ" },
    ],
    action: { text: "உங்கள் பகுதிக்கு ஒரு நோக்கத்தை எழுதுங்கள், முடிவாக, வேலையாக அல்ல.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "Y", title: "Yamazumi", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const X_MATRIX_TA_DURATION = PLAN.total;

export const XMatrixTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
