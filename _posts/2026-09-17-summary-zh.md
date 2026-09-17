---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
content_date: 2026-09-16
lang: zh
---

> 报道范围：2026-09-16（Asia/Shanghai 自然日）

> 从 69 条内容中筛选出 11 条重要资讯。

---

1. [ggml-org/llama.cpp 发布 b11003 版本](#item-1) ⭐️ 10.0/10
2. [llama.cpp b11000 修复关键使用后释放漏洞](#item-2) ⭐️ 10.0/10
3. [ollama/ollama released v0.34.2-rc1](#item-3) ⭐️ 9.0/10
4. [Nvidia 宣布原生 GPU 编程支持 Rust](#item-4) ⭐️ 9.0/10
5. [AWS says it can&\#x27;t restore some data from mideast facilities struck by Iran](#item-5) ⭐️ 9.0/10
6. [Flock 摄像头暴露出严重的安全漏洞](#item-6) ⭐️ 9.0/10
7. [Gemini Live audio](#item-7) ⭐️ 9.0/10
8. [低质中文赌场网站暗藏危险威胁基础设施](#item-8) ⭐️ 9.0/10
9. [中国长鑫存储为腾讯供应价值 200 亿元人民币的 DRAM](#item-9) ⭐️ 9.0/10
10. [中国半导体扩产链提供投资机会](#item-10) ⭐️ 9.0/10
11. [中国国产存储芯片缩小与全球领先者的差距](#item-11) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布 b11003 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b11003) ⭐️ 10.0/10

llama.cpp b11003 版本增加了对 HrmTextForCausalLM（DFM Mimir 1B）的支持，并引入了融合 gqkv 投影和循环架构优化。

github · github-actions\[bot\] · 9月16日 23:27

**标签**: `#llama.cpp`, `#AI models`, `#software engineering`, `#hardware acceleration`, `#transformers`

---

<a id="item-2"></a>
## [llama.cpp b11000 修复关键使用后释放漏洞](https://github.com/ggml-org/llama.cpp/releases/tag/b11000) ⭐️ 10.0/10

llama.cpp 项目发布了 b11000 版本，以修复一个关键安全漏洞，该漏洞涉及缓存计算图中的悬空指针，可能导致远程代码执行。 此漏洞影响广泛使用的 llama.cpp 推理引擎，可能允许未经身份验证的远程客户端劫持系统并执行任意代码，对用户和基础设施构成重大风险。 当缓存图节点持有后端缓冲区的直接指针，而这些缓冲区随后通过 FREE\_BUFFER 释放时，会导致后续 GRAPH\_RECOMPUTE 操作中出现悬空指针。

github · github-actions\[bot\] · 9月16日 21:07

**背景**: llama.cpp 是一个用于运行大型语言模型的流行推理引擎，缓存计算图通过重用先前计算的结果而不重新发送张量数据来优化性能。

**标签**: `#llama.cpp`, `#security-vulnerability`, `#use-after-free`, `#remote-code-execution`, `#inference-engine`

---

<a id="item-3"></a>
## [ollama/ollama released v0.34.2-rc1](https://github.com/ollama/ollama/releases/tag/v0.34.2-rc1) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月16日 05:21

**标签**: `#ollama`, `#llama.cpp`, `#open-source`, `#AI`, `#version-release`

---

<a id="item-4"></a>
## [Nvidia 宣布原生 GPU 编程支持 Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 9.0/10

Nvidia 推出了 CUDA Rust，允许开发者在 Rust 中直接编写 GPU 内核，填补了主机代码和设备代码之间的差距。 这一举措提高了 GPU 内核开发的可靠性和生产力，与 Rust 在系统编程和 AI 基础设施中的日益普及相一致。 CUDA Rust 支持两条路径：从 Rust 启动现有的 CUDA 内核，以及完全用 Rust 编写新的内核，利用 Rust 的类型系统和零成本抽象。

hackernews · nonmaskable · 9月16日 19:15 · [社区讨论](https://news.ycombinator.com/item?id=49724881)

**背景**: GPU 编程传统上需要像 CUDA、HLSL 或 GLSL 这样的专用语言，但 Rust 的表达型类型系统和零成本抽象为高性能计算提供了更易维护的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/">Introducing CUDA Rust: Two Tracks for Writing GPU Kernels | NVIDIA Technical Blog</a></li>
<li><a href="https://rust-gpu.github.io/">Rust GPU</a></li>
<li><a href="https://github.com/rust-cuda/cuda-sys">GitHub - rust-cuda/cuda-sys: Rust binding to CUDA APIs · GitHub</a></li>

</ul>
</details>

**社区讨论**: 开发者们欢迎这一举措，认为它减少了编写可靠 GPU 代码的痛苦，但也有人表达了对 CUDA 专有性质和供应商锁定的担忧。

**标签**: `#Rust`, `#GPU`, `#AI`, `#Nvidia`, `#CUDA`

---

<a id="item-5"></a>
## [AWS says it can&\#x27;t restore some data from mideast facilities struck by Iran](https://www.wsj.com/world/middle-east/aws-says-it-cant-restore-some-data-from-mideast-facilities-struck-by-iran-ddcb7e5d) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · berkeleyjunk · 9月16日 05:41 · [社区讨论](https://news.ycombinator.com/item?id=49719249)

**标签**: `#AWS`, `#Cloud Infrastructure`, `#Data Security`, `#Middle East`, `#Outage`

---

<a id="item-6"></a>
## [Flock 摄像头暴露出严重的安全漏洞](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 9.0/10

《连线》杂志的调查发现，Flock 摄像头包含硬编码的凭据和 API 密钥，允许未经授权访问敏感数据。 这些漏洞危及公共监控系统的隐私和安全，可能将个人数据暴露给恶意行为者。 摄像头使用漏洞披露政策薄弱，研究人员发现物理访问可在 60 秒内获得完全控制权。

hackernews · driverdan · 9月16日 21:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 制造用于公共监控的自动车牌识别摄像头。硬编码凭据是一个严重的安全风险，因为它允许攻击者绕过身份验证机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://simeononsecurity.com/articles/flock-safety-camera-security-vulnerabilities-research-2026/">Flock Safety Camera Vulnerabilities : 50+ Flaws Found</a></li>
<li><a href="https://blog.gitguardian.com/why-its-urgent-to-deal-with-your-hard-coded-credentials/">Hardcoded Credentials Vulnerability: Why Immediate Action Matters</a></li>

</ul>
</details>

**社区讨论**: 社区评论批评 Flock 的开发实践懒惰且无能，强调了硬编码密钥和漏洞披露政策不充分的风险。

**标签**: `#security`, `#vulnerabilities`, `#hardware`, `#hardcoded-credentials`, `#vulnerability-disclosure`

---

<a id="item-7"></a>
## [Gemini Live audio](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Simon Willison · 9月16日 06:47

**标签**: `#AI`, `#Gemini`, `#Voice AI`, `#Web Development`, `#Open Source`

---

<a id="item-8"></a>
## [低质中文赌场网站暗藏危险威胁基础设施](https://www.theregister.com/security/2026/09/15/low-quality-casino-sites-conceal-highly-dangerous-threat-actors/5296652) ⭐️ 9.0/10

安全分析显示，约 170 万个低质中文赌场网站正被作为隐蔽基础设施，供 APT 组织隐藏命令与控制服务器并传播恶意软件。 这一发现意义重大，因为它展示了威胁行为者如何利用外观合法的网站来规避检测并危害用户，对组织和个人的安全构成持续威胁。 自 2023 年以来，一个与中国有关的 APT 组织使用名为 &\#x27;PeckBirdy&\#x27; 的框架，将这些恶意 C2 域名隐藏在低质赌博网站中，并通过虚假软件更新诱骗用户下载恶意程序。

telegram · zaihuapd · 9月16日 15:31

**背景**: APT 组织是复杂的、长期的网络对手，通常由国家支持。命令与控制（C2）服务器是攻击者远程管理受感染系统的中心枢纽，将它们隐藏在看似无害的网站中是一种常见的规避技术。

**标签**: `#cybersecurity`, `#APT`, `#malware`, `#infrastructure`, `#threat-intelligence`

---

<a id="item-9"></a>
## [中国长鑫存储为腾讯供应价值 200 亿元人民币的 DRAM](https://news.google.com/rss/articles/CBMioAFBVV95cUxOSWM4STlIR01xM1JvdjB0TEJNM0M1UXlBNXNsMEFTWlgwYUpsc3JaNkVEeUNFQlVDSmpna0lqNkYwdnp2V0E3a2xSdnlkdWtUZGluSE5wSG1DYWxlVnhRNGg4ZlJlQUs3eGxxVl95ZnJIQzB1THJNU3RjV00wODhESWd5a0p0TXl0QTVPT2pSNktjelltNjJ0czVpLXotYkEx?oc=5) ⭐️ 9.0/10

中国存储器制造商长鑫存储已同意向腾讯供应价值 200 亿元人民币的 DRAM 芯片。 这一重要交易凸显了中国国内存储供应链日益增长的重要性，并加强了主要科技企业之间的战略合作伙伴关系。 该交易涉及大量 DRAM 芯片，反映了中国科技行业对存储组件的巨大需求。

google\_news · 朝鮮日報中文版 · 9月16日 20:02

**背景**: 长鑫存储（CXMT）是中国领先的 DRAM 芯片制造商，与三星和 SK 海力士等全球巨头竞争。腾讯是中国最大的科技公司之一，其服务严重依赖先进硬件。

**标签**: `#semiconductors`, `#memory`, `#DRAM`, `#CXMT`, `#Tencent`

---

<a id="item-10"></a>
## [中国半导体扩产链提供投资机会](https://news.google.com/rss/articles/CBMihAFBVV95cUxOSE5zTkhVajdYUXFkNlFDRThWZ2NKMS1sV2RuVW5JVmJEaGZLamZ0Tm1kSUJzRnVtQ19xV2pwZndHR0IwOVVKRDFQSFlRNlFBWVlDcDRibnpwQy1IUVRkU2ZTVWZZVDRQVC1ndTlhTjVQYXhpaFpmX0hTNkxfYUhlbTNVb28?oc=5) ⭐️ 9.0/10

南方基金吴春林认为，中国国产半导体扩产链持续上修，市场冲击后错杀机会显现。 这一新闻具有重要意义，因为它突显了中国半导体行业的潜在增长领域，这对国家技术独立和经济发展至关重要。 文章侧重于市场趋势和投资策略，而非具体的技术突破或产品细节。

google\_news · cj.sina.cn · 9月16日 09:36

**背景**: 中国半导体行业正在迅速扩张，以减少对外国技术的依赖，这得益于政府支持和国内需求。

**标签**: `#semiconductors`, `#investment`, `#manufacturing`, `#market-trends`, `#chips`

---

<a id="item-11"></a>
## [中国国产存储芯片缩小与全球领先者的差距](https://news.google.com/rss/articles/CBMiS0FVX3lxTE9zTDNwaHEzX252R2JOb3ZuMkw3WXdJb2hMYlNVWlZWdUFVLXRocWVJcW9zQmlJM1dpNUJqYmpLdHBBTXFGSl8zWnI1cw?oc=5) ⭐️ 9.0/10

中国国产存储芯片制造商正在迅速进步，缩小与全球领先者的技术差距，NAND 约为 1 年，DRAM 约为 2 年，HBM 约为 3 年。 这一进展对全球半导体供应链和国家安全具有重要意义，因为它减少了对外国技术的依赖，并加强了中国在关键内存市场的地位。 文章强调了具体的技术差距，表明虽然国产生产正在追赶，但在 HBM 等先进内存技术方面仍存在明显差异。

google\_news · me.news · 9月16日 09:24

**背景**: 存储芯片（如 NAND 和 DRAM）是电子设备的关键组件，而 HBM（高带宽内存）对于 AI 加速器和高性能计算至关重要。

**标签**: `#semiconductors`, `#memory`, `#AI hardware`, `#China tech`, `#HBM`

---