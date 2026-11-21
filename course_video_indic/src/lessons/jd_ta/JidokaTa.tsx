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
import words from "../../captions/jd_ta/words.json";

// Tamil version of JidokaTa (same design and polish as the English lesson).
// All data comes from narration/jidoka_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "மனிதத் தொடுதலுடன் ஆட்டோமேஷன்",
  outroLine: "பாருங்கள். நிறுத்துங்கள். தீருங்கள்.",
  outroSub: "Jidoka — எந்த டிஃபெக்ட்டும் முன்னே இல்லை, எந்தக் கோளாறும் மறைவில் இல்லை",
};

// Same polish as English Jidoka; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "பேஷன்ட் மானிட்டர்களில் மெல்லிய சீல்",
    sub: "டிஸ்பென்சர் இரவு முழுவதும் நன்றாக ஓடியது. அதன் நாஸில் பாதி அடைபட்டிருந்தது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "அடைபட்ட அட்ஹெசிவ் நாஸிலால் மெல்லிய சீல்", before: 140, after: 1, unit: "மானிட்டர்களுக்குப் பாதிப்பு, நாஸில் பிரச்சனைக்கு",
    fixedLabel: "மூலத்தில் பிடிபட்டது",
    takeaways: [
      { text: "முதலில் இயல்பை வரையறுங்கள்", cue: "முதலில் இயல்பை" },
      { text: "கண்டறியுங்கள், நிறுத்துங்கள், கன்டெய்ன்: எந்த டிஃபெக்ட்டும் முன்னே இல்லை", cue: "மூலத்திலேயே கண்டறியுங்கள்" },
      { text: "ஒவ்வொரு நிறுத்தமும் ஒரு பாடம்: ரூட் காஸைச் சரிசெய்யுங்கள்", cue: "ஒவ்வொரு நிறுத்தத்தையும்" },
    ],
    action: { text: "ஒரு தானியங்கி ப்ராசஸைத் தேர்ந்தெடுத்து, அது எதற்கு நிற்க வேண்டும் என்று எழுதுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "K", title: "Kaizen", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_TA_DURATION = PLAN.total;

export const JidokaTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
