---
layout: default
title: "Horizon Summary: 2026-09-03 (EN)"
date: 2026-09-03
content_date: 2026-09-02
lang: en
---

> Coverage: 2026-09-02 (Asia/Shanghai calendar day)

> From 77 items, 12 important content pieces were selected

---

1. [llama.cpp Release b10759: KleidiAI Fix and Cross-Platform Binaries](#item-1) ⭐️ 10.0/10
2. [llama.cpp Release b10758 Optimizes Hexagon DSP](#item-2) ⭐️ 10.0/10
3. [Introducing agentic video understanding with Gemini](#item-3) ⭐️ 10.0/10
4. [ollama/ollama released v0.33.3-rc2](#item-4) ⭐️ 9.0/10
5. [GeoJSON Map Viewer](#item-5) ⭐️ 9.0/10
6. [South Korea&\#x27;s Trillion-Dollar Sovereign AI Investment](#item-6) ⭐️ 9.0/10
7. [Detailed explanation of how to create a text-to-image model from scratch. \[R\]](#item-7) ⭐️ 9.0/10
8. [♻️ 英伟达 129 亿美元收购 Hugging Face，将掌控最大开源 AI 平台](#item-8) ⭐️ 9.0/10
9. [Nexus 暗网兜售 1.53 亿张驾照扫描件，FBI 已介入调查](#item-9) ⭐️ 9.0/10
10. [CXMT Refuses Apple&\#x27;s Price Cuts, Maintaining Parity with Samsung and SK Hynix](#item-10) ⭐️ 9.0/10
11. [CITIC Securities Bullish on China&\#x27;s Domestic Semiconductor Equipment Chain](#item-11) ⭐️ 9.0/10
12. [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp Release b10759: KleidiAI Fix and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10759) ⭐️ 10.0/10

llama.cpp version b10759 addresses a buffer type initialization issue with KleidiAI and provides pre-compiled binaries for macOS, iOS, Linux, Android, and Windows. This release is significant for developers and users relying on Apple Silicon and ARM-based devices, as it ensures stable performance and broadens the accessibility of local LLM inference across diverse operating systems. The KleidiAI buffer type fix prevents potential initialization errors, while the release includes disabled builds for macOS Apple Silicon with KleidiAI enabled and supports multiple backends like CUDA, Vulkan, and ROCm.

github · github-actions\[bot\] · Sep 2, 18:22

**Background**: llama.cpp is a widely used open-source library for running large language models locally, often serving as the core for tools like Ollama and LM Studio. KleidiAI is an ARM-based acceleration framework that optimizes inference on devices like phones and Raspberry Pi.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/ kleidiai : This repository is a read-only mirror of...</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#Apple Silicon`, `#KleidiAI`, `#Software Release`

---

<a id="item-2"></a>
## [llama.cpp Release b10758 Optimizes Hexagon DSP](https://github.com/ggml-org/llama.cpp/releases/tag/b10758) ⭐️ 10.0/10

llama.cpp version b10758 introduces matmul fusion and memory management fixes specifically for Hexagon DSP acceleration. This release significantly improves performance and stability for LLM inference on Qualcomm Snapdragon devices, expanding the hardware support for efficient local AI. Key improvements include fusing QKV and FFN matmuls, removing hardcoded dimension restrictions, and adding Virtual Address \(VA\) space defragmentation to prevent fragmentation issues.

github · github-actions\[bot\] · Sep 2, 17:29

**Background**: Qualcomm Hexagon DSP is a specialized micro-architecture designed for high-performance signal processing and AI workloads, often used in mobile devices. The Hexagon NPU \(Neural Processing Unit\) is a dedicated hardware accelerator for these tasks. llama.cpp is a high-performance C++ library for running Large Language Models \(LLMs\) on various hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qualcomm_Hexagon">Qualcomm Hexagon - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/8273">Performance of llama.cpp on Snapdragon X Elite/Plus · ggml-org/llama.cpp · Discussion #8273</a></li>
<li><a href="https://docs.qualcomm.com/bundle/publicresource/topics/80-N2040-61/memory.html">Memory - Hexagon V79 HVX Programmer Reference Manual</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI inference`, `#Hexagon DSP`, `#C++ optimization`, `#GPU acceleration`

---

<a id="item-3"></a>
## [Introducing agentic video understanding with Gemini](https://deepmind.google/blog/introducing-agentic-video-in-gemini/) ⭐️ 10.0/10

Google DeepMind introduces a new agentic video understanding model within Gemini, demonstrating advanced capabilities in processing and reasoning about video content.

rss · Google DeepMind News · Sep 2, 01:08

**Tags**: `#AI`, `#Video Understanding`, `#Gemini`, `#Agentic AI`, `#Google DeepMind`

---

<a id="item-4"></a>
## [ollama/ollama released v0.33.3-rc2](https://github.com/ollama/ollama/releases/tag/v0.33.3-rc2) ⭐️ 9.0/10

Ollama v0.33.3-rc2 introduces AI model optimizations and updates to MLX/llama.cpp, with a new contributor.

github · github-actions\[bot\] · Sep 2, 08:11

**Tags**: `#AI`, `#Ollama`, `#MLX`, `#llama.cpp`, `#Software Release`

---

<a id="item-5"></a>
## [GeoJSON Map Viewer](https://simonwillison.net/2026/Sep/1/geojson/) ⭐️ 9.0/10

Simon Willison shares a GeoJSON Map Viewer tool built with AI assistance to visualize and export map data.

rss · Simon Willison · Sep 2, 02:05

**Tags**: `#GeoJSON`, `#Web Tools`, `#Data Visualization`, `#Developer Tools`, `#AI-Assisted Development`

---

<a id="item-6"></a>
## [South Korea&\#x27;s Trillion-Dollar Sovereign AI Investment](https://newsletter.semianalysis.com/p/koreas-trillion-dollar-sovereign) ⭐️ 9.0/10

South Korea is launching a massive sovereign AI investment program, with Nvidia emerging as a key beneficiary while Hynix faces challenges in this strategic initiative. This investment highlights the critical role of sovereign AI strategies in national security and economic competitiveness, particularly in the semiconductor and AI infrastructure sectors. The program includes a national AI tournament and emphasizes open-source models, which could reshape the competitive landscape for AI infrastructure providers.

rss · Semianalysis · Sep 2, 04:14

**Background**: Sovereign AI refers to a nation&\#x27;s ability to develop and deploy AI systems independently, often driven by strategic interests in national security and economic growth. South Korea, a global leader in semiconductor manufacturing, is leveraging its strengths to build a robust AI ecosystem.

**Tags**: `#AI Infrastructure`, `#Semiconductors`, `#Sovereign AI`, `#Open Source`, `#Hardware`

---

<a id="item-7"></a>
## [Detailed explanation of how to create a text-to-image model from scratch. \[R\]](https://www.reddit.com/r/MachineLearning/comments/1w5c9rd/detailed_explanation_of_how_to_create_a/) ⭐️ 9.0/10

A detailed cookbook and codebase for building a text-to-image model from scratch, including a dataset and tools.

reddit · r/MachineLearning · /u/dh7net · Sep 2, 22:40

**Tags**: `#text-to-image`, `#machine-learning`, `#open-source`, `#deep-learning`, `#reproducibility`

---

<a id="item-8"></a>
## [♻️ 英伟达 129 亿美元收购 Hugging Face，将掌控最大开源 AI 平台](https://www.techzine.eu/news/analytics/143877/nvidia-to-acquire-hugging-face-for-12-9-billion/) ⭐️ 9.0/10

NVIDIA is acquiring Hugging Face for $12.9 billion to gain control of the world&\#x27;s largest open-source AI platform.

telegram · zaihuapd · Sep 2, 14:50

**Tags**: `#AI`, `#NVIDIA`, `#Hugging Face`, `#Open Source`, `#Acquisition`

---

<a id="item-9"></a>
## [Nexus 暗网兜售 1.53 亿张驾照扫描件，FBI 已介入调查](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 9.0/10

The FBI is investigating a dark web service called Nexus that is selling over 153 million scanned driver&\#x27;s licenses.

telegram · zaihuapd · Sep 2, 17:31

**Tags**: `#data\_breach`, `#identity\_theft`, `#dark\_web`, `#privacy`, `#cybersecurity`

---

<a id="item-10"></a>
## [CXMT Refuses Apple&\#x27;s Price Cuts, Maintaining Parity with Samsung and SK Hynix](https://news.google.com/rss/articles/CBMickFVX3lxTE5uWVlNeVhudklNQjN4MXNpQldzZlZ4djJ4bTdLaF9YdjMtVzhEX3ppbTNmLUdWLVRJb1hKOWRab2VLRGdJUVg4bFZ0YnptV2tFVUFIS1Q5MGx0eEY2YnFUUXBhSkZocW9OOVhJUDRRX21CZw?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies \(CXMT\) has refused Apple&\#x27;s demands for price reductions, maintaining pricing parity with major competitors Samsung and SK Hynix. This stance highlights the growing confidence of Chinese memory manufacturers in their market position and could signal a shift in global memory pricing dynamics. The news specifically mentions CXMT&\#x27;s decision to maintain pricing levels that are not lower than those of Samsung and SK Hynix in response to Apple&\#x27;s requests.

google\_news · 新浪网 · Sep 2, 21:31

**Tags**: `#semiconductors`, `#memory`, `#CXMT`, `#pricing`, `#Apple`

---

<a id="item-11"></a>
## [CITIC Securities Bullish on China&\#x27;s Domestic Semiconductor Equipment Chain](https://news.google.com/rss/articles/CBMijAFBVV95cUxNb3htSFlCOUc3YUhpa3pqMzlGUC10RTM1dnNyRzA3cmFCVGtrTFV2LXQyVklXaVRSWTlrejB6cUMzbU5pWDNzX3JmcDdCVnluNDFwRmtxU0hwTFYxWjJhSEo5eEFuc3FVOHpfNWEzand2MDNlOVlibDN0RXFkemt5QWg4YTZkWTN0UUhBUA?oc=5) ⭐️ 9.0/10

CITIC Securities has published a market outlook reiterating its strong conviction in the continued growth and development of China&\#x27;s domestic semiconductor equipment and core component supply chains. This endorsement from a major financial institution is significant as it signals confidence in the strategic importance of domestic hardware capabilities for China&\#x27;s technological self-reliance and AI infrastructure development. The analysis focuses on the entire industrial chain, including upstream equipment and downstream core components, highlighting the critical role of this sector in supporting broader semiconductor manufacturing and AI accelerator production.

google\_news · Sohu · Sep 2, 14:38

**Background**: The semiconductor equipment industry is a cornerstone of the global tech ecosystem, providing the essential machinery and tools required for fabricating integrated circuits and advanced AI hardware. China has been aggressively investing in this sector to reduce its reliance on foreign suppliers and build a self-sufficient supply chain for its burgeoning AI and consumer electronics markets.

**Tags**: `#semiconductors`, `#AI hardware`, `#market analysis`, `#China tech`, `#supply chain`

---

<a id="item-12"></a>
## [Three sites made 215,128 “best software” pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

An investigation reveals how three sites created 215,128 AI-recommended pages, with Perplexity citing them, highlighting issues with LLM-generated content.

hackernews · jakobgreenfeld · Sep 2, 21:59 · [Discussion](https://news.ycombinator.com/item?id=49536375)

**Tags**: `#AI`, `#LLMs`, `#Perplexity`, `#Search Engines`, `#Data Safety`

---