# 提示词完成合同与异常交接示例

加载条件：需要完整静态/时序交付、无工具、缺素材或失败修复示范时加载。以下为教学计划，非真实生成、素材观察或人工批准。

## 静态物体：独立提交层

步骤：确认 object-led / perceptual 与静态目标→核对结构/支撑/材质判据→不适用时序字段→组装完整文本→交审查，不把合同完成记成生成。

```yaml
artifact_id: PROMPT-ring
version: v1
artifact_type: prompt
creative_mode: perceptual
subject_type: object-led
lifecycle_status: candidate
production_status: not_applicable
approval_level: none
upstream_versions: {}
confirmed_evidence: []
open_questions: [平台参数待核验, 人工方向待确认]
recheck_trigger: [目标结构或材质改版, 引入参考资产]
next_action: await_human_review
payload:
  contract_type: static-image
  operation: create
  character: null
  target_goal: 观察带单一缺口的金属环结构与台面接触
  narrative_job: null
  completion_criteria: [环轮廓可读, 缺口朝上, 底部接触台面, 左上光源, 不新增文字或人物]
  record_layer:
    project_constants: [中性背景, 冷色金属]
    shot_delta: [本图缺口朝上]
    protected_scope: [单环, 单一缺口]
  units: {shot_ids: [], edit_unit_ids: [], request_id: null}
  capability_evidence: []
  submission_layer:
    platform: null
    model: null
    parameters: {}
    complete_required_context: 单幅物体静态研究，无需外部项目常量或历史会话
    positive_prompt: >-
      中性纯净背景上，一只冷色金属环直立于平整台面，底部与台面明确接触。
      环上仅有一个缺口，朝画面上方，正面略带侧角以同时读清轮廓与金属厚度。
      光从左上方照来，表面呈连续金属质感，焦点在环结构、缺口和接触位置。
      画面只含金属环、台面和中性背景，不出现人物、文字或额外环件。
    actual_uploaded_assets: []
    planned_but_not_uploaded: []
    verified_context_inheritance: []
  reference_duties: []
  static_fields: {composition: 单环清晰可读, focus: 结构与接触, structure: 单一缺口, state: 直立, material: 冷色金属}
  next_segment_interface: null
  allowed_changes: []
  coupled_repair_rationale: null
  high_risk_constraints: [缺口数量, 接触是否可见]
  blocked_reason: null
  human_decision: pending
  human_decision_evidence: null
```

没有参考图是合法纯文字候选，不宣称继承某已确认环资产。若必须复现具体母版而缺图，blocked_reason 应改为缺必要母版，等待素材或授权纯文字另版，不能沿用“精确身份已绑定”。

## 无角色时序提交小例

环境雾变化合同：固定机位观察已破损庭院；左孔洞和中央断柱位置不变；雾从左孔洞进入、贴地向右，终点停留右半地面，不新增人物/建筑。character:null、creative_mode:perceptual、subject_type:environment-led。废墟是起态，不强制正常态。

记录层可写“SCN-court:v1 + 雾变化”，提交层却必须包含上述完整空间/材料/起终态及实际可用参考。整图只承担经观察的拓扑职责，不顺带继承无关光色或冲突雾状态；未观察素材则不编事实。是否拆请求依据生产能力，普通终点不滥建“强制末帧”。无生成工具时 Prompt 为 not_applicable，另交 clip 的 awaiting_external_generation 与真实回传要求。

## 耦合修复与失败出口

若实际上传为完整玻璃图，文字要求破碎起态：先查上传回执和图像内容，竞争假设还包括读取职责覆盖、生成随机性。若确认输入状态冲突，获授权后联合换为目标起态参考并修正文字；保护机位/色彩/范围，说明无法分别归因。缺任一证据先等待，不擅自生成或改母版。

提交明确失败只在生产记录记 failed，提示词不伪造结果；受理不明先查询任务；人工待定仍 pending；上游变更经直接/传递影响检查标 needs_recheck，旧批准不能替代新版审查。完成标准是合同可独立执行、缺口可追踪，不是填满所有字段或保证模型服从。
