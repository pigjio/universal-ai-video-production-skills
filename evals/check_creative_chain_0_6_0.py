#!/usr/bin/env python3
"""Deterministic checks for the 0.6.0 creative discussion chain.

These checks validate authored rules and routing. They do not invoke a model,
submit to Seedance, assess artistic quality, or represent student acceptance.
"""
from pathlib import Path
import json, re, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
EXPECTED_VERSION = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]
checks = []

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

def add(name, passed, evidence):
    checks.append({"name": name, "passed": bool(passed), "evidence": evidence})

screenplay = read("skills/ai-screenplay-development/SKILL.md")
storyboard = read("skills/ai-storyboard-design/SKILL.md")
prompt = read("skills/ai-prompt-execution-contract/SKILL.md")
router = read("skills/ai-creative-workflow-router/SKILL.md")
theory = read("skills/ai-screenplay-development/references/screenplay-theory-selection-matrix.md")
genre = read("skills/ai-screenplay-development/references/genre-conventions-and-promises.md")
revision = read("skills/ai-screenplay-development/references/collaborative-revision-cases.md")
taxonomy = read("skills/ai-storyboard-design/references/shot-language-taxonomy.md")
delivery = read("skills/ai-prompt-execution-contract/references/seedance-student-delivery.md")

routes = {
    "screenplay-theory-selection-matrix.md": screenplay,
    "genre-conventions-and-promises.md": screenplay,
    "collaborative-revision-cases.md": screenplay,
    "shot-language-taxonomy.md": storyboard,
    "seedance-student-delivery.md": prompt,
}
for name, body in routes.items():
    add("route_" + name, "references/" + name in body, name + " is explicitly routed from its skill")

add("theory_selection_contract", all(x in theory for x in ["当前问题", "不适用", "最小使用强度", "一套主工具"]), "theory selection is problem-led and bounded")
add("theory_cross_book_boundary", "跨书综合" in theory and "不是任何一本书的原表" in theory, "matrix does not claim single-book provenance")
add("genre_decision_fields", all(x in genre for x in ["观众期待", "核心压力机制", "必须兑现", "高潮机制", "常见俗套", "短片压缩"]), "genre package covers production-relevant judgments")
add("genre_limited_coverage", "有限覆盖" in genre and "不宣称" in genre, "traditional genre coverage is not overstated")
add("shot_size_categories", all(re.search(r"\|\s*" + x + r"\s*\|", taxonomy) for x in ["ELS", "LS", "WS", "MS", "MCU", "CU", "ECU"]), "seven shot-size categories are explicit")
add("viewpoint_categories", all(x in taxonomy for x in ["客观镜头", "主观镜头", "POV", "OTS"]), "objective, subjective, POV and OTS are distinguished")
add("script_basis_chain", "从剧本到分镜的依据链" in taxonomy and all(x in taxonomy for x in ["场景功能", "Reaction/Decision", "首次揭示"]), "shots must trace to screenplay evidence")
add("local_revision_examples", all(x in revision for x in ["太普通", "不够电影感", "人物不对", "这一段太慢", "镜头太碎", "动作生成很乱", "只改第三镜"]), "seven common feedback paths are covered")
add("protected_scope", "受保护" in revision and "只改受影响" in revision, "confirmed and unaffected content is protected")

delivery_fields = ["镜头编号", "镜头任务", "目标时长", "景别与机位", "画面构图", "起始状态", "动作与表演", "时间轴", "摄影机运动", "物理与空间约束", "声音", "结束状态", "切点与衔接", "高风险限制"]
add("seedance_structured_contract", all(x + "：" in delivery for x in delivery_fields), "student delivery explicitly expands the former ten-part contract into labeled shot fields without a request header")
add("copy_first_delivery", all(x in delivery for x in ["使用说明", "参考素材绑定", "可直接复制", "连续生成与尾帧接力", "生成失败时优先修改什么"]), "student-facing output leads with usable blocks")
add("honest_generation_boundary", all(x in delivery for x in ["不能说已上传", "不能说已生成", "未观看视频"]), "prompt completion is separated from platform results")
add("three_outputs", all(x in router for x in ["满意的剧本", "有剧本依据的分镜", "可直接复制的 Seedance/即梦提示词"]), "router names the three student outcomes")

zh = read("skills/ai-creative-workflow-router/references/user-guide.md")
ko = read("skills/ai-creative-workflow-router/references/user-guide.ko-KR.md")
add("bilingual_version", EXPECTED_VERSION in zh and EXPECTED_VERSION in ko, f"Chinese and Korean guides declare {EXPECTED_VERSION}")
add("bilingual_three_outputs", "讨论到满意的剧本" in zh and "만족할 때까지 논의한 시나리오" in ko and "바로 복사" in ko, "both guides expose the same three-result path")

skill_versions = []
for f in (ROOT / "skills").glob("*/SKILL.md"):
    m = re.search(r"^version:\s*(\S+)", f.read_text(encoding="utf-8"), re.M)
    skill_versions.append((f.parent.name, m.group(1) if m else None))
add("ten_skill_versions", len(skill_versions) == 10 and all(v == EXPECTED_VERSION for _, v in skill_versions), f"all ten skills declare version {EXPECTED_VERSION}")

scan_ext = {".md", ".json", ".py", ".yaml", ".yml", ".txt"}
leaks = []
needle_parts = [("D:" + "\\" + "知识库"), ("/mnt/" + "d/知识库"), ("jio" + "jio的知识库")]
for f in ROOT.rglob("*"):
    if ".git" in f.parts or not f.is_file() or f.suffix.lower() not in scan_ext or f.name == Path(__file__).name:
        continue
    data = f.read_text(encoding="utf-8", errors="replace")
    if any(n in data for n in needle_parts):
        leaks.append(str(f.relative_to(ROOT)))
add("no_private_knowledge_path", not leaks, "no private knowledge-base path or owner-specific marker is published" if not leaks else ", ".join(leaks))

case_data = json.loads(read("evals/creative-chain-cases-0.6.0.json"))
add("eight_representative_cases", len(case_data.get("cases", [])) == 8 and len({c["id"] for c in case_data["cases"]}) == 8, "eight unique representative prompts are documented")

result = {
    "suite": "creative-chain-0.6.0",
    "checks": len(checks),
    "passed": sum(c["passed"] for c in checks),
    "failed": [c for c in checks if not c["passed"]],
    "details": checks,
    "scope": "deterministic authored-content, routing, bilingual parity, version, and privacy checks only"
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if result["failed"] else 0)
