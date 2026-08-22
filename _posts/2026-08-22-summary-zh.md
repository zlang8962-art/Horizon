---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
content_date: 2026-08-21
lang: zh
---

> 报道范围：2026-08-21（Asia/Shanghai 自然日）

> 从 123 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp 发布 b10549 版本，为 LFM2 模型添加张量分割功能](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10538 优化 Apple Silicon 上的 KV Cache](#item-2) ⭐️ 10.0/10
3. [长江存储科创板 IPO 获受理，拟融资 330 亿元](#item-3) ⭐️ 10.0/10
4. [Kagi 添加设置以过滤付费墙链接](#item-4) ⭐️ 9.0/10
5. [安全研究员意外通过 E.164 ARPA 漏洞暴露军事电话通话](#item-5) ⭐️ 9.0/10
6. [DeepSeek-v4-flash-vision-exp](#item-6) ⭐️ 9.0/10
7. [From Atari to EVE Online: Building on 15 Years of AI Research in Games](#item-7) ⭐️ 9.0/10
8. [全球增长最快的 DRAM 厂在中国！长鑫营收暴增 716%、贡献全球 11.3%增量 - 新浪财经](#item-8) ⭐️ 9.0/10
9. [长鑫之后，长江存储也要来了：存储“双雄”会师 A 股 - 网易新闻客户端](#item-9) ⭐️ 9.0/10
10. [全球增长最快 DRAM！长鑫营收暴增 716%、贡献全球 11.3%增量 - 星岛环球网](#item-10) ⭐️ 9.0/10
11. [ChatGPT search now uses the site:operator at scale](#item-11) ⭐️ 8.0/10
12. [Cloudflare OAuth 现支持可选作用域以提升用户控制力](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp 发布 b10549 版本，为 LFM2 模型添加张量分割功能](https://github.com/ggml-org/llama.cpp/releases/tag/b10549) ⭐️ 10.0/10

llama.cpp 项目发布了 b10549 版本，该版本为 LFM2 和 LFM2MOE 模型引入了张量分割支持，并提供了多种操作系统的跨平台二进制文件。 此次发布增强了框架运行高级大语言模型的能力，这对从事 AI 推理和部署的开发者及研究人员具有重要意义。 主要特性包括对 LFM2/LFM2MOE 模型的张量分割支持，禁用了 KleidiAI 和 ROCm 7.14 的构建，并为 macOS、Linux、Android 和 Windows 提供了全面的二进制文件。

github · github-actions\[bot\] · 8月21日 17:23

**背景**: llama.cpp 是一个流行的开源 C++ 实现，用于运行大型语言模型，专注于效率和跨平台兼容性。

**标签**: `#llama.cpp`, `#AI`, `#machine-learning`, `#open-source`, `#inference`

---

<a id="item-2"></a>
## [llama.cpp b10538 优化 Apple Silicon 上的 KV Cache](https://github.com/ggml-org/llama.cpp/releases/tag/b10538) ⭐️ 10.0/10

llama.cpp 版本 b10538 引入了针对 Apple Silicon 上大批次 KV Cache 解量化的优化，同时发布了适用于 macOS 和 Linux 的预编译二进制文件。 此次发布显著提高了在 Apple Silicon 设备上运行大语言模型的推理性能，使在这些平台上进行高性能 AI 计算变得更加容易获取。 该优化专注于 Metal API 在 KV Cache 解量化方面的性能，此次发布包括适用于多个平台的二进制文件，包括 macOS \(arm64 和 x64\)、Linux \(多种 CPU 和 GPU 后端\)、Windows、Android 和 openEuler。

github · github-actions\[bot\] · 8月21日 10:42

**背景**: llama.cpp 是 LLaMA 推理引擎的高性能 C++ 实现，旨在在消费级硬件上高效运行大语言模型。它支持包括 Apple Silicon 的 Metal、NVIDIA GPU 的 CUDA 以及跨平台 GPU 加速的 Vulkan 在内的多种硬件后端。

**标签**: `#llama.cpp`, `#AI inference`, `#Apple Silicon`, `#macOS`, `#optimization`

---

<a id="item-3"></a>
## [长江存储科创板 IPO 获受理，拟融资 330 亿元](https://api3.cls.cn/share/article/2461025?os=android&amp;amp;sv=8.8.2&amp;amp;app=cailianpress) ⭐️ 10.0/10

Yangtze Memory Technologies&\#x27; IPO application for 33 billion yuan is accepted by the Shanghai Stock Exchange, with Q2 2026 projections showing it becoming a top three global NAND player.

telegram · zaihuapd · 8月21日 22:26

**标签**: `#semiconductors`, `#NAND flash`, `#IPO`, `#Yangtze Memory`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Kagi 添加设置以过滤付费墙链接](https://kagi.com/changelog#11296) ⭐️ 9.0/10

Kagi 搜索引擎引入了一项新设置，允许用户从搜索结果中过滤掉付费墙链接。 这一功能解决了在付费墙后找到相关内容的挫败感，为订阅者和非订阅者都改善了用户体验。 该设置是 Kagi 持续提升隐私性和相关性的努力的一部分，因为该搜索引擎完全依赖用户订阅而非广告收入。

hackernews · speckx · 8月21日 21:56 · [社区讨论](https://news.ycombinator.com/item?id=49388154)

**背景**: 付费墙是一种数字限制，要求用户付费才能访问内容，新闻网站和在线出版物经常使用。Kagi 是一个高级、无广告的搜索引擎，优先考虑用户隐私，并依靠订阅来维持运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/spectailor/what-is-this-thing-called-a-paywall-9f378b5b4a9e">What is this thing called a Paywall ? | by Sezen Ahıskal | Medium</a></li>
<li><a href="https://blog.kagi.com/kagi-features">Kagi Blog - Kagi search features</a></li>
<li><a href="https://navtools.ai/tool/kagi">Kagi : Premium Ad-Free &amp; Private Search Engine</a></li>

</ul>
</details>

**社区讨论**: 用户们赞赏这一新功能，其中一条评论强调 Kagi 的 AI 助手是其他工具的优越替代品。另一位用户指出，Kagi 博客的顶部评论通常集中在赞扬而非内容本身。

**标签**: `#search-engine`, `#paywalls`, `#kagi`, `#software-tools`, `#user-experience`

---

<a id="item-5"></a>
## [安全研究员意外通过 E.164 ARPA 漏洞暴露军事电话通话](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 9.0/10

一名安全研究员意外通过利用 E.164 ARPA 域名（用于电话号码映射 ENUM）中的漏洞，记录了数十万次通往军事基地的电话通话。 这一发现揭示了电信基础设施中的一个关键安全漏洞，可能会暴露包括军事数据在内的敏感通信，并凸显了对遗留系统进行更好监管的必要性。 研究员使用工具查询 E.164 ARPA 域名，该域名本应将电话号码映射到互联网 URI，但发现其未得到妥善保护，从而允许未经授权访问通话记录。

hackernews · gavide · 8月21日 21:11 · [社区讨论](https://news.ycombinator.com/item?id=49387570)

**背景**: E.164 ARPA 域名是域名系统（DNS）中用于电话号码映射（ENUM）的保留部分，用于将电话号码转换为互联网地址。它由互联网号码分配机构（IANA）管理，旨在用于基础设施用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/E.164">E . 164 - Wikipedia</a></li>
<li><a href="https://www.rfc-editor.org/info/rfc2916/">RFC 2916: E . 164 number and DNS | RFC Editor</a></li>
<li><a href="https://en.wikipedia.org/wiki/.arpa">arpa - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员对这样一个漏洞存在多年却未被解决感到惊讶，有人质疑为何研究员未得到奖励，其他人则讨论了在其他遗留系统中可能存在的类似漏洞。

**标签**: `#security`, `#vulnerability`, `#telecommunications`, `#systems\_security`, `#data\_exposure`

---

<a id="item-6"></a>
## [DeepSeek-v4-flash-vision-exp](https://api-docs.deepseek.com/guides/vision/) ⭐️ 9.0/10

DeepSeek-v4-flash-vision-exp 引入了一种新的视觉模型，采用了特定的分词和调整大小策略，但用户报告其准确性与竞争对手相比存在一些问题。

hackernews · dares2573 · 8月21日 18:33 · [社区讨论](https://news.ycombinator.com/item?id=49386163)

**标签**: `#DeepSeek`, `#Vision AI`, `#Machine Learning`, `#Developer Tools`, `#LLM`

---

<a id="item-7"></a>
## [From Atari to EVE Online: Building on 15 Years of AI Research in Games](https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/) ⭐️ 9.0/10

Google DeepMind partners with game studios to prototype breakthrough AI gameplay based on 15 years of research.

rss · Google DeepMind News · 8月21日 19:59

**标签**: `#AI Research`, `#Game Development`, `#DeepMind`, `#AI Agents`, `#Prototyping`

---

<a id="item-8"></a>
## [全球增长最快的 DRAM 厂在中国！长鑫营收暴增 716%、贡献全球 11.3%增量 - 新浪财经](https://news.google.com/rss/articles/CBMihgFBVV95cUxQN19JckZ5c0FKQnN4bVNnQkVTM1ItQmVnM2hpeldBU1p1TE9QXzFVTEFmRElzV1kzLWJWOUs3d2hDdlZWcWU1M1V2OE5DSkxWRGR4elFPYVdHdFBKYTFVRTd5TC00bkpqNmoxcUdIQ3Vodzc2SjVhNEZTT255WnFQRlE0elZvdw?oc=5) ⭐️ 9.0/10

中国 DRAM 制造商长鑫存储（CXMT）报告营收暴增 716%，为全球 DRAM 市场扩张贡献了 11.3%的增量。

google\_news · 新浪财经 · 8月21日 10:53

**标签**: `#DRAM`, `#semiconductors`, `#memory`, `#AI hardware`, `#CXMT`

---

<a id="item-9"></a>
## [长鑫之后，长江存储也要来了：存储“双雄”会师 A 股 - 网易新闻客户端](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5jTndDeU1vUWM3ZmFpZlNsV3JobEdzUEFHY1Q5N1FUOWFBRm5STHRoaDJ2bEd6YUwtcjd0aWcxLXJrSWstWHNqT3ZpY0E1UUEtX0FRc2JSUzAzeERO?oc=5) ⭐️ 9.0/10

News article about Yangtze Memory Technologies potentially joining CXMT on the A-share market.

google\_news · 网易新闻客户端 · 8月21日 17:33

**标签**: `#semiconductors`, `#YMTC`, `#CXMT`, `#A-share`, `#memory`

---

<a id="item-10"></a>
## [全球增长最快 DRAM！长鑫营收暴增 716%、贡献全球 11.3%增量 - 星岛环球网](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9PZTVLWnJ1b2FwOWhIOEZZMzU0M01NTTFjTzg0V2hadnJMN2Qwb1pSdms4cFpHSXNndFVGNkdMRkxHRkVUckZaVVdxWUgteDJNb1pUOGwtb1QyUHFoalpKYlJxejJNMVk?oc=5) ⭐️ 9.0/10

长鑫存储的 DRAM 营收增长 716%，成为全球增长最快的 DRAM 厂商。

google\_news · 星岛环球网 · 8月21日 14:01

**标签**: `#DRAM`, `#长鑫存储`, `#半导体`, `#AI硬件`, `#内存市场`

---

<a id="item-11"></a>
## [ChatGPT search now uses the site:operator at scale](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/) ⭐️ 8.0/10

ChatGPT search now uses the site:operator at scale, as revealed by Promptwatch&\#x27;s tracking of search fanout queries.

rss · Simon Willison · 8月21日 07:57

**标签**: `#ChatGPT`, `#SEO`, `#Generative Engine Optimization`, `#Search`, `#Software Engineering`

---

<a id="item-12"></a>
## [Cloudflare OAuth 现支持可选作用域以提升用户控制力](https://blog.cloudflare.com/task-based-oauth-consent/) ⭐️ 8.0/10

Cloudflare OAuth 现在允许开发者在 OAuth 客户端中标记特定作用域为必需或可选，使用户在授权期间能更好地控制应用访问权限。 该功能通过减少应用可访问的数据量来提升安全性和用户隐私，符合行业对细粒度权限管理的趋势。 默认情况下，所有配置的作用域仍为必需，用户可在授权时取消选择可选作用域，必需和可选作用域会根据请求的作用域集进行评估。

rss · Cloudflare Blog · 8月21日 01:03

**背景**: OAuth 作用域是 OAuth 2.0 中限制应用访问用户账户的机制，而授权流程涉及用户批准应用访问其数据的操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oauth.net/2/scope/">OAuth 2.0 Scopes</a></li>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/">OAuth clients can now mark scopes as required or optional</a></li>
<li><a href="https://noise.getoto.net/2026/08/20/from-all-or-nothing-to-task-based-oauth-consent/">From all-or-nothing to task-based OAuth consent | Noise</a></li>

</ul>
</details>

**标签**: `#OAuth`, `#Authentication`, `#Security`, `#Cloudflare`, `#DeveloperTools`

---