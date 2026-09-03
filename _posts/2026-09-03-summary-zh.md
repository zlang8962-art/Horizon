---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
content_date: 2026-09-02
lang: zh
---

> 报道范围：2026-09-02（Asia/Shanghai 自然日）

> 从 77 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp 发布 b10759：KleidiAI 修复与跨平台二进制文件](#item-1) ⭐️ 10.0/10
2. [llama.cpp 发布 b10758 优化 Hexagon DSP](#item-2) ⭐️ 10.0/10
3. [Introducing agentic video understanding with Gemini](#item-3) ⭐️ 10.0/10
4. [ollama/ollama 发布了 v0.33.3-rc2 版本](#item-4) ⭐️ 9.0/10
5. [GeoJSON 地图查看器](#item-5) ⭐️ 9.0/10
6. [韩国万亿级主权 AI 投资](#item-6) ⭐️ 9.0/10
7. [从头开始创建文本到图像模型的详细指南](#item-7) ⭐️ 9.0/10
8. [♻️ 英伟达 129 亿美元收购 Hugging Face，将掌控最大开源 AI 平台](#item-8) ⭐️ 9.0/10
9. [Nexus 暗网兜售 1.53 亿张驾照扫描件，FBI 已介入调查](#item-9) ⭐️ 9.0/10
10. [长鑫存储拒绝苹果降价要求，坚持与三星和 SK 海力士持平](#item-10) ⭐️ 9.0/10
11. [中信证券看好中国国产半导体设备及核心零部件产业链](#item-11) ⭐️ 9.0/10
12. [三个网站制作了 215,128 个“最佳软件”页面用于 AI。Perplexity 引用了它们](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp 发布 b10759：KleidiAI 修复与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10759) ⭐️ 10.0/10

llama.cpp 版本 b10759 解决了 KleidiAI 的缓冲区类型初始化问题，并为 macOS、iOS、Linux、Android 和 Windows 提供了预编译的二进制文件。 此次发布对依赖 Apple Silicon 和 ARM 设备的开发者和用户至关重要，因为它确保了稳定的性能，并扩大了本地大语言模型推理在多样化操作系统上的可访问性。 KleidiAI 缓冲区类型修复可防止潜在的初始化错误，而该版本包含 macOS Apple Silicon 上启用 KleidiAI 的禁用构建，并支持 CUDA、Vulkan 和 ROCm 等多种后端。

github · github-actions\[bot\] · 9月2日 18:22

**背景**: llama.cpp 是一个广泛使用的开源库，用于在本地运行大语言模型，常作为 Ollama 和 LM Studio 等工具的核心。KleidiAI 是一个基于 ARM 的加速框架，可优化手机和树莓派等设备的推理性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/ kleidiai : This repository is a read-only mirror of...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#Apple Silicon`, `#KleidiAI`, `#Software Release`

---

<a id="item-2"></a>
## [llama.cpp 发布 b10758 优化 Hexagon DSP](https://github.com/ggml-org/llama.cpp/releases/tag/b10758) ⭐️ 10.0/10

llama.cpp 版本 b10758 针对高通 Hexagon DSP 加速引入了矩阵乘融合和内存管理修复。 此次发布显著提升了在骁龙设备上进行 LLM 推理的性能和稳定性，扩展了高效本地 AI 的硬件支持。 关键改进包括融合 QKV 和 FFN 矩阵乘、移除硬编码的维度限制，并添加虚拟地址（VA）空间碎片整理以防止碎片化问题。

github · github-actions\[bot\] · 9月2日 17:29

**背景**: 高通 Hexagon DSP 是一种专为高性能信号处理和 AI 工作负载设计的微架构，常用于移动设备。Hexagon NPU（神经网络处理单元）是用于这些任务的专用硬件加速器。llama.cpp 是一个用于在各种硬件上运行大语言模型（LLM）的高性能 C++ 库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qualcomm_Hexagon">Qualcomm Hexagon - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/8273">Performance of llama.cpp on Snapdragon X Elite/Plus · ggml-org/llama.cpp · Discussion #8273</a></li>
<li><a href="https://docs.qualcomm.com/bundle/publicresource/topics/80-N2040-61/memory.html">Memory - Hexagon V79 HVX Programmer Reference Manual</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#Hexagon DSP`, `#C++ optimization`, `#GPU acceleration`

---

<a id="item-3"></a>
## [Introducing agentic video understanding with Gemini](https://deepmind.google/blog/introducing-agentic-video-in-gemini/) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Google DeepMind News · 9月2日 01:08

**标签**: `#AI`, `#Video Understanding`, `#Gemini`, `#Agentic AI`, `#Google DeepMind`

---

<a id="item-4"></a>
## [ollama/ollama 发布了 v0.33.3-rc2 版本](https://github.com/ollama/ollama/releases/tag/v0.33.3-rc2) ⭐️ 9.0/10

Ollama v0.33.3-rc2 引入了 AI 模型优化以及 MLX/llama.cpp 的更新，并新增了一位贡献者。

github · github-actions\[bot\] · 9月2日 08:11

**标签**: `#AI`, `#Ollama`, `#MLX`, `#llama.cpp`, `#Software Release`

---

<a id="item-5"></a>
## [GeoJSON 地图查看器](https://simonwillison.net/2026/Sep/1/geojson/) ⭐️ 9.0/10

Simon Willison 分享了一个利用 AI 辅助构建的 GeoJSON 地图查看器工具，用于可视化并导出地图数据。

rss · Simon Willison · 9月2日 02:05

**标签**: `#GeoJSON`, `#Web Tools`, `#Data Visualization`, `#Developer Tools`, `#AI-Assisted Development`

---

<a id="item-6"></a>
## [韩国万亿级主权 AI 投资](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 9.0/10

韩国正在启动一项大规模的主权 AI 投资计划，Nvidia 成为主要受益者，而 Hynix 则在该战略举措中面临挑战。 这项投资凸显了主权 AI 战略在国家安全和经济竞争力中的关键作用，特别是在半导体和 AI 基础设施领域。 该计划包括国家 AI 竞赛，并强调开源模型，这可能会重塑 AI 基础设施提供商的竞争格局。

rss · Semianalysis · 9月2日 04:14

**背景**: 主权 AI 是指一个国家独立开发和部署 AI 系统的能力，通常由国家在国家安全和经济增长方面的战略利益所驱动。韩国作为全球半导体制造强国，正利用其优势构建强大的 AI 生态系统。

**标签**: `#AI Infrastructure`, `#Semiconductors`, `#Sovereign AI`, `#Open Source`, `#Hardware`

---

<a id="item-7"></a>
## [从头开始创建文本到图像模型的详细指南](https://www.reddit.com/r/MachineLearning/comments/1w5c9rd/detailed_explanation_of_how_to_create_a/) ⭐️ 9.0/10

这是一本详细的食谱和代码库，用于从零开始构建文本到图像模型，包含数据集和工具。

reddit · r/MachineLearning · /u/dh7net · 9月2日 22:40

**标签**: `#text-to-image`, `#machine-learning`, `#open-source`, `#deep-learning`, `#reproducibility`

---

<a id="item-8"></a>
## [♻️ 英伟达 129 亿美元收购 Hugging Face，将掌控最大开源 AI 平台](https://www.techzine.eu/news/analytics/143877/nvidia-to-acquire-hugging-face-for-12-9-billion/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月2日 14:50

**标签**: `#AI`, `#NVIDIA`, `#Hugging Face`, `#Open Source`, `#Acquisition`

---

<a id="item-9"></a>
## [Nexus 暗网兜售 1.53 亿张驾照扫描件，FBI 已介入调查](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 9.0/10

FBI 正在调查一个名为 Nexus 的暗网服务，该服务正在兜售超过 1.53 亿张驾照扫描件。

telegram · zaihuapd · 9月2日 17:31

**标签**: `#data\_breach`, `#identity\_theft`, `#dark\_web`, `#privacy`, `#cybersecurity`

---

<a id="item-10"></a>
## [长鑫存储拒绝苹果降价要求，坚持与三星和 SK 海力士持平](https://news.google.com/rss/articles/CBMickFVX3lxTE5uWVlNeVhudklNQjN4MXNpQldzZlZ4djJ4bTdLaF9YdjMtVzhEX3ppbTNmLUdWLVRJb1hKOWRab2VLRGdJUVg4bFZ0YnptV2tFVUFIS1Q5MGx0eEY2YnFUUXBhSkZocW9OOVhJUDRRX21CZw?oc=5) ⭐️ 9.0/10

长鑫存储（CXMT）拒绝了苹果的降价要求，坚持与主要竞争对手三星和 SK 海力士保持价格持平。 这一立场凸显了中国内存制造商对其市场地位的信心，可能预示着全球内存定价动态的转变。 该新闻特别提到，CXMT 决定在回应苹果要求时，保持不低于三星和 SK 海力士的价格水平。

google\_news · 新浪网 · 9月2日 21:31

**标签**: `#semiconductors`, `#memory`, `#CXMT`, `#pricing`, `#Apple`

---

<a id="item-11"></a>
## [中信证券看好中国国产半导体设备及核心零部件产业链](https://news.google.com/rss/articles/CBMijAFBVV95cUxNb3htSFlCOUc3YUhpa3pqMzlGUC10RTM1dnNyRzA3cmFCVGtrTFV2LXQyVklXaVRSWTlrejB6cUMzbU5pWDNzX3JmcDdCVnluNDFwRmtxU0hwTFYxWjJhSEo5eEFuc3FVOHpfNWEzand2MDNlOVlibDN0RXFkemt5QWg4YTZkWTN0UUhBUA?oc=5) ⭐️ 9.0/10

中信证券发布了一份市场展望，重申其对国产半导体设备及核心零部件产业链持续增长和发展的强烈信心。 来自主要金融机构的这一背书意义重大，因为它表明了对国内硬件能力在中国技术自主和 AI 基础设施建设中战略重要性的信心。 该分析聚焦于整个产业链，包括上游设备和下游核心零部件，强调了该板块在支持更广泛的半导体制造和 AI 加速器生产中的关键作用。

google\_news · Sohu · 9月2日 14:38

**背景**: 半导体设备行业是全球技术生态系统的基石，为制造集成电路和先进 AI 硬件提供必要的机器和工具。中国一直在积极投资该领域，以减少对外国供应商的依赖，并为其蓬勃发展的 AI 和消费电子产品市场建立自给自足的供应链。

**标签**: `#semiconductors`, `#AI hardware`, `#market analysis`, `#China tech`, `#supply chain`

---

<a id="item-12"></a>
## [三个网站制作了 215,128 个“最佳软件”页面用于 AI。Perplexity 引用了它们](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

一项调查揭示了三个网站如何创建 215,128 个 AI 推荐的页面，Perplexity 引用了这些页面，凸显了 LLM 生成内容的问题。

hackernews · jakobgreenfeld · 9月2日 21:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**标签**: `#AI`, `#LLMs`, `#Perplexity`, `#Search Engines`, `#Data Safety`

---