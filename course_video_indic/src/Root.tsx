import React from "react";
import { Composition } from "remotion";
import { UniformProductionHi, UNIFORM_PRODUCTION_HI_DURATION } from "./lessons/up_hi/UniformProductionHi";
import { PokaYokeHi, POKA_YOKE_HI_DURATION } from "./lessons/pk_hi/PokaYokeHi";
import { PokaYokeMr, POKA_YOKE_MR_DURATION } from "./lessons/pk_mr/PokaYokeMr";
import { QrqcMr, QRQC_MR_DURATION } from "./lessons/qr_mr/QrqcMr";
import { fps, width, height } from "./theme";

// Indian-language lessons only. Kept apart from course_video/ (the English
// course) so this work never touches the English pipeline.
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="UniformProductionHi"
        component={UniformProductionHi}
        durationInFrames={UNIFORM_PRODUCTION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionHiDub"
        component={UniformProductionHi}
        durationInFrames={UNIFORM_PRODUCTION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeHi"
        component={PokaYokeHi}
        durationInFrames={POKA_YOKE_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeHiDub"
        component={PokaYokeHi}
        durationInFrames={POKA_YOKE_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeMr"
        component={PokaYokeMr}
        durationInFrames={POKA_YOKE_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeMrDub"
        component={PokaYokeMr}
        durationInFrames={POKA_YOKE_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcMr"
        component={QrqcMr}
        durationInFrames={QRQC_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcMrDub"
        component={QrqcMr}
        durationInFrames={QRQC_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
    </>
  );
};
