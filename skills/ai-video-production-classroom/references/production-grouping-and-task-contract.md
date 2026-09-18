# 生产分组、任务合同与请求映射

## 适用条件

当导演镜头要转换成 Clip/DO、比较长短请求、安排重试/桥接或建立剪辑来源时加载。

## 1. 四层单位

```text
SHOT-*                导演镜头：观看、构图、动作、切点
  ↓ many-to-many
PG-* / CLIP-*         生产组：共享一个主要任务和连续状态；DO 可作显示别名
  ↓ many-to-many
REQ-*                 一次真实平台调用：独立输入快照、状态、回执和输出
  ↓ one-to-many
EDIT-*                成片采用段：来源输出及实际 in/out
```

禁止用一个 Clip/DO 同时代替四种单位。一个生产组可以多次重试；一个请求可以覆盖多个相邻组；桥接请求可以跨边界；一个输出可以裁成多个剪辑单元。

## 2. 从镜头账本形成生产组

1. 读取每个镜头的观看任务、机位、空间、主体状态、动作节点、素材需求、导演时长和切点。
2. 标记功能：建立、状态证明、触发、动作、接触、Reaction、Decision、结果、接口。
3. 先按因果链形成候选，不按旧 DO 编号或固定秒数硬拼。
4. 检查拆分边界：空间/侧别重置、复杂形态变化、素材集切换、多个独立情绪落点、关键接触、平台窗口或失败证据。
5. 给每组建立一个主要任务合同和可观察终点；若有两个不可替代的主要结果，拆组或请人工确定主从。
6. 再根据当前平台能力决定一个组对应一个或多个请求，或多个组进行长窗候选测试。

## 3. 任务合同

```yaml
production_group_id: PG-example
display_alias: DO-example        # 可选
shot_ids: []
task_contract:
  type: narrative_job | perceptual_goal | conceptual_test
  primary_job: null
  completion_criteria: []
  observable_end_state: null
  forbidden_early_reveal: []
director_duration_target: null
grouping_basis:
  spatial_continuity: null
  subject_state: null
  causal_action_chain: []
  required_reference_set: []
  split_boundary: null
planned_continuation_interface: null
risk_register: []
```

叙事项目使用 Narrative Job；感知研究使用 perceptual goal；概念实验使用 proposition/test。无人物任务同样需要可观察完成判据，但不强加角色欲望。

## 4. 组—请求映射

```yaml
group_request_map:
  - production_group_ids: [PG-A]
    generation_request_id: REQ-A-v1
    role: primary
    request_status: planned
  - production_group_ids: [PG-A]
    generation_request_id: REQ-A-v2
    role: retry
    request_status: planned
  - production_group_ids: [PG-A, PG-B]
    generation_request_id: REQ-AB-test
    role: merged_test
    request_status: planned
```

`role` 可为 `primary | retry | bridge | merged_test | pickup`。候选请求不能覆盖已接受 baseline。

## 5. 四种时长

```yaml
duration_ledger:
  director_duration_target: null
  requested_window: null
  actual_output_duration: null
  actual_edit_duration: null
```

未发生的实际值保持 `null`。平台余量只用于 handles 或完成既有动作；不得用来增加闲走、重复反应或新剧情。

## 6. 长窗、短段与桥接

- **长窗候选**：当前入口支持，空间/材质连续、运动相位重要；必须重写成连续运动包络，不能拼接两个旧 Prompt。
- **短段候选**：复杂接触/状态阶段多、窗口不足或已有长段失败证据；在可观察状态边界拆分，并记录接缝成本。
- **桥接/补段**：主体段已通过，只有边界或单个必要节点失败；保护通过段，不无故整组重生成。

单轮结果只能支持当前条件，不证明平台普遍规律。

## 7. 验收

- 每个 shot 都有生产组映射；
- 每组只有一个主要任务和可见终点；
- 组和请求不是一对一硬绑定；
- 四种时长未混填；
- 拆分/合并依据来自连续性、风险和能力证据，不是固定秒数；
- 上游导演内容未被生产层擅改。
