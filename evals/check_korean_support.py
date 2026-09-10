#!/usr/bin/env python3
"""Deterministic Korean discovery and authorization regression checks."""
from pathlib import Path
import json, re, sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    raise SystemExit("Dependency missing: install PyYAML with python -m pip install pyyaml")

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "evals/korean-cases-0.5.1.json").read_text(encoding="utf-8"))
PROTOCOL = (ROOT / "shared/novice-guidance-protocol.md").read_text(encoding="utf-8")
checks = []

def add(name, ok, evidence):
    checks.append({"name": name, "passed": bool(ok), "evidence": evidence})

route_cases = CASES.get("route_cases", [])
behavior_cases = CASES.get("behavior_cases", [])
add("ten_korean_route_cases", len(route_cases) == 10, "one Korean discovery case exists for every bundled skill")
add("six_korean_behavior_cases", len(behavior_cases) == 6, "unknown, feedback, confirmation, save, research, and recovery are covered")

skill_names = set()
for case in route_cases:
    skill = case.get("expected_skill", "")
    path = ROOT / "skills" / skill / "SKILL.md"
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    try:
        frontmatter = yaml.safe_load(text.split("---", 2)[1]) if text else {}
    except Exception:
        frontmatter = {}
    description = frontmatter.get("description", "") if isinstance(frontmatter, dict) else ""
    skill_names.add(skill)
    add(f"{case['id']}_discoverable", case.get("trigger_fragment", "") in description, f"Korean trigger is present in {skill} description")
    add(f"{case['id']}_version", frontmatter.get("version") == "0.5.1", f"{skill} declares version 0.5.1")
    add(f"{case['id']}_description_limit", len(description) <= 1024, f"{skill} description remains within the discovery limit")

add("route_skills_unique", len(skill_names) == 10, "route cases cover ten distinct skill identifiers")
for marker in [
    "默认使用用户当前主要语言回答",
    "잘 모르겠어요 / 모르겠습니다 / 먼저 추천해 주세요",
    "좋아요 / 계속해 주세요 / 방향이 맞아요",
    "이 단계를 확정합니다",
    "새 버전으로 저장해 주세요",
    "아직 저장하지 마세요 / 업로드하지 마세요 / 연구에 사용하지 마세요",
]:
    add(f"protocol_marker_{len(checks)}", marker in PROTOCOL, f"shared protocol contains Korean semantic marker: {marker}")

for skill in sorted(skill_names):
    copy = ROOT / "skills" / skill / "references" / "novice-guidance-protocol.md"
    add(f"{skill}_protocol_sync", copy.is_file() and copy.read_text(encoding="utf-8") == PROTOCOL, f"{skill} uses the canonical multilingual novice protocol")

readme = (ROOT / "README.ko-KR.md").read_text(encoding="utf-8")
add("korean_readme_starter", "이 AI 영상 제작 Skills를 처음 사용합니다" in readme, "Korean README includes a copyable natural-language starter")
add("korean_readme_feedback_boundary", "단계 확정 또는 저장 권한으로 간주하지 않습니다" in readme, "Korean README explains that positive feedback is not authorization")
add("behavior_ids_unique", len({c.get('id') for c in behavior_cases}) == len(behavior_cases), "Korean behavior case identifiers are unique")

result = {
    "suite": CASES.get("suite"),
    "checks": len(checks),
    "passed": sum(item["passed"] for item in checks),
    "failed": [item for item in checks if not item["passed"]],
    "details": checks,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if result["failed"] else 0)
