---
layout: default
title: "Horizon Summary: 2026-09-17 (EN)"
date: 2026-09-17
content_date: 2026-09-16
lang: en
---

> Coverage: 2026-09-16 (Asia/Shanghai calendar day)

> From 69 items, 11 important content pieces were selected

---

1. [ggml-org/llama.cpp released b11003](#item-1) ⭐️ 10.0/10
2. [llama.cpp b11000 Fixes Critical Use-After-Free Vulnerability](#item-2) ⭐️ 10.0/10
3. [ollama/ollama released v0.34.2-rc1](#item-3) ⭐️ 9.0/10
4. [Nvidia Announces Native GPU Programming in Rust](#item-4) ⭐️ 9.0/10
5. [AWS says it can&\#x27;t restore some data from mideast facilities struck by Iran](#item-5) ⭐️ 9.0/10
6. [Flock Cameras Exposed to Critical Security Vulnerabilities](#item-6) ⭐️ 9.0/10
7. [Gemini Live audio](#item-7) ⭐️ 9.0/10
8. [Low-quality Chinese casino sites hide dangerous threat infrastructure](#item-8) ⭐️ 9.0/10
9. [CXMT Supplies Tencent with 20 Billion RMB Worth of DRAM](#item-9) ⭐️ 9.0/10
10. [China&\#x27;s Semiconductor Expansion Chain Offers Investment Opportunities](#item-10) ⭐️ 9.0/10
11. [China&\#x27;s Domestic Storage Chips Close Gap with Global Leaders](#item-11) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11003](https://github.com/ggml-org/llama.cpp/releases/tag/b11003) ⭐️ 10.0/10

llama.cpp release b11003 adds support for HrmTextForCausalLM \(DFM Mimir 1B\) with fused gqkv projection and looped architecture optimizations.

github · github-actions\[bot\] · Sep 16, 23:27

**Tags**: `#llama.cpp`, `#AI models`, `#software engineering`, `#hardware acceleration`, `#transformers`

---

<a id="item-2"></a>
## [llama.cpp b11000 Fixes Critical Use-After-Free Vulnerability](https://github.com/ggml-org/llama.cpp/releases/tag/b11000) ⭐️ 10.0/10

The llama.cpp project released version b11000 to fix a critical security vulnerability where dangling pointers in cached compute graphs could lead to remote code execution. This vulnerability affects the widely used llama.cpp inference engine, potentially allowing unauthenticated remote clients to hijack the system and execute arbitrary code, posing a significant risk to users and infrastructure. The bug occurs when cached graph nodes hold direct pointers to backend buffers that are later freed via FREE\_BUFFER, causing dangling pointers during subsequent GRAPH\_RECOMPUTE operations.

github · github-actions\[bot\] · Sep 16, 21:07

**Background**: llama.cpp is a popular inference engine for running large language models, and cached compute graphs are used to optimize performance by reusing previously computed results without resending tensor data.

**Tags**: `#llama.cpp`, `#security-vulnerability`, `#use-after-free`, `#remote-code-execution`, `#inference-engine`

---

<a id="item-3"></a>
## [ollama/ollama released v0.34.2-rc1](https://github.com/ollama/ollama/releases/tag/v0.34.2-rc1) ⭐️ 9.0/10

Ollama v0.34.2-rc1 release includes llama.cpp updates.

github · github-actions\[bot\] · Sep 16, 05:21

**Tags**: `#ollama`, `#llama.cpp`, `#open-source`, `#AI`, `#version-release`

---

<a id="item-4"></a>
## [Nvidia Announces Native GPU Programming in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 9.0/10

Nvidia introduces CUDA Rust, enabling developers to write GPU kernels directly in Rust, closing the gap between host and device code. This move enhances reliability and productivity in GPU kernel development, aligning with Rust&\#x27;s growing adoption in systems programming and AI infrastructure. CUDA Rust supports two tracks: launching existing CUDA kernels from Rust and writing new kernels entirely in Rust, leveraging Rust&\#x27;s type system and zero-cost abstractions.

hackernews · nonmaskable · Sep 16, 19:15 · [Discussion](https://news.ycombinator.com/item?id=49724881)

**Background**: GPU programming traditionally requires specialized languages like CUDA, HLSL, or GLSL, but Rust&\#x27;s expressive type system and zero-cost abstractions offer a more maintainable alternative for high-performance computing.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/">Introducing CUDA Rust: Two Tracks for Writing GPU Kernels | NVIDIA Technical Blog</a></li>
<li><a href="https://rust-gpu.github.io/">Rust GPU</a></li>
<li><a href="https://github.com/rust-cuda/cuda-sys">GitHub - rust-cuda/cuda-sys: Rust binding to CUDA APIs · GitHub</a></li>

</ul>
</details>

**Discussion**: Developers welcome the move, noting it reduces pain in writing reliable GPU code, though some express concerns about CUDA&\#x27;s proprietary nature and vendor lock-in.

**Tags**: `#Rust`, `#GPU`, `#AI`, `#Nvidia`, `#CUDA`

---

<a id="item-5"></a>
## [AWS says it can&\#x27;t restore some data from mideast facilities struck by Iran](https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d) ⭐️ 9.0/10

AWS reports inability to restore data from Middle East data centers struck by Iran, with community discussion highlighting data residency challenges and outage tracking.

hackernews · berkeleyjunk · Sep 16, 05:41 · [Discussion](https://news.ycombinator.com/item?id=49719249)

**Tags**: `#AWS`, `#Cloud Infrastructure`, `#Data Security`, `#Middle East`, `#Outage`

---

<a id="item-6"></a>
## [Flock Cameras Exposed to Critical Security Vulnerabilities](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 9.0/10

A Wired investigation revealed that Flock cameras contain hardcoded credentials and API keys, allowing unauthorized access to sensitive data. These vulnerabilities compromise the privacy and security of public surveillance systems, potentially exposing personal data to malicious actors. The cameras use weak vulnerability disclosure policies, and researchers found that physical access can grant full control in under 60 seconds.

hackernews · driverdan · Sep 16, 21:18 · [Discussion](https://news.ycombinator.com/item?id=49726586)

**Background**: Flock Safety manufactures automated license plate recognition cameras used for public surveillance. Hardcoded credentials are a critical security risk, as they allow attackers to bypass authentication mechanisms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/">Flock Safety Camera Vulnerabilities : 50+ Flaws Found</a></li>
<li><a href="https://blog.gitguardian.com/why-its-urgent-to-deal-with-your-hard-coded-credentials/">Hardcoded Credentials Vulnerability: Why Immediate Action Matters</a></li>

</ul>
</details>

**Discussion**: Community comments criticize Flock&\#x27;s development practices as lazy and incompetent, highlighting the risks of hardcoded secrets and inadequate disclosure policies.

**Tags**: `#security`, `#vulnerabilities`, `#hardware`, `#hardcoded-credentials`, `#vulnerability-disclosure`

---

<a id="item-7"></a>
## [Gemini Live audio](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 9.0/10

Simon Willison builds a web UI for Google&\#x27;s Gemini 3.8 Live speech-to-speech models, enabling voice conversations with interruption capabilities.

rss · Simon Willison · Sep 16, 06:47

**Tags**: `#AI`, `#Gemini`, `#Voice AI`, `#Web Development`, `#Open Source`

---

<a id="item-8"></a>
## [Low-quality Chinese casino sites hide dangerous threat infrastructure](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 9.0/10

A security analysis reveals that approximately 1.7 million low-quality Chinese casino websites are being exploited as a covert infrastructure for APT groups to hide command-and-control servers and spread malware. This discovery is significant because it demonstrates how threat actors can abuse legitimate-looking websites to evade detection and compromise users, posing a persistent threat to organizations and individuals alike. Since 2023, a China-linked APT group has used the &\#x27;PeckBirdy&\#x27; framework to hide malicious C2 domains within these low-quality gambling sites and trick users into downloading malware via fake software updates.

telegram · zaihuapd · Sep 16, 15:31

**Background**: APT groups are sophisticated, long-term cyber adversaries often state-sponsored. Command-and-control \(C2\) servers are the central hub where attackers remotely manage infected systems, and hiding them within benign-looking websites is a common evasion technique.

**Tags**: `#cybersecurity`, `#APT`, `#malware`, `#infrastructure`, `#threat-intelligence`

---

<a id="item-9"></a>
## [CXMT Supplies Tencent with 20 Billion RMB Worth of DRAM](https://news.google.com/rss/articles/CBMioAFBVV95cUxOSWM4STlIR01xM1JvdjB0TEJNM0M1UXlBNXNsMEFTWlgwYUpsc3JaNkVEeUNFQlVDSmpna0lqNkYwdnp2V0E3a2xSdnlkdWtUZGluSE5wSG1DYWxlVnhRNGg4ZlJlQUs3eGxxVl95ZnJIQzB1THJNU3RjV00wODhESWd5a0p0TXl0QTVPT2pSNktjelltNjJ0czVpLXotYkEx?oc=5) ⭐️ 9.0/10

Chinese memory manufacturer CXMT has agreed to supply DRAM chips worth 20 billion RMB to Tencent. This significant deal highlights the growing importance of domestic memory supply chains in China and strengthens the strategic partnership between major tech firms. The transaction involves a substantial volume of DRAM chips, reflecting the high demand for memory components in China&\#x27;s technology sector.

google\_news · 朝鮮日報中文版 · Sep 16, 20:02

**Background**: CXMT, or China Xiangyuan Memory Technology, is a leading Chinese manufacturer of DRAM chips, competing with global giants like Samsung and SK Hynix. Tencent is one of China&\#x27;s largest technology companies, heavily reliant on advanced hardware for its services.

**Tags**: `#semiconductors`, `#memory`, `#DRAM`, `#CXMT`, `#Tencent`

---

<a id="item-10"></a>
## [China&\#x27;s Semiconductor Expansion Chain Offers Investment Opportunities](https://news.google.com/rss/articles/CBMihAFBVV95cUxOSE5zTkhVajdYUXFkNlFDRThWZ2NKMS1sV2RuVW5JVmJEaGZLamZ0Tm1kSUJzRnVtQ19xV2pwZndHR0IwOVVKRDFQSFlRNlFBWVlDcDRibnpwQy1IUVRkU2ZTVWZZVDRQVC1ndTlhTjVQYXhpaFpmX0hTNkxfYUhlbTNVb28?oc=5) ⭐️ 9.0/10

Southern Fund&\#x27;s Wu Chunlin suggests that China&\#x27;s domestic semiconductor expansion chain continues to be upgraded, revealing investment opportunities after market corrections. This news is significant as it highlights potential growth areas in China&\#x27;s semiconductor industry, which is crucial for national technological independence and economic development. The article focuses on market trends and investment strategies rather than specific technical breakthroughs or product details.

google\_news · cj.sina.cn · Sep 16, 09:36

**Background**: China&\#x27;s semiconductor industry has been expanding rapidly to reduce reliance on foreign technology, driven by government support and domestic demand.

**Tags**: `#semiconductors`, `#investment`, `#manufacturing`, `#market-trends`, `#chips`

---

<a id="item-11"></a>
## [China&\#x27;s Domestic Storage Chips Close Gap with Global Leaders](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9zTDNwaHEzX252R2JOb3ZuMkw3WXdJb2hMYlNVWlZWdUFVLXRocWVJcW9zQmlJM1dpNUJqYmpLdHBBTXFGSl8zWnI1cw?oc=5) ⭐️ 9.0/10

China&\#x27;s domestic storage chip manufacturers are rapidly advancing, narrowing the technology gap with global leaders to approximately one year for NAND, two years for DRAM, and three years for HBM. This progress is significant for the global semiconductor supply chain and national security, as it reduces reliance on foreign technology and strengthens China&\#x27;s position in critical memory markets. The article highlights specific technology gaps, indicating that while domestic production is catching up, there are still distinct differences in advanced memory technologies like HBM.

google\_news · me.news · Sep 16, 09:24

**Background**: Storage chips, such as NAND and DRAM, are essential components in electronic devices, while HBM \(High Bandwidth Memory\) is crucial for AI accelerators and high-performance computing.

**Tags**: `#semiconductors`, `#memory`, `#AI hardware`, `#China tech`, `#HBM`

---