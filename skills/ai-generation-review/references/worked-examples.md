# 评审完成案例：抽象终点、物体结构与有限证据

加载条件：需要环境/物体/抽象完成或失败示范时加载。完整可复制公共头见 review-template.md；下述案例均为虚构教学记录，文件名、时间码和观测不是本次真实工具结果，不能复制进项目证据。

## 1. 抽象变化失败的完整评审情境

假设观察者确实连续观看示例原片 demo-film-v1.mp4 的 00:00–00:06，并核对实际提交；要求为薄膜从中心向外展开、末段停稳，音频不要求。

```yaml
artifact_id: REVIEW-film-demo
version: v1
artifact_type: review
creative_mode: conceptual
subject_type: abstract
lifecycle_status: candidate
production_status: not_applicable
approval_level: none
upstream_versions: {PROMPT-film: v1, CLIP-film: v1}
confirmed_evidence: [] # 教学案例不提供真实项目证据
open_questions: [末段未停稳的根因未区分, 人工决定待定]
recheck_trigger: [实际提交补证据, 修复输出返回, 必要上游变化]
next_action: request_evidence
payload:
  character: null
  result_artifact: {id: CLIP-film, version: v1, file: demo-film-v1.mp4, provenance: fictional_example}
  actual_input_record: 示例提交快照，需真实记录替换
  requirement_refs: [PROMPT-film:v1末段停稳]
  observation_scope: {visual: full_watch_in_example, intervals: ['00:00–00:06'], audio: not_required, method: fictional_continuous_playback}
  evidence_index:
    - {id: E-demo-edge, file: demo-film-v1.mp4, interval: '00:05–00:06', region: 薄膜外缘, fact: 示例中边缘持续向外移动直至片尾, provenance: fictional_example}
  facts_observed: [仅在假设教学情境中，片尾边缘仍在移动]
  review_matrix:
    - {id: endpoint, applicable: true, requirement: 停稳可见, evidence: [E-demo-edge], scope: '00:05–00:06', item_status: fail}
    - {id: character, applicable: false, reason: 抽象无角色, requirement: null, evidence: [], scope: null, item_status: null}
    - {id: audio, applicable: false, reason: 任务无音频要求, requirement: null, evidence: [], scope: null, item_status: null}
  symptoms: [末段未出现可读停稳]
  competing_root_causes:
    - {id: H1, explanation: 请求窗口未容纳完整变化, support: 末端仍运动, unknown: 实际窗口及动作节奏}
    - {id: H2, explanation: 生成未遵守停稳要求或随机失败, support: 示例提交含停稳, unknown: 同条件重复结果}
    - {id: H3, explanation: 导出提前裁切, support: 尚无, unknown: 原始资源与导出是否同一份}
  distinguishing_evidence: [先比原始资源和EDL排除H3, 核验实际窗口与提交参数]
  minimal_tests: [获授权后固定素材模型和目标，比较可容纳闭合的分组；保留随机性限制]
  repair:
    responsible_layer: undetermined
    authorization_evidence: null
    allowed_changes: []
    coupled_rationale: null
    execution_status: not_started
  regression:
    protected_scope: [银色连续薄膜, 黑底, 向外展开, 无新增事件]
    affected_checks: [停稳, 材质连续, 范围]
    adjacent_interfaces: [若补段则复查接缝形态及运动相位]
    results: []
  rollback_path: 保留CLIP-film:v1，不自动替换任何已批准版本
  human_decision: pending
  human_decision_evidence: null
  proposed_upstream_changes: []
```

完成含义：报告完成，根因未定、修复未执行、人工未接受。没有预算则移交人工选择，不反复调用。若确认只是剪辑过早，先调整切点并回归；若实际原片确无停稳，才提出局部补段/分组候选。单次新片改善不证明窗口是唯一根因。

## 2. 物体静帧通过与不可判并存

假设已观察金属环静帧：缺口朝上、底部接触台面、左侧高光满足该帧要求，可逐项 pass。背面结构被遮挡则 unconfirmable；“回正过程自然”和“确已停止”不能由静帧证明。character:null，不要求表演；来源未知时先补文件/版本，不填真实绑定成功。

若下一帧缺口消失，竞争原因含旋转遮挡、结构漂移、参考冲突和后期裁切。先看连续区间与原始素材，不能直接重做物体母版。新结构若有美感只登记候选。

## 3. 环境截图受阻

只有孔洞换侧截图：先核对机位与是否镜像；没有相邻帧不能判全程拓扑漂移。输出 suspicious（有定位疑点）或 unconfirmable（没有足够对照），请求原片/分镜/EDL。若没有看图能力，连截图事实也保持未观察。用户不补素材时保留有限结论及拒绝来源，不把拒绝补证据写成拒绝影片。
