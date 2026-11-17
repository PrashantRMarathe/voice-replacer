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
import words from "../../captions/ik_ml/words.json";

// Malayalam version of IshikawaMl (same design and polish as the English lesson).
// All data comes from narration/ishikawa_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "ഫിഷ്ബോൺ കൊണ്ട് തുറന്ന് തിരയുക, പിന്നെ കാരണം തെളിയിക്കുക",
  outroLine: "തുറന്ന് തിരയുക. കൃത്യമായി തെളിയിക്കുക.",
  outroSub: "Ishikawa — പരീക്ഷിക്കും വരെ ഓരോ എല്ലും ഒരു ഊഹം",
};

// Same polish as English Ishikawa; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "1,000 സ്വിച്ചിൽ പോർട്ട് ടെസ്റ്റിൽ ഫെയിൽ",
    sub: "5-ൽ നിന്ന് ഉയർന്നു. മീറ്റിങ്ങിന്റെ മറുപടി: പുതിയ ടെസ്റ്റർ വാങ്ങുക.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "സ്വിച്ച് ലൈനിൽ പോർട്ട് ലിങ്ക് ഫെയിലിയർ", before: 32, after: 4, unit: "1,000 സ്വിച്ചിന്",
    fixedLabel: "രണ്ട് കാരണങ്ങളും ശരിയാക്കി",
    takeaways: [
      { text: "തലയിൽ മൂർച്ചയുള്ള, അളക്കാവുന്ന ഇഫക്റ്റ്", cue: "തലയിൽ മൂർച്ചയുള്ള" },
      { text: "6M-ൽ തുറന്ന് തിരയുക, കുറ്റപ്പെടുത്തലില്ലാതെ", cue: "ആറ് എമ്മിൽ" },
      { text: "തെളിയും വരെ ഓരോ എല്ലും ഊഹം", cue: "തെളിവ് ഉറപ്പിക്കും വരെ" },
    ],
    action: { text: "ആവർത്തിക്കുന്ന ഒരു പ്രശ്നത്തിന്റെ ഫിഷ്ബോൺ ഉണ്ടാക്കി, പരീക്ഷിക്കാൻ മൂന്ന് കാരണങ്ങൾ തിരഞ്ഞെടുക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "J", title: "Jidoka", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_ML_DURATION = PLAN.total;

export const IshikawaMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
