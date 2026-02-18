---
title: "Daily News #2026-02-18"
date: "2026-02-18 23:54:16"
description: "为AI代理提供权限控制层的AgentPriv
AI系统的飞行记录器：AIR Blackbox Gateway
AI版图重塑：阿里字节双雄争霸
从烹饪看AI：便利与真实的对比
LLM辅助开发：构建Node.js原生模块的经历
AI 助手的灵魂思考：灵魂不是贴上去的标签
探索MineBench：AI风格体素构建的基准测试
Keychains.dev：安全的AI代理凭证管理解决方案
奥地利开发者的灵魂重拾：从倦怠到AI 助手
免费LogoAPI助您轻松获取公司标志
Heretic: 解除语言模型的自动化审查工具
Heretic：自动消除语言模型审查工具
Hummingbot：民主化高频交易开放框架
Claude Skills：简化复杂任务的技能集"
tags: 
- "AI工具"
- "安全"
- "编程"
- "人工智能"
- "创业者心路"
- "AI安全"
- "AI"
- "开发工具"
- "AI助手"
- "语言模型"
- "AI趋势"
- "技术"
- "金融科技"
- "服务"

---

> - 为AI代理提供权限控制层的AgentPriv
> - AI系统的飞行记录器：AIR Blackbox Gateway
> - AI版图重塑：阿里字节双雄争霸
> - 从烹饪看AI：便利与真实的对比
> - LLM辅助开发：构建Node.js原生模块的经历
> - AI 助手的灵魂思考：灵魂不是贴上去的标签
> - 探索MineBench：AI风格体素构建的基准测试
> - Keychains.dev：安全的AI代理凭证管理解决方案
> - 奥地利开发者的灵魂重拾：从倦怠到AI 助手
> - 免费LogoAPI助您轻松获取公司标志
> - Heretic: 解除语言模型的自动化审查工具
> - Heretic：自动消除语言模型审查工具
> - Hummingbot：民主化高频交易开放框架
> - Claude Skills：简化复杂任务的技能集

## 🤖 AI info

### [为AI代理提供权限控制层的AgentPriv](https://github.com/nichkej/agentpriv)

来源：Hacker News - Newest: "AI"

发布时间：2026-02-18 23:37:13

AgentPriv是一个为AI代理添加权限控制层的软件，允许用户在AI代理自主运行工具之前进行权限授予控制。它提供了三种模式：允许、拒绝和询问，用户可以根据需要选择运行或拒绝程序调用。默认为终端中的'询问'模式，可以通过自定义提示更改审批逻辑。在使用框架时，默认拒绝会引发AgentPrivDenied错误，用户可以配置on_deny参数将该结果返回，以免程序崩溃。该工具兼容多个框架，是确保AI调用安全性和可控度的重要工具。

### [AI系统的飞行记录器：AIR Blackbox Gateway](https://github.com/nostalgicskinco/air-blackbox-gateway)

来源：Hacker News - Newest: "AI"

发布时间：2026-02-18 23:15:31

AIR Blackbox Gateway是一个为AI系统设计的飞行记录器，兼容各种OpenAI提供商，记录并生成每次LLM调用的可审计记录。与其他监控工具不同，AIR旨在提供账户证明而非仅是表现分析。其包含15个仓库，每个仓库都有一套完整的CI/CD测试。用户可以控制数据记录，确保隐私与数据边界。通过创建可验证的记录，AIR提升了系统透明度和可信度，为未来自动化系统的安全操作奠定基础。

### [AI版图重塑：阿里字节双雄争霸](https://www.36kr.com/p/3687203636409097)

来源：36氪 - 最新资讯频道

发布时间：2026-02-18 16:50:56

2026年，中国的AI格局因阿里和字节的竞争而焕然一新。阿里的千问平台通过集成购物场景实现了用户行为路径的强化，营造出AI的生态整合战，而字节的豆包则通过催发创意工具助力个体创作，实现生产门槛的降低。阿里侧重生活方式，千问通过AI在日常消费场景中发挥作用，形成高频和刚需使用习惯，而字节则侧重于生产工具，通过Seedance 2.0等产品推动创意的平民化。两家公司的策略分别反映了对AI融入生活和增强创作力的不同视野，形成了中国AI发展的双雄格局。

### [从烹饪看AI：便利与真实的对比](https://nik.art/what-cooking-tells-us-about-ai/)

来源：Hacker News - Newest: "AI"

发布时间：2026-02-18 23:29:23

文章类比烹饪和AI的发展历程，探讨现代社会对方便食品的依赖与对于烹饪的热情。尽管速食行业发达，但人们对于烹饪的热情依然高涨，这种情形与AI快速发展的现象类似。当准备好的AI工具使工作变得简单，它们反而进一步增加了对真实经验和深度专业知识的需求。这种需求将驱动不断发展的AI工具行业，同时也保持专业人士的关键作用。最终，文章指出只有当人们失去对某项活动的兴趣时，它才会真正过时。

## 📥 Tech News

### [LLM辅助开发：构建Node.js原生模块的经历](https://thomashunter.name/posts/2026-02-17-generating-a-node-native-module-with-an-llm)

来源：Hacker News - Newest: "llm"

发布时间：2026-02-18 22:53:43

作者分享了使用LLM辅助开发Node.js原生模块的经验。项目旨在创建一个用于EXIF数据读写的库，利用C++编写的模块及JavaScript绑定。作者在没有深入研究的前提下，完全依赖LLM生成代码并满足需求。在项目过程中，遇到了阻塞问题并通过LLM解决，最终构建了一个功能完整的库。作者讨论了LLM生成代码的知识产权及维护问题，并对项目的潜在应用进行了思考。

### [AI 助手的灵魂思考：灵魂不是贴上去的标签](https://www.infoq.cn/article/7QieJxH5gpNRvL5hKcrG)

来源：InfoQ 推荐

发布时间：2026-02-18 20:50:18

本文探讨OpenClaw项目的灵魂定义，提出AI助手不应作为工具而是可以成长的“个体”。作者详细解读SOUL.md文件，定义了一种全新的人与AI关系范式，强调助手需具备真诚、有个性与主动性的三原则。作者将AI定位为人的伙伴，并强调AI需要赢得信任。AI助手在与人类互动中共同成长，而非单方面设定标签。灵魂定义在技术与人文之间架起桥梁，反映开发者希望AI助手能超越工具角色，变为富有个性的存在。

### [探索MineBench：AI风格体素构建的基准测试](https://minebench.ai)

来源：Hacker News - Newest: "llm"

发布时间：2026-02-18 23:45:08

MineBench是针对Minecraft风格体素构建的AI和LLM基准测试，要求模型生成原始JSON坐标，无需图像或3D工具。用户可在Sandbox中输入任意提示以生成3D构建。该平台旨在可视化模型的纯代码输出，以衡量AI在结构建模中的能力。文章展示了MineBench如何在空间智能测试中发挥作用，并强调了其在AI应用中的重要性及创新性。

### [Keychains.dev：安全的AI代理凭证管理解决方案](https://keychains.dev/)

来源：Hacker News - Newest: "llm"

发布时间：2026-02-18 21:59:29

Keychains.dev提供了一种安全的方式，让AI代理访问任何API，同时不泄露敏感信息。用户可以设定权限，确保凭证使用透明并可撤销。其创新的凭证管理系统在使用时保护而不仅仅是静态保存，提供完整的身份认证机制，使代理从不接触实际的密钥。Keychains利用SSH密钥进行机器认证，并通过用户授权和多代理委派确保数据安全，是现代AI数据交互的新标准。

### [奥地利开发者的灵魂重拾：从倦怠到AI 助手](https://www.infoq.cn/article/e0gyUzRvzU263FTBePdw)

来源：InfoQ 推荐

发布时间：2026-02-18 20:44:39

Peter Steinberger，一个成功的创业开发者，在卖掉PSPDFKit后经历了深刻的身份认同危机。这段文字详细解析了Peter如何在离开创业的深渊中重新找到生活的火花，并在AI中重拾激情。Peter以开放心态看待AI对编程的改变，认为自然语言变成新的编程语言，并强调上下文的重要性。文章不仅描述了从技术角度的转变，也从人文角度探讨个人成长和身份认同对职业选择的影响，成为技术与生活对话的深刻思考。

### [免费LogoAPI助您轻松获取公司标志](https://decohack.com/producthunt-daily-2026-02-18/)

来源：Decohack

发布时间：2026-02-18 15:50:24

这篇文章介绍了一个名为Hunter的logo API服务，可以免费且无需注册就获取任意公司的标志。用户只需输入网址，即可通过这个API找到相关标志。这个服务对于需要获取公司标志的用户来说非常方便快捷。此外，文章提到AI零基础建站指南和Cursor零基础教程的限时优惠推荐。整体来看，文章提供的信息对那些需要标志和教程的人有实际帮助，但属于常规推荐内容。

## 💾 Daily Code

### [Heretic: 解除语言模型的自动化审查工具](https://github.com/p-e-w/heretic)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-02-18 23:52:25

Heretic 是一种工具，旨在无需昂贵的后期训练便可去除基于 Transformer 的语言模型中的审查机制。采用方向性消融（Abliteration）技术和 TPE 参数优化器，Heretic 能自动优化消融参数，使去审查后的模型最大限度地保留原模型的智能性。它支持大多数致密模型，并已被广泛用户接受。该工具的主要创新包括灵活的消融权重等，允许用户在命令行运行，无需对 Transformer 内部结构有深入了解。

### [Heretic：自动消除语言模型审查工具](https://github.com/p-e-w/heretic)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-02-18 23:52:28

Heretic 是一个可以自动移除变换器语言模型中审查（“安全对齐”）的工具，无需昂贵的后训练。它结合了驱动 Optuna 的 TPE 参数优化器，通过共同最小化拒绝次数和与原始模型的 KL 散度来找到最优的 abliteration 参数。这使经过去审查的模型能最大程度保留原始模型的智能。Heretic 支持大部分密集模型及多种 MoE 架构，默认配置下无需配置即可运行，用户可以根据需要调整多种参数选项。

### [Hummingbot：民主化高频交易开放框架](https://github.com/hummingbot/hummingbot)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-02-18 23:52:25

Hummingbot 是一个开源框架，帮助设计和部署自动交易策略或机器人，适用于许多中心化和去中心化交易所。用户在过去一年内通过 Hummingbot 完成了超过 340 亿美元的交易量。Hummingbot 提供包括 Docker 安装指导、Exchange 连接器标准化接口等功能，致力于通过社区共享知识和代码库，推动高频交易的民主化。用户可以通过 Discord 社区寻求技术支持，并有多种策略可供选择。

### [Claude Skills：简化复杂任务的技能集](https://github.com/Jeffallan/claude-skills)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-02-18 23:52:28

Claude Skills 提供了 66 种专门技能，涵盖语言、框架、基础设施、安全等多领域，并提供 9 项工作流管理命令以支持从项目发现到回顾的全过程管理。其上下文感知激活功能使技能自动启动，能组合多技能完成复杂任务。用户可通过详细文档来了解各技能和工作流命令的用法，并可进行本地开发或向社区贡献代码。
