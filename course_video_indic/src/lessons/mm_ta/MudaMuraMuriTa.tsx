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
import words from "../../captions/mm_ta/words.json";

// Tamil version of MudaMuraMuriTa (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "வேஸ்ட், சீரின்மை, அதிகச் சுமை — மூன்றையும் மேம்படுத்துங்கள்",
  outroLine: "லெவல் செய்யுங்கள். காத்திடுங்கள். நீக்குங்கள்.",
  outroSub: "3M — நிலையான ஃப்ளோ, வேகமான மக்கள் அல்ல",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "கேமராக்கள் பின்னால், ஷிஃப்ட் முடிய ஒரு மணி நேரம் முன்",
    sub: "எல்லோரும் ஓடுகிறார்கள். டெஸ்ட்டில் தவறுகள் குவிகின்றன.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "சஞ்சயின் லைன் தினமும் தாமதமாக ஓடியது", before: 150, after: 0, unit: "தினமும் நிமிட ஓவர்டைம்",
    takeaways: [
      { text: "Muda வேஸ்ட், Mura சீரின்மை, Muri அதிகச் சுமை", cue: "Muda என்பது வேஸ்ட்" },
      { text: "இவை ஒன்றையொன்று கூட்டுகின்றன: சேர்த்து மேம்படுத்துங்கள்", cue: "இவை ஒன்றையொன்று" },
      { text: "நிலையான ஃப்ளோ, வேகமான மக்கள் அல்ல", cue: "இலக்கு நிலையான" },
    ],
    action: { text: "ஒரு புராடக்ட்டுடன் உங்கள் லைனில் நடந்து, ஒவ்வொரு M-க்கும் ஒரு உதாரணத்தை டேக் செய்யுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "N", title: "Next Inspection", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_TA_DURATION = PLAN.total;

export const MudaMuraMuriTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
