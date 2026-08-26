---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
content_date: 2026-08-25
lang: zh
---

> 报道范围：2026-08-25（Asia/Shanghai 自然日）

> 从 104 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp v0.3.0：多模态、MTP 和 Tensor-Split 更新](#item-1) ⭐️ 10.0/10
2. [llm-anthropic 0.27 更新插件以兼容 Anthropic SDK v1.0.0](#item-2) ⭐️ 10.0/10
3. [英伟达宣布 Vera Rubin NVL72 和 Groq 3 LPX 以提升 AI 智能体性能](#item-3) ⭐️ 10.0/10
4. [ONNX Runtime WebGPU 插件 EP 0.3.0 发布](#item-4) ⭐️ 9.0/10
5. [苹果推出 M6 和 M5 Ultra 芯片](#item-5) ⭐️ 9.0/10
6. [OpenAI 的 Jalapeño 芯片性能超越 Nvidia 的 Blackwell](#item-6) ⭐️ 9.0/10
7. [Cloudflare 将博客迁移到开源 EmDash CMS](#item-7) ⭐️ 9.0/10
8. [持续学习使主权 AI 能够实现前沿模型](#item-8) ⭐️ 9.0/10
9. [使用 PostgreSQL、pgvector 和 Qwen3 构建最先进搜索引擎](#item-9) ⭐️ 9.0/10
10. [Qwen 预告 8 月 26 日开源 Qwen3.8-Flash-Next](#item-10) ⭐️ 9.0/10
11. [长江存储启动 IPO，聚焦 Xtacking 技术冲击全球 NAND 市场](#item-11) ⭐️ 9.0/10
12. [小米玄戒 O3 行业首发 LPDDR6，核心合作方为长鑫存储](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp v0.3.0：多模态、MTP 和 Tensor-Split 更新](https://github.com/ggml-org/llama.cpp/releases/tag/v0.3.0) ⭐️ 10.0/10

llama.cpp v0.3.0 通过 dots3-note 模型和新的 DSA-ISWA KV 缓存引入了多模态支持，为 GLM-4.5-Air 添加了多令牌预测（MTP），并实现了张量分割模式（-sm tensor）以及 DeepSeek 4 的修复。 此版本显著扩展了 llama.cpp 对 GLM-4.5-Air 和 DeepSeek 4 等先进 AI 模型的兼容性，实现了更高效的多 GPU 推理和多模态功能，这对设备端 AI 应用至关重要。 更新包括 dots3-note 的 DSA-ISWA KV 缓存、GLM-4.5-Air 的 MTP 以及 DeepSeek 4 的张量分割修复，同时 ggml 升级到 v0.22.0，改进了 Metal 内核并行编译和非原地 clamp 操作。

github · github-actions\[bot\] · 8月25日 18:22

**背景**: llama.cpp 是一个高性能的 LLM 推理引擎，针对 CPU 和 GPU 进行了优化。张量分割允许将模型权重分布在多个 GPU 上以处理大型模型，而 MTP（多令牌预测）通过一次预测多个令牌来加速推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://habr.com/ru/articles/1021832/">KV - Cache в LLM: разбираем инференс через 9 ключевых... / Хабр</a></li>
<li><a href="https://korshunov.ai/en/article/20686-llama-cpp-0-3-0-adds-dots3-note-model-and-tensor-split-for-deepseek-4/">llama.cpp 0.3.0 adds dots3-note model and tensor-split for DeepSeek 4</a></li>
<li><a href="https://glm45.org/">GLM - 4 . 5 - by Zhipu AI</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#Open Source`, `#GPU`, `#Multimodal`

---

<a id="item-2"></a>
## [llm-anthropic 0.27 更新插件以兼容 Anthropic SDK v1.0.0](https://simonwillison.net/2026/Aug/24/llm-anthropic/) ⭐️ 10.0/10

llm-anthropic 插件版本 0.27 更新以支持 Anthropic 的 Python SDK v1.0.0，该版本从 httpx 迁移到 httpx2，这与 OpenAI 近期的 v3.0.0 更新类似。 此次更新确保与最新的 Anthropic SDK 兼容，使开发人员能够在不出现破坏性更改的情况下继续使用该插件，并保持对 Claude API 的访问。 Anthropic 为升级到 SDK 1.0 提供了迁移指南，该插件的 PR \#84 成功实现了这些更改并通过了测试。

rss · Simon Willison · 8月25日 00:27

**背景**: Anthropic Python SDK 为 Python 应用程序提供对 Claude API 的访问，支持同步/异步操作以及与云平台的集成。HTTPX 是一个现代 HTTP 客户端库，而 HTTPX 2 在其基础上构建了增强功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/anthropic-sdk-python">GitHub - anthropics/anthropic-sdk-python</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Anthropic`, `#Python`, `#SDK`, `#Migration`

---

<a id="item-3"></a>
## [英伟达宣布 Vera Rubin NVL72 和 Groq 3 LPX 以提升 AI 智能体性能](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 10.0/10

英伟达首次公布了 Vera Rubin NVL72 机柜的片上实测数据，显示 DeepSeek-V4-Pro 智能体编码任务的吞吐量较 GB300 最高提升 30 倍，每百万 Token 成本最高下降 35 倍。同期宣布推理加速芯片 Groq 3 LPX 进入量产，并发布智能体专用 Vera CPU，SpaceX 计划于 2027 年将 NVL72 部署到轨道上。 Vera Rubin NVL72 架构代表了 AI 计算效率的重大飞跃，可能重塑数据中心处理大规模 AI 工作负载的方式。Groq 3 LPX 和 Vera CPU 旨在优化推理和基于智能体的任务，这对不断增长的 AI 智能体生态系统至关重要。 NVL72 系统在一个 NVLink 6 域中结合了 72 颗 Rubin GPU 和 36 颗 Vera CPU，总功耗超过 100 千瓦。Groq 3 LPX 可实现 Gemma 4 31B 每秒 3400 个 Token 的输出，系统使用被动铜缆进行机柜内 NVLink 连接。

telegram · zaihuapd · 8月25日 22:48

**背景**: Vera Rubin 是英伟达的下一代数据中心平台，Vera CPU 采用定制的 Olympus Arm 核心，并配备高带宽内存。NVL72 是一个专为 AI 推理和训练设计的机柜级系统，利用 NVLink 6 实现高速互连。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://axecompute.com/vera-rubin-the-right-compute-as-you-scale/">Vera Rubin Early Access: The Right Compute as You Scale</a></li>
<li><a href="https://benquan.hk/article-vera-rubin-nvl72.html">NVIDIA Vera Rubin NVL 72 Deep Dive 2026 | BENQUAN Global</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI Hardware`, `#Inference`, `#DeepSeek`, `#Vera Rubin`

---

<a id="item-4"></a>
## [ONNX Runtime WebGPU 插件 EP 0.3.0 发布](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.3.0) ⭐️ 9.0/10

ONNX Runtime WebGPU 插件 EP 0.3.0 添加了对 PagedAttention、MRotaryEmbedding 和其他算子的支持，同时提高了生成式模型的性能和配置可靠性。 此次发布扩展了 AI 模型覆盖范围并增强了生成式模型的性能，直接影响了 WebGPU 平台的 AI 计算和软件开发。 主要改进包括延迟调度以并行编译着色器、Intel 子组矩阵 MatMul 内核，以及扩展了算子间的整数支持。

github · edgchen1 · 8月25日 05:44

**背景**: ONNX Runtime 是一个开源的机器学习推理加速器，而 WebGPU 是一种可在 Web 上进行高性能计算的图形 API。

**标签**: `#ONNX Runtime`, `#WebGPU`, `#AI Acceleration`, `#Machine Learning`, `#Software Development`

---

<a id="item-5"></a>
## [苹果推出 M6 和 M5 Ultra 芯片](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

苹果在新的 Mac mini 中推出了 M6 芯片，并在 refreshed Mac Studio 中推出了 M5 Ultra，这标志着其首款 2nm 处理器和四芯片架构。 这些芯片在性能和 AI 能力上实现了显著飞跃，可能重塑高性能计算和本地 AI 处理的格局。 M5 Ultra 使用 UltraFusion 技术连接两个双芯片 M5 Max，实现超过 4.4TB/s 的芯片间带宽，而 M6 拥有双 16 核神经引擎以实现更快的 AI 计算。

hackernews · interpol\_p · 8月25日 21:01 · [社区讨论](https://news.ycombinator.com/item?id=49433292)

**背景**: 苹果的 M 系列芯片以其能效和性能著称，UltraFusion 技术能够在多个芯片之间实现高带宽连接，从而增强计算能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in ...</a></li>
<li><a href="https://www.macrumors.com/2026/08/25/apple-debuts-m5-ultra/">Apple Debuts M 5 Ultra as Most Powerful Chip Ever - MacRumors</a></li>
<li><a href="https://9to5mac.com/2026/08/25/apple-launches-next-gen-apple-silicon-chips-m6-and-m5-ultra/">Apple launches next-gen Apple Silicon chips: M6 and M5 Ultra - 9to5Mac</a></li>

</ul>
</details>

**社区讨论**: 用户对性能提升印象深刻，但对价格表示担忧，有传言称苹果可能会跳过 M6 Pro 和 Max 变体，专注于开发用于 AI 的 M7 芯片。

**标签**: `#Apple`, `#M6`, `#M5 Ultra`, `#AI Compute`, `#Chips`

---

<a id="item-6"></a>
## [OpenAI 的 Jalapeño 芯片性能超越 Nvidia 的 Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI 推出了其定制的 Jalapeño 芯片，声称在基准测试中性能超越了 Nvidia 的 Blackwell。 这一发展凸显了公司设计自有 AI 加速器以减少对 Nvidia 依赖并提高效率的日益增长的趋势。 Jalapeño 芯片专为 LLM 推理设计，与上一代相比提供更高的吞吐量和更低的延迟。

hackernews · Semianalysis · 8月25日 22:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

**背景**: OpenAI 和 Broadcom 宣布了一项战略合作，计划到 2029 年部署 10 吉瓦的自定义 AI 加速器，包括 Jalapeño。该芯片是 OpenAI 全栈 AI 系统方法的一部分，将模型、芯片和内存集成以优化性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/">OpenAI’s Jalapeño chip is built for fast inference at scale, benchmarks show | TechCrunch</a></li>

</ul>
</details>

**社区讨论**: 社区讨论集中在芯片的 FP4 精度、芯片尺寸以及与人类语音的效率对比，一些人指出其将 LLM 权重直接烘焙到硬件中的潜力。

**标签**: `#AI compute`, `#chips hardware`, `#inference chips`, `#OpenAI`, `#Nvidia`

---

<a id="item-7"></a>
## [Cloudflare 将博客迁移到开源 EmDash CMS](https://blog.cloudflare.com/cloudflare-blog-uses-emdash/) ⭐️ 9.0/10

Cloudflare 已将其官方博客迁移到 EmDash，这是一个基于 TypeScript 和 Astro 的新开源 CMS，旨在验证其在大规模环境下的性能表现。 这次迁移展示了 Cloudflare 对开源工具的承诺，并为对现代 CMS 架构和无服务器工作流程感兴趣的开发者提供了一个真实的案例研究。 博客经历了性能压力测试、生产流量路由和前端重新设计，以确保可靠性和可扩展性。

rss · Cloudflare Blog · 8月25日 03:00

**背景**: EmDash 是一个全栈 TypeScript CMS，旨在作为 WordPress 的精神继承者，专注于安全性、类型安全和 AI 优先的工作流程。它运行在 Cloudflare 的基础设施上，旨在通过解决插件漏洞和实现无服务器部署来取代 WordPress 等遗留系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/emdash-cms/emdash">GitHub - emdash-cms/emdash: EmDash is a full-stack TypeScript CMS based on Astro; the spiritual successor to WordPress · GitHub</a></li>
<li><a href="https://grokipedia.com/page/EmDash_CMS">EmDash (CMS)</a></li>
<li><a href="https://ailinux.me/the-cloudflare-blog-brought-to-you-by-emdash/">The Cloudflare Blog – Brought to you by EmDash - AILinuX</a></li>

</ul>
</details>

**标签**: `#software\_engineering`, `#performance`, `#infrastructure`, `#case\_study`, `#frontend`

---

<a id="item-8"></a>
## [持续学习使主权 AI 能够实现前沿模型](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 9.0/10

一份技术报告展示了在开放权重模型上进行持续学习可以实现前沿级 AI 性能，并推出了 Thomson 这一通过该方法训练的新型通用前沿模型。 这一突破使多样化的机构能够获得前沿 AI 能力，实现 AI 主权，并减少少数资金雄厚的玩家对 AI 领域的垄断。 该方法在训练过程中保持可塑性和稳定性，最小化参数干预，并在能力上显示出π形改进模式，同时消除了遗忘问题。

reddit · r/MachineLearning · /u/Forsaken\_Scientist · 8月25日 18:30

**背景**: 主权 AI 是指一个组织独立构建、部署和管理 AI 的能力，旨在解决 AI 开发中存在的信息、经济和权力不对称问题。持续学习是一种机器学习技术，使模型能够从新数据中持续学习而不会忘记之前学到的知识。

**标签**: `#Continual Learning`, `#SovereignAI`, `#Open-Weight Models`, `#Model Training`, `#AI Sovereignty`

---

<a id="item-9"></a>
## [使用 PostgreSQL、pgvector 和 Qwen3 构建最先进搜索引擎](https://www.reddit.com/r/MachineLearning/comments/1vxyrsr/how_we_built_a_sota_search_engine_using/) ⭐️ 9.0/10

Hugging Face 工程师在 Papers with Code 上实现了一个混合搜索系统，使用 PostgreSQL、pgvector 和 Qwen3-Embedding-0.6B 结合关键词和语义搜索，由 NVIDIA L4 GPU 和 Hugging Face 的 Jobs 与 Buckets 基础设施提供支持。 这种实现展示了混合搜索如何显著提高技术内容的检索准确性，为研究人员和构建 AI 驱动搜索系统的开发者提供了实用范例。 该系统使用 Qwen3-Embedding-0.6B 进行文本嵌入，通过 Hugging Face Inference Endpoints 提供实时模型服务，并在混合排名方法中结合 BM25 关键词评分和向量相似度。

reddit · r/MachineLearning · /u/NielsRogge · 8月25日 20:42

**背景**: pgvector 是一个开源 PostgreSQL 扩展，支持向量相似度搜索，而混合搜索结合了词汇（关键词）和语义（向量）方法以平衡精确度和相关性。Qwen3-Embedding-0.6B 是来自 Qwen3 系列的小型嵌入模型（0.6B 参数），针对效率进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pgvector/pgvector">GitHub - pgvector/pgvector: Open-source vector similarity search for Postgres · GitHub</a></li>
<li><a href="https://www.mongodb.com/resources/products/capabilities/hybrid-search">What Is Hybrid Search ? An In-Depth Guide | MongoDB</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-Embedding-0.6B">Qwen/Qwen3-Embedding-0.6B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#pgvector`, `#Qwen3`, `#Hybrid Search`, `#PostgreSQL`, `#Hugging Face`

---

<a id="item-10"></a>
## [Qwen 预告 8 月 26 日开源 Qwen3.8-Flash-Next](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 9.0/10

Qwen 宣布将于 2026 年 8 月 26 日 23:00（UTC+8）开源 Qwen3.8-Flash-Next 模型，提供标准版和 FP8 版本。 此次发布标志着 Qwen4 架构演进的重要一步，为 AI 生态系统中的开发者和研究人员提供了更高的效率和性能。 该模型基于新一代 Qwen4 架构，将在魔搭社区托管，并支持 FP8，可实现更快的推理和更低的内存使用。

telegram · zaihuapd · 8月25日 20:59

**背景**: 混合专家（MoE）是一种使用多个专业子模型来提高效率的 AI 架构，而 FP8 量化通过将精度降低到 8 位浮点数来实现更快的推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#AI Model`, `#Open Source`, `#MoE`, `#Qwen4`

---

<a id="item-11"></a>
## [长江存储启动 IPO，聚焦 Xtacking 技术冲击全球 NAND 市场](https://news.google.com/rss/articles/CBMiVEFVX3lxTE96ejdHVEd2MURBVDBFanJZVXV4TEFjLXgwOFktNTZFcXB2Z3dkWjlObUpuT05IVUNaUkZhWnpkb3dfZ3JOa3BFQ0lmVXdHdWZNNU54Ug?oc=5) ⭐️ 9.0/10

长江存储（YMTC）已启动 IPO 流程，计划筹集约 330 亿元人民币，以支持其扩张并竞争全球 NAND 闪存市场。 这一举措意义重大，因为长江存储是中国领先的 NAND 闪存制造商，其 IPO 可能会加速其专有 Xtacking 技术的发展和采用，从而可能打破由三星和 SK 海力士主导的全球存储器市场。 此次 IPO 是在上海科创板进行的，长江存储的 Xtacking 技术涉及使用逻辑技术节点在单独的晶圆上处理存储单元阵列和外围电路，以实现高 I/O 速度和密度。

google\_news · 虎嗅 · 8月25日 23:02

**背景**: NAND 闪存是一种非易失性存储器，广泛用于 SSD 和 USB 驱动器，以其高密度著称，但与 NOR 闪存相比，随机访问速度较慢。3D NAND 技术通过垂直堆叠存储单元来增加密度，而长江存储的 Xtacking 是该领域的一项关键创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ymtc.com/en/technicalintroduction.html">About Xtacking®-YMTC</a></li>
<li><a href="https://www.ymtc.com/en/news/41.html">YMTC Xtacking®4.0 Recognized as Most Innovative Technology at ...</a></li>
<li><a href="https://semiengineering.com/how-to-make-3d-nand/">How To Make 3D NAND - Semiconductor Engineering</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#NAND memory`, `#Xtacking technology`, `#IPO`, `#memory chips`

---

<a id="item-12"></a>
## [小米玄戒 O3 行业首发 LPDDR6，核心合作方为长鑫存储](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1oZXlFQk1FR2txdElqZjdvdGlpNTk3RmxXckxqZTJUY2ktOGo2SVUxanM3S25ZaFRTMUJNajR2SGxfTkdrcGFyQXlPd21WaHVrYlhOWHkzQXFjVnYt?oc=5) ⭐️ 9.0/10

小米自研的玄戒 O3 芯片是行业内首个集成 LPDDR6 内存的芯片，核心合作伙伴为长鑫存储。 这一合作凸显了中国在半导体供应链方面的进展，并推动了高性能内存技术在人工智能和移动应用中的发展。 与上一代相比，LPDDR6 提供更高的带宽和效率，支持旗舰设备上的高级人工智能工作负载和多任务处理。

google\_news · 电子工程专辑 · 8月25日 09:32

**背景**: LPDDR6 是低功耗 DRAM 内存的最新标准，专为高性能移动和计算设备设计。长鑫存储是一家中国 DRAM 制造商，专注于移动和企业应用的内存芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxmt.com/en/">ABOUT CXMT - CXMT</a></li>

</ul>
</details>

**标签**: `#LPDDR6`, `#CXMT`, `#Hardware`, `#Memory`, `#AI Accelerator`

---