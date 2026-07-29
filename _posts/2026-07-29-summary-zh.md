---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
content_date: 2026-07-28
lang: zh
---

> 报道范围：2026-07-28（Asia/Shanghai 自然日）

> 从 60 条内容中筛选出 8 条重要资讯。

---

1. [ggml-org/llama.cpp released b10164](#item-1) ⭐️ 10.0/10
2. [llama.cpp 发布版 b10158 添加 Eagle3-v3 支持](#item-2) ⭐️ 10.0/10
3. [Moonshot 发布 2.8 万亿参数 Kimi K3 模型权重](#item-3) ⭐️ 10.0/10
4. [Kimi K3 Architecture Overview and Notes](#item-4) ⭐️ 9.0/10
5. [关于使用哪些 AI 来完成任务的实用指南](#item-5) ⭐️ 9.0/10
6. [长鑫科技正式登陆科创板！首日市值登顶 A 股 背后中国科技产业天团陪跑 - 东方财富](#item-6) ⭐️ 9.0/10
7. [用于软件开发的 GitHub Copilot 工作流](#item-7) ⭐️ 8.0/10
8. [NeurIPS 2026 AI 生成评审争议](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10164](https://github.com/ggml-org/llama.cpp/releases/tag/b10164) ⭐️ 10.0/10

llama.cpp release b10164 adds CUDA optimizations for Mamba-2 prefill acceleration and fixes race conditions.

github · github-actions\[bot\] · 7月28日 22:28

**标签**: `#llama.cpp`, `#CUDA`, `#Mamba-2`, `#AI acceleration`, `#GPU optimization`

---

<a id="item-2"></a>
## [llama.cpp 发布版 b10158 添加 Eagle3-v3 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10158) ⭐️ 10.0/10

llama.cpp 版本 b10158 引入了 gpt-oss 模型家族中 Eagle3-v3 模型架构的支持，并为 macOS、iOS 和 Linux 提供了新的预编译二进制文件。 此次发布扩展了广泛使用的 llama.cpp 项目的功能，使用户能够在本地运行一种新的最先进模型，并显著扩大了不同操作系统上高级 AI 模型的可及性。 该发布包含一个具体说明，即启用了 KleidiAI 的 macOS Apple Silicon 构建已被禁用，同时提供了广泛的平台特定二进制文件，包括支持 CUDA 12 和 13 的 Windows 版本。

github · github-actions\[bot\] · 7月28日 16:54

**背景**: llama.cpp 是一个高性能的开源库，旨在在各种硬件（包括 CPU、GPU 和专用加速器）上本地运行大型语言模型。Eagle3-v3 是一种新的模型架构，而 gpt-oss 指的是 OpenAI 的开源权重模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/gpt-oss">GitHub - openai/ gpt - oss : gpt - oss -120b and gpt - oss -20b are two...</a></li>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/ kleidiai : This repository is a read-only mirror of...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#open-source`, `#local-ai`, `#eagle3-v3`, `#macos`

---

<a id="item-3"></a>
## [Moonshot 发布 2.8 万亿参数 Kimi K3 模型权重](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 10.0/10

Moonshot AI 已发布其 2.8 万亿参数的 Kimi K3 模型权重，可在 Hugging Face 上以 1.56TB 的下载量获取。 此次发布意义重大，因为它代表了大规模模型可用性的重大进步，为开发者和研究人员提供了一个强大的开放权重替代方案。 K3 许可证与其前身不同，要求为从 Model as a Service 运营中产生超过 2000 万美元年收入的业务与 Moonshot 签订单独协议。

rss · Simon Willison · 7月28日 07:39

**背景**: Moonshot AI 之前为其 K2 模型引入了一种修改后的 MIT 许可证，要求对大型商业实体进行署名。K3 许可证通过为高收入的 Model as a Service 业务强制要求单独的商业协议，进一步收紧了这些限制。

**标签**: `#AI`, `#OpenSource`, `#LLM`, `#Licensing`, `#Moonshot`

---

<a id="item-4"></a>
## [Kimi K3 Architecture Overview and Notes](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) ⭐️ 9.0/10

A detailed technical overview of the Kimi K3 architecture with community discussions on reproducibility and efficiency.

hackernews · ModelForge · 7月28日 23:48 · [社区讨论](https://news.ycombinator.com/item?id=49085698)

**标签**: `#AI architecture`, `#machine learning`, `#model efficiency`, `#technical documentation`, `#reproducibility`

---

<a id="item-5"></a>
## [关于使用哪些 AI 来完成任务的实用指南](https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything) ⭐️ 9.0/10

Ethan Mollick 更新了他的指南，以反映当前的 AI 情况，强调智能体系统而非简单的聊天界面。 这份指南通过提供关于为特定任务选择正确工具的实用建议，帮助用户在快速发展的 AI 生态系统中导航。 该指南指出，由于在 Codex/ChatGPT Work/Cowork 类别中没有强有力的产品，Google 的 Gemini 已被从列表中移除。

rss · Simon Willison · 7月28日 05:55

**背景**: 智能体系统是可以自主执行复杂任务的 AI 工具，代表了从传统基于聊天的 AI 模型的重要转变。

**标签**: `#AI`, `#agentic systems`, `#software tools`, `#AI models`, `#practical guide`

---

<a id="item-6"></a>
## [长鑫科技正式登陆科创板！首日市值登顶 A 股 背后中国科技产业天团陪跑 - 东方财富](https://news.google.com/rss/articles/CBMiYEFVX3lxTE9KSjNYNGpxOEpQUmt6Si1QSExVZGVsQ29IUnhhT1RkWWJuTkVrUFlfRkUwM1lPZDloNW92UHgwck40dVk3YjhHR3RqSk91ZDhqeDI5UmZtZjBJWWEzNER5LQ?oc=5) ⭐️ 9.0/10

CXMT&\#x27;s successful IPO and market debut highlight China&\#x27;s semiconductor industry growth.

google\_news · 东方财富 · 7月28日 14:51

**标签**: `#semiconductors`, `#AI`, `#IPO`, `#China`, `#DRAM`

---

<a id="item-7"></a>
## [用于软件开发的 GitHub Copilot 工作流](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/) ⭐️ 8.0/10

GitHub 博客介绍了一种实用的 GitHub Copilot 工作流，用于软件开发生命周期的各个阶段，包括原型设计、规划、实现和代码审查。 该工作流帮助开发人员简化 AI 辅助编码流程，减少在不同 AI 工具之间频繁切换的需求，并提高整体生产力。 该工作流强调在所有开发阶段使用 GitHub Copilot 作为一致的工具，而不是追逐每一个出现的新 AI 工具。

rss · GitHub Blog · 7月28日 02:00

**背景**: GitHub Copilot 是一个基于上下文建议代码片段和完整函数的 AI 驱动代码补全工具。它集成在 Visual Studio Code 等流行的 IDE 中，广泛用于加速开发任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.github.com/gh-aw/">Home | GitHub Agentic Workflows</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-cli/automate-copilot-cli/automate-with-actions">Automating tasks with Copilot CLI and GitHub Actions - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#Software Development`, `#AI Tools`, `#Workflow`, `#Prototyping`

---

<a id="item-8"></a>
## [NeurIPS 2026 AI 生成评审争议](https://www.reddit.com/r/MachineLearning/comments/1v8vuae/neurips_2026_aigenerated_reviews_d/) ⭐️ 8.0/10

一位 Reddit 用户质疑 NeurIPS 2026 使用 AI 生成评审的做法，认为部分评审员可能直接复制了 LLM 的输出而未进行适当审查。 这一讨论凸显了对顶级 AI 会议同行评审过程完整性的担忧，以及 LLM 在学术评估中可能被滥用的风险。 作者指出元评审员似乎也广泛使用了 LLM，这引发了关于问责制和使用 AI 进行评审后果的疑问。

reddit · r/MachineLearning · /u/bricklerex · 7月28日 19:34

**背景**: NeurIPS（神经信息处理系统）是机器学习研究的顶级会议，论文在此经过严格的同行评审流程以筛选出被接受的论文。

**社区讨论**: Reddit 帖子反映了研究人员对 AI 辅助评审的透明度和公平性的困惑与担忧，有人呼吁加强监督。

**标签**: `#AI`, `#NeurIPS`, `#Review Process`, `#LLM`, `#Machine Learning`

---