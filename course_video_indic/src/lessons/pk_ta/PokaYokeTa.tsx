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
import words from "../../captions/pk_ta/words.json";

// Tamil version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "தவறான வேலையைச் சாத்தியமில்லாததாக்குங்கள்",
  outroLine: "நீக்குங்கள். தடுங்கள். பிடியுங்கள்.",
  outroSub: "Poka Yoke — குவாலிட்டியை நினைவாற்றலின் நம்பிக்கையிலிருந்து வெளியே கொண்டுவாருங்கள்",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_TA_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "ரெக்கார்டர்கள் ஒரு ஸ்க்ரூ இல்லாமல் அனுப்பப்பட்டன",
    sub: "ஆபரேட்டர் திறமையானவர், கவனமானவர். ஒரு மனிதர், அவ்வளவுதான்.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "காணாமல் போன ஸ்க்ரூவுடன் அனுப்பப்பட்ட ரெக்கார்டர்கள்", before: 18, after: 1, unit: "10,000 யூனிட்களுக்கு",
    takeaways: [
      { text: "தவறுகளை ஊகிக்க முடியும்: அவற்றை டிசைனால் நீக்குங்கள்", cue: "தவறுகளை ஊகிக்க" },
      { text: "முதலில் தடுங்கள், பிறகு பிடியுங்கள், பிறகு எச்சரிக்கை", cue: "எச்சரிக்கையை விடப்" },
      { text: "ஒவ்வொரு சாதனத்தையும் மோசமான சாம்பிளால் சோதியுங்கள்", cue: "ஒவ்வொரு சாதனத்தையும்" },
    ],
    action: { text: "நினைவாற்றலை நம்பி இருக்கும் ஒரு செக்கைக் கண்டுபிடித்து, அதற்கு Poka Yoke-ஐ வரையுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "Q", title: "QRQC", cue: "அடுத்து, நீங்கள் QRQC" },
  },
};

export const PokaYokeTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
