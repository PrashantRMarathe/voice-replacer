import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "../theme";

export type Word = { w: string; s: number; e: number };

// Animated subtitle bar fixed near the bottom. Shows a sliding window of words
// and highlights the one currently being spoken (karaoke style). `words` carry
// start/end seconds relative to the scene's own audio.
export const Captions: React.FC<{ words: Word[]; windowSize?: number }> = ({
  words,
  windowSize = 7,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  // find the active word index
  let active = -1;
  for (let i = 0; i < words.length; i++) {
    if (t >= words[i].s) active = i;
    else break;
  }
  if (active < 0) return null;

  // show a window of words centered on the active one
  const half = Math.floor(windowSize / 2);
  const start = Math.max(0, Math.min(active - half, words.length - windowSize));
  const shown = words.slice(start, start + windowSize);

  return (
    <div
      style={{
        position: "absolute",
        bottom: 70,
        left: 0,
        right: 0,
        display: "flex",
        justifyContent: "center",
        gap: 12,
        flexWrap: "wrap",
        padding: "0 120px",
      }}
    >
      <div
        style={{
          background: "rgba(7,10,18,0.72)",
          borderRadius: 16,
          padding: "14px 28px",
          display: "flex",
          gap: 12,
          flexWrap: "wrap",
          justifyContent: "center",
          backdropFilter: "blur(4px)",
          border: `1px solid ${theme.colors.panelBorder}`,
          maxWidth: 1400,
        }}
      >
        {shown.map((word, i) => {
          const idx = start + i;
          const isActive = idx === active;
          return (
            <span
              key={idx}
              style={{
                fontFamily: theme.font.body,
                fontSize: 36,
                fontWeight: isActive ? 700 : 500,
                color: isActive ? theme.colors.accentSoft : theme.colors.textDim,
                textShadow: isActive ? `0 0 16px ${theme.colors.accent}88` : "none",
                transform: isActive ? "scale(1.06)" : "scale(1)",
                transition: "none",
              }}
            >
              {word.w}
            </span>
          );
        })}
      </div>
    </div>
  );
};
