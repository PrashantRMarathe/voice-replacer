import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "../theme";

// Spring rise + subtle scale pop. `delay` staggers multiple items.
export const RiseIn: React.FC<{
  delay?: number;
  children: React.ReactNode;
  style?: React.CSSProperties;
}> = ({ delay = 0, children, style }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 16, mass: 0.7 } });
  const y = interpolate(s, [0, 1], [50, 0]);
  const scale = interpolate(s, [0, 1], [0.92, 1]);
  return (
    <div style={{ opacity: s, transform: `translateY(${y}px) scale(${scale})`, ...style }}>
      {children}
    </div>
  );
};

type IconComp = React.FC<{ color: string; size?: number; progress?: number }>;

// Glowing numbered card with an animated line-icon that draws itself in, plus
// a soft pulsing glow so the scene always feels alive.
export const GlowCard: React.FC<{
  index?: string;
  title: string;
  desc?: string;
  Icon?: IconComp;
  accent?: string;
  delay?: number;
}> = ({ index, title, desc, Icon, accent = theme.colors.accent, delay = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 16 } });
  const iconProgress = interpolate(frame - delay, [6, 26], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const pulse = 0.5 + 0.5 * Math.sin((frame - delay) / 14);
  const glow = interpolate(pulse, [0, 1], [0.2, 0.45]);

  return (
    <RiseIn delay={delay}>
      <div
        style={{
          background: theme.colors.panel,
          border: `1.5px solid ${accent}`,
          borderRadius: 20,
          padding: "26px 28px",
          boxShadow: `0 0 ${18 + 18 * pulse}px ${accent}${Math.round(glow * 255).toString(16).padStart(2, "0")}, inset 0 0 20px ${accent}11`,
          minWidth: 300,
          display: "flex",
          flexDirection: "column",
          gap: 14,
        }}
      >
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          {index && (
            <div style={{ color: accent, fontFamily: theme.font.body, fontSize: 22, fontWeight: 700, letterSpacing: 0 }}>
              {index}
            </div>
          )}
          {Icon && (
            <div style={{ opacity: s }}>
              <Icon color={accent} size={52} progress={iconProgress} />
            </div>
          )}
        </div>
        <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 32, fontWeight: 600 }}>
          {title}
        </div>
        {desc && (
          <div style={{ color: theme.colors.textDim, fontFamily: theme.font.body, fontSize: 21, lineHeight: 1.4 }}>
            {desc}
          </div>
        )}
      </div>
    </RiseIn>
  );
};
