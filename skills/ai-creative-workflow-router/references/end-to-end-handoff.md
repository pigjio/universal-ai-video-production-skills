# 无角色项目贯通与改版示例

这是规范性教学 fixture，不是真实生成记录；所有例示证据只在该假设场景中成立。真实使用时必须以实际用户消息、文件或返回ID替换。公共头见 `common-contract.md`。

## 1. 输入和创作边界

假设用户已确认：一个本来破损的黑白窗框；没有人或动物；风使窗帘掀开，露出白色窗外，再回落；只要外部生成交接，不授权本Agent提交付费请求。creative_mode=perceptual，subject_type=environment-led，character=null。故事人物、Want/Need、社会文化都不适用，不能强补。

## 2. 同一条ID链

|产物|版本|直接依赖|产物状态与事实|
|---|---|---|---|
|IDEA-window|v1|{}|感知方向；假设用户选择已记录|
|SCENE-window|v1|IDEA-window:v1|窗框破损是基准；不是待恢复异常|
|SHOT-window|v1|SCENE-window:v1|一条观看变化和布料运动，镜头固定|
|PROMPT-window|v1|SCENE-window:v1, SHOT-window:v1|完整提交文字；计划参考，不声称上传|
|CLIP-window|v1|PROMPT-window:v1|awaiting_external_generation，无返回文件|
|REVIEW-window|v1|CLIP-window:v1|无结果时只做输入审查，视频检查unconfirmable|

各行展开为公共头，依赖必须为对象映射。以下是一个实际可复制的未生成记录：

```yaml
artifact_id: CLIP-window
version: v1
artifact_type: clip
creative_mode: perceptual
subject_type: environment-led
lifecycle_status: candidate
production_status: awaiting_external_generation
approval_level: none
upstream_versions:
  PROMPT-window: v1
confirmed_evidence: []
open_questions:
  - 外部平台与允许时长待核验
recheck_trigger:
  - 场景拓扑或镜头机位改变
next_action: request_external_result
payload:
  character: null
  planned_assets: [窗框基准参考]
  actual_uploaded_assets: []
  result_artifact: null
  human_decision: pending
```

提交文字应包含基准是黑白破损、支撑和风向、当前镜头读取范围、可观察运动及完成状态；不能仅引用一个外部项目文件名。

## 3. 真实结果回来后的合法推进

只有外部用户回传可访问视频/返回ID，才更新generated。评审先记录观察范围；若只回传截图，布料外观可以检查，完整运动、连续性、时长与声音仍unconfirmable。未收到人工选择不填accept。

已观察的视频也可能失败：如布料向错误方向摆动，先区分原输入风向含混、实际参考冲突、模型遵循失败。先核实际输入，不直接重画场景。若仅色彩瑕疵可后期修复，保留动作已通过部分并声明需要重审的颜色范围。

## 4. 改版与传递影响

假设SCENE-window:v2将窗洞由墙左移到墙右，风向依据和摄影构图受影响：
1. 场景创建v2，不覆盖v1。
2. SHOT-window直接引用v1 → needs_recheck。
3. PROMPT-window直接引用场景/镜头 → needs_recheck。
4. CLIP-window与REVIEW-window经依赖链受影响 → needs_recheck。
5. 旧视频若已generated，继续保留generated事实；当前approval_level置none，旧批准留approval_history。
6. 按场景→分镜→合同→片段→评审重新检查。文字更新不等于视频自动更新；必要时生成新版本。

若场景v2只修一处与镜头不可见区域相关的档案注释，检查后可判当前镜头不受影响；记录理由，而非全量重做。未知影响不可默认无关。

## 5. 验收与反例

通过：没有补角色；破损黑白保留；待外部生成结果为空；所有依赖有明确版本；改版影响传递；未把示例证据当真实证据。
失败：为了填角色字段创造人物、把窗框修成完好、写虚构返回路径、只更新Prompt却继续称旧视频已确认、用截图证明风向全过程或音轨。
