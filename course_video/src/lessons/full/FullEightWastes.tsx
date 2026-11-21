import React from "react";
import {
  AbsoluteFill, Audio, Sequence, staticFile,
  interpolate, spring, useCurrentFrame, useVideoConfig,
} from "remotion";
import { Background } from "../../components/Background";
import { RiseIn } from "../../components/ui";
import {
  IconDefect, IconOverproduction, IconWaiting, IconTalent,
  IconTransport, IconInventory, IconMotion, IconProcessing,
} from "../../components/icons";
import { Scene } from "../../scenes/Scene";
import { BrandMark } from "../../components/BrandMark";
import { theme, fps as FPS } from "../../theme";
import timings from "./timings.json";
import content from "./content.json";
import "../../fonts";

const ICONS: Record<string, React.FC<{ color: string; size?: number; progress?: number }>> = {
  Defect: IconDefect, Overproduction: IconOverproduction, Waiting: IconWaiting,
  Talent: IconTalent, Transport: IconTransport, Inventory: IconInventory,
  Motion: IconMotion, Processing: IconProcessing,
};

type Waste = { l: string; name: string; icon: string; def: string; example: string; fix: string };
const WASTES = (content as { wastes: Waste[] }).wastes;

// ---- helpers ----
const sec = (k: string) => (timings as Record<string, number>)[k] ?? 5;
const DEEP_PAD = 3.6; // extra seconds held after a deep-dive narration
const PAD = 2.8;      // extra seconds for the shorter scenes
const frames = (s: number) => Math.ceil(s * FPS);

// ---------- Scene 1: Intro ----------
const IntroScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const line = spring({ frame: frame - 20, fps, config: { damping: 20 } });
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 30, letterSpacing: 8, textAlign: "center" }}>
          {theme.brand.courseName.toUpperCase()}
        </div>
      </RiseIn>
      <RiseIn delay={10}>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 110, fontWeight: 700, textAlign: "center", marginTop: 10, textShadow: `0 0 40px ${theme.colors.accent}55` }}>
          The 8 Wastes of Lean
        </div>
      </RiseIn>
      <div style={{ height: 6, width: interpolate(line, [0, 1], [0, 480]), background: theme.colors.accent, borderRadius: 4, marginTop: 30, boxShadow: `0 0 24px ${theme.colors.accent}` }} />
      <RiseIn delay={30}>
        <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 34, marginTop: 30 }}>
          Remember them with one word: <b style={{ color: theme.colors.accentSoft }}>DOWNTIME</b>
        </div>
      </RiseIn>
    </Scene>
  );
};

// ---------- Scene 2: Value vs waste (animated bar) ----------
const ValueScene: React.FC = () => {
  const frame = useCurrentFrame();
  const grow = interpolate(frame, [30, 90], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 58, fontWeight: 600, marginBottom: 50 }}>
          Most of what we do is waste
        </div>
      </RiseIn>
      <div style={{ width: 1300, height: 90, borderRadius: 14, overflow: "hidden", display: "flex", border: `2px solid ${theme.colors.panelBorder}` }}>
        <div style={{ width: `${5 * grow}%`, background: theme.colors.good, transition: "none" }} />
        <div style={{ width: `${95 * grow}%`, background: theme.colors.danger }} />
      </div>
      <div style={{ display: "flex", gap: 60, marginTop: 34 }}>
        <RiseIn delay={30}><div style={{ color: theme.colors.good, fontFamily: theme.font.body, fontSize: 30, fontWeight: 600 }}>■ ~5% Value-added</div></RiseIn>
        <RiseIn delay={45}><div style={{ color: theme.colors.danger, fontFamily: theme.font.body, fontSize: 30, fontWeight: 600 }}>■ ~95% Waste & non-value</div></RiseIn>
      </div>
      <RiseIn delay={70}>
        <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 26, marginTop: 40, maxWidth: 1100, textAlign: "center", lineHeight: 1.4 }}>
          Value-added work is what the customer gladly pays for. Lean is the discipline of seeing — and removing — everything else.
        </div>
      </RiseIn>
    </Scene>
  );
};

// ---------- Scene 3: Muda / Mura / Muri ----------
const MMMScene: React.FC = () => {
  const items = [
    { jp: "Muda", en: "Waste", d: "The 8 wastes — effort with no value.", c: theme.colors.accent },
    { jp: "Mura", en: "Unevenness", d: "Peaks and troughs in the workload.", c: theme.colors.accent2 },
    { jp: "Muri", en: "Overburden", d: "Pushing people & machines too hard.", c: theme.colors.danger },
  ];
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 58, fontWeight: 600, marginBottom: 54 }}>
          The three enemies of flow
        </div>
      </RiseIn>
      <div style={{ display: "flex", gap: 30 }}>
        {items.map((it, i) => (
          <RiseIn key={it.jp} delay={i * 14}>
            <div style={{ width: 380, background: theme.colors.panel, border: `2px solid ${it.c}`, borderRadius: 20, padding: 34, boxShadow: `0 0 28px ${it.c}33` }}>
              <div style={{ color: it.c, fontFamily: theme.font.heading, fontSize: 52, fontWeight: 700 }}>{it.jp}</div>
              <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 28, marginTop: 6 }}>{it.en}</div>
              <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 23, marginTop: 16, lineHeight: 1.4 }}>{it.d}</div>
            </div>
          </RiseIn>
        ))}
      </div>
    </Scene>
  );
};

// ---------- Deep-dive scene for ONE waste (data-driven, reused 8x) ----------
const DeepDive: React.FC<{ w: Waste; n: number }> = ({ w, n }) => {
  const frame = useCurrentFrame();
  const Icon = ICONS[w.icon];
  const iconP = interpolate(frame, [10, 34], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const row = (label: string, text: string, color: string, delay: number) => (
    <RiseIn delay={delay}>
      <div style={{ display: "flex", gap: 18, alignItems: "flex-start", marginTop: 22 }}>
        <div style={{ color, fontFamily: theme.font.body, fontSize: 22, fontWeight: 700, minWidth: 130, textTransform: "uppercase", letterSpacing: 1 }}>{label}</div>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 30, lineHeight: 1.35, maxWidth: 1000 }}>{text}</div>
      </div>
    </RiseIn>
  );
  return (
    <Scene>
      <div style={{ width: 1500, display: "flex", flexDirection: "column" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 28 }}>
          <RiseIn>
            <div style={{ width: 130, height: 130, borderRadius: 24, background: theme.colors.panel, border: `2.5px solid ${theme.colors.accent}`, display: "flex", alignItems: "center", justifyContent: "center", boxShadow: `0 0 34px ${theme.colors.accent}55` }}>
              {Icon && <Icon color={theme.colors.accent} size={78} progress={iconP} />}
            </div>
          </RiseIn>
          <div>
            <RiseIn delay={6}>
              <div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 26, fontWeight: 700, letterSpacing: 3 }}>
                WASTE {n} OF 8 · {w.l}
              </div>
            </RiseIn>
            <RiseIn delay={12}>
              <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 76, fontWeight: 700 }}>{w.name}</div>
            </RiseIn>
          </div>
        </div>
        <div style={{ height: 2, background: theme.colors.panelBorder, marginTop: 30 }} />
        {row("What it is", w.def, theme.colors.accentSoft, 26)}
        {row("Example", w.example, theme.colors.accent2, 46)}
        {row("How to fix", w.fix, theme.colors.good, 66)}
      </div>
    </Scene>
  );
};

// ---------- Summary: DOWNTIME column lighting up ----------
const SummaryScene: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <Scene>
      <RiseIn>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 60, fontWeight: 600, marginBottom: 40 }}>
          The 8 Wastes = DOWNTIME
        </div>
      </RiseIn>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px 80px" }}>
        {WASTES.map((w, i) => {
          const lit = frame > 20 + i * 12;
          return (
            <div key={w.l} style={{ display: "flex", alignItems: "center", gap: 18, opacity: lit ? 1 : 0.15, transition: "none" }}>
              <div style={{ width: 54, height: 54, borderRadius: 12, background: theme.colors.panel, border: `2px solid ${theme.colors.accent}`, color: theme.colors.accentSoft, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: theme.font.heading, fontWeight: 700, fontSize: 30, boxShadow: lit ? `0 0 18px ${theme.colors.accent}66` : "none" }}>{w.l}</div>
              <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 34 }}>{w.name}</div>
            </div>
          );
        })}
      </div>
    </Scene>
  );
};

// ---------- Outro ----------
const OutroScene: React.FC = () => (
  <Scene>
    <RiseIn>
      <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 80, fontWeight: 700, textAlign: "center", textShadow: `0 0 40px ${theme.colors.accent}55` }}>
        See the waste. Remove the waste.
      </div>
    </RiseIn>
    <RiseIn delay={16}>
      <div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.body, fontSize: 36, marginTop: 26, textAlign: "center" }}>
        Next lesson: The 5S System →
      </div>
    </RiseIn>
  </Scene>
);

// ---------- Assemble ----------
const audio = (f: string) => staticFile(`audio/full/${f}.mp3`);

// Scene order + hold per scene. The duration below is derived from this same
// list, so the composition length always matches what renders.
const ORDER: { key: string; pad: number }[] = [
  { key: "intro", pad: PAD },
  { key: "value", pad: PAD },
  { key: "mmm", pad: PAD },
  ...WASTES.map((w) => ({ key: `waste_${w.l}`, pad: DEEP_PAD })),
  { key: "summary", pad: PAD },
  { key: "outro", pad: PAD },
];

export const FullEightWastes: React.FC = () => {
  const node = (key: string): React.ReactNode => {
    if (key === "intro") return <IntroScene />;
    if (key === "value") return <ValueScene />;
    if (key === "mmm") return <MMMScene />;
    if (key === "summary") return <SummaryScene />;
    if (key === "outro") return <OutroScene />;
    const i = WASTES.findIndex((w) => `waste_${w.l}` === key);
    return <DeepDive w={WASTES[i]} n={i + 1} />;
  };

  let from = 0;
  return (
    <AbsoluteFill style={{ background: theme.colors.bg }}>
      <Background />
      {/* VOICE-ONLY: narration is the only audio (no music, no SFX). */}
      {ORDER.map((b) => {
        const dur = frames(sec(b.key) + b.pad);
        const el = (
          <Sequence key={b.key} from={from} durationInFrames={dur}>
            {node(b.key)}
            <Audio src={audio(b.key)} />
          </Sequence>
        );
        from += dur;
        return el;
      })}
      <BrandMark />
    </AbsoluteFill>
  );
};

export const FULL_DURATION = ORDER.reduce((acc, b) => acc + frames(sec(b.key) + b.pad), 0);
