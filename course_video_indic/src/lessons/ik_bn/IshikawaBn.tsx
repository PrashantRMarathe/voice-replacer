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
import words from "../../captions/ik_bn/words.json";

// Bengali version of IshikawaBn (same design and polish as the English lesson).
// All data comes from narration/ishikawa_bn.py (+ import_clones.py).
const DATA: LessonData = {
  id: "ik_bn",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "ISHIKAWA DIAGRAM",
  title: "Ishikawa Diagram",
  subtitle: "ফিশবোন দিয়ে খোলা মনে খুঁজুন, তারপর কারণ প্রমাণ করুন",
  outroLine: "খোলা মনে খুঁজুন। নিখুঁতভাবে প্রমাণ করুন।",
  outroSub: "Ishikawa — পরখ না হওয়া পর্যন্ত প্রতিটি হাড় একটা অনুমান",
};

// Same polish as English Ishikawa; cues are phrases from the Bengali intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 32, icon: "warning", label: "প্রতি 1,000 এ সুইচ পোর্ট টেস্টে ফেল",
    sub: "5 থেকে বেড়ে। মিটিংয়ের উত্তর: নতুন টেস্টার কেনো।", until: "এই পাঠে",
  },
  recap: {
    problem: "সুইচ লাইনে পোর্ট-লিংক ফেলিওর", before: 32, after: 4, unit: "প্রতি 1,000 সুইচে",
    fixedLabel: "দুটো কারণই ঠিক",
    takeaways: [
      { text: "মাথায় স্পষ্ট, মাপা যায় এমন প্রভাব", cue: "মাথায় একটা" },
      { text: "6M এ খোলা মনে খুঁজুন, দোষারোপ ছাড়া", cue: "ছয়টি এম এ" },
      { text: "প্রমাণ না হওয়া পর্যন্ত প্রতিটি হাড় অনুমান", cue: "আর প্রতিটি হাড়কে" },
    ],
    action: { text: "বারবার ফিরে আসা একটা সমস্যার ফিশবোন বানান, আর পরখের জন্য তিনটে কারণ বাছুন।", cue: "এই সপ্তাহে আপনার কাজ" },
    next: { letter: "J", title: "Jidoka", cue: "এরপর, আপনি" },
  },
};

const PLAN = planLesson(DATA, fps);
export const ISHIKAWA_BN_DURATION = PLAN.total;

export const IshikawaBn: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("bn");
  setUI("bn");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
