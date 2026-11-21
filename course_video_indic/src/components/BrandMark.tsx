import React from "react";
import { AbsoluteFill } from "remotion";
import { theme } from "../theme";

// Persistent brand mark shown in the TOP-LEFT corner of every lesson.
// Render it once at the top level of a composition (above the scenes) so it
// stays on screen the whole video. Edit the brand text in src/theme.ts.
export const BrandMark: React.FC<{ corner?: "left" | "right" }> = ({ corner = "left" }) => {
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div
        style={{
          position: "absolute",
          top: 42,
          [corner === "left" ? "left" : "right"]: 54,
          display: "flex",
          alignItems: "center",
          gap: 12,
          opacity: 0.9,
        }}
      >
        <div
          style={{
            background: theme.colors.accent,
            color: theme.colors.bg,
            fontFamily: theme.font.heading,
            fontWeight: 700,
            fontSize: 24,
            letterSpacing: 0,
            padding: "6px 12px",
            borderRadius: 10,
            boxShadow: `0 0 18px ${theme.colors.accent}55`,
          }}
        >
          {theme.brand.shortName}
        </div>
        <div
          style={{
            color: theme.colors.textDim,
            fontFamily: theme.font.body,
            fontWeight: 600,
            fontSize: 20,
            letterSpacing: 0,
          }}
        >
          {theme.brand.fullName}
        </div>
      </div>
    </AbsoluteFill>
  );
};
