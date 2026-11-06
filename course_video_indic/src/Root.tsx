import React from "react";
import { Composition } from "remotion";
import { A3ProblemSolvingHi, A3_PROBLEM_SOLVING_HI_DURATION } from "./lessons/a3_hi/A3ProblemSolvingHi";
import { BurnDownChartHi, BURN_DOWN_CHART_HI_DURATION } from "./lessons/bd_hi/BurnDownChartHi";
import { CycleTimeStudyHi, CYCLE_TIME_STUDY_HI_DURATION } from "./lessons/ct_hi/CycleTimeStudyHi";
import { DesignThinkingHi, DESIGN_THINKING_HI_DURATION } from "./lessons/dt_hi/DesignThinkingHi";
import { EliminationOfWasteHi, ELIMINATION_OF_WASTE_HI_DURATION } from "./lessons/ew_hi/EliminationOfWasteHi";
import { FMEAHi, FMEA_HI_DURATION } from "./lessons/fm_hi/FMEAHi";
import { GembaHi, GEMBA_HI_DURATION } from "./lessons/gb_hi/GembaHi";
import { HanchoHi, HANCHO_HI_DURATION } from "./lessons/hc_hi/HanchoHi";
import { IshikawaHi, ISHIKAWA_HI_DURATION } from "./lessons/ik_hi/IshikawaHi";
import { JidokaHi, JIDOKA_HI_DURATION } from "./lessons/jd_hi/JidokaHi";
import { KaizenHi, KAIZEN_HI_DURATION } from "./lessons/kz_hi/KaizenHi";
import { LowCostAutomationHi, LOW_COST_AUTOMATION_HI_DURATION } from "./lessons/lc_hi/LowCostAutomationHi";
import { MudaMuraMuriHi, MUDA_MURA_MURI_HI_DURATION } from "./lessons/mm_hi/MudaMuraMuriHi";
import { NextInspectionHi, NEXT_INSPECTION_HI_DURATION } from "./lessons/ni_hi/NextInspectionHi";
import { OnePointLessonHi, ONE_POINT_LESSON_HI_DURATION } from "./lessons/op_hi/OnePointLessonHi";
import { PokaYokeHi, POKA_YOKE_HI_DURATION } from "./lessons/pk_hi/PokaYokeHi";
import { QrqcHi, QRQC_HI_DURATION } from "./lessons/qr_hi/QrqcHi";
import { RootCauseAnalysisHi, ROOT_CAUSE_ANALYSIS_HI_DURATION } from "./lessons/rc_hi/RootCauseAnalysisHi";
import { SkillMatrixHi, SKILL_MATRIX_HI_DURATION } from "./lessons/sk_hi/SkillMatrixHi";
import { TaktTimeHi, TAKT_TIME_HI_DURATION } from "./lessons/tt_hi/TaktTimeHi";
import { UniformProductionHi, UNIFORM_PRODUCTION_HI_DURATION } from "./lessons/up_hi/UniformProductionHi";
import { ValueStreamMappingHi, VALUE_STREAM_MAPPING_HI_DURATION } from "./lessons/vs_hi/ValueStreamMappingHi";
import { WhyWhyHi, WHY_WHY_HI_DURATION } from "./lessons/ww_hi/WhyWhyHi";
import { XMatrixHi, X_MATRIX_HI_DURATION } from "./lessons/xm_hi/XMatrixHi";
import { YamazumiHi, YAMAZUMI_HI_DURATION } from "./lessons/yz_hi/YamazumiHi";
import { ZeroDefectsHi, ZERO_DEFECTS_HI_DURATION } from "./lessons/zd_hi/ZeroDefectsHi";
import { PokaYokeMr, POKA_YOKE_MR_DURATION } from "./lessons/pk_mr/PokaYokeMr";
import { QrqcMr, QRQC_MR_DURATION } from "./lessons/qr_mr/QrqcMr";
import { A3ProblemSolvingTe, A3_PROBLEM_SOLVING_TE_DURATION } from "./lessons/a3_te/A3ProblemSolvingTe";
import { A3ProblemSolvingTa, A3_PROBLEM_SOLVING_TA_DURATION } from "./lessons/a3_ta/A3ProblemSolvingTa";
import { BurnDownChartTa, BURN_DOWN_CHART_TA_DURATION } from "./lessons/bd_ta/BurnDownChartTa";
import { KaizenTa, KAIZEN_TA_DURATION } from "./lessons/kz_ta/KaizenTa";
import { CycleTimeStudyTa, CYCLE_TIME_STUDY_TA_DURATION } from "./lessons/ct_ta/CycleTimeStudyTa";
import { DesignThinkingTa, DESIGN_THINKING_TA_DURATION } from "./lessons/dt_ta/DesignThinkingTa";
import { EliminationOfWasteTa, ELIMINATION_OF_WASTE_TA_DURATION } from "./lessons/ew_ta/EliminationOfWasteTa";
import { FMEATa, FMEA_TA_DURATION } from "./lessons/fm_ta/FMEATa";
import { GembaTa, GEMBA_TA_DURATION } from "./lessons/gb_ta/GembaTa";
import { HanchoTa, HANCHO_TA_DURATION } from "./lessons/hc_ta/HanchoTa";
import { IshikawaTa, ISHIKAWA_TA_DURATION } from "./lessons/ik_ta/IshikawaTa";
import { JidokaTa, JIDOKA_TA_DURATION } from "./lessons/jd_ta/JidokaTa";
import { LowCostAutomationTa, LOW_COST_AUTOMATION_TA_DURATION } from "./lessons/lc_ta/LowCostAutomationTa";
import { MudaMuraMuriTa, MUDA_MURA_MURI_TA_DURATION } from "./lessons/mm_ta/MudaMuraMuriTa";
import { NextInspectionTa, NEXT_INSPECTION_TA_DURATION } from "./lessons/ni_ta/NextInspectionTa";
import { OnePointLessonTa, ONE_POINT_LESSON_TA_DURATION } from "./lessons/op_ta/OnePointLessonTa";
import { PokaYokeTa, POKA_YOKE_TA_DURATION } from "./lessons/pk_ta/PokaYokeTa";
import { QrqcTa, QRQC_TA_DURATION } from "./lessons/qr_ta/QrqcTa";
import { RootCauseAnalysisTa, ROOT_CAUSE_ANALYSIS_TA_DURATION } from "./lessons/rc_ta/RootCauseAnalysisTa";
import { SkillMatrixTa, SKILL_MATRIX_TA_DURATION } from "./lessons/sk_ta/SkillMatrixTa";
import { TaktTimeTa, TAKT_TIME_TA_DURATION } from "./lessons/tt_ta/TaktTimeTa";
import { UniformProductionTa, UNIFORM_PRODUCTION_TA_DURATION } from "./lessons/up_ta/UniformProductionTa";
import { ValueStreamMappingTa, VALUE_STREAM_MAPPING_TA_DURATION } from "./lessons/vs_ta/ValueStreamMappingTa";
import { WhyWhyTa, WHY_WHY_TA_DURATION } from "./lessons/ww_ta/WhyWhyTa";
import { XMatrixTa, X_MATRIX_TA_DURATION } from "./lessons/xm_ta/XMatrixTa";
import { YamazumiTa, YAMAZUMI_TA_DURATION } from "./lessons/yz_ta/YamazumiTa";
import { ZeroDefectsTa, ZERO_DEFECTS_TA_DURATION } from "./lessons/zd_ta/ZeroDefectsTa";
import { BurnDownChartTe, BURN_DOWN_CHART_TE_DURATION } from "./lessons/bd_te/BurnDownChartTe";
import { CycleTimeStudyTe, CYCLE_TIME_STUDY_TE_DURATION } from "./lessons/ct_te/CycleTimeStudyTe";
import { DesignThinkingTe, DESIGN_THINKING_TE_DURATION } from "./lessons/dt_te/DesignThinkingTe";
import { EliminationOfWasteTe, ELIMINATION_OF_WASTE_TE_DURATION } from "./lessons/ew_te/EliminationOfWasteTe";
import { FMEATe, FMEA_TE_DURATION } from "./lessons/fm_te/FMEATe";
import { GembaTe, GEMBA_TE_DURATION } from "./lessons/gb_te/GembaTe";
import { HanchoTe, HANCHO_TE_DURATION } from "./lessons/hc_te/HanchoTe";
import { IshikawaTe, ISHIKAWA_TE_DURATION } from "./lessons/ik_te/IshikawaTe";
import { JidokaTe, JIDOKA_TE_DURATION } from "./lessons/jd_te/JidokaTe";
import { KaizenTe, KAIZEN_TE_DURATION } from "./lessons/kz_te/KaizenTe";
import { LowCostAutomationTe, LOW_COST_AUTOMATION_TE_DURATION } from "./lessons/lc_te/LowCostAutomationTe";
import { MudaMuraMuriTe, MUDA_MURA_MURI_TE_DURATION } from "./lessons/mm_te/MudaMuraMuriTe";
import { NextInspectionTe, NEXT_INSPECTION_TE_DURATION } from "./lessons/ni_te/NextInspectionTe";
import { OnePointLessonTe, ONE_POINT_LESSON_TE_DURATION } from "./lessons/op_te/OnePointLessonTe";
import { PokaYokeTe, POKA_YOKE_TE_DURATION } from "./lessons/pk_te/PokaYokeTe";
import { QrqcTe, QRQC_TE_DURATION } from "./lessons/qr_te/QrqcTe";
import { RootCauseAnalysisTe, ROOT_CAUSE_ANALYSIS_TE_DURATION } from "./lessons/rc_te/RootCauseAnalysisTe";
import { SkillMatrixTe, SKILL_MATRIX_TE_DURATION } from "./lessons/sk_te/SkillMatrixTe";
import { TaktTimeTe, TAKT_TIME_TE_DURATION } from "./lessons/tt_te/TaktTimeTe";
import { UniformProductionTe, UNIFORM_PRODUCTION_TE_DURATION } from "./lessons/up_te/UniformProductionTe";
import { ValueStreamMappingTe, VALUE_STREAM_MAPPING_TE_DURATION } from "./lessons/vs_te/ValueStreamMappingTe";
import { WhyWhyTe, WHY_WHY_TE_DURATION } from "./lessons/ww_te/WhyWhyTe";
import { XMatrixTe, X_MATRIX_TE_DURATION } from "./lessons/xm_te/XMatrixTe";
import { YamazumiTe, YAMAZUMI_TE_DURATION } from "./lessons/yz_te/YamazumiTe";
import { ZeroDefectsTe, ZERO_DEFECTS_TE_DURATION } from "./lessons/zd_te/ZeroDefectsTe";
import { fps, width, height } from "./theme";

// Indian-language lessons only. Kept apart from course_video/ (the English
// course) so this work never touches the English pipeline.
// Generated by tools/gen_root.py: edit the list there.
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="A3ProblemSolvingHi"
        component={A3ProblemSolvingHi}
        durationInFrames={A3_PROBLEM_SOLVING_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingHiDub"
        component={A3ProblemSolvingHi}
        durationInFrames={A3_PROBLEM_SOLVING_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartHi"
        component={BurnDownChartHi}
        durationInFrames={BURN_DOWN_CHART_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartHiDub"
        component={BurnDownChartHi}
        durationInFrames={BURN_DOWN_CHART_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyHi"
        component={CycleTimeStudyHi}
        durationInFrames={CYCLE_TIME_STUDY_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyHiDub"
        component={CycleTimeStudyHi}
        durationInFrames={CYCLE_TIME_STUDY_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingHi"
        component={DesignThinkingHi}
        durationInFrames={DESIGN_THINKING_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingHiDub"
        component={DesignThinkingHi}
        durationInFrames={DESIGN_THINKING_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteHi"
        component={EliminationOfWasteHi}
        durationInFrames={ELIMINATION_OF_WASTE_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteHiDub"
        component={EliminationOfWasteHi}
        durationInFrames={ELIMINATION_OF_WASTE_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAHi"
        component={FMEAHi}
        durationInFrames={FMEA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAHiDub"
        component={FMEAHi}
        durationInFrames={FMEA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaHi"
        component={GembaHi}
        durationInFrames={GEMBA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaHiDub"
        component={GembaHi}
        durationInFrames={GEMBA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoHi"
        component={HanchoHi}
        durationInFrames={HANCHO_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoHiDub"
        component={HanchoHi}
        durationInFrames={HANCHO_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaHi"
        component={IshikawaHi}
        durationInFrames={ISHIKAWA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaHiDub"
        component={IshikawaHi}
        durationInFrames={ISHIKAWA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaHi"
        component={JidokaHi}
        durationInFrames={JIDOKA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaHiDub"
        component={JidokaHi}
        durationInFrames={JIDOKA_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenHi"
        component={KaizenHi}
        durationInFrames={KAIZEN_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenHiDub"
        component={KaizenHi}
        durationInFrames={KAIZEN_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationHi"
        component={LowCostAutomationHi}
        durationInFrames={LOW_COST_AUTOMATION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationHiDub"
        component={LowCostAutomationHi}
        durationInFrames={LOW_COST_AUTOMATION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriHi"
        component={MudaMuraMuriHi}
        durationInFrames={MUDA_MURA_MURI_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriHiDub"
        component={MudaMuraMuriHi}
        durationInFrames={MUDA_MURA_MURI_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionHi"
        component={NextInspectionHi}
        durationInFrames={NEXT_INSPECTION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionHiDub"
        component={NextInspectionHi}
        durationInFrames={NEXT_INSPECTION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonHi"
        component={OnePointLessonHi}
        durationInFrames={ONE_POINT_LESSON_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonHiDub"
        component={OnePointLessonHi}
        durationInFrames={ONE_POINT_LESSON_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeHi"
        component={PokaYokeHi}
        durationInFrames={POKA_YOKE_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeHiDub"
        component={PokaYokeHi}
        durationInFrames={POKA_YOKE_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcHi"
        component={QrqcHi}
        durationInFrames={QRQC_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcHiDub"
        component={QrqcHi}
        durationInFrames={QRQC_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisHi"
        component={RootCauseAnalysisHi}
        durationInFrames={ROOT_CAUSE_ANALYSIS_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisHiDub"
        component={RootCauseAnalysisHi}
        durationInFrames={ROOT_CAUSE_ANALYSIS_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixHi"
        component={SkillMatrixHi}
        durationInFrames={SKILL_MATRIX_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixHiDub"
        component={SkillMatrixHi}
        durationInFrames={SKILL_MATRIX_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeHi"
        component={TaktTimeHi}
        durationInFrames={TAKT_TIME_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeHiDub"
        component={TaktTimeHi}
        durationInFrames={TAKT_TIME_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionHi"
        component={UniformProductionHi}
        durationInFrames={UNIFORM_PRODUCTION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionHiDub"
        component={UniformProductionHi}
        durationInFrames={UNIFORM_PRODUCTION_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingHi"
        component={ValueStreamMappingHi}
        durationInFrames={VALUE_STREAM_MAPPING_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingHiDub"
        component={ValueStreamMappingHi}
        durationInFrames={VALUE_STREAM_MAPPING_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyHi"
        component={WhyWhyHi}
        durationInFrames={WHY_WHY_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyHiDub"
        component={WhyWhyHi}
        durationInFrames={WHY_WHY_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixHi"
        component={XMatrixHi}
        durationInFrames={X_MATRIX_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixHiDub"
        component={XMatrixHi}
        durationInFrames={X_MATRIX_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiHi"
        component={YamazumiHi}
        durationInFrames={YAMAZUMI_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiHiDub"
        component={YamazumiHi}
        durationInFrames={YAMAZUMI_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsHi"
        component={ZeroDefectsHi}
        durationInFrames={ZERO_DEFECTS_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsHiDub"
        component={ZeroDefectsHi}
        durationInFrames={ZERO_DEFECTS_HI_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeMr"
        component={PokaYokeMr}
        durationInFrames={POKA_YOKE_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeMrDub"
        component={PokaYokeMr}
        durationInFrames={POKA_YOKE_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcMr"
        component={QrqcMr}
        durationInFrames={QRQC_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcMrDub"
        component={QrqcMr}
        durationInFrames={QRQC_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingTe"
        component={A3ProblemSolvingTe}
        durationInFrames={A3_PROBLEM_SOLVING_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingTeDub"
        component={A3ProblemSolvingTe}
        durationInFrames={A3_PROBLEM_SOLVING_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingTa"
        component={A3ProblemSolvingTa}
        durationInFrames={A3_PROBLEM_SOLVING_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingTaDub"
        component={A3ProblemSolvingTa}
        durationInFrames={A3_PROBLEM_SOLVING_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartTa"
        component={BurnDownChartTa}
        durationInFrames={BURN_DOWN_CHART_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartTaDub"
        component={BurnDownChartTa}
        durationInFrames={BURN_DOWN_CHART_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenTa"
        component={KaizenTa}
        durationInFrames={KAIZEN_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenTaDub"
        component={KaizenTa}
        durationInFrames={KAIZEN_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyTa"
        component={CycleTimeStudyTa}
        durationInFrames={CYCLE_TIME_STUDY_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyTaDub"
        component={CycleTimeStudyTa}
        durationInFrames={CYCLE_TIME_STUDY_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingTa"
        component={DesignThinkingTa}
        durationInFrames={DESIGN_THINKING_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingTaDub"
        component={DesignThinkingTa}
        durationInFrames={DESIGN_THINKING_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteTa"
        component={EliminationOfWasteTa}
        durationInFrames={ELIMINATION_OF_WASTE_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteTaDub"
        component={EliminationOfWasteTa}
        durationInFrames={ELIMINATION_OF_WASTE_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEATa"
        component={FMEATa}
        durationInFrames={FMEA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEATaDub"
        component={FMEATa}
        durationInFrames={FMEA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaTa"
        component={GembaTa}
        durationInFrames={GEMBA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaTaDub"
        component={GembaTa}
        durationInFrames={GEMBA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoTa"
        component={HanchoTa}
        durationInFrames={HANCHO_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoTaDub"
        component={HanchoTa}
        durationInFrames={HANCHO_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaTa"
        component={IshikawaTa}
        durationInFrames={ISHIKAWA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaTaDub"
        component={IshikawaTa}
        durationInFrames={ISHIKAWA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaTa"
        component={JidokaTa}
        durationInFrames={JIDOKA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaTaDub"
        component={JidokaTa}
        durationInFrames={JIDOKA_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationTa"
        component={LowCostAutomationTa}
        durationInFrames={LOW_COST_AUTOMATION_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationTaDub"
        component={LowCostAutomationTa}
        durationInFrames={LOW_COST_AUTOMATION_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriTa"
        component={MudaMuraMuriTa}
        durationInFrames={MUDA_MURA_MURI_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriTaDub"
        component={MudaMuraMuriTa}
        durationInFrames={MUDA_MURA_MURI_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionTa"
        component={NextInspectionTa}
        durationInFrames={NEXT_INSPECTION_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionTaDub"
        component={NextInspectionTa}
        durationInFrames={NEXT_INSPECTION_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonTa"
        component={OnePointLessonTa}
        durationInFrames={ONE_POINT_LESSON_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonTaDub"
        component={OnePointLessonTa}
        durationInFrames={ONE_POINT_LESSON_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeTa"
        component={PokaYokeTa}
        durationInFrames={POKA_YOKE_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeTaDub"
        component={PokaYokeTa}
        durationInFrames={POKA_YOKE_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcTa"
        component={QrqcTa}
        durationInFrames={QRQC_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcTaDub"
        component={QrqcTa}
        durationInFrames={QRQC_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisTa"
        component={RootCauseAnalysisTa}
        durationInFrames={ROOT_CAUSE_ANALYSIS_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisTaDub"
        component={RootCauseAnalysisTa}
        durationInFrames={ROOT_CAUSE_ANALYSIS_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixTa"
        component={SkillMatrixTa}
        durationInFrames={SKILL_MATRIX_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixTaDub"
        component={SkillMatrixTa}
        durationInFrames={SKILL_MATRIX_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeTa"
        component={TaktTimeTa}
        durationInFrames={TAKT_TIME_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeTaDub"
        component={TaktTimeTa}
        durationInFrames={TAKT_TIME_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionTa"
        component={UniformProductionTa}
        durationInFrames={UNIFORM_PRODUCTION_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionTaDub"
        component={UniformProductionTa}
        durationInFrames={UNIFORM_PRODUCTION_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingTa"
        component={ValueStreamMappingTa}
        durationInFrames={VALUE_STREAM_MAPPING_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingTaDub"
        component={ValueStreamMappingTa}
        durationInFrames={VALUE_STREAM_MAPPING_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyTa"
        component={WhyWhyTa}
        durationInFrames={WHY_WHY_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyTaDub"
        component={WhyWhyTa}
        durationInFrames={WHY_WHY_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixTa"
        component={XMatrixTa}
        durationInFrames={X_MATRIX_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixTaDub"
        component={XMatrixTa}
        durationInFrames={X_MATRIX_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiTa"
        component={YamazumiTa}
        durationInFrames={YAMAZUMI_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiTaDub"
        component={YamazumiTa}
        durationInFrames={YAMAZUMI_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsTa"
        component={ZeroDefectsTa}
        durationInFrames={ZERO_DEFECTS_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsTaDub"
        component={ZeroDefectsTa}
        durationInFrames={ZERO_DEFECTS_TA_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartTe"
        component={BurnDownChartTe}
        durationInFrames={BURN_DOWN_CHART_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartTeDub"
        component={BurnDownChartTe}
        durationInFrames={BURN_DOWN_CHART_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyTe"
        component={CycleTimeStudyTe}
        durationInFrames={CYCLE_TIME_STUDY_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyTeDub"
        component={CycleTimeStudyTe}
        durationInFrames={CYCLE_TIME_STUDY_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingTe"
        component={DesignThinkingTe}
        durationInFrames={DESIGN_THINKING_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingTeDub"
        component={DesignThinkingTe}
        durationInFrames={DESIGN_THINKING_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteTe"
        component={EliminationOfWasteTe}
        durationInFrames={ELIMINATION_OF_WASTE_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteTeDub"
        component={EliminationOfWasteTe}
        durationInFrames={ELIMINATION_OF_WASTE_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEATe"
        component={FMEATe}
        durationInFrames={FMEA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEATeDub"
        component={FMEATe}
        durationInFrames={FMEA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaTe"
        component={GembaTe}
        durationInFrames={GEMBA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaTeDub"
        component={GembaTe}
        durationInFrames={GEMBA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoTe"
        component={HanchoTe}
        durationInFrames={HANCHO_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoTeDub"
        component={HanchoTe}
        durationInFrames={HANCHO_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaTe"
        component={IshikawaTe}
        durationInFrames={ISHIKAWA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaTeDub"
        component={IshikawaTe}
        durationInFrames={ISHIKAWA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaTe"
        component={JidokaTe}
        durationInFrames={JIDOKA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaTeDub"
        component={JidokaTe}
        durationInFrames={JIDOKA_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenTe"
        component={KaizenTe}
        durationInFrames={KAIZEN_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenTeDub"
        component={KaizenTe}
        durationInFrames={KAIZEN_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationTe"
        component={LowCostAutomationTe}
        durationInFrames={LOW_COST_AUTOMATION_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationTeDub"
        component={LowCostAutomationTe}
        durationInFrames={LOW_COST_AUTOMATION_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriTe"
        component={MudaMuraMuriTe}
        durationInFrames={MUDA_MURA_MURI_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriTeDub"
        component={MudaMuraMuriTe}
        durationInFrames={MUDA_MURA_MURI_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionTe"
        component={NextInspectionTe}
        durationInFrames={NEXT_INSPECTION_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionTeDub"
        component={NextInspectionTe}
        durationInFrames={NEXT_INSPECTION_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonTe"
        component={OnePointLessonTe}
        durationInFrames={ONE_POINT_LESSON_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonTeDub"
        component={OnePointLessonTe}
        durationInFrames={ONE_POINT_LESSON_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeTe"
        component={PokaYokeTe}
        durationInFrames={POKA_YOKE_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeTeDub"
        component={PokaYokeTe}
        durationInFrames={POKA_YOKE_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcTe"
        component={QrqcTe}
        durationInFrames={QRQC_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcTeDub"
        component={QrqcTe}
        durationInFrames={QRQC_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisTe"
        component={RootCauseAnalysisTe}
        durationInFrames={ROOT_CAUSE_ANALYSIS_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisTeDub"
        component={RootCauseAnalysisTe}
        durationInFrames={ROOT_CAUSE_ANALYSIS_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixTe"
        component={SkillMatrixTe}
        durationInFrames={SKILL_MATRIX_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixTeDub"
        component={SkillMatrixTe}
        durationInFrames={SKILL_MATRIX_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeTe"
        component={TaktTimeTe}
        durationInFrames={TAKT_TIME_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeTeDub"
        component={TaktTimeTe}
        durationInFrames={TAKT_TIME_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionTe"
        component={UniformProductionTe}
        durationInFrames={UNIFORM_PRODUCTION_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionTeDub"
        component={UniformProductionTe}
        durationInFrames={UNIFORM_PRODUCTION_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingTe"
        component={ValueStreamMappingTe}
        durationInFrames={VALUE_STREAM_MAPPING_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingTeDub"
        component={ValueStreamMappingTe}
        durationInFrames={VALUE_STREAM_MAPPING_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyTe"
        component={WhyWhyTe}
        durationInFrames={WHY_WHY_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyTeDub"
        component={WhyWhyTe}
        durationInFrames={WHY_WHY_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixTe"
        component={XMatrixTe}
        durationInFrames={X_MATRIX_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixTeDub"
        component={XMatrixTe}
        durationInFrames={X_MATRIX_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiTe"
        component={YamazumiTe}
        durationInFrames={YAMAZUMI_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiTeDub"
        component={YamazumiTe}
        durationInFrames={YAMAZUMI_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsTe"
        component={ZeroDefectsTe}
        durationInFrames={ZERO_DEFECTS_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsTeDub"
        component={ZeroDefectsTe}
        durationInFrames={ZERO_DEFECTS_TE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
    </>
  );
};
