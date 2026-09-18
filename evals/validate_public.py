"""Validate the public package without network access or third-party dependencies."""
from pathlib import Path
import hashlib
import json
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "ai-character-design", "ai-creative-workflow-router", "ai-generation-review",
    "ai-prompt-execution-contract", "ai-scene-design", "ai-screenplay-development",
    "ai-storyboard-design", "ai-video-production-classroom",
    "ai-visual-ideation", "ai-worldbuilding",
)
ZH = (
    "镜头编号", "镜头任务", "目标时长", "景别与机位", "画面构图", "起始状态",
    "动作与表演", "时间轴", "摄影机运动", "物理与空间约束", "声音",
    "结束状态", "切点与衔接",
)
KO = (
    "숏 번호", "숏 목적", "목표 길이", "숏 크기와 카메라 위치", "화면 구성",
    "시작 상태", "동작과 연기", "타임라인", "카메라 움직임", "물리·공간 제약",
    "소리", "종료 상태", "컷과 연결",
)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def prompt_errors(block, fields, risk, allow_placeholders=False):
    """Check format only, not creative quality or actual platform behavior."""
    errors = []
    lines = [s.strip() for s in block.splitlines() if s.strip()]
    if not lines or lines[-1] != "无背景音乐":
        errors.append("missing final audio line")
    if lines.count("无背景音乐") != 1:
        errors.append("audio line must appear once per request")
    pattern = re.compile(r"^([^:：]+)[:：]\s*(.*)$")
    pairs = []
    for line in lines:
        if line == "无背景音乐":
            continue
        match = pattern.match(line)
        if not match:
            errors.append("unlabelled content")
        else:
            pairs.append((match[1].strip(), match[2].strip()))
    if not pairs or pairs[0][0] != fields[0]:
        errors.append("request must start with shot ID")
    if not pairs or pairs[-1][0] != risk or not pairs[-1][1]:
        errors.append("missing risk field")
    body = pairs[:-1] if pairs and pairs[-1][0] == risk else pairs
    if not body or len(body) % len(fields):
        errors.append("incomplete shot fields")
    ids = []
    for start in range(0, len(body), len(fields)):
        shot = body[start:start + len(fields)]
        if tuple(key for key, _ in shot) != fields:
            errors.append("incorrect shot field order or duplicate field")
            continue
        ids.append(shot[0][1])
        if any(not value for _, value in shot):
            errors.append("empty field")
        if not allow_placeholders and any(re.search(r"\[[^\]]*\]", value) for _, value in shot):
            errors.append("unfilled placeholder")
    if len(ids) != len(set(ids)):
        errors.append("duplicate shot ID")
    return errors

def sample(fields, risk, ids=("S07",)):
    # Synthetic values exercise structure only; they are not generation-ready prompts.
    lines = []
    for shot_id in ids:
        lines.extend(f"{key}: {shot_id if i == 0 else 'sample content'}"
                     for i, key in enumerate(fields))
    lines.extend((f"{risk}: sample restriction", "无背景音乐"))
    return "\n".join(lines)

class PublicPackageTests(unittest.TestCase):
    def test_skill_inventory_and_frontmatter(self):
        found = sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(found, sorted(SKILLS))
        for name in SKILLS:
            with self.subTest(skill=name):
                text = read(f"skills/{name}/SKILL.md")
                self.assertTrue(text.startswith("---\n"))
                head = text.split("---", 2)[1]
                self.assertIn(f"name: {name}\n", head)
                self.assertRegex(head, r'(?m)^description: ".+"$')
                self.assertIn('  version: "0.7.0"', head)
                self.assertIn("references/usage-rules.md", text)

    def test_common_usage_is_identical(self):
        texts = {read(f"skills/{name}/references/usage-rules.md") for name in SKILLS}
        self.assertEqual(len(texts), 1)
        self.assertIn("../../../shared/common-contract.md", next(iter(texts)))

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if re.match(r"https?://|mailto:|#", target):
                    continue
                rel = target.split("#", 1)[0]
                with self.subTest(file=str(path.relative_to(ROOT)), target=target):
                    resolved = (path.parent / rel).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT.resolve()))
                    self.assertTrue(resolved.is_file())

    def test_korean_navigation(self):
        for path in (
            "README.ko-KR.md", "START_HERE.ko-KR.md",
            "00_通用AI影像制作Skills_总览.ko-KR.md",
            "skills/ai-creative-workflow-router/references/user-guide.ko-KR.md",
            "shared/common-contract.ko-KR.md", "shared/novice-guidance-protocol.ko-KR.md",
        ):
            self.assertRegex(read(path), r"[가-힣]")
        guide = read("skills/ai-creative-workflow-router/references/user-guide.ko-KR.md")
        targets = re.findall(r"\[[^\]]*\]\(([^)]+)\)", guide)
        for target in targets:
            if target == "user-guide.md":  # explicit Chinese-language switch
                continue
            self.assertTrue(".ko-KR.md" in target or target.endswith(("video-template.md", "NOTICE.md")))

    def test_manifests_and_install_target(self):
        root = json.loads(read("plugin.json"))
        plugin = json.loads(read(".codex-plugin/plugin.json"))
        market = json.loads(read(".agents/plugins/marketplace.json"))["plugins"][0]
        for item in (root, plugin, market):
            self.assertEqual(item["name"], "universal-ai-video-production")
            self.assertEqual(item["version"], "0.7.0")
            self.assertEqual(item["license"], "MIT")
        self.assertEqual(plugin["skills"], "./skills/")
        self.assertTrue((ROOT / plugin["skills"]).is_dir())
        self.assertEqual(market["source"]["ref"], "v0.7.0")
        self.assertEqual(market["source"]["url"], root["repository"] + ".git")
        self.assertIn("Copyright (c) 2026 Domain Knowledge Distillation", read("LICENSE"))

    def test_publication_surface(self):
        forbidden = re.compile(
            r"NEEDS_REVIEW|方法论总纲|蒸馏稿|director-decision-layer"
            r"|screenplay-theory-selection-matrix|upstream_versions|recheck_trigger"
            r"|[A-Za-z]:\\|D:/知识库|C:/Users/", re.I)
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertIsNone(forbidden.search(path.read_text(encoding="utf-8")))
        for folder in ("provenance", "research-extension"):
            self.assertFalse(any(p.is_file() for p in (ROOT / folder).rglob("*")))

    def test_bilingual_video_templates(self):
        text = read("skills/ai-prompt-execution-contract/references/video-template.md")
        blocks = re.findall(r"\x60{3}text\n(.*?)\n\x60{3}", text, re.S)
        self.assertEqual(len(blocks), 2)
        for block, fields, risk in zip(blocks, (ZH, KO), ("高风险限制", "주요 오류 방지")):
            self.assertEqual(prompt_errors(block, fields, risk, allow_placeholders=True), [])

    def test_valid_single_and_multiple_shots(self):
        for fields, risk in ((ZH, "高风险限制"), (KO, "주요 오류 방지")):
            for ids in (("S07",), ("S07", "S23"), ("A2", "B9")):
                self.assertEqual(prompt_errors(sample(fields, risk, ids), fields, risk), [])

    def test_rejects_missing_duplicate_and_empty_fields(self):
        good = sample(ZH, "高风险限制")
        cases = [
            good.replace("无背景音乐", ""),
            good + "\nextra",
            good.replace("镜头任务: sample content\n", ""),
            good.replace("镜头任务: sample content", "镜头任务: "),
            good.replace("镜头任务: sample content", "镜头编号: S10"),
            good.replace("镜头编号: S07", "镜头编号: "),
            "请求标识: request\n" + good,
            sample(ZH, "高风险限制", ("S07", "S07")),
            good.replace("画面构图: sample content", "画面构图: [待填]"),
        ]
        for block in cases:
            with self.subTest(block=block):
                self.assertTrue(prompt_errors(block, ZH, "高风险限制"))

    def test_required_templates(self):
        for name in (
            "PROJECT_BRIEF.md", "PROJECT_INDEX.md", "SESSION_HANDOFF.md",
            "AUTHORIZATIONS.md", "DECISIONS.md", "stage-deliverable-template.md",
        ):
            self.assertTrue((ROOT / "templates" / name).is_file())
            self.assertRegex(read("templates/" + name), r"[가-힣]")
        text = read("shared/common-contract.md")
        for name in ("PROJECT_INDEX.md", "SESSION_HANDOFF.md"):
            self.assertIn(name, text)

    def test_release_inventory(self):
        manifest = json.loads(read("CHANGE_MANIFEST.json"))
        self.assertEqual(manifest["package_version"], "0.7.0")
        self.assertEqual(manifest["edition"], "public-lite")
        entries = manifest["files"]
        self.assertEqual(len(entries), len({e["path"] for e in entries}))
        listed = {e["path"] for e in entries}
        actual = {
            p.relative_to(ROOT).as_posix()
            for p in ROOT.rglob("*")
            if p.is_file() and ".git" not in p.parts
            and "__pycache__" not in p.parts
            and p.name != "CHANGE_MANIFEST.json"
        }
        self.assertEqual(actual, listed)
        for entry in entries:
            with self.subTest(file=entry["path"]):
                data = (ROOT / entry["path"]).read_bytes().replace(b"\r\n", b"\n")
                self.assertEqual(len(data), entry["bytes"])
                self.assertEqual(hashlib.sha256(data).hexdigest(), entry["sha256"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
