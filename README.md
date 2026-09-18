# 通用 AI 影像制作 Skills

[中文](README.md)｜[한국어](README.ko-KR.md)

版本：**0.7.0｜公开精简版**

一个包含十个内部技能的创作协作插件，帮助你讨论想法、完善剧本、整理角色和场景、设计文字分镜，以及输出 Midjourney／Seedance 提示词。你不需要先学习理论或选择技能。

## 开始使用

下载 [v0.7.0 压缩包](https://github.com/pigjio/universal-ai-video-production-skills/archive/refs/tags/v0.7.0.zip)，解压后让兼容的 Agent 读取 [START_HERE.md](START_HERE.md)。已有旧副本时重新获取本版；不要把旧文件夹直接合并覆盖到新包，以免保留额外文件。

支持插件安装的环境可使用本仓库的 Marketplace 清单：`.agents/plugins/marketplace.json`；插件标识为 `universal-ai-video-production`。具体安装入口以当前客户端为准。只需安装一个插件，无须分别安装十个技能。

> 我想做一部短片，请先和我讨论想法与剧本，不要一次问我很多问题。

## 你可以得到什么

- 可讨论的大纲和详细剧本，按反馈继续修改。
- 按需整理角色、场景清单，再选择是否讨论概念图提示词。
- 精简但包含面部特征的角色提示词，不默认添加 3D 风格。
- 以剧本关键词为基础的轻量场景提示词。
- 有剧本依据的文字分镜与完整字段的 Seedance 视频提示词；每个视频提示词块以“无背景音乐”结束。
- 在实际提供图片或视频后，讨论具体问题及修改方向。

本版不包含生成服务，也不保证生成效果。保存、上传、生成、付费、公开及研究使用按各自授权执行。

## 文档导航

- [快速开始](START_HERE.md)
- [使用说明](skills/ai-creative-workflow-router/references/user-guide.md)
- [功能总览](00_通用AI影像制作Skills_总览.md)
- [新手使用方式](shared/novice-guidance-protocol.md)
- [协作与保存约定](shared/common-contract.md)
- [视频提示词模板](skills/ai-prompt-execution-contract/references/video-template.md)
- [来源与许可](NOTICE.md)
- [MIT 许可证](LICENSE)

维护检查：`python evals/validate_public.py`。该检查只验证包结构、引用和固定交付约定，不证明创作质量或实际生成成功。
