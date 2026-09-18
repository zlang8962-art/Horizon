---
layout: default
title: "Horizon Summary: 2026-09-18 (ZH)"
date: 2026-09-18
content_date: 2026-09-17
lang: zh
---

> 报道范围：2026-09-17（Asia/Shanghai 自然日）

> 从 79 条内容中筛选出 12 条重要资讯。

---

1. [ggml-org/llama.cpp released b11026](#item-1) ⭐️ 10.0/10
2. [llama.cpp b11019 修复了关键的 GGUF 解析错误并添加了 LoRA 加载功能](#item-2) ⭐️ 10.0/10
3. [Rust-lang 警告针对知名 Rust 开发者的定向攻击](#item-3) ⭐️ 10.0/10
4. [美光称其展示全球首款 512 GB DDR5 模组，2027 年具备量产条件](#item-4) ⭐️ 10.0/10
5. [GitLab.com 的速率限制正在发生变化](#item-5) ⭐️ 9.0/10
6. [datasette 1.0a40](#item-6) ⭐️ 9.0/10
7. [datasette 0.65.5](#item-7) ⭐️ 9.0/10
8. [将 GitHub Copilot 运行时迁移至 Rust](#item-8) ⭐️ 9.0/10
9. [GoBench：在围棋游戏中评估大语言模型 \[R\]](#item-9) ⭐️ 9.0/10
10. [长鑫科技的临界点时刻 - 36 Kr](#item-10) ⭐️ 9.0/10
11. [中国存储芯片市场：长鑫科技一家独大与现金流压力](#item-11) ⭐️ 8.0/10
12. [PC 厂商争夺长鑫存储 DRAM 供应，订单排至 2027 年末](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11026](https://github.com/ggml-org/llama.cpp/releases/tag/b11026) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月17日 21:31

**标签**: `#llama.cpp`, `#open-source`, `#AI`, `#inference`, `#optimization`

---

<a id="item-2"></a>
## [llama.cpp b11019 修复了关键的 GGUF 解析错误并添加了 LoRA 加载功能](https://github.com/ggml-org/llama.cpp/releases/tag/b11019) ⭐️ 10.0/10

llama.cpp 的 b11019 版本修复了一个关键的 GGUF 文件解析错误，该错误导致数据部分从文件偏移量 0 开始错误填充，从而导致嵌入的 GGUF 文件加载时返回错误的张量数据。它还引入了用于加载 LoRA 适配器的新函数，并在嵌入的数据部分未对齐时禁用内存映射并发出警告。 此修复对于在本地运行大型语言模型的用户至关重要，因为错误的张量数据会严重降低模型性能或导致崩溃。LoRA 加载功能的添加扩展了该库在微调和适配模型方面的实用性，这是 AI 模型定制中的一个关键趋势。 该错误修复涉及精确的内存对齐逻辑，确保数据部分相对于 GGUF 起始位置而不是文件进行对齐。该版本包含针对多个平台和硬件后端（如 CUDA、ROCm 和 Vulkan）的二进制文件，并由包括 Johannes Gäßler 和 Claude Opus 5 在内的多位贡献者共同完成。

github · github-actions\[bot\] · 9月17日 18:35

**背景**: GGUF（GGML 通用文件）是一种由 llama.cpp 于 2023 年 8 月引入的二进制文件格式，用于高效存储模型张量和元数据。它专为模型数据的快速保存和加载而设计，并得到 Hugging Face 等工具的广泛支持。LoRA（低秩适应）是一种用于使用较小的参数更新来微调大型模型的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/ggml/blob/master/docs/gguf.md">ggml/docs/gguf.md at master · ggml-org/ggml</a></li>
<li><a href="https://huggingface.co/docs/hub/en/gguf">GGUF · Hugging Face</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#GGUF`, `#AI inference`, `#open-source`, `#bugfix`

---

<a id="item-3"></a>
## [Rust-lang 警告针对知名 Rust 开发者的定向攻击](https://blog.rust-lang.org/2026/09/17/targeted-attacks/) ⭐️ 10.0/10

Rust-lang 识别出正在进行的针对 Rust 社区成员和流行 crates 所有者的行动，旨在入侵设备并分发恶意软件。 此次攻击凸显了对 Rust 生态系统的日益增长的威胁，因为攻击者利用社会工程学手段入侵关键基础设施和供应链。 攻击者利用视频通话诱骗目标安装恶意软件，通常伪装成具有 LinkedIn 存在感的合法公司资料。

rss · Rust Blog · 9月17日 08:00

**背景**: 社会工程学攻击通过操纵个人泄露机密信息或执行有利于攻击者的操作。国家行为体（如朝鲜）已被知悉使用这些战术入侵系统并窃取数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Social_engineering_%28security%29">Social engineering (security) - Wikipedia</a></li>
<li><a href="https://www.chaincatcher.com/en/article/2172145">Slow Fog: Social engineering attacks using malicious video call links are active again, users need to be vigilant</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#social-engineering`, `#malware`, `#rust-lang`, `#targeted-attacks`

---

<a id="item-4"></a>
## [美光称其展示全球首款 512 GB DDR5 模组，2027 年具备量产条件](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 10.0/10

美光展示了全球首款采用 3D 堆叠技术的 512 GB DDR5 RDIMM，并计划于 2027 年实现量产，旨在满足高性能服务器的内存需求。

telegram · zaihuapd · 9月17日 00:15

**标签**: `#DRAM`, `#Memory`, `#Server Hardware`, `#3D Stacking`, `#DDR5`

---

<a id="item-5"></a>
## [GitLab.com 的速率限制正在发生变化](https://about.gitlab.com/blog/rate-limit-change-2026/) ⭐️ 9.0/10

GitLab.com 正在更新其速率限制，具体将免费计划上经过身份验证的请求限制提高到每小时 5,000 次，同时将未经身份验证的访问限制降低到每小时 60 次。 这一变化会影响依赖 GitLab API 的开发人员和 AI 代理，可能会迫使人们转向 GraphQL 以更高效地检索数据，并推动限制未经身份验证访问的更广泛的行业趋势。 新限制适用于所有 API 使用，虽然由于 GraphQL 能够限制结果集，因此建议 AI 代理使用，但每小时 5,000 次请求的限制仍然是一个硬性上限，需要仔细规划。

hackernews · darkwater · 9月17日 23:33 · [社区讨论](https://news.ycombinator.com/item?id=49742353)

**背景**: 速率限制是一种常见的做法，用于防止滥用并确保共享平台（如 GitLab.com）上的公平资源分配，在这些平台上，未经身份验证的请求通常受到限制，以保护基础设施和用户数据。

**社区讨论**: 用户们争论着利弊，一些人赞扬限制未经身份验证的访问对于可持续性是必要的，而另一些人则建议采用替代模式，如对抓取的数据进行货币化以支持开源项目。

**标签**: `#gitlab`, `#api`, `#rate-limiting`, `#graphql`, `#ai-agents`

---

<a id="item-6"></a>
## [datasette 1.0a40](https://simonwillison.net/2026/Sep/16/datasette/) ⭐️ 9.0/10

datasette 1.0a40 为插件引入了后台任务管理功能，并迁移至 httpx2，同时修复了若干错误。

rss · Simon Willison · 9月17日 07:51

**标签**: `#datasette`, `#python`, `#software-development`, `#bug-fixes`, `#httpx2`

---

<a id="item-7"></a>
## [datasette 0.65.5](https://simonwillison.net/2026/Sep/16/datasette-2/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Simon Willison · 9月17日 07:51

**标签**: `#datasette`, `#security`, `#software`, `#vulnerability`, `#release`

---

<a id="item-8"></a>
## [将 GitHub Copilot 运行时迁移至 Rust](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/) ⭐️ 9.0/10

GitHub 使用 Copilot CLI 和应用程序完全重写了其 Copilot 代理运行时，将其转换为超过 80 万行生产级 Rust 代码。 这次迁移展示了使用 AI 代理编写大规模生产代码的可行性，并为其他 AI 运行时迁移树立了先例。 重写工作跨越了 128 个拉取请求，并逐步发布，利用 Copilot SDK 进行经过生产测试的代理运行时集成。

rss · GitHub Blog · 9月17日 08:26

**背景**: GitHub Copilot 代理需要一个经过身份验证的运行时，而 Copilot SDK 暴露了 Copilot CLI 背后的相同引擎，用于程序化调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/agent-services/github-copilot">GitHub Copilot | Microsoft Learn</a></li>
<li><a href="https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/">Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog</a></li>

</ul>
</details>

**标签**: `#Rust`, `#GitHub Copilot`, `#Software Engineering`, `#AI Runtime`, `#Migration`

---

<a id="item-9"></a>
## [GoBench：在围棋游戏中评估大语言模型 \[R\]](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 9.0/10

GoBench 通过让大语言模型与 KataGo 对弈来评估其表现，结果显示其与 ARC-AGI 任务具有强相关性，并揭示了不同模型之间的性能差距。

reddit · r/MachineLearning · /u/Roland31415 · 9月17日 02:54

**标签**: `#AI`, `#LLM`, `#Go`, `#Benchmark`, `#Evaluation`

---

<a id="item-10"></a>
## [长鑫科技的临界点时刻 - 36 Kr](https://news.google.com/rss/articles/CBMiTkFVX3lxTE93UDZHajV5VjdQcTBqT1B5OHNtdFFZMFNuNGZnSXJVVTluQkZ4U3pFSWlSNFZCcGxxRWRwT0VLODFoYXVucjNQU2o4eVZZZw?oc=5) ⭐️ 9.0/10

本文讨论了长鑫存储科技在美国制裁和行业竞争背景下所面临的严峻挑战与关键转折点。

google\_news · 36 Kr · 9月17日 03:17

**标签**: `#semiconductors`, `#DRAM`, `#AI hardware`, `#supply chain`, `#China tech`

---

<a id="item-11"></a>
## [中国存储芯片市场：长鑫科技一家独大与现金流压力](https://news.google.com/rss/articles/CBMiUkFVX3lxTE91NTgyRlZ3Z1o4ME5qWVBpbk5neDZMVnZ3YnhwNmU1blM3QXpWb0RmZGR1OUhQWXNveXUzQWZWc3dGeEVUZkptQ3A3ZHZpYkJvS3c?oc=5) ⭐️ 8.0/10

一项财务分析显示，长鑫科技（CXMT）在中国存储芯片市场已占据主导地位，而 JMicron 等竞争对手正面临巨大的现金流压力。 这种市场集中度凸显了中国半导体行业激烈的竞争和财务脆弱性，这对于理解更广泛的供应链动态和国家技术战略至关重要。 报告指出，虽然长鑫科技蓬勃发展，但其他公司正面临流动性困境，这表明中国存储芯片制造商之间的财务健康状况和运营稳定性差距正在扩大。

google\_news · Sohu · 9月17日 23:02

**背景**: 中国存储芯片行业是国家技术独立的关键领域，CXMT 和 JMicron 等公司正竞争为智能手机、PC 和数据中心供应 DRAM 和 NAND 存储器。近期市场趋势显示，内存价格上涨和全球上行周期使长鑫科技等主要参与者受益，其全球 DRAM 市场份额已达到 10%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/09/04/changxin-memory-reaches-10-of-global-dram-market-in-q2/">ChangXin Memory reaches 10% of global DRAM market in Q2 · TechNode</a></li>
<li><a href="https://www.digitimes.com/news/a20260901VL205/profit-revenue-cxmt-dram-2026.html">China&#x27;s memory chipmakers post a record 1H — but not all of it came from chips</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory chips`, `#market analysis`, `#ChangXin`, `#financial performance`

---

<a id="item-12"></a>
## [PC 厂商争夺长鑫存储 DRAM 供应，订单排至 2027 年末](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5JQUpTVllRQXM0WVpPd2hYckkzQkhFWWxEN21lNnRaWkQxbC0xOGZLSzIwN1ZQOVdvWXpXbTl3dHlpLVhwUktDNjFGNVUxVmJtOGRUUzNXbjJ5WC1WZ0gyUDl3?oc=5) ⭐️ 8.0/10

PC 厂商正积极争夺长鑫存储（CXMT）的 DRAM 供应，且已确认的交付时间表将延续至 2027 年末。 这种激烈的竞争凸显了内存供应链对 PC 行业的重要性，并反映了国内中国内存制造商日益增长的市场影响力。 该新闻表明当前的订单积压量巨大，已将交付时间表推至 2027 年，这表明对长鑫存储内存产品的需求强劲且持续。

google\_news · 体坛 · 9月17日 09:30

**背景**: DRAM（动态随机存取存储器）是计算机中的基础组件，为操作系统和活跃应用程序提供运行所需的快速易失性内存。长鑫存储（CXMT）是一家知名的中国半导体公司，专注于 DRAM 芯片的设计和制造，该领域历史上由三星、SK 海力士和美光等全球主要参与者主导。

**标签**: `#semiconductors`, `#memory`, `#DRAM`, `#manufacturing`, `#supply\_chain`

---