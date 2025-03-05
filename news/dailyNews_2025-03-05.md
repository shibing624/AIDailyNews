---
title: "Daily News #2025-03-05"
date: "2025-03-05 23:36:25"
description: "从头开始构建LLM（8）：可训练的自注意力机制
为Ray-Ban Meta眼镜构建多模态AI
《刺客信条：影》揭示：16世纪日本的沉浸式冒险
使用LLM模式从非结构化内容中提取结构化数据
在数据中心中提倡QLC SSD的应用
字节跳动回购股票，估值增至3150亿美元
高效图像文本提取工具：Setopic
今日热榜：Apple Music 免费畅听三个月优惠
Commix：命令注入渗透测试工具
MMSegmentation：开源语义分割工具包
ggwave：声音传输的小数据通信库
GenAI Agents：全面的生成AI代理资源库
新数据集Q-EVAL-100K：文本至视觉内容质量与对齐评估
RectifiedHR：高效的训练无关高分辨率图像生成"
tags: 
- "通信"
- "优惠活动"
- "游戏开发"
- "数据存储"
- "开发"
- "安全"
- "数据传输"
- "深度学习"
- "图像生成"
- "计算机视觉"
- "LLM"
- "视觉评估"
- "人工智能"
- "数据提取"
- "AI"
- "OCR"
- "渗透测试"
- "财经"
- "自注意力"

---

> - 从头开始构建LLM（8）：可训练的自注意力机制
> - 为Ray-Ban Meta眼镜构建多模态AI
> - 《刺客信条：影》揭示：16世纪日本的沉浸式冒险
> - 使用LLM模式从非结构化内容中提取结构化数据
> - 在数据中心中提倡QLC SSD的应用
> - 字节跳动回购股票，估值增至3150亿美元
> - 高效图像文本提取工具：Setopic
> - 今日热榜：Apple Music 免费畅听三个月优惠
> - Commix：命令注入渗透测试工具
> - MMSegmentation：开源语义分割工具包
> - ggwave：声音传输的小数据通信库
> - GenAI Agents：全面的生成AI代理资源库
> - 新数据集Q-EVAL-100K：文本至视觉内容质量与对齐评估
> - RectifiedHR：高效的训练无关高分辨率图像生成


## 📥 Tech News

### [从头开始构建LLM（8）：可训练的自注意力机制](https://www.gilesthomas.com/2025/03/llm-from-scratch-8-trainable-self-attention)

来源：Hacker News - Newest: "llm"

发布时间：2025-03-05 09:41:14

本文是作者在探索Sebastian Raschka的《从零开始构建大型语言模型》时的第八篇记录，重点讲解如何实现可训练的自注意力机制。读者将学习如何基于输入序列生成上下文向量，并实现scaled dot product attention机制。作者分享了如何通过矩阵乘法有效计算所有输入的注意力权重，最终生成上下文向量，强调了理论与实践的结合，便于理解自注意力的本质。

### [为Ray-Ban Meta眼镜构建多模态AI](https://engineering.fb.com/2025/03/04/virtual-reality/building-multimodal-ai-for-ray-ban-meta-glasses/)

来源：Engineering at Meta

发布时间：2025-03-05 05:24:18

多模态AI技术能够处理多种输入类型，如语音、文本和图像，正在改变可穿戴设备的用户体验。在Ray-Ban Meta眼镜中，多模态AI支持眼镜对佩戴者视野的识别，使佩戴者可以向眼镜提问并获取相关信息，极大增强了智能交互的能力，推动了可穿戴设备的智能化进程。

### [《刺客信条：影》揭示：16世纪日本的沉浸式冒险](https://developer.apple.com/news/?id=q2zte70j)

来源：Latest News - Apple Developer

发布时间：2025-03-05 01:00:11
![](https://devimages-cdn.apple.com/wwdc-services/articles/images/71FDEFF6-B9F0-44D4-B20B-DD6B6C433BB6/2048.jpeg)
《刺客信条：影》是育碧最新力作，背景设定在16世纪的日本，游戏中引入了非洲起源的武士Yasuke和敏捷的暗影刺客Naoe。游戏支持Mac和iPad，利用Apple的先进技术（如Metal 3和M系列芯片）实现卓越的画面表现。育碧致力于历史准确性，开发团队前往日本实地考察，力求将真实的历史细节融入游戏。该作通过动态的季节、天气变化和精确的光影效果，创造出身临其境的游戏体验，标志着其在技术和创意上的巨大进步。

### [使用LLM模式从非结构化内容中提取结构化数据](https://simonwillison.net/2025/Feb/28/llm-schemas/)

来源：Hacker News - Newest: "llm"

发布时间：2025-03-05 05:56:31

本文讨论了利用大型语言模型（LLM）将非结构化内容转化为结构化数据的潜力，尤其是通过JSON模式进行输出。作者提到，现有的LLM提供商（如OpenAI与Anthropic）正在支持结构化输出功能，将用户输入的示例数据和期望输出关联，尽管性能依赖于模型的选择与实现。文中还展示了通过存储的模式进行高效数据提取的方法，结合SQLite数据库提升数据管理与查询的能力。

### [在数据中心中提倡QLC SSD的应用](https://engineering.fb.com/2025/03/04/data-center-engineering/a-case-for-qlc-ssds-in-the-data-center/)

来源：Engineering at Meta

发布时间：2025-03-05 01:00:26

随着数据量增长和对更高能效的需求，QLC SSD作为一种创新的存储解决方案应运而生。尽管HDD在密度上有所提升，但性能并无改善，而TLC闪存的价格对于扩展来说仍然具有限制。QLC技术在HDD和TLC SSD之间提供了一种中间层，旨在解决这些挑战，提升数据存储的效率和可扩展性。

### [字节跳动回购股票，估值增至3150亿美元](http://www.geekpark.net/news/346572)

来源：极客公园

发布时间：2025-03-05 08:09:45

字节跳动启动面向美国员工的新一轮股票回购，回购价为每股189.90美元，较一年前上涨11%，公司估值达3150亿美元，标志着其从估值下滑中逐步恢复。

### [高效图像文本提取工具：Setopic](https://www.setopic.com)

来源：Hacker News - Newest: "llm"

发布时间：2025-03-05 06:43:52

Setopic是一款在线光学字符识别（OCR）工具，能够从图像中提取各种文本信息，包括表格数据、代码和手写文本。使用流程简单，只需上传图片，稍等片刻即可获得提取结果。该工具支持多种场景，包括财务文档、法律文件和医疗记录，提高了处理文档的效率，非常适合需要快速转录文本的专业人士。

### [今日热榜：Apple Music 免费畅听三个月优惠](https://decohack.com/producthunt-daily-2025-03-05/)

来源：Decohack

发布时间：2025-03-05 15:16:38

本文介绍了2025年3月5日的Product Hunt热榜，重点关注了Apple Music推出的限时优惠活动，用户可以免费畅听3个月。这是一个吸引用户的福利信息，值得关注与利用。

## 💾 Daily Code

### [Commix：命令注入渗透测试工具](https://github.com/commixproject/commix)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2025-03-05 23:18:15

Commix是一个开源的命令注入漏洞检测与利用工具，由Anastasios Stasinopoulos开发，旨在自动化测试命令注入漏洞。用户可在各平台通过克隆或下载包来安装Commix，并需具备Python环境。文档涵盖使用说明与故障排查。

### [MMSegmentation：开源语义分割工具包](https://github.com/open-mmlab/mmsegmentation)

来源：Trending Python repositories on GitHub today · GitHub

发布时间：2025-03-05 23:18:15

MMSegmentation是基于PyTorch的开源语义分割工具箱，提供集成的基准测试与多种语义分割方法的支持。最新版本v1.2.0引入了新的分割算法，增强了功能。项目鼓励用户贡献和反馈，为社区的研究与开发提供灵活和标准化的工具包。

### [ggwave：声音传输的小数据通信库](https://github.com/ggerganov/ggwave)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2025-03-05 23:18:17

ggwave是一个轻量的库，允许通过声音在隔离设备间传输小数据。采用FSK调制协议，传输速度为8-16字节/秒，并使用错误校正码提高可靠性。应用场景包括无服务器广播、IoT设备通信和音频二维码等，支持多种音频后端。

### [GenAI Agents：全面的生成AI代理资源库](https://github.com/NirDiamant/GenAI_Agents)

来源：Trending repositories on GitHub this week · GitHub

发布时间：2025-03-05 23:18:17

GenAI Agents是一个涵盖生成AI代理开发与实施的资源库，提供从基础到高级的教程与实现示例，支持学习与分享。社区驱动式发展，鼓励用户贡献与交流，致力于推动生成AI代理技术的进步。

## 📚 Paper

### [新数据集Q-EVAL-100K：文本至视觉内容质量与对齐评估](https://arxiv.org/abs/2503.02357)

来源：Huggingface Daily Papers

发布时间：2025-03-05 14:09:41

本研究介绍了Q-EVAL-100K数据集，旨在评估文本至视觉内容的视觉质量和对齐水平，提供96万个人工标注的意见分数。引入的Q-Eval-Score模型在视觉质量和对齐评估中取得了优越性能，可处理长文本提示的对齐问题，展示了该数据集的重大价值，数据与代码将公开。

### [RectifiedHR：高效的训练无关高分辨率图像生成](https://arxiv.org/abs/2503.02537)

来源：Huggingface Daily Papers

发布时间：2025-03-05 13:53:05

本文提出了RectifiedHR，一种高效且简单的解决方案，用于实现训练无关的高分辨率图像生成。通过引入噪声刷新策略和能量矫正策略，有效解决训练过程中高分辨率图像生成的模糊问题。与多种基线方法进行比较，结果显示RectifiedHR在效率和效果上均超越前者，简单易实现。
