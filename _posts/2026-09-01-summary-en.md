---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
content_date: 2026-08-31
lang: en
---

> Coverage: 2026-08-31 (Asia/Shanghai calendar day)

> From 113 items, 12 important content pieces were selected

---

1. [ggml-org/llama.cpp released b10705](#item-1) ⭐️ 10.0/10
2. [NVIDIA TensorRT-LLM v1.3.0rc25 Released with KV Cache Manager V2 Default](#item-2) ⭐️ 10.0/10
3. [Hanshu Technology Unveils MRAM Inference Roadmap with 24 TB/s uHBM Bandwidth](#item-3) ⭐️ 10.0/10
4. [长鑫存储已开始小批量生产HBM3E内存 - cnBeta.COM](#item-4) ⭐️ 10.0/10
5. [ggml-org/llama.cpp released b10720](#item-5) ⭐️ 9.0/10
6. [NeurIPS accepted papers leaked? \[D\]](#item-6) ⭐️ 9.0/10
7. [Anthropic warns of malware stealing Claude sessions](#item-7) ⭐️ 9.0/10
8. [CXMT Announces Mass Production of LPDDR6 Memory](#item-8) ⭐️ 9.0/10
9. [长鑫存储状告五角大楼：一家DRAM新贵的法律反击 - or100.cc](#item-9) ⭐️ 9.0/10
10. [Apple caught off guard by AI demand for Mac Mini and Mac Studio](#item-10) ⭐️ 8.0/10
11. [I think the military commissary&\#x27;s freezers were hacked](#item-11) ⭐️ 8.0/10
12. [Understanding ChatGPT Work](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10705](https://github.com/ggml-org/llama.cpp/releases/tag/b10705) ⭐️ 10.0/10

llama.cpp b10705 release improves TENSOR\_READ\_LAZY handling and provides new binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Aug 31, 07:15

**Tags**: `#AI`, `#Machine Learning`, `#Software Development`, `#Hardware Acceleration`, `#Open Source`

---

<a id="item-2"></a>
## [NVIDIA TensorRT-LLM v1.3.0rc25 Released with KV Cache Manager V2 Default](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc25) ⭐️ 10.0/10

NVIDIA/TensorRT-LLM v1.3.0rc25 introduces KV Cache Manager V2 as the default for improved scalability and stability across multiple models, including DeepSeek V3, R1, V4, GLM-5, GPT-OSS, Mistral Large 3, Kimi K2/K2.5/K3, MiniMax M2/M3, Nemotron H, Qwen3-Next/3.5/3.8, Gemma 3/4, and others. This release is significant for AI inference optimization, as KV Cache Manager V2 is the recommended architecture for better performance and stability, and it affects a wide range of popular open-source and commercial models. The release includes a long list of known issues, such as disaggregated serving hangs, generation hangs, memory crashes on B200 GPUs, accuracy loss in certain configurations, and unsupported features for specific models like MiniMax-M3 MXFP8 and Kimi K3 96-head MLA.

github · tongyuantongyu · Aug 31, 11:24

**Background**: TensorRT-LLM is NVIDIA&\#x27;s high-performance inference engine for LLMs, optimizing for NVIDIA GPUs. KV Cache Manager is a component that manages the cache of key-value pairs used during generation, improving efficiency and reducing memory usage.

**Tags**: `#NVIDIA`, `#TensorRT-LLM`, `#AI Inference`, `#KV Cache`, `#DeepSeek`

---

<a id="item-3"></a>
## [Hanshu Technology Unveils MRAM Inference Roadmap with 24 TB/s uHBM Bandwidth](https://mp.weixin.qq.com/s/adyFanNueXUHKnxr9m64kg) ⭐️ 10.0/10

Hanshu Technology, a domestic MRAM spintronics company, has announced its uHBM and uLPU inference architecture, featuring a first-generation uHBM design with 24 TB/s read bandwidth and a uLPU targeting over 2000 tokens/s decoding for 4B multimodal models. This breakthrough addresses the critical need for high-speed, low-latency inference in large language models by leveraging MRAM&\#x27;s persistent memory capabilities, potentially reducing data movement bottlenecks and improving energy efficiency in AI accelerators. The SpinPU-ED01 verification chip has passed third-party testing and 24-hour stability verification, with the architecture designed to keep model weights in Persistent MRAM arrays and perform matrix-vector operations on-chip to minimize weight movement.

telegram · zaihuapd · Aug 31, 21:41

**Background**: High Bandwidth Memory \(HBM\) is a next-generation memory architecture that enables faster data transfer and compact integration, essential for supporting large language models and advanced graphics rendering. MRAM \(Magnetoresistive RAM\) is a spintronics-based memory technology that offers persistent storage and high endurance, making it suitable for edge-AI hardware where both model weights and intermediate states need to be stored.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mram-info.com/">MRAM -Info | MRAM Industry Portal</a></li>
<li><a href="https://www.microchipusa.com/electrical-components/ultimate-guide-to-high-bandwidth-memory">Ultimate Guide to High Bandwidth Memory</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#MRAM`, `#AI Accelerators`, `#Hardware Architecture`, `#Inference`, `#uHBM`

---

<a id="item-4"></a>
## [长鑫存储已开始小批量生产HBM3E内存 - cnBeta.COM](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB5TVNTY05ndm00OG1mbFVMVjdQTk1BYUpZREJSb25GcmwwMjNYM0tDM2luMlJ0SXpuRkdZQkRpUF94UW5IS1ZxRmV0SlpVN25QdDBzT3Bja0xNSXlUSmdCZQ?oc=5) ⭐️ 10.0/10

ChangXin Memory has begun small-batch production of HBM3E memory.

google\_news · cnBeta.COM · Aug 31, 22:41

**Tags**: `#HBM3E`, `#AI Memory`, `#Semiconductors`, `#Chips`, `#AI Compute`

---

<a id="item-5"></a>
## [ggml-org/llama.cpp released b10720](https://github.com/ggml-org/llama.cpp/releases/tag/b10720) ⭐️ 9.0/10

llama.cpp b10720 release adds ROCm radix TOP\_K optimization and provides cross-platform binaries.

github · github-actions\[bot\] · Aug 31, 23:28

**Tags**: `#llama.cpp`, `#ROCm`, `#AI`, `#cross-platform`, `#optimization`

---

<a id="item-6"></a>
## [NeurIPS accepted papers leaked? \[D\]](https://www.reddit.com/r/MachineLearning/comments/1w2r1f3/neurips_accepted_papers_leaked_d/) ⭐️ 9.0/10

A Reddit user shares a leaked GitHub repository containing ~7k NeurIPS accepted papers, seeking confirmation of its legitimacy.

reddit · r/MachineLearning · /u/Feuilius · Aug 31, 03:34

**Tags**: `#neurips`, `#machine-learning`, `#data-leak`, `#github`, `#community-discussion`

---

<a id="item-7"></a>
## [Anthropic warns of malware stealing Claude sessions](https://www.searchenginejournal.com/anthropic-warns-hackers-are-stealing-claude-sessions-to-hijack-accounts/587566/) ⭐️ 9.0/10

Anthropic has detected a malware campaign that steals Claude login sessions to hijack user accounts and consume their usage quotas. The company has forcibly logged out affected accounts and removed saved payment methods. This incident highlights a critical security vulnerability in AI service platforms where malware can bypass two-factor authentication to access sensitive user data and financial information. The malware includes Windows variants like Vidar, LummaC2, StealC, RedLine, and Acreed, as well as Mac malware named AMOS. Users are advised to stop using pirated software, clear cookies, and consider reinstalling their systems if infected.

telegram · zaihuapd · Aug 31, 11:22

**Tags**: `#security`, `#malware`, `#anthropic`, `#claude`, `#account-hijacking`

---

<a id="item-8"></a>
## [CXMT Announces Mass Production of LPDDR6 Memory](https://news.google.com/rss/articles/CBMiXEFVX3lxTE85Tk42a1hGZzJCTEhSdTZCN2NEejRfdERuNHBMd1JCS2k4WnYyZFpzWGxKcjRDLWJhaVZWRlBrNU03dE9mQzNRMldxcUFOSzNsYkVHLUVCWmNBOGlJ?oc=5) ⭐️ 9.0/10

CXMT \(ChangXin Memory Technologies\) has officially announced the mass production of its LPDDR6 memory chips, marking a significant milestone in domestic semiconductor manufacturing. LPDDR6 is a critical component for modern AI accelerators and high-performance computing systems, and achieving mass production strengthens China&\#x27;s position in the global memory supply chain. While specific technical specifications like data rates or power consumption are not detailed in the provided content, the announcement confirms the successful transition from development to mass production.

google\_news · 证券时报 · Aug 31, 00:00

**Background**: LPDDR \(Low Power Double Data Rate\) memory is a type of SDRAM designed for mobile devices and low-power computing, offering higher bandwidth and efficiency than standard DDR. LPDDR6 represents the latest generation, promising faster speeds and lower power consumption compared to LPDDR5.

**Tags**: `#semiconductors`, `#memory`, `#AI accelerators`, `#hardware`, `#mass production`

---

<a id="item-9"></a>
## [长鑫存储状告五角大楼：一家DRAM新贵的法律反击 - or100.cc](https://news.google.com/rss/articles/CBMiREFVX3lxTE9kMHJveGhJeExPcUR1VnZtVnVuZno3VmVmRUpVMzBLcGxxWTMySEVyUkdZaF9jOVRYUU00cnpieE0ybUh1?oc=5) ⭐️ 9.0/10

Chinese DRAM manufacturer CXMT sues the US Department of Defense over alleged inclusion in a blacklist.

google\_news · or100.cc · Aug 31, 11:14

**Tags**: `#DRAM`, `#semiconductors`, `#national-security`, `#export-controls`, `#legal-dispute`

---

<a id="item-10"></a>
## [Apple caught off guard by AI demand for Mac Mini and Mac Studio](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/) ⭐️ 8.0/10

Apple faces unexpected demand for Mac Mini and Mac Studio due to AI workloads, sparking debate about local vs. cloud AI training.

hackernews · thm · Aug 31, 20:41 · [Discussion](https://news.ycombinator.com/item?id=49508982)

**Tags**: `#Apple`, `#AI`, `#Mac`, `#Hardware`, `#Local AI`

---

<a id="item-11"></a>
## [I think the military commissary&\#x27;s freezers were hacked](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) ⭐️ 8.0/10

A potential hack of military commissary freezers raises concerns about infrastructure security and misconfigurations.

hackernews · jcurbo · Aug 31, 19:45 · [Discussion](https://news.ycombinator.com/item?id=49508506)

**Tags**: `#security`, `#infrastructure`, `#industrial systems`, `#military`, `#cybersecurity`

---

<a id="item-12"></a>
## [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

This article explains the dual nature of ChatGPT Work, a cloud-based and local AI productivity tool.

rss · Simon Willison · Aug 31, 07:59

**Tags**: `#AI`, `#Productivity`, `#Software Tools`, `#OpenAI`, `#Developer Experience`

---