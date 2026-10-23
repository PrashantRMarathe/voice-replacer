import React from "react";
import { AbsoluteFill, Sequence, spring, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { Background } from "../components/Background";
import { RiseIn } from "../components/ui";
import { Scene } from "../scenes/Scene";
import { Guide, Worker, SpeechBubble } from "../components/characters";
import { theme } from "../theme";
import "../fonts";

// ---- Scene 1: the guide introduces the lesson ----
const GuideIntro: React.FC = () => {
  return (
    <Scene>
      <div style={{ display: "flex", alignItems: "center", gap: 40 }}>
        <Guide size={420} delay={6} />
        <div style={{ display: "flex", flexDirection: "column", gap: 24, marginTop: -60 }}>
          <RiseIn delay={2}>
            <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 26, letterSpacing: 6 }}>
              {theme.brand.courseName.toUpperCase()}
            </div>
            <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 78, fontWeight: 700 }}>
              The 8 Wastes
            </div>
          </RiseIn>
          <SpeechBubble delay={26} text="Hi! I'm your guide. Let's spot the 8 wastes hiding in every factory." />
        </div>
      </div>
    </Scene>
  );
};

// ---- Scene 2: a worker ACTS OUT the Waiting waste ----
const WaitingAct: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const tag = spring({ frame: frame - 40, fps, config: { damping: 13 } });
  // the "machine" sits idle; a small light blinks red
  const red = 0.4 + 0.6 * (0.5 + 0.5 * Math.sin(frame / 10));
  return (
    <Scene>
      <div style={{ width: 1500, display: "flex", flexDirection: "column", alignItems: "center" }}>
        <RiseIn>
          <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 60, fontWeight: 700 }}>
            Waste #3 — <span style={{ color: theme.colors.accentSoft }}>Waiting</span>
          </div>
        </RiseIn>
        <div style={{ display: "flex", alignItems: "flex-end", gap: 80, marginTop: 40, height: 460 }}>
          {/* the idle worker, arms crossed, tired, bobbing */}
          <div style={{ position: "relative" }}>
            <Worker size={360} delay={10} pose="CrossedArmsWB" face="Tired" />
            <div style={{
              position: "absolute", top: -10, right: -30,
              transform: `scale(${tag})`, opacity: tag,
              color: theme.colors.danger, fontFamily: theme.font.body,
              fontWeight: 700, fontSize: 34,
            }}>
              ⏳ Waiting…
            </div>
          </div>
          {/* the paused machine */}
          <RiseIn delay={18}>
            <div style={{
              width: 300, height: 360,
              background: theme.colors.panel,
              border: `2px solid ${theme.colors.panelBorder}`,
              borderRadius: 18,
              display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
              gap: 18,
            }}>
              <div style={{
                width: 40, height: 40, borderRadius: 20,
                background: theme.colors.danger,
                boxShadow: `0 0 ${16 + 18 * red}px ${theme.colors.danger}`,
                opacity: red,
              }} />
              <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 26 }}>
                Machine idle
              </div>
            </div>
          </RiseIn>
        </div>
        {/* guide reacts in the corner */}
        <div style={{ position: "absolute", right: 40, bottom: 20 }}>
          <Guide size={230} delay={30} fromX={160} face="Concerned" />
        </div>
      </div>
    </Scene>
  );
};

export const CharacterSample: React.FC = () => {
  return (
    <AbsoluteFill style={{ background: theme.colors.bg }}>
      <Background />
      <Sequence durationInFrames={150}><GuideIntro /></Sequence>
      <Sequence from={150} durationInFrames={210}><WaitingAct /></Sequence>
    </AbsoluteFill>
  );
};

export const CHARACTER_SAMPLE_DURATION = 360;
