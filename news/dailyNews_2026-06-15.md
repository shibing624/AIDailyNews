---
title: "Daily News #2026-06-15"
date: "2026-06-15 00:23:24"
description: "Dream Server：搭建本地 AI 服务的全能工具
Manticthink: 用于 Ollama 模型的私密 Web UI
Tw93 工程师杂志的最新内容漫谈与推荐
Pytest: 强大简洁的Python测试框架
Kronos: 开源金融行情语言模型
AI助力的实时跨平台搜索引擎：/last30days
PM技能市场：构建更智能的产品决策"
tags: 
- "测试框架"
- "金融AI"
- "人工智能搜索"
- "产品管理"
- "技术周刊"
- "AI本地部署"
- "隐私AI工具"

---

> - Dream Server：搭建本地 AI 服务的全能工具
> - Manticthink: 用于 Ollama 模型的私密 Web UI
> - Tw93 工程师杂志的最新内容漫谈与推荐
> - Pytest: 强大简洁的Python测试框架
> - Kronos: 开源金融行情语言模型
> - AI助力的实时跨平台搜索引擎：/last30days
> - PM技能市场：构建更智能的产品决策

## 🤖 AI info

### [Dream Server：搭建本地 AI 服务的全能工具](https://github.com/Light-Heart-Labs/DreamServer)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-15 00:09:07

Dream Server 是一个面向本地搭建 AI 服务器的工具，通过整合诸如 Ollama、Open WebUI、n8n、ComfyUI 和隐私工具等功能，为用户提供无需云订阅的 AI 部署方案。它支持 Linux、macOS 和 Windows 平台，并通过硬件自动检测，合理选取和优化 LLM（大语言模型），简化安装和管理流程。此外，Dream Server 专注隐私保护，所有数据默认存储在本地，用户可选择额外的云模式。此工具还充分考虑了扩展性，所有服务支持插件化设计，方便用户在实例中加入更多自定义模块。其简化流程和开箱即用的特性使得不具备深厚技术背景的用户也能轻松实现本地 AI 部署，是自建 AI 服务的理想选择。

### [Manticthink: 用于 Ollama 模型的私密 Web UI](https://manticthink.com/d/tq00dkq)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-15 00:06:08

Manticthink 提供了一个免费的 Web UI 可用来连接 Ollama 模型，支持输入自己的 API 密钥或直接使用本地 Ollama 实例。该工具突出了隐私保护，从不存储用户密钥或消息，除非用户主动选择通过 AI 辩论功能共享内容。此外，Manticthink 支持模型多样性，允许用户从 gpt-oss、Qwen 到 Llama 等模型中选择。其简约无安装需求的特点，让用户可快速启动并运行一个浏览器端的 AI 环境，适用于需要轻量级、高隐私需求的场景。然而，其功能专注于 Web UI 页面，可能对深度集成需求稍显不足。

## 📥 Tech News

### [Tw93 工程师杂志的最新内容漫谈与推荐](https://weekly.tw93.fun/posts/270/)

来源：潮流周刊

发布时间：2026-06-15 08:00:00

本文是一个接地气的技术周刊更新，通过多个模块展示作者的近期动态与技术推荐。作者在随手拍摄杭州乔村风景时引入内容，并分享了诸多技术相关的信息：如简历生成工具 Kami，软件 Mole 的最新更新以及相关开发数据，还包括桌面应用打包工具 Pake 和聊天应用 Kaku 的更新。本周刊同时融入个人随笔，作者反思其账号作为一个“非流量型”的自我表达载体的定位，呈现出接地气且真实的工程师视角。这种贯穿技术推荐和个人生活的杂志风格增加了独特性，让读者感受到持续迭代的魅力，非常适合技术爱好者关注。

## 💾 Daily Code

### [Pytest: 强大简洁的Python测试框架](https://github.com/pytest-dev/pytest)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-15 00:22:29

Pytest 是一个流行的 Python 测试框架，旨在简化小型测试编写，同时支持复杂的功能测试。其特色包括详细的断言内省、模块和函数的自动发现、参数化测试管理，以及支持运行 unittest（或 trial）测试套件。此外，Pytest 自带强大的插件架构，拥有超过 1300 多个插件和热衷的开发者社区。支持 Python 3.10+ 和 PyPy3，并提供开箱即用的企业支持服务（通过 Tidelift 提供）。开发者可以通过其丰富的文档、Bug 提交（通过 GitHub）、以及 Open Collective 资助平台来获得支持。此外，Pytest 完全开源，遵循 MIT 许可证发布，是测试 Python 项目的一个推荐选择。

### [Kronos: 开源金融行情语言模型](https://github.com/shiyu-coder/Kronos)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-15 00:22:29

Kronos 是首个针对金融 K 线（K-Lines）序列设计的开源基础模型，专注于处理高噪声的金融数据。其两阶段框架包括：先通过专门的分词器量化 OHLCV 数据为分层离散 tokens，然后利用大规模自回归 Transformer 进行预训练，为多种量化任务提供了统一解决方案。Kronos 提供了多种模型（大小和参数量不同），并支持 Hugging Face Hub 的存取。此外，官方提供了用户友好的预测工具（KronosPredictor）和一个可视化预测结果的在线 demo。通过提供微调脚本和高效的并行预测接口，Kronos 成为金融市场分析和预测领域的重要工具，尤其适用于量化交易和时间序列分析的开发者和研究人员。

### [AI助力的实时跨平台搜索引擎：/last30days](https://github.com/mvanhorn/last30days-skill)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-15 00:22:33

/last30days 是一个由AI代理驱动的实时跨平台搜索和内容整合引擎。它通过聚合多个平台（如Reddit、YouTube、X等）的用户互动数据（如点赞、浏览量等），提供基于真实人群参与度的评分，而非传统的SEO算法。此工具适用于会议前、销售前、分析工具对比甚至旅行准备等场景，可以快速获取目标对象最近30天的动态信息。该引擎支持零配置操作，可整合各平台API或用户自定义密钥，并能生成可共享的HTML简报。其核心理念为以社会相关性替代SEO相关性，提供最新鲜且真实的跨平台整合信息。

### [PM技能市场：构建更智能的产品决策](https://github.com/phuryn/pm-skills)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-15 00:22:33

PM Skills Marketplace 提供68项项目管理技能和42个链式工作流覆盖产品生命周期的各个阶段，从策略制定到执行和增长。通过内置的PM框架和循序指导，提高产品决策质量，而不仅是加速文档。其技能与Claude等AI助手集成，自动加载或通过命令触发。9个插件涵盖产品发现、战略、执行等领域，功能包括假设测试、产品矩阵设计、受访者脚本生成等。支持命令行界面（CLI）和多种AI助手，方便开发者或PM快速上手。
