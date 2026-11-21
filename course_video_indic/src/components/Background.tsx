import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { theme } from "../theme";

// Deterministic pseudo-random so particles are stable across renders.
const rand = (seed: number) => {
  const x = Math.sin(seed * 999.13) * 43758.5453;
  return x - Math.floor(x);
};

const PARTICLES = Array.from({ length: 12 }, (_, i) => ({
  x: rand(i) * 1920,
  baseY: rand(i + 50) * 1080,
  r: 1.5 + rand(i + 100) * 2.5,
  speed: 0.2 + rand(i + 150) * 0.5,
  drift: rand(i + 200) * 40,
}));

export const Background: React.FC = () => {
  const frame = useCurrentFrame();
  const grid = (frame * 0.15) % 60;

  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at 50% 0%, ${theme.colors.bgGradientTop} 0%, ${theme.colors.bgGradientBottom} 70%)`,
      }}
    >
      <AbsoluteFill
        style={{
          backgroundImage: `linear-gradient(${theme.colors.panelBorder}55 1px, transparent 1px), linear-gradient(90deg, ${theme.colors.panelBorder}55 1px, transparent 1px)`,
          backgroundSize: "60px 60px",
          backgroundPosition: `${grid}px ${grid}px`,
          maskImage: "radial-gradient(ellipse at 50% 40%, black 20%, transparent 70%)",
          opacity: 0.22,
        }}
      />
      {/* floating particles */}
      <svg width={1920} height={1080} style={{ position: "absolute" }}>
        {PARTICLES.map((p, i) => {
          const y = (p.baseY - frame * p.speed) % 1080;
          const yy = y < 0 ? y + 1080 : y;
          const x = p.x + Math.sin(frame / 60 + i) * p.drift;
          const op = 0.06 + 0.1 * (0.5 + 0.5 * Math.sin(frame / 30 + i));
          return <circle key={i} cx={x} cy={yy} r={p.r * 0.8} fill={theme.colors.accent} opacity={op} />;
        })}
      </svg>
      <AbsoluteFill
        style={{
          background: `radial-gradient(circle at 50% -10%, ${theme.colors.accent}12, transparent 55%)`,
        }}
      />
    </AbsoluteFill>
  );
};
