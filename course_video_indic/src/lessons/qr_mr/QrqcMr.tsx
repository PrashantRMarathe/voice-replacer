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
import words from "../../captions/qr_mr/words.json";

// Marathi version of QrqcMr (same design and polish as the English lesson).
// All data comes from narration/qrqc_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "qr_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "QRQC",
  title: "Quick Response Quality Control",
  subtitle: "मिनिटांत कृती — पुराव्यासह बंद",
  outroLine: "पकडा. रोखा. सिद्ध करा.",
  outroSub: "QRQC — वेगवान रिस्पॉन्स, खरा पुरावा",
};

// Same polish as English QRQC; cues are phrases from the Marathi intro/outro.
// hook.value is 24 (the page-5 count), not the English polish's 18.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 24, icon: "camera", label: "कॅमेरे दुपारपर्यंत फोकस टेस्टमध्ये फेल",
    sub: "कोणीतरी टेस्टर रीसेट केला, आणि लाइन चालू राहिली.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "वेअरहाउसकडे जाणारे संशयित कॅमेरे", before: 2000, after: 0, unit: "संशयित कॅमेरे हिशोबाशिवाय",
    takeaways: [
      { text: "वेगाने कृती, पण पुराव्यासह", cue: "वेगाने कृती" },
      { text: "आधी कंटेनमेंट, प्रत्येक युनिटचा हिशोब", cue: "आधी कंटेनमेंट" },
      { text: "उपाय सिद्ध झाल्यावरच बंद करा", cue: "आणि मुद्दा तेव्हाच" },
    ],
    action: { text: "एका गंभीर डिफेक्टसाठी तुमच्या रिस्पॉन्स प्लानची पहिली 30 मिनिटं लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const QRQC_MR_DURATION = PLAN.total;

export const QrqcMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
