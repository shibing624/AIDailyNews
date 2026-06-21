---
title: "Daily News #2026-06-22"
date: "2026-06-22 00:32:43"
description: "Neuralwatt: 基于能耗的AI推理服务平台
Jacobi: 专为物理仿真子程序设计的IDE
特斯拉计划推出模块化AI数据中心硬件“Megapod”
Open Knowledge Format (OKF)：基于 Markdown 的通用知识表示格式
AkaRouter：经济高效的一键多模型API路由方案
DeerFlow 2.0：超级代理系统的重构与升级
OpenMontage——开放视频制作的未来
极致高效的AI代码智能引擎：Codebase-Memory-MCP分析
Agent Reach：赋能AI获取多平台互联网数据的能力层"
tags: 
- "多媒体自动化"
- "代码智能引擎"
- "人工智能"
- "API路由"
- "网络数据应用"
- "代理系统"
- "AI云服务"
- "物理模拟"
- "知识表示"

---

> - Neuralwatt: 基于能耗的AI推理服务平台
> - Jacobi: 专为物理仿真子程序设计的IDE
> - 特斯拉计划推出模块化AI数据中心硬件“Megapod”
> - Open Knowledge Format (OKF)：基于 Markdown 的通用知识表示格式
> - AkaRouter：经济高效的一键多模型API路由方案
> - DeerFlow 2.0：超级代理系统的重构与升级
> - OpenMontage——开放视频制作的未来
> - 极致高效的AI代码智能引擎：Codebase-Memory-MCP分析
> - Agent Reach：赋能AI获取多平台互联网数据的能力层

## 🤖 AI info

### [Neuralwatt: 基于能耗的AI推理服务平台](https://portal.neuralwatt.com/)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-22 00:09:18

Neuralwatt 是一个提供基于能耗定价的AI推理服务的平台，目标是提高AI工作负载的透明性和可控性。用户可以通过API连接不同的大型语言模型，实时查看每次推理的能量消耗及相应成本。它同时支持托管服务和本地部署，提供详细的能效指标以便优化AI计算工作负载。平台特色包括vLLM推理优化、与OpenAI兼容的API、按需求选择能耗或令牌计费模式，并支持多种开源模型接入。Neuralwatt 为那些注重AI运行效率、成本透明以及节能的开发者与企业提供了一个高性能解决方案。

### [Jacobi: 专为物理仿真子程序设计的IDE](https://jacobee.netlify.app/)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-22 00:20:46

Jacobi 是一款专为物理仿真子程序开发设计的IDE，支持 Fortran、C++ 和 Python 语言。它通过对接分析解法，对开发者编写的子程序进行测试并给出AI诊断，包括指出具体失败原因和代码中的相关位置。当前主要支持 Abaqus，未来计划支持 COMSOL 和 LS-DYNA 等生态。特点包括自动语法高亮、静态分析、AI代码补全，无需项目配置即可直接运行测试。每次测试会将子程序的所有数值结果送至 AI 进行诊断，并提供物理学先导的具体解释。此外，还支持材料参数校正、解析 Abaqus 输入文件、浏览日志等功能，强化开发效率和准确性。这个工具适合致力于提高子程序物理行为正确性的开发者。

### [特斯拉计划推出模块化AI数据中心硬件“Megapod”](https://electrek.co/2026/06/21/tesla-megapod-ai-data-center-hardware/)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-22 00:17:06

特斯拉申请了名为“Megapod”的商标，计划推出模块化AI数据中心硬件。这款产品被描述为一体化的AI计算系统，整合服务器、数据处理硬件、网络设备、电力分配单元和冷却系统。但市场已有如Nvidia GB200 NVL72等成熟竞争品，又面临同名产品的商标冲突问题。此外，特斯拉无销售计算硬件的经验，其AI硬件开发历来进展缓慢。现有的成功点在于其电池与能源管理业务，因此若“Megapod”聚焦于电力与热管理的整合解决方案，可能更具可行性。当前，产品状态仍停留在构想阶段，未来能否形成实际产品仍有待观察。

## 📥 Tech News

### [Open Knowledge Format (OKF)：基于 Markdown 的通用知识表示格式](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)

来源：Hacker News - Newest: "llm"

发布时间：2026-06-22 00:06:05

OKF（Open Knowledge Format）是一种通用、厂商中立的知识表示格式，基于 Markdown 文件和 YAML 前缀数据结构，适用于知识的结构化管理及存储。其主要优点是便于机器和人类共用文件同时实现跨平台操作。OKF 提供知识目录、参考代理及可视化工具，将知识以图形化和文本文档格式输出，促进文档生成和消费的集成化。参考代理支持两阶段操作，利用 BigQuery 生成初始文档后，通过 LLM 爬取补充信息或扩展链接，并生成自包含的交互式 HTML 视图。这种格式适合开发者、高级工程师和学术用途的知识库管理，凸显了其在知识分享和组织上的灵活性和效率。

### [AkaRouter：经济高效的一键多模型API路由方案](https://akarouter.dev)

来源：Hacker News - Newest: "llm"

发布时间：2026-06-22 00:19:59

AkaRouter 是一个多模型 API 集成服务，主打高经济性和低复杂性。该平台提供单一 API Key 即可访问多种热门 LLM 模型，如 Claude、GPT、Google Gemini 等，支持每次调用收费且价格固定，消除输入输出分词成本的复杂计算问题，提供稳定且透明的定价策略。其动态路由机制提升了可用性，确保请求被实时监控并自动重新分配，避免因外部 API 宕机引发中断。此外，AkaRouter 支持弹性订阅，允许自由组合模型，匹配生产需要。每次调用收费，无隐藏费用，为用户降低 87% 的 API 开销，适用于大中型企业的生产环境和研发需求。

## 💾 Daily Code

### [DeerFlow 2.0：超级代理系统的重构与升级](https://github.com/bytedance/deer-flow)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-22 00:31:15

DeerFlow是一个开源的超级代理框架，旨在通过整合子代理、长期记忆和沙盒环境来强大增强工作流程。DeerFlow 2.0进行了重构，支持统一管理多模型和工具，拥有独立的技能和模块化扩展功能，其功能集包括计算代理、自定义工具连接、冲突避免与上下文传递等。新增的InfoQuest模块显著增强了搜索与爬取能力。同时，系统完全支持嵌入式Python客户端，并能够无缝连接如Claude Code、Codex等主流语言模型。支持Docker快速部署，建议应用到高性能环境中以实现高效协同。DeerFlow因其在开源社区的积极开发，展示了强大的创新能力，是开发者和研究人员管理复杂任务流的利器。

### [OpenMontage——开放视频制作的未来](https://github.com/calesthio/OpenMontage)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-22 00:31:15

OpenMontage是一款首个开源的智能化视频制作系统，其核心功能是通过代理（agent），将文字描述转化为完整的视频作品，包括研究、剧本编写、素材生成、剪辑及最终输出。它支持创建基于图像的动态视频以及结合免费的开放素材进行视频生产，使用者甚至无需手动生成素材。提供了精心设计的样例，如太空科幻预告片《SIGNAL FROM TOMORROW》、动画短片《THE LAST BANANA》等，表明了其强大的自定义生成能力。同时，它还可以基于参考视频创建新的视频概念和制作路径。此外，OpenMontage免费提供多种无人工参与的基础功能，使用者只需提供必要的关键内容，系统即可自动完成繁琐的生产过程。整体功能和灵活性极大地便利了希望低成本、高效生产视频的开发者群体，是一款极具创新性和实用价值的工具。

### [极致高效的AI代码智能引擎：Codebase-Memory-MCP分析](https://github.com/DeusData/codebase-memory-mcp)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-22 00:31:19

Codebase-Memory-MCP 是一个高效强大的代码智能引擎，能够以毫秒级完成代码库的全索引。其核心功能包括对158种语言的支持，通过Tree-sitter的AST分析和混合LSP技术，为Python、TypeScript、Java等语言提供语义解析。产品能够构建持久的知识图谱，包括函数、类、HTTP路由等详情。此外，它具备14种工具如死代码检测、架构追踪等。MCP以极高性能著称，如3分钟内索引Linux Kernel的28M代码行。所有操作均100%本地进行，确保安全性和隐私。其内置的3D knowledge graph UI为复杂项目提供直观的可视化支持，极具吸引力且易于部署。

### [Agent Reach：赋能AI获取多平台互联网数据的能力层](https://github.com/Panniantong/Agent-Reach)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-22 00:31:19

Agent Reach 为AI代理提供快速接入各平台数据的能力，具备极高的兼容性和扩展性。支持阅读网页、提取视频字幕、RSS订阅等广泛功能，能实时追踪各平台规则变化并自动适配。工具完全开源，数据和登录凭证本地化管理保障用户隐私，支持通过CLI一键完成安装、配置。它的多渠道后端路由设计，确保工具即使在接入接口变化时也能快速切换并保持稳定工作。支持包括小红书、B站、Twitter等多平台数据，适合需要扩展AI联网功能的开发者。对Agent Reach的模块化组件设计避免了技术维护的复杂性，是一个极具潜力的网络数据应用层解决方案。
