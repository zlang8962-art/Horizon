---
layout: default
title: "Horizon Summary: 2026-08-17 (EN)"
date: 2026-08-17
content_date: 2026-08-16
lang: en
---

> Coverage: 2026-08-16 (Asia/Shanghai calendar day)

> From 61 items, 11 important content pieces were selected

---

1. [llama.cpp b10453 Release: Model Optimization and Cross-Platform Binaries](#item-1) ⭐️ 10.0/10
2. [Ollama v0.32.14 Adds WebP Transcoding and Fixes Qwen Renderer](#item-2) ⭐️ 9.0/10
3. [Claude: System Prompts](#item-3) ⭐️ 9.0/10
4. [SSOG-Attention: A Sub-quadratic Alternative to SDPA](#item-4) ⭐️ 9.0/10
5. [Investigating Long-Range Recall Failures in Linear Attention for DNA Modeling](#item-5) ⭐️ 9.0/10
6. [Anthropic Q2 Revenue Surges 14-Fold to Over $11.5 Billion](#item-6) ⭐️ 9.0/10
7. [Researchers Use AI to Track Telegram Piracy, Closing 524 Channels in 61 Days](#item-7) ⭐️ 9.0/10
8. [SK Hynix Restarting Dalian Factory Amid China&\#x27;s Storage Rise](#item-8) ⭐️ 9.0/10
9. [CXMT DDR5 Memory Reaches 9,000 MT/s and DDR5-6000 CL28](#item-9) ⭐️ 9.0/10
10. [YMTC Surpasses Micron and Kioxia to Become World&\#x27;s Third-Largest NAND Supplier](#item-10) ⭐️ 9.0/10
11. [The Emerging AI Credit Resale Economy](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp b10453 Release: Model Optimization and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10453) ⭐️ 10.0/10

The llama.cpp project released version b10453, which removes the ggml\_concat function to optimize model architecture and provides pre-built binaries for macOS, Linux, Android, and Windows across various architectures and hardware accelerators. This update improves the efficiency and compatibility of local LLM inference, making it easier for developers and users to run models on diverse hardware without complex setup. The release includes disabled builds for KleidiAI on macOS and ROCm 7.14 on Ubuntu, alongside support for CUDA 12 and 13, Vulkan, SYCL, and OpenVINO on Windows and Linux.

github · github-actions\[bot\] · Aug 16, 20:54

**Background**: llama.cpp is a high-performance C++ inference engine designed to run large language models locally with minimal dependencies. It supports the GGUF model format and various hardware backends like CUDA and Vulkan.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases: ggml-org/llama.cpp - GitHub</a></li>
<li><a href="https://newreleases.io/project/github/ggml-org/llama.cpp/release/b10453">ggml-org/llama.cpp b10453 on GitHub - NewReleases.io</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI inference`, `#C++`, `#open-source`, `#LLM`

---

<a id="item-2"></a>
## [Ollama v0.32.14 Adds WebP Transcoding and Fixes Qwen Renderer](https://github.com/ollama/ollama/releases/tag/v0.32.14) ⭐️ 9.0/10

Ollama v0.32.14 introduces WebP image transcoding for llama-server and fixes handling of non-leading system messages in the Qwen renderer. This update improves compatibility with WebP images and stabilizes the Qwen renderer, enhancing the reliability of self-hosted LLM servers for users. The WebP transcoding feature ensures better image support in llama-server, while the Qwen renderer fix addresses potential rendering errors in multi-turn conversations.

github · github-actions\[bot\] · Aug 16, 03:41

**Background**: Ollama is a tool for running large language models locally, and llama-server is a component that exposes an API for model management. WebP is a modern image format optimized for the web, and Qwen is a text rendering model used in Ollama&\#x27;s ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.google.com/speed/webp">An image format for the Web | WebP | Google for Developers</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md">llama.cpp/tools/server/README.md at master · ggml ... - GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Ollama`, `#Software Release`, `#AI Server`, `#Bug Fixes`

---

<a id="item-3"></a>
## [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 9.0/10

This article explores the system prompts used by Claude AI models, highlighting changes and their implications for model behavior.

hackernews · tosh · Aug 16, 20:48 · [Discussion](https://news.ycombinator.com/item?id=49319556)

**Tags**: `#AI`, `#System Prompts`, `#Anthropic`, `#Model Behavior`, `#Prompt Engineering`

---

<a id="item-4"></a>
## [SSOG-Attention: A Sub-quadratic Alternative to SDPA](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 9.0/10

SSOG-Attention introduces a novel attention mechanism that replaces standard scaled dot-product attention \(SDPA\) with a sum of separable Gaussians, reducing complexity from O\(N²·d\) to O\(N·√N·d\). This innovation addresses the quadratic memory complexity of SDPA, which is a bottleneck for scaling transformer models, and offers a scalable alternative for large-scale deep learning applications. SSOG learns a few Gaussian atoms per attention head and steers them geometrically based on query tokens, achieving faster convergence and better memory efficiency compared to SDPA, especially on larger datasets like ImageNet-1k.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 18:06

**Background**: Scaled dot-product attention \(SDPA\), introduced in the 2017 paper &\#x27;Attention is All You Need&\#x27;, is a core operation in transformer models but suffers from quadratic memory complexity with respect to sequence length. Sub-quadratic attention mechanisms aim to reduce this complexity using techniques like low-rank approximations and sparsity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.02521">[2602.02521] Scaled Dot-Product Attention implements ... Implementing and Optimizing the Scaled Dot-Product Attention ... Scaled Dot-Product Attention Core—Sliding Window ... - Springer (Beta) Implementing High-Performance Transformers with Scaled ... Scaled Dot-Product Attention | intel/intel-npu-acceleration ... Scaled Dot-Product Attention | ml-explore/mlx | DeepWiki torch.nn.functional.scaled_dot_product_attention</a></li>
<li><a href="https://louiswang524.github.io/blog/ssa-subquadratic-sparse-attention/">From Quadratic to Linear: A Survey of Subquadratic Sparse Attention ...</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#attention-mechanism`, `#optimization`, `#efficiency`, `#deep-learning`

---

<a id="item-5"></a>
## [Investigating Long-Range Recall Failures in Linear Attention for DNA Modeling](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 9.0/10

A researcher discovered that linear attention models struggle with long-range recall on DNA sequences, achieving only 25% performance on a Needle in a Haystack benchmark, even when compared to the HyenaDNA model. This issue is critical for genomic modeling, as DNA sequences can reach 1M tokens, making standard attention mechanisms computationally infeasible and highlighting a fundamental limitation in current linear attention architectures. The researcher tested various approaches, including external memory and hybrid architectures, but improvements were marginal. Performance degraded significantly as context length increased from 16K to longer sequences, suggesting a scaling challenge.

reddit · r/MachineLearning · /u/No-Coffee-8227 · Aug 16, 15:47

**Background**: Linear attention models are designed to replace expensive quadratic attention with linear complexity, enabling processing of long sequences like DNA. HyenaDNA is a state-of-the-art genomic model using implicit convolutions to handle 1M-token contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.15794">[2306.15794] HyenaDNA: Long-Range Genomic Sequence Modeling ... HyenaDNA: learning from DNA with 1 Million token context HyenaDNA: Long-Range Genomic Sequence Modeling at Single ... HyenaDNA: Long-Range Genomic Sequence Modeling at Single ... HyenaDNA | Proceedings of the 37th International Conference ... LongSafari/hyenadna-large-1m-seqlen · Hugging Face</a></li>
<li><a href="https://grokipedia.com/page/needle_in_the_haystack">Needle in the Haystack</a></li>

</ul>
</details>

**Tags**: `#linear-attention`, `#long-range-recall`, `#dna-sequence-modeling`, `#machine-learning`, `#ai-compute`

---

<a id="item-6"></a>
## [Anthropic Q2 Revenue Surges 14-Fold to Over $11.5 Billion](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 9.0/10

Anthropic&\#x27;s preliminary Q2 revenue exceeded $11.5 billion, representing a 14-fold increase year-over-year and surpassing the $787 million reported in the same period last year. This unprecedented financial growth underscores the massive scale of adoption and investment in AI technologies, signaling a pivotal moment for the industry&\#x27;s commercialization and potential public market entry. The company achieved positive adjusted operating income for the first time, with plans to launch a major IPO in the fall, though the figures remain preliminary and subject to adjustment.

telegram · zaihuapd · Aug 16, 15:26

**Background**: Anthropic is a San Francisco-based AI safety and research company founded by former OpenAI researchers, known for developing Claude, a series of proprietary large language models \(LLMs\) focused on ethical and legal compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Revenue`, `#Business`, `#Finance`

---

<a id="item-7"></a>
## [Researchers Use AI to Track Telegram Piracy, Closing 524 Channels in 61 Days](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 9.0/10

Researchers developed an AI tool called Anti-RIP to detect and flag Telegram piracy channels, successfully closing 524 previously unknown channels within 61 days after submitting their findings to Telegram and copyright holders. This breakthrough demonstrates the practical application of AI in combating digital piracy and copyright infringement, potentially setting a precedent for automated enforcement mechanisms across social media platforms. The tool analyzed 1057 Telegram channels and 209,000 posts, identifying 983 channels involved in piracy with 485 million views across 19,033 films, while achieving 98% accuracy in flagging 802 suspected piracy channels from 249,000 new channels.

telegram · zaihuapd · Aug 16, 17:13

**Background**: Telegram has become a significant platform for distributing pirated content, with public channels posing substantial risks for copyright holders, as highlighted by studies on the video piracy ecosystem on the platform.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.08418">Binge, Bot, Repeat: Unpacking the Ecosystem of Video Piracy on...</a></li>
<li><a href="https://webkyte.com/blog/piracy-on-telegram-guide">Piracy on Telegram : How to Detect and Remove Copyrighted Content</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cybersecurity`, `#Copyright Enforcement`, `#Telegram`, `#Data Analysis`

---

<a id="item-8"></a>
## [SK Hynix Restarting Dalian Factory Amid China&\#x27;s Storage Rise](https://news.google.com/rss/articles/CBMieEFVX3lxTE5ZcWxnRmJOSEJYamlmYmR1aEdIMXVHTFJFLXdfbnQ4UnRvdDRjdTBpeGtNcjJJRUE2VDhRWFVJelhYVDRPVDFaclV5ZHhTUkctaWtobW1WdTdaOUV5bjJJcjYzMDd0bUU4XzIxczI0VHZZTTI1a01lUg?oc=5) ⭐️ 9.0/10

SK Hynix has resumed construction of its Dalian factory, signaling renewed investment in China&\#x27;s storage sector. This move reflects the growing competitiveness of Chinese storage manufacturers like YMTC and CXMT, potentially reshaping the global memory market. The Dalian plant previously faced delays, but its restart aligns with China&\#x27;s broader push to reduce reliance on foreign memory suppliers.

google\_news · 新浪网 · Aug 16, 21:26

**Background**: China&\#x27;s storage industry is led by YMTC \(NAND Flash\) and CXMT \(DRAM\), with both companies making significant strides in 3D NAND and DRAM technologies. The government has supported this growth through initiatives like the National Memory Base in Wuhan.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E9%95%BF%E6%B1%9F%E5%AD%98%E5%82%A8%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/20002721">长江存储科技有限责任公司_百度百科 追赶三星、海力士！继长鑫后，长江存储宣布IPO，估值或破万亿！湖北国... 长江存储 - 维基百科，自由的百科全书 企业简介-长江存储 - YMTC 长江存储IPO幕后：武汉20多年前押注芯片行业，是复制“合肥模式”？ 长鑫存储 vs 长江存储：中国存储双雄的全面对比 一、核心差异：DRAM v...</a></li>
<li><a href="https://baike.baidu.com/item/%E9%95%BF%E9%91%AB%E7%A7%91%E6%8A%80%E9%9B%86%E5%9B%A2%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/64261783">长鑫科技集团股份有限公司_百度百科</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/%E9%95%B7%E6%B1%9F%E5%AD%98%E5%84%B2">长江存储 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory`, `#manufacturing`, `#China`, `#SK Hynix`

---

<a id="item-9"></a>
## [CXMT DDR5 Memory Reaches 9,000 MT/s and DDR5-6000 CL28](https://news.google.com/rss/articles/CBMiggFBVV95cUxNWFZnRXpOZWp4MW5PYnJvSEVHSWxCa0VNc0Q0OV9JV0JPVTZUOGNQZmt1TENDbDROMzQtWGpxN2E5Zl9Vc21VanFsUDZmck5RMHBhVzNQbktweXV1bXplOGdlV2hSX1VTeko0UV9iY1JYOHZuOXUydTl6Z1dncWNIaDJB?oc=5) ⭐️ 9.0/10

CXMT DDR5 memory has demonstrated speeds up to 9,000 MT/s and stable operation at DDR5-6000 CL28, marking a significant performance milestone for Chinese memory manufacturers. This achievement highlights CXMT&\#x27;s progress in closing the gap with global memory leaders and provides a viable domestic alternative for AI compute infrastructure in China. While 9,000 MT/s was demonstrated, CXMT&\#x27;s official specifications list DDR5 ICs with data rates up to 8,000 Mbit/s, and the CL28 latency is achievable on specific AM5 platforms.

google\_news · igor´sLAB · Aug 16, 23:51

**Background**: CXMT \(ChangXin Memory Technologies\) is a Chinese semiconductor manufacturer based in Hefei, focusing on memory solutions like DDR4 and DDR5. DDR5 is the latest standard for system memory, offering higher speeds and efficiency than DDR4.

<details><summary>References</summary>
<ul>
<li><a href="https://www.igorslab.de/en/cxmt-ddr5-reaches-9000-mt-s-ddr5-6000-cl28/">CXMT DDR 5 : 9,000 MT / s and DDR 5 -6000 CL28 | igor´sLAB</a></li>
<li><a href="https://wccftech.com/chinese-ddr5-memory-achives-9000-mtps-speeds-offers-cl30-cl28-specs-with-ease/">Chinese DDR 5 Memory Achieves 9000 MT / s Speeds, Now Offers...</a></li>
<li><a href="https://www.topcpu.net/en/news/cxmt-ddr5-hits-8800mts-on-am5-nears-9000">CXMT DDR 5 Reaches a Stable 8800 MT / s on AM5, Moving Closer to...</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#Memory`, `#Hardware`, `#AI Infrastructure`, `#Semiconductors`

---

<a id="item-10"></a>
## [YMTC Surpasses Micron and Kioxia to Become World&\#x27;s Third-Largest NAND Supplier](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPVm5EeWVXWW5QWTFLeVVoaWVBSWpEQmZuOHRtVnNucXlBY3JuQWVLemh0SXlBZzdxaGlSa1dqMk9hUk1Md3dvWFdDSDlVMWc1eU5aTGVYdnBUWG5QZk9xUGpwcXZISXJ3eXkzMTk1bDN3bV9VTlRreHh2UlVBOTRoazJqS3NMR2QyN2FIam1rWWpJNnFnMlNBRTRlYURCeUZIRXpIZWQtZlVJVXZIbFh1T25hYTcxQjUxSFY1RjdfWmxsWDRaQ05sTUJQNjBiQW1ES19R?oc=5) ⭐️ 9.0/10

Yangtze Memory Technologies Corporation \(YMTC\) has surpassed Micron and Kioxia to become the world&\#x27;s third-largest NAND flash memory supplier, capturing 14% of the global market share in the second quarter of 2026. This milestone marks a significant shift in the global semiconductor landscape, reducing China&\#x27;s reliance on foreign memory suppliers and intensifying competition in the memory market. YMTC&\#x27;s growth is driven by its expansion in 3D NAND technology and production capacity, though it still lags behind Micron and Kioxia in NAND chip revenue.

google\_news · TradingKey · Aug 16, 14:31

**Background**: YMTC is a Chinese semiconductor company founded in 2016 with government support, specializing in NAND flash memory. The company has rapidly advanced its technology, including 3D NAND, to compete with global leaders like Samsung and Western Digital.

<details><summary>References</summary>
<ul>
<li><a href="https://www.digitalcitizen.life/ymtc-becomes-worlds-third-largest-nand-supplier-with-14-percent-market-share/">YMTC Becomes World’s Third Largest NAND Supplier With 14 ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time">YMTC breaks into the top three NAND makers for the first time ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory`, `#NAND`, `#YMTC`, `#market-share`

---

<a id="item-11"></a>
## [The Emerging AI Credit Resale Economy](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 8.0/10

Token brokers are now buying unused AI model credits from startups and reselling them off-market through marketplaces, routers, and message boards. This resale market raises significant security and compliance risks for AI providers while creating new economic opportunities for users and brokers. The resale economy exploits off-market inference channels, often bypassing official pricing models and creating new abuse patterns that are difficult to detect.

hackernews · mlenhard · Aug 16, 22:44 · [Discussion](https://news.ycombinator.com/item?id=49320611)

**Background**: AI providers often offer credits as part of accelerator grants or promotional packages, creating a pool of unused resources that can be monetized through resale.

<details><summary>References</summary>
<ul>
<li><a href="https://ideaverse.ai/blog/the-ai-credit-resale-economy-token-brokers-off-market-inference-mswb8szl">The AI Credit Resale Economy: Token Brokers, Off-Market Inference</a></li>
<li><a href="https://www.solvimon.com/blog/ai-credit-pricing-models-how-tokens-credits-hybrid-billing-work">AI credit pricing models: how tokens, credits, and hybrid ...</a></li>
<li><a href="https://credswap.works/">CredSwap — The Verified Marketplace for AI &amp; Cloud Credits</a></li>

</ul>
</details>

**Discussion**: Users express skepticism about trusting third-party platforms with their data, while some note that similar abuse patterns exist in other industries like airline loyalty programs.

**Tags**: `#AI`, `#security`, `#abuse`, `#credits`, `#marketplace`

---