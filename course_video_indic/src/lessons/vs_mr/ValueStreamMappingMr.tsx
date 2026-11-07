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
import words from "../../captions/vs_mr/words.json";

// Marathi version of ValueStreamMappingMr (same design and polish as the English lesson).
// All data comes from narration/value_stream_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "vs_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "VALUE STREAM MAPPING",
  title: "Value Stream Mapping",
  subtitle: "ऑर्डरपासून डिलिव्हरीपर्यंत, पूर्ण फ्लो पाहा",
  outroLine: "पाहा. मोजा. फ्लो बनवा.",
  outroSub: "Value Stream Mapping — प्रतीक्षा शोधा, फ्लो डिझाइन करा",
};

// Same polish as English ValueStreamMapping; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 15, icon: "clock", label: "मिनिटं, एक सेट-टॉप बॉक्स बनायला आणि टेस्ट करायला",
    sub: "तरीही ग्राहकापर्यंत पोहोचायला सुमारे चार दिवस.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "मिनिटांच्या कामासाठी दिवसांची प्रतीक्षा", before: 4200, after: 2100, unit: "तीन बफरमध्ये प्रतीक्षेतली युनिट",
    fixedLabel: "फ्युचर स्टेट: निम्मी प्रतीक्षा",
    takeaways: [
      { text: "खऱ्या मटेरियल + माहिती फ्लोचा नकाशा", cue: "खऱ्या फ्लोचा नकाशा" },
      { text: "लीड टाइम प्रतीक्षेत लपलेला आहे, कामात नाही", cue: "तुमचा बहुतेक लीड" },
      { text: "स्टॉक कमी करण्याआधी फ्युचर स्टेट सिद्ध करा", cue: "आणि कोणताही स्टॉक" },
    ],
    action: { text: "एका प्रॉडक्ट फॅमिलीसोबत डिस्पॅचपासून उलटं चाला, आणि प्रत्येक ढीग मोजा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "W", title: "Why-Why Analysis", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const VALUE_STREAM_MAPPING_MR_DURATION = PLAN.total;

export const ValueStreamMappingMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
