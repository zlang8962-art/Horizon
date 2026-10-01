---
layout: default
title: "Horizon Summary: 2026-10-01 (ZH)"
date: 2026-10-01
content_date: 2026-09-30
lang: zh
---

> 报道范围：2026-09-30（Asia/Shanghai 自然日）

> 从 71 条内容中筛选出 7 条重要资讯。

---

1. [ggml-org/llama.cpp 发布了 b11280 版本](#item-1) ⭐️ 10.0/10
2. [Ollama v0.35.1-rc0：引入网络搜索、MLX 和 llama.cpp 更新](#item-2) ⭐️ 9.0/10
3. [GPT-6.1 Sol：接近 Astra 智能水平，价格仅为五分之一](#item-3) ⭐️ 9.0/10
4. [Photo Scrubber：本地 AI 面部模糊与元数据移除工具](#item-4) ⭐️ 9.0/10
5. [DeepMind 推出用于 AI 生成蛋白质的 SynthID Bio](#item-5) ⭐️ 9.0/10
6. [Cloudflare AI Gateway 自动路由器降低 AI 成本](#item-6) ⭐️ 9.0/10
7. [近 70 亿资金出逃长鑫科技，半导体等赛道龙头遭集中抛售](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布了 b11280 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b11280) ⭐️ 10.0/10

llama.cpp b11280 版本添加了 SYC L 张量 Allreduce 优化，并提供了 AI 推理的跨平台二进制文件。

github · github-actions\[bot\] · 9月30日 19:27

**标签**: `#llama.cpp`, `#AI inference`, `#C++`, `#SYCL`, `#open-source`

---

<a id="item-2"></a>
## [Ollama v0.35.1-rc0：引入网络搜索、MLX 和 llama.cpp 更新](https://github.com/ollama/ollama/releases/tag/v0.35.1-rc0) ⭐️ 9.0/10

Ollama v0.35.1-rc0 引入了网络搜索支持，升级了 MLX 和 llama.cpp 版本，并增加了显式模型能力。 此次更新通过启用网络搜索并借助更新的 MLX 和 llama.cpp 版本提升性能，增强了 Ollama 的功能，使开发者和用户受益。 该版本允许每次响应最多进行十次网络搜索，并支持显式模型能力，相关 PR 链接提供了更多细节。

github · github-actions\[bot\] · 9月30日 04:14

**背景**: MLX 是苹果为 Apple Silicon 设计的机器学习框架，llama.cpp 则是一个用于高效 LLM 推理的 C/C++ 实现。Ollama 是一个用于本地运行和管理这些模型的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/fine-tuning-open-source-llms-apples-mlx-framework-guide-vishnu-n-c-ylqrc">Fine-Tuning Open-Source LLMs with Apple &#x27;s MLX Framework ...</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/ C++ · GitHub</a></li>

</ul>
</details>

**标签**: `#AI`, `#Ollama`, `#llama.cpp`, `#MLX`, `#Software Release`

---

<a id="item-3"></a>
## [GPT-6.1 Sol：接近 Astra 智能水平，价格仅为五分之一](https://simonwillison.net/2026/Sep/29/hn-49898129/) ⭐️ 9.0/10

Simon Willison 对 GPT-6.1 Sol 的分析显示，其智能水平接近 Astra，但价格仅为之前的五分之一，这是在 OpenAI DevDay 2026 之后发布的。 该模型为开发者带来了显著的成本性能突破，可能使更广泛的应用能够以较低成本获得高级 AI 能力。 GPT-6.1 Sol 在 GPT-6 系列中定位低于旗舰模型 GPT-6 Astra，API 价格为每 100 万个输入令牌 2.00 美元，最快版本达到每秒 65 个令牌。

rss · Simon Willison · 9月30日 02:27

**背景**: Pelican Bicycle Benchmark 是 Simon Willison 于 2024 年 10 月创建的评估工具，用于测试大语言模型生成物理上不可能场景（如一只骑自行车的鹈鹕）的有效 SVG 代码的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-1-sol">GPT - 6 . 1 Sol Models - Intelligence, Performance... | Artificial Analysis</a></li>
<li><a href="https://tokenharbor.ai/models/gpt-6.1-sol">GPT - 6 . 1 Sol API — $2.00/1M in · Token Harbor</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6.1-sol">GPT - 6 . 1 Sol - API Pricing &amp; Providers | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI`, `#Machine Learning`, `#GPT`, `#OpenAI`, `#Model Evaluation`

---

<a id="item-4"></a>
## [Photo Scrubber：本地 AI 面部模糊与元数据移除工具](https://simonwillison.net/2026/Sep/29/photo-scrubber/) ⭐️ 9.0/10

Simon Willison 发布了 Photo Scrubber，这是一个实验性的本地工具，使用 AI 自动检测并模糊照片中的人脸，同时移除元数据。 该工具通过在设备上进行面部检测和元数据清理，解决了隐私问题，这对于保护公共摄影中的个人身份至关重要。 它利用 Google 的 MediaPipe C++ 库，通过 @mediapipe/tasks-vision 编译为 WebAssembly，并使用 BlazeFace 模型进行面部检测。

rss · Simon Willison · 9月30日 00:45

**背景**: WebAssembly 允许高性能应用程序在 Web 浏览器中运行，而 MediaPipe 为面部检测等实时任务提供了优化的机器学习解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/unqlite_db/porting-a-face-detector-written-in-c-to-webassembly-27p6">Porting a face detector written in C to WebAssembly - DEV Community</a></li>
<li><a href="https://www.infoq.com/news/2020/03/google-mediapipe-webassembly/">Google&#x27;s MediaPipe Machine Learning Framework... - InfoQ</a></li>
<li><a href="https://www.engineering.fyi/article/mediapipe-on-the-web">MediaPipe on the Web | Google Engineering Blog | Engineering.fyi</a></li>

</ul>
</details>

**标签**: `#privacy`, `#face-detection`, `#webassembly`, `#developer-tools`, `#privacy-preserving`

---

<a id="item-5"></a>
## [DeepMind 推出用于 AI 生成蛋白质的 SynthID Bio](https://deepmind.google/blog/introducing-synthid-bio/) ⭐️ 9.0/10

DeepMind 推出了 SynthID Bio，这是一种概念验证的水印技术，旨在将不可见的信号嵌入 AI 生成的蛋白质中，同时保持其生物功能。 这一创新解决了 AI 生成生物数据中日益增长的归属和安全需求，这对于维护科学研究和应用中的信任至关重要。 该技术确保蛋白质在研究或治疗用途中保持完全功能，同时水印可以被检测到，以验证 AI 生成序列的来源。

rss · Google DeepMind News · 9月30日 23:03

**背景**: AI 生成的蛋白质越来越多地用于药物发现和合成生物学，但如果没有强大的水印方法，很难将它们与天然或手动设计的序列区分开来。

**标签**: `#AI`, `#Proteins`, `#Watermarking`, `#DeepMind`, `#Biotechnology`

---

<a id="item-6"></a>
## [Cloudflare AI Gateway 自动路由器降低 AI 成本](https://blog.cloudflare.com/auto-router/) ⭐️ 9.0/10

Cloudflare AI Gateway 现在拥有一个模型路由器，它使用边缘部署的分类器评估请求复杂度，以选择最佳模型。 这一创新允许组织在保持性能的同时，通过平衡预期输出质量和令牌成本，大幅削减 AI 花费。 路由器自动选择最符合质量阈值的成本效益模型，确保组织为优质模型支付的费用不会超过必要金额。

rss · Cloudflare Blog · 9月30日 21:00

**背景**: 模型路由充当应用程序和专用 AI 模型之间的智能中介，决定哪个模型最适合特定任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/auto-router/">Cut your AI spend with AI Gateway&#x27;s Auto Router</a></li>
<li><a href="https://developers.cloudflare.com/ai-gateway/features/auto-router/">Auto Router · Cloudflare AI Gateway docs</a></li>
<li><a href="https://medium.com/@Colorwheelx/what-is-model-routing-and-why-it-matters-for-smarter-ai-systems-65fc9fa6474e">What Is Model Routing , and Why It Matters for Smarter AI... | Medium</a></li>

</ul>
</details>

**标签**: `#AI Gateway`, `#Model Routing`, `#Cost Optimization`, `#Edge Computing`, `#Cloudflare`

---

<a id="item-7"></a>
## [近 70 亿资金出逃长鑫科技，半导体等赛道龙头遭集中抛售](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPeE5FVWM4MjhXallDMlZhdWlueEhJMVA3LUs1UTdUNXlXQXpXaWRkZ1VVYkM2UFh6VHFpaW54clJ3QTNPdXlYM2ExS0IyaWYwYnhzZVhTOGl6U2kxWEl0SVpDc1REUzgyOW5fLVgyMGc1TVJkNEstUEtncjJ3RUFfQldBdm1rdEVS?oc=5) ⭐️ 8.0/10

财经新闻报道，半导体制造商长鑫科技（CXMT）近 70 亿资金出逃。 如此大规模的资金出逃表明投资者对该公司财务状况及半导体市场的波动性存在担忧。 长鑫科技是一家主要的中国 DRAM 制造商，此次资金出逃是半导体龙头股遭集中抛售趋势的一部分。

google\_news · 新浪财经 · 9月30日 22:03

**背景**: 长鑫存储技术股份有限公司（CXMT）是一家总部位于合肥的中国集成电路企业，专注于 DRAM 的生产。它采取垂直整合制造（IDM）模式，专注于 DRAM 芯片的设计、制造和测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8">长鑫存储 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#CXMT`, `#investment`, `#capital`

---