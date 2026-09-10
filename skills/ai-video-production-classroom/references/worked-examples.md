# 无角色与受阻生产：完成交付示例

加载条件：课堂演示、无角色任务、外部待生成或上游改版交接时加载。以下为教学示范，不代表真实调用、资产批准或平台能力。

## 无工具仍可完成的生产包

输入：只授权写稿，conceptual / abstract，黑底中银色薄膜从中心向外展开，最后停在画面中央区域；不含角色、地面或叙事冲突。操作顺序：冻结判据→选静态/视频分支→建四层映射→列未知能力→组装提交文本→等待提交授权。

```yaml
artifact_id: CLIP-film
version: v1
artifact_type: clip
creative_mode: conceptual
subject_type: abstract
lifecycle_status: candidate
production_status: planned
approval_level: none
upstream_versions: {PROMPT-film: v1}
confirmed_evidence: []
open_questions: [目标平台模式、窗口与输出能力待核验, 尚未授权付费提交]
recheck_trigger: [PROMPT-film改版, 平台能力核验完成, 实际输出返回]
next_action: await_user_authorization
payload:
  profile: abstract-study
  character: null
  target_goal: 银色薄膜由中心展开，边缘停稳
  completion_criteria: [展开方向向外, 中央覆盖范围可见, 终点停稳, 不新增人物或地面]
  authorized_actions: [write_draft]
  authorization_evidence: null # 示例中未提供实际授权消息，执行时须替换真实来源
  protected_scope: [黑底, 银色薄膜材质, 无角色]
  shot_ids: [SHOT-film]
  edit_units: [{edit_unit_id: EDIT-film, source_request_id: REQ-film, planned_in_out: 待输出后选择完整展开与停稳区间, actual_in_out: null}]
  production_group_id: PG-film
  display_alias: DO-film
  task_contract: {type: conceptual_test, primary_job: 观察薄膜由中心展开并停稳, observable_end_state: 薄膜边缘停止移动, forbidden_early_reveal: []}
  generation_requests: [{request_id: REQ-film, role: primary, status: planned}]
  director_duration_target: 待导演确认可读展开及停稳的节奏
  requested_window: null
  actual_output_duration: null
  capability_checks: [{capability: temporal_generation, status: unknown, source: null, checked_at: null, model: null}]
  reference_duties: []
  actual_uploaded_assets: []
  planned_but_not_uploaded: []
  complete_submission_text: >-
    固定正面观看纯黑背景中的银色薄膜，不出现人物、地面或文字。
    薄膜最初集中在画面中心，保持金属薄膜的连续表面和细微褶皱，
    从中心向外连续展开，边缘不超出中央区域，随后停止扩张，保留可观察的停稳终点。
    背景、材质和机位不变；不增加爆炸、碎片或其他事件。
  actual_submission_snapshot: null
  platform_model_parameters: {}
  returned_task_id: null
  returned_output_id: null
  result_file: null
  error_or_block: 无生成工具且付费提交未授权
  baseline: null
  allowed_changes: []
  coupled_repair_rationale: null
  continuation_interface: null
  review_record: null
  human_decision: pending
  human_decision_evidence: null
```

判定：这是完整请求草案，不是已交给外部执行，更不是成片。取得提交授权并明确外部执行者后，才可改为 `awaiting_external_generation`；实际受理后再改 `submitted`。回传真实快照/任务 ID/原片/参数。纯文本描述“中央区域”若验收需精确边界，应先由导演给可视边界或明确范围，不让执行者擅自发明比例。

## 失败与恢复

- 平台无所需窗口：保留导演目标，比较单次请求与按形态状态拆分，不压掉停稳证明。
- 只得到任务 ID：submitted，查询结果；不写 generated。
- 返回片段末端还在扩张：真实观察后才判终点 fail；保留第一返回基线，局部补停稳或调整分组，回归材质和边缘范围。
- 人工未决定：pending 合法；报告可交付，不覆盖旧批准段。

## 改版影响小例

PROMPT-film:v2 经授权把展开终点改为“填满画面”。旧 CLIP-film:v1 的中央停稳结果不能被直接视为符合新版。沿 PROMPT→CLIP→REVIEW→采用片段标受影响项 needs_recheck，旧批准历史保留但当前失效。未受影响且独立的片头黑场可经影响检查保留并记理由。新片通过目标终点及受保护材质回归、取得相应裁决后再恢复 confirmed；失败可回看旧版，但不能把旧版冒充新版交付。
