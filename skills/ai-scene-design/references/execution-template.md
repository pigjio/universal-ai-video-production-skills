# 场景执行记录与阶段交付模板

生产交接/验证及受管理产物上游改版时加载 `common-contract.md`。生产记录使用此完整头，专项字段放 payload，不另造生命周期。讨论和探索不强制公共头、母版或测试；正式成稿只交用户指定范围，不把全部字段变成入场要求。仅讨论不写文件；授权落盘时确认项目目录并保留旧批准版本。

```yaml
artifact_id: SCN-example
version: v1
artifact_type: scene
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
payload:
  character: null
  function: ""
  first_read: ""
  second_read: ""
  perceptual_or_narrative_change: ""
  world_evidence: []
  space:
    boundaries: []
    entry_exit: []
    landmark_chain: []
    support_surfaces: []
    scale_reference: ""
    action_or_motion_envelope: []
  camera: {position: "", direction: "", aspect_ratio: "", visual_flow: ""}
  neutral_combination_test: {method: "", evidence: [], result: pending}
  light_key: {source: "", direction: "", area_and_falloff: "", fill: "", shadow: ""}
  look: {value: "", color: "", materials: [], weather: ""}
  color_script: []
  baseline_state: ""
  variant_delta: {keep: [], change: [], add: [], remove: []}
  assets: []
  handoff: {recipient: "", invariants: [], variables: [], unresolved: []}
  quality_check: {result: pending, reasons: []}
```

## 填写与裁决

先填任务与信息层，再空间、动作包络、机位，最后光色。字段未知写 open_questions，不编实际尺寸或图像结果。质量检查 result 的 pass/hold/rework/pending 是单项判断，不替代公共生命周期、生成进度或批准层级。

规范填写样例：SCN-window、v1、perceptual、environment-led；character 为 null；基准是破窗与褪色窗帘；任务是观察布边遮光的节奏；运动包络是帘布最大摆幅，不需要角色站位或人物阻力。neutral_combination_test 记录“待灰盒/连续草图”，confirmed_evidence 保持空。

未通过时把可见症状、相关锚点、最小修改、复测方法放 handoff.unresolved。接收方应能回答“哪个状态、哪些字段不能动、哪里尚未验证”，否则交接不完整。
