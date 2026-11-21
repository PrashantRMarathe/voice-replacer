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
import words from "../../captions/zd_ta/words.json";

// Tamil version of ZeroDefectsTa (same design and polish as the English lesson).
// All data comes from narration/zero_defects_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "டிஃபெக்ட்களைத் தடுங்கள் — சோதிப்பதோடு நிறுத்தாதீர்கள்",
  outroLine: "தடுங்கள். அளவிடுங்கள். மேம்படுத்துங்கள்.",
  outroSub: "Zero Defects — தினசரி மேனேஜ்மென்ட்டில் இணைந்தது",
};

// Same polish as English ZeroDefects; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "போன்கள் ரீவொர்க்குக்குத் திரும்பின",
    sub: "ஒரு கனெக்டர், தவறாக அமர்ந்தது. அது ஒவ்வொரு விஷுவல் செக்கிலும் தேறியது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "தவறாக அமர்ந்த கனெக்டரால் சார்ஜிங் ஃபெயிலியர்", before: 1200, after: 200,
    unit: "ஃபெயில் ஆன போன்கள், 40,000-இல்", fixedLabel: "மீண்டும் வருவது கடினம்: 83% குறைவு",
    takeaways: [
      { text: "டிஃபெக்ட்களைத் தடுங்கள், சோதிப்பது மட்டுமல்ல", cue: "டிஃபெக்ட்களைத் தடுங்கள்" },
      { text: "தெளிவான வரையறைகளுடன் நேர்மையாக அளவிடுங்கள்", cue: "தெளிவான வரையறைகளுடன்" },
      { text: "சிஸ்டத்தைச் சரிசெய்யுங்கள், நபரை அல்ல", cue: "ஏதாவது ஃபெயில்" },
    ],
    action: { text: "திரும்பத் திரும்ப வரும் ஒரு டிஃபெக்ட்டைத் தேர்ந்தெடுத்து, அதை நடக்கவே முடியாததாக எப்படி ஆக்குவது என்று கேளுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "Z", title: "Zero Defects", kicker: "இந்தப் பாடத்தை முடித்ததற்கு", cue: "இப்போது செல்லுங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_TA_DURATION = PLAN.total;

export const ZeroDefectsTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
