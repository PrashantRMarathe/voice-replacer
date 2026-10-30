import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { theme } from "../theme";
import { toLines, Word } from "../lessons/plan";

export type { Word };

// Shows the ACTIVE caption line (whole sentence, or half of a long one) — no
// per-word highlight, which desyncs on approximate timings. Line splitting
// lives in plan.ts so the burned captions and the .srt export match exactly.
export const Captions: React.FC<{ words: Word[] }> = ({ words }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  const sentences = React.useMemo(() => toLines(words), [words]);
  let active = -1;
  for (let i = 0; i < sentences.length; i++) {
    if (t >= sentences[i].s) active = i;
    else break;
  }
  if (active < 0) return null;
  const line = sentences[active].text;

  return (
    <div
      style={{
        position: "absolute",
        bottom: 70,
        left: 0,
        right: 0,
        display: "flex",
        justifyContent: "center",
        padding: "0 120px",
      }}
    >
      <div
        style={{
          background: "rgba(7,10,18,0.72)",
          borderRadius: 14,
          padding: "12px 26px",
          backdropFilter: "blur(4px)",
          border: `1px solid ${theme.colors.panelBorder}`,
          maxWidth: 1300,
          textAlign: "center",
          fontFamily: theme.font.body,
          fontSize: 30,
          fontWeight: 500,
          lineHeight: 1.35,
          color: theme.colors.text,
        }}
      >
        {line}
      </div>
    </div>
  );
};
