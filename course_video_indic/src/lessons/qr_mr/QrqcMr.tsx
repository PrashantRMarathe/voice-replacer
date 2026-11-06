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

// Marathi version of QRQC (same design and polish as the English lesson).
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
  subtitle: "मिनिटांत प्रतिक्रिया — पुराव्याने क्लोज",
  outroLine: "शोधा. कंटेन करा. सिद्ध करा.",
  outroSub: "QRQC — झटपट प्रतिक्रिया, खरा पुरावा",
};

const PLAN = planLesson(DATA, fps);
export const QRQC_MR_DURATION = PLAN.total;

// Same polish as English QRQC; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "camera", label: "कॅमेरे दुपारपर्यंत फोकस टेस्टमध्ये फेल",
    sub: "कुणीतरी टेस्टर रीसेट केला, आणि लाइन चालूच राहिली.", until: "या धड्यात",
  },
  recap: {
    problem: "संशयित कॅमेरे वेअरहाऊसकडे निघाले", before: 2000, after: 0, unit: "संशयित कॅमेरे हिशेबाबाहेर",
    takeaways: [
      { text: "वेगाने प्रतिक्रिया द्या, पण पुराव्यासह", cue: "वेगाने प्रतिक्रिया द्या" },
      { text: "आधी कंटेन करा, प्रत्येक युनिट जुळवा", cue: "आधी कंटेन करा" },
      { text: "फिक्स सिद्ध झाल्यावरच क्लोज करा", cue: "आणि एखादा इश्यू" },
    ],
    action: { text: "एका क्रिटिकल डिफेक्टसाठी तुमच्या प्रतिक्रिया प्लॅनची पहिली 30 मिनिटं लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "R", title: "Root Cause Analysis", cue: "पुढे, तुम्ही रूट कॉज" },
  },
};

export const QrqcMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
