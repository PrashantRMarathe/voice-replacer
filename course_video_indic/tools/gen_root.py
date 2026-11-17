"""Write src/Root.tsx and scripts/lessons.ts from one lesson list.
check.ts looks for literal id="..." strings in Root.tsx, so each composition is spelled out.

  python tools/gen_root.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent

# (lesson id = component folder, component / composition name, duration const)
LESSONS = [
    ("a3_hi", "A3ProblemSolvingHi", "A3_PROBLEM_SOLVING_HI_DURATION"),
    ("bd_hi", "BurnDownChartHi", "BURN_DOWN_CHART_HI_DURATION"),
    ("ct_hi", "CycleTimeStudyHi", "CYCLE_TIME_STUDY_HI_DURATION"),
    ("dt_hi", "DesignThinkingHi", "DESIGN_THINKING_HI_DURATION"),
    ("ew_hi", "EliminationOfWasteHi", "ELIMINATION_OF_WASTE_HI_DURATION"),
    ("fm_hi", "FMEAHi", "FMEA_HI_DURATION"),
    ("gb_hi", "GembaHi", "GEMBA_HI_DURATION"),
    ("hc_hi", "HanchoHi", "HANCHO_HI_DURATION"),
    ("ik_hi", "IshikawaHi", "ISHIKAWA_HI_DURATION"),
    ("jd_hi", "JidokaHi", "JIDOKA_HI_DURATION"),
    ("kz_hi", "KaizenHi", "KAIZEN_HI_DURATION"),
    ("lc_hi", "LowCostAutomationHi", "LOW_COST_AUTOMATION_HI_DURATION"),
    ("mm_hi", "MudaMuraMuriHi", "MUDA_MURA_MURI_HI_DURATION"),
    ("ni_hi", "NextInspectionHi", "NEXT_INSPECTION_HI_DURATION"),
    ("op_hi", "OnePointLessonHi", "ONE_POINT_LESSON_HI_DURATION"),
    ("pk_hi", "PokaYokeHi", "POKA_YOKE_HI_DURATION"),
    ("qr_hi", "QrqcHi", "QRQC_HI_DURATION"),
    ("rc_hi", "RootCauseAnalysisHi", "ROOT_CAUSE_ANALYSIS_HI_DURATION"),
    ("sk_hi", "SkillMatrixHi", "SKILL_MATRIX_HI_DURATION"),
    ("tt_hi", "TaktTimeHi", "TAKT_TIME_HI_DURATION"),
    ("up_hi", "UniformProductionHi", "UNIFORM_PRODUCTION_HI_DURATION"),
    ("vs_hi", "ValueStreamMappingHi", "VALUE_STREAM_MAPPING_HI_DURATION"),
    ("ww_hi", "WhyWhyHi", "WHY_WHY_HI_DURATION"),
    ("xm_hi", "XMatrixHi", "X_MATRIX_HI_DURATION"),
    ("yz_hi", "YamazumiHi", "YAMAZUMI_HI_DURATION"),
    ("zd_hi", "ZeroDefectsHi", "ZERO_DEFECTS_HI_DURATION"),
    ("pk_mr", "PokaYokeMr", "POKA_YOKE_MR_DURATION"),
    ("qr_mr", "QrqcMr", "QRQC_MR_DURATION"),
    ("a3_te", "A3ProblemSolvingTe", "A3_PROBLEM_SOLVING_TE_DURATION"),
    ("a3_ta", "A3ProblemSolvingTa", "A3_PROBLEM_SOLVING_TA_DURATION"),
    ("bd_ta", "BurnDownChartTa", "BURN_DOWN_CHART_TA_DURATION"),
    ("kz_ta", "KaizenTa", "KAIZEN_TA_DURATION"),
    ("ct_ta", "CycleTimeStudyTa", "CYCLE_TIME_STUDY_TA_DURATION"),
    ("dt_ta", "DesignThinkingTa", "DESIGN_THINKING_TA_DURATION"),
    ("ew_ta", "EliminationOfWasteTa", "ELIMINATION_OF_WASTE_TA_DURATION"),
    ("fm_ta", "FMEATa", "FMEA_TA_DURATION"),
    ("gb_ta", "GembaTa", "GEMBA_TA_DURATION"),
    ("hc_ta", "HanchoTa", "HANCHO_TA_DURATION"),
    ("ik_ta", "IshikawaTa", "ISHIKAWA_TA_DURATION"),
    ("jd_ta", "JidokaTa", "JIDOKA_TA_DURATION"),
    ("lc_ta", "LowCostAutomationTa", "LOW_COST_AUTOMATION_TA_DURATION"),
    ("mm_ta", "MudaMuraMuriTa", "MUDA_MURA_MURI_TA_DURATION"),
    ("ni_ta", "NextInspectionTa", "NEXT_INSPECTION_TA_DURATION"),
    ("op_ta", "OnePointLessonTa", "ONE_POINT_LESSON_TA_DURATION"),
    ("pk_ta", "PokaYokeTa", "POKA_YOKE_TA_DURATION"),
    ("qr_ta", "QrqcTa", "QRQC_TA_DURATION"),
    ("rc_ta", "RootCauseAnalysisTa", "ROOT_CAUSE_ANALYSIS_TA_DURATION"),
    ("sk_ta", "SkillMatrixTa", "SKILL_MATRIX_TA_DURATION"),
    ("tt_ta", "TaktTimeTa", "TAKT_TIME_TA_DURATION"),
    ("up_ta", "UniformProductionTa", "UNIFORM_PRODUCTION_TA_DURATION"),
    ("vs_ta", "ValueStreamMappingTa", "VALUE_STREAM_MAPPING_TA_DURATION"),
    ("ww_ta", "WhyWhyTa", "WHY_WHY_TA_DURATION"),
    ("xm_ta", "XMatrixTa", "X_MATRIX_TA_DURATION"),
    ("yz_ta", "YamazumiTa", "YAMAZUMI_TA_DURATION"),
    ("zd_ta", "ZeroDefectsTa", "ZERO_DEFECTS_TA_DURATION"),
    ("bd_te", "BurnDownChartTe", "BURN_DOWN_CHART_TE_DURATION"),
    ("ct_te", "CycleTimeStudyTe", "CYCLE_TIME_STUDY_TE_DURATION"),
    ("dt_te", "DesignThinkingTe", "DESIGN_THINKING_TE_DURATION"),
    ("ew_te", "EliminationOfWasteTe", "ELIMINATION_OF_WASTE_TE_DURATION"),
    ("fm_te", "FMEATe", "FMEA_TE_DURATION"),
    ("gb_te", "GembaTe", "GEMBA_TE_DURATION"),
    ("hc_te", "HanchoTe", "HANCHO_TE_DURATION"),
    ("ik_te", "IshikawaTe", "ISHIKAWA_TE_DURATION"),
    ("jd_te", "JidokaTe", "JIDOKA_TE_DURATION"),
    ("kz_te", "KaizenTe", "KAIZEN_TE_DURATION"),
    ("lc_te", "LowCostAutomationTe", "LOW_COST_AUTOMATION_TE_DURATION"),
    ("mm_te", "MudaMuraMuriTe", "MUDA_MURA_MURI_TE_DURATION"),
    ("ni_te", "NextInspectionTe", "NEXT_INSPECTION_TE_DURATION"),
    ("op_te", "OnePointLessonTe", "ONE_POINT_LESSON_TE_DURATION"),
    ("pk_te", "PokaYokeTe", "POKA_YOKE_TE_DURATION"),
    ("qr_te", "QrqcTe", "QRQC_TE_DURATION"),
    ("rc_te", "RootCauseAnalysisTe", "ROOT_CAUSE_ANALYSIS_TE_DURATION"),
    ("sk_te", "SkillMatrixTe", "SKILL_MATRIX_TE_DURATION"),
    ("tt_te", "TaktTimeTe", "TAKT_TIME_TE_DURATION"),
    ("up_te", "UniformProductionTe", "UNIFORM_PRODUCTION_TE_DURATION"),
    ("vs_te", "ValueStreamMappingTe", "VALUE_STREAM_MAPPING_TE_DURATION"),
    ("ww_te", "WhyWhyTe", "WHY_WHY_TE_DURATION"),
    ("xm_te", "XMatrixTe", "X_MATRIX_TE_DURATION"),
    ("yz_te", "YamazumiTe", "YAMAZUMI_TE_DURATION"),
    ("zd_te", "ZeroDefectsTe", "ZERO_DEFECTS_TE_DURATION"),
    ("a3_mr", "A3ProblemSolvingMr", "A3_PROBLEM_SOLVING_MR_DURATION"),
    ("bd_mr", "BurnDownChartMr", "BURN_DOWN_CHART_MR_DURATION"),
    ("ct_mr", "CycleTimeStudyMr", "CYCLE_TIME_STUDY_MR_DURATION"),
    ("dt_mr", "DesignThinkingMr", "DESIGN_THINKING_MR_DURATION"),
    ("ew_mr", "EliminationOfWasteMr", "ELIMINATION_OF_WASTE_MR_DURATION"),
    ("fm_mr", "FMEAMr", "FMEA_MR_DURATION"),
    ("gb_mr", "GembaMr", "GEMBA_MR_DURATION"),
    ("hc_mr", "HanchoMr", "HANCHO_MR_DURATION"),
    ("ik_mr", "IshikawaMr", "ISHIKAWA_MR_DURATION"),
    ("jd_mr", "JidokaMr", "JIDOKA_MR_DURATION"),
    ("kz_mr", "KaizenMr", "KAIZEN_MR_DURATION"),
    ("lc_mr", "LowCostAutomationMr", "LOW_COST_AUTOMATION_MR_DURATION"),
    ("mm_mr", "MudaMuraMuriMr", "MUDA_MURA_MURI_MR_DURATION"),
    ("ni_mr", "NextInspectionMr", "NEXT_INSPECTION_MR_DURATION"),
    ("op_mr", "OnePointLessonMr", "ONE_POINT_LESSON_MR_DURATION"),
    ("rc_mr", "RootCauseAnalysisMr", "ROOT_CAUSE_ANALYSIS_MR_DURATION"),
    ("sk_mr", "SkillMatrixMr", "SKILL_MATRIX_MR_DURATION"),
    ("tt_mr", "TaktTimeMr", "TAKT_TIME_MR_DURATION"),
    ("up_mr", "UniformProductionMr", "UNIFORM_PRODUCTION_MR_DURATION"),
    ("vs_mr", "ValueStreamMappingMr", "VALUE_STREAM_MAPPING_MR_DURATION"),
    ("ww_mr", "WhyWhyMr", "WHY_WHY_MR_DURATION"),
    ("xm_mr", "XMatrixMr", "X_MATRIX_MR_DURATION"),
    ("yz_mr", "YamazumiMr", "YAMAZUMI_MR_DURATION"),
    ("zd_mr", "ZeroDefectsMr", "ZERO_DEFECTS_MR_DURATION"),
    ("pk_kn", "PokaYokeKn", "POKA_YOKE_KN_DURATION"),
    ("a3_kn", "A3ProblemSolvingKn", "A3_PROBLEM_SOLVING_KN_DURATION"),
    ("bd_kn", "BurnDownChartKn", "BURN_DOWN_CHART_KN_DURATION"),
    ("ct_kn", "CycleTimeStudyKn", "CYCLE_TIME_STUDY_KN_DURATION"),
    ("dt_kn", "DesignThinkingKn", "DESIGN_THINKING_KN_DURATION"),
    ("ew_kn", "EliminationOfWasteKn", "ELIMINATION_OF_WASTE_KN_DURATION"),
    ("fm_kn", "FMEAKn", "FMEA_KN_DURATION"),
    ("gb_kn", "GembaKn", "GEMBA_KN_DURATION"),
    ("hc_kn", "HanchoKn", "HANCHO_KN_DURATION"),
    ("ik_kn", "IshikawaKn", "ISHIKAWA_KN_DURATION"),
    ("jd_kn", "JidokaKn", "JIDOKA_KN_DURATION"),
    ("kz_kn", "KaizenKn", "KAIZEN_KN_DURATION"),
    ("lc_kn", "LowCostAutomationKn", "LOW_COST_AUTOMATION_KN_DURATION"),
    ("mm_kn", "MudaMuraMuriKn", "MUDA_MURA_MURI_KN_DURATION"),
    ("ni_kn", "NextInspectionKn", "NEXT_INSPECTION_KN_DURATION"),
    ("op_kn", "OnePointLessonKn", "ONE_POINT_LESSON_KN_DURATION"),
    ("qr_kn", "QrqcKn", "QRQC_KN_DURATION"),
    ("rc_kn", "RootCauseAnalysisKn", "ROOT_CAUSE_ANALYSIS_KN_DURATION"),
    ("sk_kn", "SkillMatrixKn", "SKILL_MATRIX_KN_DURATION"),
    ("tt_kn", "TaktTimeKn", "TAKT_TIME_KN_DURATION"),
    ("up_kn", "UniformProductionKn", "UNIFORM_PRODUCTION_KN_DURATION"),
    ("vs_kn", "ValueStreamMappingKn", "VALUE_STREAM_MAPPING_KN_DURATION"),
    ("ww_kn", "WhyWhyKn", "WHY_WHY_KN_DURATION"),
    ("xm_kn", "XMatrixKn", "X_MATRIX_KN_DURATION"),
    ("yz_kn", "YamazumiKn", "YAMAZUMI_KN_DURATION"),
    ("zd_kn", "ZeroDefectsKn", "ZERO_DEFECTS_KN_DURATION"),
    ("pk_bn", "PokaYokeBn", "POKA_YOKE_BN_DURATION"),
    ("a3_bn", "A3ProblemSolvingBn", "A3_PROBLEM_SOLVING_BN_DURATION"),
    ("bd_bn", "BurnDownChartBn", "BURN_DOWN_CHART_BN_DURATION"),
    ("ct_bn", "CycleTimeStudyBn", "CYCLE_TIME_STUDY_BN_DURATION"),
    ("dt_bn", "DesignThinkingBn", "DESIGN_THINKING_BN_DURATION"),
    ("ew_bn", "EliminationOfWasteBn", "ELIMINATION_OF_WASTE_BN_DURATION"),
    ("fm_bn", "FMEABn", "FMEA_BN_DURATION"),
    ("gb_bn", "GembaBn", "GEMBA_BN_DURATION"),
    ("hc_bn", "HanchoBn", "HANCHO_BN_DURATION"),
    ("ik_bn", "IshikawaBn", "ISHIKAWA_BN_DURATION"),
    ("jd_bn", "JidokaBn", "JIDOKA_BN_DURATION"),
    ("kz_bn", "KaizenBn", "KAIZEN_BN_DURATION"),
    ("lc_bn", "LowCostAutomationBn", "LOW_COST_AUTOMATION_BN_DURATION"),
    ("mm_bn", "MudaMuraMuriBn", "MUDA_MURA_MURI_BN_DURATION"),
    ("ni_bn", "NextInspectionBn", "NEXT_INSPECTION_BN_DURATION"),
    ("op_bn", "OnePointLessonBn", "ONE_POINT_LESSON_BN_DURATION"),
    ("qr_bn", "QrqcBn", "QRQC_BN_DURATION"),
    ("rc_bn", "RootCauseAnalysisBn", "ROOT_CAUSE_ANALYSIS_BN_DURATION"),
    ("sk_bn", "SkillMatrixBn", "SKILL_MATRIX_BN_DURATION"),
    ("tt_bn", "TaktTimeBn", "TAKT_TIME_BN_DURATION"),
    ("up_bn", "UniformProductionBn", "UNIFORM_PRODUCTION_BN_DURATION"),
    ("vs_bn", "ValueStreamMappingBn", "VALUE_STREAM_MAPPING_BN_DURATION"),
    ("ww_bn", "WhyWhyBn", "WHY_WHY_BN_DURATION"),
    ("xm_bn", "XMatrixBn", "X_MATRIX_BN_DURATION"),
    ("yz_bn", "YamazumiBn", "YAMAZUMI_BN_DURATION"),
    ("zd_bn", "ZeroDefectsBn", "ZERO_DEFECTS_BN_DURATION"),
    ("pk_ml", "PokaYokeMl", "POKA_YOKE_ML_DURATION"),
    ("a3_ml", "A3ProblemSolvingMl", "A3_PROBLEM_SOLVING_ML_DURATION"),
    ("bd_ml", "BurnDownChartMl", "BURN_DOWN_CHART_ML_DURATION"),
    ("ct_ml", "CycleTimeStudyMl", "CYCLE_TIME_STUDY_ML_DURATION"),
    ("dt_ml", "DesignThinkingMl", "DESIGN_THINKING_ML_DURATION"),
    ("ew_ml", "EliminationOfWasteMl", "ELIMINATION_OF_WASTE_ML_DURATION"),
    ("fm_ml", "FMEAMl", "FMEA_ML_DURATION"),
    ("gb_ml", "GembaMl", "GEMBA_ML_DURATION"),
    ("hc_ml", "HanchoMl", "HANCHO_ML_DURATION"),
    ("ik_ml", "IshikawaMl", "ISHIKAWA_ML_DURATION"),
    ("jd_ml", "JidokaMl", "JIDOKA_ML_DURATION"),
    ("kz_ml", "KaizenMl", "KAIZEN_ML_DURATION"),
    ("lc_ml", "LowCostAutomationMl", "LOW_COST_AUTOMATION_ML_DURATION"),
    ("mm_ml", "MudaMuraMuriMl", "MUDA_MURA_MURI_ML_DURATION"),
    ("ni_ml", "NextInspectionMl", "NEXT_INSPECTION_ML_DURATION"),
    ("op_ml", "OnePointLessonMl", "ONE_POINT_LESSON_ML_DURATION"),
    ("qr_ml", "QrqcMl", "QRQC_ML_DURATION"),
    ("rc_ml", "RootCauseAnalysisMl", "ROOT_CAUSE_ANALYSIS_ML_DURATION"),
    ("sk_ml", "SkillMatrixMl", "SKILL_MATRIX_ML_DURATION"),
    ("tt_ml", "TaktTimeMl", "TAKT_TIME_ML_DURATION"),
    ("up_ml", "UniformProductionMl", "UNIFORM_PRODUCTION_ML_DURATION"),
    ("vs_ml", "ValueStreamMappingMl", "VALUE_STREAM_MAPPING_ML_DURATION"),
    ("ww_ml", "WhyWhyMl", "WHY_WHY_ML_DURATION"),
    ("xm_ml", "XMatrixMl", "X_MATRIX_ML_DURATION"),
    ("yz_ml", "YamazumiMl", "YAMAZUMI_ML_DURATION"),
    ("zd_ml", "ZeroDefectsMl", "ZERO_DEFECTS_ML_DURATION"),
]
# A lesson joins Root only once it is voiced (its captions exist), so scripts can land early.
LESSONS = [l for l in LESSONS if (HERE / "src/captions" / l[0]).is_dir()]

imports = "\n".join(f'import {{ {c}, {d} }} from "./lessons/{i}/{c}";' for i, c, d in LESSONS)
comps = ""
for i, c, d in LESSONS:
    for suffix, extra in (("", ""), ("Dub", "\n        defaultProps={{ captions: false }}")):
        comps += f"""      <Composition
        id="{c}{suffix}"
        component={{{c}}}
        durationInFrames={{{d}}}
        fps={{fps}}
        width={{width}}
        height={{height}}{extra}
      />
"""
(HERE / "src/Root.tsx").write_text(f"""import React from "react";
import {{ Composition }} from "remotion";
{imports}
import {{ fps, width, height }} from "./theme";

// Indian-language lessons only. Kept apart from course_video/ (the English
// course) so this work never touches the English pipeline.
// Generated by tools/gen_root.py: edit the list there.
export const RemotionRoot: React.FC = () => {{
  return (
    <>
{comps}    </>
  );
}};
""", encoding="utf-8")

p = HERE / "scripts/lessons.ts"
s = p.read_text(encoding="utf-8")
start = s.index("export const PAGE_LESSONS")
end = s.index("};", start) + 2
body = "\n".join(f'  {i}: "{c}",' for i, c, _ in LESSONS)
p.write_text(s[:start] + f"export const PAGE_LESSONS: Record<string, string> = {{\n{body}\n}};" + s[end:], encoding="utf-8")
print(f"Root.tsx + lessons.ts: {len(LESSONS)} lessons")
