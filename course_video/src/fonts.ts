// Fonts load from public/fonts (no network at render time): fetching them from
// Google mid-render killed a 12-minute render when the internet dropped.
// Only the weights the course uses (Poppins 400-700, Inter variable), latin.
import { cancelRender, continueRender, delayRender, staticFile } from "remotion";

const FACES: [family: string, file: string, weight: string][] = [
  ["Poppins", "Poppins-400.woff2", "400"],
  ["Poppins", "Poppins-500.woff2", "500"],
  ["Poppins", "Poppins-600.woff2", "600"],
  ["Poppins", "Poppins-700.woff2", "700"],
  ["Inter", "Inter-var.woff2", "100 900"],
];

if (typeof document !== "undefined") {
  const handle = delayRender("Loading local fonts");
  Promise.all(FACES.map(async ([family, file, weight]) => {
    const face = new FontFace(family, `url(${staticFile(`fonts/${file}`)}) format("woff2")`, { weight, style: "normal" });
    // (this TS DOM lib lacks FontFaceSet.add; every browser Remotion uses has it)
    (document.fonts as unknown as { add(f: FontFace): void }).add(await face.load());
  }))
    .then(() => continueRender(handle))
    .catch((err) => cancelRender(err));
}
