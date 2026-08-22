---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
content_date: 2026-08-21
lang: en
---

> Coverage: 2026-08-21 (Asia/Shanghai calendar day)

> From 123 items, 12 important content pieces were selected

---

1. [llama.cpp Release b10549 Adds Tensor Split for LFM2 Models](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10538 Optimizes KV Cache for Apple Silicon](#item-2) ⭐️ 10.0/10
3. [长江存储科创板 IPO 获受理，拟融资 330 亿元](#item-3) ⭐️ 10.0/10
4. [Kagi Adds Setting to Filter Paywalled Links](#item-4) ⭐️ 9.0/10
5. [Security researcher accidentally exposed military phone calls via E.164 ARPA vulnerability](#item-5) ⭐️ 9.0/10
6. [DeepSeek-v4-flash-vision-exp](#item-6) ⭐️ 9.0/10
7. [From Atari to EVE Online: Building on 15 Years of AI Research in Games](#item-7) ⭐️ 9.0/10
8. [全球增长最快的DRAM厂在中国！长鑫营收暴增716%、贡献全球11.3%增量 - 新浪财经](#item-8) ⭐️ 9.0/10
9. [长鑫之后，长江存储也要来了：存储“双雄”会师A股 - 网易新闻客户端](#item-9) ⭐️ 9.0/10
10. [全球增长最快DRAM！长鑫营收暴增716%、贡献全球11.3%增量 - 星岛环球网](#item-10) ⭐️ 9.0/10
11. [ChatGPT search now uses the site:operator at scale](#item-11) ⭐️ 8.0/10
12. [Cloudflare OAuth Now Supports Optional Scopes for Better User Control](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp Release b10549 Adds Tensor Split for LFM2 Models](https://github.com/ggml-org/llama.cpp/releases/tag/b10549) ⭐️ 10.0/10

The llama.cpp project released version b10549, which introduces tensor split support for LFM2 and LFM2MOE models, alongside a wide range of cross-platform binaries for various operating systems. This release enhances the framework&\#x27;s ability to run advanced large language models efficiently, which is significant for developers and researchers working on AI inference and deployment. Key features include support for tensor split on LFM2/LFM2MOE models, disabled builds for KleidiAI and ROCm 7.14, and a comprehensive set of binaries for macOS, Linux, Android, and Windows.

github · github-actions\[bot\] · Aug 21, 17:23

**Background**: llama.cpp is a popular open-source C++ implementation for running large language models, focusing on efficiency and cross-platform compatibility.

**Tags**: `#llama.cpp`, `#AI`, `#machine-learning`, `#open-source`, `#inference`

---

<a id="item-2"></a>
## [llama.cpp b10538 Optimizes KV Cache for Apple Silicon](https://github.com/ggml-org/llama.cpp/releases/tag/b10538) ⭐️ 10.0/10

llama.cpp version b10538 introduces an optimization for KV cache dequantization specifically targeting large batches on Apple Silicon, while also releasing pre-built binaries for macOS and Linux. This release significantly improves inference performance for users running large language models on Apple Silicon devices, making high-performance AI computing more accessible on these platforms. The optimization focuses on Metal API performance for KV cache dequantization, and the release includes binaries for multiple platforms including macOS \(arm64 and x64\), Linux \(various CPU and GPU backends\), Windows, Android, and openEuler.

github · github-actions\[bot\] · Aug 21, 10:42

**Background**: llama.cpp is a high-performance C++ implementation of the LLaMA inference engine, designed to run large language models efficiently on consumer hardware. It supports various hardware backends including Metal for Apple Silicon, CUDA for NVIDIA GPUs, and Vulkan for cross-platform GPU acceleration.

**Tags**: `#llama.cpp`, `#AI inference`, `#Apple Silicon`, `#macOS`, `#optimization`

---

<a id="item-3"></a>
## [长江存储科创板 IPO 获受理，拟融资 330 亿元](https://api3.cls.cn/share/article/2461025?os=android&amp;amp;sv=8.8.2&amp;amp;app=cailianpress) ⭐️ 10.0/10

Yangtze Memory Technologies&\#x27; IPO application for 33 billion yuan is accepted by the Shanghai Stock Exchange, with Q2 2026 projections showing it becoming a top three global NAND player.

telegram · zaihuapd · Aug 21, 22:26

**Tags**: `#semiconductors`, `#NAND flash`, `#IPO`, `#Yangtze Memory`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Kagi Adds Setting to Filter Paywalled Links](https://kagi.com/changelog#11296) ⭐️ 9.0/10

Kagi search engine has introduced a new setting that allows users to filter out paywalled links from their search results. This feature addresses the frustration of finding relevant content behind paywalls, improving the user experience for subscribers and non-subscribers alike. The setting is part of Kagi&\#x27;s ongoing efforts to enhance privacy and relevance, as the search engine relies entirely on user subscriptions rather than ad revenue.

hackernews · speckx · Aug 21, 21:56 · [Discussion](https://news.ycombinator.com/item?id=49388154)

**Background**: A paywall is a digital restriction that requires users to pay for access to content, commonly used by news sites and online publications. Kagi is a premium, ad-free search engine that prioritizes user privacy and relies on subscriptions for sustainability.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/spectailor/what-is-this-thing-called-a-paywall-9f378b5b4a9e">What is this thing called a Paywall ? | by Sezen Ahıskal | Medium</a></li>
<li><a href="https://blog.kagi.com/kagi-features">Kagi Blog - Kagi search features</a></li>
<li><a href="https://navtools.ai/tool/kagi">Kagi : Premium Ad-Free &amp; Private Search Engine</a></li>

</ul>
</details>

**Discussion**: Users appreciate the new feature, with one comment highlighting Kagi&\#x27;s AI Assistant as a superior alternative to other tools. Another user noted that the top comments on Kagi blogs often focus on praise rather than the content itself.

**Tags**: `#search-engine`, `#paywalls`, `#kagi`, `#software-tools`, `#user-experience`

---

<a id="item-5"></a>
## [Security researcher accidentally exposed military phone calls via E.164 ARPA vulnerability](https://lina.sh/blog/hijacking-e164-arpa) ⭐️ 9.0/10

A security researcher accidentally logged hundreds of thousands of phone calls to military bases by exploiting a vulnerability in the E.164 ARPA domain, which is used for telephone number mapping \(ENUM\). This discovery reveals a critical security flaw in the telecommunications infrastructure that could expose sensitive communications, including military data, and highlights the need for better oversight of legacy systems. The researcher used a tool to query the E.164 ARPA domain, which is supposed to map phone numbers to Internet URIs, but found it was not properly secured, allowing unauthorized access to call logs.

hackernews · gavide · Aug 21, 21:11 · [Discussion](https://news.ycombinator.com/item?id=49387570)

**Background**: The E.164 ARPA domain is a reserved part of the Domain Name System \(DNS\) used for telephone number mapping \(ENUM\), which translates phone numbers into Internet addresses. It is managed by the Internet Assigned Numbers Authority \(IANA\) and is intended for infrastructure purposes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/E.164">E . 164 - Wikipedia</a></li>
<li><a href="https://www.rfc-editor.org/info/rfc2916/">RFC 2916: E . 164 number and DNS | RFC Editor</a></li>
<li><a href="https://en.wikipedia.org/wiki/.arpa">arpa - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed surprise that such a vulnerability existed for years without being addressed, with some questioning why the researcher was not rewarded and others discussing the potential for similar exploits in other legacy systems.

**Tags**: `#security`, `#vulnerability`, `#telecommunications`, `#systems\_security`, `#data\_exposure`

---

<a id="item-6"></a>
## [DeepSeek-v4-flash-vision-exp](https://api-docs.deepseek.com/guides/vision/) ⭐️ 9.0/10

DeepSeek-v4-flash-vision-exp introduces a new vision model with specific tokenization and resizing strategies, but users report accuracy issues compared to competitors.

hackernews · dares2573 · Aug 21, 18:33 · [Discussion](https://news.ycombinator.com/item?id=49386163)

**Tags**: `#DeepSeek`, `#Vision AI`, `#Machine Learning`, `#Developer Tools`, `#LLM`

---

<a id="item-7"></a>
## [From Atari to EVE Online: Building on 15 Years of AI Research in Games](https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/) ⭐️ 9.0/10

Google DeepMind partners with game studios to prototype breakthrough AI gameplay based on 15 years of research.

rss · Google DeepMind News · Aug 21, 19:59

**Tags**: `#AI Research`, `#Game Development`, `#DeepMind`, `#AI Agents`, `#Prototyping`

---

<a id="item-8"></a>
## [全球增长最快的DRAM厂在中国！长鑫营收暴增716%、贡献全球11.3%增量 - 新浪财经](https://news.google.com/rss/articles/CBMihgFBVV95cUxQN19JckZ5c0FKQnN4bVNnQkVTM1ItQmVnM2hpeldBU1p1TE9QXzFVTEFmRElzV1kzLWJWOUs3d2hDdlZWcWU1M1V2OE5DSkxWRGR4elFPYVdHdFBKYTFVRTd5TC00bkpqNmoxcUdIQ3Vodzc2SjVhNEZTT255WnFQRlE0elZvdw?oc=5) ⭐️ 9.0/10

Chinese DRAM manufacturer CXMT reported 716% revenue growth, contributing 11.3% of global DRAM market expansion.

google\_news · 新浪财经 · Aug 21, 10:53

**Tags**: `#DRAM`, `#semiconductors`, `#memory`, `#AI hardware`, `#CXMT`

---

<a id="item-9"></a>
## [长鑫之后，长江存储也要来了：存储“双雄”会师A股 - 网易新闻客户端](https://news.google.com/rss/articles/CBMiXEFVX3lxTE5jTndDeU1vUWM3ZmFpZlNsV3JobEdzUEFHY1Q5N1FUOWFBRm5STHRoaDJ2bEd6YUwtcjd0aWcxLXJrSWstWHNqT3ZpY0E1UUEtX0FRc2JSUzAzeERO?oc=5) ⭐️ 9.0/10

News article about Yangtze Memory Technologies potentially joining CXMT on the A-share market.

google\_news · 网易新闻客户端 · Aug 21, 17:33

**Tags**: `#semiconductors`, `#YMTC`, `#CXMT`, `#A-share`, `#memory`

---

<a id="item-10"></a>
## [全球增长最快DRAM！长鑫营收暴增716%、贡献全球11.3%增量 - 星岛环球网](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9PZTVLWnJ1b2FwOWhIOEZZMzU0M01NTTFjTzg0V2hadnJMN2Qwb1pSdms4cFpHSXNndFVGNkdMRkxHRkVUckZaVVdxWUgteDJNb1pUOGwtb1QyUHFoalpKYlJxejJNMVk?oc=5) ⭐️ 9.0/10

长鑫存储的DRAM营收增长716%，成为全球增长最快的DRAM厂商。

google\_news · 星岛环球网 · Aug 21, 14:01

**Tags**: `#DRAM`, `#长鑫存储`, `#半导体`, `#AI硬件`, `#内存市场`

---

<a id="item-11"></a>
## [ChatGPT search now uses the site:operator at scale](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/) ⭐️ 8.0/10

ChatGPT search now uses the site:operator at scale, as revealed by Promptwatch&\#x27;s tracking of search fanout queries.

rss · Simon Willison · Aug 21, 07:57

**Tags**: `#ChatGPT`, `#SEO`, `#Generative Engine Optimization`, `#Search`, `#Software Engineering`

---

<a id="item-12"></a>
## [Cloudflare OAuth Now Supports Optional Scopes for Better User Control](https://blog.cloudflare.com/task-based-oauth-consent/) ⭐️ 8.0/10

Cloudflare OAuth now allows developers to mark specific scopes as required or optional, giving users more control over app access during authorization. This feature improves security and user privacy by reducing the amount of data an app can access, aligning with the industry trend of granular permission management. By default, all configured scopes remain required, and optional scopes can be deselected by users at authorization time, with required and optional scopes evaluated against the requested set.

rss · Cloudflare Blog · Aug 21, 01:03

**Background**: OAuth scopes are mechanisms in OAuth 2.0 to limit an application&\#x27;s access to a user&\#x27;s account, while consent flows involve users approving an app&\#x27;s access to their data.

<details><summary>References</summary>
<ul>
<li><a href="https://oauth.net/2/scope/">OAuth 2.0 Scopes</a></li>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-08-20-oauth-optional-scopes/">OAuth clients can now mark scopes as required or optional</a></li>
<li><a href="https://noise.getoto.net/2026/08/20/from-all-or-nothing-to-task-based-oauth-consent/">From all-or-nothing to task-based OAuth consent | Noise</a></li>

</ul>
</details>

**Tags**: `#OAuth`, `#Authentication`, `#Security`, `#Cloudflare`, `#DeveloperTools`

---