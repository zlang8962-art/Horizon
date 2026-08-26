---
layout: default
title: "Horizon Summary: 2026-08-26 (EN)"
date: 2026-08-26
content_date: 2026-08-25
lang: en
---

> Coverage: 2026-08-25 (Asia/Shanghai calendar day)

> From 104 items, 12 important content pieces were selected

---

1. [llama.cpp v0.3.0: Multimodal, MTP, and Tensor-Split Updates](#item-1) ⭐️ 10.0/10
2. [llm-anthropic 0.27 updates plugin for Anthropic SDK v1.0.0](#item-2) ⭐️ 10.0/10
3. [NVIDIA Announces Vera Rubin NVL72 and Groq 3 LPX for AI Agents](#item-3) ⭐️ 10.0/10
4. [ONNX Runtime WebGPU Plugin EP 0.3.0 Released](#item-4) ⭐️ 9.0/10
5. [Apple Introduces M6 and M5 Ultra Chips](#item-5) ⭐️ 9.0/10
6. [OpenAI&\#x27;s Jalapeño Chip Outperforms Nvidia&\#x27;s Blackwell](#item-6) ⭐️ 9.0/10
7. [Cloudflare Migrates Blog to Open-Source EmDash CMS](#item-7) ⭐️ 9.0/10
8. [Continual Learning Enables SovereignAI with Frontier Models](#item-8) ⭐️ 9.0/10
9. [Building a State-of-the-Art Search Engine with PostgreSQL, pgvector, and Qwen3](#item-9) ⭐️ 9.0/10
10. [Qwen Announces Open Source Qwen3.8-Flash-Next on August 26](#item-10) ⭐️ 9.0/10
11. [Yangtze Memory Launches IPO, Focusing on Xtacking to Challenge Global NAND Market](#item-11) ⭐️ 9.0/10
12. [Xiaomi Xuanjie O3 Industry-First LPDDR6 Launch with CXMT](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp v0.3.0: Multimodal, MTP, and Tensor-Split Updates](https://github.com/ggml-org/llama.cpp/releases/tag/v0.3.0) ⭐️ 10.0/10

llama.cpp v0.3.0 introduces multimodal support via the dots3-note model with a new DSA-ISWA KV cache, adds Multi-Token Prediction \(MTP\) for GLM-4.5-Air, and implements tensor-split mode \(-sm tensor\) along with fixes for DeepSeek 4. This release significantly expands llama.cpp&\#x27;s compatibility with advanced AI models like GLM-4.5-Air and DeepSeek 4, enabling more efficient multi-GPU inference and multimodal capabilities that are crucial for on-device AI applications. The update includes the DSA-ISWA KV cache for dots3-note, MTP for GLM-4.5-Air, and tensor-split fixes for DeepSeek 4, while ggml is bumped to v0.22.0 with improved Metal kernel parallel compilation and non-in-place clamp operations.

github · github-actions\[bot\] · Aug 25, 18:22

**Background**: llama.cpp is a high-performance C++ inference engine for LLMs, optimized for CPU and GPU. Tensor-split allows distributing model weights across multiple GPUs to handle large models, while MTP \(Multi-Token Prediction\) accelerates inference by predicting multiple tokens at once.

<details><summary>References</summary>
<ul>
<li><a href="https://habr.com/ru/articles/1021832/">KV - Cache в LLM: разбираем инференс через 9 ключевых... / Хабр</a></li>
<li><a href="https://korshunov.ai/en/article/20686-llama-cpp-0-3-0-adds-dots3-note-model-and-tensor-split-for-deepseek-4/">llama.cpp 0.3.0 adds dots3-note model and tensor-split for DeepSeek 4</a></li>
<li><a href="https://glm45.org/">GLM - 4 . 5 - by Zhipu AI</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#Open Source`, `#GPU`, `#Multimodal`

---

<a id="item-2"></a>
## [llm-anthropic 0.27 updates plugin for Anthropic SDK v1.0.0](https://simonwillison.net/2026/Aug/24/llm-anthropic/) ⭐️ 10.0/10

The llm-anthropic plugin version 0.27 updates to support Anthropic&\#x27;s Python SDK v1.0.0, which migrates from httpx to httpx2, similar to OpenAI&\#x27;s recent v3.0.0 update. This update ensures compatibility with the latest Anthropic SDK, allowing developers to continue using the plugin without breaking changes and maintaining access to Claude&\#x27;s API. Anthropic provides a migration guide for upgrading to SDK 1.0, and the plugin&\#x27;s PR \#84 successfully implements these changes to pass tests.

rss · Simon Willison · Aug 25, 00:27

**Background**: The Anthropic Python SDK provides access to the Claude API for Python applications, supporting synchronous/asynchronous operations and integrations with cloud platforms. HTTPX is a modern HTTP client library, and HTTPX 2 builds upon it with enhanced features.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/anthropic-sdk-python">GitHub - anthropics/anthropic-sdk-python</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Anthropic`, `#Python`, `#SDK`, `#Migration`

---

<a id="item-3"></a>
## [NVIDIA Announces Vera Rubin NVL72 and Groq 3 LPX for AI Agents](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/) ⭐️ 10.0/10

NVIDIA has released the first on-chip test data for the Vera Rubin NVL72 rack, showing a 30x throughput increase and 35x cost reduction for DeepSeek-V4-Pro agent coding tasks compared to GB300. The company also announced the production-ready Groq 3 LPX inference accelerator and the Vera CPU, with SpaceX planning to deploy the NVL72 in orbit by 2027. The Vera Rubin NVL72 architecture represents a significant leap in AI compute efficiency, potentially reshaping how data centers handle large-scale AI workloads. The Groq 3 LPX and Vera CPU are designed to optimize inference and agent-based tasks, which are critical for the growing AI agent ecosystem. The NVL72 system combines 72 Rubin GPUs and 36 Vera CPUs in a single NVLink 6 domain, with a total power consumption exceeding 100 kilowatts. The Groq 3 LPX can achieve 3400 tokens per second for Gemma 4 31B, and the system uses passive copper cables for intra-rack NVLink connections.

telegram · zaihuapd · Aug 25, 22:48

**Background**: Vera Rubin is NVIDIA&\#x27;s next-generation data center platform, featuring custom-designed Olympus Arm cores in the Vera CPU and high-bandwidth memory. The NVL72 is a rack-scale system designed for AI inference and training, leveraging NVLink 6 for high-speed interconnects.

<details><summary>References</summary>
<ul>
<li><a href="https://axecompute.com/vera-rubin-the-right-compute-as-you-scale/">Vera Rubin Early Access: The Right Compute as You Scale</a></li>
<li><a href="https://benquan.hk/article-vera-rubin-nvl72.html">NVIDIA Vera Rubin NVL 72 Deep Dive 2026 | BENQUAN Global</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI Hardware`, `#Inference`, `#DeepSeek`, `#Vera Rubin`

---

<a id="item-4"></a>
## [ONNX Runtime WebGPU Plugin EP 0.3.0 Released](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.3.0) ⭐️ 9.0/10

ONNX Runtime WebGPU Plugin EP 0.3.0 adds support for PagedAttention, MRotaryEmbedding, and other operators while improving generative-model performance and configuration reliability. This release expands AI model coverage and enhances generative-model performance, directly impacting AI compute and software development for WebGPU platforms. Key improvements include deferred dispatch for parallel shader compilation, Intel subgroup-matrix MatMul kernels, and expanded integer support across operators.

github · edgchen1 · Aug 25, 05:44

**Background**: ONNX Runtime is an open-source machine learning inference accelerator, and WebGPU is a graphics API that enables high-performance computing on the web.

**Tags**: `#ONNX Runtime`, `#WebGPU`, `#AI Acceleration`, `#Machine Learning`, `#Software Development`

---

<a id="item-5"></a>
## [Apple Introduces M6 and M5 Ultra Chips](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

Apple unveiled the M6 chip in a new Mac mini and the M5 Ultra in a refreshed Mac Studio, marking its first 2nm processor and quad-die architecture. These chips represent a significant leap in performance and AI capabilities, potentially reshaping the landscape for high-performance computing and on-device AI processing. The M5 Ultra uses UltraFusion to connect two dual-die M5 Max chips, achieving over 4.4TB/s inter-die bandwidth, while the M6 features a Dual 16-core Neural Engine for faster AI compute.

hackernews · interpol\_p · Aug 25, 21:01 · [Discussion](https://news.ycombinator.com/item?id=49433292)

**Background**: Apple&\#x27;s M-series chips are known for their energy efficiency and performance, with the UltraFusion technology enabling high-bandwidth connections between multiple dies for enhanced computing power.

<details><summary>References</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in ...</a></li>
<li><a href="https://www.macrumors.com/2026/08/25/apple-debuts-m5-ultra/">Apple Debuts M 5 Ultra as Most Powerful Chip Ever - MacRumors</a></li>
<li><a href="https://9to5mac.com/2026/08/25/apple-launches-next-gen-apple-silicon-chips-m6-and-m5-ultra/">Apple launches next-gen Apple Silicon chips: M6 and M5 Ultra - 9to5Mac</a></li>

</ul>
</details>

**Discussion**: Users are impressed by the performance gains but express concerns about pricing, with one rumor suggesting Apple might skip M6 Pro and Max variants to focus on an M7 chip for AI.

**Tags**: `#Apple`, `#M6`, `#M5 Ultra`, `#AI Compute`, `#Chips`

---

<a id="item-6"></a>
## [OpenAI&\#x27;s Jalapeño Chip Outperforms Nvidia&\#x27;s Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI has unveiled its custom Jalapeño chip, claiming it outperforms Nvidia&\#x27;s Blackwell in benchmark tests. This development highlights the growing trend of companies designing their own AI accelerators to reduce reliance on Nvidia and improve efficiency. The Jalapeño chip is designed for LLM inference, offering higher throughput and lower latency compared to previous generations.

hackernews · Semianalysis · Aug 25, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49434378)

**Background**: OpenAI and Broadcom announced a strategic collaboration to deploy 10 gigawatts of custom AI accelerators, including Jalapeño, by 2029. The chip is part of OpenAI&\#x27;s full-stack approach to AI systems, integrating models, chips, and memory for optimized performance.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/08/25/openais-jalapeno-chip-is-built-for-fast-inference-at-scale-benchmarks-show/">OpenAI’s Jalapeño chip is built for fast inference at scale, benchmarks show | TechCrunch</a></li>

</ul>
</details>

**Discussion**: Community discussions focus on the chip&\#x27;s FP4 precision, die size, and efficiency compared to human speech, with some noting its potential for baking LLM weights directly into hardware.

**Tags**: `#AI compute`, `#chips hardware`, `#inference chips`, `#OpenAI`, `#Nvidia`

---

<a id="item-7"></a>
## [Cloudflare Migrates Blog to Open-Source EmDash CMS](https://blog.cloudflare.com/cloudflare-blog-uses-emdash/) ⭐️ 9.0/10

Cloudflare has migrated its official blog to EmDash, a new open-source CMS built on TypeScript and Astro, to validate its performance at massive scale. This migration demonstrates Cloudflare&\#x27;s commitment to open-source tools and provides a real-world case study for developers interested in modern CMS architectures and serverless workflows. The blog underwent performance stress-testing, production traffic routing, and a frontend redesign to ensure reliability and scalability.

rss · Cloudflare Blog · Aug 25, 03:00

**Background**: EmDash is a full-stack TypeScript CMS designed as a spiritual successor to WordPress, focusing on security, type safety, and AI-agent-first workflows. It runs on Cloudflare&\#x27;s infrastructure and aims to replace legacy systems like WordPress by addressing plugin vulnerabilities and enabling serverless deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/emdash-cms/emdash">GitHub - emdash-cms/emdash: EmDash is a full-stack TypeScript CMS based on Astro; the spiritual successor to WordPress · GitHub</a></li>
<li><a href="https://grokipedia.com/page/EmDash_CMS">EmDash (CMS)</a></li>
<li><a href="https://ailinux.me/the-cloudflare-blog-brought-to-you-by-emdash/">The Cloudflare Blog – Brought to you by EmDash - AILinuX</a></li>

</ul>
</details>

**Tags**: `#software\_engineering`, `#performance`, `#infrastructure`, `#case\_study`, `#frontend`

---

<a id="item-8"></a>
## [Continual Learning Enables SovereignAI with Frontier Models](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 9.0/10

A technical report demonstrates that continual learning on open-weight models can achieve frontier-level AI performance, introducing Thomson, a new general-purpose frontier model trained with this approach. This breakthrough democratizes access to frontier AI capabilities, enabling diverse institutions to achieve AI sovereignty and reducing the dominance of a few heavily funded players. The approach preserves plasticity and stability during training, minimizes parameter interventions, and shows a π-shaped improvement pattern across capabilities while eliminating the forgetting problem.

reddit · r/MachineLearning · /u/Forsaken\_Scientist · Aug 25, 18:30

**Background**: SovereignAI refers to an organization&\#x27;s ability to independently build, deploy, and govern AI, addressing concerns about information, economic, and power asymmetry in AI development. Continual learning is a machine learning technique that enables models to learn continuously from new data without forgetting previously learned knowledge.

**Tags**: `#Continual Learning`, `#SovereignAI`, `#Open-Weight Models`, `#Model Training`, `#AI Sovereignty`

---

<a id="item-9"></a>
## [Building a State-of-the-Art Search Engine with PostgreSQL, pgvector, and Qwen3](https://www.reddit.com/r/MachineLearning/comments/1vxyrsr/how_we_built_a_sota_search_engine_using/) ⭐️ 9.0/10

Hugging Face engineers implemented a hybrid search system on Papers with Code that combines keyword and semantic search using PostgreSQL, pgvector, and Qwen3-Embedding-0.6B, powered by NVIDIA L4 GPUs and Hugging Face&\#x27;s Jobs and Buckets infrastructure. This implementation demonstrates how hybrid search can significantly improve retrieval accuracy for technical content, setting a practical example for researchers and developers building AI-powered search systems. The system uses Qwen3-Embedding-0.6B for text embeddings, Hugging Face Inference Endpoints for live model serving, and combines BM25 keyword scoring with vector similarity in a hybrid ranking approach.

reddit · r/MachineLearning · /u/NielsRogge · Aug 25, 20:42

**Background**: pgvector is an open-source PostgreSQL extension that enables vector similarity search, while hybrid search combines lexical \(keyword\) and semantic \(vector\) approaches to balance precision and relevance. Qwen3-Embedding-0.6B is a small embedding model \(0.6B parameters\) from the Qwen3 series optimized for efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pgvector/pgvector">GitHub - pgvector/pgvector: Open-source vector similarity search for Postgres · GitHub</a></li>
<li><a href="https://www.mongodb.com/resources/products/capabilities/hybrid-search">What Is Hybrid Search ? An In-Depth Guide | MongoDB</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3-Embedding-0.6B">Qwen/Qwen3-Embedding-0.6B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#pgvector`, `#Qwen3`, `#Hybrid Search`, `#PostgreSQL`, `#Hugging Face`

---

<a id="item-10"></a>
## [Qwen Announces Open Source Qwen3.8-Flash-Next on August 26](https://www.modelscope.cn/models/Qwen/Qwen3.8-Flash-Next) ⭐️ 9.0/10

Qwen has announced the upcoming open-source release of the Qwen3.8-Flash-Next model, scheduled for August 26, 2026, at 23:00 UTC+8, with both standard and FP8 versions available. This release marks a significant step in the Qwen4 architecture evolution, offering improved efficiency and performance for developers and researchers in the AI ecosystem. The model is based on the next-generation Qwen4 architecture and will be hosted on the ModelScope community, with FP8 support enabling faster inference and lower memory usage.

telegram · zaihuapd · Aug 25, 20:59

**Background**: Mixture of Experts \(MoE\) is an AI architecture that uses multiple specialized submodels to improve efficiency, while FP8 quantization reduces precision to 8-bit floating-point for faster inference.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#Qwen`, `#AI Model`, `#Open Source`, `#MoE`, `#Qwen4`

---

<a id="item-11"></a>
## [Yangtze Memory Launches IPO, Focusing on Xtacking to Challenge Global NAND Market](https://news.google.com/rss/articles/CBMiVEFVX3lxTE96ejdHVEd2MURBVDBFanJZVXV4TEFjLXgwOFktNTZFcXB2Z3dkWjlObUpuT05IVUNaUkZhWnpkb3dfZ3JOa3BFQ0lmVXdHdWZNNU54Ug?oc=5) ⭐️ 9.0/10

Yangtze Memory \(YMTC\) has initiated its IPO process, aiming to raise approximately 33 billion RMB to fund its expansion and compete in the global NAND flash memory market. This move is significant as YMTC is a leading Chinese manufacturer of NAND flash memory, and its IPO could accelerate the development and adoption of its proprietary Xtacking technology, potentially disrupting the global memory market dominated by Samsung and SK Hynix. The IPO is for the Shanghai STAR Market \(科创板\), and YMTC&\#x27;s Xtacking technology involves processing memory cell arrays and peripheral circuits on separate wafers using logic technology nodes to achieve high I/O speed and density.

google\_news · 虎嗅 · Aug 25, 23:02

**Background**: NAND flash memory is a type of non-volatile memory widely used in SSDs and USB drives, known for high density but slower random access compared to NOR flash. 3D NAND technology stacks memory cells vertically to increase density, with YMTC&\#x27;s Xtacking being a key innovation in this field.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ymtc.com/en/technicalintroduction.html">About Xtacking®-YMTC</a></li>
<li><a href="https://www.ymtc.com/en/news/41.html">YMTC Xtacking®4.0 Recognized as Most Innovative Technology at ...</a></li>
<li><a href="https://semiengineering.com/how-to-make-3d-nand/">How To Make 3D NAND - Semiconductor Engineering</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#NAND memory`, `#Xtacking technology`, `#IPO`, `#memory chips`

---

<a id="item-12"></a>
## [Xiaomi Xuanjie O3 Industry-First LPDDR6 Launch with CXMT](https://news.google.com/rss/articles/CBMiXEFVX3lxTE1oZXlFQk1FR2txdElqZjdvdGlpNTk3RmxXckxqZTJUY2ktOGo2SVUxanM3S25ZaFRTMUJNajR2SGxfTkdrcGFyQXlPd21WaHVrYlhOWHkzQXFjVnYt?oc=5) ⭐️ 9.0/10

Xiaomi&\#x27;s self-developed Xuanjie O3 chip is the first in the industry to integrate LPDDR6 memory, with ChangXin Memory Technologies \(CXMT\) as the core partner. This partnership highlights China&\#x27;s progress in semiconductor supply chains and advances high-performance memory technology for AI and mobile applications. LPDDR6 offers higher bandwidth and efficiency compared to previous generations, supporting advanced AI workloads and multitasking on flagship devices.

google\_news · 电子工程专辑 · Aug 25, 09:32

**Background**: LPDDR6 is the latest standard in low-power DRAM memory, designed for high-performance mobile and computing devices. CXMT is a Chinese DRAM manufacturer specializing in memory chips for mobile and enterprise applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cxmt.com/en/">ABOUT CXMT - CXMT</a></li>

</ul>
</details>

**Tags**: `#LPDDR6`, `#CXMT`, `#Hardware`, `#Memory`, `#AI Accelerator`

---