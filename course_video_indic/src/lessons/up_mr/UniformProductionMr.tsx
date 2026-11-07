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
import words from "../../captions/up_mr/words.json";

// Marathi version of UniformProductionMr (same design and polish as the English lesson).
// All data comes from narration/uniform_production_mr.py (+ import_clones.py).
const DATA: LessonData = {
  id: "up_mr",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "UNIFORM PRODUCTION",
  title: "Uniform Production",
  subtitle: "व्हॉल्यूम आणि मिक्स लेव्हल करा, स्थिर आणि विश्वासार्ह फ्लोसाठी",
  outroLine: "लेव्हल करा. क्रम ठरवा. स्थिर करा.",
  outroSub: "Uniform Production — असा वेग, जो तुमची लाइन टिकवू शकेल",
};

// Same polish as English UniformProduction; cues are phrases from the Marathi intro/outro.
// recap.after is 6,000 (the page-4 daily rate), not the English polish's 2,400.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 3000, icon: "wave", label: "फोन सोमवारी. मंगळवारी जवळजवळ काहीच नाही.",
    sub: "बुधवारपर्यंत, टेस्ट बेंच कामात बुडाली आहे.", until: "या लेसनमध्ये",
  },
  recap: {
    problem: "एक खूप खडबडीत शेड्यूल", before: 0, after: 6000, unit: "चांगली युनिट रोज, प्रत्येक दिवशी",
    fixedLabel: "एक स्थिर, लेव्हल वेग",
    takeaways: [
      { text: "व्हॉल्यूम आणि मिक्स, दोन्ही लेव्हल करा", cue: "व्हॉल्यूम आणि मिक्स, दोन्ही" },
      { text: "आधी बॉटलनेक आणि चेंजओव्हर तपासा", cue: "कोणत्याही पॅटर्नवर" },
      { text: "दृश्य प्लान, बदलाचे स्पष्ट नियम", cue: "आणि प्लान दृश्य" },
    ],
    action: { text: "मोठ्या बॅचमध्ये बनणारं एक प्रॉडक्ट शोधा, आणि छोट्या, पुनरावृत्तीच्या पॅटर्नचं स्केच बनवा.", cue: "या आठवड्याचं तुमचं काम" },
    next: { letter: "V", title: "Value Stream Mapping", cue: "पुढे, तुम्ही" },
  },
};

const PLAN = planLesson(DATA, fps);
export const UNIFORM_PRODUCTION_MR_DURATION = PLAN.total;

export const UniformProductionMr: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("mr");
  setUI("mr");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
