# 通用 AI 影像制作 Skills｜0.7.0 总览

[中文说明](00_通用AI影像制作Skills_总览.md)｜[한국어 안내](00_通用AI影像制作Skills_总览.ko-KR.md)

0.7.0 由十个专业 Skill、两份共享协议、六个项目模板和三层使用深度组成。默认面向从未使用过 Agent 的普通创作者；复杂度由 Agent 在内部承担，专业判断、证据和人工裁决不降级。本版重点补齐类型与理论选型、具体景别语言、模糊反馈局部修订，以及面向 Seedance / 即梦的可复制交付。

## 0.7.0 使用变化

学生不需要学理论或填写追踪表，只需自然地说想改什么，由 Agent 在内部完成以下判断。

- **表演：**把情绪名称转成接收刺激、采取行动、调整或坚持的过程，让停顿、视线和物件动作呈现选择，而不是套用“难过就低头”。
- **声音：**区分对白原文、说话者、听者、可见口部和声音起止。画外人物对白不偷换成旁白；能力未知时给后期方案，不承诺配音自动解决口型。
- **生成风险：**解释精细接触、多动作等风险，比较保留故事含义的替代拍法；真实平台测试需单独授权。
- **局部修改：**追踪剧本意图到镜头和提示词的关联，明确受影响与不变内容。发生冲突先说明，不擅改受保护镜头。

可以直接说：“不要解释情绪，用动作让我看懂。” / “这句台词拍听的人。” / “只改第二镜，后面有冲突先告诉我。”

**v0.7.0 已发布，Marketplace 安装入口指向 v0.7.0。** 经用户要求，角色概念提示词修订已合入同一版本，v0.7.0 标签已更新；已安装或缓存旧内容的用户需要重新获取。真实视频生成、学生使用体验与艺术满意度仍需另外验证。

## 用户看到的工作方式

```text
用户自然描述
→ Agent识别当前入口和阶段
→ 每轮完成一个小目标
→ 用户比较、否决或确认
→ 阶段完整成果展示
→ 用户明确确认阶段完成
→ 按有效授权保存新的完整Markdown版本
→ 回读 + 更新PROJECT_INDEX与SESSION_HANDOFF
→ 进入下一阶段或跨会话恢复
```

“不错、继续、方向可以”不构成阶段完成。保存作品也不构成上传、生成、发布或研究同意。

## 十个 Skill

| Skill | 面向用户的职责 | 阶段主文件 |
|---|---|---|
| [ai-creative-workflow-router](skills/ai-creative-workflow-router/SKILL.md) | 唯一新手入口、跨阶段路由、恢复、授权与最小回退 | `项目简报_vNNN.md` |
| [ai-visual-ideation](skills/ai-visual-ideation/SKILL.md) | 从模糊想法形成可比较创意方向 | `创意核心_vNNN.md` |
| [ai-screenplay-development](skills/ai-screenplay-development/SKILL.md) | 剧本、动作谱、场景链、对白、诊断与改写 | `剧本_vNNN.md` |
| [ai-worldbuilding](skills/ai-worldbuilding/SKILL.md) | 世界规则、材料机制、空间时间与一致性 | `世界观设定_vNNN.md` |
| [ai-character-design](skills/ai-character-design/SKILL.md) | 角色概念、造型、表演与生产资产 | `角色设计_名称_vNNN.md` |
| [ai-scene-design](skills/ai-scene-design/SKILL.md) | 场景拓扑、构图、光色、材质与状态派生 | `场景设计_名称_vNNN.md` |
| [ai-storyboard-design](skills/ai-storyboard-design/SKILL.md) | Beat、观看顺序、调度、节奏与连续性 | `分镜_场次_vNNN.md` |
| [ai-prompt-execution-contract](skills/ai-prompt-execution-contract/SKILL.md) | 静态/视频生成合同和 Seedance 正式请求 | `生成请求_对象_vNNN.md` |
| [ai-video-production-classroom](skills/ai-video-production-classroom/SKILL.md) | 生产组、平台请求、续接、真实状态与剪辑交付 | `视频生产计划_vNNN.md` |
| [ai-generation-review](skills/ai-generation-review/SKILL.md) | 真实媒体证据、十维评审、诊断、修复与回归 | `生成评审_对象_vNNN.md` |

## 三种交互模式

- **新手**：默认，普通语言，每轮一个小目标。
- **协作**：共同比较方案，解释必要取舍。
- **专业**：显示完整字段、状态、依赖和生产交接。

交互模式不等于工作深度。讨论、探索草案、正式成稿、生产交接/验证仍分别管理。

## 三层使用深度

- **production**：默认，完成实际创作和生产。
- **provenance**：按需查看方法来源、证据等级和迁移边界。
- **research**：只有明确研究同意后启用；生产快照可被研究层只读引用，研究层不得反写生产确认状态。

## 专业生产链

```text
已确认 storyboard shots
→ production_group / Clip / DO
→ generation_request
→ 真实平台提交与原始 output
→ 十维 review
→ edit_unit
→ 人工裁决与交付
```

计划、写稿、保存、提交、返回、机器评审和人工接受是不同状态。

学生端的简化出口是：**满意的剧本 → 有剧本依据的分镜 → 可直接复制的逐镜 Seedance 提示词**。理论只在后台参与判断，用户追问时才解释依据与边界。

## 文件和恢复

项目模板位于 `templates/`。每次完整落盘必须创建新版本、回读主文件，并更新、回读 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`。新会话先读取 `AUTHORIZATIONS.md`、索引、交接和实际成果，不凭记忆猜最新版。

## 验证边界

静态验证只证明结构和规则闭合；Agent 文本/文件测试只证明受测路径中的行为；真实生成、艺术质量和外部新手可用性必须分别验证。
