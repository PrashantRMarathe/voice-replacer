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
import words from "../../captions/kz_mr/words.json";

// Marathi version of KaizenMr (same design and polish as the English lesson).
// All data comes from narration/kaizen_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "kz_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "KAIZEN",
  title: "Kaizen",
  subtitle: "छोटे बदल, दररोज, काम करणाऱ्या लोकांकडून",
  outroLine: "पाहा. छोटं करून पाहा. स्टँडर्ड बनवा. पुन्हा करा.",
  outroSub: "Kaizen — आजची सर्वात चांगली पद्धत, उद्याची बेसलाइन",
};

// Same polish as English Kaizen; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 2, icon: "weight", label: "वेळा प्रत्येक मॉनिटर उलटवला जायचा",
    sub: "तोंड खाली, मग तोंड वर. नेहमीपासून असंच होत आलं होतं.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "मॉनिटर उलटवल्याने पॅनल स्क्रॅच", before: 15, after: 3, unit: "स्क्रॅच प्रति 1,000 मॉनिटर",
    fixedLabel: "90 दिवसांवरही टिकलं",
    takeaways: [
      { text: "Kaizen ही रोजची सवय आहे", cue: "Kaizen ही रोजची" },
      { text: "छोटं तपासा; दुसरं काही बिघडलं नाही ना ते तपासा", cue: "छोट्या प्रमाणात" },
      { text: "प्रत्येक फायद्याचं स्टँडर्ड बनवा", cue: "आणि प्रत्येक फायद्याचं" },
    ],
    action: { text: "एका ऑपरेटरला विचारा की त्याच्या कामात अवघड काय आहे, आणि एक छोटा उपाय तपासा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "L", title: "Low Cost Automation", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const KAIZEN_MR_DURATION = PLAN.total;

export const KaizenMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
