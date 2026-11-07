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
import words from "../../captions/fm_mr/words.json";

// Marathi version of FMEAMr (same design and polish as the English lesson).
// All data comes from narration/fmea_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "fm_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "FMEA",
  title: "FMEA",
  subtitle: "फेल्युअर मोड अँड इफेक्ट्स ॲनालिसिस: फेल्युअरआधी विचार करा",
  outroLine: "साखळी बनवा. स्कोअर द्या. रोखा.",
  outroSub: "FMEA — एक जिवंत प्लान, फॉर्म नाही",
};

// Same polish as English FMEA; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 6, icon: "warning", label: "आउटडोर रेडिओ पाण्याने भरून परत आले",
    sub: "दोनमध्ये गॅस्केट गहाळ, चारमध्ये वाकलेलं. सगळे फायनल इन्स्पेक्शनमध्ये पास होते.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "आउटडोर 5G रेडिओवर गॅस्केटचा धोका", before: 240, after: 32, unit: "रिस्क प्रायॉरिटी नंबर",
    fixedLabel: "धोका कमी, ट्रायलमध्ये सिद्ध",
    takeaways: [
      { text: "परिणाम → फेल्युअर मोड → नियंत्रित होणारं कारण", cue: "एक स्पष्ट साखळी" },
      { text: "पुराव्याने स्कोअर; आकड्यापेक्षा समज मोठी", cue: "पुराव्यासह" },
      { text: "आधी प्रतिबंध, सिद्ध करा, मग पुन्हा स्कोअर", cue: "आणि प्रतिबंध" },
    ],
    action: { text: "एक महत्त्वाची पायरी निवडा, आणि तुमच्या टीमसोबत तिची फेल्युअर साखळी लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "G", title: "Gemba", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const FMEA_MR_DURATION = PLAN.total;

export const FMEAMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
