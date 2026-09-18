---
name: ai-creative-workflow-router
description: "从想法、剧本、图片或生成问题开始，协调 AI 短片创作。한국어 영상 제작 요청도 단계에 맞게 안내합니다。"
metadata:
  version: "0.7.0"
  author: Domain Knowledge Distillation
  license: MIT
---

# AI 影像创作入口

先读取 [使用约定](references/usage-rules.md)。用户不需要记住或手动选择技能。

## 选择当前工作

按用户当前需求读取同包对应 SKILL.md，已有成果不重做；无关阶段可跳过。

| 需求 | 内部入口 |
|---|---|
| 只有想法或想比较方向 | [创意](../ai-visual-ideation/SKILL.md) |
| 大纲、详细剧本或对白 | [剧本](../ai-screenplay-development/SKILL.md) |
| 必要的世界设定 | [世界观](../ai-worldbuilding/SKILL.md) |
| 角色与 Midjourney 角色概念 | [角色](../ai-character-design/SKILL.md) |
| 场景与 Midjourney 场景概念 | [场景](../ai-scene-design/SKILL.md) |
| 分镜文字 | [分镜](../ai-storyboard-design/SKILL.md) |
| 可复制的图像／Seedance 提示词 | [提示词](../ai-prompt-execution-contract/SKILL.md) |
| 生成安排、素材准备与续接 | [视频生产](../ai-video-production-classroom/SKILL.md) |
| 实际生成结果的检查与修改 | [结果评审](../ai-generation-review/SKILL.md) |

先回应当前目标，再建议一个下一步。已有资料够用时直接试写；缺口会明显改变方向时才询问。

大纲或详细剧本完整稿讨论收口后，按剧本技能询问是否需要角色／场景清单与概念图提示词，或继续修改。用户拒绝、延后或已经指定下一步时不重复询问。

使用说明：[中文](references/user-guide.md) / [한국어](references/user-guide.ko-KR.md)。
