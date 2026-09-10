# Seedance 四镜头生产分组与请求策略比较（仅计划）

```yaml
artifact_id: CLIPPLAN-case-2-grouping
version: v1
artifact_type: clip
creative_mode: narrative
subject_type: character-led
lifecycle_status: draft
production_status: planned
approval_level: none
upstream_versions:
  SHOT-01: null
  SHOT-02: null
  SHOT-03: null
  SHOT-04: null
confirmed_evidence:
  - "本轮用户输入：四个镜头均已获批准；导演目标时长依次为 3、4、3、3 秒。"
open_questions:
  - "四个已批准镜头的明确版本号未提供。"
  - "Seedance 的具体产品入口、模型/版本与生成模式未提供。"
  - "当前入口是否支持覆盖导演总目标 13 秒的单次窗口与受控多镜头，未知。"
  - "当前入口的素材槽位、首尾帧/视频续接与声音能力，未知。"
  - "画幅、分辨率、参考素材及声音设计目标未提供。"
recheck_trigger:
  - "任一镜头内容或导演时长改版。"
  - "Seedance 入口、模型、模式或能力核验结果变化。"
  - "取得真实生成结果、真实尾帧或人工评审结论。"
next_action: await_user_authorization
payload:
  record_completeness: incomplete
  profile: general
  authorized_actions:
    - text_planning
    - save_plan_to_specified_path
  unauthorized_actions:
    - upload_assets
    - submit_generation
    - incur_cost
    - claim_generation_or_review
  human_decision: pending
```

## 1. 口径与当前状态

- **shot / 镜头**：导演观看、构图、动作与切点单位；本案为 `SHOT-01` 至 `SHOT-04`，内容和导演时长意图不由生产层改写。
- **production_group / 生产组**：共享一个主要任务、连续状态和参考集合的规划单位。下文以 `PG-*` 为正式 ID。
- **Clip / DO**：这里只是 production_group 的显示别名，不是新的镜头、请求或剪辑段；例如 `PG-01` 可显示为 `CLIP-01 / DO-01`。
- **generation_request / 生成请求**：一次真实平台调用，必须有独立 `REQ-*`、输入快照、参数、回执和输出。下文所有 `REQ-*` 都只是候选计划，尚未提交。
- **edit_unit / 剪辑单元**：后期拟采用的一段，以 `EDIT-*` 标识，并追溯到真实请求输出及实际 in/out。当前没有输出，也没有实际裁切，故 actual 字段全部为 `null`。

**状态结论：**本文件只获授权做文本规划并保存；没有上传、付费生成、评审或剪辑授权。所有 generation_request 均为 `planned`，下一步为 `await_user_authorization`，不是 `awaiting_external_generation`、`submitted` 或 `generated`。当前没有基线视频。

## 2. Shot 账本（导演层，不等于生产组）

| shot_id | 已批准观看内容 | 功能 | 导演目标时长 | 起始状态 | 可见结束状态 |
|---|---|---|---:|---|---|
| SHOT-01 | 建立无人长廊 | 建立 | 3 秒 | 长廊状态待已批准分镜/素材确认 | 长廊仍无人；门与空间方位已建立 |
| SHOT-02 | 主体 A 进入并走到门前 | 进入／移动 | 4 秒 | 长廊无人，门未被操作 | A 到达门前；尚未推门 |
| SHOT-03 | 主体 A 推门，门完全打开 | 接触／动作结果 | 3 秒 | A 位于门前，门未开 | 门完全打开；A 尚未做后退遮眼反应 |
| SHOT-04 | 门后强光照入，主体 A 后退一步并遮眼 | 光线触发／Reaction | 3 秒 | 门已完全打开，A 尚未后退遮眼 | 强光已照入；A 已后退一步并完成遮眼姿态 |

> “无人”只约束 SHOT-01；“完全打开”必须在 SHOT-03 可见；“后退一步并遮眼”必须在 SHOT-04 可见。剪辑不能隐藏这些批准的结果证明。

## 3. Production group / Clip / DO 规划

采用四组是**内容与状态边界的规划基线**，不是对平台请求数量的预判。每组只有一个主要任务与一个可观察终点。

| production_group_id | 显示别名 | shot 映射 | 主要任务（Narrative Job） | 完成判据 | 可见终点 | 不得提前出现 | 分组／边界依据 |
|---|---|---|---|---|---|---|---|
| PG-01 | CLIP-01 / DO-01 | SHOT-01 | 建立 A 进入前的无人长廊与门的空间关系 | 长廊、门、行进方向可读；全段无 A | 空间关系成立，长廊仍无人 | A 入画；推门；门后强光；遮眼反应 | “无人基线”是后续进入动作的独立状态证明 |
| PG-02 | CLIP-02 / DO-02 | SHOT-02 | 让 A 从进入长廊连续走到门前 | A 的进入、行走与到达均可读；身份、方位和移动方向连贯 | A 稳定到达门前，门尚未被推动 | 门开启；强光照入；后退遮眼 | 到达门前是接触动作前的可观察状态边界 |
| PG-03 | CLIP-03 / DO-03 | SHOT-03 | 完成 A 推门至门完全打开的接触动作 | 手—门接触与开启因果可读；门达到完全打开状态 | 门完全打开，A 仍未执行 SHOT-04 的反应 | A 后退一步或遮眼；将强光反应提前 | 复杂接触完成后形成明确结构状态边界 |
| PG-04 | CLIP-04 / DO-04 | SHOT-04 | 呈现门后强光触发 A 后退一步并遮眼 | 强光来源为门后；后退恰为一步；遮眼动作完成；因果顺序可读 | 强光已进入长廊，A 完成后退一步与遮眼 | 在强光照入前预演后退或遮眼 | 光线状态突变与人物 Reaction 构成独立结果 |

### 状态接口

1. **IF-01（PG-01→PG-02）**：同一长廊、门位置与相机侧别；末端仍无人；A 从既定入口方向进入。若分请求，只能先按权威文字/已批准素材重建；真实结果存在后才可判断是否连续。
2. **IF-02（PG-02→PG-03）**：A 位于门前，朝向门，门未被推动；手与门的距离、站位和遮挡需从邻近运动区间核验，不能凭单张尾帧证明动作速度。
3. **IF-03（PG-03→PG-04）**：门已完全打开，A 尚未后退遮眼；下一段先建立该既成状态，不重演推门。强光的首次明确照入及 A 的 Reaction 留在 SHOT-04。此边界最敏感，须核对门状态、手臂相位、A 的重心、光色与运动方向。

## 4. 四种时长账本

四种时长严格分栏：导演目标已知；平台请求窗口尚未核验；没有真实输出或剪辑，因此后两项不得填写计划值冒充实际值。

| 对象 | director_duration_target | requested_window | actual_output_duration | actual_edit_duration |
|---|---:|---|---|---|
| SHOT-01 / PG-01 / EDIT-01 | 3 秒 | `null`（unknown） | `null` | `null` |
| SHOT-02 / PG-02 / EDIT-02 | 4 秒 | `null`（unknown） | `null` | `null` |
| SHOT-03 / PG-03 / EDIT-03 | 3 秒 | `null`（unknown） | `null` | `null` |
| SHOT-04 / PG-04 / EDIT-04 | 3 秒 | `null`（unknown） | `null` | `null` |
| 全序列导演目标 | 13 秒 | `null`（unknown；不可等同为“已支持 13 秒请求”） | `null` | `null` |

请求窗口待核验后才能选择；若平台只提供离散窗口，额外时间仅可作为裁切 handles 或既有动作闭合余量，不得增加闲走、重复反应或新剧情。

## 5. Generation request 策略比较

以下方案共享同一套四个 production_group 和导演目标；差别仅在**一次平台调用覆盖哪些组**。它们是互斥或按条件启用的候选，不表示要全部生成。

| 方案 | generation_request 计划 | 覆盖关系 | 主要收益 | 主要风险／成本 | 启用证据门 | 退出／回退 |
|---|---|---|---|---|---|---|
| A. 长窗单请求 | `REQ-LONG-01`，role=`merged_test`，status=`planned` | PG-01～PG-04；SHOT-01～04 | 减少请求间身份、空间、门状态、运动相位与光色接缝 | 当前入口是否支持 13 秒及受控多镜未知；长段可能漏镜头节点、提前揭示强光、接触漂移或节奏失控；局部重试成本可能高 | 必须有当前 Seedance 入口/模型/模式对足够窗口和多镜控制的能力证据；再确认额度与提交授权 | 任一关键节点缺失或漂移时保留可用区间，定位失败段，转方案 B 或仅对接口转方案 C；不自动覆盖任何已接受版本 |
| B. 按状态边界拆短请求 | `REQ-S01-01`→PG-01；`REQ-S02-01`→PG-02；`REQ-S03-01`→PG-03；`REQ-S04-01`→PG-04；均 role=`primary`、status=`planned` | 每请求一组／一镜 | 每次只有一个主要任务；便于定位无人建立、到门前、推门完成、强光 Reaction 的失败与局部重试 | 增加 IF-01～03 的身份、位置、速度、门状态、光色和声音接缝；短段不等于必然稳定 | 若多镜能力未知、仅有单镜证据、窗口不足，或实测长段失败率高，则优先；每个实际窗口仍待核验 | 接口失败而主体段通过时不整段重做，转方案 C；若短请求仍漂移，不能伪称状态边界已解决 |
| C. 桥接／pickup | 按故障边界新建 `REQ-B12-01`、`REQ-B23-01` 或 `REQ-B34-01`，role=`bridge`；只创建实际需要者 | 可跨相邻 PG 边界，但不改变 shot 归属 | 保护已通过主体段，仅修复接缝或必要动作相位；成本较集中 | 桥段也会引入新身份／几何漂移；必须重新评审；不能靠切点隐藏推门完成或 Reaction | 只有两侧主体段已有真实可访问输出且通过内容评审、仅边界不合格时启用；依赖真实尾帧者必须等邻近区间观察合格且入口支持相应输入 | 真实尾帧不合格则冻结下游，改用稍早合格切点、上游 pickup，或经授权采用明确标注的文字重建；不得传播坏接口 |

### 长窗候选的连续运动包络（不是提交文本）

若且仅若能力核验通过，`REQ-LONG-01` 应按连续因果重写，而不是拼接四段旧 Prompt：无人长廊建立 → A 进入并到门前 → A 接触并推门至完全打开 → 门后强光照入 → A 后退一步并遮眼。内部仍保留四个 shot 节点和切点；强光及 Reaction 不得提前，推门完全打开不得被跳过。

### 短请求的依赖顺序

- `REQ-S01-01` 与后续请求的提交方式取决于参考素材与续接能力；在没有可复用真实上下文前，不声称其输出可自动传给 `REQ-S02-01`。
- `REQ-S03-01` 依赖“门前、门未开”的合格起点；`REQ-S04-01` 依赖“门完全打开、A 未反应”的合格起点。
- 若采用真实尾帧/视频续接，后续请求必须等待上游实际输出与接口评审；若采用 `textual_reconstruction`，须明确它不是像素级媒体继承，并列出未知状态。

### 桥接优先级

1. **IF-03 优先观察**：推门完全打开到强光 Reaction 同时涉及门几何、接触相位、光线突变与人物重心，最可能需要 `REQ-B34-01`。
2. IF-02 若手—门接触不连续，可用 `REQ-B23-01` 或 PG-03 起始 pickup；不得删去可见接触因果。
3. IF-01 通常可用合法切点隔开建立镜头与人物入场；若导演切点要求连续运动且接缝失败，再考虑 `REQ-B12-01`。

上述优先级是风险预判，不是项目实测结论，也不授权创建或提交桥接请求。

## 6. Edit unit 计划（与 shot、PG、REQ 分开）

| edit_unit_id | 对应 shot | production_group | 长窗方案候选来源 | 短段方案候选来源 | 桥接可能影响 | planned_in_out | actual_in_out |
|---|---|---|---|---|---|---|---|
| EDIT-01 | SHOT-01 | PG-01 | REQ-LONG-01 的 SHOT-01 区间 | REQ-S01-01 | REQ-B12-01 可能替换末端／接缝 | 待真实输出后按 3 秒导演目标选择，并保留合法 handles | `null` |
| EDIT-02 | SHOT-02 | PG-02 | REQ-LONG-01 的 SHOT-02 区间 | REQ-S02-01 | REQ-B12-01／REQ-B23-01 可能替换边界 | 待真实输出后按 4 秒导演目标选择，并保留完整到达结果 | `null` |
| EDIT-03 | SHOT-03 | PG-03 | REQ-LONG-01 的 SHOT-03 区间 | REQ-S03-01 | REQ-B23-01／REQ-B34-01 可能替换边界 | 待真实输出后按 3 秒导演目标选择；门完全打开必须可见 | `null` |
| EDIT-04 | SHOT-04 | PG-04 | REQ-LONG-01 的 SHOT-04 区间 | REQ-S04-01 | REQ-B34-01 可能替换起始接缝 | 待真实输出后按 3 秒导演目标选择；强光、一步后退、遮眼均须可见 | `null` |

候选来源不是最终采用来源。只有获得真实 output/resource ID 并完成实际裁切后，才能填写 `source_output_id`、actual in/out 和 actual edit duration。当前没有导出文件，也未验证播放、画幅、时长、音轨、字幕或水印。

## 7. Seedance 能力证据账本

本案没有提供 URL、核验日期、模型版本、具体产品入口或项目实测；因此不能把任何平台能力写成已知事实，也不能把“Seedance”品牌名当作 13 秒多镜、素材槽位、续接或声音支持的证据。

| capability | status | evidence_level | source / checked_at | model / product_entry / mode | 本计划的处理 |
|---|---|---|---|---|---|
| 单请求覆盖导演总目标 13 秒的窗口 | unknown | 无 O1/O2/T/P/A 证据 | `null` / `null` | 全部 `null` | `REQ-LONG-01.requested_window=null`；核验前不提交 |
| 单请求内受控多镜头／镜头切换 | unknown | 无 O1/O2/T/P/A 证据 | `null` / `null` | 全部 `null` | 长窗仅作条件候选；默认不能宣称可行或稳定 |
| 素材槽位数量、类型与职责绑定 | unknown | 无 O1/O2/T/P/A 证据 | `null` / `null` | 全部 `null` | 不虚构图片／视频／首尾帧数量，不写假上传记录 |
| 首尾帧、真实尾帧或视频续接 | unknown | 无 O1/O2/T/P/A 证据 | `null` / `null` | 全部 `null` | 桥接的媒体继承路径保持 blocked；可另列文字重建候选但不称连续 |
| 声音生成／输入／保留／输出 | unknown | 无 O1/O2/T/P/A 证据 | `null` / `null` | 全部 `null` | 不假定生成声音；声音尾部与 audio bridge 均待声音设计及能力核验 |
| 当前项目在该入口的稳定性 | unknown | 无项目观察 P、无人工接受 A | `null` / `null` | 全部 `null` | 不声称长窗或短段哪种“已更稳定” |

### 提交前必须取得的能力证据

1. 具体 Seedance 产品入口（UI/API/其他）、模型与版本、generation mode，以及核验时间。
2. 当前入口的可选时长／最大窗口、是否能承载目标 13 秒、画幅与分辨率。
3. 多镜头控制是否在该入口与模式可用；官方支持与本项目稳定性分栏记录。
4. 图片、视频、首帧、尾帧和音频各自的真实槽位数、计数方式、格式限制及上传回执机制。
5. 是否支持真实尾帧／视频续接、上下文继承及相应资源 ID。
6. 声音是输入、生成还是输出能力；若不支持，明确后期声音方案，而不是默认“无声已通过”。
7. 字符／令牌限制、额度、输出获取方式，以及 UI/API 能力差异。

证据记录须包含 `source_url`、`checked_at`、`model_version`、`product_entry`、`generation_mode` 和适用范围。官方产品事实（O1）只能证明声明支持，不能证明本案稳定；真实请求观察（P）也只能支持相同入口、版本与参数下的局部判断。

## 8. 等待状态与放行闸门

### 当前等待状态

```yaml
plan_status: planned
next_action: await_user_authorization
submission_authorized: false
asset_upload_authorized: false
cost_authorized: false
review_authorized: false
edit_authorized: false
returned_task_id: null
returned_output_id: null
result_file: null
first_return_baseline: null
accepted_baseline: null
human_decision: pending
blocked_by:
  - exact_upstream_shot_versions
  - seedance_entry_model_mode_capability_evidence
  - aspect_ratio_and_resolution
  - reference_asset_inventory_and_duties
  - sound_requirement
  - generation_and_cost_authorization
```

### 放行顺序

1. 补齐四个 shot 的批准版本、画幅／分辨率、参考资产及职责、声音目标。
2. 按第 7 节核验当前 Seedance 入口能力，并将 unknown 更新为有来源的 known 或继续 unknown。
3. 基于证据选择 A 或 B 作为首轮候选；C 不是无条件首轮方案，只在主体段真实通过而边界失败后启用。
4. 单独取得上传、费用与生成授权；授权前所有 REQ 保持 `planned`。
5. 若获授权并实际提交，保存完整输入快照、真实上传回执、模型参数、task ID 和错误；仅有 task ID 时为 `submitted`，不是 `generated`。
6. 只有真实可访问输出才建立 `first_return_baseline` 并进入评审；评审需逐项检查四个可见终点及三个接口。人工接受仍需独立证据。
7. 只有实际剪辑后才填写 edit unit 的 source output、actual in/out 与 actual edit duration；未导出前不得称成片完成。

## 9. 计划结论

- **生产分组基线**：四个 shot 映射为四个 production_group（PG-01～04）；Clip/DO 仅为显示别名。这样保留无人建立、到门前、门完全打开、强光 Reaction 四个不可替代的可见结果。
- **首轮策略不预判**：若核验到当前入口支持足够窗口与受控多镜，可比较 `REQ-LONG-01`；若能力仍未知、窗口不足或只有单镜证据，则采用按状态边界拆分的四个短请求计划。
- **桥接是条件修复**：仅在真实主体段通过、接口失败后局部启用，优先保护合格段；真实尾帧不合格时冻结下游。
- **真实性声明**：目前仅完成规划文件。没有调用 Seedance，没有上传素材，没有任务 ID，没有生成结果，没有评审结论，没有剪辑采用段，也没有成片。
