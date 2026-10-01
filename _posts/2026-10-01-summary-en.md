---
layout: default
title: "Horizon Summary: 2026-10-01 (EN)"
date: 2026-10-01
content_date: 2026-09-30
lang: en
---

> Coverage: 2026-09-30 (Asia/Shanghai calendar day)

> From 71 items, 7 important content pieces were selected

---

1. [ggml-org/llama.cpp released b11280](#item-1) ⭐️ 10.0/10
2. [Ollama v0.35.1-rc0: Web Search, MLX, and llama.cpp Updates](#item-2) ⭐️ 9.0/10
3. [GPT-6.1 Sol: Near-Astra intelligence for a fifth of the price](#item-3) ⭐️ 9.0/10
4. [Photo Scrubber: Local AI Face Blur &amp; Metadata Removal Tool](#item-4) ⭐️ 9.0/10
5. [DeepMind Introduces SynthID Bio for AI-Generated Proteins](#item-5) ⭐️ 9.0/10
6. [Cloudflare AI Gateway Auto Router Reduces AI Costs](#item-6) ⭐️ 9.0/10
7. [Massive Capital Outflow from CXMT, a DRAM Giant](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11280](https://github.com/ggml-org/llama.cpp/releases/tag/b11280) ⭐️ 10.0/10

llama.cpp release b11280 adds SYC L tensor allreduce optimizations and provides cross-platform binaries for AI inference.

github · github-actions\[bot\] · Sep 30, 19:27

**Tags**: `#llama.cpp`, `#AI inference`, `#C++`, `#SYCL`, `#open-source`

---

<a id="item-2"></a>
## [Ollama v0.35.1-rc0: Web Search, MLX, and llama.cpp Updates](https://github.com/ollama/ollama/releases/tag/v0.35.1-rc0) ⭐️ 9.0/10

Ollama v0.35.1-rc0 introduces web search support, bumping MLX and llama.cpp versions, and adds explicit model capabilities. This update enhances Ollama&\#x27;s functionality by enabling web search and improving performance with newer MLX and llama.cpp versions, benefiting developers and users. The release allows up to ten web searches per response and supports explicit model capabilities, with specific PRs linked for further details.

github · github-actions\[bot\] · Sep 30, 04:14

**Background**: MLX is Apple&\#x27;s machine learning framework for Apple Silicon, while llama.cpp is a C/C++ implementation for efficient LLM inference. Ollama is a tool for running and managing these models locally.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/fine-tuning-open-source-llms-apples-mlx-framework-guide-vishnu-n-c-ylqrc">Fine-Tuning Open-Source LLMs with Apple &#x27;s MLX Framework ...</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/ C++ · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Ollama`, `#llama.cpp`, `#MLX`, `#Software Release`

---

<a id="item-3"></a>
## [GPT-6.1 Sol: Near-Astra intelligence for a fifth of the price](https://simonwillison.net/2026/Sep/29/hn-49898129/) ⭐️ 9.0/10

Simon Willison&\#x27;s analysis of GPT-6.1 Sol highlights its near-Astra intelligence at a fifth of the price compared to previous models, following OpenAI DevDay 2026. This model represents a significant cost-performance breakthrough for developers, potentially democratizing access to high-level AI capabilities for a wider range of applications. GPT-6.1 Sol is positioned below the flagship GPT-6 Astra in the GPT-6 series and offers a competitive API price of $2.00 per 1M input tokens, with the fastest variant reaching 65 tokens/second.

rss · Simon Willison · Sep 30, 02:27

**Background**: The Pelican Bicycle Benchmark is an informal evaluation tool created by Simon Willison in October 2024 to test an LLM&\#x27;s ability to generate valid SVG code for physically impossible scenes, such as a pelican riding a bicycle.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-1-sol">GPT - 6 . 1 Sol Models - Intelligence, Performance... | Artificial Analysis</a></li>
<li><a href="https://tokenharbor.ai/models/gpt-6.1-sol">GPT - 6 . 1 Sol API — $2.00/1M in · Token Harbor</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6.1-sol">GPT - 6 . 1 Sol - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#GPT`, `#OpenAI`, `#Model Evaluation`

---

<a id="item-4"></a>
## [Photo Scrubber: Local AI Face Blur &amp; Metadata Removal Tool](https://simonwillison.net/2026/Sep/29/photo-scrubber/) ⭐️ 9.0/10

Simon Willison released Photo Scrubber, an experimental local tool that uses AI to automatically detect and blur faces in photographs while removing metadata. This tool addresses privacy concerns by enabling on-device face detection and metadata scrubbing, which is crucial for protecting individual identities in public photography. It leverages Google&\#x27;s MediaPipe C++ library, compiled to WebAssembly via @mediapipe/tasks-vision, and uses the BlazeFace model for face detection.

rss · Simon Willison · Sep 30, 00:45

**Background**: WebAssembly allows high-performance applications to run in web browsers, while MediaPipe provides optimized ML solutions for real-time tasks like face detection.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/unqlite_db/porting-a-face-detector-written-in-c-to-webassembly-27p6">Porting a face detector written in C to WebAssembly - DEV Community</a></li>
<li><a href="https://www.infoq.com/news/2020/03/google-mediapipe-webassembly/">Google&#x27;s MediaPipe Machine Learning Framework... - InfoQ</a></li>
<li><a href="https://www.engineering.fyi/article/mediapipe-on-the-web">MediaPipe on the Web | Google Engineering Blog | Engineering.fyi</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#face-detection`, `#webassembly`, `#developer-tools`, `#privacy-preserving`

---

<a id="item-5"></a>
## [DeepMind Introduces SynthID Bio for AI-Generated Proteins](https://deepmind.google/blog/introducing-synthid-bio/) ⭐️ 9.0/10

DeepMind has introduced SynthID Bio, a proof-of-concept watermarking technique designed to embed invisible signals into AI-generated proteins while preserving their biological function. This innovation addresses the growing need for attribution and safety in AI-generated biological data, which is crucial for maintaining trust in scientific research and applications. The technique ensures that the proteins remain fully functional for research or therapeutic use, while the watermark can be detected to verify the source of the AI-generated sequence.

rss · Google DeepMind News · Sep 30, 23:03

**Background**: AI-generated proteins are increasingly used in drug discovery and synthetic biology, but distinguishing them from natural or manually designed sequences is challenging without robust watermarking methods.

**Tags**: `#AI`, `#Proteins`, `#Watermarking`, `#DeepMind`, `#Biotechnology`

---

<a id="item-6"></a>
## [Cloudflare AI Gateway Auto Router Reduces AI Costs](https://blog.cloudflare.com/auto-router/) ⭐️ 9.0/10

Cloudflare AI Gateway now features a model router that evaluates request complexity using an edge-deployed classifier to select the optimal model. This innovation allows organizations to dramatically cut AI spend while maintaining performance by balancing expected output quality against token costs. The router automatically selects the most cost-effective model that meets quality thresholds, ensuring organizations never pay more than necessary for premium models.

rss · Cloudflare Blog · Sep 30, 21:00

**Background**: Model routing acts as a smart middleman between applications and specialized AI models, deciding which model is best suited for a specific task.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/auto-router/">Cut your AI spend with AI Gateway&#x27;s Auto Router</a></li>
<li><a href="https://developers.cloudflare.com/ai-gateway/features/auto-router/">Auto Router · Cloudflare AI Gateway docs</a></li>
<li><a href="https://medium.com/@Colorwheelx/what-is-model-routing-and-why-it-matters-for-smarter-ai-systems-65fc9fa6474e">What Is Model Routing , and Why It Matters for Smarter AI... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI Gateway`, `#Model Routing`, `#Cost Optimization`, `#Edge Computing`, `#Cloudflare`

---

<a id="item-7"></a>
## [Massive Capital Outflow from CXMT, a DRAM Giant](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPeE5FVWM4MjhXallDMlZhdWlueEhJMVA3LUs1UTdUNXlXQXpXaWRkZ1VVYkM2UFh6VHFpaW54clJ3QTNPdXlYM2ExS0IyaWYwYnhzZVhTOGl6U2kxWEl0SVpDc1REUzgyOW5fLVgyMGc1TVJkNEstUEtncjJ3RUFfQldBdm1rdEVS?oc=5) ⭐️ 8.0/10

Financial news reports a massive capital outflow of nearly 7 billion from semiconductor manufacturer CXMT. This significant capital flight signals investor concerns about the company&\#x27;s financial health and the broader semiconductor market&\#x27;s volatility. CXMT is a major Chinese DRAM manufacturer, and this outflow is part of a broader trend of concentrated selling in leading semiconductor stocks.

google\_news · 新浪财经 · Sep 30, 22:03

**Background**: ChangXin Memory Technologies \(CXMT\) is a Chinese integrated device manufacturer headquartered in Hefei, specializing in DRAM production. It operates an IDM \(integrated device manufacturer\) model, focusing on the design, manufacturing, and testing of DRAM chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8">长鑫存储 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#DRAM`, `#CXMT`, `#investment`, `#capital`

---