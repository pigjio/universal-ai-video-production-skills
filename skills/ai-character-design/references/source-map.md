# 来源地图与迁移边界

本包以可识别的源 skill 与 reference 为迁移依据；以下是来源索引，不是运行时依赖。不要求安装源 skill，不声明未核验原书页码、材料总数或覆盖率。

| 本包模块 | 源 skill / 参考 | 迁移与适用边界 |
|---|---|---|
| 主流程、五维、体块、下游接口 | `character-design/SKILL.md`；`character-design/references/ai-graphic-framework.md` | 保留大形先行、形状与功能联系；本包评分尺度是接口化整理而非书中原表 |
| 四层验收 | `character-design/references/acceptance-framework.md` | 保留 A/B/C/D 测试与回退，移除角色名、固定比例与项目表情阈值 |
| 表情及模块迭代 | `character-design/references/expression-and-head-sheet-workflow.md` | 以 neutral 和小模块控制漂移；不固化平台格数 |
| 混合生物 | `character-design/references/hybrid-creature-design.md` | 来源按系统分工，自然规律转为结构、运动与功能；不复制器物变身剧情 |
| 系列 DNA | `character-design/references/series-crowd-derivation.md` | 观察→共享/专属→校准→扩群；不带入文明层级或服装 Canon |
| 有益意外 | `character-design/references/live-reference-and-emergent-variant-review.md` | 双向参考、功能判断、双重读取；不固定花毛结构禁令 |
| 标尺与固定卡 | `character-design/references/production-scale-lock.md`、`character-design/references/deterministic-character-lock-card.md` | 标尺明确、确定性合成；来源尺寸和版式仅作经验 |
| 公共交接 | 本包修订合同与 **common-contract.md** | 本包统一协议，不继承源版混用状态 |

查来源时先定位本包模块，再定位表中源文件和主题；找不到来源细节时标未核验，不推定书页。完成判断示例：四层验收已迁移，但源版的特定角色高度不应迁移；本包应测试项目自身标尺，而不是宣称复刻原项目生产验证。

## 0.3.0 定向蒸馏融合来源

本轮依据《创作搭档Skills_蒸馏知识融合审查.md》角色八项，读取下列蒸馏稿相应源段。以下行号是所读 Markdown 定位，不是原书页码；稿件内附原书页码未经本轮核对。只核读二次蒸馏内容，未核原书、未认证全库准确性或覆盖率；若原始提取单元标 NEEDS_REVIEW，则仍是候选启发，不因本包采纳而升级为原书事实。方法、竞争解释和创作示例已经随包自足，不需要外部源文件。

### 稿名索引（角色设计视觉全量重蒸馏）

- **角色总纲**：**00_角色设计知识库总纲.md**。
- **Silver**：`The Silver Way Techniques, Tips, and Tutorials for Effective Character Design (Stephen Silver) (1) - 方法论总纲.md`（不是同库另一份无作者名的近名稿）。
- **Force**：`Force Character Design from Life Drawing (1) - 方法论总纲.md`。
- **Caricature**：`The Mad Art of Caricature A Serious Guide to Drawing Funny Faces (1) - 方法论总纲.md`。
- **Expression**：`The Artists Complete Guide to Facial Expression (1) - 方法论总纲.md`。

### 覆盖与来源章节映射

| 单元 | 所读蒸馏章节与行段 | 本包落点 | 转译边界 |
|---|---|---|---|
| 观点反证 | Force 模块2 Opinion，115–140；角色总纲 3.1 角色内核，612–630 | SKILL Phase1；design-foundations「观点与反证」 | 同职业两种压力策略是本包新例；不重建 Core Card、不强补创伤 |
| 等距机械节奏 | Silver 3.5 清晰优先于复杂，134–151；错误/症状/修正表，478–490；Force 模块6 Shape 操作步骤，295–307 | SKILL Phase3；design-foundations「等距与机械节奏」 | 区分有意秩序与无意僵硬；不迁固定变体配额或强制不对称 |
| 完整 Force 路径 | Force 模块4 Force，188–218 | SKILL Phase5/G5；performance-and-production「完整 Force 路径」 | 入口/峰值/释放/锚点为表演组织；动态失衡不套静态支撑，不作力学认证 |
| 五形/T 形识别 | Caricature 模块3 Five Shapes、模块4 T-shape、模块5 Alpha Shape，134–203 | SKILL Phase6；design-foundations「五形与 T 形」 | 比距离/大小/角度、负形及下巴联动；标准比例非平均脸目标 |
| 风格探索/锁定派生 | 角色总纲 3.8 风格化，768–780；Force 模块7 Ratio Bounding Box，318–343 | SKILL 原则6、Phase3/8、迭代规则；design-foundations「风格探索与锁定派生」 | 新探索允许体块比例联动；已锁派生按授权，越界另开版本，不静默替母版 |
| 三层表情基线 | Expression 模块1 neutral baseline，99–123；Caricature 阶段7 3D 建模/绑定交接，540–554 | SKILL Phase6/G6；performance-and-production「三层表情基线」 | 工程 neutral mesh 与 resting pose 分离是综合接口化解释；非原书术语认证 |
| 复合/压抑表情 | Expression 模块8–10，337–431；补读模块11，435–463；模块12 身体状态表情，467–489 | SKILL Phase6/G6；performance-and-production「复合与压抑表情」 | 分区职责、尺度、身体状态竞争解释；不用表情测谎，AI 预期非受众实测 |
| 群像关系动作 | Force 模块10 Reportage，439–473；角色总纲 Phase10 群像、关系与场景可读性测试，526–543 | SKILL Phase9；branches-and-diagnostics「群像关系动作」 | 同刺激/不同策略/双人无脸姿态为讨论转译；不擅改关系，最终调度交分镜 |

四种互动模式、讨论循环及证据作用域来自本包《修订合同.md》与融合审查建议的协议整理，不冒称某书原有完整 Agent 流程。新增保安、修理工、跃沟、礼貌微笑及双人门前动作均为说明性创作例，不是源书引文、原书案例或实际生成/观众/绑定测试结果。本轮不迁入源稿固定数量、比例三分法硬规则、形状人格定律或项目 Canon。
