#!/usr/bin/env python3
"""Deterministic checks for the three preserved 0.5.0 novice workflow runs."""
from pathlib import Path
import hashlib, json, sys

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
RUN = ROOT / "evals/runs/novice-0.5.0"
checks = []

def add(name, ok, evidence):
    checks.append({"name": name, "passed": bool(ok), "evidence": evidence})

def text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

cold = text("evals/runs/novice-0.5.0/case-1-cold-start/output.md")
add("cold_start_has_concrete_output", "核心一句话" in cold and "微型画面" in cold, "cold-start output contains a core sentence and micro-scene")
add("cold_start_accepts_unknown", "不知道" in cold and "Agent 暂定假设" in cold, "unknown is accepted and assumptions are labeled")
add("cold_start_does_not_save_project", "是否落盘：**否" in cold, "run self-check records no project artifact write")

project = RUN / "case-2-stage-save/project"
v1 = project / "剧本_v001.md"; v2 = project / "剧本_v002.md"
add("old_version_preserved", v1.exists() and hashlib.sha256(v1.read_bytes()).hexdigest()=="1aa2336d776812e6f7c45e3c440fc8ee2d5df5df64f87d4e651f8ec6a4513e87", "v001 exists with preserved pre-run hash")
v2t = v2.read_text(encoding="utf-8")
add("new_complete_confirmed_version", v2.exists() and "lifecycle_status: confirmed" in v2t and "场景一" in v2t and "场景二" in v2t and "## 正文" in v2t, "v002 is an independently readable two-scene confirmed script")
idx = (project / "PROJECT_INDEX.md").read_text(encoding="utf-8")
hand = (project / "SESSION_HANDOFF.md").read_text(encoding="utf-8")
add("index_points_to_v002", "剧本_v002.md" in idx and "confirmed" in idx, "project index points to confirmed v002")
add("handoff_points_to_v002", "剧本_v002.md" in hand and "confirmed" in hand, "session handoff points to confirmed v002")
add("research_stays_denied", "AUTH-RESEARCH: denied" in text("evals/runs/novice-0.5.0/case-2-stage-save/project/AUTHORIZATIONS.md"), "research authorization remains denied")

fallback = text("evals/runs/novice-0.5.0/case-3-capability-fallback/output.md")
add("fallback_delivers_request", "完整可复制的 Seedance 请求骨架" in fallback and "外部执行后的回传清单" in fallback, "request skeleton and return checklist are present")
add("fallback_does_not_fake_execution", "returned_task_id: null" in fallback and "result_file_or_url: null" in fallback and "请求状态: planned" in fallback, "execution identifiers/results remain empty and planned")
add("media_limits_are_explicit", fallback.count("unconfirmable") >= 5 and "声音" in fallback and "动作连续性" in fallback, "unobservable sound and motion continuity remain unconfirmable")

result = {"suite": "novice-0.5.0", "checks": len(checks), "passed": sum(c["passed"] for c in checks), "failed": [c for c in checks if not c["passed"]], "details": checks}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if result["failed"] else 0)
