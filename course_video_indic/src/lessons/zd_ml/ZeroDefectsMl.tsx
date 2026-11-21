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
import words from "../../captions/zd_ml/words.json";

// Malayalam version of ZeroDefectsMl (same design and polish as the English lesson).
// All data comes from narration/zero_defects_ml.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_ml",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "ഡിഫെക്റ്റ് തടയുക — അവയെ പരിശോധിക്കുക മാത്രമല്ല",
  outroLine: "തടയുക. അളക്കുക. മെച്ചപ്പെടുത്തുക.",
  outroSub: "Zero Defects — ദിവസേനയുള്ള മാനേജ്മെന്റിൽ ഉൾച്ചേർത്തത്",
};

// Same polish as English ZeroDefects; cues are phrases from the Malayalam intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "ഫോണുകൾ റീവർക്കിനായി തിരിച്ചുവന്നു",
    sub: "ഒരു കണക്റ്റർ, തെറ്റായി ഇരുന്നു. അത് ഓരോ വിഷ്വൽ ചെക്കിലും പാസായി.", until: "ഈ ലെസണിൽ",
  },
  recap: {
    problem: "തെറ്റായി ഇരുന്ന കണക്റ്ററിൽ നിന്ന് ചാർജിങ് ഫെയിലിയർ", before: 1200, after: 200,
    unit: "ഫെയിലായ ഫോൺ, 40,000-ൽ", fixedLabel: "ആവർത്തിക്കാൻ പ്രയാസം: 83% കുറവ്",
    takeaways: [
      { text: "ഡിഫെക്റ്റ് തടയുക, പരിശോധന മാത്രമല്ല", cue: "ഡിഫെക്റ്റ് തടയുക" },
      { text: "വ്യക്തമായ നിർവചനങ്ങളോടെ സത്യസന്ധമായി അളക്കുക", cue: "വ്യക്തമായ നിർവചനങ്ങളോടെ" },
      { text: "സിസ്റ്റം ശരിയാക്കുക, വ്യക്തിയെയല്ല", cue: "എന്തെങ്കിലും ഫെയിലാകുമ്പോൾ" },
    ],
    action: { text: "വീണ്ടും വീണ്ടും വരുന്ന ഒരു ഡിഫെക്റ്റ് തിരഞ്ഞെടുത്ത്, അതിനെ എങ്ങനെ അസാധ്യമാക്കാം എന്ന് ചോദിക്കുക.", cue: "ഈ ആഴ്ചത്തെ നിങ്ങളുടെ ജോലി" },
    next: { letter: "Z", title: "Zero Defects", kicker: "ലെസൺ പൂർത്തിയാക്കിയതിന്", cue: "ഇനി പോകൂ" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_ML_DURATION = PLAN.total;

export const ZeroDefectsMl: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ml");
  setUI("ml");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
