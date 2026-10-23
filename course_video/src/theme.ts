// Central design system for the whole course. Change colors here once and
// every lesson updates. Keeps all 40 videos looking identical and professional.

export const theme = {
  colors: {
    bg: "#0a0e1a", // deep navy
    bgGradientTop: "#0d1324",
    bgGradientBottom: "#070a12",
    panel: "#111726",
    panelBorder: "#1d2740",
    accent: "#2dd4bf", // teal
    accentSoft: "#5eead4",
    accent2: "#38bdf8", // sky blue
    text: "#ffffff",
    textDim: "#9fb0c9",
    danger: "#f87171",
    good: "#34d399",
  },
  font: {
    heading: '"Poppins", system-ui, sans-serif',
    body: '"Inter", system-ui, sans-serif',
  },
  // Branding shown on intro/outro. Edit these for your course.
  brand: {
    courseName: "Lean Manufacturing Mastery",
    author: "Your Name",
  },
};

export const fps = 30;
export const width = 1920;
export const height = 1080;
