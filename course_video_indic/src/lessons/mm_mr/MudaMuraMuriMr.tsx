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
import words from "../../captions/mm_mr/words.json";

// Marathi version of MudaMuraMuriMr (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "वेस्ट, असमानता आणि जादा भार — तिन्ही सुधारा",
  outroLine: "लेव्हल करा. वाचवा. काढा.",
  outroSub: "3M — स्थिर फ्लो, जलद लोक नाही",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "कॅमेरे मागे, शिफ्ट संपायला एक तास बाकी",
    sub: "प्रत्येकजण धावतोय. टेस्टवर चुका साचतायत.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "संजयची लाइन रोज उशिरा चालायची", before: 150, after: 0, unit: "मिनिटं ओव्हरटाइम प्रति दिवस",
    takeaways: [
      { text: "Muda वेस्ट, Mura असमानता, Muri जादा भार", cue: "Muda म्हणजे वेस्ट" },
      { text: "ते एकमेकांना वाढवतात: एकत्र सुधारा", cue: "ते एकमेकांना" },
      { text: "स्थिर फ्लो, जलद लोक नाही", cue: "आणि ध्येय आहे" },
    ],
    action: { text: "एका प्रॉडक्टसोबत तुमच्या लाइनवरून चाला, आणि प्रत्येक M चं एक उदाहरण टॅग करा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "N", title: "Next Inspection", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_MR_DURATION = PLAN.total;

export const MudaMuraMuriMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
