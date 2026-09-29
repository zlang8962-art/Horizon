---
layout: default
title: "Horizon Summary: 2026-09-29 (ZH)"
date: 2026-09-29
content_date: 2026-09-28
lang: zh
---

> 报道范围：2026-09-28（Asia/Shanghai 自然日）

> 从 89 条内容中筛选出 10 条重要资讯。

---

1. [ggml-org/llama.cpp 发布 b11232 版本](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b11224](#item-2) ⭐️ 10.0/10
3. [介绍 cf：面向整个 Cloudflare API 的代理 CLI 工具](#item-3) ⭐️ 10.0/10
4. [免费开源 AI 工程课程现已提供 523 课时的书籍版本](#item-4) ⭐️ 10.0/10
5. [♻️ 英伟达发布 AI 智能体安全平台，助力防止 AI 代理逃逸](#item-5) ⭐️ 10.0/10
6. [Cloudflare 开源 BEACON：数十亿真实用户网络性能测量数据](#item-6) ⭐️ 9.0/10
7. [Functional Gradient Descent with Adaptive Representations \[R\]](#item-7) ⭐️ 9.0/10
8. [全球第 4 大 DRAM 厂商中国 CXMT 启动 IPO 流程…募资 295 亿元人民币 - cnnews.chosun.com](#item-8) ⭐️ 9.0/10
9. [SK 海力士子公司 Solidigm 拟赴美上市，或创半导体 IPO 新纪录](#item-9) ⭐️ 9.0/10
10. [中国扩大 AI 人才出境限制，亲属也需审批](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布 b11232 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b11232) ⭐️ 10.0/10

llama.cpp b11232 版本为 x86 架构添加了针对非向量倍数头部维度的分块 Flash Attention，并支持带掩码的加载和存储 AVX2 指令。

github · github-actions\[bot\] · 9月28日 22:22

**标签**: `#llama.cpp`, `#AI inference`, `#Flash Attention`, `#AVX2`, `#SIMD optimization`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b11224](https://github.com/ggml-org/llama.cpp/releases/tag/b11224) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月28日 15:06

**标签**: `#llama.cpp`, `#Vulkan`, `#GPU`, `#AI`, `#Software`

---

<a id="item-3"></a>
## [介绍 cf：面向整个 Cloudflare API 的代理 CLI 工具](https://blog.cloudflare.com/cloudflare-cf-cli-launch/) ⭐️ 10.0/10

Cloudflare 发布了 cf，这是一个代理 CLI 工具，可镜像整个 Cloudflare API，并开源了其内部 SDK 生成器 Forge。

rss · Cloudflare Blog · 9月28日 22:50

**标签**: `#CLI`, `#Developer Tools`, `#Cloudflare`, `#Open Source`, `#TypeScript`

---

<a id="item-4"></a>
## [免费开源 AI 工程课程现已提供 523 课时的书籍版本](https://www.reddit.com/r/MachineLearning/comments/1ws6e9p/free_opensource_ai_engineering_course_where_you/) ⭐️ 10.0/10

AI Engineering from Scratch 课程发布了六本 EPUB 和 PDF 卷，涵盖 523 课时的 20 个阶段，现已提供包括中文在内的八种语言版本。 这一全面且以标准库优先的课程使基础 AI 工程知识的获取民主化，使学习者能够从头开始构建算法，而无需依赖高级库。 该课程通过动手实现强调可重复性，通过 CI 包含自动化测试，并修复了损坏的数据集和模型，同时支持通过 npx skills add 进行编码代理。

reddit · r/MachineLearning · /u/SeveralSeat2176 · 9月28日 13:49

**背景**: AI Engineering from Scratch 是一个 MIT 许可的项目，通过要求学生使用标准库从头实现每个算法，来教授线性代数、反向传播、transformers 和 LLM 等核心概念。

**标签**: `#AI Engineering`, `#Open Source`, `#Machine Learning`, `#Education`, `#Transformers`

---

<a id="item-5"></a>
## [♻️ 英伟达发布 AI 智能体安全平台，助力防止 AI 代理逃逸](https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/) ⭐️ 10.0/10

英伟达推出了 Open Agent Safety 平台，包含 OpenShell 和 Sentry 等工具，旨在防止 AI 代理逃出沙箱并阻止未经授权的系统访问。

telegram · zaihuapd · 9月28日 17:33

**标签**: `#AI Safety`, `#Agent Security`, `#Sandbox Escape`, `#NVIDIA`, `#Developer Tools`

---

<a id="item-6"></a>
## [Cloudflare 开源 BEACON：数十亿真实用户网络性能测量数据](https://blog.cloudflare.com/how-fast-is-the-web/) ⭐️ 9.0/10

Cloudflare 开源了 BEACON 数据集，将数十亿个匿名化的真实用户监控（RUM）性能记录公开托管在 Google BigQuery 上供分析。 该数据集为开发者和研究人员提供了前所未有的真实网络性能数据访问权限，能够支持基于证据的优化并深入理解不同环境下的用户体验。 该数据集包含核心网络指标、软导航指标以及跨浏览器和地区的性能细分，提供了关于加载性能、交互性和视觉稳定性的见解。

rss · Cloudflare Blog · 9月28日 22:43

**背景**: 核心网络指标是一组用于衡量网页加载性能、交互性和视觉稳定性的真实用户体验指标，对于提供出色的用户体验至关重要。真实用户监控（RUM）从实际访问网站的用户的实时数据中捕获信息，通过分析页面在不同环境中的加载和表现方式，帮助识别性能问题并优化用户体验。Google BigQuery 是一个托管的无服务器数据仓库产品，通过 SQL 查询和内置机器学习功能，支持对海量数据集的可扩展分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/search/docs/appearance/core-web-vitals">Understanding Core Web Vitals and Google search results | Google Search Central | Documentation | Google for Developers</a></li>
<li><a href="https://web.dev/explore/learn-core-web-vitals">Core Web Vitals | web.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_BigQuery">Google BigQuery</a></li>

</ul>
</details>

**标签**: `#web-performance`, `#open-source`, `#real-user-monitoring`, `#data-science`, `#developer-tools`

---

<a id="item-7"></a>
## [Functional Gradient Descent with Adaptive Representations \[R\]](https://www.reddit.com/r/MachineLearning/comments/1wsejb7/functional_gradient_descent_with_adaptive/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

reddit · r/MachineLearning · /u/dccsillag0 · 9月28日 21:23

**标签**: `#machine-learning`, `#gradient-descent`, `#neurips`, `#optimization`, `#adaptive-representations`

---

<a id="item-8"></a>
## [全球第 4 大 DRAM 厂商中国 CXMT 启动 IPO 流程…募资 295 亿元人民币 - cnnews.chosun.com](https://news.google.com/rss/articles/CBMijgFBVV95cUxNcTUxQTAySVlIb0NoTGpCR09pbWtqbWowVlE1ZXNuX1B5SWpsRHp2ZUdfUmlTNWlpUzkwcHNhMVI1R2IyQzdYdFF3dmNiZTZVSkF3bWJYQmlqTUJ2UG9LS0t6V0luNGJ6VWhSVWxUZy05eEhKYk0yOUdXZWxielR6ZnEwUWdYOUVncndiUll3?oc=5) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

google\_news · cnnews.chosun.com · 9月28日 19:08

**标签**: `#DRAM`, `#Semiconductors`, `#AI Hardware`, `#IPO`, `#China Tech`

---

<a id="item-9"></a>
## [SK 海力士子公司 Solidigm 拟赴美上市，或创半导体 IPO 新纪录](https://news.google.com/rss/articles/CBMi2wFBVV95cUxQamFuRDVHalRYeUdlUGMtc0JWQ2hkY3dkVTVqWVplVmRxdWd0X25kVHFhaW1RS3NveWdwcXJzeldBU2RDUjlWeFVnS2psMzd4S0dJSGVSTldFSmprOFJuVFRlQXhJdWlnOW1lSHJxSF9RMG90Q2hiZTltX2RObWRRcjRSZlpKX053ZlotaV9BcHNjTGRhLW8zajNQRENUWGtUSjY5QlFySzB6VVVMS2NhR1NrdXdVZnBXejRXWXNPSjlvWW9jZzdsVzlCSWdnWEpnNmRVMFBwOF9vazg?oc=5) ⭐️ 9.0/10

SK 海力士的子公司 Solidigm 计划在美国上市，这可能创下半导体首次公开募股的新纪录。 这一举措意义重大，因为它凸显了半导体行业持续的整合和金融活动，可能影响市场趋势和投资流向。 投资者应密切关注具体的估值指标、公司的财务表现以及当前内存芯片股票的市场状况。

google\_news · TradingKey · 9月28日 00:47

**背景**: Solidigm 是 NAND 闪存和 DRAM 的领先制造商，于 2021 年从 SK 海力士分拆出来，专注于企业级和数据中心解决方案。

**标签**: `#semiconductor`, `#IPO`, `#SK Hynix`, `#Solidigm`, `#hardware`

---

<a id="item-10"></a>
## [中国扩大 AI 人才出境限制，亲属也需审批](https://www.bloomberg.com/news/articles/2026-09-28/china-broadens-travel-curbs-to-encompass-family-of-top-ai-talent) ⭐️ 8.0/10

中国扩大了对顶尖 AI 人才的出境限制，要求其亲属也需经过审批，这将对科技行业产生影响。

telegram · zaihuapd · 9月28日 18:27

**标签**: `#AI`, `#China`, `#National Security`, `#Tech Policy`, `#Talent`

---