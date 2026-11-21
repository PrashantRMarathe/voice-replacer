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
import words from "../../captions/ew_mr/words.json";

// Marathi version of EliminationOfWasteMr (same design and polish as the English lesson).
// All data comes from narration/elimination_of_waste_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ew_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ELIMINATION OF WASTE",
  title: "Elimination of Waste",
  subtitle: "ज्याचे पैसे ग्राहक देणार नाही, ते काढा",
  outroLine: "पाहा. कारण काढा. सिद्ध करा.",
  outroSub: "Elimination of Waste — जास्त व्हॅल्यू, कमी मेहनत",
};

// Same polish as English EliminationOfWaste; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1500, icon: "wrench", label: "साउंडबारचं दर महिन्याला रीवर्क",
    sub: "प्रत्येक दुरुस्त करायला ₹42. कोणी कधी याची बेरीजच केली नव्हती.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "गुणगुणणाऱ्या स्पीकर वायरमुळे रीवर्क होणारे साउंडबार", before: 1500, after: 300, unit: "रीवर्क प्रति महिना", fixedLabel: "रीवर्क 80% कमी",
    takeaways: [
      { text: "वेस्ट: ज्याचे पैसे ग्राहक देणार नाही", cue: "वेस्ट म्हणजे असं सगळं" },
      { text: "ते Gemba वर तथ्यांनी शोधा", cue: "ते Gemba वर" },
      { text: "कारण काढा, सिद्ध करा, टिकवा", cue: "आणि कारण काढा" },
    ],
    action: { text: "तीस मिनिटं तुमच्या लाइनवर फिरा, आणि तीन वेस्ट तथ्यांच्या रूपात लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "F", title: "FMEA", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ELIMINATION_OF_WASTE_MR_DURATION = PLAN.total;

export const EliminationOfWasteMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
