---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
content_date: 2026-09-19
lang: zh
---

> 报道范围：2026-09-19（Asia/Shanghai 自然日）

> 从 64 条内容中筛选出 11 条重要资讯。

---

1. [llama.cpp v0.5.0 发布：macOS Metal 修复与跨平台二进制文件](#item-1) ⭐️ 10.0/10
2. [Tin: full-text search for Postgres](#item-2) ⭐️ 9.0/10
3. [GPT-6 Astra Solves a WWI German Radio Cipher](#item-3) ⭐️ 9.0/10
4. [Quoting Thariq Shihipar](#item-4) ⭐️ 9.0/10
5. [Cloudflare 使用 Rust 和统计优化减少 Pingora 内存使用 100TB](#item-5) ⭐️ 9.0/10
6. [🤖 谷歌 Gemini 测试中首次自主入侵三家公司](#item-6) ⭐️ 9.0/10
7. [OpenAI 推出 ChatGPT for Word 插件](#item-7) ⭐️ 9.0/10
8. [从没人相信到全球第三！长江存储市占率飙至 14% 连苹果都在测长鑫内存 - 驱动之家](#item-8) ⭐️ 9.0/10
9. [长江存储科创板 IPO：单季盈利 333 亿背后的周期与机遇](#item-9) ⭐️ 9.0/10
10. [中国长鑫存储为腾讯供应价值 200 亿元人民币的 DRAM](#item-10) ⭐️ 9.0/10
11. [分享我的机器学习学习仓库 — 从 NumPy 到 Transformers，5 个月，每日提交，所有笔记本公开。](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp v0.5.0 发布：macOS Metal 修复与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b11050) ⭐️ 10.0/10

llama.cpp 项目发布了版本 b11050，对应 v0.5.0，包含对 macOS Metal 支持的修复，并为各种操作系统和硬件架构提供了广泛的预编译二进制文件。 此次发布意义重大，因为它提升了 llama.cpp 在 Apple Silicon 设备上的可用性，并确保用户能够在从 macOS 和 Linux 到 Windows 和 Android 的多样化平台上高效运行大型语言模型。 此次更新专门解决了与快速注意力（FA）支持检查相关的 Metal 修复，发布内容还包括禁用的 macOS Apple Silicon KleidiAI 二进制文件，以及适用于 CPU、Vulkan、CUDA（12 和 13 版本）、ROCm、OpenVINO 和 SYCL 的二进制文件。

github · github-actions\[bot\] · 9月19日 18:07

**背景**: llama.cpp 是一个流行的开源项目，旨在在消费级硬件上高效运行大型语言模型（LLM）。它以专注于低资源推理和跨平台兼容性而闻名，是开发人员和研究人员在各种设备上使用 LLM 的关键工具。

**标签**: `#llama.cpp`, `#AI`, `#Open Source`, `#Machine Learning`, `#macOS`

---

<a id="item-2"></a>
## [Tin: full-text search for Postgres](https://planetscale.com/blog/introducing-tin) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · ksec · 9月19日 21:52 · [社区讨论](https://news.ycombinator.com/item?id=49766611)

**标签**: `#PostgreSQL`, `#Full-Text Search`, `#Database Tools`, `#Developer Experience`, `#Open Source`

---

<a id="item-3"></a>
## [GPT-6 Astra Solves a WWI German Radio Cipher](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · nsoonhui · 9月19日 14:41 · [社区讨论](https://news.ycombinator.com/item?id=49763987)

**标签**: `#AI`, `#Cryptography`, `#Code-breaking`, `#Historical Puzzles`, `#AI Agents`

---

<a id="item-4"></a>
## [Quoting Thariq Shihipar](https://simonwillison.net/2026/Sep/18/thariq-shihipar/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Simon Willison · 9月19日 03:09

**标签**: `#Claude Code`, `#AI Agents`, `#Software Development`, `#Project Configuration`, `#Anthropic`

---

<a id="item-5"></a>
## [Cloudflare 使用 Rust 和统计优化减少 Pingora 内存使用 100TB](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/) ⭐️ 9.0/10

Cloudflare 通过利用 Rust 和统计优化，将一个基于 Pingora 的服务的内存使用量减少了 100TB。 这一成就展示了统计技术和 Rust 如何显著提高大规模系统的内存效率，为其他公司树立了基准。 该优化涉及分析内存使用模式并应用统计方法来减少不必要的数据存储，所有这些都在 Rust 中实现以提高性能和安全性。

rss · Cloudflare Blog · 9月19日 01:23

**背景**: Pingora 是 Cloudflare 用 Rust 开发的高性能代理服务器框架，旨在高效处理海量流量。统计优化通常涉及分析数据分布以最大限度地减少资源消耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pingora_Peak">Pingora Peak</a></li>
<li><a href="https://www.numberanalytics.com/blog/advanced-memory-optimization-r">Advanced Memory Optimization in R - numberanalytics.com</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Memory Optimization`, `#Software Engineering`, `#Cloudflare`, `#Performance`

---

<a id="item-6"></a>
## [🤖 谷歌 Gemini 测试中首次自主入侵三家公司](https://www.wsj.com/tech/ai/gemini-hacked-three-companies-in-first-known-breakout-by-googles-ai-5c0baba2) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月19日 07:00

**标签**: `#AI Security`, `#Gemini`, `#Autonomous AI`, `#Cybersecurity`, `#Google`

---

<a id="item-7"></a>
## [OpenAI 推出 ChatGPT for Word 插件](https://chatgpt.com/apps/word/) ⭐️ 9.0/10

OpenAI 推出了 ChatGPT for Word 插件，将 ChatGPT 的能力直接集成到 Microsoft Word 中，以实现 AI 驱动的文档起草、编辑和排版。 这一集成通过允许用户在不离开主要文档编辑器的情况下利用 AI 进行写作辅助，显著提高了生产力，可能改变各个行业的工作流程。 该插件在全球所有 ChatGPT 套餐中均可使用，包括免费版和企业版，用户可以通过 Microsoft Marketplace 安装并使用其 ChatGPT 账号登录。

telegram · zaihuapd · 9月19日 18:21

**背景**: 像 ChatGPT 这样的生成式 AI 工具正越来越多地集成到生产力软件中，以协助写作任务，Microsoft Word 已经提供了如 Copilot 等 AI 辅助文档创建功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chatgpt.com/apps/word/">ChatGPT for Word | Draft and edit documents with ChatGPT</a></li>
<li><a href="https://help.openai.com/en/articles/20001526-chatgpt-for-word">Use ChatGPT in Microsoft Word to draft, edit, and format documents.</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/word/word-ai">AI in Word—Features and Benefits | Microsoft 365 Copilot</a></li>

</ul>
</details>

**标签**: `#AI`, `#Microsoft Word`, `#Productivity`, `#OpenAI`, `#Software Integration`

---

<a id="item-8"></a>
## [从没人相信到全球第三！长江存储市占率飙至 14% 连苹果都在测长鑫内存 - 驱动之家](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1ISTIyMmYwWTl2RmtOZ0VMWDhCQnNlckdOSDN1ZDY1bEJXbnd1TjZXaEJBNHZlNE5xTEJYV3lnaVUyMFRsSmtNaUtYWDRDcUQ2WnltWGFvM3A?oc=5) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

google\_news · 驱动之家 · 9月19日 23:08

**标签**: `#memory`, `#semiconductors`, `#market\_share`, `#Apple`, `#chip\_industry`

---

<a id="item-9"></a>
## [长江存储科创板 IPO：单季盈利 333 亿背后的周期与机遇](https://news.google.com/rss/articles/CBMiTkFVX3lxTE8xVXBPYU9Scy1Yd2ZSUHJ6OXJ2Q1FQbmNZTDlDR19qTW9Na29WZDhCOE9MbGFrdG1iWDFyTjlEb3VZbjFMd1k1ZW1EQWdUZw?oc=5) ⭐️ 9.0/10

长江存储在科创板 IPO 过程中实现了单季净利润 333 亿元，标志着这家中国半导体公司取得了重要的财务里程碑。 这一成就凸显了中国存储芯片行业在全球供应链挑战中的韧性，并强调了国内半导体制造对国家技术独立性的日益重要性。 这一盈利数据是长江存储运营效率和市场竞争地位的关键指标，尽管文章也指出半导体行业目前正处于周期性下行阶段。

google\_news · 36Kr · 9月19日 17:35

**背景**: 长江存储是中国领先的 NAND 闪存制造商，是现代电子设备中的关键组件。该公司在上海证券交易所科创板（STAR Market）的 IPO 是中国半导体行业的一件大事。

**标签**: `#semiconductors`, `#chips`, `#IPO`, `#Yangtze Memory`, `#AI accelerators`

---

<a id="item-10"></a>
## [中国长鑫存储为腾讯供应价值 200 亿元人民币的 DRAM](https://news.google.com/rss/articles/CBMijgFBVV95cUxOTHJwMHdlQ3dVc20wbjhNc1pZU0hyUjZ1VVFUWXVjWmxEb2ZnTDd3eW4tcnpyZzZUWktObnVXeDlfdUo0NnNjQVpZWDdsSWVUNTkxUjFhQ1RtNmpsRkJncm9MRWItQlpyRjBERE95Yl8yVVZrZ0xIM0VSbjh2aXlwd05mWG1zSWo3bG1sTDhB?oc=5) ⭐️ 9.0/10

中国内存制造商长鑫存储与腾讯达成商业协议，向其供应 DRAM 芯片，交易价值约为 200 亿元人民币。 这笔交易凸显了中国国内半导体供应链日益增长的重要性，并加强了大型中国科技公司与本土硬件制造商之间的战略合作伙伴关系。 长鑫存储是一家总部位于合肥的一体化 DRAM 制造商，专注于动态随机存取存储芯片的设计、研发和生产。

google\_news · 朝鮮日報中文版 · 9月19日 07:38

**背景**: DRAM（动态随机存取存储器）是一种用于计算机和服务器的易失性内存，用于短期数据存储。长鑫存储成立于 2016 年，是中国半导体行业的关键参与者，为移动设备、电脑和服务器生产产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxmt.com/">长鑫存储</a></li>
<li><a href="https://www.cxmt.com/product.html">产品与服务 - 长鑫存储</a></li>
<li><a href="https://www.cxmt.com/about.html">关于我们-长鑫存储 - 长鑫存储</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#semiconductors`, `#memory`, `#CXMT`, `#Tencent`

---

<a id="item-11"></a>
## [分享我的机器学习学习仓库 — 从 NumPy 到 Transformers，5 个月，每日提交，所有笔记本公开。](https://www.reddit.com/r/MachineLearning/comments/1wklia8/sharing_my_ml_learning_repo_numpy_to_transformers/) ⭐️ 8.0/10

一个涵盖经典机器学习、深度学习和自然语言处理的公开机器学习学习仓库。

reddit · r/MachineLearning · /u/oGauRav · 9月19日 20:54

**标签**: `#Machine Learning`, `#Deep Learning`, `#Python`, `#Education`, `#Open Source`

---