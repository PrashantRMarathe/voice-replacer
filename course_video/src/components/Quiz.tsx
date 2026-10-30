import React from "react";
import { Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { RiseIn } from "./ui";
import { Scene } from "../scenes/Scene";
import { theme } from "../theme";
import { QUIZ_LEAD, QUIZ_HOLD, DEFAULT_THINK } from "../lessons/plan";
import { usePolish, Sfx, CountdownRing, ActingGuide } from "../lessons/shared/polish";

export type QuizData = {
  num: number;
  question: string;
  options: string[];
  correct: number;       // index of the correct option
  explanation: string;
  think?: number;        // seconds to think before the answer reveals
};

const LETTERS = ["A", "B", "C", "D"];

// A quiz scene: question + options appear, a countdown gives time to think,
// then the correct option is highlighted and the explanation is shown.
export const QuizScene: React.FC<{ data: QuizData }> = ({ data }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const think = data.think ?? DEFAULT_THINK;
  const revealT = QUIZ_LEAD + think;            // seconds when the answer appears
  const revealFrame = Math.round(revealT * fps);
  const revealed = t >= revealT;
  const countdown = Math.max(0, Math.ceil(revealT - t));
  const { polish } = usePolish();
  const thinkFrom = Math.round(QUIZ_LEAD * fps);

  return (
    <Scene>
      <div style={{ width: 1500, display: "flex", flexDirection: "column", alignItems: "center" }}>
        {/* badge */}
        <RiseIn>
          <div style={{ color: theme.colors.bg, background: theme.colors.accent, fontFamily: theme.font.body, fontSize: 22, fontWeight: 700, letterSpacing: 2, padding: "6px 18px", borderRadius: 20 }}>
            QUICK CHECK #{data.num}
          </div>
        </RiseIn>
        {/* question */}
        <RiseIn delay={6}>
          <div style={{ color: theme.colors.text, fontFamily: theme.font.heading, fontSize: 48, fontWeight: 600, textAlign: "center", marginTop: 20, maxWidth: 1300 }}>
            {data.question}
          </div>
        </RiseIn>

        {/* options */}
        <div style={{ display: "flex", flexDirection: "column", gap: 16, marginTop: 34, width: 1100 }}>
          {data.options.map((opt, i) => {
            const isCorrect = i === data.correct;
            const color = revealed && isCorrect ? theme.colors.good : theme.colors.panelBorder;
            const dim = revealed && !isCorrect ? 0.4 : 1;
            return (
              <RiseIn key={i} delay={12 + i * 6}>
                <div style={{
                  display: "flex", alignItems: "center", gap: 18,
                  background: theme.colors.panel,
                  border: `2px solid ${color}`,
                  borderRadius: 14, padding: "18px 24px", opacity: dim,
                  boxShadow: revealed && isCorrect ? `0 0 26px ${theme.colors.good}55` : "none",
                }}>
                  <div style={{ width: 40, height: 40, borderRadius: 10, background: revealed && isCorrect ? theme.colors.good : theme.colors.panelBorder, color: theme.colors.bg, fontFamily: theme.font.heading, fontWeight: 700, fontSize: 22, display: "flex", alignItems: "center", justifyContent: "center" }}>
                    {revealed && isCorrect ? "✓" : LETTERS[i]}
                  </div>
                  <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 28 }}>{opt}</div>
                </div>
              </RiseIn>
            );
          })}
        </div>

        {/* countdown OR explanation */}
        <div style={{ marginTop: 28, minHeight: 90 }}>
          {!revealed ? (
            polish.bigQuiz ? <CountdownRing start={thinkFrom} end={revealFrame} /> : (
            <div style={{ color: theme.colors.accentSoft, fontFamily: theme.font.body, fontSize: 30, fontWeight: 600, textAlign: "center" }}>
              Think{"…"} {countdown}
            </div>)
          ) : (
            <Sequence from={revealFrame} layout="none">
              <RiseIn>
                <div style={{ maxWidth: 1200, background: `${theme.colors.good}14`, border: `1.5px solid ${theme.colors.good}`, borderRadius: 16, padding: "18px 26px", display: "flex", gap: 16 }}>
                  <div style={{ color: theme.colors.good, fontFamily: theme.font.body, fontSize: 20, fontWeight: 700, letterSpacing: 2, minWidth: 92 }}>ANSWER</div>
                  <div style={{ color: theme.colors.text, fontFamily: theme.font.body, fontSize: 26, lineHeight: 1.4 }}>{data.explanation}</div>
                </div>
              </RiseIn>
            </Sequence>
          )}
        </div>
      </div>
      {polish.acting && (
        <div style={{ position: "absolute", right: 50, bottom: 24 }}>
          <ActingGuide size={230} expr={revealed ? "smile" : "surprised"} facing="left" hops={[revealFrame]} delay={14} />
        </div>
      )}
      <Sfx name="sting" at={0} volume={0.4} />
      {Array.from({ length: Math.max(0, Math.floor(think)) }, (_, i) => (
        <Sfx key={i} name="tick" at={thinkFrom + i * fps} volume={0.25} />
      ))}
      <Sfx name="reveal" at={revealFrame} volume={0.4} />
    </Scene>
  );
};

// A silent quiz lasts: appear + think + hold-on-answer. (Narrated quizzes are
// timed by planLesson in lessons/plan.ts.)
export const quizDuration = (fps: number, think = DEFAULT_THINK) => Math.round((QUIZ_LEAD + think + QUIZ_HOLD) * fps);
