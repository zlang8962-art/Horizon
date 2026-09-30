---
layout: default
title: "Horizon Summary: 2026-09-30 (ZH)"
date: 2026-09-30
content_date: 2026-09-29
lang: zh
---

> 报道范围：2026-09-29（Asia/Shanghai 自然日）

> 从 102 条内容中筛选出 12 条重要资讯。

---

1. [ggml-org/llama.cpp released b11245](#item-1) ⭐️ 10.0/10
2. [llama.cpp 发布 b11242 修复 GCC 15 错误](#item-2) ⭐️ 10.0/10
3. [Cloudflare 使用前沿 AI 模型测试自适应 WAF](#item-3) ⭐️ 10.0/10
4. [长江存储首次跻身全球市场占有率前三名](#item-4) ⭐️ 10.0/10
5. [长鑫科技拟动用 180 亿人民币超募资金 加码研发和后道测试 - 联合早报](#item-5) ⭐️ 10.0/10
6. [PS5 复发漏洞利用](#item-6) ⭐️ 9.0/10
7. [A Privacy Analysis of Web and Mobile Conversational AI Agents \[pdf\]](#item-7) ⭐️ 9.0/10
8. [OpenAI DevDay 2026 实时博客](#item-8) ⭐️ 9.0/10
9. [Claude Sonnet 5.5：更快、更便宜、更出色](#item-9) ⭐️ 9.0/10
10. [GLM-5.3 稀疏注意力如何影响 HBM 内存使用](#item-10) ⭐️ 9.0/10
11. [Using AI to chart a course for our post-quantum migration](#item-11) ⭐️ 9.0/10
12. [我们如何利用开源 AI 安全代理发现 24 个 Android 漏洞](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11245](https://github.com/ggml-org/llama.cpp/releases/tag/b11245) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月29日 14:13

**标签**: `#llama.cpp`, `#AI inference`, `#software engineering`, `#cross-platform`, `#optimization`

---

<a id="item-2"></a>
## [llama.cpp 发布 b11242 修复 GCC 15 错误](https://github.com/ggml-org/llama.cpp/releases/tag/b11242) ⭐️ 10.0/10

llama.cpp 版本 b11242 修复了 GCC 15 的 stringop-overflow 错误，并提供了用于 AI 推理的跨平台二进制文件。 此次发布意义重大，因为它解决了 GCC 15 用户的编译问题，并扩大了高效 LLM 推理在不同硬件平台上的可访问性。 更新包括对 decode\_embd\_batch 函数的修复，并因编译问题禁用了 macOS Apple Silicon 的 KleidiAI 支持，同时为 Linux、Windows、macOS 和 Android 提供了广泛的二进制选项。

github · github-actions\[bot\] · 9月29日 07:49

**背景**: llama.cpp 是一个领先的 C++ 推理引擎，旨在在各种硬件架构和边缘设备上高效运行大型语言模型（LLM）。它支持包括 CUDA、Vulkan、OpenVINO 和 SYCL 在内的多种后端，使其成为本地 AI 部署的通用工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://llama-cpp.com/">Llama.cpp - Run LLM Inference in C/C++</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#C++`, `#cross-platform`, `#GCC 15`

---

<a id="item-3"></a>
## [Cloudflare 使用前沿 AI 模型测试自适应 WAF](https://blog.cloudflare.com/adaptive-ai-waf-testing/) ⭐️ 10.0/10

Cloudflare 开发了一种自适应 Web 应用防火墙（WAF）测试工具，该工具会根据之前的拦截或放行结果动态调整请求，并在授权的测试环境中揭示了六个攻击类别中的检测漏洞。 这种测试方法突出了当前 WAF 实现中的关键安全漏洞，展示了自适应测试如何发现静态方法可能遗漏的盲点，并促使进行必要的安全改进。 测试工具在反馈循环中运行，每个请求都会根据 WAF 的响应进行修改，使系统能够探索固定测试套件无法生成的攻击变体。

rss · Cloudflare Blog · 9月29日 21:00

**背景**: Web 应用防火墙（WAF）通过过滤和监控 Web 应用与互联网之间的 HTTP 流量来保护 Web 应用，识别并阻止恶意流量。

**标签**: `#WAF`, `#Security Testing`, `#AI Models`, `#Cloudflare`, `#Web Application Security`

---

<a id="item-4"></a>
## [长江存储首次跻身全球市场占有率前三名](https://news.google.com/rss/articles/CBMiSkFVX3lxTE5EYmhCQXRaVk1ORDVJTlVKN29XVlpCdC1HZDJQSDZRVU5ONks5MDFHUG5lamdmYXpvaUMtSUpxVTZqV3BfeDlpVDl3?oc=5) ⭐️ 10.0/10

长江存储（YMTC）已超越美光、铠侠和闪迪，成为全球第三大 NAND 闪存供应商，市场占有率达到 14%。 这一里程碑标志着全球半导体格局的重大转变，挑战了传统西方供应商，并减少了对它们的依赖。 尽管市场占有率排名第三，但 YMTC 的收入份额仅排名第五，表明其平均售价低于三星和 SK 海力士等竞争对手。

google\_news · 集微网 · 9月29日 18:09

**背景**: 长江存储成立于 2016 年，总部位于武汉，是中国领先的 NAND 闪存制造商，自 2022 年 12 月起面临美国制裁。该公司正在推进 IPO，估值在 2-3 万亿元人民币之间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalcitizen.life/ymtc-becomes-worlds-third-largest-nand-supplier-with-14-percent-market-share/">YMTC Becomes World’s Third Largest NAND Supplier With 14 Percent Market Share</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory`, `#YMTC`, `#market-share`, `#chips`

---

<a id="item-5"></a>
## [长鑫科技拟动用 180 亿人民币超募资金 加码研发和后道测试 - 联合早报](https://news.google.com/rss/articles/CBMiakFVX3lxTE5UQW9mbEFPc3R4UktxWl9kUXJMaXVUcjVwVUxNRDNJVnBEamx4NEkwWWstUHpOZVlTdGFZeUJLZzhsZVoxcmw2RTA2V3p5NHBKaUpnNkl3NkdHOVBRZUVndy1PdlhyYjNBY2c?oc=5) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

google\_news · 联合早报 · 9月29日 10:05

**标签**: `#semiconductors`, `#AI accelerators`, `#chip manufacturing`, `#investment`, `#memory`

---

<a id="item-6"></a>
## [PS5 复发漏洞利用](https://github.com/ntfargo/Relapse-Exploit) ⭐️ 9.0/10

一款针对 WebKit JavaScriptCore JIT 引擎的 PS5 漏洞利用程序。

hackernews · therepanic · 9月29日 23:44 · [社区讨论](https://news.ycombinator.com/item?id=49895304)

**标签**: `#security`, `#exploit`, `#WebKit`, `#PS5`, `#JavaScriptCore`

---

<a id="item-7"></a>
## [A Privacy Analysis of Web and Mobile Conversational AI Agents \[pdf\]](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-%28clean%29.pdf) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · damaru2 · 9月29日 17:03 · [社区讨论](https://news.ycombinator.com/item?id=49890226)

**标签**: `#privacy`, `#ai`, `#security`, `#conversational-ai`, `#data-exposure`

---

<a id="item-8"></a>
## [OpenAI DevDay 2026 实时博客](https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/) ⭐️ 9.0/10

一篇关于 OpenAI DevDay 2026 的实时博客，重点关注人工智能和大型语言模型的发展。

rss · Simon Willison · 9月29日 23:55

**标签**: `#ai`, `#openai`, `#llms`, `#generative-ai`, `#coding-agents`

---

<a id="item-9"></a>
## [Claude Sonnet 5.5：更快、更便宜、更出色](https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/) ⭐️ 9.0/10

Anthropic 发布了 Claude Sonnet 5.5，这是一款新模型，运行速度比前代快 30% 以上，成本降低多达 30%，同时在所有基准测试中都有所提升。 这次发布意义重大，因为它使 Anthropic 的强大模型更加可及且具有成本效益，可能会改变 AI 助手市场的竞争格局。 Sonnet 5.5 现在是 claude.ai 免费层级的模型，为 OpenAI 的 ChatGPT 免费层级提供了更强大的替代方案，但在被推向极端思考努力时，仍然存在与 Opus 5.5 相同的 token 限制漏洞。

rss · Simon Willison · 9月29日 06:07

**背景**: Anthropic 是一家 AI 安全公司，开发像 Claude 这样的大型语言模型。这些模型在大量文本数据上训练，以理解和生成类人文本，不同的模型变体（如 Sonnet 和 Opus）提供不同的能力水平和成本。

**标签**: `#AI`, `#Machine Learning`, `#Claude`, `#Model Performance`, `#Cost Optimization`

---

<a id="item-10"></a>
## [GLM-5.3 稀疏注意力如何影响 HBM 内存使用](https://newsletter.semianalysis.com/p/sparse-savings-persistent-demand-inside-glm53) ⭐️ 9.0/10

GLM-5.3 引入了先进的稀疏注意力机制，包括 HiSparse 和 IndexShare，以优化 HBM 内存使用并提高计算效率。 这一突破解决了 AI 计算效率和软硬件协同设计中的关键挑战，使模型推理更加可扩展和具有成本效益。 文章详细说明了稀疏注意力如何减少内存占用，并讨论了权衡，例如单轮次异步优化对性能的影响。

rss · Semianalysis · 9月29日 03:26

**背景**: HBM（高带宽内存）是 AI 加速器中的关键组件，而稀疏注意力机制允许模型专注于相关标记，从而减少冗余计算。

**标签**: `#GLM-5.3`, `#Sparse Attention`, `#HBM Memory`, `#AI Compute`, `#Hardware-Software Co-design`

---

<a id="item-11"></a>
## [Using AI to chart a course for our post-quantum migration](https://blog.cloudflare.com/ai-driven-cryptography-discovery/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Cloudflare Blog · 9月29日 21:00

**标签**: `#AI`, `#Cryptography`, `#Post-Quantum Security`, `#Software Engineering`, `#Cloudflare`

---

<a id="item-12"></a>
## [我们如何利用开源 AI 安全代理发现 24 个 Android 漏洞](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/) ⭐️ 9.0/10

GitHub 博客文章详细介绍了开源 AI 安全代理是如何发现 24 个 Android 漏洞的，并为开发者提供了可操作的见解。

rss · GitHub Blog · 9月29日 03:00

**标签**: `#AI Security`, `#Android Vulnerabilities`, `#Open Source Tools`, `#Software Security`, `#Developer Tools`

---