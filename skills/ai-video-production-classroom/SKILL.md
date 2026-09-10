---
name: ai-video-production-classroom
description: "用于教学或执行平台中立的 AI 视频生产，把镜头变成生产组、Seedance/即梦 Clip/DO、生成请求、参考绑定、真实尾帧/文字续接、评审与剪辑交接；Use for image-to-video, text-to-video, multimodal generation, capability-based grouping, continuation, baseline logging and unavailable-generator handoffs. A single-character classroom profile is optional, never a universal prerequisite."
version: 0.5.0
author: Domain Knowledge Distillation
license: MIT
metadata:
  hermes:
    tags: [ai-video, seedance, teaching, classroom, clip, do, baseline, production]
    related_skills: [ai-storyboard-design, ai-prompt-execution-contract, ai-generation-review]
---

# AI 视频生产｜平台中立执行与课堂练习

## 新手逐轮引导与阶段成果落盘

任何交互先加载 `references/novice-guidance-protocol.md`；生产状态、授权、证据、外部执行和依赖同时加载 `references/common-contract.md`。新手节奏不能削弱平台状态机、四层生产单位、能力证据和真实提交/返回边界。

阶段落盘必须保存完整正文，并在写后回读通过后更新 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`；这三个文件及其状态必须相互一致。

- 每轮只推进 **1 个小目标**，最多提出 **1 个真正阻断问题**；“不知道/你先排/都可以”合法，给可撤销且标明假设的默认。首轮即交一个小产出，如首个 production_group、shot→request 映射或能力待核清单，不能只问平台参数。
- 用户否决 Agent 假设即局部撤回；已有生产表只改请求范围。跨会话先读项目索引、阶段交接、最新计划和真实证据记录；不可读就说明缺口，以最小摘要继续，绝不补造授权、平台状态或句柄。
- 积极反馈不等于阶段完成、保存、上传、付费提交、人工通过或研究同意。先交完整可执行生产计划。已有有效持续保存授权时，只问是否确认本阶段完成，明确确认后直接保存；没有持续授权时，用一个合并问题主动提供“确认并保存为新的 Markdown 版本 / 确认但暂不保存 / 继续修改”三种自然选择，并说明预计文件名与已知目录。只有明确确认才将**计划产物**标 `confirmed`，计划 confirmed 不会把请求状态提升为 submitted/generated/reviewed。
- 阶段确认与保存授权不得互相推导，但不得拆成两轮重复询问。目录未知时并入同一个收尾问题；用户选择保存且目录明确后，自动创建缺失的项目基础记录文件。上传、付费、提交、重试、发布和研究必须按动作另行授权，持续保存授权不能代替。
- 主文件名为 `视频生产计划_vNNN.md`，保存输入冻结、四层映射、能力依据、完整请求/回传需求、状态、风险和下一动作的**完整正文**，不只存摘要。真实提交快照、上传回执、任务 ID、返回 ID/文件、错误和观察证据必须另建证据记录并引用；只有实际取得才写，绝不可把计划字段复制成证据或伪造生成结果。
- 写前扫描版本并使用下一未占用三位号，旧计划/批准稿不覆盖；写后回读核对，再更新项目索引与阶段交接。写入、回读、索引、交接任一步失败只报未完成/部分完成。生成工具、Skill、文件或媒体不可用时，仍交完整计划和生成请求/外部回传清单，但不声称上传、提交、生成、观看或导出。
- 保存作品不等于同意研究、评测、训练、公开、上传、留存或二次使用；专项用途另取明确可撤销同意。

## 1. 通用目标与可选课堂 profile

本技能把已明确的镜头/视觉变化转为可追踪生成请求，完成输入冻结、能力选择、提交、回传、评审及剪辑交接。不包含平台私有 SOP，不定义项目故事或美术设定，也不强行将所有任务缩成单角色短片。

`profile: general` 是默认。用户选择 `single-character-classroom` 时才采用“一个已确认角色、一个主要场景、一个主要动作、一个可见结果”的小练习约束。这是控制教学难度，不是通用生产闸门。也可选择 environment-study、object-study、abstract-study，或保持 general。

携带 creative_mode 与 subject_type；environment-led/object-led/abstract 的 `character: null` 完全合法。叙事作品可记录 Narrative Job；感知/概念任务记录感知目标、材料/空间约束、可观察变化和完成判据。静态资产不必通过视频练习，交提示词静态分支。

先判断工作深度：讨论时可直接解释能力条件或局部试排，不提交、不要求完整生产记录；探索草案可比较长短请求、分组或桥接方案，明确哪些只是待验证假设；正式成稿只交付用户指定的课堂练习、请求表或交接范围。仅在生产交接/验证、明确要求登记受管理产物，或受管理上游换版时加载 `references/common-contract.md`，状态、证据与写入使用公共协议。落盘先确定授权工作区、保留历史版本。项目明确规则可覆盖时长和格式偏好，不能覆盖授权及证据真实。

## 2. 条件加载路由

| 条件 | 加载文件 | 预期产出 |
|---|---|---|
| 进入生产交接、验证、无工具受阻或基线比较 | `references/production-modes-and-baseline.md` | 能力证据、执行/等待/失败状态、实验账本 |
| 导演镜头转 Clip/DO、任务合同、重试/桥接/合并映射 | `references/production-grouping-and-task-contract.md` | shot→production_group→request→edit_unit 四层映射 |
| 目标为 Seedance/即梦或需核验平台能力 | `references/seedance-capability-and-evidence.md` | 生成模式、动态能力档案、官方/经验/实测证据分层 |
| 镜头分组、长短请求、续接与剪辑 | `references/clip-continuity.md` | 四层映射、能力矩阵、接口和回退策略 |
| 真实尾帧、文字重启、长窗桥接或剪辑交付 | `references/continuation-and-edit-delivery.md` | 接口资格、EDL、来源追溯和输出验证 |
| 课堂演示、无角色或受阻交接 | `references/worked-examples.md` | 可交付实例与上游改版影响链 |
| 溯源或核对是否夹带私有规则 | `references/source-map.md` | 源版位置、通用化范围 |

提交文本由 `ai-prompt-execution-contract` 组装；真实结果交 `ai-generation-review`。这些是包内技能，不依赖源版安装路径。

## 3. 进入条件与输入冻结

1. 记录本轮授权：分组、写稿、上传、付费生成、审查、剪辑分别确认。已有镜头可局部进入，不必重走全流程。
2. 引用必要上游稳定 ID→版本及当前批准证据；候选输入可用于授权探索，不能标生产批准。无角色不要求角色资产；纯文字生成可无参考图，但空间/材料/变化仍应明确。
3. 冻结任务、主体白名单/范围、已确认基准状态、目标画幅、导演时长意图、可读结果及不可修改范围。废墟可就是基准，不要求先生成“完整正常态”。
4. 核对文件可访问、内容已视觉观察与实际上传状态，不能凭文件名填画面。素材不在本环境就请求回传或交外部人工核验。

## 4. 四层生产单位与能力条件矩阵

- **shot / 镜头**：导演观看、构图、动作和切点单位。
- **production_group / 生产组**：共享一个主要任务、连续空间/状态和参考集合的生产规划单位；Clip/DO 可作显示别名。
- **edit_unit / 剪辑单元**：后期采用的一段，记录来源请求和 in/out；可能横跨镜头，也可能只是镜头一部分。
- **generation_request / 生成请求**：实际一次平台调用，具有输入快照、参数、任务句柄、输出和失败状态。

分开 ID，显式映射。不要把一个 Clip/DO 同时当成镜头、生产组、剪辑段和请求。一个生产组可有多个重试/补段请求，一个请求也可覆盖多个相邻生产组。导演目标时长、平台生成窗口、实际输出时长和成片采用时长分别记录；无实际结果时裁切是 planned，不写成已经执行。

每个生产组建立一个任务合同：叙事任务使用 Narrative Job，感知任务使用 perceptual goal，概念任务使用 conceptual test；都要有可观察完成判据、可见终点和不得提前出现的信息。若两个不可替代结果争夺同组，拆组或请人工明确主从。

| 已核对的条件 | 优先候选 | 风险与退出条件 |
|---|---|---|
| 平台支持目标长窗口，空间/材料基线连续，跨段运动相位重要，额度允许比较 | 一次较长请求，内部保留镜头/变化节点 | 长段漏动作或漂移→定位失败区间，再短段/桥接；不自动替换已批准版本 |
| 已观察到长段高失败率，复杂接触/状态多，平台窗口不足或局部重试成本低 | 按可观察状态边界拆短请求 | 接口速度/身份/光色不连续→桥接或受控合并；不压缩必要结果证明 |
| 多镜头能力未知或只有单镜能力证据 | 按单镜/单变化试验，或等待核验 | 不声称短段必然稳定；仍保存结果验证 |
| 前后主体已通过，仅边界有问题 | 短桥接、局部补段或后期切点 | 不无故整段重生成；不能用剪辑掩盖关键因果错误 |
| 参数/窗口/槽位信息缺失 | 平台中立方案与待查项 | 不固定秒数，不先宣称可生成 |

平台能力必须记录来源、核对时间、模型/版本及适用模式；文档支持不等于项目已实测稳定。窗口余量用于可裁 handles 或既有动作闭合，不添无功能行走或重复反应。改变导演内容须退回分镜确认，而非生产层擅改。

## 5. 执行、等待与基线

1. 从能力矩阵选请求边界，列覆盖镜头及计划剪辑单元。
2. 按参考图事实→本镜读取范围→禁止继承指定职责；整图拓扑/权威全貌构图可用，避免无关图或冲突状态。抽象效果必须具备范围、材质、运动路径和终点。
3. 组装完整提交层；不假定平台读得到本地路径、项目常量或前次对话。平台有真实上下文继承时保存来源句柄。
4. 提交前确认素材资源可用、参数受支持、额度/授权足够；独立请求可在工具和授权允许时并行，依赖真实尾帧的请求等待上游真实且合格的接口。
5. 保存实际提交快照、上传回执、模型/参数、调用时间、任务 ID、返回资源/文件和错误。不将 submitted 当 generated；仅任务句柄而无输出时仍在 submitted。
6. 第一轮真实可访问输出是生成基线，不是预期描述；它即使失败也保留。已通过基线和新候选分开，不把“用户喜欢旧版”外推为普遍模型规律。
7. 转评审，记录观察范围和人工待裁决；没有视频只能做合同审计，不能判断动作/声音。

| 实际情况 | 生产状态/下一步 |
|---|---|
| 无工具，外部待生成 | awaiting_external_generation；交完整输入、计划素材和回传清单 |
| 必需素材缺失 | planned；blocked_reason 写具体资产及受阻职责，请回传；纯文字替代须授权另版 |
| 用户拒绝提交/预算 | planned 或 not_started；保留拒绝证据，await_user_authorization，不代操作 |
| 返回受理 ID 无视频 | submitted；查询任务，不伪造生成文件 |
| 明确错误/拒绝/生成失败 | failed；记录错误，先检查已受理情况再决定授权重试 |
| 超时且不知是否受理 | submitted（已知任务 ID）或 planned（无受理证据）；标 submission_uncertain，先查状态避免重复扣费 |
| 真实结果可访问 | generated→under_review；以实际观察推进 |
| 等待人工 | 保留真实生产状态；human_decision: pending，await_human_review |

## 6. Clip / 请求生产记录模板

本记录跟踪一个请求及它的计划/实际剪辑映射，标题 Clip 不再替代字段语义。公共头所有字段保留。

```yaml
artifact_id: CLIP-example
version: v1
artifact_type: clip
creative_mode: perceptual
subject_type: environment-led
lifecycle_status: draft
production_status: planned
approval_level: none
upstream_versions: {}
confirmed_evidence: []
open_questions: []
recheck_trigger: []
next_action: verify_capabilities
payload:
  profile: general
  character: null
  target_goal: null
  completion_criteria: []
  authorized_actions: []
  authorization_evidence: null
  protected_scope: []
  shot_ids: []
  edit_units: []  # edit_unit_id、source_request_id、planned/actual in-out
  production_group_id: PG-example
  display_alias: DO-example
  task_contract: {type: perceptual_goal, primary_job: null, observable_end_state: null, forbidden_early_reveal: []}
  generation_requests: []  # request_id、role(primary/retry/bridge/merged_test/pickup)、status
  director_duration_target: null
  requested_window: null
  actual_output_duration: null
  capability_checks: []
  reference_duties: []
  actual_uploaded_assets: []
  planned_but_not_uploaded: []
  complete_submission_text: null
  actual_submission_snapshot: null
  platform_model_parameters: {}
  returned_task_id: null
  returned_output_id: null
  result_file: null
  error_or_block: null
  baseline: null
  allowed_changes: []
  coupled_repair_rationale: null
  continuation_interface: null
  review_record: null
  human_decision: pending
  human_decision_evidence: null
```

## 7. 回归、交付和版本失效

默认只改一个主变量便于归因，但并非永远只能一个：相冲突的素材和文字状态、相互依赖的起点与下游接口可联合修复。写清联动依据、允许变化、受保护版本和回归项；单次随机生成不能证明根因或普遍优越性。先控制平台/模型/参数与素材，再重复可负担的比较；种子不可控则明确混杂。

上游改版追踪直接及传递受影响依赖→`needs_recheck`，历史批准保留但不再作为有效门禁；记录无关项保留理由。重审后恢复 confirmed，不因旧片已生成就认定它符合新稿。

交付真实成片时记录来源资源、采用版本、裁切范围、替换段与声音决定，验证播放、画幅、时长和音轨。未做的检查标未验证；没有剪辑工具就交剪辑决策表，不宣称成片已导出。

- [ ] profile 已声明，非叙事/无角色不被课堂角色约束拦截。
- [ ] shot、production_group、generation_request、edit_unit 四层分开，长短选择有能力条件而非固定秒数。
- [ ] 每个生产组有一个主要任务合同和可观察终点；DO 只是可选别名。
- [ ] Seedance 能力带来源、日期、模型、产品入口和模式；官方事实、案例归纳、第三方经验、项目观察和人工接受未混写。
- [ ] 输入版本、基准状态、可见终点和参考职责明确。
- [ ] 计划/上传/受理/生成/评审/人工接受分开，有真实证据才晋级。
- [ ] 缺工具、缺素材、提交失败、拒绝和人工等待各有出口。
- [ ] 修复范围受控，耦合修复已说明，失败与通过版本均保留。
- [ ] 尾帧/文字重建接口诚实标来源，坏接口不继续传播。
