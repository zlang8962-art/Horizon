---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
content_date: 2026-08-16
lang: zh
---

> 报道范围：2026-08-16（Asia/Shanghai 自然日）

> 从 61 条内容中筛选出 11 条重要资讯。

---

1. [llama.cpp b10453 发布：模型优化与跨平台二进制文件](#item-1) ⭐️ 10.0/10
2. [Ollama v0.32.14 添加 WebP 转码并修复 Qwen 渲染器](#item-2) ⭐️ 9.0/10
3. [Claude: System Prompts](#item-3) ⭐️ 9.0/10
4. [SSOG-Attention：SDPA 的次二次方替代方案](#item-4) ⭐️ 9.0/10
5. [调查线性注意力在 DNA 建模中的长程召回失败问题](#item-5) ⭐️ 9.0/10
6. [Anthropic 第二季营收暴涨 14 倍，初步数字超 115 亿美元](#item-6) ⭐️ 9.0/10
7. [研究人员用 AI 追踪 Telegram 盗版，61 天发现 524 个频道被关闭](#item-7) ⭐️ 9.0/10
8. [SK 海力士重启大连工厂建设，中国存储崛起驱动产业变局](#item-8) ⭐️ 9.0/10
9. [CXMT DDR5 内存达到 9,000 MT/s 和 DDR5-6000 CL28](#item-9) ⭐️ 9.0/10
10. [长江存储超越美光和铠侠，成为全球第三大 NAND 闪存供应商](#item-10) ⭐️ 9.0/10
11. [新兴的 AI 积分转售经济](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp b10453 发布：模型优化与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10453) ⭐️ 10.0/10

llama.cpp 项目发布了 b10453 版本，移除了 ggml\_concat 函数以优化模型架构，并为 macOS、Linux、Android 和 Windows 提供了针对不同架构和硬件加速器的预编译二进制文件。 此次更新提高了本地 LLM 推理的效率和兼容性，使开发者和用户能够在各种硬件上运行模型而无需复杂的配置。 该版本包含 macOS 上 KleidiAI 和 Ubuntu 上 ROCm 7.14 的禁用构建，同时支持 Windows 和 Linux 上的 CUDA 12 和 13、Vulkan、SYCL 和 OpenVINO。

github · github-actions\[bot\] · 8月16日 20:54

**背景**: llama.cpp 是一个高性能的 C++ 推理引擎，旨在以最少的依赖在本地运行大型语言模型。它支持 GGUF 模型格式和各种硬件后端，如 CUDA 和 Vulkan。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases: ggml-org/llama.cpp - GitHub</a></li>
<li><a href="https://newreleases.io/project/github/ggml-org/llama.cpp/release/b10453">ggml-org/llama.cpp b10453 on GitHub - NewReleases.io</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#C++`, `#open-source`, `#LLM`

---

<a id="item-2"></a>
## [Ollama v0.32.14 添加 WebP 转码并修复 Qwen 渲染器](https://github.com/ollama/ollama/releases/tag/v0.32.14) ⭐️ 9.0/10

Ollama v0.32.14 为 llama-server 引入了 WebP 图像转码，并修复了 Qwen 渲染器对非首条系统消息的处理问题。 此次更新提高了对 WebP 图像的兼容性，并稳定了 Qwen 渲染器，从而提升了自托管 LLM 服务器的可靠性。 WebP 转码功能确保了 llama-server 对图像的更好支持，而 Qwen 渲染器的修复则解决了多轮对话中可能出现的渲染错误。

github · github-actions\[bot\] · 8月16日 03:41

**背景**: Ollama 是一个用于在本地运行大语言模型的工具，llama-server 是一个用于模型管理的 API 组件。WebP 是一种为网络优化的现代图像格式，Qwen 是 Ollama 生态系统中使用的文本渲染模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.google.com/speed/webp">An image format for the Web | WebP | Google for Developers</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md">llama.cpp/tools/server/README.md at master · ggml ... - GitHub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Ollama`, `#Software Release`, `#AI Server`, `#Bug Fixes`

---

<a id="item-3"></a>
## [Claude: System Prompts](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 9.0/10

This article explores the system prompts used by Claude AI models, highlighting changes and their implications for model behavior.

hackernews · tosh · 8月16日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**标签**: `#AI`, `#System Prompts`, `#Anthropic`, `#Model Behavior`, `#Prompt Engineering`

---

<a id="item-4"></a>
## [SSOG-Attention：SDPA 的次二次方替代方案](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 9.0/10

SSOG-Attention 引入了一种新颖的注意力机制，用可分离高斯之和替换了标准的缩放点积注意力（SDPA），将复杂度从 O\(N²·d\) 降低到 O\(N·√N·d\)。 这一创新解决了 SDPA 的二次方内存复杂度问题，这是扩展 Transformer 模型的瓶颈，并为大规模深度学习应用提供了可扩展的替代方案。 SSOG 为每个注意力头学习几个高斯原子，并根据查询令牌进行几何引导，与 SDPA 相比，在收敛速度和内存效率方面表现更好，特别是在 ImageNet-1k 等大型数据集上。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 18:06

**背景**: 缩放点积注意力（SDPA）于 2017 年在论文《Attention is All You Need》中引入，是 Transformer 模型的核心操作，但存在随序列长度呈二次方增长的内存复杂度问题。次二次方注意力机制旨在通过低秩近似和稀疏性等技术降低这种复杂度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.02521">[2602.02521] Scaled Dot-Product Attention implements ... Implementing and Optimizing the Scaled Dot-Product Attention ... Scaled Dot-Product Attention Core—Sliding Window ... - Springer (Beta) Implementing High-Performance Transformers with Scaled ... Scaled Dot-Product Attention | intel/intel-npu-acceleration ... Scaled Dot-Product Attention | ml-explore/mlx | DeepWiki torch.nn.functional.scaled_dot_product_attention</a></li>
<li><a href="https://louiswang524.github.io/blog/ssa-subquadratic-sparse-attention/">From Quadratic to Linear: A Survey of Subquadratic Sparse Attention ...</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#attention-mechanism`, `#optimization`, `#efficiency`, `#deep-learning`

---

<a id="item-5"></a>
## [调查线性注意力在 DNA 建模中的长程召回失败问题](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 9.0/10

研究人员发现线性注意力模型在 DNA 序列上难以实现长程召回，在 Needle in a Haystack 基准测试中仅达到 25%的性能，即使与 HyenaDNA 模型相比也是如此。 这一问题对基因组建模至关重要，因为 DNA 序列可达 100 万个标记，使得标准注意力机制在计算上不可行，并凸显了当前线性注意力架构的根本局限性。 研究人员测试了各种方法，包括外部记忆和混合架构，但改进微乎其微。随着上下文长度从 16K 增加到更长序列，性能显著下降，表明存在扩展性挑战。

reddit · r/MachineLearning · /u/No-Coffee-8227 · 8月16日 15:47

**背景**: 线性注意力模型旨在用线性复杂度替代昂贵的二次注意力，从而处理 DNA 等长序列。HyenaDNA 是一种最先进的基因组模型，使用隐式卷积处理 100 万个标记的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.15794">[2306.15794] HyenaDNA: Long-Range Genomic Sequence Modeling ... HyenaDNA: learning from DNA with 1 Million token context HyenaDNA: Long-Range Genomic Sequence Modeling at Single ... HyenaDNA: Long-Range Genomic Sequence Modeling at Single ... HyenaDNA | Proceedings of the 37th International Conference ... LongSafari/hyenadna-large-1m-seqlen · Hugging Face</a></li>
<li><a href="https://grokipedia.com/page/needle_in_the_haystack">Needle in the Haystack</a></li>

</ul>
</details>

**标签**: `#linear-attention`, `#long-range-recall`, `#dna-sequence-modeling`, `#machine-learning`, `#ai-compute`

---

<a id="item-6"></a>
## [Anthropic 第二季营收暴涨 14 倍，初步数字超 115 亿美元](https://www.cnbc.com/2026/08/15/anthropic-revenue-jumps-to-over-11point5-billion-in-q2-report.html) ⭐️ 9.0/10

Anthropic 第二季初步营收超过 115 亿美元，同比增长逾 14 倍，高于去年同期的 7.87 亿美元。 这种前所未有的财务增长凸显了 AI 技术的巨大采用规模和投资力度，标志着行业商业化的重要时刻，并可能引发潜在的公开市场进入。 该公司首次实现调整后营业利润转正，并计划于今秋启动大型 IPO，但数字仍为初步数据，可能进行调整。

telegram · zaihuapd · 8月16日 15:26

**背景**: Anthropic 是一家位于旧金山的 AI 安全和研究公司，由前 OpenAI 研究人员创立，以开发 Claude 系列专有大型语言模型（LLM）而闻名，这些模型专注于伦理和法律合规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Revenue`, `#Business`, `#Finance`

---

<a id="item-7"></a>
## [研究人员用 AI 追踪 Telegram 盗版，61 天发现 524 个频道被关闭](https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/) ⭐️ 9.0/10

研究人员开发了一款名为 Anti-RIP 的 AI 工具来检测并标记 Telegram 盗版频道，在将结果提交给 Telegram 和版权方后，61 天内成功关闭了 524 个此前未知的盗版频道。 这一突破展示了 AI 在打击数字盗版和版权侵权方面的实际应用，可能为社交媒体平台上的自动化执法机制树立先例。 该工具分析了 1057 个 Telegram 频道和 20.9 万条帖子，识别出 983 个涉及盗版的频道，相关帖子累计获得 4.85 亿次浏览，涉及 19033 部影视作品，同时从 24.9 万个新频道中标记了 802 个疑似盗版频道，测试准确率达到 98%。

telegram · zaihuapd · 8月16日 17:13

**背景**: Telegram 已成为分发盗版内容的重要平台，公开频道对版权所有者构成了重大风险，正如关于该平台上视频盗版生态系统的研究所强调的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.08418">Binge, Bot, Repeat: Unpacking the Ecosystem of Video Piracy on...</a></li>
<li><a href="https://webkyte.com/blog/piracy-on-telegram-guide">Piracy on Telegram : How to Detect and Remove Copyrighted Content</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cybersecurity`, `#Copyright Enforcement`, `#Telegram`, `#Data Analysis`

---

<a id="item-8"></a>
## [SK 海力士重启大连工厂建设，中国存储崛起驱动产业变局](https://news.google.com/rss/articles/CBMieEFVX3lxTE5ZcWxnRmJOSEJYamlmYmR1aEdIMXVHTFJFLXdfbnQ4UnRvdDRjdTBpeGtNcjJJRUE2VDhRWFVJelhYVDRPVDFaclV5ZHhTUkctaWtobW1WdTdaOUV5bjJJcjYzMDd0bUU4XzIxczI0VHZZTTI1a01lUg?oc=5) ⭐️ 9.0/10

SK 海力士已重启大连工厂的建设，这标志着对中国存储行业的重新投资。 这一举措反映了中国存储制造商（如 YMTC 和 CXMT）竞争力的提升，可能重塑全球存储器市场。 大连工厂此前曾面临延误，但其重启与中国减少对外国存储供应商依赖的更广泛努力相一致。

google\_news · 新浪网 · 8月16日 21:26

**背景**: 中国存储行业由 YMTC（NAND 闪存）和 CXMT（DRAM）主导，这两家公司都在 3D NAND 和 DRAM 技术上取得了重大进展。政府通过在武汉建设国家存储器基地等举措支持了这一增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E9%95%BF%E6%B1%9F%E5%AD%98%E5%82%A8%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8/20002721">长江存储科技有限责任公司_百度百科 追赶三星、海力士！继长鑫后，长江存储宣布IPO，估值或破万亿！湖北国... 长江存储 - 维基百科，自由的百科全书 企业简介-长江存储 - YMTC 长江存储IPO幕后：武汉20多年前押注芯片行业，是复制“合肥模式”？ 长鑫存储 vs 长江存储：中国存储双雄的全面对比 一、核心差异：DRAM v...</a></li>
<li><a href="https://baike.baidu.com/item/%E9%95%BF%E9%91%AB%E7%A7%91%E6%8A%80%E9%9B%86%E5%9B%A2%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/64261783">长鑫科技集团股份有限公司_百度百科</a></li>
<li><a href="https://zh.wikipedia.org/zh-cn/%E9%95%B7%E6%B1%9F%E5%AD%98%E5%84%B2">长江存储 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory`, `#manufacturing`, `#China`, `#SK Hynix`

---

<a id="item-9"></a>
## [CXMT DDR5 内存达到 9,000 MT/s 和 DDR5-6000 CL28](https://news.google.com/rss/articles/CBMiggFBVV95cUxNWFZnRXpOZWp4MW5PYnJvSEVHSWxCa0VNc0Q0OV9JV0JPVTZUOGNQZmt1TENDbDROMzQtWGpxN2E5Zl9Vc21VanFsUDZmck5RMHBhVzNQbktweXV1bXplOGdlV2hSX1VTeko0UV9iY1JYOHZuOXUydTl6Z1dncWNIaDJB?oc=5) ⭐️ 9.0/10

CXMT DDR5 内存已演示达到 9,000 MT/s 的速度，并在 DDR5-6000 CL28 下稳定运行，标志着中国内存制造商的重要性能里程碑。 这一成就凸显了 CXMT 在缩小与全球内存领导者差距方面的进展，并为中国的 AI 计算基础设施提供了可行的国内替代方案。 虽然演示了 9,000 MT/s，但 CXMT 的官方规格列出的 DDR5 IC 数据速率最高为 8,000 Mbit/s，且 CL28 延迟可在特定的 AM5 平台上实现。

google\_news · igor´sLAB · 8月16日 23:51

**背景**: CXMT（长鑫存储）是一家总部位于合肥的中国半导体制造商，专注于 DDR4 和 DDR5 等内存解决方案。DDR5 是系统内存的最新标准，比 DDR4 提供更高的速度和效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.igorslab.de/en/cxmt-ddr5-reaches-9000-mt-s-ddr5-6000-cl28/">CXMT DDR 5 : 9,000 MT / s and DDR 5 -6000 CL28 | igor´sLAB</a></li>
<li><a href="https://wccftech.com/chinese-ddr5-memory-achives-9000-mtps-speeds-offers-cl30-cl28-specs-with-ease/">Chinese DDR 5 Memory Achieves 9000 MT / s Speeds, Now Offers...</a></li>
<li><a href="https://www.topcpu.net/en/news/cxmt-ddr5-hits-8800mts-on-am5-nears-9000">CXMT DDR 5 Reaches a Stable 8800 MT / s on AM5, Moving Closer to...</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#Memory`, `#Hardware`, `#AI Infrastructure`, `#Semiconductors`

---

<a id="item-10"></a>
## [长江存储超越美光和铠侠，成为全球第三大 NAND 闪存供应商](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPVm5EeWVXWW5QWTFLeVVoaWVBSWpEQmZuOHRtVnNucXlBY3JuQWVLemh0SXlBZzdxaGlSa1dqMk9hUk1Md3dvWFdDSDlVMWc1eU5aTGVYdnBUWG5QZk9xUGpwcXZISXJ3eXkzMTk1bDN3bV9VTlRreHh2UlVBOTRoazJqS3NMR2QyN2FIam1rWWpJNnFnMlNBRTRlYURCeUZIRXpIZWQtZlVJVXZIbFh1T25hYTcxQjUxSFY1RjdfWmxsWDRaQ05sTUJQNjBiQW1ES19R?oc=5) ⭐️ 9.0/10

长江存储科技集团（YMTC）已超越美光和铠侠，成为全球第三大 NAND 闪存供应商，在 2026 年第二季度占据了 14%的全球市场份额。 这一里程碑标志着全球半导体格局的重大转变，减少了中国对外国存储供应商的依赖，并加剧了存储市场的竞争。 YMTC 的增长得益于其在 3D NAND 技术和产能方面的扩张，尽管其在 NAND 芯片收入方面仍落后于美光和铠侠。

google\_news · TradingKey · 8月16日 14:31

**背景**: YMTC 是一家成立于 2016 年的中国半导体公司，在政府支持下专注于 NAND 闪存。该公司迅速推进其技术，包括 3D NAND，以与三星和西部数据等全球领导者竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalcitizen.life/ymtc-becomes-worlds-third-largest-nand-supplier-with-14-percent-market-share/">YMTC Becomes World’s Third Largest NAND Supplier With 14 ...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time">YMTC breaks into the top three NAND makers for the first time ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory`, `#NAND`, `#YMTC`, `#market-share`

---

<a id="item-11"></a>
## [新兴的 AI 积分转售经济](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 8.0/10

代币经纪人现在正在从初创公司购买未使用的 AI 模型积分，并通过市场、路由器和消息板在市场外转售。 这种转售市场为 AI 提供商带来了重大的安全和合规风险，同时为用户和经纪人创造了新的经济机会。 转售经济利用市场外的推理渠道，经常绕过官方定价模式，并创造出难以检测的新滥用模式。

hackernews · mlenhard · 8月16日 22:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI 提供商经常将积分作为加速器资助或促销套餐的一部分提供，从而创造出一池可以被转售的未使用资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ideaverse.ai/blog/the-ai-credit-resale-economy-token-brokers-off-market-inference-mswb8szl">The AI Credit Resale Economy: Token Brokers, Off-Market Inference</a></li>
<li><a href="https://www.solvimon.com/blog/ai-credit-pricing-models-how-tokens-credits-hybrid-billing-work">AI credit pricing models: how tokens, credits, and hybrid ...</a></li>
<li><a href="https://credswap.works/">CredSwap — The Verified Marketplace for AI &amp; Cloud Credits</a></li>

</ul>
</details>

**社区讨论**: 用户对将数据托付给第三方平台表示怀疑，而一些人指出类似的滥用模式在其他行业如航空公司忠诚度计划中已经存在。

**标签**: `#AI`, `#security`, `#abuse`, `#credits`, `#marketplace`

---