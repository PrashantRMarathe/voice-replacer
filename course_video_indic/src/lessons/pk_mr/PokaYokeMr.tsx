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
import words from "../../captions/pk_mr/words.json";

// Marathi version of Poka Yoke (same design and polish as the English lesson).
// All data comes from narration/poka_yoke_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "pk_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "POKA YOKE",
  title: "Poka Yoke",
  subtitle: "चुकीचं काम अशक्य करा",
  outroLine: "काढून टाका. रोखा. पकडा.",
  outroSub: "Poka Yoke — क्वालिटीला स्मरणशक्तीच्या भरवशातून बाहेर काढा",
};

const PLAN = planLesson(DATA, fps);
export const POKA_YOKE_MR_DURATION = PLAN.total;

// Same polish as English PokaYoke; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 18, icon: "screw", label: "रेकॉर्डर एका स्क्रूशिवाय पाठवले गेले",
    sub: "ऑपरेटर कुशल आणि काळजी घेणारी होती. फक्त माणूस.", until: "या धड्यात",
  },
  recap: {
    problem: "रेकॉर्डर गहाळ स्क्रूसह पाठवले गेले", before: 18, after: 1, unit: "प्रति 10,000 युनिट",
    takeaways: [
      { text: "चुकांचा अंदाज बांधता येतो: त्या डिझाइनमधून काढा", cue: "चुकांचा अंदाज" },
      { text: "आधी रोखा, मग पकडा, मग इशारा", cue: "इशाऱ्यापेक्षा पकडणं" },
      { text: "प्रत्येक डिव्हाइसला खराब सॅम्पलने तपासा", cue: "आणि प्रत्येक डिव्हाइसला" },
    ],
    action: { text: "स्मरणशक्तीवर अवलंबून असलेला एक चेक शोधा, आणि त्यासाठी Poka Yoke स्केच करा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "Q", title: "QRQC", cue: "पुढे, तुम्ही QRQC" },
  },
};

export const PokaYokeMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
