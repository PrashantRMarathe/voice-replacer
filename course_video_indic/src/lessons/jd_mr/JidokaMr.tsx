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
import words from "../../captions/jd_mr/words.json";

// Marathi version of JidokaMr (same design and polish as the English lesson).
// All data comes from narration/jidoka_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "jd_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "JIDOKA",
  title: "Jidoka",
  subtitle: "मानवी स्पर्श असलेलं ऑटोमेशन",
  outroLine: "पाहा. थांबवा. सोडवा.",
  outroSub: "Jidoka — कोणताही डिफेक्ट पुढे नाही, कोणतीही गडबड लपलेली नाही",
};

// Same polish as English Jidoka; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 140, icon: "warning", label: "पेशंट मॉनिटरवर पातळ सील",
    sub: "डिस्पेन्सर रात्रभर छान चालला. त्याचं नोझल अर्धं बंद होतं.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "बंद ॲडहेसिव्ह नोझलमुळे पातळ सील", before: 140, after: 1, unit: "मॉनिटरवर परिणाम, प्रति नोझल समस्या",
    fixedLabel: "सोर्सवर पकडलं",
    takeaways: [
      { text: "आधी सामान्य ठरवा", cue: "आधी सामान्य" },
      { text: "पकडा, थांबवा, कंटेन करा: कोणताही डिफेक्ट पुढे नाही", cue: "सोर्सवरच" },
      { text: "प्रत्येक थांबा एक धडा: रूट कॉज दुरुस्त करा", cue: "आणि प्रत्येक थांबा" },
    ],
    action: { text: "एक ऑटोमॅटिक प्रोसेस निवडा, आणि ती कशावर थांबायला हवी ते लिहा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "K", title: "Kaizen", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const JIDOKA_MR_DURATION = PLAN.total;

export const JidokaMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
