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
import { A3ProblemSolvingMr, A3_PROBLEM_SOLVING_MR_DURATION } from "./lessons/a3_mr/A3ProblemSolvingMr";
import { BurnDownChartMr, BURN_DOWN_CHART_MR_DURATION } from "./lessons/bd_mr/BurnDownChartMr";
import { CycleTimeStudyMr, CYCLE_TIME_STUDY_MR_DURATION } from "./lessons/ct_mr/CycleTimeStudyMr";
import { DesignThinkingMr, DESIGN_THINKING_MR_DURATION } from "./lessons/dt_mr/DesignThinkingMr";
import { EliminationOfWasteMr, ELIMINATION_OF_WASTE_MR_DURATION } from "./lessons/ew_mr/EliminationOfWasteMr";
import { FMEAMr, FMEA_MR_DURATION } from "./lessons/fm_mr/FMEAMr";
import { GembaMr, GEMBA_MR_DURATION } from "./lessons/gb_mr/GembaMr";
import { HanchoMr, HANCHO_MR_DURATION } from "./lessons/hc_mr/HanchoMr";
import { IshikawaMr, ISHIKAWA_MR_DURATION } from "./lessons/ik_mr/IshikawaMr";
import { JidokaMr, JIDOKA_MR_DURATION } from "./lessons/jd_mr/JidokaMr";
import { KaizenMr, KAIZEN_MR_DURATION } from "./lessons/kz_mr/KaizenMr";
import { LowCostAutomationMr, LOW_COST_AUTOMATION_MR_DURATION } from "./lessons/lc_mr/LowCostAutomationMr";
import { MudaMuraMuriMr, MUDA_MURA_MURI_MR_DURATION } from "./lessons/mm_mr/MudaMuraMuriMr";
import { NextInspectionMr, NEXT_INSPECTION_MR_DURATION } from "./lessons/ni_mr/NextInspectionMr";
import { OnePointLessonMr, ONE_POINT_LESSON_MR_DURATION } from "./lessons/op_mr/OnePointLessonMr";
import { RootCauseAnalysisMr, ROOT_CAUSE_ANALYSIS_MR_DURATION } from "./lessons/rc_mr/RootCauseAnalysisMr";
import { SkillMatrixMr, SKILL_MATRIX_MR_DURATION } from "./lessons/sk_mr/SkillMatrixMr";
import { TaktTimeMr, TAKT_TIME_MR_DURATION } from "./lessons/tt_mr/TaktTimeMr";
import { UniformProductionMr, UNIFORM_PRODUCTION_MR_DURATION } from "./lessons/up_mr/UniformProductionMr";
import { ValueStreamMappingMr, VALUE_STREAM_MAPPING_MR_DURATION } from "./lessons/vs_mr/ValueStreamMappingMr";
import { WhyWhyMr, WHY_WHY_MR_DURATION } from "./lessons/ww_mr/WhyWhyMr";
import { XMatrixMr, X_MATRIX_MR_DURATION } from "./lessons/xm_mr/XMatrixMr";
import { YamazumiMr, YAMAZUMI_MR_DURATION } from "./lessons/yz_mr/YamazumiMr";
import { ZeroDefectsMr, ZERO_DEFECTS_MR_DURATION } from "./lessons/zd_mr/ZeroDefectsMr";
import { PokaYokeKn, POKA_YOKE_KN_DURATION } from "./lessons/pk_kn/PokaYokeKn";
import { A3ProblemSolvingKn, A3_PROBLEM_SOLVING_KN_DURATION } from "./lessons/a3_kn/A3ProblemSolvingKn";
import { BurnDownChartKn, BURN_DOWN_CHART_KN_DURATION } from "./lessons/bd_kn/BurnDownChartKn";
import { CycleTimeStudyKn, CYCLE_TIME_STUDY_KN_DURATION } from "./lessons/ct_kn/CycleTimeStudyKn";
import { DesignThinkingKn, DESIGN_THINKING_KN_DURATION } from "./lessons/dt_kn/DesignThinkingKn";
import { EliminationOfWasteKn, ELIMINATION_OF_WASTE_KN_DURATION } from "./lessons/ew_kn/EliminationOfWasteKn";
import { FMEAKn, FMEA_KN_DURATION } from "./lessons/fm_kn/FMEAKn";
import { GembaKn, GEMBA_KN_DURATION } from "./lessons/gb_kn/GembaKn";
import { HanchoKn, HANCHO_KN_DURATION } from "./lessons/hc_kn/HanchoKn";
import { IshikawaKn, ISHIKAWA_KN_DURATION } from "./lessons/ik_kn/IshikawaKn";
import { JidokaKn, JIDOKA_KN_DURATION } from "./lessons/jd_kn/JidokaKn";
import { KaizenKn, KAIZEN_KN_DURATION } from "./lessons/kz_kn/KaizenKn";
import { LowCostAutomationKn, LOW_COST_AUTOMATION_KN_DURATION } from "./lessons/lc_kn/LowCostAutomationKn";
import { MudaMuraMuriKn, MUDA_MURA_MURI_KN_DURATION } from "./lessons/mm_kn/MudaMuraMuriKn";
import { NextInspectionKn, NEXT_INSPECTION_KN_DURATION } from "./lessons/ni_kn/NextInspectionKn";
import { OnePointLessonKn, ONE_POINT_LESSON_KN_DURATION } from "./lessons/op_kn/OnePointLessonKn";
import { QrqcKn, QRQC_KN_DURATION } from "./lessons/qr_kn/QrqcKn";
import { RootCauseAnalysisKn, ROOT_CAUSE_ANALYSIS_KN_DURATION } from "./lessons/rc_kn/RootCauseAnalysisKn";
import { SkillMatrixKn, SKILL_MATRIX_KN_DURATION } from "./lessons/sk_kn/SkillMatrixKn";
import { TaktTimeKn, TAKT_TIME_KN_DURATION } from "./lessons/tt_kn/TaktTimeKn";
import { UniformProductionKn, UNIFORM_PRODUCTION_KN_DURATION } from "./lessons/up_kn/UniformProductionKn";
import { ValueStreamMappingKn, VALUE_STREAM_MAPPING_KN_DURATION } from "./lessons/vs_kn/ValueStreamMappingKn";
import { WhyWhyKn, WHY_WHY_KN_DURATION } from "./lessons/ww_kn/WhyWhyKn";
import { XMatrixKn, X_MATRIX_KN_DURATION } from "./lessons/xm_kn/XMatrixKn";
import { YamazumiKn, YAMAZUMI_KN_DURATION } from "./lessons/yz_kn/YamazumiKn";
import { ZeroDefectsKn, ZERO_DEFECTS_KN_DURATION } from "./lessons/zd_kn/ZeroDefectsKn";
import { PokaYokeBn, POKA_YOKE_BN_DURATION } from "./lessons/pk_bn/PokaYokeBn";
import { A3ProblemSolvingBn, A3_PROBLEM_SOLVING_BN_DURATION } from "./lessons/a3_bn/A3ProblemSolvingBn";
import { BurnDownChartBn, BURN_DOWN_CHART_BN_DURATION } from "./lessons/bd_bn/BurnDownChartBn";
import { CycleTimeStudyBn, CYCLE_TIME_STUDY_BN_DURATION } from "./lessons/ct_bn/CycleTimeStudyBn";
import { DesignThinkingBn, DESIGN_THINKING_BN_DURATION } from "./lessons/dt_bn/DesignThinkingBn";
import { EliminationOfWasteBn, ELIMINATION_OF_WASTE_BN_DURATION } from "./lessons/ew_bn/EliminationOfWasteBn";
import { FMEABn, FMEA_BN_DURATION } from "./lessons/fm_bn/FMEABn";
import { GembaBn, GEMBA_BN_DURATION } from "./lessons/gb_bn/GembaBn";
import { HanchoBn, HANCHO_BN_DURATION } from "./lessons/hc_bn/HanchoBn";
import { IshikawaBn, ISHIKAWA_BN_DURATION } from "./lessons/ik_bn/IshikawaBn";
import { JidokaBn, JIDOKA_BN_DURATION } from "./lessons/jd_bn/JidokaBn";
import { KaizenBn, KAIZEN_BN_DURATION } from "./lessons/kz_bn/KaizenBn";
import { LowCostAutomationBn, LOW_COST_AUTOMATION_BN_DURATION } from "./lessons/lc_bn/LowCostAutomationBn";
import { MudaMuraMuriBn, MUDA_MURA_MURI_BN_DURATION } from "./lessons/mm_bn/MudaMuraMuriBn";
import { NextInspectionBn, NEXT_INSPECTION_BN_DURATION } from "./lessons/ni_bn/NextInspectionBn";
import { OnePointLessonBn, ONE_POINT_LESSON_BN_DURATION } from "./lessons/op_bn/OnePointLessonBn";
import { QrqcBn, QRQC_BN_DURATION } from "./lessons/qr_bn/QrqcBn";
import { RootCauseAnalysisBn, ROOT_CAUSE_ANALYSIS_BN_DURATION } from "./lessons/rc_bn/RootCauseAnalysisBn";
import { SkillMatrixBn, SKILL_MATRIX_BN_DURATION } from "./lessons/sk_bn/SkillMatrixBn";
import { TaktTimeBn, TAKT_TIME_BN_DURATION } from "./lessons/tt_bn/TaktTimeBn";
import { UniformProductionBn, UNIFORM_PRODUCTION_BN_DURATION } from "./lessons/up_bn/UniformProductionBn";
import { ValueStreamMappingBn, VALUE_STREAM_MAPPING_BN_DURATION } from "./lessons/vs_bn/ValueStreamMappingBn";
import { WhyWhyBn, WHY_WHY_BN_DURATION } from "./lessons/ww_bn/WhyWhyBn";
import { XMatrixBn, X_MATRIX_BN_DURATION } from "./lessons/xm_bn/XMatrixBn";
import { YamazumiBn, YAMAZUMI_BN_DURATION } from "./lessons/yz_bn/YamazumiBn";
import { ZeroDefectsBn, ZERO_DEFECTS_BN_DURATION } from "./lessons/zd_bn/ZeroDefectsBn";
import { PokaYokeMl, POKA_YOKE_ML_DURATION } from "./lessons/pk_ml/PokaYokeMl";
import { A3ProblemSolvingMl, A3_PROBLEM_SOLVING_ML_DURATION } from "./lessons/a3_ml/A3ProblemSolvingMl";
import { BurnDownChartMl, BURN_DOWN_CHART_ML_DURATION } from "./lessons/bd_ml/BurnDownChartMl";
import { CycleTimeStudyMl, CYCLE_TIME_STUDY_ML_DURATION } from "./lessons/ct_ml/CycleTimeStudyMl";
import { DesignThinkingMl, DESIGN_THINKING_ML_DURATION } from "./lessons/dt_ml/DesignThinkingMl";
import { EliminationOfWasteMl, ELIMINATION_OF_WASTE_ML_DURATION } from "./lessons/ew_ml/EliminationOfWasteMl";
import { FMEAMl, FMEA_ML_DURATION } from "./lessons/fm_ml/FMEAMl";
import { GembaMl, GEMBA_ML_DURATION } from "./lessons/gb_ml/GembaMl";
import { HanchoMl, HANCHO_ML_DURATION } from "./lessons/hc_ml/HanchoMl";
import { IshikawaMl, ISHIKAWA_ML_DURATION } from "./lessons/ik_ml/IshikawaMl";
import { JidokaMl, JIDOKA_ML_DURATION } from "./lessons/jd_ml/JidokaMl";
import { KaizenMl, KAIZEN_ML_DURATION } from "./lessons/kz_ml/KaizenMl";
import { LowCostAutomationMl, LOW_COST_AUTOMATION_ML_DURATION } from "./lessons/lc_ml/LowCostAutomationMl";
import { MudaMuraMuriMl, MUDA_MURA_MURI_ML_DURATION } from "./lessons/mm_ml/MudaMuraMuriMl";
import { NextInspectionMl, NEXT_INSPECTION_ML_DURATION } from "./lessons/ni_ml/NextInspectionMl";
import { OnePointLessonMl, ONE_POINT_LESSON_ML_DURATION } from "./lessons/op_ml/OnePointLessonMl";
import { QrqcMl, QRQC_ML_DURATION } from "./lessons/qr_ml/QrqcMl";
import { RootCauseAnalysisMl, ROOT_CAUSE_ANALYSIS_ML_DURATION } from "./lessons/rc_ml/RootCauseAnalysisMl";
import { SkillMatrixMl, SKILL_MATRIX_ML_DURATION } from "./lessons/sk_ml/SkillMatrixMl";
import { TaktTimeMl, TAKT_TIME_ML_DURATION } from "./lessons/tt_ml/TaktTimeMl";
import { UniformProductionMl, UNIFORM_PRODUCTION_ML_DURATION } from "./lessons/up_ml/UniformProductionMl";
import { ValueStreamMappingMl, VALUE_STREAM_MAPPING_ML_DURATION } from "./lessons/vs_ml/ValueStreamMappingMl";
import { WhyWhyMl, WHY_WHY_ML_DURATION } from "./lessons/ww_ml/WhyWhyMl";
import { XMatrixMl, X_MATRIX_ML_DURATION } from "./lessons/xm_ml/XMatrixMl";
import { YamazumiMl, YAMAZUMI_ML_DURATION } from "./lessons/yz_ml/YamazumiMl";
import { ZeroDefectsMl, ZERO_DEFECTS_ML_DURATION } from "./lessons/zd_ml/ZeroDefectsMl";
import { PokaYokeEs, POKA_YOKE_ES_DURATION } from "./lessons/pk_es/PokaYokeEs";
import { A3ProblemSolvingEs, A3_PROBLEM_SOLVING_ES_DURATION } from "./lessons/a3_es/A3ProblemSolvingEs";
import { BurnDownChartEs, BURN_DOWN_CHART_ES_DURATION } from "./lessons/bd_es/BurnDownChartEs";
import { CycleTimeStudyEs, CYCLE_TIME_STUDY_ES_DURATION } from "./lessons/ct_es/CycleTimeStudyEs";
import { DesignThinkingEs, DESIGN_THINKING_ES_DURATION } from "./lessons/dt_es/DesignThinkingEs";
import { EliminationOfWasteEs, ELIMINATION_OF_WASTE_ES_DURATION } from "./lessons/ew_es/EliminationOfWasteEs";
import { FMEAEs, FMEA_ES_DURATION } from "./lessons/fm_es/FMEAEs";
import { GembaEs, GEMBA_ES_DURATION } from "./lessons/gb_es/GembaEs";
import { HanchoEs, HANCHO_ES_DURATION } from "./lessons/hc_es/HanchoEs";
import { IshikawaEs, ISHIKAWA_ES_DURATION } from "./lessons/ik_es/IshikawaEs";
import { JidokaEs, JIDOKA_ES_DURATION } from "./lessons/jd_es/JidokaEs";
import { KaizenEs, KAIZEN_ES_DURATION } from "./lessons/kz_es/KaizenEs";
import { LowCostAutomationEs, LOW_COST_AUTOMATION_ES_DURATION } from "./lessons/lc_es/LowCostAutomationEs";
import { MudaMuraMuriEs, MUDA_MURA_MURI_ES_DURATION } from "./lessons/mm_es/MudaMuraMuriEs";
import { NextInspectionEs, NEXT_INSPECTION_ES_DURATION } from "./lessons/ni_es/NextInspectionEs";
import { OnePointLessonEs, ONE_POINT_LESSON_ES_DURATION } from "./lessons/op_es/OnePointLessonEs";
import { QrqcEs, QRQC_ES_DURATION } from "./lessons/qr_es/QrqcEs";
import { RootCauseAnalysisEs, ROOT_CAUSE_ANALYSIS_ES_DURATION } from "./lessons/rc_es/RootCauseAnalysisEs";
import { SkillMatrixEs, SKILL_MATRIX_ES_DURATION } from "./lessons/sk_es/SkillMatrixEs";
import { TaktTimeEs, TAKT_TIME_ES_DURATION } from "./lessons/tt_es/TaktTimeEs";
import { UniformProductionEs, UNIFORM_PRODUCTION_ES_DURATION } from "./lessons/up_es/UniformProductionEs";
import { ValueStreamMappingEs, VALUE_STREAM_MAPPING_ES_DURATION } from "./lessons/vs_es/ValueStreamMappingEs";
import { WhyWhyEs, WHY_WHY_ES_DURATION } from "./lessons/ww_es/WhyWhyEs";
import { XMatrixEs, X_MATRIX_ES_DURATION } from "./lessons/xm_es/XMatrixEs";
import { YamazumiEs, YAMAZUMI_ES_DURATION } from "./lessons/yz_es/YamazumiEs";
import { ZeroDefectsEs, ZERO_DEFECTS_ES_DURATION } from "./lessons/zd_es/ZeroDefectsEs";
import { PokaYokeFr, POKA_YOKE_FR_DURATION } from "./lessons/pk_fr/PokaYokeFr";
import { A3ProblemSolvingFr, A3_PROBLEM_SOLVING_FR_DURATION } from "./lessons/a3_fr/A3ProblemSolvingFr";
import { BurnDownChartFr, BURN_DOWN_CHART_FR_DURATION } from "./lessons/bd_fr/BurnDownChartFr";
import { CycleTimeStudyFr, CYCLE_TIME_STUDY_FR_DURATION } from "./lessons/ct_fr/CycleTimeStudyFr";
import { DesignThinkingFr, DESIGN_THINKING_FR_DURATION } from "./lessons/dt_fr/DesignThinkingFr";
import { EliminationOfWasteFr, ELIMINATION_OF_WASTE_FR_DURATION } from "./lessons/ew_fr/EliminationOfWasteFr";
import { FMEAFr, FMEA_FR_DURATION } from "./lessons/fm_fr/FMEAFr";
import { GembaFr, GEMBA_FR_DURATION } from "./lessons/gb_fr/GembaFr";
import { HanchoFr, HANCHO_FR_DURATION } from "./lessons/hc_fr/HanchoFr";
import { IshikawaFr, ISHIKAWA_FR_DURATION } from "./lessons/ik_fr/IshikawaFr";
import { JidokaFr, JIDOKA_FR_DURATION } from "./lessons/jd_fr/JidokaFr";
import { KaizenFr, KAIZEN_FR_DURATION } from "./lessons/kz_fr/KaizenFr";
import { LowCostAutomationFr, LOW_COST_AUTOMATION_FR_DURATION } from "./lessons/lc_fr/LowCostAutomationFr";
import { MudaMuraMuriFr, MUDA_MURA_MURI_FR_DURATION } from "./lessons/mm_fr/MudaMuraMuriFr";
import { NextInspectionFr, NEXT_INSPECTION_FR_DURATION } from "./lessons/ni_fr/NextInspectionFr";
import { OnePointLessonFr, ONE_POINT_LESSON_FR_DURATION } from "./lessons/op_fr/OnePointLessonFr";
import { QrqcFr, QRQC_FR_DURATION } from "./lessons/qr_fr/QrqcFr";
import { RootCauseAnalysisFr, ROOT_CAUSE_ANALYSIS_FR_DURATION } from "./lessons/rc_fr/RootCauseAnalysisFr";
import { SkillMatrixFr, SKILL_MATRIX_FR_DURATION } from "./lessons/sk_fr/SkillMatrixFr";
import { TaktTimeFr, TAKT_TIME_FR_DURATION } from "./lessons/tt_fr/TaktTimeFr";
import { UniformProductionFr, UNIFORM_PRODUCTION_FR_DURATION } from "./lessons/up_fr/UniformProductionFr";
import { ValueStreamMappingFr, VALUE_STREAM_MAPPING_FR_DURATION } from "./lessons/vs_fr/ValueStreamMappingFr";
import { WhyWhyFr, WHY_WHY_FR_DURATION } from "./lessons/ww_fr/WhyWhyFr";
import { XMatrixFr, X_MATRIX_FR_DURATION } from "./lessons/xm_fr/XMatrixFr";
import { YamazumiFr, YAMAZUMI_FR_DURATION } from "./lessons/yz_fr/YamazumiFr";
import { ZeroDefectsFr, ZERO_DEFECTS_FR_DURATION } from "./lessons/zd_fr/ZeroDefectsFr";
import { PokaYokeDe, POKA_YOKE_DE_DURATION } from "./lessons/pk_de/PokaYokeDe";
import { A3ProblemSolvingDe, A3_PROBLEM_SOLVING_DE_DURATION } from "./lessons/a3_de/A3ProblemSolvingDe";
import { BurnDownChartDe, BURN_DOWN_CHART_DE_DURATION } from "./lessons/bd_de/BurnDownChartDe";
import { CycleTimeStudyDe, CYCLE_TIME_STUDY_DE_DURATION } from "./lessons/ct_de/CycleTimeStudyDe";
import { DesignThinkingDe, DESIGN_THINKING_DE_DURATION } from "./lessons/dt_de/DesignThinkingDe";
import { EliminationOfWasteDe, ELIMINATION_OF_WASTE_DE_DURATION } from "./lessons/ew_de/EliminationOfWasteDe";
import { FMEADe, FMEA_DE_DURATION } from "./lessons/fm_de/FMEADe";
import { GembaDe, GEMBA_DE_DURATION } from "./lessons/gb_de/GembaDe";
import { HanchoDe, HANCHO_DE_DURATION } from "./lessons/hc_de/HanchoDe";
import { IshikawaDe, ISHIKAWA_DE_DURATION } from "./lessons/ik_de/IshikawaDe";
import { JidokaDe, JIDOKA_DE_DURATION } from "./lessons/jd_de/JidokaDe";
import { KaizenDe, KAIZEN_DE_DURATION } from "./lessons/kz_de/KaizenDe";
import { LowCostAutomationDe, LOW_COST_AUTOMATION_DE_DURATION } from "./lessons/lc_de/LowCostAutomationDe";
import { MudaMuraMuriDe, MUDA_MURA_MURI_DE_DURATION } from "./lessons/mm_de/MudaMuraMuriDe";
import { NextInspectionDe, NEXT_INSPECTION_DE_DURATION } from "./lessons/ni_de/NextInspectionDe";
import { OnePointLessonDe, ONE_POINT_LESSON_DE_DURATION } from "./lessons/op_de/OnePointLessonDe";
import { QrqcDe, QRQC_DE_DURATION } from "./lessons/qr_de/QrqcDe";
import { RootCauseAnalysisDe, ROOT_CAUSE_ANALYSIS_DE_DURATION } from "./lessons/rc_de/RootCauseAnalysisDe";
import { SkillMatrixDe, SKILL_MATRIX_DE_DURATION } from "./lessons/sk_de/SkillMatrixDe";
import { TaktTimeDe, TAKT_TIME_DE_DURATION } from "./lessons/tt_de/TaktTimeDe";
import { UniformProductionDe, UNIFORM_PRODUCTION_DE_DURATION } from "./lessons/up_de/UniformProductionDe";
import { ValueStreamMappingDe, VALUE_STREAM_MAPPING_DE_DURATION } from "./lessons/vs_de/ValueStreamMappingDe";
import { WhyWhyDe, WHY_WHY_DE_DURATION } from "./lessons/ww_de/WhyWhyDe";
import { XMatrixDe, X_MATRIX_DE_DURATION } from "./lessons/xm_de/XMatrixDe";
import { YamazumiDe, YAMAZUMI_DE_DURATION } from "./lessons/yz_de/YamazumiDe";
import { ZeroDefectsDe, ZERO_DEFECTS_DE_DURATION } from "./lessons/zd_de/ZeroDefectsDe";
import { PokaYokeAr, POKA_YOKE_AR_DURATION } from "./lessons/pk_ar/PokaYokeAr";
import { A3ProblemSolvingAr, A3_PROBLEM_SOLVING_AR_DURATION } from "./lessons/a3_ar/A3ProblemSolvingAr";
import { BurnDownChartAr, BURN_DOWN_CHART_AR_DURATION } from "./lessons/bd_ar/BurnDownChartAr";
import { CycleTimeStudyAr, CYCLE_TIME_STUDY_AR_DURATION } from "./lessons/ct_ar/CycleTimeStudyAr";
import { DesignThinkingAr, DESIGN_THINKING_AR_DURATION } from "./lessons/dt_ar/DesignThinkingAr";
import { EliminationOfWasteAr, ELIMINATION_OF_WASTE_AR_DURATION } from "./lessons/ew_ar/EliminationOfWasteAr";
import { FMEAAr, FMEA_AR_DURATION } from "./lessons/fm_ar/FMEAAr";
import { GembaAr, GEMBA_AR_DURATION } from "./lessons/gb_ar/GembaAr";
import { HanchoAr, HANCHO_AR_DURATION } from "./lessons/hc_ar/HanchoAr";
import { IshikawaAr, ISHIKAWA_AR_DURATION } from "./lessons/ik_ar/IshikawaAr";
import { JidokaAr, JIDOKA_AR_DURATION } from "./lessons/jd_ar/JidokaAr";
import { KaizenAr, KAIZEN_AR_DURATION } from "./lessons/kz_ar/KaizenAr";
import { LowCostAutomationAr, LOW_COST_AUTOMATION_AR_DURATION } from "./lessons/lc_ar/LowCostAutomationAr";
import { MudaMuraMuriAr, MUDA_MURA_MURI_AR_DURATION } from "./lessons/mm_ar/MudaMuraMuriAr";
import { NextInspectionAr, NEXT_INSPECTION_AR_DURATION } from "./lessons/ni_ar/NextInspectionAr";
import { OnePointLessonAr, ONE_POINT_LESSON_AR_DURATION } from "./lessons/op_ar/OnePointLessonAr";
import { QrqcAr, QRQC_AR_DURATION } from "./lessons/qr_ar/QrqcAr";
import { RootCauseAnalysisAr, ROOT_CAUSE_ANALYSIS_AR_DURATION } from "./lessons/rc_ar/RootCauseAnalysisAr";
import { SkillMatrixAr, SKILL_MATRIX_AR_DURATION } from "./lessons/sk_ar/SkillMatrixAr";
import { TaktTimeAr, TAKT_TIME_AR_DURATION } from "./lessons/tt_ar/TaktTimeAr";
import { UniformProductionAr, UNIFORM_PRODUCTION_AR_DURATION } from "./lessons/up_ar/UniformProductionAr";
import { ValueStreamMappingAr, VALUE_STREAM_MAPPING_AR_DURATION } from "./lessons/vs_ar/ValueStreamMappingAr";
import { WhyWhyAr, WHY_WHY_AR_DURATION } from "./lessons/ww_ar/WhyWhyAr";
import { XMatrixAr, X_MATRIX_AR_DURATION } from "./lessons/xm_ar/XMatrixAr";
import { YamazumiAr, YAMAZUMI_AR_DURATION } from "./lessons/yz_ar/YamazumiAr";
import { ZeroDefectsAr, ZERO_DEFECTS_AR_DURATION } from "./lessons/zd_ar/ZeroDefectsAr";
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
      <Composition
        id="A3ProblemSolvingMr"
        component={A3ProblemSolvingMr}
        durationInFrames={A3_PROBLEM_SOLVING_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingMrDub"
        component={A3ProblemSolvingMr}
        durationInFrames={A3_PROBLEM_SOLVING_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartMr"
        component={BurnDownChartMr}
        durationInFrames={BURN_DOWN_CHART_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartMrDub"
        component={BurnDownChartMr}
        durationInFrames={BURN_DOWN_CHART_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyMr"
        component={CycleTimeStudyMr}
        durationInFrames={CYCLE_TIME_STUDY_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyMrDub"
        component={CycleTimeStudyMr}
        durationInFrames={CYCLE_TIME_STUDY_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingMr"
        component={DesignThinkingMr}
        durationInFrames={DESIGN_THINKING_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingMrDub"
        component={DesignThinkingMr}
        durationInFrames={DESIGN_THINKING_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteMr"
        component={EliminationOfWasteMr}
        durationInFrames={ELIMINATION_OF_WASTE_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteMrDub"
        component={EliminationOfWasteMr}
        durationInFrames={ELIMINATION_OF_WASTE_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAMr"
        component={FMEAMr}
        durationInFrames={FMEA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAMrDub"
        component={FMEAMr}
        durationInFrames={FMEA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaMr"
        component={GembaMr}
        durationInFrames={GEMBA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaMrDub"
        component={GembaMr}
        durationInFrames={GEMBA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoMr"
        component={HanchoMr}
        durationInFrames={HANCHO_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoMrDub"
        component={HanchoMr}
        durationInFrames={HANCHO_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaMr"
        component={IshikawaMr}
        durationInFrames={ISHIKAWA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaMrDub"
        component={IshikawaMr}
        durationInFrames={ISHIKAWA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaMr"
        component={JidokaMr}
        durationInFrames={JIDOKA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaMrDub"
        component={JidokaMr}
        durationInFrames={JIDOKA_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenMr"
        component={KaizenMr}
        durationInFrames={KAIZEN_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenMrDub"
        component={KaizenMr}
        durationInFrames={KAIZEN_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationMr"
        component={LowCostAutomationMr}
        durationInFrames={LOW_COST_AUTOMATION_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationMrDub"
        component={LowCostAutomationMr}
        durationInFrames={LOW_COST_AUTOMATION_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriMr"
        component={MudaMuraMuriMr}
        durationInFrames={MUDA_MURA_MURI_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriMrDub"
        component={MudaMuraMuriMr}
        durationInFrames={MUDA_MURA_MURI_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionMr"
        component={NextInspectionMr}
        durationInFrames={NEXT_INSPECTION_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionMrDub"
        component={NextInspectionMr}
        durationInFrames={NEXT_INSPECTION_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonMr"
        component={OnePointLessonMr}
        durationInFrames={ONE_POINT_LESSON_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonMrDub"
        component={OnePointLessonMr}
        durationInFrames={ONE_POINT_LESSON_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisMr"
        component={RootCauseAnalysisMr}
        durationInFrames={ROOT_CAUSE_ANALYSIS_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisMrDub"
        component={RootCauseAnalysisMr}
        durationInFrames={ROOT_CAUSE_ANALYSIS_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixMr"
        component={SkillMatrixMr}
        durationInFrames={SKILL_MATRIX_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixMrDub"
        component={SkillMatrixMr}
        durationInFrames={SKILL_MATRIX_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeMr"
        component={TaktTimeMr}
        durationInFrames={TAKT_TIME_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeMrDub"
        component={TaktTimeMr}
        durationInFrames={TAKT_TIME_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionMr"
        component={UniformProductionMr}
        durationInFrames={UNIFORM_PRODUCTION_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionMrDub"
        component={UniformProductionMr}
        durationInFrames={UNIFORM_PRODUCTION_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingMr"
        component={ValueStreamMappingMr}
        durationInFrames={VALUE_STREAM_MAPPING_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingMrDub"
        component={ValueStreamMappingMr}
        durationInFrames={VALUE_STREAM_MAPPING_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyMr"
        component={WhyWhyMr}
        durationInFrames={WHY_WHY_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyMrDub"
        component={WhyWhyMr}
        durationInFrames={WHY_WHY_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixMr"
        component={XMatrixMr}
        durationInFrames={X_MATRIX_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixMrDub"
        component={XMatrixMr}
        durationInFrames={X_MATRIX_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiMr"
        component={YamazumiMr}
        durationInFrames={YAMAZUMI_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiMrDub"
        component={YamazumiMr}
        durationInFrames={YAMAZUMI_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsMr"
        component={ZeroDefectsMr}
        durationInFrames={ZERO_DEFECTS_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsMrDub"
        component={ZeroDefectsMr}
        durationInFrames={ZERO_DEFECTS_MR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeKn"
        component={PokaYokeKn}
        durationInFrames={POKA_YOKE_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeKnDub"
        component={PokaYokeKn}
        durationInFrames={POKA_YOKE_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingKn"
        component={A3ProblemSolvingKn}
        durationInFrames={A3_PROBLEM_SOLVING_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingKnDub"
        component={A3ProblemSolvingKn}
        durationInFrames={A3_PROBLEM_SOLVING_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartKn"
        component={BurnDownChartKn}
        durationInFrames={BURN_DOWN_CHART_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartKnDub"
        component={BurnDownChartKn}
        durationInFrames={BURN_DOWN_CHART_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyKn"
        component={CycleTimeStudyKn}
        durationInFrames={CYCLE_TIME_STUDY_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyKnDub"
        component={CycleTimeStudyKn}
        durationInFrames={CYCLE_TIME_STUDY_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingKn"
        component={DesignThinkingKn}
        durationInFrames={DESIGN_THINKING_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingKnDub"
        component={DesignThinkingKn}
        durationInFrames={DESIGN_THINKING_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteKn"
        component={EliminationOfWasteKn}
        durationInFrames={ELIMINATION_OF_WASTE_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteKnDub"
        component={EliminationOfWasteKn}
        durationInFrames={ELIMINATION_OF_WASTE_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAKn"
        component={FMEAKn}
        durationInFrames={FMEA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAKnDub"
        component={FMEAKn}
        durationInFrames={FMEA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaKn"
        component={GembaKn}
        durationInFrames={GEMBA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaKnDub"
        component={GembaKn}
        durationInFrames={GEMBA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoKn"
        component={HanchoKn}
        durationInFrames={HANCHO_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoKnDub"
        component={HanchoKn}
        durationInFrames={HANCHO_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaKn"
        component={IshikawaKn}
        durationInFrames={ISHIKAWA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaKnDub"
        component={IshikawaKn}
        durationInFrames={ISHIKAWA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaKn"
        component={JidokaKn}
        durationInFrames={JIDOKA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaKnDub"
        component={JidokaKn}
        durationInFrames={JIDOKA_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenKn"
        component={KaizenKn}
        durationInFrames={KAIZEN_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenKnDub"
        component={KaizenKn}
        durationInFrames={KAIZEN_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationKn"
        component={LowCostAutomationKn}
        durationInFrames={LOW_COST_AUTOMATION_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationKnDub"
        component={LowCostAutomationKn}
        durationInFrames={LOW_COST_AUTOMATION_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriKn"
        component={MudaMuraMuriKn}
        durationInFrames={MUDA_MURA_MURI_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriKnDub"
        component={MudaMuraMuriKn}
        durationInFrames={MUDA_MURA_MURI_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionKn"
        component={NextInspectionKn}
        durationInFrames={NEXT_INSPECTION_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionKnDub"
        component={NextInspectionKn}
        durationInFrames={NEXT_INSPECTION_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonKn"
        component={OnePointLessonKn}
        durationInFrames={ONE_POINT_LESSON_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonKnDub"
        component={OnePointLessonKn}
        durationInFrames={ONE_POINT_LESSON_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcKn"
        component={QrqcKn}
        durationInFrames={QRQC_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcKnDub"
        component={QrqcKn}
        durationInFrames={QRQC_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisKn"
        component={RootCauseAnalysisKn}
        durationInFrames={ROOT_CAUSE_ANALYSIS_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisKnDub"
        component={RootCauseAnalysisKn}
        durationInFrames={ROOT_CAUSE_ANALYSIS_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixKn"
        component={SkillMatrixKn}
        durationInFrames={SKILL_MATRIX_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixKnDub"
        component={SkillMatrixKn}
        durationInFrames={SKILL_MATRIX_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeKn"
        component={TaktTimeKn}
        durationInFrames={TAKT_TIME_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeKnDub"
        component={TaktTimeKn}
        durationInFrames={TAKT_TIME_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionKn"
        component={UniformProductionKn}
        durationInFrames={UNIFORM_PRODUCTION_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionKnDub"
        component={UniformProductionKn}
        durationInFrames={UNIFORM_PRODUCTION_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingKn"
        component={ValueStreamMappingKn}
        durationInFrames={VALUE_STREAM_MAPPING_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingKnDub"
        component={ValueStreamMappingKn}
        durationInFrames={VALUE_STREAM_MAPPING_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyKn"
        component={WhyWhyKn}
        durationInFrames={WHY_WHY_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyKnDub"
        component={WhyWhyKn}
        durationInFrames={WHY_WHY_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixKn"
        component={XMatrixKn}
        durationInFrames={X_MATRIX_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixKnDub"
        component={XMatrixKn}
        durationInFrames={X_MATRIX_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiKn"
        component={YamazumiKn}
        durationInFrames={YAMAZUMI_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiKnDub"
        component={YamazumiKn}
        durationInFrames={YAMAZUMI_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsKn"
        component={ZeroDefectsKn}
        durationInFrames={ZERO_DEFECTS_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsKnDub"
        component={ZeroDefectsKn}
        durationInFrames={ZERO_DEFECTS_KN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeBn"
        component={PokaYokeBn}
        durationInFrames={POKA_YOKE_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeBnDub"
        component={PokaYokeBn}
        durationInFrames={POKA_YOKE_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingBn"
        component={A3ProblemSolvingBn}
        durationInFrames={A3_PROBLEM_SOLVING_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingBnDub"
        component={A3ProblemSolvingBn}
        durationInFrames={A3_PROBLEM_SOLVING_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartBn"
        component={BurnDownChartBn}
        durationInFrames={BURN_DOWN_CHART_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartBnDub"
        component={BurnDownChartBn}
        durationInFrames={BURN_DOWN_CHART_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyBn"
        component={CycleTimeStudyBn}
        durationInFrames={CYCLE_TIME_STUDY_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyBnDub"
        component={CycleTimeStudyBn}
        durationInFrames={CYCLE_TIME_STUDY_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingBn"
        component={DesignThinkingBn}
        durationInFrames={DESIGN_THINKING_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingBnDub"
        component={DesignThinkingBn}
        durationInFrames={DESIGN_THINKING_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteBn"
        component={EliminationOfWasteBn}
        durationInFrames={ELIMINATION_OF_WASTE_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteBnDub"
        component={EliminationOfWasteBn}
        durationInFrames={ELIMINATION_OF_WASTE_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEABn"
        component={FMEABn}
        durationInFrames={FMEA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEABnDub"
        component={FMEABn}
        durationInFrames={FMEA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaBn"
        component={GembaBn}
        durationInFrames={GEMBA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaBnDub"
        component={GembaBn}
        durationInFrames={GEMBA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoBn"
        component={HanchoBn}
        durationInFrames={HANCHO_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoBnDub"
        component={HanchoBn}
        durationInFrames={HANCHO_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaBn"
        component={IshikawaBn}
        durationInFrames={ISHIKAWA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaBnDub"
        component={IshikawaBn}
        durationInFrames={ISHIKAWA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaBn"
        component={JidokaBn}
        durationInFrames={JIDOKA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaBnDub"
        component={JidokaBn}
        durationInFrames={JIDOKA_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenBn"
        component={KaizenBn}
        durationInFrames={KAIZEN_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenBnDub"
        component={KaizenBn}
        durationInFrames={KAIZEN_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationBn"
        component={LowCostAutomationBn}
        durationInFrames={LOW_COST_AUTOMATION_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationBnDub"
        component={LowCostAutomationBn}
        durationInFrames={LOW_COST_AUTOMATION_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriBn"
        component={MudaMuraMuriBn}
        durationInFrames={MUDA_MURA_MURI_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriBnDub"
        component={MudaMuraMuriBn}
        durationInFrames={MUDA_MURA_MURI_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionBn"
        component={NextInspectionBn}
        durationInFrames={NEXT_INSPECTION_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionBnDub"
        component={NextInspectionBn}
        durationInFrames={NEXT_INSPECTION_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonBn"
        component={OnePointLessonBn}
        durationInFrames={ONE_POINT_LESSON_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonBnDub"
        component={OnePointLessonBn}
        durationInFrames={ONE_POINT_LESSON_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcBn"
        component={QrqcBn}
        durationInFrames={QRQC_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcBnDub"
        component={QrqcBn}
        durationInFrames={QRQC_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisBn"
        component={RootCauseAnalysisBn}
        durationInFrames={ROOT_CAUSE_ANALYSIS_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisBnDub"
        component={RootCauseAnalysisBn}
        durationInFrames={ROOT_CAUSE_ANALYSIS_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixBn"
        component={SkillMatrixBn}
        durationInFrames={SKILL_MATRIX_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixBnDub"
        component={SkillMatrixBn}
        durationInFrames={SKILL_MATRIX_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeBn"
        component={TaktTimeBn}
        durationInFrames={TAKT_TIME_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeBnDub"
        component={TaktTimeBn}
        durationInFrames={TAKT_TIME_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionBn"
        component={UniformProductionBn}
        durationInFrames={UNIFORM_PRODUCTION_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionBnDub"
        component={UniformProductionBn}
        durationInFrames={UNIFORM_PRODUCTION_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingBn"
        component={ValueStreamMappingBn}
        durationInFrames={VALUE_STREAM_MAPPING_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingBnDub"
        component={ValueStreamMappingBn}
        durationInFrames={VALUE_STREAM_MAPPING_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyBn"
        component={WhyWhyBn}
        durationInFrames={WHY_WHY_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyBnDub"
        component={WhyWhyBn}
        durationInFrames={WHY_WHY_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixBn"
        component={XMatrixBn}
        durationInFrames={X_MATRIX_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixBnDub"
        component={XMatrixBn}
        durationInFrames={X_MATRIX_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiBn"
        component={YamazumiBn}
        durationInFrames={YAMAZUMI_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiBnDub"
        component={YamazumiBn}
        durationInFrames={YAMAZUMI_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsBn"
        component={ZeroDefectsBn}
        durationInFrames={ZERO_DEFECTS_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsBnDub"
        component={ZeroDefectsBn}
        durationInFrames={ZERO_DEFECTS_BN_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeMl"
        component={PokaYokeMl}
        durationInFrames={POKA_YOKE_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeMlDub"
        component={PokaYokeMl}
        durationInFrames={POKA_YOKE_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingMl"
        component={A3ProblemSolvingMl}
        durationInFrames={A3_PROBLEM_SOLVING_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingMlDub"
        component={A3ProblemSolvingMl}
        durationInFrames={A3_PROBLEM_SOLVING_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartMl"
        component={BurnDownChartMl}
        durationInFrames={BURN_DOWN_CHART_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartMlDub"
        component={BurnDownChartMl}
        durationInFrames={BURN_DOWN_CHART_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyMl"
        component={CycleTimeStudyMl}
        durationInFrames={CYCLE_TIME_STUDY_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyMlDub"
        component={CycleTimeStudyMl}
        durationInFrames={CYCLE_TIME_STUDY_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingMl"
        component={DesignThinkingMl}
        durationInFrames={DESIGN_THINKING_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingMlDub"
        component={DesignThinkingMl}
        durationInFrames={DESIGN_THINKING_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteMl"
        component={EliminationOfWasteMl}
        durationInFrames={ELIMINATION_OF_WASTE_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteMlDub"
        component={EliminationOfWasteMl}
        durationInFrames={ELIMINATION_OF_WASTE_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAMl"
        component={FMEAMl}
        durationInFrames={FMEA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAMlDub"
        component={FMEAMl}
        durationInFrames={FMEA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaMl"
        component={GembaMl}
        durationInFrames={GEMBA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaMlDub"
        component={GembaMl}
        durationInFrames={GEMBA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoMl"
        component={HanchoMl}
        durationInFrames={HANCHO_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoMlDub"
        component={HanchoMl}
        durationInFrames={HANCHO_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaMl"
        component={IshikawaMl}
        durationInFrames={ISHIKAWA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaMlDub"
        component={IshikawaMl}
        durationInFrames={ISHIKAWA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaMl"
        component={JidokaMl}
        durationInFrames={JIDOKA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaMlDub"
        component={JidokaMl}
        durationInFrames={JIDOKA_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenMl"
        component={KaizenMl}
        durationInFrames={KAIZEN_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenMlDub"
        component={KaizenMl}
        durationInFrames={KAIZEN_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationMl"
        component={LowCostAutomationMl}
        durationInFrames={LOW_COST_AUTOMATION_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationMlDub"
        component={LowCostAutomationMl}
        durationInFrames={LOW_COST_AUTOMATION_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriMl"
        component={MudaMuraMuriMl}
        durationInFrames={MUDA_MURA_MURI_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriMlDub"
        component={MudaMuraMuriMl}
        durationInFrames={MUDA_MURA_MURI_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionMl"
        component={NextInspectionMl}
        durationInFrames={NEXT_INSPECTION_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionMlDub"
        component={NextInspectionMl}
        durationInFrames={NEXT_INSPECTION_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonMl"
        component={OnePointLessonMl}
        durationInFrames={ONE_POINT_LESSON_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonMlDub"
        component={OnePointLessonMl}
        durationInFrames={ONE_POINT_LESSON_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcMl"
        component={QrqcMl}
        durationInFrames={QRQC_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcMlDub"
        component={QrqcMl}
        durationInFrames={QRQC_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisMl"
        component={RootCauseAnalysisMl}
        durationInFrames={ROOT_CAUSE_ANALYSIS_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisMlDub"
        component={RootCauseAnalysisMl}
        durationInFrames={ROOT_CAUSE_ANALYSIS_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixMl"
        component={SkillMatrixMl}
        durationInFrames={SKILL_MATRIX_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixMlDub"
        component={SkillMatrixMl}
        durationInFrames={SKILL_MATRIX_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeMl"
        component={TaktTimeMl}
        durationInFrames={TAKT_TIME_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeMlDub"
        component={TaktTimeMl}
        durationInFrames={TAKT_TIME_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionMl"
        component={UniformProductionMl}
        durationInFrames={UNIFORM_PRODUCTION_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionMlDub"
        component={UniformProductionMl}
        durationInFrames={UNIFORM_PRODUCTION_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingMl"
        component={ValueStreamMappingMl}
        durationInFrames={VALUE_STREAM_MAPPING_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingMlDub"
        component={ValueStreamMappingMl}
        durationInFrames={VALUE_STREAM_MAPPING_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyMl"
        component={WhyWhyMl}
        durationInFrames={WHY_WHY_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyMlDub"
        component={WhyWhyMl}
        durationInFrames={WHY_WHY_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixMl"
        component={XMatrixMl}
        durationInFrames={X_MATRIX_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixMlDub"
        component={XMatrixMl}
        durationInFrames={X_MATRIX_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiMl"
        component={YamazumiMl}
        durationInFrames={YAMAZUMI_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiMlDub"
        component={YamazumiMl}
        durationInFrames={YAMAZUMI_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsMl"
        component={ZeroDefectsMl}
        durationInFrames={ZERO_DEFECTS_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsMlDub"
        component={ZeroDefectsMl}
        durationInFrames={ZERO_DEFECTS_ML_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeEs"
        component={PokaYokeEs}
        durationInFrames={POKA_YOKE_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeEsDub"
        component={PokaYokeEs}
        durationInFrames={POKA_YOKE_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingEs"
        component={A3ProblemSolvingEs}
        durationInFrames={A3_PROBLEM_SOLVING_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingEsDub"
        component={A3ProblemSolvingEs}
        durationInFrames={A3_PROBLEM_SOLVING_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartEs"
        component={BurnDownChartEs}
        durationInFrames={BURN_DOWN_CHART_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartEsDub"
        component={BurnDownChartEs}
        durationInFrames={BURN_DOWN_CHART_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyEs"
        component={CycleTimeStudyEs}
        durationInFrames={CYCLE_TIME_STUDY_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyEsDub"
        component={CycleTimeStudyEs}
        durationInFrames={CYCLE_TIME_STUDY_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingEs"
        component={DesignThinkingEs}
        durationInFrames={DESIGN_THINKING_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingEsDub"
        component={DesignThinkingEs}
        durationInFrames={DESIGN_THINKING_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteEs"
        component={EliminationOfWasteEs}
        durationInFrames={ELIMINATION_OF_WASTE_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteEsDub"
        component={EliminationOfWasteEs}
        durationInFrames={ELIMINATION_OF_WASTE_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAEs"
        component={FMEAEs}
        durationInFrames={FMEA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAEsDub"
        component={FMEAEs}
        durationInFrames={FMEA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaEs"
        component={GembaEs}
        durationInFrames={GEMBA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaEsDub"
        component={GembaEs}
        durationInFrames={GEMBA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoEs"
        component={HanchoEs}
        durationInFrames={HANCHO_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoEsDub"
        component={HanchoEs}
        durationInFrames={HANCHO_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaEs"
        component={IshikawaEs}
        durationInFrames={ISHIKAWA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaEsDub"
        component={IshikawaEs}
        durationInFrames={ISHIKAWA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaEs"
        component={JidokaEs}
        durationInFrames={JIDOKA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaEsDub"
        component={JidokaEs}
        durationInFrames={JIDOKA_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenEs"
        component={KaizenEs}
        durationInFrames={KAIZEN_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenEsDub"
        component={KaizenEs}
        durationInFrames={KAIZEN_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationEs"
        component={LowCostAutomationEs}
        durationInFrames={LOW_COST_AUTOMATION_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationEsDub"
        component={LowCostAutomationEs}
        durationInFrames={LOW_COST_AUTOMATION_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriEs"
        component={MudaMuraMuriEs}
        durationInFrames={MUDA_MURA_MURI_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriEsDub"
        component={MudaMuraMuriEs}
        durationInFrames={MUDA_MURA_MURI_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionEs"
        component={NextInspectionEs}
        durationInFrames={NEXT_INSPECTION_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionEsDub"
        component={NextInspectionEs}
        durationInFrames={NEXT_INSPECTION_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonEs"
        component={OnePointLessonEs}
        durationInFrames={ONE_POINT_LESSON_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonEsDub"
        component={OnePointLessonEs}
        durationInFrames={ONE_POINT_LESSON_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcEs"
        component={QrqcEs}
        durationInFrames={QRQC_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcEsDub"
        component={QrqcEs}
        durationInFrames={QRQC_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisEs"
        component={RootCauseAnalysisEs}
        durationInFrames={ROOT_CAUSE_ANALYSIS_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisEsDub"
        component={RootCauseAnalysisEs}
        durationInFrames={ROOT_CAUSE_ANALYSIS_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixEs"
        component={SkillMatrixEs}
        durationInFrames={SKILL_MATRIX_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixEsDub"
        component={SkillMatrixEs}
        durationInFrames={SKILL_MATRIX_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeEs"
        component={TaktTimeEs}
        durationInFrames={TAKT_TIME_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeEsDub"
        component={TaktTimeEs}
        durationInFrames={TAKT_TIME_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionEs"
        component={UniformProductionEs}
        durationInFrames={UNIFORM_PRODUCTION_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionEsDub"
        component={UniformProductionEs}
        durationInFrames={UNIFORM_PRODUCTION_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingEs"
        component={ValueStreamMappingEs}
        durationInFrames={VALUE_STREAM_MAPPING_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingEsDub"
        component={ValueStreamMappingEs}
        durationInFrames={VALUE_STREAM_MAPPING_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyEs"
        component={WhyWhyEs}
        durationInFrames={WHY_WHY_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyEsDub"
        component={WhyWhyEs}
        durationInFrames={WHY_WHY_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixEs"
        component={XMatrixEs}
        durationInFrames={X_MATRIX_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixEsDub"
        component={XMatrixEs}
        durationInFrames={X_MATRIX_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiEs"
        component={YamazumiEs}
        durationInFrames={YAMAZUMI_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiEsDub"
        component={YamazumiEs}
        durationInFrames={YAMAZUMI_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsEs"
        component={ZeroDefectsEs}
        durationInFrames={ZERO_DEFECTS_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsEsDub"
        component={ZeroDefectsEs}
        durationInFrames={ZERO_DEFECTS_ES_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeFr"
        component={PokaYokeFr}
        durationInFrames={POKA_YOKE_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeFrDub"
        component={PokaYokeFr}
        durationInFrames={POKA_YOKE_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingFr"
        component={A3ProblemSolvingFr}
        durationInFrames={A3_PROBLEM_SOLVING_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingFrDub"
        component={A3ProblemSolvingFr}
        durationInFrames={A3_PROBLEM_SOLVING_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartFr"
        component={BurnDownChartFr}
        durationInFrames={BURN_DOWN_CHART_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartFrDub"
        component={BurnDownChartFr}
        durationInFrames={BURN_DOWN_CHART_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyFr"
        component={CycleTimeStudyFr}
        durationInFrames={CYCLE_TIME_STUDY_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyFrDub"
        component={CycleTimeStudyFr}
        durationInFrames={CYCLE_TIME_STUDY_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingFr"
        component={DesignThinkingFr}
        durationInFrames={DESIGN_THINKING_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingFrDub"
        component={DesignThinkingFr}
        durationInFrames={DESIGN_THINKING_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteFr"
        component={EliminationOfWasteFr}
        durationInFrames={ELIMINATION_OF_WASTE_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteFrDub"
        component={EliminationOfWasteFr}
        durationInFrames={ELIMINATION_OF_WASTE_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAFr"
        component={FMEAFr}
        durationInFrames={FMEA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAFrDub"
        component={FMEAFr}
        durationInFrames={FMEA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaFr"
        component={GembaFr}
        durationInFrames={GEMBA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaFrDub"
        component={GembaFr}
        durationInFrames={GEMBA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoFr"
        component={HanchoFr}
        durationInFrames={HANCHO_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoFrDub"
        component={HanchoFr}
        durationInFrames={HANCHO_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaFr"
        component={IshikawaFr}
        durationInFrames={ISHIKAWA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaFrDub"
        component={IshikawaFr}
        durationInFrames={ISHIKAWA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaFr"
        component={JidokaFr}
        durationInFrames={JIDOKA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaFrDub"
        component={JidokaFr}
        durationInFrames={JIDOKA_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenFr"
        component={KaizenFr}
        durationInFrames={KAIZEN_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenFrDub"
        component={KaizenFr}
        durationInFrames={KAIZEN_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationFr"
        component={LowCostAutomationFr}
        durationInFrames={LOW_COST_AUTOMATION_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationFrDub"
        component={LowCostAutomationFr}
        durationInFrames={LOW_COST_AUTOMATION_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriFr"
        component={MudaMuraMuriFr}
        durationInFrames={MUDA_MURA_MURI_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriFrDub"
        component={MudaMuraMuriFr}
        durationInFrames={MUDA_MURA_MURI_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionFr"
        component={NextInspectionFr}
        durationInFrames={NEXT_INSPECTION_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionFrDub"
        component={NextInspectionFr}
        durationInFrames={NEXT_INSPECTION_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonFr"
        component={OnePointLessonFr}
        durationInFrames={ONE_POINT_LESSON_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonFrDub"
        component={OnePointLessonFr}
        durationInFrames={ONE_POINT_LESSON_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcFr"
        component={QrqcFr}
        durationInFrames={QRQC_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcFrDub"
        component={QrqcFr}
        durationInFrames={QRQC_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisFr"
        component={RootCauseAnalysisFr}
        durationInFrames={ROOT_CAUSE_ANALYSIS_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisFrDub"
        component={RootCauseAnalysisFr}
        durationInFrames={ROOT_CAUSE_ANALYSIS_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixFr"
        component={SkillMatrixFr}
        durationInFrames={SKILL_MATRIX_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixFrDub"
        component={SkillMatrixFr}
        durationInFrames={SKILL_MATRIX_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeFr"
        component={TaktTimeFr}
        durationInFrames={TAKT_TIME_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeFrDub"
        component={TaktTimeFr}
        durationInFrames={TAKT_TIME_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionFr"
        component={UniformProductionFr}
        durationInFrames={UNIFORM_PRODUCTION_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionFrDub"
        component={UniformProductionFr}
        durationInFrames={UNIFORM_PRODUCTION_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingFr"
        component={ValueStreamMappingFr}
        durationInFrames={VALUE_STREAM_MAPPING_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingFrDub"
        component={ValueStreamMappingFr}
        durationInFrames={VALUE_STREAM_MAPPING_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyFr"
        component={WhyWhyFr}
        durationInFrames={WHY_WHY_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyFrDub"
        component={WhyWhyFr}
        durationInFrames={WHY_WHY_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixFr"
        component={XMatrixFr}
        durationInFrames={X_MATRIX_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixFrDub"
        component={XMatrixFr}
        durationInFrames={X_MATRIX_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiFr"
        component={YamazumiFr}
        durationInFrames={YAMAZUMI_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiFrDub"
        component={YamazumiFr}
        durationInFrames={YAMAZUMI_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsFr"
        component={ZeroDefectsFr}
        durationInFrames={ZERO_DEFECTS_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsFrDub"
        component={ZeroDefectsFr}
        durationInFrames={ZERO_DEFECTS_FR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeDe"
        component={PokaYokeDe}
        durationInFrames={POKA_YOKE_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeDeDub"
        component={PokaYokeDe}
        durationInFrames={POKA_YOKE_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingDe"
        component={A3ProblemSolvingDe}
        durationInFrames={A3_PROBLEM_SOLVING_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingDeDub"
        component={A3ProblemSolvingDe}
        durationInFrames={A3_PROBLEM_SOLVING_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartDe"
        component={BurnDownChartDe}
        durationInFrames={BURN_DOWN_CHART_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartDeDub"
        component={BurnDownChartDe}
        durationInFrames={BURN_DOWN_CHART_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyDe"
        component={CycleTimeStudyDe}
        durationInFrames={CYCLE_TIME_STUDY_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyDeDub"
        component={CycleTimeStudyDe}
        durationInFrames={CYCLE_TIME_STUDY_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingDe"
        component={DesignThinkingDe}
        durationInFrames={DESIGN_THINKING_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingDeDub"
        component={DesignThinkingDe}
        durationInFrames={DESIGN_THINKING_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteDe"
        component={EliminationOfWasteDe}
        durationInFrames={ELIMINATION_OF_WASTE_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteDeDub"
        component={EliminationOfWasteDe}
        durationInFrames={ELIMINATION_OF_WASTE_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEADe"
        component={FMEADe}
        durationInFrames={FMEA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEADeDub"
        component={FMEADe}
        durationInFrames={FMEA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaDe"
        component={GembaDe}
        durationInFrames={GEMBA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaDeDub"
        component={GembaDe}
        durationInFrames={GEMBA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoDe"
        component={HanchoDe}
        durationInFrames={HANCHO_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoDeDub"
        component={HanchoDe}
        durationInFrames={HANCHO_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaDe"
        component={IshikawaDe}
        durationInFrames={ISHIKAWA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaDeDub"
        component={IshikawaDe}
        durationInFrames={ISHIKAWA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaDe"
        component={JidokaDe}
        durationInFrames={JIDOKA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaDeDub"
        component={JidokaDe}
        durationInFrames={JIDOKA_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenDe"
        component={KaizenDe}
        durationInFrames={KAIZEN_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenDeDub"
        component={KaizenDe}
        durationInFrames={KAIZEN_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationDe"
        component={LowCostAutomationDe}
        durationInFrames={LOW_COST_AUTOMATION_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationDeDub"
        component={LowCostAutomationDe}
        durationInFrames={LOW_COST_AUTOMATION_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriDe"
        component={MudaMuraMuriDe}
        durationInFrames={MUDA_MURA_MURI_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriDeDub"
        component={MudaMuraMuriDe}
        durationInFrames={MUDA_MURA_MURI_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionDe"
        component={NextInspectionDe}
        durationInFrames={NEXT_INSPECTION_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionDeDub"
        component={NextInspectionDe}
        durationInFrames={NEXT_INSPECTION_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonDe"
        component={OnePointLessonDe}
        durationInFrames={ONE_POINT_LESSON_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonDeDub"
        component={OnePointLessonDe}
        durationInFrames={ONE_POINT_LESSON_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcDe"
        component={QrqcDe}
        durationInFrames={QRQC_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcDeDub"
        component={QrqcDe}
        durationInFrames={QRQC_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisDe"
        component={RootCauseAnalysisDe}
        durationInFrames={ROOT_CAUSE_ANALYSIS_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisDeDub"
        component={RootCauseAnalysisDe}
        durationInFrames={ROOT_CAUSE_ANALYSIS_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixDe"
        component={SkillMatrixDe}
        durationInFrames={SKILL_MATRIX_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixDeDub"
        component={SkillMatrixDe}
        durationInFrames={SKILL_MATRIX_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeDe"
        component={TaktTimeDe}
        durationInFrames={TAKT_TIME_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeDeDub"
        component={TaktTimeDe}
        durationInFrames={TAKT_TIME_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionDe"
        component={UniformProductionDe}
        durationInFrames={UNIFORM_PRODUCTION_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionDeDub"
        component={UniformProductionDe}
        durationInFrames={UNIFORM_PRODUCTION_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingDe"
        component={ValueStreamMappingDe}
        durationInFrames={VALUE_STREAM_MAPPING_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingDeDub"
        component={ValueStreamMappingDe}
        durationInFrames={VALUE_STREAM_MAPPING_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyDe"
        component={WhyWhyDe}
        durationInFrames={WHY_WHY_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyDeDub"
        component={WhyWhyDe}
        durationInFrames={WHY_WHY_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixDe"
        component={XMatrixDe}
        durationInFrames={X_MATRIX_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixDeDub"
        component={XMatrixDe}
        durationInFrames={X_MATRIX_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiDe"
        component={YamazumiDe}
        durationInFrames={YAMAZUMI_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiDeDub"
        component={YamazumiDe}
        durationInFrames={YAMAZUMI_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsDe"
        component={ZeroDefectsDe}
        durationInFrames={ZERO_DEFECTS_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsDeDub"
        component={ZeroDefectsDe}
        durationInFrames={ZERO_DEFECTS_DE_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="PokaYokeAr"
        component={PokaYokeAr}
        durationInFrames={POKA_YOKE_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="PokaYokeArDub"
        component={PokaYokeAr}
        durationInFrames={POKA_YOKE_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="A3ProblemSolvingAr"
        component={A3ProblemSolvingAr}
        durationInFrames={A3_PROBLEM_SOLVING_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="A3ProblemSolvingArDub"
        component={A3ProblemSolvingAr}
        durationInFrames={A3_PROBLEM_SOLVING_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="BurnDownChartAr"
        component={BurnDownChartAr}
        durationInFrames={BURN_DOWN_CHART_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="BurnDownChartArDub"
        component={BurnDownChartAr}
        durationInFrames={BURN_DOWN_CHART_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="CycleTimeStudyAr"
        component={CycleTimeStudyAr}
        durationInFrames={CYCLE_TIME_STUDY_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="CycleTimeStudyArDub"
        component={CycleTimeStudyAr}
        durationInFrames={CYCLE_TIME_STUDY_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="DesignThinkingAr"
        component={DesignThinkingAr}
        durationInFrames={DESIGN_THINKING_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="DesignThinkingArDub"
        component={DesignThinkingAr}
        durationInFrames={DESIGN_THINKING_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="EliminationOfWasteAr"
        component={EliminationOfWasteAr}
        durationInFrames={ELIMINATION_OF_WASTE_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="EliminationOfWasteArDub"
        component={EliminationOfWasteAr}
        durationInFrames={ELIMINATION_OF_WASTE_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="FMEAAr"
        component={FMEAAr}
        durationInFrames={FMEA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="FMEAArDub"
        component={FMEAAr}
        durationInFrames={FMEA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="GembaAr"
        component={GembaAr}
        durationInFrames={GEMBA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="GembaArDub"
        component={GembaAr}
        durationInFrames={GEMBA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="HanchoAr"
        component={HanchoAr}
        durationInFrames={HANCHO_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="HanchoArDub"
        component={HanchoAr}
        durationInFrames={HANCHO_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="IshikawaAr"
        component={IshikawaAr}
        durationInFrames={ISHIKAWA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="IshikawaArDub"
        component={IshikawaAr}
        durationInFrames={ISHIKAWA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="JidokaAr"
        component={JidokaAr}
        durationInFrames={JIDOKA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="JidokaArDub"
        component={JidokaAr}
        durationInFrames={JIDOKA_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="KaizenAr"
        component={KaizenAr}
        durationInFrames={KAIZEN_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="KaizenArDub"
        component={KaizenAr}
        durationInFrames={KAIZEN_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="LowCostAutomationAr"
        component={LowCostAutomationAr}
        durationInFrames={LOW_COST_AUTOMATION_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="LowCostAutomationArDub"
        component={LowCostAutomationAr}
        durationInFrames={LOW_COST_AUTOMATION_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="MudaMuraMuriAr"
        component={MudaMuraMuriAr}
        durationInFrames={MUDA_MURA_MURI_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="MudaMuraMuriArDub"
        component={MudaMuraMuriAr}
        durationInFrames={MUDA_MURA_MURI_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="NextInspectionAr"
        component={NextInspectionAr}
        durationInFrames={NEXT_INSPECTION_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="NextInspectionArDub"
        component={NextInspectionAr}
        durationInFrames={NEXT_INSPECTION_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="OnePointLessonAr"
        component={OnePointLessonAr}
        durationInFrames={ONE_POINT_LESSON_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="OnePointLessonArDub"
        component={OnePointLessonAr}
        durationInFrames={ONE_POINT_LESSON_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="QrqcAr"
        component={QrqcAr}
        durationInFrames={QRQC_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="QrqcArDub"
        component={QrqcAr}
        durationInFrames={QRQC_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="RootCauseAnalysisAr"
        component={RootCauseAnalysisAr}
        durationInFrames={ROOT_CAUSE_ANALYSIS_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="RootCauseAnalysisArDub"
        component={RootCauseAnalysisAr}
        durationInFrames={ROOT_CAUSE_ANALYSIS_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="SkillMatrixAr"
        component={SkillMatrixAr}
        durationInFrames={SKILL_MATRIX_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="SkillMatrixArDub"
        component={SkillMatrixAr}
        durationInFrames={SKILL_MATRIX_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="TaktTimeAr"
        component={TaktTimeAr}
        durationInFrames={TAKT_TIME_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="TaktTimeArDub"
        component={TaktTimeAr}
        durationInFrames={TAKT_TIME_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="UniformProductionAr"
        component={UniformProductionAr}
        durationInFrames={UNIFORM_PRODUCTION_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="UniformProductionArDub"
        component={UniformProductionAr}
        durationInFrames={UNIFORM_PRODUCTION_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ValueStreamMappingAr"
        component={ValueStreamMappingAr}
        durationInFrames={VALUE_STREAM_MAPPING_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ValueStreamMappingArDub"
        component={ValueStreamMappingAr}
        durationInFrames={VALUE_STREAM_MAPPING_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="WhyWhyAr"
        component={WhyWhyAr}
        durationInFrames={WHY_WHY_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="WhyWhyArDub"
        component={WhyWhyAr}
        durationInFrames={WHY_WHY_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="XMatrixAr"
        component={XMatrixAr}
        durationInFrames={X_MATRIX_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="XMatrixArDub"
        component={XMatrixAr}
        durationInFrames={X_MATRIX_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="YamazumiAr"
        component={YamazumiAr}
        durationInFrames={YAMAZUMI_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="YamazumiArDub"
        component={YamazumiAr}
        durationInFrames={YAMAZUMI_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
      <Composition
        id="ZeroDefectsAr"
        component={ZeroDefectsAr}
        durationInFrames={ZERO_DEFECTS_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
      />
      <Composition
        id="ZeroDefectsArDub"
        component={ZeroDefectsAr}
        durationInFrames={ZERO_DEFECTS_AR_DURATION}
        fps={fps}
        width={width}
        height={height}
        defaultProps={{ captions: false }}
      />
    </>
  );
};
