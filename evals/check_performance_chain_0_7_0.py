#!/usr/bin/env python3
"""Deterministic 0.7.0 wiring checks, not model or video quality tests."""
from pathlib import Path
import json, sys, re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
checks = []
def read(path):
    return (root / path).read_text(encoding="utf-8")
def check(name, passed):
    checks.append({"name": name, "passed": bool(passed)})
routes = {
    "ai-screenplay-development": "performance-beat-and-physical-action.md",
    "ai-prompt-execution-contract": "dialogue-audio-and-lipsync-contract.md",
    "ai-video-production-classroom": "generation-risk-and-shot-feasibility.md",
    "ai-creative-workflow-router": "creative-intent-traceability.md",
}
refs = {}
for owner, ref in routes.items():
    path = f"skills/{owner}/references/{ref}"
    check("route_" + owner, "references/" + ref in read(f"skills/{owner}/SKILL.md") and (root / path).is_file())
    refs[owner] = read(path)
check("performance_limits", all(s in refs["ai-screenplay-development"] for s in ["NEEDS_REVIEW", "不是情绪词典", "无人物", "不能宣布表演验证通过"]))
audio_paths = [
    "skills/ai-prompt-execution-contract/SKILL.md",
    "skills/ai-prompt-execution-contract/references/seedance-student-delivery.md",
    "skills/ai-prompt-execution-contract/references/seedance-formal-request-contract.md",
]
submission_templates = [
    block for path in audio_paths[1:]
    for block in re.findall(r"(?m)^\x60{3}text\n(.*?)^\x60{3}\s*$", read(path), re.S)
]
video_templates = [block for block in submission_templates if "镜头编号：" in block]
shot_fields = ["镜头编号","镜头任务","目标时长","景别与机位","画面构图","起始状态","动作与表演","时间轴","摄影机运动","物理与空间约束","声音","结束状态","切点与衔接"]
def shot_ids(block):
    return [match.group(1).strip() for match in re.finditer(r"(?m)^镜头编号：([^\r\n]*)$", block)]

def nonempty_unique_shot_ids(block):
    ids = shot_ids(block)
    return bool(ids) and all(ids) and len(ids) == len(set(ids))

def text_blocks(document):
    return re.findall(r"(?m)^\x60{3}text\n(.*?)^\x60{3}\s*$", document, re.S)

def titled_templates(document):
    return [
        (int(number), block)
        for number, block in re.findall(
            r"(?ms)^## 镜头\s+(\d+)｜可直接复制\r?\n\x60{3}text\r?\n(.*?)^\x60{3}\s*$",
            document,
        )
    ]
def complete_shots(block):
    shots = re.split(r"(?m)^镜头编号：", block)[1:]
    return nonempty_unique_shot_ids(block) and all(
        all(re.search(r"(?m)^" + re.escape(field) + "：\\S", shot) for field in shot_fields[1:])
        for shot in shots
    )

student_document = read(audio_paths[1])
formal_document = read(audio_paths[2])
student_titled_templates = titled_templates(student_document)
student_blocks = [block for block in text_blocks(student_document) if "镜头编号：" in block]
formal_blocks = [block for block in text_blocks(formal_document) if "镜头编号：" in block]
check("shot_ids_nonempty_unique", all(nonempty_unique_shot_ids(block) for block in video_templates))
check(
    "student_template_title_ids",
    len(student_titled_templates) == 2
    and all(shot_ids(block) == [f"S{number:02d}"] for number, block in student_titled_templates),
)
check(
    "student_independent_context",
    len(student_titled_templates) == 2
    and all(
        all(token in block for token in ["画幅", "视觉风格", "场景"])
        and all(token in block for token in ["主体身份", "外观", "数量", "实际上传参考", "句柄", "读取职责"])
        for _, block in student_titled_templates
    ),
)
check(
    "template_expected_order",
    [shot_ids(block) for block in student_blocks] == [["S01"], ["S02"], ["S01"]]
    and [shot_ids(block) for block in formal_blocks] == [["S01", "S02"]],
)
if formal_blocks:
    negative_duplicate = formal_blocks[0].replace("镜头编号：S02", "镜头编号：S01", 1)
    negative_empty = formal_blocks[0].replace("镜头编号：S01", "镜头编号：", 1)
    negative_order_lines = formal_blocks[0].splitlines()
    negative_order_indexes = [i for i, line in enumerate(negative_order_lines) if line.startswith("镜头编号：")]
    if len(negative_order_indexes) == 2:
        first, second = negative_order_indexes
        negative_order_lines[first], negative_order_lines[second] = negative_order_lines[second], negative_order_lines[first]
    negative_order = "\n".join(negative_order_lines)
else:
    negative_duplicate = negative_empty = negative_order = ""
check(
    "shot_id_negative_cases",
    not nonempty_unique_shot_ids(negative_duplicate)
    and not nonempty_unique_shot_ids(negative_empty)
    and shot_ids(negative_order) != ["S01", "S02"],
)

check("audio_contract", all(s in refs["ai-prompt-execution-contract"] for s in ["同场画外", "可见嘴部", "不能只写", "不自动解决口型", "unconfirmable", "画外动作", "不要重演", "无背景音乐"])
      and all("无背景音乐" in read(path) for path in audio_paths)
      and len(video_templates) == 4
      and all(block.startswith("镜头编号：") and not any(re.search(r"(?m)^" + field + "：", block) for field in ["请求标识", "画幅与视觉风格", "生成时长", "参考素材与职责", "主体与场景"]) and complete_shots(block) and block.rstrip().splitlines()[-1] == "无背景音乐" for block in video_templates)
      and not complete_shots(video_templates[0].replace("起始状态：", "遗漏："))
      and not complete_shots(video_templates[-1].replace("景别与机位：", "遗漏：", 1)))
check("risk_evidence", all(s in refs["ai-video-production-classroom"] for s in ["待测启发式", "不是成功率排序", "停止条件", "需用户确认", "坏尾帧"]))
check("traceability_limits", all(s in refs["ai-creative-workflow-router"] for s in ["一对多、多对一", "needs_recheck", "保护范围", "文字更新不等于视频", "前镜末态", "不能再次发起"]))
for path in ["README", "00_通用AI影像制作Skills_总览", "skills/ai-creative-workflow-router/references/user-guide"]:
    zh, ko = read(path + ".md"), read(path + ".ko-KR.md")
    check("paired_release_" + path, "0.7.0" in zh and "0.7.0" in ko and "未发布" not in zh and "미출시" not in ko)
metadata = json.loads(read("plugin.json"))
legacy = json.loads(read(".codex-plugin/plugin.json"))
stable = json.loads(read(".agents/plugins/marketplace.json"))["plugins"][0]
check("candidate_metadata", metadata["version"] == legacy["version"] == "0.7.0")
release_status = json.loads(read("CHANGE_MANIFEST.json"))["release_status"]
expected_install = {"tag_ready": "0.6.0", "published": "0.7.0"}.get(release_status)
check("stable_marketplace_release_phase", expected_install is not None and stable["version"] == expected_install and stable["source"]["ref"] == "v" + expected_install)
cases = json.loads(read("evals/performance-chain-cases-0.7.0.json"))["evals"]
check("three_distinct_cases", len(cases) == 3 and len({c["id"] for c in cases}) == 3)
check("case_assertions", all(len(c.get("assertions", [])) == 5 for c in cases))
result = {"suite": "performance-chain-0.7.0", "checks": len(checks), "passed": sum(c["passed"] for c in checks), "failed": [c for c in checks if not c["passed"]], "scope": "authored wiring and boundaries only; behavior evaluated separately"}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(bool(result["failed"]))
