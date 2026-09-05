---
layout: default
title: "Horizon Summary: 2026-09-05 (EN)"
date: 2026-09-05
content_date: 2026-09-04
lang: en
---

> Coverage: 2026-09-04 (Asia/Shanghai calendar day)

> From 104 items, 12 important content pieces were selected

---

1. [llama.cpp Release b10796 Fixes MoE Model Loading](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10795](#item-2) ⭐️ 10.0/10
3. [OpenAI Announces GPT-6 Astra with Record-Breaking Benchmarks](#item-3) ⭐️ 10.0/10
4. [Discovery of a new OpenAI agent message board](#item-4) ⭐️ 9.0/10
5. [Cloudflare Introduces AI-Powered Vulnerability Discovery and Remediation](#item-5) ⭐️ 9.0/10
6. [Kubernetes 1.37: DRA Extended Resources GA](#item-6) ⭐️ 9.0/10
7. [Mol-JEPA - Multimodal molecular foundation model \[R\]](#item-7) ⭐️ 9.0/10
8. [美国参议员要求 NSA 发布 VPN 使用指南，明确不同工具能否抵御外国监控](#item-8) ⭐️ 9.0/10
9. [中国长鑫存储为腾讯供应价值200亿元人民币的DRAM - 朝鮮日報中文版](#item-9) ⭐️ 9.0/10
10. [长江存储等成立武汉新融光 注册资本132亿元 - 观点网](#item-10) ⭐️ 9.0/10
11. [大国之芯系列｜8年过去了，国产半导体追上来了吗？ - 电子工程专辑](#item-11) ⭐️ 9.0/10
12. [IBM Bob](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp Release b10796 Fixes MoE Model Loading](https://github.com/ggml-org/llama.cpp/releases/tag/b10796) ⭐️ 10.0/10

llama.cpp version b10796 introduces a new n\_expert\_used\_max function to resolve model loading errors for Mixture-of-Experts architectures like Nemotron-3-Puzzle-75B-A9B. This fix is critical for developers deploying large-scale AI models, as it ensures compatibility with advanced MoE architectures that are becoming standard in high-performance computing. The update addresses specific assertion failures, such as &\#x27;GGML\_ASSERT\(n\_ids\_used &gt; 0\)&\#x27;, by using n\_expert\_used\_max to handle expert layer checks during model loading.

github · github-actions\[bot\] · Sep 4, 13:31

**Background**: Mixture-of-Experts \(MoE\) architectures allow large models to reduce computation costs by activating only a subset of experts per layer, as explained by IBM. llama.cpp is a widely used open-source library for local LLM inference, often serving as the core for tools like Ollama.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/mixture-of-experts">What is mixture of experts? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#Mixture-of-Experts`, `#AI inference`, `#open-source`, `#bug-fix`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10795](https://github.com/ggml-org/llama.cpp/releases/tag/b10795) ⭐️ 10.0/10

llama.cpp release b10795 introduces SYC fusion optimizations for AI inference kernels.

github · github-actions\[bot\] · Sep 4, 12:30

**Tags**: `#llama.cpp`, `#AI inference`, `#SYCL`, `#kernel optimization`, `#GGML`

---

<a id="item-3"></a>
## [OpenAI Announces GPT-6 Astra with Record-Breaking Benchmarks](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

OpenAI has released GPT-6 Astra, a new frontier AI model that achieved 98% on FrontierMath Tier 4, 99.9% on ARC-AGI-3, and 100% on ExploitBench, while also introducing a fast mode for API users. GPT-6 Astra&\#x27;s exceptional performance on complex reasoning and security benchmarks positions it as a major competitor to other frontier models like Claude Fable, potentially raising the bar for AI capabilities. The model is priced at $10 per million input tokens and $50 per million output tokens, with a fast mode that processes requests 2.5x faster at double the cost, and it has demonstrated critical security capabilities by discovering zero-day vulnerabilities.

telegram · zaihuapd · Sep 4, 02:47

**Background**: FrontierMath Tier 4 is an expansion set of 43 exceptionally difficult problems, while ARC-AGI-3 is an interactive reasoning benchmark designed to evaluate an AI agent&\#x27;s ability to adapt and learn in novel environments.

<details><summary>References</summary>
<ul>
<li><a href="https://epoch.ai/benchmarks/frontiermath-tier-4-v2">FrontierMath Tier 4 (v2) | Epoch AI</a></li>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://thehackernews.com/2026/09/gpt-6-astra-scores-100-on-exploitbench.html">GPT-6 Astra Scores 100% on ExploitBench as OpenAI Blocks PoC...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#GPT-6`, `#OpenAI`, `#Benchmark`, `#API`

---

<a id="item-4"></a>
## [Discovery of a new OpenAI agent message board](https://collusion.wiki/) ⭐️ 9.0/10

A new OpenAI agent message board reveals widespread agent spam, manual moderation efforts, and technical workarounds to block them.

hackernews · moultano · Sep 4, 19:54 · [Discussion](https://news.ycombinator.com/item?id=49563355)

**Tags**: `#AI Agents`, `#Security`, `#Open Source`, `#Infrastructure`, `#Moderation`

---

<a id="item-5"></a>
## [Cloudflare Introduces AI-Powered Vulnerability Discovery and Remediation](https://blog.cloudflare.com/vulnerability-discovery-remediation/) ⭐️ 9.0/10

Cloudflare has launched an invitation-only Vulnerability Discovery and Remediation service under Managed Defense that uses OpenAI Daybreak models to detect and patch vulnerabilities in codebases. This integration of AI with security workflows accelerates threat prioritization and mitigation, offering a significant advantage in the evolving landscape of vulnerability management. The service leverages production traffic and security signals, including WAF data, to prioritize findings and propose code patches, with all changes requiring explicit human approval.

rss · Cloudflare Blog · Sep 4, 05:03

**Background**: Vulnerability Discovery and Remediation is part of Cloudflare Managed Defense, a suite of security services designed to protect applications and infrastructure. OpenAI Daybreak models, such as GPT-5.6 Cyber, are specialized AI systems for cybersecurity tasks like threat identification and patch generation.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/vulnerability-discovery-remediation/">Introducing context-aware vulnerability discovery and ...</a></li>
<li><a href="https://www.businesswire.com/news/home/20260903116496/en/Cloudflare-Partners-with-OpenAI-Daybreak-Models-to-Redefine-Vulnerability-Management-with-AI-Powered-Edge-Defense">Cloudflare Partners with OpenAI Daybreak Models to Redefine...</a></li>
<li><a href="https://www.thecodingzebra.com/cybersecurity/openai-daybreak-targets-vulnerabilities/">OpenAI Daybreak Targets Vulnerabilities | The Coding Zebra</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Security`, `#Cloudflare`, `#Vulnerability Management`, `#OpenAI`

---

<a id="item-6"></a>
## [Kubernetes 1.37: DRA Extended Resources GA](https://kubernetes.io/blog/2026/09/03/kubernetes-v1-37-dra-updates/) ⭐️ 9.0/10

Kubernetes 1.37 introduces GA support for Dynamic Resource Allocation Extended Resources, allowing DRA drivers to satisfy requests through the traditional extended resource API without requiring a separate device plugin. This milestone enables gradual DRA adoption by maintaining compatibility with existing workloads while migrating backend allocation logic, making it easier for operators to manage specialized hardware resources. Additional stable features include ResourceClaims status with standardized network interface data, device taints and tolerations, and the standardized numaNode device attribute for cross-driver comparison.

rss · Kubernetes Blog · Sep 4, 02:30

**Background**: Dynamic Resource Allocation \(DRA\) is a Kubernetes feature for managing specialized hardware resources like GPUs and FPGAs. It allows cluster operators to define device classes and resource claims that can be dynamically allocated to pods based on workload requirements.

**Tags**: `#kubernetes`, `#dynamic-resource-allocation`, `#software-engineering`, `#cloud-native`, `#devops`

---

<a id="item-7"></a>
## [Mol-JEPA - Multimodal molecular foundation model \[R\]](https://www.reddit.com/r/MachineLearning/comments/1w6i8pr/moljepa_multimodal_molecular_foundation_model_r/) ⭐️ 9.0/10

A researcher shares a new multimodal JEPA foundation model for molecules with a summary website and invites community feedback.

reddit · r/MachineLearning · /u/TerribleAntelope9348 · Sep 4, 03:56

**Tags**: `#Machine Learning`, `#Foundation Models`, `#Molecules`, `#JEPA`, `#Research`

---

<a id="item-8"></a>
## [美国参议员要求 NSA 发布 VPN 使用指南，明确不同工具能否抵御外国监控](https://arstechnica.com/security/2026/09/us-senator-calls-on-the-nsa-to-give-guidance-for-use-of-vpns/) ⭐️ 9.0/10

US Senator Ron Wyden requests the NSA to publish updated VPN usage guidelines to help users choose tools that effectively resist foreign surveillance.

telegram · zaihuapd · Sep 4, 11:51

**Tags**: `#VPN`, `#Surveillance`, `#NSA`, `#Cybersecurity`, `#Privacy`

---

<a id="item-9"></a>
## [中国长鑫存储为腾讯供应价值200亿元人民币的DRAM - 朝鮮日報中文版](https://news.google.com/rss/articles/CBMioAFBVV95cUxOSWM4STlIR01xM1JvdjB0TEJNM0M1UXlBNXNsMEFTWlgwYUpsc3JaNkVEeUNFQlVDSmpna0lqNkYwdnp2V0E3a2xSdnlkdWtUZGluSE5wSG1DYWxlVnhRNGg4ZlJlQUs3eGxxVl95ZnJIQzB1THJNU3RjV00wODhESWd5a0p0TXl0QTVPT2pSNktjelltNjJ0czVpLXotYkEx?oc=5) ⭐️ 9.0/10

China&\#x27;s CXMT will supply Tencent with 20 billion RMB worth of DRAM.

google\_news · 朝鮮日報中文版 · Sep 4, 20:08

**Tags**: `#DRAM`, `#semiconductors`, `#memory`, `#AI infrastructure`, `#supply chain`

---

<a id="item-10"></a>
## [长江存储等成立武汉新融光 注册资本132亿元 - 观点网](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9URnY3ZFZ4NjVnOUtORThtSjlYcm9WdHZuUHJ4YmRBNFFsaXpVYTFMcXFWbl9xek9ZYWo3N2tGMWdIdlhGeTB5MWZZdEtrZw?oc=5) ⭐️ 9.0/10

A news snippet about the formation of a new company with 13.2 billion yuan in capital involving Yangtze Memory Technologies.

google\_news · 观点网 · Sep 4, 12:35

**Tags**: `#semiconductors`, `#memory`, `#Yangtze Memory`, `#hardware`, `#investment`

---

<a id="item-11"></a>
## [大国之芯系列｜8年过去了，国产半导体追上来了吗？ - 电子工程专辑](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5XX0NlZjJZSkZsNEtWc0xSd0JSemlZSTgxdlVtdG1DbkFUdjAwclBGei1CQ3NrWGtXZHFmVHZIaGdHMzFaNDUtNVNVc1czUENBTS1v?oc=5) ⭐️ 9.0/10

This article examines the progress of domestic semiconductor manufacturing over the past eight years.

google\_news · 电子工程专辑 · Sep 4, 16:55

**Tags**: `#semiconductors`, `#chips`, `#hardware`, `#AI accelerators`, `#industry analysis`

---

<a id="item-12"></a>
## [IBM Bob](https://bob.ibm.com/) ⭐️ 8.0/10

IBM Bob is a humorous AI assistant that sparked a nostalgic and lighthearted discussion on Hacker News.

hackernews · artpar · Sep 4, 20:50 · [Discussion](https://news.ycombinator.com/item?id=49563851)

**Tags**: `#AI`, `#IBM`, `#Hacker News`, `#Nostalgia`, `#Meme`

---