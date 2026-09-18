# 通用 AI 影像制作 Plugin

[中文说明](README.md)｜[한국어 안내](README.ko-KR.md)

面向 AI 短片、动画和视觉叙事的 Codex 创作协作插件。用户只需安装一次，即可获得一个总控 Router 和九个专业 Skill；它们共同把创意、剧本、世界观、角色、场景、分镜、生成请求、视频生产和结果评审串成一条可追踪、可恢复的工作流。

版本：**0.7.0｜表演、声音与跨阶段一致性增强版**

> 你不需要记住 Skill 名，也不需要先学提示词。你只需描述、比较、否决和确认；Agent 负责选择方法、维护阶段、版本和文件。

## 0.7.0 使用变化

学生不需要学理论或填写追踪表，只需自然地说想改什么，由 Agent 在内部完成以下判断。

- **表演：**把情绪名称转成接收刺激、采取行动、调整或坚持的过程，让停顿、视线和物件动作呈现选择，而不是套用“难过就低头”。
- **声音：**区分对白原文、说话者、听者、可见口部和声音起止。画外人物对白不偷换成旁白；能力未知时给后期方案，不承诺配音自动解决口型。
- **生成风险：**解释精细接触、多动作等风险，比较保留故事含义的替代拍法；真实平台测试需单独授权。
- **局部修改：**追踪剧本意图到镜头和提示词的关联，明确受影响与不变内容。发生冲突先说明，不擅改受保护镜头。

可以直接说：“不要解释情绪，用动作让我看懂。” / “这句台词拍听的人。” / “只改第二镜，后面有冲突先告诉我。”

**v0.7.0 已发布，Marketplace 安装入口指向 v0.7.0。** 经用户要求，角色概念提示词修订已合入同一版本，v0.7.0 标签已更新；已安装或缓存旧内容的用户需要重新获取。真实视频生成、学生使用体验与艺术满意度仍需另外验证。

## 主要特性

- **四种自然入口**：从模糊想法、现有故事或剧本、已有图片、失败的生成结果任意切入。
- **一个 Plugin，十个专业 Skill**：只安装一次，内部覆盖从早期创意到真实生成结果评审的完整链路。
- **新手、协作、专业三种交流方式**：复杂度可以调整，专业判断和证据门槛不降低。
- **每轮一个小目标**：最多询问一个真正阻断的问题；“不知道”是有效回答。
- **阶段确认与保存分离**：积极反馈不等于定稿，保存不等于上传、生成、付费、发布或研究同意。
- **完整 Markdown 阶段成果**：确认后创建新版本，不静默覆盖旧版，并回读验证。
- **跨会话恢复**：通过项目索引、授权记录和会话交接恢复真实进度，不凭聊天记忆猜最新版。
- **生产证据可追踪**：区分 planned、submitted、generated、reviewed 与人工接受，不把提示词完成冒充生成完成。
- **Seedance / 即梦生产支持**：包含镜头分组、素材职责、正式请求、续接、十维评审和局部返修方法。
- **研究默认关闭**：生产、方法溯源和研究分层管理，研究使用必须另行获得明确同意。
- **中韩文自然协作**：韩文请求可直接触发总控与十个专业阶段；Agent 跟随用户语言，授权和状态逻辑不随语言改变。

## Plugin 内的十个 Skills

这十个 Skill 是同一个 Plugin 的内部专业模块，不需要分别安装。安装后它们会在新会话中可用；Codex 会按当前任务加载匹配的 Skill。通常直接描述需求即可，也可以在支持的界面用 `@` 明确调用某个 Skill。

| Skill | 用途 |
|---|---|
| [`ai-creative-workflow-router`](skills/ai-creative-workflow-router/SKILL.md) | 新手入口、跨阶段路由、恢复与最小回退 |
| [`ai-visual-ideation`](skills/ai-visual-ideation/SKILL.md) | 从模糊想法形成可比较的创意方向 |
| [`ai-screenplay-development`](skills/ai-screenplay-development/SKILL.md) | 剧本、场景链、动作、对白、诊断与改写 |
| [`ai-worldbuilding`](skills/ai-worldbuilding/SKILL.md) | 世界规则、资源制度、时空关系与一致性 |
| [`ai-character-design`](skills/ai-character-design/SKILL.md) | 角色概念、造型、表演和生产资产 |
| [`ai-scene-design`](skills/ai-scene-design/SKILL.md) | 场景空间、构图、光色、材质与状态派生 |
| [`ai-storyboard-design`](skills/ai-storyboard-design/SKILL.md) | Beat、调度、镜头节奏和连续性 |
| [`ai-prompt-execution-contract`](skills/ai-prompt-execution-contract/SKILL.md) | 静态图像及视频的可执行生成请求 |
| [`ai-video-production-classroom`](skills/ai-video-production-classroom/SKILL.md) | 平台请求、视频续接、生产状态和剪辑交付 |
| [`ai-generation-review`](skills/ai-generation-review/SKILL.md) | 基于真实媒体证据的诊断、修复和回归评审 |

## 快速开始

### ChatGPT 桌面端 / Codex

打开 **Plugins** 目录，找到 `Universal AI Video Production` 并选择安装。仓库已经公开，无需申请私有仓库读取权限。如果目录中尚未出现该插件，请让工作区管理员先按下方步骤导入 Marketplace。安装完成后请新建聊天或会话；十个 Skill 会变为可用能力，并在匹配任务时按需加载。

### Codex CLI

在 Codex CLI 中输入 `/plugins`，从已配置的 Marketplace 安装 `universal-ai-video-production`，然后启动一个新会话。Codex IDE 扩展目前不支持 Plugins；在 IDE 中请改用下方“手动获取并作为项目使用”的方式。

### 工作区管理员从 GitHub 导入

管理员进入 **Admin → Plugins → Add → Import marketplace**，填写仓库地址：

```text
https://github.com/pigjio/universal-ai-video-production-skills
```

Marketplace 清单位于仓库根目录的 `.agents/plugins/marketplace.json`，因此 **Path 留空**。这是公开仓库，不需要私有仓库读取权限；导入后，成员即可通过 Plugins 目录安装。

如果本地 Agent 已具备 GitHub 与插件管理能力，也可以让它协助完成上述步骤；这只是便捷方式，不是所有 Codex 入口都支持的通用安装方式。

后续可直接用自然语言开始，不需要记住 Skill 名，例如：

```text
我是第一次使用这套 AI 影像制作 Skills。我只有一个模糊想法，请一次只带我完成一个小目标；我不知道时给我容易比较的选项。
```

也可以直接使用韩文：

```text
저는 AI 영상을 처음 만듭니다. 지금은 막연한 아이디어만 있습니다. 한 번에 한 단계씩 도와주세요. 제가 모르겠다고 하면 비교하기 쉬운 선택지를 주세요.
```

Codex 官方说明：[构建 Plugins](https://learn.chatgpt.com/docs/build-plugins)、[使用 Plugins](https://learn.chatgpt.com/docs/plugins)、[企业工作区插件管理](https://learn.chatgpt.com/docs/enterprise/plugin-management)。

### 手动获取并作为项目使用

```bash
git clone https://github.com/pigjio/universal-ai-video-production-skills.git
cd universal-ai-video-production-skills
```

仓库已经公开，克隆时不需要 GitHub 私有仓库访问权限。

### 在 Agent 中打开仓库

- **Codex / Hermes 及兼容 Agent**：打开仓库根目录；入口规则位于 [`AGENTS.md`](AGENTS.md)。
- **Claude Code**：打开仓库根目录；入口规则位于 [`CLAUDE.md`](CLAUDE.md)。
- **其他 Agent**：先让它读取 [`START_HERE.md`](START_HERE.md)、[`shared/novice-guidance-protocol.md`](shared/novice-guidance-protocol.md) 和 [`shared/common-contract.md`](shared/common-contract.md)。

无需手动选择 Skill。总控会根据任务加载最小必要的领域方法。

### 用自然语言开始

可以直接复制：

> 我是第一次使用 Agent。我现在有【一个想法 / 故事或剧本 / 图片 / 不理想的生成结果】。请一次只带我完成一个小目标；我不知道时给我容易比较的选项。

也可以从具体任务开始：

```text
我有一个关于告别的短片想法，但还没想清楚。先给我三个容易比较的核心意象。
```

```text
这是我的剧本。不要全部重写，先找出第二场失去张力的原因，并试改关键动作。
```

```text
这是角色参考图和生成结果。请先判断身份漂移发生在哪里，再给最小修复方案。
```

### 确认并保存阶段成果

阶段成果成熟后，Agent 会让你选择：**确认并保存、确认但暂不保存、继续修改**。需要保存时可说：

> 我确认本阶段完成。请保存为新的 Markdown 版本，不覆盖旧版。

第一次保存时，提供一个项目文件夹即可。Agent 会自动创建缺失的基础记录：

- `PROJECT_BRIEF.md`
- `AUTHORIZATIONS.md`
- `PROJECT_INDEX.md`
- `SESSION_HANDOFF.md`
- `DECISIONS.md`

阶段成果默认按 `名称_vNNN.md` 保存。完整保存还包括回读主文件、更新并回读项目索引和会话交接。

### 下次继续

在新会话中说：

> 请先读取 AUTHORIZATIONS.md、PROJECT_INDEX.md 和 SESSION_HANDOFF.md，再读取当前采用的完整成果文件。用普通语言告诉我已经确认到哪里，然后一次推进一个小目标。

## 学生最终会得到什么

学生不需要先学习剧作、导演或提示词理论。只需用自然语言描述、比较、否决和确认，Agent 在后台调用专业方法，逐步形成：

1. **满意的剧本**：类型承诺、人物选择、场景因果与对白经讨论收敛；
2. **有剧本依据的分镜**：每个景别、视点、动作和切点能追溯到场景功能、信息或表演需要；
3. **可直接复制的 Seedance / 即梦视频提示词**：按生成请求提供素材绑定、起点、空间、摄影、时间轴、物理、声音、终点和关键禁止项。

用户说“太普通”“不够电影感”“人物不对”“这一段太慢”“镜头太碎”或“只改第三镜”都可以。Agent 应把反馈转成少量可比较方案，只改受影响内容。提示词完成不代表已经上传或生成；真实出片仍需平台执行和结果评审。

## 工作流

```text
自然语言需求
→ Agent 识别入口与当前阶段
→ 每轮完成一个小目标
→ 用户比较、否决或确认
→ 展示完整阶段成果
→ 明确确认与授权保存
→ 创建新的 Markdown 版本并回读验证
→ 更新项目索引和会话交接
→ 进入下一阶段或跨会话恢复
```

从分镜进入生产时：

```text
storyboard shots
→ production_group / Clip / DO
→ generation_request
→ 真实平台提交与原始输出
→ 十维评审
→ edit_unit
→ 人工裁决与交付
```

计划、提交、生成、评审和人工接受是不同状态。没有真实媒体时，系统不会伪造任务 ID、时间码、声音结论或通过结果。

## 交互方式与工作深度

交流方式可以随时切换：

- **新手模式**：默认，使用普通语言逐步推进；
- **协作模式**：共同比较、试写和推敲方案；
- **专业模式**：显示完整字段、依赖、状态和生产交接。

工作深度独立管理：

- `production`：默认，用于真实创作和生产；
- `provenance`：按需查看方法来源和证据边界；
- `research`：只有明确同意后启用，不能反向改变生产确认状态。

## 权限边界

以下行为分别需要相应授权，不能相互替代：

- 保存草稿或定稿；
- 覆盖或删除文件；
- 上传素材；
- 调用付费生成；
- 发布作品；
- 将作品用于评测、研究、训练或公开展示。

“不错”“继续”“方向对了”只代表积极反馈，不自动构成阶段确认或任何外部操作授权。

## 校验

在仓库根目录运行：

```bash
python evals/validate_package.py .
```

静态校验覆盖 Skill 版本和引用、共享协议一致性、项目模板、公共 schema、递归资源与私有路径泄漏。它不能替代真实平台生成、艺术质量判断或外部用户测试。

## 文档导航

- [新手入口](START_HERE.md)
- [0.7.0总览](00_通用AI影像制作Skills_总览.md)
- [完整使用说明](skills/ai-creative-workflow-router/references/user-guide.md)
- [新手协作协议](shared/novice-guidance-protocol.md)
- [公共状态与授权协议](shared/common-contract.md)
- [0.5.0 验证报告](03_0.5.0_新手引导与阶段落盘验证报告.md)
- [0.5.1 韩文增强测试报告](evals/korean-validation-0.5.1.md)
- [0.6.0 创作协作增强与验证报告](evals/validation-0.6.0.md)
- [0.7.0变更与验证报告](evals/validation-0.7.0.md)

## 验证边界

0.6.0 在原有结构化工作流和韩文支持基础上，增加了剧作理论选择、类型惯例、剧本到分镜的依据链，以及面向 Seedance / 即梦的可复制交付结构。它不代表所有模型、平台入口、随机种子、艺术风格和真实用户路径都已验证。平台能力会变化；涉及模型时长、素材数量、声音或编辑能力的结论，应记录来源、模型、入口和核验日期。
