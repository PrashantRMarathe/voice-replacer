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
import words from "../../captions/hc_ml/words.json";

// Malayalam version of HanchoMl (same design and polish as the English lesson).
// All data comes from narration/hancho_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "hc_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "HANCHO",
  title: "Hancho",
  subtitle: "ഷോപ്പ് ഫ്ലോർ നേതൃത്വം, ഓരോ ഷിഫ്റ്റിന്റെയും ഓരോ മണിക്കൂറും",
  outroLine: "Gemba-യിൽ നയിക്കുക. ആളുകളെ വളർത്തുക.",
  outroSub: "Hancho — സ്റ്റാൻഡേർഡ് തിരിച്ചെത്തിക്കുക, ദിവസവും മെച്ചപ്പെടുത്തുക",
};

// Same polish as English Hancho; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 20, icon: "clock", label: "TV ഓരോ മണിക്കൂറും കുറവ്, ഒരു ഷിഫ്റ്റ് മുഴുവൻ",
    sub: "പിറ്റേന്ന് രാവിലത്തെ റിപ്പോർട്ട് വരെ ആരും അറിഞ്ഞില്ല.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "മോഡൽ മാറ്റത്തിന് ശേഷം ഔട്ട്പുട്ട് ഗ്യാപ്", before: 98, after: 120, unit: "മണിക്കൂറിൽ TV",
    fixedLabel: "അതേ ഷിഫ്റ്റിൽ തിരിച്ചെത്തി",
    takeaways: [
      { text: "Gemba-യിൽ നിന്ന് നയിക്കുക: സ്റ്റാൻഡേർഡും യഥാർത്ഥവും", cue: "Gemba-യിൽ നിന്ന് നയിക്കുക" },
      { text: "ഗ്യാപ് ഓരോ മണിക്കൂറും കാണിക്കുക; അതേ ഷിഫ്റ്റിൽ നടപടി", cue: "ഓരോ ഗ്യാപും" },
      { text: "ലൈൻ നിങ്ങളെ ആശ്രയിക്കാതിരിക്കാൻ ആളുകളെ വളർത്തുക", cue: "ലൈൻ നിങ്ങളെ" },
    ],
    action: { text: "ഒരു ഷിഫ്റ്റിനുള്ള നിങ്ങളുടെ ലീഡർ സ്റ്റാൻഡേർഡ് വർക്ക് എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "I", title: "Ishikawa Diagram", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const HANCHO_ML_DURATION = PLAN.total;

export const HanchoMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
