---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
content_date: 2026-09-09
lang: en
---

> Coverage: 2026-09-09 (Asia/Shanghai calendar day)

> From 85 items, 12 important content pieces were selected

---

1. [huggingface/transformers released v5.17.0](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10868 Release Adds MoE Support and Cross-Platform Binaries](#item-2) ⭐️ 10.0/10
3. [ggml-org/llama.cpp released b10867](#item-3) ⭐️ 10.0/10
4. [NVIDIA TensorRT-LLM v1.3.0rc26 Released](#item-4) ⭐️ 9.0/10
5. [Shopify acquires Tailwind](#item-5) ⭐️ 9.0/10
6. [GPT-6 Astra, looped transformers, and hidden reasoning](#item-6) ⭐️ 9.0/10
7. [Desert Ant Labs: local, fast models that run on device](#item-7) ⭐️ 9.0/10
8. [Read the Docs DDoS Attack Analysis](#item-8) ⭐️ 9.0/10
9. [On the Navier–Stokes Millennium Prize Problem](#item-9) ⭐️ 9.0/10
10. [How we rebuilt Cloudflare Workers’ module registry for Node.js compatibility](#item-10) ⭐️ 9.0/10
11. [Kubernetes v1.37: Advancing Workload-Aware Scheduling](#item-11) ⭐️ 9.0/10
12. [存储芯片产能稳了！长鑫存储、长江存储囤够三年DUV光刻机：美国想卡脖子 晚了 - 驱动之家](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [huggingface/transformers released v5.17.0](https://github.com/huggingface/transformers/releases/tag/v5.17.0) ⭐️ 10.0/10

Hugging Face Transformers v5.17.0 introduces HYV4, a 780B-parameter MoE model with 1M context window and advanced attention mechanisms.

github · vasqu · Sep 9, 23:42

**Tags**: `#AI`, `#Machine Learning`, `#Transformers`, `#MoE`, `#Deep Learning`

---

<a id="item-2"></a>
## [llama.cpp b10868 Release Adds MoE Support and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10868) ⭐️ 10.0/10

The llama.cpp project has released version b10868, which includes support for Mixture-of-Experts \(MoE\) models and provides pre-built binaries for macOS, Linux, Android, and Windows. This release significantly expands the tool&\#x27;s compatibility with advanced AI architectures like MoE, which are increasingly used in large-scale language models, while making it easier for developers to run inference across different operating systems. The release includes binaries for various platforms and hardware backends, such as Apple Silicon, CUDA, Vulkan, and ROCm, but the macOS Apple Silicon build with KleidiAI is currently disabled.

github · github-actions\[bot\] · Sep 9, 10:00

**Background**: llama.cpp is a popular open-source library for running large language models efficiently on consumer hardware, and MoE is a technique that splits a model into multiple expert sub-networks to improve performance and efficiency.

**Tags**: `#llama.cpp`, `#open-source`, `#AI`, `#inference`, `#cross-platform`

---

<a id="item-3"></a>
## [ggml-org/llama.cpp released b10867](https://github.com/ggml-org/llama.cpp/releases/tag/b10867) ⭐️ 10.0/10

llama.cpp b10867 disables lazy tensor loading by default on iGPUs to fix regressions, with new binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Sep 9, 01:31

**Tags**: `#llama.cpp`, `#AI inference`, `#GPU optimization`, `#open-source`, `#integrated graphics`

---

<a id="item-4"></a>
## [NVIDIA TensorRT-LLM v1.3.0rc26 Released](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc26) ⭐️ 9.0/10

NVIDIA released TensorRT-LLM v1.3.0rc26, addressing critical bugs in LoRA adapters for routed experts, KV cache memory estimation, and FlashInfer backend memory leaks. This release improves the stability and reliability of large language model inference on NVIDIA GPUs, which is crucial for production deployments and optimizing GPU resource utilization. Known issues include LoRA adapters targeting routed experts being ignored, V2 KV cache manager overestimating memory needs, and FlashInfer backend memory accumulation over time.

github · tongyuantongyu · Sep 9, 17:37

**Background**: TensorRT-LLM is NVIDIA&\#x27;s library for optimizing inference on GPUs, and KV cache memory estimation is critical for managing GPU memory during LLM generation to prevent out-of-memory errors.

<details><summary>References</summary>
<ul>
<li><a href="https://lyceum.technology/magazine/kv-cache-memory-calculation-llm/">KV Cache Memory Calculation for LLMs | Technical Guide | Lyceum Technology</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library for LLM Serving · GitHub</a></li>

</ul>
</details>

**Tags**: `#TensorRT-LLM`, `#GPU memory management`, `#AI inference`, `#bug fixes`, `#NVIDIA`

---

<a id="item-5"></a>
## [Shopify acquires Tailwind](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 9.0/10

Shopify acquires Tailwind CSS, with community discussion focusing on AI&\#x27;s impact on the company and the value of Tailwind as a software development tool.

hackernews · EdwinHoksberg · Sep 9, 21:27 · [Discussion](https://news.ycombinator.com/item?id=49626190)

**Tags**: `#Tailwind CSS`, `#Shopify`, `#AI in Software Development`, `#Developer Tools`, `#Open Source`

---

<a id="item-6"></a>
## [GPT-6 Astra, looped transformers, and hidden reasoning](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 9.0/10

The article introduces GPT-6 Astra, a model that utilizes looped transformers and hidden reasoning techniques, which were previously misunderstood as a &\#x27;secret technique&\#x27; for monitoring thought processes. This development is significant because it clarifies that looped transformers are essentially a memory-efficient alternative to stacking more transformer layers, potentially impacting how AI models are trained and deployed. The technique involves reusing model weights during inference to reduce GPU memory usage, similar to Universal Transformers, and can be interpreted as hidden reasoning when the model&\#x27;s output is fed back into itself.

hackernews · ModelForge · Sep 9, 22:37 · [Discussion](https://news.ycombinator.com/item?id=49627370)

**Background**: Transformers are a type of neural network architecture widely used in natural language processing. Looped transformers, also known as Universal Transformers, extend the standard transformer by allowing the model to iterate over its own outputs, effectively creating a recurrent structure.

**Discussion**: Community members debated the computational requirements of looped transformers and shared references to research on Chain of Thought \(CoT\) and Universal Transformers, while one user expressed disappointment over changes to the Astra model.

**Tags**: `#AI`, `#Transformers`, `#Inference`, `#Deep Learning`, `#GPT`

---

<a id="item-7"></a>
## [Desert Ant Labs: local, fast models that run on device](https://desertant.com/blog/introducing-desert-ant-labs/) ⭐️ 9.0/10

Desert Ant Labs introduces local, device-based AI models with a focus on accessibility and cost-efficiency, sparking a discussion on their practical and economic implications.

hackernews · willwhitedc · Sep 9, 19:39 · [Discussion](https://news.ycombinator.com/item?id=49624823)

**Tags**: `#local-ai`, `#device-compute`, `#developer-tools`, `#ai-models`, `#software-architecture`

---

<a id="item-8"></a>
## [Read the Docs DDoS Attack Analysis](https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/) ⭐️ 9.0/10

Read the Docs experienced a significant DDoS attack, which was analyzed in a Hacker News discussion. This incident highlights the growing threat of AI-driven DDoS attacks and the limitations of current web defenses. The attackers evaded Cloudflare&\#x27;s defenses, suggesting the attack was sophisticated and possibly AI-driven.

hackernews · davidfischer · Sep 9, 23:55 · [Discussion](https://news.ycombinator.com/item?id=49628614)

**Background**: Read the Docs is a popular platform for hosting software documentation, often using static hosting and CDN caching.

**Discussion**: Comments suggest the attack may have been a test target for an AI lab, and legal responses were debated.

**Tags**: `#ddos`, `#cloudflare`, `#security`, `#ai`, `#networking`

---

<a id="item-9"></a>
## [On the Navier–Stokes Millennium Prize Problem](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 9.0/10

OpenAI&\#x27;s unreleased model reportedly resolves the Navier–Stokes Millennium Prize Problem, sparking controversy over academic collaboration.

rss · Simon Willison · Sep 9, 07:55

**Tags**: `#AI`, `#Mathematics`, `#OpenAI`, `#Controversy`, `#Research`

---

<a id="item-10"></a>
## [How we rebuilt Cloudflare Workers’ module registry for Node.js compatibility](https://blog.cloudflare.com/workers-module-registry-nodejs/) ⭐️ 9.0/10

Cloudflare rebuilt its Workers module registry to enable Node.js compatibility with features like import.meta and lazy compilation.

rss · Cloudflare Blog · Sep 9, 21:00

**Tags**: `#Cloudflare`, `#JavaScript`, `#Module Registry`, `#Node.js`, `#Developer Tools`

---

<a id="item-11"></a>
## [Kubernetes v1.37: Advancing Workload-Aware Scheduling](https://kubernetes.io/blog/2026/09/08/kubernetes-v1-37-advancing-workload-aware-scheduling/) ⭐️ 9.0/10

Kubernetes v1.37 introduces workload-aware scheduling features, including gang scheduling and preemption policies, along with the new CompositePodGroup API and controller integration APIs. This release significantly enhances Kubernetes&\#x27; ability to handle complex AI/ML and batch workloads, making it more suitable for high-performance distributed systems and advanced workload structures. The Workload and PodGroup APIs graduate to Beta, enabling &\#x27;all-or-nothing&\#x27; scheduling, while the minCount field becomes mutable for dynamic elasticity. The CompositePodGroup API supports multi-level topology constraints and preemption policies.

rss · Kubernetes Blog · Sep 9, 02:30

**Background**: Kubernetes is a container orchestration platform that manages containerized applications. Workload-aware scheduling is an advanced feature that optimizes resource allocation for complex workloads like AI/ML.

**Tags**: `#Kubernetes`, `#Workload-Aware Scheduling`, `#AI/ML`, `#Software Engineering`, `#Distributed Systems`

---

<a id="item-12"></a>
## [存储芯片产能稳了！长鑫存储、长江存储囤够三年DUV光刻机：美国想卡脖子 晚了 - 驱动之家](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9PMXc1SE5INnBFOERuamwySE5qMVpWMUtQb21lUEU5LWNrd1FhRUV1RWthTE9uM2JPc0xPUmtjcjZzLXpKYjFTRzhEMjN2N1BvbHBOR0ZONy0?oc=5) ⭐️ 9.0/10

Chinese memory manufacturers stockpile three years of DUV lithography machines to counter US export restrictions.

google\_news · 驱动之家 · Sep 9, 17:46

**Tags**: `#semiconductors`, `#memory`, `#lithography`, `#supply-chain`, `#export-controls`

---