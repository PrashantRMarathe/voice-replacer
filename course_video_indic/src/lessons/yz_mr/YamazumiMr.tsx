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
import words from "../../captions/yz_mr/words.json";

// Marathi version of YamazumiMr (same design and polish as the English lesson).
// All data comes from narration/yamazumi_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "yz_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "YAMAZUMI",
  title: "Yamazumi",
  subtitle: "खऱ्या डेटाने, TAKT समोर लाइन बॅलन्स करा",
  outroLine: "मोजा. रचा. बॅलन्स करा.",
  outroSub: "Yamazumi — असा फ्लो, जो डिझाइनमुळे टिकतो",
};

// Same polish as English Yamazumi; cues are phrases from the Marathi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3, icon: "person", label: "ऑपरेटर वाट पाहतात, तर एक स्क्रूमध्ये गाडलेला",
    sub: "कोणीही आळशी नाही. काम फक्त असमानपणे साचलं आहे.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "स्टेशन B, TAKT च्या वर", before: 35, after: 30, unit: "स्टेशन B वर कामाचे सेकंद",
    fixedLabel: "मग TAKT वर",
    takeaways: [
      { text: "खरं काम मोजा, सर्वात चांगली केस नाही", cue: "खरं काम मोजा" },
      { text: "TAKT समोर रचा, ढीग पाहा", cue: "ते TAKT समोर" },
      { text: "सेफ्टी किंवा क्वालिटी पणाला न लावता बॅलन्स", cue: "आणि काळजीपूर्वक" },
    ],
    action: { text: "तुमच्या लाइनच्या एका स्टेशनचा वेळ मोजा, आणि TAKT समोर त्याचा बार बनवा.", cue: "या आठवड्यात तुमचं काम" },
    next: { letter: "Z", title: "Zero Defects", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const YAMAZUMI_MR_DURATION = PLAN.total;

export const YamazumiMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
