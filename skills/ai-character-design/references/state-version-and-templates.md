# 状态、版本与角色交接模板

正式登记资产、生产交接/验证或已登记资产上游改版时加载 `common-contract.md`。以下是完整阶段产物头；模块表属于 payload，不能替代公共头。讨论直接回应、不落盘、不强制公共头或全包；探索可保留未知与暂定基线，不把探索候选等同正式可交接 candidate。正式成稿只覆盖用户指定范围；授权写入时确定项目目录、保留版本，不静默覆盖批准稿。interaction_mode 仅作对话概念，不加入本公共 YAML。

```yaml
artifact_id: CHR-example
version: v1
artifact_type: character
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
  character: example
  functional_or_perceptual_premise: ""
  core: {want: null, fear: null, contradiction: null, core_verbs: []}
  design_pillars: []
  shape: {silhouette: "", gesture_line: "", masses: "", memory_anchors: []}
  scale: {unit: "", standard_pose: "", endpoints: "", reference_height: null}
  expression_and_motion: []
  costume_props_materials: []
  source_master_id: null
  parent_id: null
  module: core
  invariants: []
  variables: []
  forbidden_changes: []
  tests: []
  downstream:
    recipient: scene_or_storyboard_or_model_rig_animation
    required_inputs: []
    locked_constraints: []
    unresolved_risks: []
  change_log: []
```

## 使用步骤与完成样例

1. 稳定 ID 不含版本。原始母版、表情模块、服装变体和输入固定卡若独立交付，分别有稳定 ID，且 `upstream_versions` 指向确切来源版本。
2. Core Card 填功能句、五维与动作；给建模时补唯一标尺和多视图；给分镜时补可读角度、接触与关键反应。用同一公共头，不让接收方猜批准层级。
3. 证据写实际图/文件/人工裁决引用；方向批准不是生产批准，更不是已生成。计划测试与真实结果分别记录。
4. 无角色作品填 `payload.character: null`，跳过角色设计或仅记录不适用决定，不添加人物来过闸门；感知/概念模式的内心冲突字段可为 null。

规范填写示例：`CHR-helper` 的 `v2` 仅改肩部活动空间，`upstream_versions: {SCR-main: v1}`；payload 写“胸前折叠体块不变、肩侧减薄，待抱持动作验证”，公共头维持 candidate、not_applicable、none（分别填入对应字段）。没有图片不得填 generated。

## 上游变化与失败分支

剧本/世界或角色母版变化 → 列直接及传递依赖 → 受影响产物置 `needs_recheck` → 保留历史批准但不作为当前有效门禁 → 重审证据后才恢复 `confirmed`。例如 CHR-helper 肩宽变化影响 SCN-workspace 的活动通道，继而影响 STB-pass 的转身镜头；脸部材质不相关可经影响检查保留并记录理由。发现引用了旧母版，先修依赖与状态再生成，不用改版本号掩盖旧证据。
