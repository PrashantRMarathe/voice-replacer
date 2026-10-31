import React from "react";
import { Composition, Still } from "remotion";
import { EightWastes, EIGHT_WASTES_DURATION } from "./lessons/EightWastes";
import { FullEightWastes, FULL_DURATION } from "./lessons/full/FullEightWastes";
import { CharacterSample, CHARACTER_SAMPLE_DURATION } from "./lessons/CharacterSample";
import { ZeroDefects, ZERO_DEFECTS_DURATION } from "./lessons/zd/ZeroDefects";
import { Yamazumi, YAMAZUMI_DURATION } from "./lessons/yz/Yamazumi";
import { XMatrix, X_MATRIX_DURATION } from "./lessons/xm/XMatrix";
import { UniformProduction, UNIFORM_PRODUCTION_DURATION } from "./lessons/up/UniformProduction";
import { ValueStreamMapping, VALUE_STREAM_MAPPING_DURATION } from "./lessons/vs/ValueStreamMapping";
import { WhyWhy, WHY_WHY_DURATION } from "./lessons/ww/WhyWhy";
import { MudaMuraMuri, MUDA_MURA_MURI_DURATION } from "./lessons/mm/MudaMuraMuri";
import { NextInspection, NEXT_INSPECTION_DURATION } from "./lessons/ni/NextInspection";
import { OnePointLesson, ONE_POINT_LESSON_DURATION } from "./lessons/op/OnePointLesson";
import { PokaYoke, POKA_YOKE_DURATION } from "./lessons/pk/PokaYoke";
import { PokaYokeShort, PokaYokeThumb, PokaYokeCheatSheet, POKA_YOKE_SHORT_DURATION } from "./lessons/pk/PokaYokeExtras";
import { QRQC, QRQC_DURATION } from "./lessons/qr/QRQC";
import { RootCauseAnalysis, ROOT_CAUSE_ANALYSIS_DURATION } from "./lessons/rc/RootCauseAnalysis";
import { SkillMatrix, SKILL_MATRIX_DURATION } from "./lessons/sk/SkillMatrix";
import { TaktTime, TAKT_TIME_DURATION } from "./lessons/tt/TaktTime";
import { A3ProblemSolving, A3_PROBLEM_SOLVING_DURATION } from "./lessons/a3/A3ProblemSolving";
import { BurnDownChart, BURN_DOWN_CHART_DURATION } from "./lessons/bd/BurnDownChart";
import { CycleTimeStudy, CYCLE_TIME_STUDY_DURATION } from "./lessons/ct/CycleTimeStudy";
import { DesignThinking, DESIGN_THINKING_DURATION } from "./lessons/dt/DesignThinking";
import { EliminationOfWaste, ELIMINATION_OF_WASTE_DURATION } from "./lessons/ew/EliminationOfWaste";
import { FMEA, FMEA_DURATION } from "./lessons/fm/FMEA";
import { Gemba, GEMBA_DURATION } from "./lessons/gb/Gemba";
import { Hancho, HANCHO_DURATION } from "./lessons/hc/Hancho";
import { Ishikawa, ISHIKAWA_DURATION } from "./lessons/ik/Ishikawa";
import { Jidoka, JIDOKA_DURATION } from "./lessons/jd/Jidoka";
import { Kaizen, KAIZEN_DURATION } from "./lessons/kz/Kaizen";
import { LowCostAutomation, LOW_COST_AUTOMATION_DURATION } from "./lessons/lc/LowCostAutomation";
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
      <Composition
        id="ZeroDefects"
        component={ZeroDefects}
        durationInFrames={ZERO_DEFECTS_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsDub"
        component={ZeroDefects}
        durationInFrames={ZERO_DEFECTS_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="Yamazumi"
        component={Yamazumi}
        durationInFrames={YAMAZUMI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiDub"
        component={Yamazumi}
        durationInFrames={YAMAZUMI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrix"
        component={XMatrix}
        durationInFrames={X_MATRIX_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixDub"
        component={XMatrix}
        durationInFrames={X_MATRIX_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProduction"
        component={UniformProduction}
        durationInFrames={UNIFORM_PRODUCTION_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionDub"
        component={UniformProduction}
        durationInFrames={UNIFORM_PRODUCTION_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMapping"
        component={ValueStreamMapping}
        durationInFrames={VALUE_STREAM_MAPPING_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingDub"
        component={ValueStreamMapping}
        durationInFrames={VALUE_STREAM_MAPPING_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhy"
        component={WhyWhy}
        durationInFrames={WHY_WHY_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyDub"
        component={WhyWhy}
        durationInFrames={WHY_WHY_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuri"
        component={MudaMuraMuri}
        durationInFrames={MUDA_MURA_MURI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriDub"
        component={MudaMuraMuri}
        durationInFrames={MUDA_MURA_MURI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspection"
        component={NextInspection}
        durationInFrames={NEXT_INSPECTION_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionDub"
        component={NextInspection}
        durationInFrames={NEXT_INSPECTION_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLesson"
        component={OnePointLesson}
        durationInFrames={ONE_POINT_LESSON_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonDub"
        component={OnePointLesson}
        durationInFrames={ONE_POINT_LESSON_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYoke"
        component={PokaYoke}
        durationInFrames={POKA_YOKE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeDub"
        component={PokaYoke}
        durationInFrames={POKA_YOKE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      {/* promo pieces */}
      <Composition
        id="PokaYokeShort"
        component={PokaYokeShort}
        durationInFrames={POKA_YOKE_SHORT_DURATION}
        fps={fps}
        width={1080}
        height={1920}
      />
      <Still id="PokaYokeThumb" component={PokaYokeThumb} width={1280} height={720} />
      <Still id="PokaYokeCheatSheet" component={PokaYokeCheatSheet} width={1240} height={1754} />
      <Composition
        id="QRQC"
        component={QRQC}
        durationInFrames={QRQC_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QRQCDub"
        component={QRQC}
        durationInFrames={QRQC_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysis"
        component={RootCauseAnalysis}
        durationInFrames={ROOT_CAUSE_ANALYSIS_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisDub"
        component={RootCauseAnalysis}
        durationInFrames={ROOT_CAUSE_ANALYSIS_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrix"
        component={SkillMatrix}
        durationInFrames={SKILL_MATRIX_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixDub"
        component={SkillMatrix}
        durationInFrames={SKILL_MATRIX_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTime"
        component={TaktTime}
        durationInFrames={TAKT_TIME_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeDub"
        component={TaktTime}
        durationInFrames={TAKT_TIME_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
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
      {/* A to L page lessons */}
      <Composition
        id="A3ProblemSolving"
        component={A3ProblemSolving}
        durationInFrames={A3_PROBLEM_SOLVING_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingDub"
        component={A3ProblemSolving}
        durationInFrames={A3_PROBLEM_SOLVING_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChart"
        component={BurnDownChart}
        durationInFrames={BURN_DOWN_CHART_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartDub"
        component={BurnDownChart}
        durationInFrames={BURN_DOWN_CHART_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudy"
        component={CycleTimeStudy}
        durationInFrames={CYCLE_TIME_STUDY_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyDub"
        component={CycleTimeStudy}
        durationInFrames={CYCLE_TIME_STUDY_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinking"
        component={DesignThinking}
        durationInFrames={DESIGN_THINKING_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingDub"
        component={DesignThinking}
        durationInFrames={DESIGN_THINKING_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWaste"
        component={EliminationOfWaste}
        durationInFrames={ELIMINATION_OF_WASTE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteDub"
        component={EliminationOfWaste}
        durationInFrames={ELIMINATION_OF_WASTE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEA"
        component={FMEA}
        durationInFrames={FMEA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEADub"
        component={FMEA}
        durationInFrames={FMEA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="Gemba"
        component={Gemba}
        durationInFrames={GEMBA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaDub"
        component={Gemba}
        durationInFrames={GEMBA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="Hancho"
        component={Hancho}
        durationInFrames={HANCHO_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoDub"
        component={Hancho}
        durationInFrames={HANCHO_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="Ishikawa"
        component={Ishikawa}
        durationInFrames={ISHIKAWA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaDub"
        component={Ishikawa}
        durationInFrames={ISHIKAWA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="Jidoka"
        component={Jidoka}
        durationInFrames={JIDOKA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaDub"
        component={Jidoka}
        durationInFrames={JIDOKA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="Kaizen"
        component={Kaizen}
        durationInFrames={KAIZEN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenDub"
        component={Kaizen}
        durationInFrames={KAIZEN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomation"
        component={LowCostAutomation}
        durationInFrames={LOW_COST_AUTOMATION_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationDub"
        component={LowCostAutomation}
        durationInFrames={LOW_COST_AUTOMATION_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
    </>
  );
};
