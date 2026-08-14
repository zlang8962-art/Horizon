---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
content_date: 2026-08-13
lang: en
---

> Coverage: 2026-08-13 (Asia/Shanghai calendar day)

> From 100 items, 12 important content pieces were selected

---

1. [DeepSeek V4 Pro 0813 Model Weights Released on Hugging Face](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10410](#item-2) ⭐️ 9.0/10
3. [llama.cpp b10405: HIP FP Fixes and Cross-Platform Binaries](#item-3) ⭐️ 9.0/10
4. [ollama/ollama released v0.32.10](#item-4) ⭐️ 9.0/10
5. [DeepSeek Harness: Developer Preview of AI Agent Framework](#item-5) ⭐️ 9.0/10
6. [Spaghettifying DRAM: Novel Memory Subsystem Attack](#item-6) ⭐️ 9.0/10
7. [Simon Willison releases alchemy-utils 0.1a1](#item-7) ⭐️ 9.0/10
8. [Cloudflare Certificate Transparency Monitoring Now Generally Available](#item-8) ⭐️ 9.0/10
9. [City2Graph: Python Library for Urban Heterogeneous Graphs](#item-9) ⭐️ 9.0/10
10. [DeepMind&\#x27;s SL2T Model Brings Sign Language Translation to Pixel 11 Keyboard](#item-10) ⭐️ 9.0/10
11. [DeepSeek-V4-Pro Officially Released with Peak/Off-Peak API Pricing](#item-11) ⭐️ 9.0/10
12. [Yangtze Memory Ranks Third Globally in Market Share](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Pro 0813 Model Weights Released on Hugging Face](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 10.0/10

DeepSeek V4 Pro 0813 model weights are now available on Hugging Face, following its initial API-only release via OpenRouter. This release allows developers to run the model locally, fostering broader adoption and experimentation beyond API access. The model contains 1.7T parameters and requires 893 GB of storage, with notable differences in visual outputs across reasoning levels.

rss · Simon Willison · Aug 13, 07:59

**Background**: DeepSeek is a Chinese AI company known for cost-effective, open-weight large language models like DeepSeek-R1. The company has previously released models under open-source licenses, enabling community-driven development.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/docs/quickstart">OpenRouter Quickstart Guide</a></li>
<li><a href="https://openrouter.ai/openrouter">OpenRouter API and Models | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#Model Release`, `#Weights`, `#API`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10410](https://github.com/ggml-org/llama.cpp/releases/tag/b10410) ⭐️ 9.0/10

llama.cpp release b10410 adds SYCL fp16 promotion and provides binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Aug 13, 23:52

**Tags**: `#llama.cpp`, `#open-source`, `#AI-inference`, `#SYCL`, `#GPU-acceleration`

---

<a id="item-3"></a>
## [llama.cpp b10405: HIP FP Fixes and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10405) ⭐️ 9.0/10

llama.cpp version b10405 removes unsafe floating-point optimizations for HIP builds to ensure IEEE 754 compliance and introduces pre-compiled binaries for macOS, iOS, Linux, Android, and Windows. This release is critical for developers using AMD GPUs, as the IEEE-conformant fixes prevent divergent behavior in speculative decoding on RDNA3.5 hardware, ensuring reproducible and numerically safe inference across platforms. The update disables KleidiAI support for macOS Apple Silicon and ROCm 7.14 builds, while offering extensive options including Vulkan, OpenVINO, SYCL, and CUDA 12/13 for Linux and Windows.

github · github-actions\[bot\] · Aug 13, 15:32

**Background**: llama.cpp is a high-performance C++ library for running Large Language Models \(LLMs\) on consumer hardware. HIP is AMD&\#x27;s API for GPU programming, and IEEE 754 is the standard for floating-point arithmetic that ensures consistent numerical results across different hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html">Low precision floating point types — HIP 7.14.60850 Documentation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#llama.cpp`, `#GPU`, `#macOS`, `#Linux`

---

<a id="item-4"></a>
## [ollama/ollama released v0.32.10](https://github.com/ollama/ollama/releases/tag/v0.32.10) ⭐️ 9.0/10

Ollama v0.32.10 release includes performance optimizations, bug fixes, and a new contributor.

github · github-actions\[bot\] · Aug 13, 06:36

**Tags**: `#ollama`, `#machine-learning`, `#software-release`, `#performance`, `#bug-fix`

---

<a id="item-5"></a>
## [DeepSeek Harness: Developer Preview of AI Agent Framework](https://deepseek.com/harness/en/) ⭐️ 9.0/10

DeepSeek Harness is now available as a developer preview, an open-source AI agent framework that enables traceable model execution and dynamic plugin capabilities. This framework addresses critical needs in AI compute and software building by providing tools for model training, inference, and agent workflows, offering practical value through features like traceability and hot-reload. The framework uses an architecture where everything is a plugin, supports an append-only session log for recording all model interactions, and is currently released under the MIT license with expected rough edges.

hackernews · bjin · Aug 13, 20:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**Background**: AI agent frameworks are tools that help developers build autonomous AI systems capable of executing complex tasks. DeepSeek Harness is part of the broader trend of open-source tools for AI development, focusing on improving transparency and flexibility in agent workflows.

**Discussion**: The developer preview has received positive feedback for its traceability features, with users noting that it allows inspection of all model interactions, unlike some US models that encrypt traces. Some users expressed concerns about plugin fatigue, while others highlighted its use of the Cordis v4 system for dynamic plugin management.

**Tags**: `#AI`, `#Agent Framework`, `#Developer Tools`, `#Open Source`, `#DeepSeek`

---

<a id="item-6"></a>
## [Spaghettifying DRAM: Novel Memory Subsystem Attack](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

Researchers have introduced a novel DRAM attack called &\#x27;Spaghettifying DRAM&\#x27; that exploits vulnerabilities in the memory subsystem to gain significant control over system memory. This attack demonstrates how deeply interconnected DRAM controllers and memory subsystems are, revealing critical security implications for modern computing hardware. The attack targets AMD Jaguar architecture from 2013 and requires ring-0 access, with limited information on its applicability to newer CPU families like Zen 3.

hackernews · matt\_d · Aug 13, 22:17 · [Discussion](https://news.ycombinator.com/item?id=49286341)

**Background**: DRAM \(Dynamic Random Access Memory\) is a volatile memory type used in computers for storing data temporarily. The memory subsystem includes the DRAM controller, which manages data transfer between the CPU and memory, and is often complex due to proprietary firmware and refresh requirements.

**Discussion**: Community members express excitement about the accompanying Black Hat talk by Christopher Domas, while others discuss the increasing complexity of DRAM and the potential impact on gaming consoles like Xbox and PlayStation.

**Tags**: `#DRAM`, `#security`, `#hardware`, `#attack`, `#AMD`

---

<a id="item-7"></a>
## [Simon Willison releases alchemy-utils 0.1a1](https://simonwillison.net/2026/Aug/13/alchemy-utils/) ⭐️ 9.0/10

Simon Willison has released alchemy-utils 0.1a1, a Python library that provides performance optimizations for DuckDB exports and CSV imports. This release is significant for data professionals and developers who work with large datasets, as it improves the efficiency of common data manipulation tasks. The library focuses on optimizing the performance of DuckDB exports and CSV imports, which are critical operations in data workflows.

rss · Simon Willison · Aug 13, 11:03

**Background**: DuckDB is an in-process SQL OLAP database management system designed for analytical workloads, while CSV \(Comma Separated Values\) is a widely used file format for storing tabular data. Python&\#x27;s built-in csv module provides basic functionality for reading and writing CSV files, but performance can be a bottleneck for large datasets.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/docs/current/guides/performance/overview">Performance Guide – DuckDB</a></li>
<li><a href="https://duckdb.org/docs/lts/guides/performance/how_to_tune_workloads">Tuning Workloads – DuckDB</a></li>

</ul>
</details>

**Tags**: `#python`, `#duckdb`, `#csv`, `#performance`, `#open-source`

---

<a id="item-8"></a>
## [Cloudflare Certificate Transparency Monitoring Now Generally Available](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/) ⭐️ 9.0/10

Cloudflare has announced the general availability of Certificate Transparency Monitoring, which removes routine emails about certificates issued for your domain. This change simplifies security alert management by ensuring that only non-routine certificate events trigger notifications, helping administrators focus on genuine threats. The feature is an opt-in tool that allows domain owners to double-check SSL/TLS certificates issued for their domains, improving security oversight without overwhelming users with noise.

rss · Cloudflare Blog · Aug 13, 21:00

**Background**: Certificate Transparency \(CT\) is an Internet security standard that requires Certificate Authorities to submit newly issued certificates to public, tamper-evident logs, enabling domain owners to monitor and audit certificate issuance.

<details><summary>References</summary>
<ul>
<li><a href="https://certificate.transparency.dev/">Certificate Transparency : Certificate Transparency</a></li>
<li><a href="https://cloudflare-docs-7ou.pages.dev/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">Certificate Transparency Monitoring · Cloudflare SSL/TLS docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_Transparency">Certificate Transparency - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#certificate-transparency`, `#tls`, `#monitoring`, `#cloudflare`

---

<a id="item-9"></a>
## [City2Graph: Python Library for Urban Heterogeneous Graphs](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 9.0/10

City2Graph is a new Python library that converts geospatial data into analysis-ready heterogeneous graphs for GeoAI and urban spatial analysis, with a paper published in Computers, Environment and Urban Systems. This library bridges the gap between urban data and graph neural networks, enabling more sophisticated spatial analysis and GeoAI applications that were previously difficult to implement. It supports morphological graphs from OpenStreetMap/Overture Maps, transit data via DuckDB, mobility flows, and various proximity metrics, with seamless integration into PyTorch Geometric.

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · Aug 13, 19:59

**Background**: Heterogeneous graphs are networks with multiple node and edge types, commonly used in recommendation systems and social networks. PyTorch Geometric is a popular library for building graph neural networks. Delaunay triangulation is a geometric technique used to create meshes from point data, often applied in urban analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tobilg/duckdb-gtfs">GitHub - tobilg/ duckdb - gtfs : Loading and analyzing GTFS Schedule...</a></li>
<li><a href="https://pytorch-geometric.readthedocs.io/en/latest/notes/heterogeneous.html">Heterogeneous Graph Learning — pytorch_geometric documentation</a></li>
<li><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218877">A formal model of neighborhood representation and applications in urban building aggregation supported by Delaunay triangulation | PLOS One</a></li>

</ul>
</details>

**Tags**: `#GeoAI`, `#Graph Neural Networks`, `#Python Library`, `#Urban Systems`, `#Spatial Analysis`

---

<a id="item-10"></a>
## [DeepMind&\#x27;s SL2T Model Brings Sign Language Translation to Pixel 11 Keyboard](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 9.0/10

DeepMind has released the SL2T model, a large-scale multilingual sign language-to-text system, and integrated it into Pixel 11 devices via Gboard and Live Transcribe for real-time American Sign Language \(ASL\) translation. This breakthrough addresses a significant accessibility gap by enabling real-time communication for the Deaf and hard of hearing community, marking the first time sign language AI has reached mainstream consumer hardware. Trained on over 100,000 hours of data from 50+ sign languages, SL2T achieves a 70 BLEURT score on the FLEURS-ASL benchmark and uses privacy-focused pose estimation to process only hand and body keypoints without raw video.

telegram · zaihuapd · Aug 13, 16:55

**Background**: While spoken language AI tools like dictation and translation have become mainstream, the world&\#x27;s 200+ sign languages used by 70 million people have been largely underserved by technology until now.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://en.cryptonomist.ch/2026/08/13/sign-language-ai-translation-slt2/">Sign Language AI Translation: Google&#x27;s Breakthrough with SL2T ...</a></li>
<li><a href="https://www.unite.ai/google-deepmind-brings-sign-language-translation-to-phones-with-sl2t/">Google DeepMind Brings Sign Language Translation to Phones ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Sign Language`, `#Privacy`, `#Mobile`, `#DeepMind`

---

<a id="item-11"></a>
## [DeepSeek-V4-Pro Officially Released with Peak/Off-Peak API Pricing](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 9.0/10

DeepSeek-V4-Pro is officially released for APP, web, and API with enhanced agent capabilities and native Responses API support. The API introduces peak/off-peak pricing effective August 17, 2026, with off-peak rates at half the peak price. This release significantly impacts AI developers by offering cost-efficient pricing models and advanced agent capabilities, potentially accelerating the adoption of agentic workflows in software development. The model supports three thinking modes \(low, high, max\) and is compatible with Codex. DeepSeek also released Harness, an MIT-licensed open-source agent framework with plugin-based architecture driven by the Cordis meta-framework.

telegram · zaihuapd · Aug 13, 19:12

**Background**: DeepSeek is an AI research company known for developing large language models. The Cordis framework is a meta-framework for spatiotemporal composability used to build modular agent systems. The Responses API is a standard format for AI agent interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/11027/deepseek-harness-mit-claude-code-rival">DeepSeek Harness v0.1: Open-Source MIT Rival to Claude Code</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DeepSeek`, `#API`, `#Pricing`, `#Model Release`

---

<a id="item-12"></a>
## [Yangtze Memory Ranks Third Globally in Market Share](https://news.google.com/rss/articles/CBMickFVX3lxTE1IRTNLRE42azI1TWFaWDdEbTRudEtHd1RaMFBxZlp2QXpGUGloeTZ0U2tvcFpRRXo2MGpzWmdnQ0NMSEtxVEtjZkF4RzdIRU4xSjVXbngzVkJ2OUdySmRTUkZjamZFbFNwNS1WYlZSd2pvdw?oc=5) ⭐️ 9.0/10

Yangtze Memory Technologies has achieved a historic milestone by securing the third position in global market share for NAND flash memory. This achievement marks a significant step in China&\#x27;s semiconductor self-reliance strategy, reducing dependency on foreign suppliers and strengthening the domestic supply chain. The company&\#x27;s success highlights the growing competitiveness of Chinese memory manufacturers in the global market.

google\_news · 央广网 · Aug 13, 18:57

**Background**: Yangtze Memory Technologies is a leading Chinese semiconductor company specializing in NAND flash memory production. The global NAND flash market is dominated by South Korean and Japanese firms, but Chinese companies have been rapidly gaining ground in recent years.

**Tags**: `#semiconductors`, `#memory`, `#China`, `#AI hardware`, `#industry analysis`

---