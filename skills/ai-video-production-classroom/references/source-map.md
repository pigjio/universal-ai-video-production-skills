# 视频生产方法来源与通用化边界

加载条件：追溯 Clip/DO 分组、Seedance 能力、真实尾帧、请求状态、剪辑交付或检查项目规则泄漏时加载。来源路径只作审计锚点，不是外部运行依赖。

## 0.7.0 增量来源

0.7.0 新增 `generation-risk-and-shot-feasibility.md`：采用 Katz 的覆盖、动作匹配、剪辑连接与 Glebas 的观众因果阅读比较替代拍法；风险类别、测试预算和修复门为工程启发式，不是平台成功率证据。

## 本次迁移来源

| 原生方法来源 | 通用化能力 | 包内落点 | 不迁移项 |
|---|---|---|---|
| `ai-video-production/SKILL.md`：导演镜头→Clip/DO、请求、提交、评审、尾帧和剪辑 | 四层生产模型、授权与真实状态 | 本技能正文 | 项目 Canon、角色/场景资产、固定 DO 编号 |
| **scene-unit-formal-do-decomposition.md**、**formal-do-expansion-from-director-master.md** | 按任务、空间、状态、动作链、素材集分组 | **production-grouping-and-task-contract.md** | 30 秒前提、V4、项目目录与连续编号 |
| **merged-do-long-window-test.md** | 长窗合并不是拼接；候选不覆盖基线；桥接回退 | **production-grouping-and-task-contract.md**、**continuation-and-edit-delivery.md** | 固定平台时长和项目状态串 |
| **prompt-start-end-state-integration.md**、**textual-do-handoffs-without-upstream-media.md**、**textual-tail-frame-restart-and-reverse-camera-bridge.md** | 真实尾帧、文字重建、独立重启、遮挡桥候选 | **clip-continuity.md**、**continuation-and-edit-delivery.md** | 特定场景拓扑和角色例 |
| **seedance-2-official-prompt-audit.md**、**handbook-to-tested-project-rule-audit.md** | O1/O2/T/P/A 证据层；动态能力档案 | **seedance-capability-and-evidence.md** | 发布时固定数值不升格永久事实 |
| **baseline-regression-minimal-diff.md**、**storyboard-revision-do-rebuild-validation.md** | 基线保护、上游影响传播、局部修复 | **production-modes-and-baseline.md**、正文 | 项目知识库双副本和确认索引 |
| 原生剪辑交付与真实任务句柄规则 | EDL、实际采用段、导出验证 | **continuation-and-edit-delivery.md** | 具体 CLI/API SOP |

## 保留的通用版优势

- narrative/perceptual/conceptual 与无角色路径贯通；
- planned、awaiting_external_generation、submitted、generated、reviewed 和人工接受分离；
- 未知能力允许保持 unknown；
- 单次生成不证明普遍规律；
- 平台限制不会写死在主技能。

## 证据边界

本次迁移已实际读取原生技能及关键 references。所有固定时长、素材槽位、音频、多镜头和接口能力仍需按当前模型、入口与日期复核。项目实测和人工接受只作为局部证据，不等于官方能力或 Canon 自动更新。
