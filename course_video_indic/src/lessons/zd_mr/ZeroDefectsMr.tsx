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
import words from "../../captions/zd_mr/words.json";

// Marathi version of ZeroDefectsMr (same design and polish as the English lesson).
// All data comes from narration/zero_defects_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "zd_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ZERO DEFECTS",
  title: "Zero Defects",
  subtitle: "डिफेक्ट रोखा — फक्त त्यांची तपासणी करू नका",
  outroLine: "रोखा. मोजा. सुधारा.",
  outroSub: "Zero Defects — रोजच्या मॅनेजमेंटचा भाग",
};

// Same polish as English ZeroDefects; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 400, icon: "power", label: "फोन रीवर्कसाठी परत आले",
    sub: "एक कनेक्टर, चुकीच्या पद्धतीने बसलेला. तो प्रत्येक व्हिज्युअल चेकमध्ये पास झाला.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "चुकीच्या बसलेल्या कनेक्टरमुळे चार्जिंग फेल्युअर", before: 1200, after: 200,
    unit: "फेल फोन, 40,000 पैकी", fixedLabel: "पुनरावृत्ती अवघड: 83% कमी",
    takeaways: [
      { text: "डिफेक्ट रोखा, फक्त तपासणी नाही", cue: "डिफेक्ट रोखा" },
      { text: "स्पष्ट व्याख्यांसह प्रामाणिकपणे मोजा", cue: "स्पष्ट व्याख्यांसह" },
      { text: "सिस्टिम दुरुस्त करा, व्यक्तीला नाही", cue: "आणि काही फेल" },
    ],
    action: { text: "वारंवार परत येणारा एक डिफेक्ट निवडा, आणि तो अशक्य कसा करायचा ते विचारा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "Z", title: "Zero Defects", kicker: "लेसन पूर्ण", cue: "आता जा" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ZERO_DEFECTS_MR_DURATION = PLAN.total;

export const ZeroDefectsMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
