---
layout: default
title: "Horizon Summary: 2026-09-23 (EN)"
date: 2026-09-23
content_date: 2026-09-22
lang: en
---

> Coverage: 2026-09-22 (Asia/Shanghai calendar day)

> From 84 items, 12 important content pieces were selected

---

1. [vLLM v0.30.0: New Models and Hardware Optimizations](#item-1) ⭐️ 10.0/10
2. [阿里发布宣称最强国产 AI 芯片真武 V900，算力提升至 3 倍](#item-2) ⭐️ 10.0/10
3. [OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005](#item-3) ⭐️ 9.0/10
4. [llm-typesafe 0.1a0](#item-4) ⭐️ 9.0/10
5. [Jev introduces a new shape of LLM - System One, aka Decision Models](#item-5) ⭐️ 9.0/10
6. [Mapping MoE Models to Inference Hardware](#item-6) ⭐️ 9.0/10
7. [Introducing Worker Previews: Isolated preview environments for every change your agent makes](#item-7) ⭐️ 9.0/10
8. [Kubernetes v1.37: Tracking When a PersistentVolumeClaim Was Last Used \(Beta\)](#item-8) ⭐️ 9.0/10
9. [Xiaomi Releases MiMo-V2.6 Multimodal AI Model](#item-9) ⭐️ 9.0/10
10. [Understanding and Enhancing Kimi Delta Attention \[R\]](#item-10) ⭐️ 9.0/10
11. [OpenAI Establishes Math and AI Advisory Group](#item-11) ⭐️ 9.0/10
12. [长鑫科技宣布第五代技术平台正式量产 - 中华网财经](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [vLLM v0.30.0: New Models and Hardware Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 10.0/10

vLLM v0.30.0 introduces new AI models like DeepSeek-V4.1 and GLM-5.3, hardware optimizations including MXFP8 and ROCm support, and a Fast Start feature for efficient weight caching. This release significantly advances AI compute efficiency by supporting advanced models and hardware, enabling faster and more scalable inference for developers and enterprises. Key features include Fast Start for persistent GPU weight caching, HiSparse for host-resident sparse-MLA decode, and Model Runner V2 improvements like dual-batch overlap and FULL CUDA graphs.

github · khluu · Sep 22, 13:20

**Background**: vLLM is a high-performance inference engine for large language models, focusing on optimizing GPU memory and throughput. The release includes support for new hardware like ROCm and advanced quantization methods.

**Tags**: `#vllm`, `#AI`, `#DeepSeek`, `#GPU`, `#Software-Engineering`

---

<a id="item-2"></a>
## [阿里发布宣称最强国产 AI 芯片真武 V900，算力提升至 3 倍](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 10.0/10

Alibaba announces its True Power V900 AI chip, claiming a 3x performance increase and massive scalability.

telegram · zaihuapd · Sep 22, 11:30

**Tags**: `#AI Chip`, `#Semiconductor`, `#Cloud Computing`, `#Hardware`, `#Alibaba`

---

<a id="item-3"></a>
## [OpenAI GPT–6 Astra breaks Enigma message that has resisted solution since 2005](https://www.cryptocellar.org/bgac/the-mvueh-break.html) ⭐️ 9.0/10

OpenAI&\#x27;s GPT-6 Astra model breaks a 2005-resistant Enigma message with community collaboration and technical analysis.

hackernews · sohkamyung · Sep 22, 21:52 · [Discussion](https://news.ycombinator.com/item?id=49801324)

**Tags**: `#AI`, `#Cryptography`, `#Enigma`, `#OpenAI`, `#Historical Computing`

---

<a id="item-4"></a>
## [llm-typesafe 0.1a0](https://simonwillison.net/2026/Sep/22/llm-typesafe/) ⭐️ 9.0/10

A new plugin for the LLM tool adds support for the TypeSafe AI Jev model, enabling yes/no and choice queries.

rss · Simon Willison · Sep 22, 23:54

**Tags**: `#AI`, `#LLM`, `#Plugin`, `#TypeSafe`, `#Jev`

---

<a id="item-5"></a>
## [Jev introduces a new shape of LLM - System One, aka Decision Models](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 9.0/10

Jev is a new &\#x27;System One&\#x27; or &\#x27;decision model&\#x27; that outputs typed probabilistic decisions instead of text, offering a faster and cheaper alternative to traditional LLMs.

rss · Simon Willison · Sep 22, 07:09

**Tags**: `#AI`, `#LLMs`, `#Decision Models`, `#TypeSafe AI`, `#Model Architecture`

---

<a id="item-6"></a>
## [Mapping MoE Models to Inference Hardware](https://newsletter.semianalysis.com/p/computation-and-data-movement-for) ⭐️ 9.0/10

This analysis explores how to map Mixture-of-Experts \(MoE\) models onto inference hardware, focusing on data movement and efficient serving. Efficient serving of MoE models is critical for scaling large language models, as it directly impacts inference latency and cost in production environments. The analysis covers the structural flow of MoE models, the challenges of data movement between experts, and strategies for optimizing serving infrastructure.

rss · Semianalysis · Sep 22, 02:14

**Background**: Mixture-of-Experts \(MoE\) models are a type of neural network architecture that dynamically selects a subset of experts to process each input, enabling efficient scaling of model size. Efficient serving requires careful management of data movement and computational resources to minimize latency and maximize throughput.

**Tags**: `#AI inference`, `#MoE models`, `#hardware optimization`, `#data movement`, `#efficient serving`

---

<a id="item-7"></a>
## [Introducing Worker Previews: Isolated preview environments for every change your agent makes](https://blog.cloudflare.com/worker-previews/) ⭐️ 9.0/10

Cloudflare introduces Worker Previews, a feature that provides isolated preview environments for every change made by AI agents to test changes in parallel without affecting production.

rss · Cloudflare Blog · Sep 22, 21:00

**Tags**: `#cloudflare`, `#developer-tools`, `#preview-environments`, `#ai-agents`, `#software-workflows`

---

<a id="item-8"></a>
## [Kubernetes v1.37: Tracking When a PersistentVolumeClaim Was Last Used \(Beta\)](https://kubernetes.io/blog/2026/09/21/kubernetes-v1-37-pvc-last-used-time/) ⭐️ 9.0/10

Kubernetes v1.37 introduces a beta feature to track when a PersistentVolumeClaim was last used, helping users manage storage lifecycle.

rss · Kubernetes Blog · Sep 22, 02:30

**Tags**: `#kubernetes`, `#storage`, `#developer-tools`, `#cloud-native`, `#beta-feature`

---

<a id="item-9"></a>
## [Xiaomi Releases MiMo-V2.6 Multimodal AI Model](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 9.0/10

Xiaomi has released MiMo-V2.6, a multimodal AI model that required $3.5 million in reinforcement learning \(RL\) training costs and includes a live benchmarking dashboard. The substantial RL training cost highlights the financial investment required for frontier intelligence models, while the live benchmarking dashboard offers transparency for the AI community. The model&\#x27;s live dashboard allows users to monitor performance metrics in real-time, and the $3.5M RL training cost reflects the scale of resources needed for advanced AI development.

reddit · r/MachineLearning · /u/we\_are\_mammals · Sep 22, 15:56

**Background**: Multimodal AI models process and generate content across different data types, such as text, images, and audio. Reinforcement learning is a training method where an agent learns to make decisions by receiving rewards or penalties based on its actions.

**Tags**: `#AI`, `#Multimodal`, `#Benchmarking`, `#Xiaomi`, `#RL Training`

---

<a id="item-10"></a>
## [Understanding and Enhancing Kimi Delta Attention \[R\]](https://www.reddit.com/r/MachineLearning/comments/1wn5uv9/understanding_and_enhancing_kimi_delta_attention_r/) ⭐️ 9.0/10

This post introduces Complex KDA, a novel enhancement to Kimi Delta Attention that improves expressivity for orthogonal transformations and shows competitive performance in language modeling.

reddit · r/MachineLearning · /u/Yossarian\_1234 · Sep 22, 18:34

**Tags**: `#machine-learning`, `#attention-mechanisms`, `#deep-learning`, `#model-optimization`, `#neural-networks`

---

<a id="item-11"></a>
## [OpenAI Establishes Math and AI Advisory Group](https://techcrunch.com/2026/09/21/openai-forms-math-advisory-group-as-its-ai-resolves-more-than-100-open-problems/) ⭐️ 9.0/10

OpenAI announced on September 21 that it has established an independent Math and AI Advisory Group at the Institute for Advanced Study, with nine mathematicians as its initial members. This move highlights the increasing intersection of advanced AI capabilities and fundamental mathematics, potentially setting new standards for how AI research is evaluated and coordinated. The group will evaluate research findings, coordinate releases, and provide advice, though it has no authority to alter OpenAI&\#x27;s research progress or decision-making processes.

telegram · zaihuapd · Sep 22, 11:00

**Background**: The Institute for Advanced Study is a prestigious research institution known for fostering groundbreaking work in mathematics and theoretical physics. The group&\#x27;s formation comes amid growing scrutiny of AI labs&\#x27; competitive race to solve famous mathematical problems.

**Tags**: `#OpenAI`, `#AI Research`, `#Mathematics`, `#Institute for Advanced Study`, `#AI Advisory`

---

<a id="item-12"></a>
## [长鑫科技宣布第五代技术平台正式量产 - 中华网财经](https://news.google.com/rss/articles/CBMibkFVX3lxTFBoNGpLV3NOX3IyTE93Y0J0NDZPWG5lbGhXSFF4dDVSLWVCdWowcS14UnZORGhfWDJDVkxPM3RWcDNzb0JJeU5aa1Rtd0taWGQ1eUhqZ2x2dk1fME5QZDdxNklycmhCNkJhZWc4MFJB?oc=5) ⭐️ 9.0/10

CXMT announces mass production of its fifth-generation memory technology platform.

google\_news · 中华网财经 · Sep 22, 16:25

**Tags**: `#semiconductors`, `#memory`, `#CXMT`, `#AI accelerators`, `#manufacturing`

---