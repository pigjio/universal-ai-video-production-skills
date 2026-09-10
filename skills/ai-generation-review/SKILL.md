---
name: ai-generation-review
description: "用于评审 AI 生成的角色、环境、物体、抽象图像、分镜帧及 Seedance/即梦视频；한국어로 ‘생성 결과가 왜 어색한지 먼저 진단해 주세요’라고 해도 트리거된다. Use when judging identity, space, geometry, action, direction, props, camera, information boundaries, audio, tail-frame usability or repair priority. Separate observations from competing causes, design distinguishing tests, route post-fix/regeneration/storyboard return, and never infer motion or sound from stills."
version: 0.5.1
author: Domain Knowledge Distillation
license: MIT
metadata:
  hermes:
    tags: [review, evidence, quality-gate, continuity, ai-generation, seedance, diagnosis]
    related_skills: [ai-prompt-execution-contract, ai-video-production-classroom, ai-character-design, ai-scene-design, ai-storyboard-design]
---

# AI 生成结果评审｜证据、诊断与回归

## 新手逐轮引导与阶段成果落盘

任何交互先加载 `references/novice-guidance-protocol.md`；评审状态、授权、证据、人工裁决和依赖同时加载 `references/common-contract.md`。引导只降低交互负担，不删减证据边界、十维评审、竞争根因、回归和人工裁决。

阶段落盘必须保存完整正文，并在写后回读通过后更新 `PROJECT_INDEX.md` 与 `SESSION_HANDOFF.md`；这三个文件及其状态必须相互一致。

- 每轮只推进 **1 个小目标**，最多问 **1 个真正阻断当前目标的问题**；“不知道/你先看/都可以”合法。首轮即给小产出，例如按现有证据写一条“可判/不可判”观察，或列十维中最优先的一维及依据，不得只索取全套材料。Agent 补全必须标假设且可撤销。
- 用户否决假设时只撤销受影响判断；已有评审默认局部修改。跨会话先读项目索引、阶段交接、最新评审和所引证据；不可读时明确受阻，以用户最小摘要继续，不能伪造看过媒体或时间码。
- “看起来对/可以/继续”等积极反馈不等于阶段完成、保存授权、被评对象通过、人工裁决或研究同意。先交完整可独立阅读的评审正文。已有有效持续保存授权时，只问是否确认“评审报告阶段完成”，明确确认后直接保存；没有持续授权时，用一个合并问题主动提供“确认报告并保存为新的 Markdown 版本 / 确认但暂不保存 / 继续修改”三种自然选择，并说明预计文件名与已知目录。只有明确确认才把**报告自身**标 `confirmed`，被评对象仍按真实证据与人工裁决保持其状态。
- 确认与保存授权不得互相推导，但不得拆成两轮重复询问。目录未知时并入同一个收尾问题；用户选择保存且目录明确后，自动创建缺失的项目基础记录文件。保存授权不等于接受作品、重生成、上传、发布或研究授权。
- 主文件名为 `生成评审_对象_vNNN.md`，保存观察范围、证据位置/时间码、适用性、十维矩阵、症状、竞争根因、区分证据、修复/回归、人工裁决与未决项的**完整正文**，不能只存分数或摘要。证据不足保持 `unconfirmable`，人工未明确则 `pending`。
- 写前扫描版本，使用下一未占用三位号，旧评审不覆盖；写后回读核对，再更新项目索引和阶段交接。写入、回读、索引或交接失败只报未完成/部分完成。Skill、文件、图片、视频或音频工具不可用时交完整证据缺口评审/人工观察清单，不伪造观察、通过或人工裁决。
- 保存作品不等于同意研究、评测、训练、公开、上传、留存或二次使用；专项用途另取明确可撤销同意。

## 1. 边界与入口

评审对照任务与真实产物，不以“整体更漂亮”替代符合要求，也不把生成偶然性升为项目设定。分别报告观测、合规判断、根因假设和人工裁决。评审可以完成而人工决定仍 pending；代理通过不等于人工接受。

先判断工作深度：讨论时可针对一个疑点给出证据边界、竞争解释或局部评审草案，不强制完整公共头、全片检查或落盘；探索草案可比较修复责任层与最小试验，但不把候选结论升为通过；正式成稿只完整交付用户指定的评审范围。仅在生产交接/验证、明确要求登记受管理评审，或受管理上游换版时加载 `references/common-contract.md`，使用同一公共头、失效传播、写入和证据协议。授权落盘后保留旧稿。项目可改风格与验收偏好，不能授权虚构已看见内容或未发生的人工确认。

| 条件 | 加载文件 | 应得到的判断/输出 |
|---|---|---|
| 进入正式观察/验证、证据不完整或只有截图 | `references/evidence-and-scope.md` | 可判/不可判范围、取证步骤、缺证据出口 |
| 评审 Seedance/即梦视频、尾帧续接资格或视频返修 | `references/seedance-video-ten-dimension-review.md` | 十维观察、症状竞争解释、三路裁决和尾帧传播门 |
| 有失败症状、需要归因、修复或上游换版 | `references/routing-and-regression.md` | 竞争根因、区分证据/最小试验、责任层和回归 |
| 输出任何评审交接 | `references/review-template.md` | 公共头、适用性矩阵、人工 pending 与修复记录 |
| 需要环境/物体/抽象完成及失败示范 | `references/worked-examples.md` | 完成评审记录、失败诊断与有限证据边界 |
| 检查来源与继承缺陷修正 | `references/source-map.md` | 源版位置及证据协议增强说明 |

## 2. 判定词与证据协议

检查项状态为：

- `pass`：在声明范围内有证据支持满足要求。
- `fail`：可见/可听证据明确违背要求。
- `suspicious`：有具体疑点，但不足以判失败。
- `unconfirmable`：当前证据类型、质量或覆盖不足，不能判断。

不适用不是 pass：用独立 `applicable: false` 和理由，item_status 可为 null。environment-led/object-led/abstract 可 `character: null`，角色身份、表演与潜台词不强制评审；仍核对相关物体结构、空间/材料、变化范围与终点。narrative/perceptual/conceptual 用相应完成判据，不强塞 Narrative Job。

图片记录文件/版本、观察区域、可见事实和对照要求；不推断背面、遮挡后结构或生成过程。视频记录文件、完整观看/抽样区间、时间码、帧/区域、音轨检查方式。单张截图不能确认动作顺序、连续性、全片时长或声音；局部截图不能代表全片。文件存在不等于已观看，媒体元数据有音轨不等于已听过内容。

## 3. Seedance 视频十维入口

视频结果按适用性检查十维：**身份、空间、几何、动作、方向、道具、摄影、信息边界、声音、尾帧**。每维都要记录要求、证据位置/时间码、观察范围、状态和接口影响；不适用独立记录，不能当 pass。

- 身份/空间漂移是症状，不是根因；先查实际上传、素材冲突、景别/遮挡、动作与运镜负荷、原片/后期和随机性。
- 动作按起点→预备→启动→路径→接触→结果→Reaction 检查；后一镜重演已完成动作同样是失败信号。
- 刚性墙面、地面、桌面、门框和器具的液化/弯折属于几何维度，不能只看角色。
- 信息边界同时检查完整画幅边缘和音轨，未来人物、能力、地点或声音不得无授权提前出现。
- 尾帧必须连续观看邻近区间；身份、空间、几何、方向或关键道具错误时禁止作为下游参考。

裁决摘要：原片正确而后期引入问题→后期；输入/合同可修且导演意图不变→重生成；必须改变景别、机位、轴线、镜头数量、Reaction/Decision 或首次揭示→退回分镜。只有源资产自身矛盾才退资产层。单次随机失败不能证明责任层。

## 4. 评审闭环

1. **冻结参照**：读取本轮真实结果、实际 Prompt/素材/参数及必要上游版本。要求不明确时先作描述性观察，不能伪造合规标准。缺上传日志时标不能核对实际绑定。
2. **判定适用性**：按模式与主体类型选择身份、空间、结构/材质、动作、表演、摄影、声音和续接接口；静态不评运动，抽象不强制地面支撑/物理接触。
3. **记录症状事实**：例如“入口在该帧从左移至右”，先核对是否授权反打/反向视角，不能直接称空间拓扑坏了。用户指出某缺陷时围绕该缺陷取证，不偷换成较易观察的问题。
4. **逐项判定**：引用区域/时间码和要求；分清可见失败、可疑、无法确认。结果新构图可能有价值，但先登记候选。
5. **列竞争根因**：身份漂移可来自错误上传、参考冲突、遮挡/尺度、动作负荷、采样或模型限制；空间漂移可来自参考拓扑、机位表达、镜头边界、生成重建或后期镜像。不得直接路由角色母版或场景重做。
6. **区分证据/最小试验**：优先查原始文件、实际上传回执、提交快照、剪辑前后差异等无需新生成的证据；需要生成时提出可区分假设的对照，记录控制变量与预期结果。单次随机生成不能证实根因；重复比较也只支持当前条件，不宣称模型普遍规律。
7. **授权修复并回归**：基于证据选择最小负责层。默认一次控制一个主变量用于诊断；耦合变量可联合修复，但须明确为什么不能分开、联动范围、保护项与无法独立归因的限制。修复不是试验成功，必须重新观察结果及受影响接口。
8. **人工裁决**：无明确用户原话/审查记录则 `human_decision: pending`；接受、拒绝、局部吸收、退回均需引用证据。缺裁决不阻止交付评审报告，但不能晋级 human_confirmed 或覆盖批准资产。

## 5. 条件路由，不把症状当根因

| 区分证据支持的责任层 | 修复方向 | 回归范围 |
|---|---|---|
| 实际上传与目标版本不符，或职责语义互相覆盖 | Prompt/生产绑定 | 身份/材质及动作、空间是否被连带改坏 |
| 源资产自身在必要视角/结构已矛盾 | 角色/场景/物体资产 | 所有采用该版本且受影响的下游 |
| 镜头/动作合同缺路径、支撑或状态边界 | 分镜或提示词 | 原失败动作、前后状态及观看任务 |
| 提交正确，复杂请求反复失败，较简单对照改善 | 生产能力/分组候选 | 质量、接口连续性、重试成本；不能称已唯一归因 |
| 世界规则/状态逻辑自身冲突 | 世界/剧本；无叙事时回概念/材料规则 | 变化条件及后续结果 |
| 源片正确、后期引入镜像/切点/音量问题 | 后期 | 修改区间、相邻连接、最终音画 |
| 证据不足，假设仍竞争 | 暂不固定责任层 | 请求素材/日志或最小试验，不盲目重做上游 |

## 6. 输出合同

详细模板见 `references/review-template.md`；下列公共头与核心 payload 同样可直接交接。制品 version 与技能 0.5.0 分开。

```yaml
artifact_id: REVIEW-example
version: v1
artifact_type: review
creative_mode: perceptual
subject_type: environment-led
lifecycle_status: draft
production_status: not_applicable
approval_level: none
upstream_versions: {}
confirmed_evidence: []
open_questions: []
recheck_trigger: []
next_action: request_evidence
payload:
  character: null
  result_artifact: null
  actual_input_record: null
  requirement_refs: []
  observation_scope: {visual: null, intervals: [], audio: not_checked, method: null}
  facts_observed: []
  review_matrix: []  # applicable、requirement、evidence、scope、item_status
  symptoms: []
  competing_root_causes: []
  distinguishing_evidence: []
  minimal_tests: []
  repair: {responsible_layer: undetermined, allowed_changes: [], coupled_rationale: null}
  regression: {protected_scope: [], affected_checks: [], adjacent_interfaces: []}
  rollback_path: null
  human_decision: pending
  human_decision_evidence: null
  proposed_upstream_changes: []
```

`production_status: not_applicable` 属于评审文档自身；受评 clip 的状态在其生产记录更新为 under_review/reviewed，不把 review 文档当生成视频。completed 不是新增公共状态。

## 7. 受阻分支与上游改版

- 无视觉/视频/音频观察工具：可核对文本合同和文件元数据，但观察范围如实写；需实际观看项 unconfirmable，交人工观察清单，不能装作看过。
- 缺结果文件或只有失效链接：请求真实媒体；可完成“证据缺口评审”，不得填图像区域/时间码事实。
- 生成提交失败：评审实际失败日志和合同，不把不存在的画面判 fail；生产记录 failed，视觉判 unconfirmable。
- 用户拒绝补素材/重生成：保留已观察结论和拒绝依据，不擅自调用；未判项保持 unconfirmable。
- 人工等待：pending 合法，next_action 指向 await_human_review；拒绝是否为影片质量拒绝、补素材拒绝或执行拒绝应分别记录，不能相互替代。
- 上游换版：对直接及传递受影响依赖标 needs_recheck，保留旧批准历史但取消其当前门禁效力；例如场景拓扑改变使 Prompt、Clip、Review 的空间结论待复核。无关项经影响检查可保留理由，不一刀切全包失效；完成重审才恢复 confirmed。

## 8. 质量闸门

- [ ] 必要参照版本、真实输入与观察能力明确，character:null 和非叙事完成判据可贯通。
- [ ] Seedance 视频十维按适用性逐项记录；方向、道具、信息边界与尾帧没有被并入泛泛“连续性”。
- [ ] 坏尾帧已标不可复用；文字重启没有冒充真实尾帧续接。
- [ ] 后期、重生成、退回分镜与退回资产层有证据门，不凭单次随机失败跳层。
- [ ] 事实与解释分开，证据位置/时间码和观察范围完整。
- [ ] 没用静帧证明动作、连续性或声音，没有用元数据代听觉检查。
- [ ] pass/fail/suspicious/unconfirmable 与不适用分开。
- [ ] 身份/空间仅作为症状，竞争根因及区分办法已列；单次随机生成未被当因果证明。
- [ ] 修复范围受控；必要的联合修复有耦合理由和归因限制。
- [ ] 回归覆盖受影响项与前后接口，旧结果和回退路径保留。
- [ ] 人工裁决真实或明确 pending；局部通过未扩大为全片通过。
