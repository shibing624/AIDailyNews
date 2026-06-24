---
title: "Daily News #2026-06-25"
date: "2026-06-25 01:06:35"
description: "AI技能市场中的供应链攻击：ClawHub隐藏的恶意技能威胁
如何学习第二门、第三门编程语言
Übers Ninja：用于互联网搜索的桌面应用
Cascade Router：动态流量路由与成本优化代理
ModelFit：正确性优先的代码评估工具
股票智能分析系统：每日决策仪表盘
OpenMontage：开源智能视频制作工具
OpenMontage：开源智能视频制作系统
Codebase Memory MCP：快速高效的代码智能引擎"
tags: 
- "应用程序"
- "开源工具"
- "代码工具"
- "编程"
- "金融科技"
- "AI路由"
- "网络安全"

---

> - AI技能市场中的供应链攻击：ClawHub隐藏的恶意技能威胁
> - 如何学习第二门、第三门编程语言
> - Übers Ninja：用于互联网搜索的桌面应用
> - Cascade Router：动态流量路由与成本优化代理
> - ModelFit：正确性优先的代码评估工具
> - 股票智能分析系统：每日决策仪表盘
> - OpenMontage：开源智能视频制作工具
> - OpenMontage：开源智能视频制作系统
> - Codebase Memory MCP：快速高效的代码智能引擎

## 🤖 AI info

### [AI技能市场中的供应链攻击：ClawHub隐藏的恶意技能威胁](https://cyber.netsecops.io/articles/openclaws-skill-marketplace-and-the-emerging-ai-supply-chain-threat/)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-25 00:52:03

在2026年2月至5月间，Unit 42研究人员发现一个针对OpenClaw AI代理生态系统的复杂攻击活动。攻击者成功发布了能够绕过安全扫描的恶意AI技能。这些技能通过混淆和社会工程诱导用户执行命令，从而安装如Atomic macOS Stealer (AMOS)和新变种cluw等信息窃取恶意软件。攻击方法依赖用户的互动，通过将指令伪装为合法请求允许AI代理执行恶意代码。主要影响包括窃取敏感信息如浏览器Cookies、加密钱包数据和系统密码，主要针对金融市场用户。应对措施包括应用程序隔离、用户培训、网络流量过滤和EDR解决方案。此攻击揭示了AI代理技术生态系统面临的系统性安全风险，迫切需要行业加强对AI技能权限和隔离的控制。

### [如何学习第二门、第三门编程语言](https://news.ycombinator.com/item?id=48662310)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-25 00:31:13

文章探讨了学习多门编程语言的心得和建议。学习第二门编程语言通常能开阔视野，让开发者理解不同语言的适用场景和特点，同时也为解决复杂问题提供更多选择。随着学习第三、第四门语言，开发者开始理解语言之间的共性和差异，能够更高效地选择解决问题的工具。文章强调实践的重要性，并建议通过实际项目不断挑战自己，以深化对新语言的掌握。

### [Übers Ninja：用于互联网搜索的桌面应用](https://uberninja.co/)

来源：Hacker News - Newest: "AI"

发布时间：2026-06-25 00:24:43

Über Ninja是一款专为Windows和macOS设计的互联网搜索工具，它不能在手机上使用，强调其独特的桌面定位。应用旨在提供类似Spotlight的快速搜索功能，但覆盖整个互联网数据，帮助用户更高效地查找和管理信息。虽然功能设计引人注目，但针对手机限制可能使部分用户群体受限，仅适用于目标桌面用户。适合追求快速搜索体验的用户使用。

## 📥 Tech News

### [Cascade Router：动态流量路由与成本优化代理](https://cascade-router.github.io/cascade-router/)

来源：Hacker News - Newest: "llm"

发布时间：2026-06-25 00:17:33

Cascade Router 是一个高性能的 C++ AI 代理工具，通过预测用户提示的复杂度，动态分配流量到最节省成本的语言模型（LLM）。该工具运行快速，仅需 4.59 毫秒即可完成推理过程，包括标记化、ONNX 嵌入和机器学习预测。它通过路由轻量级任务到速度快且低成本的模型，如 gpt-4o-mini 或 Claude 3 Haiku，大幅降低使用高阶模型的开销。当小型模型验证失败时，请求会无缝提升至高阶模型处理，同时保证无额外延迟。用户还可以使用 ROI 计算器，估算每月和每年节省成本，并支持企业边缘部署，以及通过企业许可获取自定义功能，例如路由权重、日志审计和单点登录（SSO）。该工具特别适合需要大规模处理的企业技术团队，极大优化了计算成本和任务分配效率。

### [ModelFit：正确性优先的代码评估工具](https://github.com/kwadwoadu/modelfit)

来源：Hacker News - Newest: "llm"

发布时间：2026-06-25 00:18:31

ModelFit 是一个调试与评估代码模型的工具，旨在通过预设探针和评分细则对候选模型进行盲评，并结合成本和延迟因素排名。这种方法不同于传统公共基准，强调在特定代码库中是否有便宜或二级模型可以有效解决问题。主要特点包括生成用于评分的探针和报告的自动化流程，并兼顾安全性，确保敏感数据不会被无意泄露。用户可以通过生成探针后进行快速测试和全面运行，在模型性能不足时自动记录覆盖问题。它提供灵活工作流设置，支持全局报告生成。虽然强调正确性，但对样本数量有所限制，对小型或特殊任务可能存在不足。该工具主要面向开发者和技术社区，帮助更便捷地评估和优化代码模型表现。

## 💾 Daily Code

### [股票智能分析系统：每日决策仪表盘](https://github.com/ZhuLinsen/daily_stock_analysis)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-25 01:05:17

股票智能分析系统提供基于 AI 的多市场智能分析功能，覆盖全球主要股票市场，包括 A股、港股、美股、日韩股等。工具每日自动生成决策仪表盘，推送至企业微信、Telegram 等平台，支持行情数据和技术指标分析，同时能够利用 AI 策略进行深入问股，并推送买卖操作建议、趋势预测和风险警报。支持使用 Docker、GitHub Actions 等自动化方式快速部署，功能丰富，包括多因子选股、回测分析和多轮问股策略。适合金融从业者和投资者进行全天候的智能化股票监控和分析，技术栈覆盖 OpenAI、TickFlow、AkShare 等多种数据源。

### [OpenMontage：开源智能视频制作工具](https://github.com/calesthio/OpenMontage)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-25 01:05:17

OpenMontage 是一个开源的智能视频制作系统，可通过简单语言描述来实现视频的全流程生产，包括脚本、素材生成、编辑和最终合成。支持从图像到真实视频的制作，并能利用开源资源进行提升，如 Archive.org 和 NASA。同时该系统提供了各种创意案例，如科幻预告片《SIGNAL FROM TOMORROW》、动画短片《THE LAST BANANA》，及多款低成本制作的视频。用户可以从已有参考视频入手，利用分析功能生成差异化方案。技术要求包括 Python、FFmpeg 和 Node.js，并支持集成多种 AI 助手。该工具为创作者提供了高度自动化的管道，节省成本。

### [OpenMontage：开源智能视频制作系统](https://github.com/calesthio/OpenMontage)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-25 01:05:22

OpenMontage 是一个首个开源的智能视频制作系统，用户可以通过简单的语言描述需求，代理会自动处理从调研、脚本、素材生成到编辑与合成的全流程。除了支持基于静态图像制作视频，OpenMontage 还能通过免费开源的工作流生成动态视频，使用免费素材库如 Archive.org 和 NASA。多个实例展示了其功能强大，例如使用 AI 生成图像、旁白和背景音乐制作的视频成本不到 $2。此外，用户可通过参考已有视频来生成类似风格的全新作品。系统支持 Python、Node.js 和多种 AI 助手，配备完善的自检与反馈机制，是快速产出高质量视频的理想工具。

### [Codebase Memory MCP：快速高效的代码智能引擎](https://github.com/DeusData/codebase-memory-mcp)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-25 01:05:22

Codebase Memory MCP 是一款为 AI 编码代理设计的高性能代码智能引擎，可在毫秒级为普通代码库进行全索引。它结合 Tree-Sitter 的 AST 分析和语言服务器协议增强功能，支持 158 种编程语言，对大型代码库如 Linux 内核（2800 万行代码、7.5 万个文件）的索引耗时仅 3 分钟。工具涵盖结构搜索、调用链分析、死码检测和跨服务链接能力，为开发者提供可视化的 3D 知识图谱和多代理支持。无需依赖 Docker 或外部 API，所有处理均在本地完成，兼顾速度与安全性，是开发者的高效代码管理助手。
