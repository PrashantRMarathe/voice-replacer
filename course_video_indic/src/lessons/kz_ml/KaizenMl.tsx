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
import words from "../../captions/kz_ml/words.json";

// Malayalam version of KaizenMl (same design and polish as the English lesson).
// All data comes from narration/kaizen_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "ചെറിയ മാറ്റങ്ങൾ, ഓരോ ദിവസവും, ജോലി ചെയ്യുന്നവരിൽ നിന്ന്",
  outroLine: "കാണുക. ചെറുതായി പരീക്ഷിക്കുക. സ്റ്റാൻഡേർഡ് ആക്കുക. ആവർത്തിക്കുക.",
  outroSub: "Kaizen — ഇന്നത്തെ ഏറ്റവും നല്ല രീതി, നാളത്തെ ബേസ്ലൈൻ",
};

// Same polish as English Kaizen; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "തവണ ഓരോ മോണിറ്ററും മറിച്ചു",
    sub: "മുഖം താഴേക്ക്, പിന്നെ മുകളിലേക്ക്. എപ്പോഴും ഇങ്ങനെയായിരുന്നു.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "മോണിറ്റർ മറിക്കലിൽ നിന്ന് പാനൽ പോറൽ", before: 15, after: 3, unit: "1,000 മോണിറ്ററിന് പോറൽ",
    fixedLabel: "90 ദിവസത്തിലും നിലനിന്നു",
    takeaways: [
      { text: "Kaizen ദിവസേനയുള്ള ശീലമാണ്", cue: "Kaizen ദിവസേനയുള്ള" },
      { text: "ചെറുതായി പരീക്ഷിക്കുക; മറ്റൊന്നും മോശമായില്ലെന്ന് പരിശോധിക്കുക", cue: "ചെറിയ തോതിൽ" },
      { text: "ഓരോ നേട്ടവും സ്റ്റാൻഡേർഡ് ആക്കുക", cue: "ഓരോ നേട്ടവും" },
    ],
    action: { text: "ഒരു ഓപ്പറേറ്ററോട് അവരുടെ ജോലിയിൽ എന്താണ് പ്രയാസമെന്ന് ചോദിച്ച്, ഒരു ചെറിയ പരിഹാരം പരീക്ഷിക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "L", title: "Low Cost Automation", cue: "അടുത്തതായി, നിങ്ങൾ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_ML_DURATION = PLAN.total;

export const KaizenMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
