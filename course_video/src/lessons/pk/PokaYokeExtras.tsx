import React from "react";
import { AbsoluteFill, Audio, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Background } from "../../components/Background";
import { BrandMark } from "../../components/BrandMark";
import { Character } from "../../components/characters";
import { VisualIcon } from "../../components/visualIcons";
import { RiseIn } from "../../components/ui";
import { cueTime, ActingGuide } from "../shared/polish";
import { toLines } from "../plan";
import { theme, fps } from "../../theme";
import { POKA_YOKE_DATA as DATA, POKA_YOKE_TEXT as TEXT, POKA_YOKE_POLISH as POLISH } from "./PokaYoke";
import "../../fonts";

// Promo pieces built from the same lesson data: a vertical Short of the hook,
// a YouTube thumbnail, and a one-page A4 cheat sheet. Trial for Poka Yoke.

const LETTER = "P";
const words = DATA.words.intro ?? [];
const swapAt = cueTime(words, "In this lesson") ?? 13;
const END_CARD = 3.5;
export const POKA_YOKE_SHORT_DURATION = Math.ceil(((DATA.timings.intro ?? 30) + 0.6 + END_CARD) * fps);

// ---------- vertical Short (1080x1920): the hook ----------
export const PokaYokeShort: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps: f, durationInFrames } = useVideoConfig();
  const t = frame / f;
  const swap = Math.round(swapAt * f);
  const endAt = durationInFrames - Math.round(END_CARD * f);
  const lines = React.useMemo(() => toLines(words, 34), []);
  const line = [...lines].reverse().find((l) => t >= l.s);
  const n = spring({ frame: frame - 25, fps: f, config: { damping: 30 }, durationInFrames: 40 });
  const hook = POLISH.hook!;
  return (
    <AbsoluteFill style={{ background: theme.colors.bg }}>
      <Background />
      <Audio src={staticFile(`audio/${DATA.id}/intro.mp3`)} />
      {/* series badge */}
      <div style={{ position: "absolute", top: 150, width: "100%", display: "flex", justifyContent: "center" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 18, background: theme.colors.panel, border: `2px solid ${theme.colors.accent}`, borderRadius: 50, padding: "10px 30px 10px 12px" }}>
          <div style={{ width: 64, height: 64, borderRadius: 64, background: theme.colors.accent, color: theme.colors.bg, fontFamily: theme.font.heading, fontSize: 40, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center" }}>{LETTER}</div>
          <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 34, fontWeight: 700, letterSpacing: 3 }}>LEAN A–Z</div>
        </div>
      </div>

      {frame < endAt && (
        <div style={{ position: "absolute", top: 330, width: "100%", display: "flex", flexDirection: "column", alignItems: "center", textAlign: "center", padding: "0 70px" }}>
          {frame < swap ? (
            <>
              <VisualIcon name={hook.icon} color={theme.colors.danger} size={190} />
              <div style={{ color: theme.colors.danger, fontFamily: theme.font.heading, fontSize: 300, fontWeight: 700, lineHeight: 1 }}>{Math.round(hook.value * n).toLocaleString("en-US")}</div>
              <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 66, fontWeight: 700, lineHeight: 1.15 }}>{hook.label}</div>
            </>
          ) : (
            <Sequence from={swap} layout="none">
              <RiseIn><div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 40, fontWeight: 700, letterSpacing: 6 }}>THE FIX</div></RiseIn>
              <RiseIn delay={6}><div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 150, fontWeight: 700, lineHeight: 1.05, textShadow: `0 0 50px ${theme.colors.accent}55` }}>{TEXT.title}</div></RiseIn>
              <RiseIn delay={14}><div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.body, fontSize: 52, marginTop: 20 }}>{TEXT.subtitle}</div></RiseIn>
              <div style={{ display: "flex", gap: 40, marginTop: 60 }}>
                {["key", "pin", "sensor"].map((ic, i) => (
                  <RiseIn key={ic} delay={30 + i * 10}>
                    <div style={{ background: theme.colors.panel, border: `2px solid ${theme.colors.accent}`, borderRadius: 28, padding: 30 }}>
                      <VisualIcon name={ic} color={theme.colors.accent} size={120} />
                    </div>
                  </RiseIn>
                ))}
              </div>
            </Sequence>
          )}
        </div>
      )}

      {/* big captions */}
      {frame < endAt && line && (
        <div style={{ position: "absolute", top: 1290, width: "100%", display: "flex", justifyContent: "center", padding: "0 60px" }}>
          <div style={{ background: "rgba(7,10,18,0.8)", border: `2px solid ${theme.colors.panelBorder}`, borderRadius: 24, padding: "22px 34px", color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 56, fontWeight: 600, lineHeight: 1.25, textAlign: "center" }}>
            {line.text}
          </div>
        </div>
      )}

      {/* end card */}
      {frame >= endAt && (
        <Sequence from={endAt} layout="none">
          <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", textAlign: "center", padding: 80 }}>
            <RiseIn><div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 46 }}>Full lesson</div></RiseIn>
            <RiseIn delay={6}><div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 96, fontWeight: 700, marginTop: 10 }}>{TEXT.title}</div></RiseIn>
            <RiseIn delay={12}><div style={{ color: theme.colors.accent, fontFamily: theme.font.body, fontSize: 46, fontWeight: 700, marginTop: 20 }}>Lean A–Z · letter {LETTER} · link in bio</div></RiseIn>
          </AbsoluteFill>
        </Sequence>
      )}

      <div style={{ position: "absolute", bottom: 40, width: "100%", display: "flex", justifyContent: "center" }}>
        <ActingGuide size={330} expr={frame < swap ? "concerned" : "smile"} hops={[swap, endAt]} fromX={0} />
      </div>
      <BrandMark />
    </AbsoluteFill>
  );
};

// ---------- thumbnail (1280x720) ----------
export const PokaYokeThumb: React.FC = () => (
  <AbsoluteFill style={{ background: `radial-gradient(circle at 75% 40%, #12304a 0%, ${theme.colors.bg} 65%)` }}>
    <div style={{ position: "absolute", left: 70, top: 70, display: "flex", flexDirection: "column", gap: 10 }}>
      <div style={{ display: "flex", alignItems: "center", gap: 22 }}>
        <div style={{ width: 150, height: 150, borderRadius: 28, background: theme.colors.accent, color: theme.colors.bg, fontFamily: theme.font.heading, fontSize: 120, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center" }}>{LETTER}</div>
        <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 34, fontWeight: 700, letterSpacing: 5 }}>LEAN<br />A–Z</div>
      </div>
      <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 124, fontWeight: 800, lineHeight: 1, marginTop: 24, textShadow: "0 6px 0 #000a" }}>POKA YOKE</div>
      <div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.heading, fontSize: 46, fontWeight: 600 }}>Make mistakes impossible</div>
      <div style={{ marginTop: 26, alignSelf: "flex-start", background: theme.colors.good, color: theme.colors.bg, fontFamily: theme.font.heading, fontSize: 52, fontWeight: 800, borderRadius: 18, padding: "10px 26px", transform: "rotate(-2deg)" }}>94% fewer defects</div>
    </div>
    <div style={{ position: "absolute", right: 30, bottom: -40 }}>
      <Character size={480} gender="f" outfit={theme.colors.accent} hairColor="#3a2416" expr="smile" pose="pointing" top="blazer" />
    </div>
  </AbsoluteFill>
);

// ---------- one-page cheat sheet (A4 portrait, 1240x1754; render --scale=2) ----------
export const PokaYokeCheatSheet: React.FC = () => {
  const r = POLISH.recap!;
  return (
    <AbsoluteFill style={{ background: theme.colors.bg, padding: "56px 56px 40px", fontFamily: theme.font.body, color: theme.colors.text }}>
      <div style={{ display: "flex", alignItems: "center", gap: 22 }}>
        <div style={{ width: 92, height: 92, borderRadius: 18, background: theme.colors.accent, color: theme.colors.bg, fontFamily: theme.font.heading, fontSize: 70, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center" }}>{LETTER}</div>
        <div style={{ flex: 1 }}>
          <div style={{ color: theme.colors.accent, fontSize: 18, fontWeight: 700, letterSpacing: 4 }}>{theme.brand.fullName} · LEAN A–Z CHEAT SHEET</div>
          <div style={{ fontFamily: theme.font.heading, fontSize: 56, fontWeight: 700, lineHeight: 1.1 }}>{TEXT.title}</div>
          <div style={{ color: theme.colors.textDim, fontSize: 22 }}>{TEXT.subtitle}</div>
        </div>
      </div>
      <div style={{ height: 2, background: theme.colors.panelBorder, margin: "26px 0" }} />
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 14, flex: 1 }}>
        {DATA.pages.map((p) => (
          <div key={p.key} style={{ background: theme.colors.panel, border: `1.5px solid ${theme.colors.panelBorder}`, borderRadius: 12, padding: "12px 14px" }}>
            <div style={{ display: "flex", gap: 8, alignItems: "baseline" }}>
              <div style={{ color: theme.colors.accent, fontSize: 14, fontWeight: 700 }}>{String(p.num).padStart(2, "0")}</div>
              <div style={{ fontFamily: theme.font.heading, fontSize: 18, fontWeight: 700, lineHeight: 1.2 }}>{p.title}</div>
            </div>
            <div style={{ marginTop: 6, display: "flex", flexDirection: "column", gap: 3 }}>
              {p.bullets.map((b, i) => (
                <div key={i} style={{ fontSize: 13.5, lineHeight: 1.3, color: "#d6deea" }}>
                  <span style={{ color: theme.colors.accent }}>{"▸ "}</span>{b}
                </div>
              ))}
            </div>
            <div style={{ marginTop: 8, borderLeft: `3px solid ${theme.colors.accent2}`, paddingLeft: 8, fontSize: 13, lineHeight: 1.35, color: "#a9c7e8" }}>
              {p.example}
            </div>
          </div>
        ))}
      </div>
      <div style={{ display: "flex", gap: 14, marginTop: 18 }}>
        <div style={{ flex: 2, background: `${theme.colors.accent}14`, border: `1.5px solid ${theme.colors.accent}`, borderRadius: 12, padding: "14px 18px" }}>
          <div style={{ color: theme.colors.accent, fontSize: 14, fontWeight: 700, letterSpacing: 3 }}>REMEMBER</div>
          {r.takeaways.map((t, i) => <div key={i} style={{ fontSize: 18, marginTop: 4 }}>{i + 1}. {t.text}</div>)}
        </div>
        <div style={{ flex: 1, background: `${theme.colors.accent2}14`, border: `1.5px solid ${theme.colors.accent2}`, borderRadius: 12, padding: "14px 18px" }}>
          <div style={{ color: theme.colors.accent2, fontSize: 14, fontWeight: 700, letterSpacing: 3 }}>THIS WEEK</div>
          <div style={{ fontSize: 17, marginTop: 4, lineHeight: 1.35 }}>{r.action.text}</div>
        </div>
      </div>
      <div style={{ marginTop: 14, display: "flex", justifyContent: "space-between", color: theme.colors.textDim, fontSize: 14 }}>
        <div>{theme.brand.fullName}</div>
        <div>Next: {r.next.letter} · {r.next.title}</div>
      </div>
    </AbsoluteFill>
  );
};

