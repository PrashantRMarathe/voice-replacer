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
import words from "../../captions/mm_hi/words.json";

// hi version of MudaMuraMuriHi (same design and polish as the English lesson).
// All data comes from narration/muda_mura_muri_hi.py (+ import_clones.py).
const DATA: LessonData = {
  id: "mm_hi",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "MUDA · MURA · MURI",
  title: "Muda, Mura & Muri",
  subtitle: "वेस्ट, असमानता और ज़्यादा बोझ — तीनों सुधारें",
  outroLine: "लेवल करें। बचाएँ। हटाएँ।",
  outroSub: "3M — स्थिर फ़्लो, तेज़ लोग नहीं",
};

// Same polish as English MudaMuraMuri; cues are phrases from the Hindi intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 40, icon: "clock", label: "कैमरे पीछे, शिफ़्ट खत्म होने से एक घंटा पहले",
    sub: "हर कोई भाग रहा है। टेस्ट पर गलतियाँ जमा हो रही हैं।", until: "इस लेसन में",
  },
  recap: {
    problem: "संजय की लाइन रोज़ लेट चलती थी", before: 150, after: 0, unit: "मिनट ओवरटाइम प्रति दिन",
    takeaways: [
      { text: "Muda वेस्ट, Mura असमानता, Muri ज़्यादा बोझ", cue: "Muda है वेस्ट" },
      { text: "ये एक-दूसरे को बढ़ाते हैं: साथ सुधारें", cue: "ये एक-दूसरे को" },
      { text: "स्थिर फ़्लो, तेज़ लोग नहीं", cue: "और लक्ष्य है" },
    ],
    action: { text: "एक प्रोडक्ट को अपनी लाइन से गुज़ारते हुए चलें, और हर M का एक उदाहरण टैग करें।", cue: "इस हफ़्ते का आपका काम" },
    next: { letter: "N", title: "Next Inspection", cue: "आगे, आप" },
  },
};

const PLAN = planLesson(DATA, fps);
export const MUDA_MURA_MURI_HI_DURATION = PLAN.total;

export const MudaMuraMuriHi: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("hi");
  setUI("hi");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
