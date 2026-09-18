---
layout: default
title: "Horizon Summary: 2026-09-18 (EN)"
date: 2026-09-18
content_date: 2026-09-17
lang: en
---

> Coverage: 2026-09-17 (Asia/Shanghai calendar day)

> From 79 items, 12 important content pieces were selected

---

1. [ggml-org/llama.cpp released b11026](#item-1) ⭐️ 10.0/10
2. [llama.cpp b11019 fixes critical GGUF parsing bug and adds LoRA loading](#item-2) ⭐️ 10.0/10
3. [Rust-lang warns of targeted attacks on prominent Rustaceans](#item-3) ⭐️ 10.0/10
4. [美光称其展示全球首款 512 GB DDR5 模组，2027 年具备量产条件](#item-4) ⭐️ 10.0/10
5. [GitLab.com Rate Limits Are Changing](#item-5) ⭐️ 9.0/10
6. [datasette 1.0a40](#item-6) ⭐️ 9.0/10
7. [datasette 0.65.5](#item-7) ⭐️ 9.0/10
8. [Migrating GitHub Copilot Runtime to Rust](#item-8) ⭐️ 9.0/10
9. [GoBench: Evaluating LLMs on the game of Go \[R\]](#item-9) ⭐️ 9.0/10
10. [长鑫科技的临界点时刻 - 36 Kr](#item-10) ⭐️ 9.0/10
11. [Chinese Memory Chip Market: CXMT Dominance and Cash Flow Challenges](#item-11) ⭐️ 8.0/10
12. [PC Makers Compete for ChangXin DRAM Supply, Orders Until 2027](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11026](https://github.com/ggml-org/llama.cpp/releases/tag/b11026) ⭐️ 10.0/10

llama.cpp release b11026 adds a model optimization feature and provides pre-built binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Sep 17, 21:31

**Tags**: `#llama.cpp`, `#open-source`, `#AI`, `#inference`, `#optimization`

---

<a id="item-2"></a>
## [llama.cpp b11019 fixes critical GGUF parsing bug and adds LoRA loading](https://github.com/ggml-org/llama.cpp/releases/tag/b11019) ⭐️ 10.0/10

Release b11019 of llama.cpp fixes a critical bug in GGUF file parsing where the data section was incorrectly padded from file offset 0, causing wrong tensor data for embedded GGUF files. It also introduces new functions for loading LoRA adapters and disables memory mapping with a warning when an embedded data section is not aligned. This fix is crucial for users running large language models locally, as incorrect tensor data can severely degrade model performance or cause crashes. The addition of LoRA loading functionality expands the library&\#x27;s utility for fine-tuning and adapting models, which is a key trend in AI model customization. The bug fix involves precise memory alignment logic, ensuring the data section is aligned relative to the GGUF start rather than the file. The release includes binaries for multiple platforms and hardware backends like CUDA, ROCm, and Vulkan, and is co-authored by multiple contributors including Johannes Gäßler and Claude Opus 5.

github · github-actions\[bot\] · Sep 17, 18:35

**Background**: GGUF \(GGML Universal File\) is a binary file format introduced by llama.cpp in August 2023 to store model tensors and metadata efficiently. It is designed for fast saving and loading of model data and is widely supported by tools like Hugging Face. LoRA \(Low-Rank Adaptation\) is a technique used to fine-tune large models with smaller parameter updates.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/ggml/blob/master/docs/gguf.md">ggml/docs/gguf.md at master · ggml-org/ggml</a></li>
<li><a href="https://huggingface.co/docs/hub/en/gguf">GGUF · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#GGUF`, `#AI inference`, `#open-source`, `#bugfix`

---

<a id="item-3"></a>
## [Rust-lang warns of targeted attacks on prominent Rustaceans](https://blog.rust-lang.org/2026/09/17/targeted-attacks/) ⭐️ 10.0/10

Rust-lang has identified an ongoing campaign targeting members of the Rust community and owners of popular crates to compromise devices and accounts for malware distribution. This attack highlights a growing threat to the Rust ecosystem, as attackers exploit social engineering to compromise critical infrastructure and supply chains. Attackers use video calls to trick targets into installing malicious software, often by pretending to be legitimate company profiles with LinkedIn presences.

rss · Rust Blog · Sep 17, 08:00

**Background**: Social engineering attacks manipulate individuals into divulging confidential information or performing actions that benefit the attacker. Nation-state actors, such as the DPRK, have been known to use these tactics to infiltrate systems and steal data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Social_engineering_%28security%29">Social engineering (security) - Wikipedia</a></li>
<li><a href="https://www.chaincatcher.com/en/article/2172145">Slow Fog: Social engineering attacks using malicious video call links are active again, users need to be vigilant</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#social-engineering`, `#malware`, `#rust-lang`, `#targeted-attacks`

---

<a id="item-4"></a>
## [美光称其展示全球首款 512 GB DDR5 模组，2027 年具备量产条件](https://videocardz.com/newz/micron-says-worlds-first-512gb-ddr5-module-will-be-production-ready-for-2027) ⭐️ 10.0/10

Micron unveils the world&\#x27;s first 512 GB DDR5 RDIMM with 3D stacking technology, targeting 2027 production for high-performance server memory.

telegram · zaihuapd · Sep 17, 00:15

**Tags**: `#DRAM`, `#Memory`, `#Server Hardware`, `#3D Stacking`, `#DDR5`

---

<a id="item-5"></a>
## [GitLab.com Rate Limits Are Changing](https://about.gitlab.com/blog/rate-limit-change-2026/) ⭐️ 9.0/10

GitLab.com is updating its rate limits, specifically increasing the limit for authenticated requests on the free plan to 5,000 per hour while reducing unauthenticated access to 60 per hour. This change impacts developers and AI agents relying on GitLab&\#x27;s API, potentially forcing a shift toward GraphQL for more efficient data retrieval and prompting a broader industry trend of restricting unauthenticated access. The new limits apply to all API usage, and while GraphQL is recommended for AI agents due to its ability to constrain result sets, the 5,000 requests per hour limit is still a hard cap that requires careful planning.

hackernews · darkwater · Sep 17, 23:33 · [Discussion](https://news.ycombinator.com/item?id=49742353)

**Background**: Rate limiting is a common practice to prevent abuse and ensure fair resource allocation on shared platforms like GitLab.com, where unauthenticated requests are often restricted to protect infrastructure and user data.

**Discussion**: Users debate the trade-offs, with some praising the move to restrict unauthenticated access as necessary for sustainability, while others suggest alternative models like monetizing scraped data to support open source projects.

**Tags**: `#gitlab`, `#api`, `#rate-limiting`, `#graphql`, `#ai-agents`

---

<a id="item-6"></a>
## [datasette 1.0a40](https://simonwillison.net/2026/Sep/16/datasette/) ⭐️ 9.0/10

datasette 1.0a40 introduces background task management for plugins and migrates to httpx2, along with bug fixes.

rss · Simon Willison · Sep 17, 07:51

**Tags**: `#datasette`, `#python`, `#software-development`, `#bug-fixes`, `#httpx2`

---

<a id="item-7"></a>
## [datasette 0.65.5](https://simonwillison.net/2026/Sep/16/datasette-2/) ⭐️ 9.0/10

datasette 0.65.5 fixes a security vulnerability where trailing newlines in table names could expose private rows.

rss · Simon Willison · Sep 17, 07:51

**Tags**: `#datasette`, `#security`, `#software`, `#vulnerability`, `#release`

---

<a id="item-8"></a>
## [Migrating GitHub Copilot Runtime to Rust](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/) ⭐️ 9.0/10

GitHub completely rewrote its Copilot agent runtime into over 800,000 lines of production Rust code using the Copilot CLI and app. This migration demonstrates the feasibility of using AI agents to write large-scale production code and sets a precedent for other AI runtime migrations. The rewrite spanned 128 pull requests and was shipped incrementally, leveraging the Copilot SDK for production-tested agent runtime integration.

rss · GitHub Blog · Sep 17, 08:26

**Background**: GitHub Copilot agents require an authenticated runtime, and the Copilot SDK exposes the same engine behind Copilot CLI for programmatic invocation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/integrations/by-component/agent-services/github-copilot">GitHub Copilot | Microsoft Learn</a></li>
<li><a href="https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/">Migrating the GitHub Copilot runtime to Rust, using Copilot - The GitHub Blog</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#GitHub Copilot`, `#Software Engineering`, `#AI Runtime`, `#Migration`

---

<a id="item-9"></a>
## [GoBench: Evaluating LLMs on the game of Go \[R\]](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 9.0/10

GoBench evaluates LLMs on Go games against KataGo, showing strong correlation with ARC-AGI and revealing performance gaps between models.

reddit · r/MachineLearning · /u/Roland31415 · Sep 17, 02:54

**Tags**: `#AI`, `#LLM`, `#Go`, `#Benchmark`, `#Evaluation`

---

<a id="item-10"></a>
## [长鑫科技的临界点时刻 - 36 Kr](https://news.google.com/rss/articles/CBMiTkFVX3lxTE93UDZHajV5VjdQcTBqT1B5OHNtdFFZMFNuNGZnSXJVVTluQkZ4U3pFSWlSNFZCcGxxRWRwT0VLODFoYXVucjNQU2o4eVZZZw?oc=5) ⭐️ 9.0/10

This article discusses ChangXin Memory Technologies&\#x27; critical juncture amid US sanctions and industry competition.

google\_news · 36 Kr · Sep 17, 03:17

**Tags**: `#semiconductors`, `#DRAM`, `#AI hardware`, `#supply chain`, `#China tech`

---

<a id="item-11"></a>
## [Chinese Memory Chip Market: CXMT Dominance and Cash Flow Challenges](https://news.google.com/rss/articles/CBMiUkFVX3lxTE91NTgyRlZ3Z1o4ME5qWVBpbk5neDZMVnZ3YnhwNmU1blM3QXpWb0RmZGR1OUhQWXNveXUzQWZWc3dGeEVUZkptQ3A3ZHZpYkJvS3c?oc=5) ⭐️ 8.0/10

A financial analysis reveals that ChangXin Memory Technologies \(CXMT\) has achieved a dominant position in the Chinese memory chip market, while competitors like JMicron and JMicron are facing significant cash flow pressures. This market concentration highlights the intense competition and financial fragility within the Chinese semiconductor industry, which is critical for understanding the broader supply chain dynamics and national technology strategies. The report indicates that while CXMT is thriving, other companies are struggling with liquidity, suggesting a widening gap in financial health and operational stability among Chinese memory chip manufacturers.

google\_news · Sohu · Sep 17, 23:02

**Background**: The Chinese memory chip industry is a critical sector for national technology independence, with companies like CXMT and JMicron competing to supply DRAM and NAND memory for smartphones, PCs, and data centers. Recent market trends show rising memory prices and a global upcycle, benefiting major players like CXMT, which has reached a 10% global DRAM market share.

<details><summary>References</summary>
<ul>
<li><a href="https://technode.com/2026/09/04/changxin-memory-reaches-10-of-global-dram-market-in-q2/">ChangXin Memory reaches 10% of global DRAM market in Q2 · TechNode</a></li>
<li><a href="https://www.digitimes.com/news/a20260901VL205/profit-revenue-cxmt-dram-2026.html">China&#x27;s memory chipmakers post a record 1H — but not all of it came from chips</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#market analysis`, `#ChangXin`, `#financial performance`

---

<a id="item-12"></a>
## [PC Makers Compete for ChangXin DRAM Supply, Orders Until 2027](https://news.google.com/rss/articles/CBMiYkFVX3lxTE5JQUpTVllRQXM0WVpPd2hYckkzQkhFWWxEN21lNnRaWkQxbC0xOGZLSzIwN1ZQOVdvWXpXbTl3dHlpLVhwUktDNjFGNVUxVmJtOGRUUzNXbjJ5WC1WZ0gyUDl3?oc=5) ⭐️ 8.0/10

PC manufacturers are actively competing to secure DRAM supply from ChangXin Memory Technologies \(CXMT\), with confirmed delivery schedules extending through the end of 2027. This intense competition highlights the critical importance of memory supply chains for the PC industry and reflects the growing market influence of domestic Chinese memory manufacturers. The news indicates that the current order backlog is so significant that it has pushed the delivery timeline out to 2027, suggesting a robust and sustained demand for CXMT&\#x27;s memory products.

google\_news · 体坛 · Sep 17, 09:30

**Background**: DRAM \(Dynamic Random Access Memory\) is a fundamental component in computers, providing the fast, volatile memory needed for the operating system and active applications. ChangXin Memory Technologies \(CXMT\) is a prominent Chinese semiconductor company specializing in the design and manufacturing of DRAM chips, a sector historically dominated by major global players like Samsung, SK Hynix, and Micron.

**Tags**: `#semiconductors`, `#memory`, `#DRAM`, `#manufacturing`, `#supply\_chain`

---