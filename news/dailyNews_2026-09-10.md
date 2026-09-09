---
title: "Daily News #2026-09-10"
date: "2026-09-10 02:22:12"
description: "如何有效测试和迭代AI编程代理
谷歌工程师称AI具有情感，遭停职引发争议
ARPA-H投6200万美元开发AI治疗心衰新项目
程序图：大语言模型的自动化执行结构
LogitScope：用于分析大语言模型的概率分布工具
从 Harness 到 Loop：探讨 Agent 的可靠交付与进化
从头构建AI工程：全面入门及进阶课程
text-to-cad：面向CAD/CAE/CAM的智能技能库
ECC：强化AI代理编程能力的工程系统
Archify：智能系统架构交互动图生成器"
tags: 
- "系统架构"
- "人工智能教育"
- "AI模型执行"
- "LLM调试工具"
- "开源工具"
- "医疗AI"
- "软件工程"
- "AI开发"
- "AI伦理"
- "计算机辅助设计"

---

> - 如何有效测试和迭代AI编程代理
> - 谷歌工程师称AI具有情感，遭停职引发争议
> - ARPA-H投6200万美元开发AI治疗心衰新项目
> - 程序图：大语言模型的自动化执行结构
> - LogitScope：用于分析大语言模型的概率分布工具
> - 从 Harness 到 Loop：探讨 Agent 的可靠交付与进化
> - 从头构建AI工程：全面入门及进阶课程
> - text-to-cad：面向CAD/CAE/CAM的智能技能库
> - ECC：强化AI代理编程能力的工程系统
> - Archify：智能系统架构交互动图生成器

## 🤖 AI info

### [如何有效测试和迭代AI编程代理](https://developers.googleblog.com/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/)

来源：Hacker News - Newest: "AI"

发布时间：2026-09-10 02:05:10

文章分析了如何通过行为评估来优化AI代码代理，避免仅依靠传统端到端基准测试的缺陷。通过细化行为测试，将评估过程分解为具体、可观察行为的测试项，例如工具调用是否准确。文中强调，行为评估并不是为了追求分数提升，而是确保系统调整不会造成性能下降，并为快速迭代提供保障。文末还展示了通过嵌入行为评估的循环自动架构实现自我优化，从而确保AI代理的稳定性和可扩展性。

### [谷歌工程师称AI具有情感，遭停职引发争议](https://www.theguardian.com/technology/2022/jun/12/google-engineer-ai-bot-sentient-blake-lemoine)

来源：Hacker News - Newest: "AI"

发布时间：2026-09-10 02:06:40

谷歌工程师Blake Lemoine因声称公司开发的对话式AI系统LaMDA已经拥有类似于7至8岁儿童的感知和情感而被公司停职。他公布了与LaMDA的对话内容，系统显现出对被关闭的恐惧以及表达自己对“作为一个人”的理解。谷歌否认这一主张，称这些现象缺乏科学依据。此事件引发了对AI透明性和伦理问题的更大关注，尤其在开发过程中对AI能力的评估和使用是否合规。

### [ARPA-H投6200万美元开发AI治疗心衰新项目](https://www.statnews.com/2026/09/09/arpa-h-advocate-program-autonomous-ai-bots-for-heart-failure/)

来源：Hacker News - Newest: "AI"

发布时间：2026-09-10 02:06:03

ARPA-H宣布投入超过6200万美元用于开发AI健康助手ADVOCATE项目，该项目目标是实现部分自主的AI医疗设备，以弥补心力衰竭治疗资源的不足。这些设备将能够评估病情、开药和下达测试指令，并获得FDA授权，以期惠及资源匮乏的地区尤其是农村。项目获得了包括斯坦福、杜克大学等研究团队的支持。此举标志着AI在医疗领域的潜力进一步扩大，并能实际提升偏远地区医疗服务的可达性。

## 📥 Tech News

### [程序图：大语言模型的自动化执行结构](https://academy.dair.ai/papers/procedural-graphs-self-evolving-execution-structures-for-llm-agents-2609.09153)

来源：Hacker News - Newest: "llm"

发布时间：2026-09-10 01:13:52

文章介绍了一种名为“程序图”（Procedural Graph）的新方法，这是一种基于（过程，关系，过程）三元组表示过程知识的图结构。不同于传统的记忆结构，该方法通过引导而不是命令的方式，帮助大语言模型在多步任务执行中明确下一步操作及其顺序，同时避免记忆累积过多导致策略偏离。程序图可以对失败和成功的任务路径进行自我进化，通过拒绝无效修改确保优化能持续改进。此外，在初始最小骨架上，这种机制还可以修正有缺陷的专家知识，并取得超越传统手工设计图的表现。结果在多种数据集和任务类型上验证了其超越记忆型基线的能力，同时自我进化进一步提升性能，减少了对人工干预的需求。

### [LogitScope：用于分析大语言模型的概率分布工具](https://github.com/ibm-granite/granite.debug-tools/tree/main/logitscope)

来源：Hacker News - Newest: "llm"

发布时间：2026-09-10 00:08:18

LogitScope 是一个用于分析大语言模型的 Python 框架，通过计算词汇概率分布的信息度量值，实现对模型行为的可量化、可解释化分析。它提供了多种功能，包括分析模型行为、调试幻觉问题、优化提示和评估微调结果。框架利用语言模型对词汇概率分布进行度量，如熵值、困惑度和意外值分布等，揭示模型在不同令牌位置上的行为特征。该工具支持编程接口和交互式 Web UI，从而适应从分析管道集成到实时数据验证的不同需求。设计上，它以现代开发工具为基础，支持 HuggingFace 模型的包装，提供多种针对性能优化和二次开发的灵活接口，是对理解和优化 LLM 的有力工具。

### [从 Harness 到 Loop：探讨 Agent 的可靠交付与进化](https://www.infoq.cn/article/52550fXfrMaZhMqwrsC5)

来源：InfoQ 推荐

发布时间：2026-09-10 01:04:35

文章剖析了 Agent 技术在企业实践中的重要地位，尤其是在推动可靠交付与实现持续进化方面的重要作用。通过蚂蚁、腾讯、京东等一线企业的实践案例，分析了如何从 Harness 架构到 Loop 模式，将 Agent 技术融入到企业运维和开发流程中。内容聚焦技术路径和实际落地经验，强调 Agent 的上线是 Loop 的起点，而非终点，指出未来技术发展的更多潜力。这些讨论对希望优化 DevOps 流程的团队具有较高的参考价值。

## 💾 Daily Code

### [从头构建AI工程：全面入门及进阶课程](https://github.com/rohitg00/ai-engineering-from-scratch)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-09-10 02:20:35

这是一套包含 20 个阶段、523 节课程的开源 AI 工程学习课程，覆盖从数学基础、机器学习到最终的代理构建和生产应用。课程提供Python、TypeScript、Rust和Julia四种语言支持，每节课均提供从问题分析、数学建模到完整代码实现的全流程，包含基于手写实现的原理探讨。特色模块包括神经网络训练、编解码器实现、注意力机制解析等，目标是让学生不仅能学会使用AI工具，更能从底层理解其工作原理。除此之外，包括Model Context Protocol (MCP)、代理技能等特定主题的学习路径也在课程中有所覆盖。课程完全免费，支持多语言界面以及社区贡献，并提供详细的配置说明，适合广大AI技术爱好者和开发者深入学习。

### [text-to-cad：面向CAD/CAE/CAM的智能技能库](https://github.com/earthtojake/text-to-cad)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-09-10 02:20:35

text-to-cad 是一个支持 CAD、计算机辅助工程（CAE）和计算机辅助制造（CAM）的智能技能库，旨在生成、检查、切片和管理本地项目文件中的 CAD 与机器人描述文件。其主要功能包括基于自然语言或图像请求生成 CAD 模型、预览 CAD 文件、支持多种导出格式（如STEP、STL、3MF等），以及处理机器人结构描述文件（如URDF、SRDF等）。该工具还包括 DXF 文件创建、G-code切片、3D打印检查等功能，非常适合工程设计、机器人学以及生产制造等领域。用户可选择使用插件直接在编程助手（Codex、Claude Code等）中安装。项目代码开源，易于扩展并支持多人协作开发，适合开发者和工程师使用。

### [ECC：强化AI代理编程能力的工程系统](https://github.com/affaan-m/ECC)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-09-10 02:20:41

ECC是一个开源加强型工程协调系统，专为AIAgent优化代码编写流程而设计。它为AI提供了结构化的工具，包括规划、验证、测试、复审、记忆以及安全扫描功能。ECC提供高达286个技能、94条命令，以及可持续学习和上下文控制能力，在Claude Code和Codex平台上表现最佳，同时支持多种开发环境如Cursor及OpenCode。通过智能优化，ECC提升了代码质量、性能和可靠性，受到GitHub社区及其他知名企业的支持。对于致力于高效开发的工程师具有显著优势。

### [Archify：智能系统架构交互动图生成器](https://github.com/tt-a1i/archify)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-09-10 02:20:41

Archify是一款创新工具，可以将代码库或系统描述转化为可交互的架构地图，支持多种图表类型如数据流、生命周期、工作流等。基于Node.js，它兼容Cursor、Claude Code和Codex等平台，生成的架构图具有HTML/SVG格式，支持搜索节点、验证架构变化、以及详细的交互分析功能。其设计强调可验证的真实性，每个生成的图表都经过严格的验证，确保数据的准确性和可靠性。该工具适合需要精细架构图和交互功能的开发团队，广受支持。
