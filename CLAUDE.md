# Claude Code 项目入口

开始工作前依次读取：

1. `START_HERE.md`
2. `shared/novice-guidance-protocol.md`
3. `shared/common-contract.md`
4. 当前项目的 `PROJECT_BRIEF.md`、`AUTHORIZATIONS.md`、`PROJECT_INDEX.md`、`SESSION_HANDOFF.md`（若存在）

执行要求：

- 不让用户先选 Skill；用自然语言识别四个入口并内部路由。
- 默认新手模式，一轮一个小目标，最多问一个真正阻断的问题；接受“不知道”。
- 用户只负责描述、比较、否决和确认；不要把推荐、积极反馈或“继续”升级成确认。
- 区分讨论、探索、正式成稿和生产交接。
- 阶段成熟时主动用一个问题提供“确认并保存 / 确认但不保存 / 继续修改”；confirmed 落盘需要明确阶段确认和有效保存授权，draft/candidate 落盘也要明确授权。
- 保存完整 Markdown 成果，默认写新版本而非覆盖；首次保存时自动从 `templates/` 创建缺失的五个基础记录文件，不要求用户手工复制或填写内部字段；回读验证后更新并回读 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`。任何失败都必须如实报告。
- 阶段保存授权不包含覆盖、上传、花费、发布或研究。研究默认 denied，需单独启用且不能反向修改 production 确认状态。
- production 默认启用；provenance 仅按需记录；research-extension 按独立同意启用。

如需领域方法，可读取相应 `skills/*/SKILL.md` 及 references；不要要求用户记住目录或技能名。
