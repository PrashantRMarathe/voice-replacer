// On-screen words built into the shared scenes, in this project's languages.
// tools/sync_from_english.py points the copied English components at `UI`
// (the English project keeps its own literals). One label set per language;
// each lesson picks its set with setUI(lang) at the top of its component, so
// a Hindi and a Marathi lesson in the same render never show the wrong words.
export type UiLang = "hi" | "mr";

type UiSet = {
  example: string;
  quickCheck: string;
  think: string;
  answer: string;
  strongest: string;
  weakest: string;
  good: string;
  notGood: string;
  average: string;
  rememberStart: string;
  threeThings: string;
  actionThisWeek: string;
  nextLesson: string;
  problemFixed: string;               // recap: under the fixed number
  screws: (n: number) => string;      // assembly visual counter
  fixtureLocked: string;              // assembly visual, before 6/6
  fixtureReleases: string;            // assembly visual, at 6/6
};

const SETS: Record<UiLang, UiSet> = {
  hi: {
    example: "उदाहरण",
    quickCheck: "क्विक चेक",
    think: "सोचिए…",
    answer: "जवाब",
    strongest: "सबसे मज़बूत",
    weakest: "सबसे कमज़ोर",
    good: "सही",
    notGood: "सही नहीं",
    average: "औसत",
    rememberStart: "शुरुआत याद है?",
    threeThings: "तीन बातें याद रखें",
    actionThisWeek: "इस हफ़्ते आपका काम",
    nextLesson: "अगला लेसन",
    problemFixed: "समस्या हल",
    screws: (n) => `स्क्रू ${n}/6`,
    fixtureLocked: "6/6 तक फ़िक्स्चर लॉक",
    fixtureReleases: "सब ठीक: फ़िक्स्चर खुलता है",
  },
  mr: {
    example: "उदाहरण",
    quickCheck: "झटपट तपासणी",
    think: "विचार करा…",
    answer: "उत्तर",
    strongest: "सर्वात मजबूत",
    weakest: "सर्वात कमकुवत",
    good: "बरोबर",
    notGood: "बरोबर नाही",
    average: "सरासरी",
    rememberStart: "सुरुवात आठवते?",
    threeThings: "तीन गोष्टी लक्षात ठेवा",
    actionThisWeek: "या आठवड्याचं तुमचं काम",
    nextLesson: "पुढचा धडा",
    problemFixed: "समस्या सुटली",
    screws: (n) => `स्क्रू ${n}/6`,
    fixtureLocked: "6/6 होईपर्यंत फिक्स्चर लॉक",
    fixtureReleases: "सगळं ठीक: फिक्स्चर उघडतं",
  },
};

// Live binding: the shared components import { UI } and see the current set.
// Hindi is the default so existing lessons keep working.
export let UI: UiSet = SETS.hi;
export const setUI = (lang: UiLang) => { UI = SETS[lang]; };
