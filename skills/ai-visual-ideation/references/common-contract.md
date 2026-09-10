# 公共交接、阶段确认与执行协议

协议版本：0.5.0。每个技能携带本文与 `novice-guidance-protocol.md` 的逐字一致副本；发布时核验，不依赖特定机器上的共享目录。

## 0. 工作深度与专业协议的适用范围

`interaction_mode` 是对话层概念，不加入公共 YAML。新手、协作、专业三种交互方式见 `novice-guidance-protocol.md`。无论哪种交互方式，都必须区分以下工作深度：

- **讨论**：直接回答当前问题、给具体判断或局部试写；允许未知与不收敛，不要求完整公共头、候选状态、锁定母版、生产测试或落盘。
- **探索草案**：允许可替换假设、联动候选和比较；明确标暂定，不冒充批准或正式 candidate。
- **正式成稿**：只完整交付用户指定范围；输入足够时直接写，不以不断追问替代创作。成稿仍须用户确认才成为 confirmed。
- **生产交接/验证**：进入受管理产物、外部执行、上游换版或证据审查时，执行本文全部公共头、授权、证据和依赖闸门。

共同循环是：当前意图 → 直接判断/具体试写 → 必要时少量替代与代价 → 吸收反馈 → 只改受影响项。授权规则与执行进度分开；讨论不落盘不等于禁止在对话中形成有用草案。

## 1. 公共头与域内容分离

生产交接/验证及明确要求登记的正式产物以公共头开头，具体设计与表格放 payload。讨论、探索和仅供阅读的局部成稿不强制公共头。

```yaml
artifact_id: ART-example
version: v1
artifact_type: idea
creative_mode: narrative
subject_type: character-led
lifecycle_status: draft
production_status: not_applicable
approval_level: none
upstream_versions: {}
confirmed_evidence: []
open_questions: []
recheck_trigger: []
next_action: request_review
payload: {}
```

- `artifact_id`：逻辑产物的稳定 ID，不含版本；`version` 单独递增。技能版本不是产物版本。
- `artifact_type`：idea / script / world / character / scene / storyboard / prompt / clip / review。
- `creative_mode`：narrative / perceptual / conceptual。改变模式是创作变更，不可由下游擅自转换。
- `subject_type`：character-led / environment-led / object-led / abstract；无人物时 `payload.character` 为 null，人物字段标“不适用”。
- `lifecycle_status`：draft / candidate / confirmed / needs_recheck / invalidated。
- `production_status`：not_applicable / not_started / planned / awaiting_external_generation / submitted / generated / under_review / reviewed / failed。
- `approval_level`：none / direction_approved / production_approved / human_confirmed。
- `upstream_versions`：稳定 ID 到明确版本的映射，不写“最新版”。
- `confirmed_evidence`：真实人工选择或核验依据；没有就留空，不能编造。
- `open_questions`、`recheck_trigger`、`next_action`：分别记录未决问题、复核触发条件和下一步。

### 未知输入与局部审查

模式、主体、原记录或版本未提供时不要猜。允许在 `draft` 或 `needs_recheck` 的诊断记录中显式置 null，并在 `payload.record_completeness` 写 `incomplete`、在 `open_questions` 列出缺口、`approval_level` 置 `none`。这是合法接收/诊断记录，不是可放行的正式生产交接。进入正式 candidate/confirmed 或生产提交前，补齐适用枚举与依赖版本；未拿到原记录时输出差异补丁/影响报告，不伪造完整旧头。

## 2. 状态与人工裁决不可互相替代

方向确认不代表生产母版通过；提示词通过不代表请求已发；返回文件不代表通过评审；机器通过不代表人工接受；人工接受局部不代表全部入 Canon；文件已保存也不代表内容已确认。

正式候选必须满足公共协议要求；探索中的方向、局部试写、输入未齐内容仍是草案。拒绝当前候选可保持 candidate 并记录拒绝原因/另起版本；明确不再使用才 invalidated。评审记录自身 confirmed 可以表示报告已确认，但不改变被评对象状态。

无生成工具时可为 `awaiting_external_generation`，真实结果字段为 null；只有取得可核验提交凭据才 submitted，只有取得可访问返回文件/结果 ID 才 generated。文本设计通常为 `not_applicable`。

人工裁决至少允许 pending / accept / reject / partial-absorb / return。尚未答复必须 pending，不能代用户批准。

## 3. 阶段完成闸门

`confirmed` 是阶段级事实，不是语气判断。只有同时满足以下条件才能把阶段标为 confirmed：

1. **对象清楚**：说明被确认的阶段、产物 ID、版本和范围；局部确认不能扩张为整项目确认。
2. **完整成果已展示**：用户已看到将要保存的完整正文或明确可定位的完整文件，而不是仅看到摘要。
3. **明确阶段确认**：用户表达“确认这一版/本阶段完成/按此定稿/锁定本阶段”等明确含义。Agent 推荐、沉默、继续下一步，以及“不错、挺好、方向对了、可以看看、差不多”等积极反馈都不算。
4. **保存授权有效**：本次明确授权，或已有项目级持续保存授权且本阶段又得到明确确认。
5. **依赖与未决项可见**：上游版本明确；不阻断的未知项可保留，但不能隐藏或伪造。

存在歧义时只问一个短问题，例如：“你是要继续调整，还是确认本阶段并按已有授权保存？”未经回答保持 draft/candidate。

项目级持续授权只减少重复询问，**永远不能替代每一阶段的内容确认**。撤销持续授权后，未来保存恢复为逐次询问；撤销不删除历史文件。

## 4. 本地 Markdown 落盘硬规则

### 4.1 允许保存的条件

- `confirmed`：只有通过阶段完成闸门，且存在有效的阶段确认保存授权，才可写入 confirmed 成果。
- `draft` / `candidate`：仅在用户明确要求保存草稿或候选时落盘；文件名和正文必须显著标状态，不能伪装成确认稿。
- 未授权时可以在对话中给完整内容，但不得自行落盘。

### 4.2 必须保存完整成果

保存用户已经看到和确认的**完整阶段成果**，包括适用的正文、关键表格、公共头、未决项和交接信息。不得只保存摘要、聊天纪要、链接列表或“详见对话”。如内容过长需拆分，索引必须列出全部组成文件，并将它们视为同一个版本。

### 4.3 版本与覆盖

- 新版本使用新文件名或新版本目录；默认**不覆盖**旧版。
- `artifact_id` 稳定，`version` 递增；文件名建议为 `<阶段或产物>-<版本>-<状态>.md`。
- 覆盖、删除、移动历史文件是独立高风险动作，必须获得针对目标文件的明确授权。项目级“阶段确认后持续保存”不包含覆盖权。
- 上游换版时保留旧成果与批准历史，不把旧 confirmed 悄悄改写。

### 4.4 首次保存的项目自动初始化

当项目目录已明确，且用户已经给出本轮保存授权或有效持续保存授权时，Agent 负责检查项目基础记录。若 `PROJECT_BRIEF.md`、`AUTHORIZATIONS.md`、`PROJECT_INDEX.md`、`SESSION_HANDOFF.md`、`DECISIONS.md` 中有缺失，应从包内 `templates/` 自动创建缺失项，填写已知的最小信息，未知内容保持“未知/暂无”，随后回读验证。不得要求新手手工复制模板、选择 Skill 或填写内部状态字段。

自动初始化属于本地保存事务的一部分，只创建支持版本、授权、索引、交接和决定追踪的基础文件。`stage-deliverable-template.md` 是 Agent 的内部参考，不要求复制到用户项目。模板不可读时可以创建语义等价的最小结构，但必须说明实际来源与创建结果，不能声称使用了未读取的模板。

初始化 `AUTHORIZATIONS.md` 时，只记录用户本轮明确给出的授权原意、范围与有效期；未授权项保持 denied。自动初始化本身不产生覆盖、删除、上传、付费、生成、发布、评测、训练或研究权限。已有基础文件不得用空模板覆盖；内容冲突时保留原文件并标记待复核。

### 4.5 写后验证与登记

每次保存必须完成（首次保存还包括上述基础文件初始化与回读）：

1. 写入目标文件；
2. 回读目标文件，核验路径、版本、状态、正文完整性和关键段落；必要时做结构或哈希校验；
3. 更新 `PROJECT_INDEX.md`：登记产物、版本、状态、路径、上游依赖和确认依据；
4. 更新 `SESSION_HANDOFF.md`：记录最后完成阶段、当前有效版本、待决问题和下一小步；
5. 授权发生变化时更新 `AUTHORIZATIONS.md`，决定变化时更新 `DECISIONS.md`；
6. 回读上述更新，确认交叉引用存在且一致。

任一步写入或验证失败，必须如实报告失败位置与仍可信的状态；**不得声称“已保存、已更新、已完成落盘”**。部分写入要标明 partial，并避免把索引升级为 confirmed。

### 4.6 保存不等于其他授权

保存作品不等于：覆盖旧文件、上传素材、调用外部服务、产生费用、公开发布、训练/分析用途、采集研究数据或参与研究。各项分别授权。尤其是**保存作品绝不等于研究同意**；研究默认 denied，须单独、明确、可撤回地启用。

## 5. 授权与外部执行边界

授权至少分为：阶段确认后的本地新版本保存、draft/candidate 保存、覆盖/删除、上传、付费或资源消耗、公开发布、研究数据同意。不得用一项推导另一项。

用户只授权准备而未授权提交时，产物可为 planned，`next_action=await_user_authorization`；已明确由用户/外部工具执行且交接准备好时才可为 awaiting_external_generation。两者都不允许擅自上传、付费或宣称提交。文件存在不等于远端可访问，素材清单不等于上传证据。

默认可建议用户在项目首次明确同意后启用“每个阶段明确确认后，自动保存一个不覆盖旧版的新版本”的持续授权。持续授权的有效范围、启用证据和撤销状态必须记入 `AUTHORIZATIONS.md`；未记录或语义不清视为未授权。

## 6. 跨会话恢复协议

新会话按以下顺序恢复，不凭聊天记忆猜测：

1. 找到项目根目录；读取 `PROJECT_BRIEF.md`（若有）。
2. 读取 `AUTHORIZATIONS.md`，确认当前可执行边界；研究权限缺失时一律视为 denied。
3. 读取 `PROJECT_INDEX.md`，定位当前 confirmed、candidate、draft 及其明确版本。
4. 读取 `SESSION_HANDOFF.md`，了解上一会话停点、未决问题和下一小步。
5. 按索引回读当前有效成果文件；仅有索引而文件不存在时，不接受其 confirmed 状态。
6. 必要时读取 `DECISIONS.md`，核对用户明确决定与被否决方向。
7. 用自然语言向用户复述“已确认到哪里、当前候选是什么、本轮建议的小目标”；恢复本身不产生新确认。

冲突处理：实际成果文件、明确确认依据、索引和交接记录应一致。若不一致，保持原文件，标记 `needs_recheck`，向用户说明冲突；不可选择最方便的一项冒充事实。研究层记录不得反向修改 production 的确认状态。

## 7. 上游换版与传递复核

保留旧产物及旧批准历史，记录实际变化字段。按 `upstream_versions` 追踪直接和传递消费者，检查身份、空间、规则、动作、时间、声音或接口影响。受影响对象标 `needs_recheck`，当前 `approval_level` 置 none，旧批准移入 `payload.approval_history`；曾经生成的事实保持真实，但不再作为当前批准版。未知影响也先复核；无关者记录检查理由。复核后更新实际版本、证据和批准，必要时重新生成，不一律重做。

## 8. 模式、证据与修复

- narrative 用目标/阻力/选择/后果，但具体冲突模型只在适用时启用。
- perceptual 用感知目标/材料空间约束/观看变化/完成判据。
- conceptual 用命题/对照操作/观察指标/反例与解释限制。
- 基准按项目确认，可以黑白、受损、无人、有人或抽象；不自动恢复正常彩色。
- 平台能力未知时列待核验项，不从示例推断时长、参考数量、音频或首尾帧能力。
- 图片不能证明动作和音轨；抽样帧不能证明全段连续；缺结果不评结果。
- 默认比较一个主要变量；确属耦合问题可联合修改，但声明不能单变量归因。参考文件存在、静态校验通过或 Agent 执行，都不是实际生成或人工确认的证据。

优先级：真实性与用户授权不可被下层覆盖；通用正文规定默认范围；reference 仅在条件满足时启用；项目明确确认可覆盖创作风格、时长和布局等默认。冲突不清时列冲突并暂停受影响步骤。

## 9. 最终交付闸门

公共头完整、依赖明确、模式未漂移、证据真实、未决项可见；生成进度与批准分开；旧版本影响已处理；下一步明确。若声称完成落盘，还必须有：有效授权、明确阶段确认、完整新版本文件、成功回读、同步更新并回读 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`。讨论和局部成稿只检查适用项，不为填字段编造批准、证据、母版或生产测试。
