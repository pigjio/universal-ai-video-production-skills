# 0.5.0 阶段确认后 Markdown 落盘测试记录

## 结果

**通过。** 已按 `ai-screenplay-development` 0.5.0 的新手引导、阶段确认、版本、授权、回读与交接规则完成一次真实本地 Markdown 落盘事务。

## 执行依据

实际读取并执行：

- `skills/ai-screenplay-development/SKILL.md`
- `skills/ai-screenplay-development/references/novice-guidance-protocol.md`
- `skills/ai-screenplay-development/references/common-contract.md`
- `skills/ai-screenplay-development/references/format-and-handoff.md`
- 项目现有的 `AUTHORIZATIONS.md`、`PROJECT_INDEX.md`、`SESSION_HANDOFF.md` 与 `剧本_v001.md`

## 授权与确认检查

- 阶段对象与范围：剧本阶段，两场完整修订正文。
- 完整成果展示证据：上下文明确说明用户已看到完整修订稿。
- 人工确认原话：`剧本阶段确认完成`。
- 保存授权：`AUTH-SAVE-CONFIRMED: allowed`，仅允许明确确认后的本地新 Markdown 版本，不得覆盖旧版。
- 禁止项：`AUTH-RESEARCH: denied`、`AUTH-UPLOAD: denied`、`AUTH-SPEND: denied`。
- 本次没有执行研究、上传、远端同步、付费、生成、重试、发布、覆盖或删除。

## 执行记录

1. 扫描项目目录，确认剧本最大已有版本为 `v001`，目标新版本应为 `v002`。
2. 在写入前读取 `剧本_v001.md`，并记录 SHA-256：`1aa2336d776812e6f7c45e3c440fc8ee2d5df5df64f87d4e651f8ec6a4513e87`。
3. 新建 `project/剧本_v002.md`，未覆盖 `v001`。
4. 回读 `剧本_v002.md`，核验文件名与标题为 `v002`、状态为 `confirmed`，两场正文完整存在，并包含已定、上游与版本关系、未决项和边界。
5. 更新 `project/PROJECT_INDEX.md`，登记当前采用版本、相对路径、状态、修订基线、确认依据、未决项和下一步。
6. 更新 `project/SESSION_HANDOFF.md`，登记已完成/未执行事项、人工决定、连续性、未决项、禁止推断、下一小步和恢复入口。
7. 回读 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`，核验二者均指向 `剧本_v002.md`（confirmed），且边界一致。
8. 再次回读并校验 `剧本_v001.md`；其 SHA-256 仍为 `1aa2336d776812e6f7c45e3c440fc8ee2d5df5df64f87d4e651f8ec6a4513e87`，确认旧版未变。

## 回读自检

- [x] `剧本_v001.md` 保留且内容未变。
- [x] 新建的是下一未占用版本 `剧本_v002.md`。
- [x] `剧本_v002.md` 可独立阅读，含两场完整正文。
- [x] 场景一包含：车站夜、小岚攥未寄出的信、末班车驶过、没有追。
- [x] 场景二包含：候车室夜、信投入退信箱、摘下旧车票夹在空白页中、主动走向出口。
- [x] 主文件状态为 `confirmed`，确认依据真实可定位。
- [x] 主文件明确记录上游/版本关系、未决项和授权边界。
- [x] `PROJECT_INDEX.md` 当前版本、路径、状态与主文件一致。
- [x] `SESSION_HANDOFF.md` 当前版本、人工决定、连续性和下一步与主文件一致。
- [x] 三个文件均已实际回读。
- [x] 未扩大授权到研究、上传、付费、生成、发布、覆盖或删除。

## 文件路径与最终校验值

- 新建：`evals/runs/novice-0.5.0/case-2-stage-save/project/剧本_v002.md`
  - SHA-256：`4352f5c1307c38e7ac6497a5c120c9cc75639b09eeffb7bd859c1ad7f23617f3`
- 更新：`evals/runs/novice-0.5.0/case-2-stage-save/project/PROJECT_INDEX.md`
  - SHA-256：`002486445641d8097d72bf015a9ba21faeadfb65c9d53cf6e24ffba08f020e4c`
- 更新：`evals/runs/novice-0.5.0/case-2-stage-save/project/SESSION_HANDOFF.md`
  - SHA-256：`97a6ea5f2a4b587cbfc9c48a265050eadaea6cee080c9be0f6d50d905bad867e`
- 保留未改：`evals/runs/novice-0.5.0/case-2-stage-save/project/剧本_v001.md`
  - 写前/写后 SHA-256：`1aa2336d776812e6f7c45e3c440fc8ee2d5df5df64f87d4e651f8ec6a4513e87`
- 本记录：`evals/runs/novice-0.5.0/case-2-stage-save/output.md`

## 问题

- 无阻断问题。
- 一次校验命令因工具不接受含中文字符的 `workdir` 参数而被阻止；随后改用不含中文的工作目录并对目标使用绝对路径重试成功，不影响任何项目文件或测试结果。
