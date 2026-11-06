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
import words from "../../captions/sk_ta/words.json";

// Tamil version of SkillMatrixTa (same design and polish as the English lesson).
// All data comes from narration/skill_matrix_ta.py (+ import_clones.py).
const DATA: LessonData = {
  id: "sk_ta",
  timings: timings as Record<string, number>,
  pages: (content as { pages: Page[] }).pages,
  quizzes: (quizzes as { quizzes: Quiz[] }).quizzes,
  words: words as Record<string, Word[]>,
};

const TEXT: LessonText = {
  label: "SKILL TRAINING MATRIX",
  title: "Skill Training Matrix",
  subtitle: "யார் உண்மையில் எந்த வேலையைச் செய்ய முடியும் — இடைவெளிகள் எங்கே",
  outroLine: "சரிபாருங்கள். பயிற்சி கொடுங்கள். கவர் செய்யுங்கள்.",
  outroSub: "Skill Matrix — திறனின் உயிருள்ள கண்ட்ரோல்",
};

// Same polish as English SkillMatrix; cues are phrases from the Tamil intro/outro.
const POLISH: Polish = {
  sound: true, acting: true, focus: true, bigQuiz: true,
  hook: {
    value: 1, icon: "person", label: "லென்ஸ் ஃபோகஸ் செட் செய்யத் தெரிந்த நபர்",
    sub: "பாலாவுக்கு உடல்நலமில்லை. பத்து மணிக்குள், முழு செல்லும் நின்றது.", until: "இந்தப் பாடத்தில்",
  },
  recap: {
    problem: "ஒரே லென்ஸ் ஃபோகஸ் நிபுணர், அவரும் உடல்நலமின்றி", before: 1, after: 2, unit: "தகுதியான லென்ஸ் ஃபோகஸ் நிபுணர்கள்",
    takeaways: [
      { text: "நிரூபித்த திறன், வருகை அல்ல", cue: "ஸ்கில் மேட்ரிக்ஸ் நிரூபிக்கப்பட்ட" },
      { text: "ஒவ்வொரு ஷிஃப்ட்டிலும் தகுதியான பேக்கப்பை எண்ணுங்கள்", cue: "ஒவ்வொரு முக்கிய" },
      { text: "இதை உயிரோடு வையுங்கள், ஆதாரத்துடன்", cue: "இதை உயிரோடு" },
    ],
    action: { text: "உங்கள் மூன்று மிக முக்கிய ஸ்டேஷன்களை எழுதி, ஒவ்வொன்றுக்கும் தகுதியான ஆட்களை எண்ணுங்கள்.", cue: "இந்த வாரம் உங்கள் வேலை" },
    next: { letter: "T", title: "TAKT Time", cue: "அடுத்து, நீங்கள்" },
  },
};

const PLAN = planLesson(DATA, fps);
export const SKILL_MATRIX_TA_DURATION = PLAN.total;

export const SkillMatrixTa: React.FC<{ captions?: boolean }> = ({ captions = true }) => {
  ensureIndicFont("ta");
  setUI("ta");
  return (
    <PageLesson data={DATA} blocks={PLAN.blocks} text={TEXT} captions={captions}
      polish={{ ...POLISH, sound: captions }} />
  );
};
