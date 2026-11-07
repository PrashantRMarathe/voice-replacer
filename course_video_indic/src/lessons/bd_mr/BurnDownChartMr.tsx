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
import words from "../../captions/bd_mr/words.json";

// Marathi version of BurnDownChartMr (same design and polish as the English lesson).
// All data comes from narration/burn_down_chart_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "bd_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "BURN DOWN CHART",
  title: "Burn Down Chart",
  subtitle: "डेडलाइनआधी उरलेलं काम पाहा",
  outroLine: "लाइन ठरवा. गॅप पाहा. आजच कृती करा.",
  outroSub: "Burn Down Chart — आता शुक्रवारचे धक्के नाहीत",
};

// Same polish as English BurnDownChart; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 80, icon: "box", label: "राउटर ट्रकमधून राहिले",
    sub: "शुक्रवार दुपारपर्यंत कोणाला कल्पनाही नव्हती.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "डिस्पॅचवेळी कमी पडलेले राउटर", before: 80, after: 0, unit: "राउटर कमी",
    takeaways: [
      { text: "आधी आयडियल लाइन; ती पुन्हा कधीच नाही", cue: "आधी आयडियल लाइन" },
      { text: "फक्त पूर्ण आणि चांगलं काम मोजा", cue: "फक्त तेच काम" },
      { text: "आयडियलच्या वर? त्याच दिवशी कृती, ओनरसह", cue: "आणि लाइन आयडियलच्या" },
    ],
    action: { text: "डेडलाइन असलेलं एक काम निवडा, आणि उद्याच्या शिफ्टआधी त्याचा बर्न-डाउन बनवा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "C", title: "Cycle Time Study", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const BURN_DOWN_CHART_MR_DURATION = PLAN.total;

export const BurnDownChartMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
