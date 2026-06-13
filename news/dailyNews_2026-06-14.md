---
title: "Daily News #2026-06-14"
date: "2026-06-14 00:16:04"
description: "SkillSpector：AI技能的安全扫描工具
LMCache：优化LLM推理性能的KV缓存管理层
/last30days：AI整合平台最新动态搜索工具
PM Skills Marketplace：AI赋能产品管理决策"
tags: 
- "产品管理"
- "安全扫描"
- "LLM优化"
- "技术工具"

---

> - SkillSpector：AI技能的安全扫描工具
> - LMCache：优化LLM推理性能的KV缓存管理层
> - /last30days：AI整合平台最新动态搜索工具
> - PM Skills Marketplace：AI赋能产品管理决策

## 💾 Daily Code

### [SkillSpector：AI技能的安全扫描工具](https://github.com/NVIDIA/SkillSpector)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-14 00:15:24

SkillSpector是一款专注于AI代理技能的安全扫描工具，能够在技能安装前检测漏洞、恶意模式以及安全风险。研究表明，超过26%的AI技能含有漏洞，其中5.2%具有潜在恶意意图。SkillSpector支持多种输入格式（包括Git仓库、URL、压缩文件等），涵盖64种漏洞模式，如提示注入、数据外泄、权限提升等。提供静态分析及可选的LLM语义评估两阶段分析，并支持实时漏洞查询和多种输出格式（JSON、Markdown等）。此外，其风险评分机制为技能分配清晰的严重程度等级，并提供改进建议。SkillSpector为开发者提供了领先的AI安全保障，是检测AI技能漏洞和保障系统安全的不二选择。

### [LMCache：优化LLM推理性能的KV缓存管理层](https://github.com/LMCache/LMCache)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2026-06-14 00:15:24

LMCache是一种用于大规模LLM推理的KV缓存管理层，致力于提升推理的效率和质量。它通过将KV缓存转变为可持久存储和跨多个引擎共享的资源，显著减少时间到第一个结果的延迟（TTFT）并提高吞吐量，特别是在长对话、多轮对话和知识增强的工作负载中表现出色。LMCache支持引擎独立部署，能够与主流的开源推理引擎、硬件供应商及储存系统无缝集成。其关键特性包括持久化的分层KV缓存传输与复用、多样化的存储与传输后端、丰富的缓存观察性指标和可插拔的缓存转换功能。适用于追求高效运行、大规模推理场景的开发者，是构建现代AI推理系统的基础组件。

### [/last30days：AI整合平台最新动态搜索工具](https://github.com/mvanhorn/last30days-skill)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-14 00:15:27

/last30days 是一个由AI代理驱动的搜索工具，综合多个平台的数据，包括 Reddit、X（Twitter）、YouTube、TikTok、GitHub 等，通过用户互动数据（点赞、评论、真实金钱支持）筛选内容，并生成权威简报。它能实时搜索最新动态，整合各平台隔离的数据，实现前所未有的搜索体验，比如了解会议对象的最新活动或全球热点话题。这个工具适合需要快速且全面了解信息的用户，例如分析业务动态、管理销售决策或追踪技术发展。

### [PM Skills Marketplace：AI赋能产品管理决策](https://github.com/phuryn/pm-skills)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2026-06-14 00:15:27

PM Skills Marketplace 提供 68 项 PM 技能和 42 个工作流，通过 AI 助手实现更优的产品决策。这些技能涵盖发现、策略、执行、发布、增长等领域，将经典产品管理框架直接嵌入日常工作流。Marketplace 支持 Claude Code 和 Cowork，同时兼容其他 AI 助手，让用户可流畅使用端到端工作流程。通过插件安装后，它能够自动加载相关技能，同时支持命令链式操作，比如从创意头脑风暴到风险假设优先级排列再到实验设计，帮助团队快速且高效地整理结构化的产品管理流程。
