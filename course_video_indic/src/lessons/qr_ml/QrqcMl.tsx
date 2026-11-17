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
import words from "../../captions/qr_ml/words.json";

// Malayalam version of QrqcMl (same design and polish as the English lesson).
// All data comes from narration/qrqc_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "മിനിറ്റുകളിൽ നടപടി — തെളിവോടെ അടയ്ക്കൽ",
  outroLine: "കണ്ടെത്തുക. തടയുക. തെളിയിക്കുക.",
  outroSub: "QRQC — വേഗമുള്ള പ്രതികരണം, യഥാർത്ഥ തെളിവ്",
};

// Same polish as English QRQC; cues are phrases from the Malayalam intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "ക്യാമറകൾ ഉച്ചയോടെ ഫോക്കസ് ടെസ്റ്റിൽ ഫെയിൽ",
    sub: "ആരോ ടെസ്റ്റർ റീസെറ്റ് ചെയ്തു, ലൈൻ ഓടിക്കൊണ്ടിരുന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "വെയർഹൗസിലേക്ക് പോകുന്ന സംശയമുള്ള ക്യാമറകൾ", before: 2000, after: 0, unit: "കണക്കില്ലാത്ത സംശയമുള്ള ക്യാമറകൾ",
    takeaways: [
      { text: "വേഗം നടപടി, പക്ഷേ തെളിവോടെ", cue: "വേഗം നടപടി" },
      { text: "ആദ്യം കണ്ടെയ്ൻമെന്റ്, ഓരോ യൂണിറ്റിന്റെയും കണക്ക്", cue: "ആദ്യം കണ്ടെയ്ൻമെന്റ്" },
      { text: "പരിഹാരം തെളിഞ്ഞാൽ മാത്രം അടയ്ക്കുക", cue: "പരിഹാരം യഥാർത്ഥ" },
    ],
    action: { text: "ഒരു ഗുരുതര ഡിഫെക്റ്റിനുള്ള നിങ്ങളുടെ പ്രതികരണ പ്ലാനിന്റെ ആദ്യ 30 മിനിറ്റ് എഴുതുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_ML_DURATION = PLAN.total;

export const QrqcMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
