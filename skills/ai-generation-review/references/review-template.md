# 完整评审记录与交接模板

加载条件：输出任何评审交接时加载。先用 evidence-and-scope.md 确定范围，有症状再用 routing-and-regression.md；公共头服从 common-contract.md。

## 填写顺序与门禁

1. 填真实受评文件/版本与要求，缺失字段保持 null 并列问题，不从文件名猜画面。
2. 写观察方法、范围和证据索引；逐项判 applicable 与四种 item_status。
3. 症状与根因分栏，给竞争假设、区分办法和授权修复；无证据不固定责任层。
4. 写回归保护与回退，保留人工 pending。评审文档 production_status 为 not_applicable；受评 clip 的 under_review/reviewed 属于其自己的记录。
5. 交付前核对任何接受/拒绝是否有明确裁决来源。评审完成不等于 human_confirmed；拒绝补素材不等于拒绝影片质量。

## 可复制模板

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
open_questions: [待填写真实受评资源和要求]
recheck_trigger: [受评资源或必要上游版本变化]
next_action: request_evidence
payload:
  character: null
  result_artifact: null
  actual_input_record: null
  requirement_refs: []
  observation_scope:
    visual: not_observed
    intervals: []
    audio: not_checked
    method: null
    limitations: []
  evidence_index: [] # id、file/version、来源、区域/时间码、观察方法、事实
  facts_observed: []
  review_matrix: [] # dimension(identity/space/geometry/action/direction/prop/camera/reveal/audio/tail)、applicable/reason、requirement、evidence、scope、item_status、interface_impact
  symptoms: []
  competing_root_causes: [] # id、解释、支持、反证/未知
  distinguishing_evidence: [] # 假设对、检查、预期、实际证据
  minimal_tests: [] # 授权、变量、控制、随机性、预期、预算/停止条件、结果
  repair:
    responsible_layer: undetermined
    authorization_evidence: null
    allowed_changes: []
    coupled_rationale: null
    attribution_limits: null
    execution_status: not_started
  regression:
    baseline_id_version: null
    authorized_delta: []
    unchanged_assertions: []
    protected_scope: []
    affected_checks: []
    adjacent_interfaces: []
    diff_audit: []
    results: []
  rollback_path: null
  decision:
    recommendation: request_evidence
    candidates: [accept, post_repair, regenerate, return_storyboard, return_asset]
    rationale_evidence: []
  tail_handoff:
    applicable: false
    eligible_for_reuse: false
    blocked_by: []
    textual_restart_required: false
  human_decision: pending
  human_decision_evidence: null
  proposed_upstream_changes: []
  handoff: {recipient: null, required_inputs: [], acceptance_conditions: []}
```

## 已填写交接例：真实媒体缺失（情境示范，不是假造看图记录）

```yaml
artifact_id: REVIEW-fog-evidence-gap
version: v1
artifact_type: review
creative_mode: perceptual
subject_type: environment-led
lifecycle_status: candidate
production_status: not_applicable
approval_level: none
upstream_versions: {PROMPT-fog: v1}
confirmed_evidence: []
open_questions: [缺真实视频、实际提交及上传记录，无法观察雾路径]
recheck_trigger: [收到原片或实际输入记录, PROMPT-fog改版]
next_action: request_evidence
payload:
  character: null
  result_artifact: null
  actual_input_record: null
  requirement_refs: [PROMPT-fog:v1要求固定机位，雾从左孔洞进入并停留右半地面]
  observation_scope: {visual: not_observed, intervals: [], audio: not_checked, method: text_contract_only}
  evidence_index: []
  facts_observed: []
  review_matrix:
    - {dimension: action, id: fog_path, applicable: true, requirement: 左入右停, evidence: [], scope: 无视频, item_status: unconfirmable, interface_impact: unknown}
    - {dimension: space, id: topology, applicable: true, requirement: 固定空间锚点, evidence: [], scope: 无画面, item_status: unconfirmable, interface_impact: unknown}
    - {dimension: identity, id: identity, applicable: false, reason: 无角色项目, requirement: null, evidence: [], scope: null, item_status: null, interface_impact: none}
  symptoms: []
  competing_root_causes: []
  distinguishing_evidence: [先取回实际原片和提交，不对不存在的观测归因]
  minimal_tests: []
  repair: {responsible_layer: undetermined, authorization_evidence: null, allowed_changes: [], coupled_rationale: null, execution_status: not_started}
  regression: {protected_scope: [PROMPT-fog:v1固定机位和空间范围], affected_checks: [fog_path, topology], adjacent_interfaces: [], results: []}
  rollback_path: 无修复执行，保留PROMPT-fog:v1，不替换任何批准资产
  human_decision: pending
  human_decision_evidence: null
  proposed_upstream_changes: []
  handoff: {recipient: 外部执行者或人工观察者, required_inputs: [原片, 实际提交, 上传回执, 模型参数], acceptance_conditions: [资源可访问, 观察范围明确, 裁决有来源]}
```

若用户拒绝回传：记录拒绝证据，next_action 改 await_user_authorization 或 await_human_review（按实际等待对象）；未判项仍 unconfirmable。若后来收到原片，另存新评审版本，定位实际证据后才更改 item_status，不把上述示范中的要求当已发生事实。
