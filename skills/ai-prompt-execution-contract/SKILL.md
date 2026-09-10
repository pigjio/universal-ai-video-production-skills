---
name: ai-prompt-execution-contract
description: "用于把已确认的创意、角色、环境、物体、抽象视觉或分镜转成可执行且可评审的生成合同；Seedance/即梦正式 DO、逐镜视频提示词、参考素材职责、状态接力和容量压缩也触发。Use when writing, auditing, assembling or repairing static-image and temporal-video prompts, including self-contained Seedance generation requests. Separate record shorthand from submitted payload, encode observable outcomes, and preserve authorization and evidence boundaries."
version: 0.5.0
author: Domain Knowledge Distillation
license: MIT
metadata:
  hermes:
    tags: [prompt-contract, prompt-engineering, ai-image, ai-video, seedance, references, continuity]
    related_skills: [ai-storyboard-design, ai-character-design, ai-scene-design, ai-video-production-classroom, ai-generation-review]
---

# AI 影像提示词执行合同

## 新手逐轮引导与阶段成果落盘

任何交互先加载 `references/novice-guidance-protocol.md`；状态、授权、证据、提交与依赖处理同时加载 `references/common-contract.md`。引导不得弱化自包含合同、参考职责、平台能力核验、状态接力和真实性边界。

阶段落盘必须保存完整正文，并在写后回读通过后更新 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`；这三个文件及其状态必须相互一致。

- 每轮只推进 **1 个小目标**，最多问 **1 个真正阻断当前目标的问题**；“不知道/你决定/都行”合法，给标明假设且可撤销的默认。首轮交一个小产出，例如目标—约束—可观察结果—完成判据四行骨架或一个可复制请求片段，不只索取参数。
- 用户可否决任何 Agent 假设，只撤销受影响内容；已有合同默认做局部修改。跨会话先读项目索引、阶段交接和最新版本；不可用则明确缺口，以用户最小摘要重建，不伪造上游、素材或平台状态。
- “好/可以/继续”等不等于阶段完成、保存授权、提交授权或研究同意。先交完整可独立执行正文。已有有效持续保存授权时，只问是否确认本阶段完成，明确确认后直接保存；没有持续授权时，用一个合并问题主动提供“确认并保存为新的 Markdown 版本 / 确认但暂不保存 / 继续修改”三种自然选择，并说明预计文件名与已知目录。只有明确确认才标 `confirmed`。提示词合同保存/confirmed 仍不代表已上传、submitted、generated 或 production_approved。
- 阶段确认与保存授权不得互相推导，但不得拆成两轮重复询问。目录未知时并入同一个收尾问题；用户选择保存且目录明确后，自动创建缺失的项目基础记录文件。上传、付费、提交、生成、发布和研究始终分别授权。
- 主文件名为 `生成请求_对象_vNNN.md`，保存记录层、完整实际提交层/可复制请求、素材职责、参数待核、状态、完成判据、未决项与回传清单的**完整正文**，不能只存摘要。无生成工具也要交付完整请求并如实标 `awaiting_external_generation`/待外部执行，绝不伪造上传、任务 ID、返回文件或生成结果。
- 写前扫描版本，取下一未占用三位号且不覆盖旧版；写后回读核对存在、版本和请求正文，再更新项目索引与阶段交接。任何写入、回读、索引或交接失败都只报未完成/部分完成和恢复步骤。文件、Skill、素材/媒体不可用时输出完整可复制 Markdown，不声称已读取、写入或观察。
- 保存作品不等于研究、评测、训练、公开、上传、留存或二次使用同意；专项用途另取明确可撤销同意。

## 1. 边界、进入条件与参考路由

本阶段把创作判断变成一次请求可独立执行、结果可观察的合同，不代替导演设计，也不把提示词完成等同生成成功。静态图可从已明确的资产/构图需求直接进入，不必虚构剧本或分镜。

先判断工作深度：讨论时直接回答或局部试写，不强制完整公共头、提交层或生产测试；探索草案可比较可替换的合同假设，但标暂定、不升为生产 candidate；正式成稿只交付用户指定范围。仅在生产交接/验证、明确要求登记受管理产物，或受管理上游换版时加载 `references/common-contract.md`，此时公共状态、版本失效传播、证据及文件写入以该协议为准。授权落盘后确定工作区、保留版本，不静默覆盖批准稿。正文是通用默认，参考是条件方法；明确授权的项目格式可以覆盖格式偏好，不能覆盖证据真实性与授权。

| 条件 | 加载文件 | 取得的决策/产出 |
|---|---|---|
| 第一次使用或复合任务不知先后 | `references/methodology-map.md` | 分支顺序与交接检查 |
| 静态/视频/非叙事字段选择 | `references/static-vs-temporal.md` | 必需与不适用字段、完成判据 |
| 有参考图、继承上下文或需压缩提交 | `references/reference-duty-and-assembly.md` | 事实→读取范围→禁止继承、提交账本 |
| 动作、抽象效果、失败诊断或局部修复 | `references/causality-and-diagnostics.md` | 正向生命周期、竞争假设、修复范围 |
| 要写可复制的 Seedance/即梦正式 DO 或逐镜视频稿 | `references/seedance-formal-request-contract.md` | 自包含请求块、逐镜五字段、确定性结构校验 |
| 相邻请求需要真实尾帧、文字状态或独立重启 | `references/seedance-state-handoff.md` | 接口来源、状态字段、禁止重演与坏尾帧阻断 |
| 当前入口有已核验容量限制且提交块超限 | `references/seedance-capacity-compression.md` | 详细审核版→精简提交版的无损压缩与回归 |
| 需要完整交付或异常分支示范 | `references/worked-examples.md` | 完成合同、缺证据与失败记录 |
| 核查方法来源/通用化边界 | `references/source-map.md` | 已读源版具体位置与保留/改写理由 |

## 2. 先选择模式，不强加人物叙事

携带 `creative_mode: narrative | perceptual | conceptual` 和 `subject_type: character-led | environment-led | object-led | abstract`。二者独立：物体可承担叙事，角色也可仅作感知观察。

- character-led：引用必要角色版本，核对可见身份、姿态/比例。人物弧线不是每次生成的输入。
- environment-led：`character: null` 合法；以空间、材料、光色、环境变化和可读锚点验收。
- object-led：`character: null` 合法；以结构、接触/支撑、材质及状态变化验收。
- abstract：`character: null` 合法；以覆盖范围、材质、形态、运动路径和终点验收，不凭空增加角色、场景拓扑或物理接触。

通用必需是 **目标—约束—可观察结果—完成判据**。`narrative_job` 只在叙事信息/情绪职责相关时选填；非叙事填感知目标或概念关系，静态图不强塞 Narrative Job。

## 3. 区分三种单位和两层输入

- **镜头 shot**：导演规定的取景/观看/切点单位。
- **剪辑单元 edit_unit**：后期选用、裁切、排列的一段素材，可以包含多个镜头或一个镜头的部分。
- **生成请求 generation_request**：平台实际一次调用；可覆盖多个镜头，也可仅生成一个镜头的部分。一次请求的返回可以裁成多个剪辑单元，同一剪辑单元也可能来自多次补生成。

不要让同一个 Clip/DO 名称暗中承担三种含义。分别记录稳定 ID、覆盖关系、导演目标时长、请求窗口及计划/实际裁切；时长策略交 `ai-video-production-classroom` 的能力矩阵，不固定长短、秒数或每镜时长。

记录层可用“项目常量 + 本镜差异 + 上游版本”；提交层必须组装完整必要上下文、实际可用素材与参数。平台不自动读取本地路径或前次对话。若确有上下文继承，记录服务支持及实际会话/资源证据，不把计划视为上传。

## 4. 执行步骤

1. **冻结要求**：确认授权为写稿、上传、付费提交还是仅审查；锁定任务、主体类型、必要上游稳定 ID→版本、完成判据和不可改范围。上游候选可用于探索，但标候选、不能冒充生产批准。
2. **选择合同**：`static-image` 或 `temporal-video`；局部修复是 `operation: local-repair`，仍保留媒体类型。只保留适用字段。
3. **核验素材**：区分文件存在、视觉已看见、实际已上传三个事实。逐份记录可见事实→本镜读取范围→禁止继承。整图可以用于全局拓扑或经确认的全貌构图；禁止的是无职责的笼统继承，不是一律禁全图。多面板按实际文件计上传数，面板定位另记。
4. **组装正向合同**：静态写主体/结构/状态、构图焦点、材质与判据；时序按起始→触发→路径/接触（适用时）→反馈→终点。不把所有变化压成一个形容词，也不要求抽象色场有手、地面或反应镜。
5. **摄影和声音**：运镜写初始机位、触发、运动路径、停稳/切点；固定镜头直接写固定。音轨仅在任务需要时写，未知生成能力留问项，不保证模型产出。普通结束状态融入镜头结果，只有真实续接或关键末帧职责才单列接口。
6. **校对提交层**：反向核对每个必需约束在文本/参数/素材的哪个位置落地；风格、全局状态也必须在实际请求中可见。压缩只去重复，不删身份、状态范围、方向、因果和可见终点。核对字符/槽位等当前限制，未知时停在待核验。
7. **交付**：合同本身完成可交付，真实生成结果另由生产记录跟踪。提交前保留授权和输入快照；返回后转 `ai-generation-review`，不提前宣称合格。

### Seedance 正式执行稿分支

当用户只要求拆分 Clip/DO 时，先交生产组与请求映射；当用户明确要求“正式 DO”“可复制 Seedance 提示词”时，才加载正式请求合同并逐请求展开。`DO` 是可选显示别名，不得暗中混同导演镜头、平台调用和剪辑采用段。

每个独立平台请求必须自包含：请求窗口与画幅、视觉状态、唯一任务及完成判据、主体边界、实际上传素材职责、逐镜镜头任务/构图动作/摄影注意力/声音切点，以及真实需要时的续接接口。公共 YAML、内部路径和审批记录留在记录层，不粘入平台代码块。

Seedance 的时长、素材数量、输入模态和字符限制是动态能力。只采用带官方来源、核验日期、模型、产品入口和模式的当前证据；官方案例归纳、第三方经验与项目实测分别标注，均不冒充永久官方语法。

## 5. 公共头与输出模板

以下是记录模板，不把行政字段直接粘入平台提示词。`version` 是该制品修订号，技能版本为 0.5.0。引用素材的 ID 不含版本。空列表表示尚无证据，不代表已核验。

```yaml
artifact_id: PROMPT-example
version: v1
artifact_type: prompt
creative_mode: perceptual
subject_type: environment-led
lifecycle_status: draft
production_status: not_applicable
approval_level: none
upstream_versions: {}
confirmed_evidence: []
open_questions: []
recheck_trigger: []
next_action: request_review
payload:
  contract_type: temporal-video
  operation: create
  character: null
  target_goal: null
  narrative_job: null  # 仅叙事相关时填写
  completion_criteria: []
  record_layer: {project_constants: [], shot_delta: [], protected_scope: []}
  units: {shot_ids: [], edit_unit_ids: [], request_id: null}
  capability_evidence: []
  submission_layer:
    platform: null
    model: null
    parameters: {}
    complete_required_context: null
    positive_prompt: null
    actual_uploaded_assets: []
    planned_but_not_uploaded: []
    verified_context_inheritance: []
  reference_duties: []  # asset_id/version/file、可见事实、读取范围、禁止继承、上传证据
  static_fields: null  # 静态时填构图/焦点/结构/状态/材质，删除 temporal_fields
  temporal_fields: {state_chain: [], camera: null, audio_requirement: null}
  next_segment_interface: null  # 仅实际续接职责时填写
  allowed_changes: []
  coupled_repair_rationale: null
  high_risk_constraints: []
  blocked_reason: null
  human_decision: pending
  human_decision_evidence: null
```

## 6. 能力缺口与失败出口

- 无工具：交付独立可复制文本、计划素材、参数待核项和外部回传清单；待执行的 clip/request 用 `awaiting_external_generation`，提示词制品本身保持 `not_applicable`。不得把计划清单标为已上传。
- 缺素材/无法看图：列缺失项和受阻判据；可给候选文本，不编视觉事实。用户明确授权改纯文字方案时另存候选并注明不再保证图像身份/拓扑继承。
- 提交失败：生产记录为 `failed`，记录错误及已知任务句柄；未确认受理的超时先查询，不能盲目重复付费调用。不得虚构结果文件。
- 用户拒绝生成/预算：保留合同，记录拒绝依据，`next_action: await_user_authorization`，不提交。
- 人工等待：`human_decision: pending`，不代填接受；`next_action: await_human_review`。有明确原话/裁决引用才更新决定和批准层。

## 7. 诊断、版本与闸门

失败处理采用 **症状→竞争根因→区分证据/最小试验→授权修复→回归**。身份/空间漂移不是根因；先比较实际输入与合同，再考虑资产、提示词、镜头负荷、采样及平台能力。单次随机生成不能证实根因。默认控制一个主变量用于归因；耦合变量可联合修复，但须列明共同原因、必要联动、保护范围，不能声称已隔离每个变量贡献。

上游改版时按稳定 ID 追踪直接及传递受影响依赖→`needs_recheck`，保留旧批准历史但不继续作为当前门禁；无关依赖经影响检查可保留并记理由。重审后才恢复 `confirmed`。

- [ ] 模式贯通，`character: null` 未被当缺角色错误；静态/时序字段适用。
- [ ] 镜头、剪辑单元和生成请求覆盖关系明确，没有固定时长假设。
- [ ] 参考事实、读取范围、禁止继承、计划/真实上传分开。
- [ ] 正向结果可观察；抽象效果的范围、材质、路径、终点可检查。
- [ ] 提交层完整，不依赖平台不可见文档；未知能力和缺素材未掩盖。
- [ ] Seedance 正式稿一个请求一个闭合代码块；镜头 ID、五字段、时长、实际素材与续接接口确定性闭合。
- [ ] DO 仅作显示别名；shot、production_group、generation_request、edit_unit 没有混号。
- [ ] 平台固定数值有当前来源/日期/入口；工程启发式未冒充官方规则。
- [ ] 根因与症状分开；修复有授权、保护范围及回归项。
- [ ] 没有虚构返回、通过或人工裁决；等待和失败均有下一动作。
