# 通用 AI 影像制作 Skills｜0.5.0 新手引导与阶段落盘版

当前版本：**0.5.0**。本版以 0.4.0 Seedance 生产融合版为稳定专业基线，不削减创意、剧本、世界观、角色、场景、分镜、提示词、视频生产和生成评审知识；主要改进是把方法转成第一次使用 Agent 的创作者也能跟随的逐轮协作系统，并在每个明确确认完成的阶段保存完整本地 Markdown 成果。

## 从哪里开始

- 普通用户：先看 [`START_HERE.md`](START_HERE.md)，或直接用自然语言告诉 Agent 自己有什么。
- Codex：项目根的 [`AGENTS.md`](AGENTS.md) 会让 Agent 使用同一套规则。
- Claude Code：项目根的 [`CLAUDE.md`](CLAUDE.md) 会让 Agent 使用同一套规则。
- 方法总控：[`skills/ai-creative-workflow-router/SKILL.md`](skills/ai-creative-workflow-router/SKILL.md)。用户无需记住 Skill 名。
- 统一新手协议：[`shared/novice-guidance-protocol.md`](shared/novice-guidance-protocol.md)。
- 公共状态、授权和阶段落盘协议：[`shared/common-contract.md`](shared/common-contract.md)。

## 0.5.0 的核心变化

1. **外简内严**：用户只需描述、比较、否决和确认；Agent 管理术语、阶段、依赖、版本与文件。
2. **三种交互模式**：新手模式默认；可切换协作或专业模式，不改变专业质量门槛。
3. **首轮四入口**：模糊想法、已有故事/剧本、已有图片、生成效果不对；不先展示十个 Skill。
4. **每轮一个小目标**：最多一个阻断问题；“不知道”合法；首轮必须有小产出。
5. **确认语义隔离**：推荐、积极反馈、阶段确认、保存、生产提交、人工接受和研究同意互不替代。
6. **阶段成果落盘**：用户明确确认阶段完成后，按有效保存授权创建新的完整 Markdown 版本，不只保存摘要，不覆盖旧版。
7. **落盘事务验证**：写后回读，并更新、回读 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`；任一步失败只能报告部分完成或未完成。
8. **跨会话恢复**：先读授权、索引、交接和实际成果文件，不凭聊天记忆猜最新版。
9. **多入口适配**：提供 `START_HERE.md`、`AGENTS.md`、`CLAUDE.md` 与可复制项目模板。
10. **三层深度**：production 默认；provenance 按需；research 必须明确单独启用，不能反向修改生产确认状态。

## 阶段主文件

| 阶段 | 默认主文件 |
|---|---|
| 项目启动 | `项目简报_vNNN.md` |
| 创意 | `创意核心_vNNN.md` |
| 剧本 | `剧本_vNNN.md` |
| 世界观 | `世界观设定_vNNN.md` |
| 角色 | `角色设计_名称_vNNN.md` |
| 场景 | `场景设计_名称_vNNN.md` |
| 分镜 | `分镜_场次_vNNN.md` |
| 提示词/正式请求 | `生成请求_对象_vNNN.md` |
| 视频生产 | `视频生产计划_vNNN.md` |
| 生成评审 | `生成评审_对象_vNNN.md` |

文件名只是默认；项目可采用自己的命名约定，但必须保留状态、版本、不覆盖和可追溯原则。

## 项目初始化

普通新手不需要手工复制模板。第一次确认并授权保存、且项目目录明确后，Agent 自动从 `templates/` 创建缺失的五个基础记录文件：

- `PROJECT_BRIEF.md`
- `PROJECT_INDEX.md`
- `SESSION_HANDOFF.md`
- `DECISIONS.md`
- `AUTHORIZATIONS.md`

`stage-deliverable-template.md` 仅供 Agent 内部组织完整阶段成果，不要求复制到用户项目。已有文件不会被空模板覆盖；未知信息保持“未知/暂无”。

项目首次可明确授权：“每个阶段在我明确确认后，自动保存一个新的本地 Markdown 完整版本并更新索引和交接；不得覆盖旧版。”该授权不包括草稿保存、覆盖、上传、付费、生成、发布或研究。

## 已保留的 0.4.0 专业能力

- `shot → production_group/Clip/DO → generation_request → edit_unit` 四层生产模型；
- Seedance/即梦正式请求、逐镜字段、素材职责、状态接力与容量压缩；
- 平台能力按来源和核验条件分层，不把固定时长或槽位当永久规则；
- planned、submitted、generated、reviewed 与人工接受的证据门；
- 身份、空间、几何、动作、方向、道具、摄影、信息边界、声音、尾帧十维评审；
- 竞争性根因、最小测试、局部修复、上游改版传播与回归保护。

## 校验

在包根运行：

```bash
python evals/validate_package.py .
```

静态校验检查 10 个 Skill 的版本和引用、两套协议副本一致性、项目模板、公共 schema、递归资源和私有路径泄漏。新手案例规格见 `evals/novice-cases-0.5.0.md`。

## 证据边界

本版可以分别报告：

- 结构与静态验证；
- 已保存证据的 Agent 文本/文件工作流；
- 真实平台提交与媒体观察；
- 外部新手使用反馈和人工质量裁决。

前两项通过不能证明真实 Seedance 生成质量、成功率提升、随机种子稳定性或外部用户可用性。0.4.0 测试材料在本包中仅作为历史基线；当前发布状态以 0.5.0 源文件、验证报告和变更清单为准。