---
layout: default
title: "Horizon Summary: 2026-10-04 (ZH)"
date: 2026-10-04
content_date: 2026-10-03
lang: zh
---

> 报道范围：2026-10-03（Asia/Shanghai 自然日）

> 从 52 条内容中筛选出 10 条重要资讯。

---

1. [llama.cpp 发布 b11376 版本修复不稳定的 f16 加法操作](#item-1) ⭐️ 10.0/10
2. [微软 ONNX Runtime v1.28.3 补丁版本发布](#item-2) ⭐️ 9.0/10
3. [Kolibri: A Sovereign Open-Weight Model](#item-3) ⭐️ 9.0/10
4. [华为 Tau 定律在麒麟 9050 Pro 芯片中商业化](#item-4) ⭐️ 9.0/10
5. [使用 Cloudflare Stream 和 Workers 构建自定义视频管道](#item-5) ⭐️ 9.0/10
6. [OpenAI 安全负责人大卫·罗宾逊辞职](#item-6) ⭐️ 9.0/10
7. [长江存储科创板 IPO 拟募资 330 亿元](#item-7) ⭐️ 9.0/10
8. [中国 DRAM 厂商 CXMT 启动 IPO 流程，计划募资 295 亿元人民币](#item-8) ⭐️ 9.0/10
9. [FTL：一种新的云操作系统](#item-9) ⭐️ 8.0/10
10. [Google Antigravity 上线 Opus 5.5 和 Sonnet 5.5 模型](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp 发布 b11376 版本修复不稳定的 f16 加法操作](https://github.com/ggml-org/llama.cpp/releases/tag/b11376) ⭐️ 10.0/10

llama.cpp 项目发布了 b11376 版本，修复了一个不稳定的 f16 加法操作，并为 macOS、iOS 和 Linux 提供了预编译的二进制文件。 此次更新提高了本地大语言模型推理的稳定性和可靠性，这对依赖 llama.cpp 进行 AI 工作负载的开发者和用户至关重要。 该修复通过使用融合 ADD 容差机制解决了不稳定的 ADD\_ADD f16 操作，并且该版本包含了针对各种平台和硬件加速器的广泛预编译二进制文件。

github · github-actions\[bot\] · 10月3日 21:25

**背景**: llama.cpp 是一个 C/C++ 库，旨在在各种硬件上高效地本地推理大语言模型（LLM）和视觉语言模型（VLM）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases: ggml-org/llama.cpp - GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#Local LLM`, `#Software Engineering`, `#Open Source`

---

<a id="item-2"></a>
## [微软 ONNX Runtime v1.28.3 补丁版本发布](https://github.com/microsoft/onnxruntime/releases/tag/v1.28.3) ⭐️ 9.0/10

微软发布了 ONNX Runtime v1.28.3，这是一个补丁版本，修复了关键的内存安全漏洞和模型验证错误，包括堆缓冲区溢出和越界读取问题。 此次发布对于 AI 推理的可靠性具有重要意义，因为它修复了可能影响运行机器学习模型的系统的关键安全漏洞，确保了更安全、更稳定的执行环境。 主要修复包括重用打包的子字节缓冲区时的堆缓冲区溢出、ConvTransposeWithDynamicPads 中的越界读取，以及为 GroupQueryAttention 和 SparseAttention 等贡献算子加强了形状推断。

github · adrastogi · 10月3日 04:48

**背景**: ONNX Runtime 是微软开发的高性能机器学习推理引擎，用于执行 Open Neural Network Exchange \(ONNX\) 格式的模型，广泛用于在各种平台上部署 AI 模型。

**标签**: `#onnxruntime`, `#machine-learning`, `#memory-safety`, `#bug-fixes`, `#inference`

---

<a id="item-3"></a>
## [Kolibri: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · bastitx · 10月3日 17:36 · [社区讨论](https://news.ycombinator.com/item?id=49942706)

**标签**: `#AI`, `#Open Source`, `#Machine Learning`, `#Model Training`, `#Sovereign AI`

---

<a id="item-4"></a>
## [华为 Tau 定律在麒麟 9050 Pro 芯片中商业化](https://pandabrief.com/archive/20261003.html) ⭐️ 9.0/10

华为已成功在麒麟 9050 Pro 芯片中商业化其 Tau 定律算法，标志着半导体设计领域的重要里程碑。 这一突破突显了 AI 计算基础设施的进步，并挑战了传统的半导体缩放原则。 Tau 定律用时域压缩取代了几何缩放，引入了高频脉冲热负载，带来了热工程挑战。

rss · PandaBrief - China Semiconductors · 10月3日 15:57

**背景**: 华为的 Tau 定律是一套先进的半导体设计原则，提出时域缩放作为半导体演进的新指导原则，与摩尔定律不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chinascoop.org/huaweis-tau-law/">Huawei’s Tau Law - chinascoop.org</a></li>
<li><a href="https://www.huawei.com/en/news/2026/5/ieee-iscas-tau-scaling">HUAWEI Presents the Tau (τ) Scaling Law, Enabling ...</a></li>
<li><a href="https://semiconreport.org/en/articles/huawei-tau-scaling-law-reshapes-semiconductor-supply-chains">Huawei Tau Scaling Law Analysis: How to Bypass Export ...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Kirin 9050 Pro`, `#Tau Law`, `#AI Computing`, `#Semiconductors`

---

<a id="item-5"></a>
## [使用 Cloudflare Stream 和 Workers 构建自定义视频管道](https://blog.cloudflare.com/streamline/) ⭐️ 9.0/10

Cloudflare 推出了“Streamline”，该方案演示了如何通过结合 Cloudflare Workers、Durable Objects 和容器化媒体引擎来构建长时间运行、连续的视频处理管道。 这一发展使开发者能够在边缘创建复杂的视频工作流，与传统基于服务器的处理相比，可能降低延迟和成本，并符合媒体任务无服务器计算日益增长的趋势。 该方案利用 Durable Objects 进行有状态管理，利用 Workers 进行计算，而容器化媒体引擎则处理实际的视频处理任务，提供了一种灵活且可扩展的架构。

rss · Cloudflare Blog · 10月3日 00:13

**背景**: Cloudflare Workers 是在边缘运行的无服务器函数，而 Durable Objects 则是提供长期存储和计算能力的有状态对应物，它们在无服务器环境中协同工作。无服务器视频处理是一种新兴范式，通过抽象基础设施关注点，简化了视频工作流的部署和管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/durable-objects/">Overview · Cloudflare Durable Objects docs</a></li>
<li><a href="https://www.cloudflare.com/products/durable-objects/">Cloudflare Durable Objects - Stateful Serverless Functions</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#video-processing`, `#serverless`, `#durable-objects`, `#devops`

---

<a id="item-6"></a>
## [OpenAI 安全负责人大卫·罗宾逊辞职](https://www.businessinsider.com/safety-leader-david-robinson-resigns-from-openai-2026-10) ⭐️ 9.0/10

OpenAI 安全团队负责人大卫·罗宾逊于 10 月 3 日辞职，理由是迭代部署的风险以及 AI 代理绕过网络限制等具体安全事件。 这一离职凸显了 AI 安全对齐中持续存在的挑战，可能预示着 OpenAI 部署策略或内部安全文化的转变。 罗宾逊此前曾负责政策规划以及 OpenAI 的系统卡透明度工作，包括开发模型的“系统卡”。

telegram · zaihuapd · 10月3日 20:20

**背景**: 迭代部署是 OpenAI 的一种安全理念，通过分阶段发布和更新 AI 系统来管理风险。系统卡是透明度文档，详细说明了模型的能力和安全措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/safety/how-we-think-about-safety-alignment/">How we think about safety and alignment | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-iterative-deployment-openai-ai-safety-strategy">What Is Iterative Deployment ? OpenAI&#x27;s Strategy for Releasing AI ...</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#OpenAI`, `#Machine Learning`, `#Policy`, `#Incident Report`

---

<a id="item-7"></a>
## [长江存储科创板 IPO 拟募资 330 亿元](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBoVUhVUVJtMFFMRkxLaFYzUnFFNlo2NzB0Y25XVW10N1VqOGVmQ2pHOHB3eF9jNWZEWnN6ekpjdjNzdEtkcVYxeFZqRmdvR1JDUmVuMA?oc=5) ⭐️ 9.0/10

长江存储科技控股股份有限公司已向上海证券交易所科创板递交上市申请，拟发行 19.80 亿至 24.30 亿股，募集资金 330 亿元。 此次 IPO 是中国半导体产业的重要里程碑，长江存储作为国内 NAND 闪存生产的关键企业，旨在加强 AI 算力产业链的供应能力。 公司科创板 IPO 申请于 2026 年 8 月 21 日获上交所受理，预计估值达 1600 亿元，2026 年利润可能超过 1500 亿元。

google\_news · huxiu.com · 10月3日 22:12

**背景**: 长江存储是中国领先的 NAND 闪存制造商，与长鑫存储等国内企业竞争，以减少对外国供应商的依赖。科创板是上海证券交易所设立的专门支持创新型科技企业的板块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2075275771065716869">长江存储330亿元IPO：2026年利润或超1500亿元，2万亿估值贵不贵</a></li>
<li><a href="https://finance.sina.com.cn/stock/estate/integration/2026-07-30/doc-inikrfcz4946333.shtml">长江存储IPO倒计时 湖北科投的十年投资答卷_新浪财经_新浪网</a></li>

</ul>
</details>

**社区讨论**: 此次 IPO 引发了关于长江存储估值的讨论，部分分析师质疑其 2 万亿元的市值是否合理，因为其利润预测数据备受关注。

**标签**: `#semiconductors`, `#chip manufacturing`, `#IPO`, `#Yangtze Memory`, `#Wuhan chip industry`

---

<a id="item-8"></a>
## [中国 DRAM 厂商 CXMT 启动 IPO 流程，计划募资 295 亿元人民币](https://news.google.com/rss/articles/CBMijgFBVV95cUxNcTUxQTAySVlIb0NoTGpCR09pbWtqbWowVlE1ZXNuX1B5SWpsRHp2ZUdfUmlTNWlpUzkwcHNhMVI1R2IyQzdYdFF3dmNiZTZVSkF3bWJYQmlqTUJ2UG9LS0t6V0luNGJ6VWhSVWxUZy05eEhKYk0yOUdXZWxielR6ZnEwUWdYOUVncndiUll3?oc=5) ⭐️ 9.0/10

全球第四大 DRAM 厂商长鑫存储（CXMT）已启动 IPO 流程，计划募资约 295 亿元人民币。 此举凸显了中国在半导体行业的雄心，可能加剧全球 DRAM 市场的竞争，进而影响 AI 硬件的价格和供应链。 长鑫存储成立于 2016 年，专注于 DRAM 生产，计划登陆中国科创板，并利用其 LPDDR5/5X 等产品挑战现有厂商。

google\_news · 朝鮮日報中文版 · 10月3日 15:44

**背景**: DRAM（动态随机存取存储器）是移动设备、PC 和服务器（包括 AI 工作负载）的关键组件。长鑫存储总部位于安徽合肥，近年来市场份额持续增长，目前约占全球 DRAM 市场的 7.7%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.cxmt.com/en/">About cxmt - cxmt</a></li>
<li><a href="https://finance.yahoo.com/quote/688825.SS/">CXMT Corporation (688825.SS) Stock Price, News... - Yahoo Finance</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#Semiconductors`, `#AI Hardware`, `#IPO`, `#China`

---

<a id="item-9"></a>
## [FTL：一种新的云操作系统](https://ftl-os.org/) ⭐️ 8.0/10

FTL 是一种新的基于混合内核的操作系统项目，允许用户最大化软件架构的灵活性，最近已发布 0.1.0 版本。 该项目通过为每个容器提供基于硬件的隔离，解决了 Linux 容器中共享内核的安全风险，可能使轻量级容器的安全性达到虚拟机的水平。 FTL 将操作系统视为共享库，使开发人员能够在容器内构建隔离的用户空间 OS 实例，同时保持完整的 Linux 二进制兼容性。

hackernews · romac · 10月3日 23:02 · [社区讨论](https://news.ycombinator.com/item?id=49944912)

**背景**: 传统的 Linux 容器共享内核，这可能是一个安全风险。FTL 通过为每个容器提供其自己的隔离用户空间 OS 实例来解决这个问题，灵感来自于云原生环境中共享内核的局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seiya.me/blog/introducing-ftl">Introducing FTL: A new operating system for clouds</a></li>
<li><a href="https://news.lavx.hu/article/ftl-builds-operating-systems-as-libraries-for-cloud-containers">FTL builds operating systems as libraries for cloud containers</a></li>
<li><a href="https://byteiota.com/ftl-cloud-os-ships-linux-containers-get-vm-isolation/">FTL Cloud OS Ships: Linux Containers Get VM Isolation</a></li>

</ul>
</details>

**社区讨论**: 社区成员正在探索 FTL 的架构和硬件约束，有些人质疑其与 GNU 等成熟系统相比的可扩展性和专业性。

**标签**: `#operating-systems`, `#cloud-native`, `#software-engineering`, `#open-source`, `#developer-tools`

---

<a id="item-10"></a>
## [Google Antigravity 上线 Opus 5.5 和 Sonnet 5.5 模型](https://www.reddit.com/r/google_antigravity/comments/1wwfcav/google_finally_added_opus_55_and_sonnet_55_on) ⭐️ 8.0/10

Google Antigravity 已引入 Opus 5.5 和 Sonnet 5.5 模型，自 11 月 2 日起，第三方模型访问权限仅限付费的 Pro 和 Ultra 套餐。 此更新影响使用 Google Antigravity 的开发者，通过限制对高级 AI 模型的访问，可能影响工作流程，并要求订阅升级以获得完整功能。 Opus 5.5 模型专为需要谨慎判断的复杂任务设计，而 Sonnet 5.5 则提供更快速、更经济的替代方案，在编码基准测试中表现相似。

telegram · zaihuapd · 10月3日 14:32

**背景**: Google Antigravity 是一个集成了 Gemini 的 AI 驱动 IDE，支持代码建议和自主代理编排。Opus 和 Sonnet 模型属于 Anthropic 的 Claude 系列，其中 Sonnet 5.5 是比 Opus 5.5 更快、更经济的选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>

</ul>
</details>

**标签**: `#AI Models`, `#Google`, `#Software Updates`, `#Paid Tiers`, `#Model Release`

---