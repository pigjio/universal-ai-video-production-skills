# 提示词合同来源与通用化边界

加载条件：核查 Seedance 正式执行稿、素材职责、状态接力、容量压缩或证据层来源时加载。此文件只用于追溯，不是运行依赖。

## 0.7.0 增量来源

0.7.0 新增 `dialogue-audio-and-lipsync-contract.md`：Dialogue 蒸馏提供语言行动、潜台词和角色声音；Film Directing Shot by Shot 蒸馏提供声音预演、对话调度与反应覆盖。音轨字段、计时和口型分支是工程综合；尚未核验专门声音设计/混音著作。

## 本次迁移来源

| 原生方法来源 | 迁移出的通用能力 | 包内落点 | 删除/降级内容 |
|---|---|---|---|
| `ai-video-production/SKILL.md`：Clip/DO、正式提示词、提交与评审接口 | 只分组与正式展开分层；自包含请求；真实提交证据 | 本技能正文 | 项目 Canon、角色名、固定 Scene/DO 编号、个人路径 |
| **formal-do-expansion-from-director-master.md** | 从导演母稿确定性抽取；逐镜五字段；素材真实性；结构校验 | **seedance-formal-request-contract.md** | V4、连续编号、本地双副本、固定项目状态串 |
| **prompt-group-boundaries-and-scene-local-reading.md** | 主体边界、素材职责、局部/分区读取、条件模块 | **seedance-formal-request-contract.md**、**reference-duty-and-assembly.md** | “任何场景图都只能局部读取”等过强规则 |
| **seedance-2-shot-decomposition.md** | 单一主要变化、形成→接触→结果→Reaction 的风险拆分 | **seedance-formal-request-contract.md**、**causality-and-diagnostics.md** | 固定 15/30/60 秒和项目镜号；改标工程启发式 |
| **prompt-start-end-state-integration.md**、**textual-do-handoffs-without-upstream-media.md** | 第一镜建立起点、结果融入切点、文字/媒体接力、禁止重演 | **seedance-state-handoff.md** | 固定场景和角色例 |
| **seedance-prompt-capacity-compression.md** | 按独立提交块计数、保护区、详细版/提交版、压缩回归 | **seedance-capacity-compression.md** | 固定字符数；改为当前入口能力证据 |
| **seedance-2-official-prompt-audit.md**、**handbook-to-tested-project-rule-audit.md** | 官方事实、官方案例归纳、第三方经验、项目观察分层 | 本技能正文与视频生产能力档案 | 历史数值不作为永久常量 |
| **baseline-regression-minimal-diff.md** 等项目回归经验 | 授权范围、跨提示层残留、最小差异保护 | **causality-and-diagnostics.md** | 项目文件名、确认索引和具体剧情事实 |
| Seedance 电影镜头提示词手册的目标/资产/起点/空间/摄影/时间轴/物理/声音/终点/禁止结构 | 面向普通创作者的最小可复制出口 | **seedance-student-delivery.md** | 本地路径、固定项目素材和长段原文；重组为原创交付模板与小例 |

## 证据说明

- 本轮已实际读取原生 `ai-video-production` 正文及上述相关 references，并对照桌面 0.3.0 目标文件。
- 原生技能和项目案例是方法来源，不是外部用户必须安装或访问的依赖；本包内规则应独立可执行。
- 官方平台事实仍需执行时核验当前 URL、日期、模型、产品入口和模式。
- 项目真实生成只支持当时条件下的观察；不能外推为 Seedance 普遍规律。
- 教学示例均为示意，不写入 `confirmed_evidence`，也不冒充生成结果或人工接受。
