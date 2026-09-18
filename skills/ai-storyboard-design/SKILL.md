---
name: ai-storyboard-design
description: "Use when discussing, exploring, designing or diagnosing narrative and non-narrative AI storyboards. 支持分镜讨论与非叙事感知/概念序列，比较构图语气、视觉七要素、空间显隐和试讲反馈；按需深化 Beat、Blocking、连续性、Timing 与 Animatic 交接，不替代平台 SOP。한국어로 ‘이 장면을 스토리보드로 나눠 주세요’라고 해도 트리거된다."
version: 0.7.0
author: Domain Knowledge Distillation
license: MIT
metadata:
  hermes:
    tags: [storyboard, shot-design, visual-storytelling, blocking, continuity, timing, animatic]
    related_skills: [ai-screenplay-development, ai-character-design, ai-scene-design, ai-prompt-execution-contract, ai-video-production-classroom, ai-generation-review]
---

# AI 影像分镜设计｜完整可执行封装

## 新手逐轮引导与阶段成果落盘

任何交互先加载 `references/novice-guidance-protocol.md`；涉及状态、授权、证据、依赖或交接时同时加载 `references/common-contract.md`。真实性与用户授权优先；引导协议不削弱 Beat、Blocking、连续性、Timing、Animatic 与证据闸门。

阶段落盘必须保存完整正文，并在写后回读通过后更新 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`；这三个文件及其状态必须相互一致。

- 每轮只推进 **1 个小目标**，最多提出 **1 个真正阻断当前小目标的问题**。“不知道/你先建议/都可以”合法；给可撤销、标明假设的默认方案。首轮必须有小产出，例如 Scene Director Brief 的三行骨架、前三个 Beat 或两种镜头策略，不得只发输入问卷。
- 用户否决 Agent 假设时立即撤销对应项，仅改受影响范围；已有分镜/剧本默认局部修改。跨会话先读项目索引、阶段交接和最新版本恢复已定、暂定、否决及未决；不可读取时说明边界，以最小摘要继续，不假装已恢复。
- 积极反馈不等于阶段完成、保存授权或研究同意。先交完整可独立阅读的本阶段正文。已有有效持续保存授权时，只问是否确认本阶段完成，明确确认后直接保存；没有持续授权时，用一个合并问题主动提供“确认并保存为新的 Markdown 版本 / 确认但暂不保存 / 继续修改”三种自然选择，并说明预计文件名与已知目录。只有明确确认后，产物才可标 `confirmed`，否则保持 `draft/candidate`。
- 阶段确认与写文件仍分属不同授权，但不得拆成两轮重复询问。目录未知时并入同一个收尾问题；用户选择保存且目录明确后，自动创建缺失的项目基础记录文件。持续授权可撤销，不扩展到上传、付费生成、发布、研究、评测、训练或留存。
- 主文件名为 `分镜_场次_vNNN.md`。保存 Director Brief、Beat、Blocking/Floor Plan、逐镜卡、Timing/声音/接口、风险与未决项等**完整正文**，不能只存摘要或修改清单。扫描已有版本并使用下一未占用三位号，绝不覆盖旧版。
- 写后回读核对存在性、版本与正文关键段，再更新项目索引和阶段交接的路径、版本、状态、上游依赖、未决项、下一动作。任何写入、回读、索引或交接失败都报告未完成/部分完成，不报成功；Skill、文件或媒体不可用时给完整可复制 Markdown 与恢复清单，不伪造观察。
- 保存作品不等于同意研究、评测、训练、公开、上传或二次使用；这些用途须另取明确、可撤销的专项同意。

## 1. 这项工作解决什么问题

分镜不是把剧本句子逐句画出来，也不是罗列景别和运镜。分镜把戏剧行动重新组织为观众能够连续读取的视觉经验：观众先看见什么、理解什么、感受到什么，角色如何行动、反应并作出下一次选择，以及这些变化如何通过镜头、剪辑和时间被证明。

```text
剧本场景
→ Scene Director Brief
→ Story Beat
→ Blocking / Floor Plan
→ Thumbnail与视觉焦点
→ Shot Design
→ Continuity / Editing
→ Timing / Animatic
→ Layout、视频生成和动画交接
```

本技能服务叙事及非叙事 AI 短片、短动画和学生练习。它负责导演层的判断，可在探索中提出标明假设的视觉试写；不擅自改写剧本或确认场景 Canon，不替代最终平台 Prompt，也不把项目案例写成通用规则。

先选本轮交互模式：**讨论**直接回答或试写；**探索草案**允许未知、可替换假设和联动候选；**正式成稿**只完成指定范围；**生产交接/验证**或受管理产物上游改版才加载 `references/common-contract.md`，处理公共头、授权、证据和依赖复核。讨论不要求母版、动作测试、完整流程、落盘或生产包；探索候选不等于正式可交接 candidate。感知型、概念型以感知或形式变化替代人物冲突；无角色允许 `character: null`，人物字段与闸门不适用。

共同讨论循环：当前意图 → 直接判断/具体试写 → 必要的替代与代价 → 吸收反馈 → 只改受影响项。内部保留已定、暂定、否决原因和开放项，不要求固定表格或每轮收敛；输入足够就成稿，只追问影响当前判断的缺口。AI 预测不冒充观众反馈。

核心判断：七要素（空间、线、形、明度、色彩、运动、节奏）可选择主导变量跨段组织，不只换景别和时长。制作空间成立不要求观众全时清楚；平面、有限、暧昧与长镜头可主动设计。固定机位与运镜比较信息、关系和感知作用，不按主体是否位移一刀切。探索可联动，故障诊断优先单变量，均保护已批准共享约束。

## 2. 核心知识模型

### 2.1 分镜的最小单位是 Beat，不是句子

当目标、阻力、信息、情绪、关系或决定发生变化时，才形成新的 Beat。同一动作若没有新的信息或状态，不必机械切镜；但首次证据、角色 Reaction、主动 Decision 和不可逆 Result 不能为了省镜而删除。

### 2.2 每个镜头有一个 Narrative Job

一个镜头可以包含连续动作，但只保留一个主要观看任务，例如：建立空间关系、显示接触、揭示证据、承接反应、展示决定或锁定结果。景别、角度、运镜和声音只有在改变信息、关系、情绪、空间理解或节奏时才有存在理由。

### 2.3 动作是状态转换

每个动作都用以下链条检查：

```text
输入状态
→ Anticipation / 触发
→ Action Start
→ 路径与接触 / 失败
→ Result
→ Reaction
→ Decision-Action
→ 输出状态
```

“角色走过去”“他看见了”“门打开了”不是完整动作，除非明确起始位置、动力、接触或证据、结束状态和对后续的影响。

### 2.4 观众读取有顺序

每镜应说明：第一眼看什么，第二眼发现什么，何时理解变化，切点由什么触发。构图、明度、色彩、剪影、视线、运动和声音共同管理注意力，不能只靠文字解释。

### 2.5 连续性不是装饰，而是因果可读性

优先保护：

```text
情绪与故事理解 > 动作方向与眼迹 > 道具/支撑面 > 二维平面 > 三维空间细节
```

实际项目中仍需同时记录屏幕方向、轴线、人物位置、左右手、重心、道具状态和声音桥，避免用“承接上一镜”掩盖断裂。

## 3. 输入诊断与工作模式

按当前问题读取必要输入；下表用于完整设计，讨论不要求补齐全部字段：

```yaml
project:
  medium: narrative_ai_short / animation / film / previs
  audience:
  duration:
  visual_constraints:
scene:
  task:
  location:
  input_state:
  output_state:
  irreversible_change:
  audience_question:
characters:
  goals:
  obstacles:
  relations:
  core_verbs:
assets:
  confirmed_character_refs:
  confirmed_scene_refs:
  props_and_states:
open_decisions:
  -
```

根据用户意图选择一个主模式：

| 模式 | 先解决什么 | 首个输出 |
|---|---|---|
| 场级规划 | 戏剧任务、信息边界、结果 | Director Brief + Beat List |
| 逐镜设计 | 动作、焦点、镜头职责 | Shot Cards |
| 空间混乱 | 支撑面、路线、轴线、入口出口 | Floor Plan + 地标链 |
| 节奏问题 | 观看时间、Hold、动作相位 | Timing Sheet |
| 连续性问题 | 尾帧—起帧状态接力 | Transition Audit |
| 生成交接 | 资产职责和镜头执行输入 | Handoff Brief |

如果叙事因果缺口阻断当前设计，标记缺口并建议回到 `ai-screenplay-development`；讨论可先给条件方案，不因缺角色目标而阻断非叙事设计。如果确认图与旧文字冲突，以当前已确认资产和人工裁决为准，并把冲突单列为待裁决。

## 4. 按任务范围选用的方法（不是每轮强制完整流程）

### Step 1：建立 Scene Director Brief

```text
场景任务：这一场必须完成什么？
角色目标：谁主动想得到什么？
主要阻力：什么具体阻止他？
观众问题：观众在等待哪个答案？
信息分配：角色知道什么，观众知道什么？
输入状态：场景开始时人物、道具、空间是什么状态？
输出状态：场景结束时什么改变？
不可逆变化：什么不能在下一镜假装没有发生？
空间锚点：入口、出口、地标、支撑面、轴线。
信息边界：本场不得提前泄露什么？
```

质量要求：场景必须至少有一次状态或价值变化；如果只是气氛展示，要明确其视觉/感知任务，而不要强行伪造冲突。

### Step 2：拆 Story Beat

为每个 Beat 写：

```text
Beat ID：
目标 / 阻力：
可见行动：
新增信息：
情绪或关系变化：
Reaction：角色如何理解刚发生的事？
Decision-Action：角色下一步主动选择什么？
结果与下一 Beat 钩子：
```

合并重复证明，保留以下不可替代节点：首次出现、首次证据、失败、反应、决定、代价、不可逆结果。若删除一个 Beat 后后续因果完全不变，它很可能是冗余。

信息增量不只指新事件，也包括观众理解、期待、情绪、空间关系或感知节律的变化。删镜后这些作用仍完整才考虑合并；不能把有功能的静止误判为无信息。负载按注意力转移次数、陌生空间、动作相位、台词/字幕竞争和读取难度判断，不用固定秒数或镜数阈值。若负载过高，先简化竞争焦点、调整演绎时间，再决定是否切镜，并在 Animatic 中验证。

### Step 3：建立 Blocking / Floor Plan

先在平面上标记：

- 角色起点、终点和行动路线；
- 目标与阻力的方向；
- 固定道具、支撑面和可接触边界；
- 入口、出口和过渡空间；
- 摄影机可用区域；
- 屏幕左右、轴线和视线落点。

复杂空间使用地标链：

```text
上游尾帧位置
→ 第一真实落脚面
→ 可见入口/过渡边界
→ 穿越边界
→ 内部目标位置
```

“看见入口”不等于“已经进入”。需要连续展示穿越因果时，用落脚、视线或支撑面变化证明关键节点；允许有意省略过渡，但新镜须以空间锚点、声音桥或明确时间省略让观众重新定位，不把省略误写成连续运动。

### Step 4：先做 Thumbnail，再做漂亮画面

Thumbnail 的任务是测试大形和观看路径，不是完成美术。每个候选构图检查：

1. 角色、目标、阻力的关系是否一眼可读；
2. 深/平面/有限/暧昧空间线索是否符合意图，而非必须前中后景齐全；
3. 视觉焦点是否由明度、大小、轮廓、方向或对比支持；
4. 角色剪影和行动方向是否清楚；
5. 摄影机是否站在能证明动作的位置。

缩小或灰度观察仍读不出关系时，先改构图、Blocking、景别或明度，不要增加细节。

### Step 5：选择景别、角度、POV 与运镜

涉及具体景别类别、人物裁切、客观/主观/POV/OTS、景别曲线或“为什么用这个镜头”时加载 `references/shot-language-taxonomy.md`。每个镜头先追溯剧本中的场景功能、动作、信息、Reaction/Decision、空间或声音依据，再选择能让关键证据可读的景别；景别是叙事距离，不按模型常识随意装饰。

| 选择 | 主要功能 |
|---|---|
| 宽景 | 空间、路线、人物关系、后果 |
| 中景 | 完整动作、调度、人与物关系 |
| 近景 | 反应、表情、接触、选择 |
| 特写 | 唯一关键证据或细节 |
| POV | 某角色真实可见的信息，不等于全知镜头 |
| 高/低角度 | 改变力量、脆弱、压迫或观察关系 |
| 推拉摇移/跟拍 | 只有在信息、空间、关系、情绪或节奏发生变化时使用 |

先问“观众现在需要知道什么”，再问“用什么镜头拍”。相邻镜头若角度、焦点和画面结构完全相同，必须说明重复的功能，否则合并或制造有意义的对比。

### Step 6：写逐镜卡

人物改变策略、压抑情绪或无对白决定时，先沿剧本意图选择可见证据，不把“悲伤/紧张”直接换成通用表情；需要补意图时经剧本阶段读取[表演节拍](../ai-screenplay-development/references/performance-beat-and-physical-action.md)，身份/习惯脸回角色的表演参考。有对白不自动切说话者：比较听者反应、同场画外声和声音桥，写清谁能听见、何时听见；声音执行交提示词阶段。跨阶段覆盖由总控的[意图追踪参考](../ai-creative-workflow-router/references/creative-intent-traceability.md)维护，不让生产层为避风险擅改镜头。

```text
镜头编号 / 时长：
Narrative Job：本镜唯一观看任务。
起始状态：人物、道具、空间和重心。
构图与焦点：第一眼→第二眼，前中后景关系。
动作链：触发 → 起动 → 路径/接触/失败 → 结果。
Reaction / Decision：可见反应与下一次主动选择。
景别 / 角度 / POV / 机位：
运镜与停稳：运动由什么触发，何时停下。
声音与切点：声音来源、重音、桥接和切入切出理由。
尾帧接口：下一镜实际继承什么。
不得提前出现：
```

避免用统一套话填充“更详细”。细节只有在改变空间、动作、注意力、声音或连续性时才加入。

### Step 7：检查动作接力和镜间接口

逐对检查上一镜尾帧与下一镜起帧：

```text
位置 / 重心 / 姿态
左右手 / 道具 / 接触点
支撑面 / 屏幕方向 / 轴线
视线落点 / 动作相位 / 速度
情绪输入 / Reaction 是否已完成
声音桥 / 已完成动作是否被重启
```

前一镜—当前镜—后一镜至少一起复核。若发现断裂，先判断是 Beat 拆分问题、Blocking 问题、动作相位问题、资产状态问题还是执行描述问题，再回最小必要层。

### Step 8：制作 Timing Sheet 与 Animatic

每镜拆出：

```text
信息读取时间
Anticipation
动作启动
Contact / Failure
Result
Reaction
Hold
声音重音与切点
```

先保留完整演绎，再在 Animatic 中压缩。压缩时优先删除重复证明和无功能 Hold，不得为了适配平台时长切断失败、Reaction、Decision 或代价。镜头标题上的秒数不能替代真实动作负载检查。

计时与编号回归加载 `references/timing-verification.md`；交叉剪辑、威胁应对或表情断裂时加载 `references/threat-response-and-emotion-continuity.md`。分别记录银幕时间与故事事件时间，画外动作不能因切镜暂停；后镜继承前镜情绪，变化须有可辨识的触发或明确省略。

## 5. 诊断与回退矩阵

| 症状 | 优先排查 | 最小回退 |
|---|---|---|
| 画面漂亮但看不懂 | Scene Task、焦点、Blocking | Brief / Thumbnail |
| 人物像在等待 | 目标、阻力、主动行动、Decision | Beat |
| 动作像结果切片 | 起始状态、触发、路径、Contact | Action Chain |
| 反应消失 | 时长、镜头任务、切点 | Beat / Timing |
| 空间瞬移 | 支撑面、地标链、轴线、入口 | Floor Plan |
| 左右手/道具穿帮 | 状态、接触点、参考职责 | Continuity Ledger |
| 相邻镜头重复 | POV、焦点、角度、功能对比 | Shot Design |
| 节奏匀速 | 信息强度、静动波、Hold和切点 | Timing / Animatic |
| 镜头提前泄露结果 | 信息分配、禁止提前出现 | Beat / Scene Brief |
| 角色身份漂移 | 实际资产、参考职责、平台读取、Prompt冲突 | 先修输入，再判断是否回角色母版 |

禁止把“重写整场”作为默认修复。故障诊断优先一次只改变一个主要变量，便于归因；探索允许机位、光色、调度、顺序联动比较，保留前版和整组差量，不把方案胜出伪称单因素因果。试讲后按反馈只改受影响项，详见 `references/pitch-feedback-and-exploration.md`。

## 6. 按正式交付范围适用的质量闸门（讨论不要求生产证据）

### 场级闸门

- [ ] 场景任务、观众问题和输出状态明确；
- [ ] Beat 之间存在因果或信息推进；
- [ ] 角色有可见目标、阻力、Reaction 和 Decision；
- [ ] 不可逆变化没有被中间镜头抹平；
- [ ] 空间入口、出口、支撑面和路线成立。

### 镜头级闸门

- [ ] 每镜的主要观看职责清楚；非叙事用感知/概念任务，复杂镜内转折按读取负载验证；
- [ ] 起始状态、动作过程和结果可见；
- [ ] 第一眼焦点明确；
- [ ] 景别、角度、运镜和声音具有功能；
- [ ] Thumbnail 缩小/灰度后仍能读出关系和动作；
- [ ] 没有把未来信息提前泄露。

### 序列与 Animatic 闸门

- [ ] 尾帧到起帧状态连续；
- [ ] 角色、道具、手、支撑面和屏幕方向没有瞬移；
- [ ] 动作时长覆盖 Anticipation、Contact、Result、Reaction；
- [ ] 节奏有强弱变化而非平均切分；
- [ ] 声音、切点和视觉动作相互支持；
- [ ] 下游可以读取当前状态和真实尾帧。

证据不足时标记为“无法确认”，不得判定通过。单张截图不能证明完整视频的动作顺序、连续性或声音；必须记录已观察范围和证据时间码。

## 7. 输出与交接

根据任务只交付必要层级：

```text
场级：Director Brief + Beat List + 风险与待裁决
规划级：Floor Plan + Thumbnail逻辑 + Shot List
逐镜级：Shot Cards + 动作/反应/接口
Animatic级：Timing Sheet + Hold/切点/声音节拍
下游级：稳定镜头、资产职责、起始状态、结束状态、尾帧接口
```

生产交接及需登记状态/依赖的正式记录使用以下公共头，具体内容放 payload。讨论、探索不强制该头，正式成稿只交指定范围；不得为了填满字段编造批准或证据：

```yaml
artifact_id: SB-example
version: v1
artifact_type: storyboard
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

稳定 ID 不含版本，upstream_versions 为稳定 ID 到版本的映射。确认依据只能引用真实证据或人工裁决；方向批准不代表生产批准、生成完成或进入 Canon。generated 必须有真实返回 ID 或文件。上游改版时直接及传递受影响依赖标为 needs_recheck，保留旧批准历史但不再作为当前有效门禁，重审后才恢复 confirmed；无关依赖记录影响检查理由后可保留。

## 8. 按需加载的参考资料

- `references/common-contract.md`：生产交接/验证及受管理产物上游改版时加载公共状态、证据与写入合同。
- `references/visual-structure-and-space.md`：只换景别却节奏平、构图语气比较、长镜头或主动隐藏空间时加载，选择七要素主导变化与重新定位线索。
- `references/pitch-feedback-and-exploration.md`：需要试讲、吸收实际反馈、删合调序或区分联动探索/单变量诊断时加载；缺证据时选低成本验证，不强制完整 Animatic。
- `references/timing-verification.md`：计算镜头/场景/全片时长、核编号与映射及修订回归时加载。
- `references/threat-response-and-emotion-continuity.md`：并行事件、威胁等待、情绪跳变或信息负载失衡时加载。
- `references/source-map.md`：需要定位源技能与参考资料、核来源边界时加载；来源不是执行依赖。
- `references/storyboard-methodology-map.md`：十类专业来源与方法互补关系；需要追溯知识来源时读取。
- `references/director-decision-layer.md`：观众体验、Goal/Opposition/Decision、Reaction和技法功能判断。
- `references/shot-language-taxonomy.md`：具体景别、人物裁切、视点、角度、景别曲线及剧本依据链。
- `references/detailed-shot-expansion.md`：从场级结构扩写到逐镜卡时读取。
- `references/storyboard-quality-gates.md`：进行系统质量审查时读取。
- `references/shot-transition-audit.md`：逐对审查镜间尾帧—起帧时读取。
- `references/full-performance-before-timing-compression.md`：需要压缩时长或制作 Animatic 时读取。
- `references/scene-shot-size-rhythm-rebuild.md`：景别和节奏平坦时读取。
- `references/v3-action-relay-continuity.md`：动作接力或多镜动作连续性出错时读取。

这些参考文件是通用方法的深层支撑，不包含任何项目 Canon。平台 DO/Clip、素材上传、平台参数和实际视频生成交由 `ai-video-production-classroom`。

## 9. 常见误区

1. 把剧本句子逐句翻成镜头；修复：先拆 Beat 和状态变化。
2. 先选漂亮机位再寻找动作；修复：先写目标、阻力、接触和结果。
3. 一个长镜头的注意力转折读不清；修复：先调镜内调度、光色显隐和停留，仍超负载才切镜，不强制拆长镜头。
4. 删除 Reaction 和 Decision 以凑时长；修复：先删重复证明，再压缩 Hold。
5. 把确认图当作完整空间而不核对支撑面；修复：先做 Floor Plan 和地标链。
6. 用“承接上一镜”代替接口；修复：逐项写位置、姿态、道具、视线和声音。
7. 只看单张图就判定视频连续；修复：记录观察范围和时间码。
8. 生成结果改变剧情后反向修改 Canon；修复：结果先作候选，人工确认后才吸收。

## 10. 生产交接最终执行检查（讨论/局部成稿不套完整清单）

- [ ] 我当前处理的是导演/分镜问题，而非未解决的剧本或平台问题；
- [ ] 我读取了当前有效的角色、场景和道具约束；
- [ ] 我先写了场级任务或 Beat，而不是直接堆镜头术语；
- [ ] 每镜都能说明观众第一眼看什么、发生什么、结果是什么；
- [ ] Reaction、Decision、代价和不可逆变化没有被删除；
- [ ] 动作、空间、声音和时间都通过证据检查；
- [ ] 版本、状态、上游引用和待裁决项已记录；
- [ ] 输出可以直接交给下游，而不要求下游猜测缺失状态。
