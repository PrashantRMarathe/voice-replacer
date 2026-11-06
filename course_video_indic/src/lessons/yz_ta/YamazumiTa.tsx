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
import words from "../../captions/yz_ta/words.json";

// Tamil version of YamazumiTa (same design and polish as the English lesson).
// All data comes from narration/yamazumi_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "உண்மையான டேட்டாவால், TAKT-க்கு எதிராக லைனை பேலன்ஸ் செய்யுங்கள்",
  outroLine: "அளவிடுங்கள். அடுக்குங்கள். பேலன்ஸ் செய்யுங்கள்.",
  outroSub: "Yamazumi — டிசைனால் நிலைக்கும் ஃப்ளோ",
};

// Same polish as English Yamazumi; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "ஆபரேட்டர்கள் காத்திருப்பில், ஒருவர் ஸ்க்ரூக்களில் புதைந்து",
    sub: "யாரும் சோம்பேறி அல்ல. வேலை சீரற்ற முறையில் குவிந்திருக்கிறது, அவ்வளவுதான்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "ஸ்டேஷன் B, TAKT-க்கு மேலே", before: 35, after: 30, unit: "ஸ்டேஷன் B-யில் வேலை வினாடிகள்",
    fixedLabel: "மீண்டும் TAKT-இல்",
    takeaways: [
      { text: "உண்மையான வேலையை அளவிடுங்கள், சிறந்த கேஸை அல்ல", cue: "உண்மையான வேலையை" },
      { text: "TAKT-க்கு எதிராக அடுக்குங்கள், குவியலைப் பாருங்கள்", cue: "அதை TAKT-க்கு எதிராக" },
      { text: "சேஃப்டி, குவாலிட்டியைப் பணயம் வைக்காமல் பேலன்ஸ்", cue: "கவனமாக மீண்டும்" },
    ],
    action: { text: "உங்கள் லைனின் ஒரு ஸ்டேஷனின் நேரத்தை அளந்து, TAKT-க்கு எதிராக அதன் பாரை வரையுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "Z", title: "Zero Defects", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_TA_DURATION = PLAN.total;

export const YamazumiTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
