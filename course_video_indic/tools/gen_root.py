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
]
# A lesson joins Root only once it is voiced (its captions exist), so scripts can land early.
LESSONS = [l for l in LESSONS if (HERE / "src/captions" / l[0]).is_dir()    ("ik_te", "IshikawaTe", "ISHIKAWA_TE_DURATION"),
    ("jd_te", "JidokaTe", "JIDOKA_TE_DURATION"),
    ("kz_te", "KaizenTe", "KAIZEN_TE_DURATION"),
    ("lc_te", "LowCostAutomationTe", "LOW_COST_AUTOMATION_TE_DURATION"),
]

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
