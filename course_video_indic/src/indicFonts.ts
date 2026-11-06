// Fonts for translated lessons. Loaded only by the lesson that needs them (from
// inside its component), so English renders never fetch extra fonts. theme.ts
// lists these families after Poppins/Inter, so they draw only the native-script
// glyphs; English words and digits keep the course fonts.
import { loadFont as loadDevanagari } from "@remotion/google-fonts/NotoSansDevanagari";
import { loadFont as loadTelugu } from "@remotion/google-fonts/NotoSansTelugu";
import { loadFont as loadTamil } from "@remotion/google-fonts/NotoSansTamil";

export type IndicLang = "hi" | "mr" | "te" | "ta";

// Marathi uses the Devanagari script too, so it shares the Noto Sans Devanagari loader.
const devanagari = () => loadDevanagari("normal", { weights: ["400", "600", "700"], subsets: ["devanagari"] });

const loaders: Record<IndicLang, () => void> = {
  hi: devanagari,
  mr: devanagari,
  te: () => loadTelugu("normal", { weights: ["400", "600", "700"], subsets: ["telugu"] }),
  ta: () => loadTamil("normal", { weights: ["400", "600", "700"], subsets: ["tamil"] }),
};

const loaded = new Set<IndicLang>();

export const ensureIndicFont = (lang: IndicLang) => {
  if (loaded.has(lang)) return;
  loaded.add(lang);
  loaders[lang]();
};
