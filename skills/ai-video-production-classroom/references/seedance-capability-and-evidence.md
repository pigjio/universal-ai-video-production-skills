# Seedance 能力档案与证据分层

## 目的

把 Seedance 的当前产品能力、官方案例组织方式、第三方建议和项目实测分开。平台信息会变，任何时长、素材槽位、输入模态、音频能力或接口语法都必须带适用入口和核验时间。

## 1. 证据层级

| 层级 | 含义 | 可支持 | 不可支持 |
|---|---|---|---|
| O1 官方产品事实 | 当前官方产品页/API 文档明确声明 | 输入模态、窗口、槽位、输出能力 | 不证明具体项目稳定 |
| O2 官方案例归纳 | 从官方演示和示例 Prompt 归纳 | 素材职责、因果顺序等组织候选 | 不得称唯一或强制语法 |
| T 第三方经验 | 手册、教程、社区测试 | 待验证策略 | 不得冒充官方事实 |
| P 项目观察 | 有真实请求、输入和返回结果 | 当前入口/版本/参数下的局部判断 | 不得外推平台普遍规律 |
| A 人工接受基线 | 项目内有明确人工裁决的结果 | 当前项目回归与交付 | 不等于平台上限或 Canon 自动更新 |

## 2. 能力记录

```yaml
capability:
  name: multimodal_reference
  claim: null
  evidence_level: O1
  source_url: null
  checked_at: null
  model_version: null
  product_entry: null       # UI/API/具体产品入口
  generation_mode: null
  capability_status: known | unknown | superseded
  scope_limit: null
  runtime_recheck_required: true
```

来源缺 URL、日期、模型或入口时，不把数值写入主技能硬规则。发布页支持多镜头，不等于当前项目中复杂多镜稳定。

## 3. 生成模式选择

| mode | 使用条件 | 受阻处理 |
|---|---|---|
| `text_to_video` | 无需身份/拓扑继承，当前入口支持 | 不因缺图静默降级；先确认用户接受可控性下降 |
| `image_to_video` | 有一张或多张已核验图承担身份、构图或状态 | 上传失败则保持 planned，不能当纯文字已执行 |
| `reference_to_video / multimodal` | 多种参考职责且当前模式支持 | 先核素材上限和职责冲突 |
| `real_tail_frame_continuation` | 上游真实末段合格并已上传 | 坏尾帧冻结下游 |
| `video_continuation` | 平台支持视频输入且真实资源可用 | 保存资源 ID 和续接能力证据 |
| `textual_reconstruction` | 不要求像素级连续，权威文字起点明确 | 明确不是实际媒体继承 |
| `external_execution` | 本环境无生成工具，但交接包完整且用户指定外部执行 | 状态为 awaiting_external_generation，不冒称 submitted |

## 4. 状态证据门

| 状态 | 最低证据 |
|---|---|
| `planned` | 请求/分组计划 |
| `awaiting_external_generation` | 外部执行者已明确、交接包完整；不代表已提交 |
| `submitted` | task ID、受理回执或可核验查询记录 |
| `generated` | 可访问 output ID、URL 或文件 |
| `under_review` | 已记录真实观察范围 |
| `reviewed` | 评审报告已完成 |
| `human accepted` | 真实人工裁决证据 |

只有写稿授权时保持 `planned + next_action: await_user_authorization`。超时但已有任务 ID 时标 `submitted + submission_uncertain`，先查状态，避免重复扣费。

## 5. 执行前核验清单

- 产品入口、模型版本和生成模式；
- 当前可选时长/画幅；
- 图片、视频、音频的实际输入能力与计数方式；
- 多镜头、首尾帧、续接和声音能力；
- 字符/令牌容量和计数方法；
- UI 与 API 是否能力不同；
- 来源日期是否过期；
- 当前项目是否有真实稳定性证据。

未知时交平台中立方案和待核清单，不伪造能力，也不把历史固定数值当永久常量。
