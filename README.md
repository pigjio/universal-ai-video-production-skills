# 通用 AI 影像制作 Plugin

[中文说明](README.md)｜[한국어 안내](README.ko-KR.md)

面向 AI 短片、动画和视觉叙事的 Codex 创作协作插件。用户只需安装一次，即可获得一个总控 Router 和九个专业 Skill；它们共同把创意、剧本、世界观、角色、场景、分镜、生成请求、视频生产和结果评审串成一条可追踪、可恢复的工作流。

版本：**0.7.0**

> 你不需要记住 Skill 名，也不需要先学提示词。你只需描述、比较、否决和确认；Agent 负责选择方法、维护阶段、版本和文件。

## 创作协作

学生不需要先学理论或填写长表，只需自然地说明想法和希望修改的地方。可以从大纲、详细剧本、角色、场景或分镜开始，也可以直接修改已有成果。

大纲或详细剧本讨论收口后，Agent 会询问是否需要整理角色、场景清单及 Midjourney 概念图提示词。角色提示词保留面部特征，不默认添加 3D 风格；场景以剧本关键词和必要的视觉方向为主。

**v0.7.0 已发布，Marketplace 安装入口指向 v0.7.0。** 已安装或缓存旧内容的用户需要重新获取。真实视频生成、学生使用体验与艺术满意度仍需另外验证。

## 主要特性

- **四种自然入口**：从模糊想法、现有故事或剧本、已有图片、失败的生成结果任意切入。
- **一个 Plugin，十个专业 Skill**：只安装一次，内部覆盖从早期创意到真实生成结果评审的完整链路。
- **自然语言协作**：按需要比较方向、试写或局部修改，不要求学生先学术语。
- **每轮一个小目标**：最多询问一个真正阻断的问题；“不知道”是有效回答。
- **阶段确认与保存分离**：积极反馈不等于定稿，保存不等于上传、生成、付费、发布或研究同意。
- **完整 Markdown 阶段成果**：确认后创建新版本，不静默覆盖旧版，并回读验证。
- **跨会话恢复**：通过项目索引、授权记录和会话交接恢复真实进度，不凭聊天记忆猜最新版。
- **生产证据可追踪**：区分 planned、submitted、generated、reviewed 与人工接受，不把提示词完成冒充生成完成。
- **Seedance / 即梦提示词支持**：提供逐镜完整字段、素材准备与续接说明；视频提示词末行固定为“无背景音乐”。
- **研究使用需单独同意**：普通创作与保存授权不包含研究使用。
- **中韩文自然协作**：韩文请求可直接触发总控与十个专业阶段；Agent 跟随用户语言，授权和状态逻辑不随语言改变。

## Plugin 内的十个 Skills

这十个 Skill 是同一个 Plugin 的内部专业模块，不需要分别安装。安装后它们会在新会话中可用；Codex 会按当前任务加载匹配的 Skill。通常直接描述需求即可，也可以在支持的界面用 `@` 明确调用某个 Skill。

| Skill | 用途 |
|---|---|
| [`ai-creative-workflow-router`](skills/ai-creative-workflow-router/SKILL.md) | 新手入口、当前任务选择与会话恢复 |
| [`ai-visual-ideation`](skills/ai-visual-ideation/SKILL.md) | 从模糊想法形成可比较的创意方向 |
| [`ai-screenplay-development`](skills/ai-screenplay-development/SKILL.md) | 大纲、详细剧本、动作与对白修改 |
| [`ai-worldbuilding`](skills/ai-worldbuilding/SKILL.md) | 当前故事所需的世界设定与一致性 |
| [`ai-character-design`](skills/ai-character-design/SKILL.md) | 角色外形与 Midjourney 概念图提示词 |
| [`ai-scene-design`](skills/ai-scene-design/SKILL.md) | 剧本场景与 Midjourney 概念图提示词 |
| [`ai-storyboard-design`](skills/ai-storyboard-design/SKILL.md) | 有剧本依据的文字分镜、节奏与衔接 |
| [`ai-prompt-execution-contract`](skills/ai-prompt-execution-contract/SKILL.md) | 可复制的图像与 Seedance 视频提示词 |
| [`ai-video-production-classroom`](skills/ai-video-production-classroom/SKILL.md) | 生成准备、素材安排与视频续接 |
| [`ai-generation-review`](skills/ai-generation-review/SKILL.md) | 根据实际图片或视频讨论问题与修改 |

## 快速开始

### 获取与安装

下载 [v0.7.0 压缩包](https://github.com/pigjio/universal-ai-video-production-skills/archive/refs/tags/v0.7.0.zip)，解压后让兼容 Agent 读取 `START_HERE.md`。更新时使用新解压目录，不与旧文件夹混合。

支持插件安装的环境可以使用本仓库的 Marketplace 清单 `.agents/plugins/marketplace.json`。插件标识为 `universal-ai-video-production`，只需安装一次。具体入口以当前客户端为准。

仓库地址：

```text
https://github.com/pigjio/universal-ai-video-production-skills
```

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

1. **经讨论完善的剧本**：围绕用户想法，逐步修改情节、动作与对白；
2. **有剧本依据的分镜**：按当前剧本讨论景别、视点、动作、时长与衔接；
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
文字分镜
→ 可复制的视频提示词与素材准备
→ 授权后进行真实平台生成
→ 根据实际结果讨论修改
→ 用户确认与交付
```

计划、提交、生成、评审和人工接受是不同状态。没有真实媒体时，系统不会伪造任务 ID、时间码、声音结论或通过结果。

## 交互方式

默认用普通语言逐步推进；也可以要求批量输出、比较方案或只修改某一处。不必按固定顺序经过所有阶段，也可以暂停或只讨论而不保存。

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
python evals/validate_public.py
```

静态检查覆盖包结构、引用、中韩文导航、提示词字段和文件清单，不替代真实平台生成、艺术质量判断或用户测试。

## 文档导航

- [快速开始](START_HERE.md)
- [使用说明](skills/ai-creative-workflow-router/references/user-guide.md)
- [功能总览](00_通用AI影像制作Skills_总览.md)
- [新手使用方式](shared/novice-guidance-protocol.md)
- [协作与保存约定](shared/common-contract.md)
- [视频提示词模板](skills/ai-prompt-execution-contract/references/video-template.md)
- [来源与许可](NOTICE.md)
- [MIT 许可证](LICENSE)

## 验证边界

本插件提供创作协作与文本交付，不包含图片或视频生成服务。提示词完成不代表已上传、生成或通过评审，也不保证作品质量或人物一致性。平台的时长、素材数量、声音及口型能力需按实际模型和入口核验。
