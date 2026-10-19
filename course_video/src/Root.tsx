import React from "react";
import { Composition } from "remotion";
import { EightWastes, EIGHT_WASTES_DURATION } from "./lessons/EightWastes";
import { FullEightWastes, FULL_DURATION } from "./lessons/full/FullEightWastes";
import { CharacterSample, CHARACTER_SAMPLE_DURATION } from "./lessons/CharacterSample";
import { fps, width, height } from "./theme";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="CharacterSample"
        component={CharacterSample}
        durationInFrames={CHARACTER_SAMPLE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FullEightWastes"
        component={FullEightWastes}
        durationInFrames={FULL_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EightWastes"
        component={EightWastes}
        durationInFrames={EIGHT_WASTES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      {/* dub-ready master: same video, no burned captions */}
      <Composition
        id="EightWastesDub"
        component={EightWastes}
        durationInFrames={EIGHT_WASTES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
    </>
  );
};
