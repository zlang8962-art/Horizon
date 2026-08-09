---
layout: default
title: "Horizon Summary: 2026-08-10 (ZH)"
date: 2026-08-10
content_date: 2026-08-09
lang: zh
---

> 报道范围：2026-08-09（Asia/Shanghai 自然日）

> 从 72 条内容中筛选出 10 条重要资讯。

---

1. [llama.cpp b10332 版本发布，包含 CI 修复和预编译二进制文件](#item-1) ⭐️ 10.0/10
2. [llama.cpp v0.3.33 发布：CPU 后端修复与跨平台二进制文件](#item-2) ⭐️ 9.0/10
3. [噪声感知训练揭示模拟硬件中类似阈值的准确率崩溃](#item-3) ⭐️ 9.0/10
4. [首个可存活噬菌体基因组生成设计](#item-4) ⭐️ 9.0/10
5. [全球最大单体 AI 算力设施在内蒙古乌兰察布投产](#item-5) ⭐️ 9.0/10
6. [MiniMax H3 团队办 AMA：将开源 2K 模型与稀疏注意力](#item-6) ⭐️ 9.0/10
7. [知情人士：苹果测试长鑫科技存储芯片 用于 iPhone 和 MacBook](#item-7) ⭐️ 9.0/10
8. [Claude Code 的自动模式现已成为 Pro、Max 和 Team 计划的默认设置](#item-8) ⭐️ 8.0/10
9. [长鑫科技财务转折：从亏损 300 亿到日赚 3 亿](#item-9) ⭐️ 8.0/10
10. [全球最大半导体 ETF 管理人考虑将长鑫科技纳入旗下基金](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp b10332 版本发布，包含 CI 修复和预编译二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10332) ⭐️ 10.0/10

llama.cpp 项目发布了 b10332 版本，从 CI 流程中移除了 GGML\_HIP\_ROCWMMA\_FATTN 标志，并为 macOS、Linux、Windows 和 Android 的各种架构提供了预编译二进制文件。 此次发布通过修复特定的 CI 问题并提供即用型二进制文件，提高了 llama.cpp（一个广泛使用的本地运行大语言模型的工具）的稳定性和兼容性，从而造福开发者和用户。 该版本提供了针对 macOS（Apple Silicon 和 Intel）、Linux（Ubuntu 支持 CPU、Vulkan、ROCm、OpenVINO 和 SYCL）、Windows（支持 CPU、OpenCL Adreno、CUDA 12/13、Vulkan、OpenVINO、SYCL 和 HIP）、Android（arm64 CPU）和 openEuler 的预编译二进制文件，并禁用了 macOS 的 KleidiAI 支持。

github · github-actions\[bot\] · 8月9日 18:48

**背景**: llama.cpp 是一个用于本地运行大语言模型的高性能 C++ 库，针对 CUDA、ROCm 和 Vulkan 等各种硬件后端进行了优化。GGML\_HIP\_ROCWMMA\_FATTN 是一个标志，用于在 AMD GPU（特别是 RDNA3+ 或 CDNA 架构）上启用 rocWMMA 库以增强 Flash Attention 性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/15021">Performance of llama.cpp on AMD ROCm ( HIP ) · ggml -org llama.cpp...</a></li>
<li><a href="https://www.banandre.com/blog/amd-rdna3-faster-llamacpp-performance-rocm-optimizations">AMD RDNA3 Users Finally Get Decent llama.cpp... - Banandre</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html">Trillion-Parameter LLM on an AMD Ryzen™ AI Max+ Cluster</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#open-source`, `#AI`, `#machine-learning`, `#local-inference`

---

<a id="item-2"></a>
## [llama.cpp v0.3.33 发布：CPU 后端修复与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10333) ⭐️ 9.0/10

llama.cpp v0.3.33 \(b10333\) 发布包含了对 SpaceMiT 后端中缺失的 Q5\_0 调度的关键修复，并提供了 macOS、Linux 和 iOS 的预构建二进制文件。 此次发布对 AI 开发者和用户具有重要意义，因为它提高了在特定硬件架构上 LLM 推理的可靠性，并使软件在不同操作系统上的可访问性更高。 SpaceMiT 后端修复解决了 Q5\_0 量化的一个具体问题，该发布提供了广泛的二进制文件支持，包括针对不同平台的 CPU、Vulkan、CUDA、ROCm 和 OpenVINO 后端。

github · github-actions\[bot\] · 8月9日 19:21

**背景**: llama.cpp 是一个流行的 C/C++ 库，用于在消费级硬件上高效运行大语言模型 \(LLM\)。它支持各种量化格式，如 Q5\_0，以减少内存使用并优化性能。SpaceMiT 后端是针对 SpacemiT RISC-V CPU 的特定实现，而 KleidiAI 是一个针对 AI 微内核的 ARM 优化库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases: ggml-org/llama.cpp - GitHub</a></li>
<li><a href="https://github.com/spacemit-com">spacemit.com · GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#software release`, `#CPU backend`, `#cross-platform`

---

<a id="item-3"></a>
## [噪声感知训练揭示模拟硬件中类似阈值的准确率崩溃](https://www.reddit.com/r/MachineLearning/comments/1vjmw53/noiseaware_training_for_analog_hardware_accuracy/) ⭐️ 9.0/10

Reddit 帖子报告了实验结果，显示模拟存内计算的准确率在阈值处急剧下降而非平滑退化，且噪声感知训练显著改变了这一阈值。 这一发现对模拟计算生态系统具有重要意义，因为它挑战了平滑退化的假设，并强调了硬件感知训练策略对于维持模型性能的必要性。 实验显示准确率从 83%降至 64%，随后接近随机水平，而噪声感知训练在匹配噪声水平下将性能从 61%提升至 39%，表明优化器找到了更平坦的极小值。

reddit · r/MachineLearning · /u/Georgiou1226 · 8月9日 18:55

**背景**: 模拟存内计算因其节能特性受到关注，但固有的噪声和变异性会降低模型准确率。硬件感知训练方法旨在通过在训练期间模拟噪声来缓解这些问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismix.dev/news/3bf841047f18">Noise-aware training for analog hardware: accuracy collapses ...</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56595-2">The inherent adversarial robustness of analog in-memory ...</a></li>
<li><a href="https://aihwkit.readthedocs.io/en/latest/hwa_training.html">Analog Hardware-aware Training - Read the Docs</a></li>

</ul>
</details>

**社区讨论**: 作者邀请社区讨论平坦极小值解释是否正确，或是否有其他因素驱动性能差距，并询问关于直接针对噪声鲁棒性进行优化的研究。

**标签**: `#analog-compute`, `#noise-robustness`, `#hardware-software-co-design`, `#machine-learning`, `#in-memory-compute`

---

<a id="item-4"></a>
## [首个可存活噬菌体基因组生成设计](https://www.reddit.com/r/MachineLearning/comments/1vjj4pr/r_generative_design_of_novel_bacteriophages_with/) ⭐️ 9.0/10

研究人员报告了首个使用前沿基因组语言模型 Evo 1 和 Evo 2 生成的可存活噬菌体基因组设计，产生了 16 种具有显著进化新颖性的新型噬菌体。 这一突破展示了 AI 在基因组尺度设计功能性生物系统的潜力，为合成生物学和生物技术应用开辟了新途径。 该研究以裂解性噬菌体 ΦX174 为设计模板，实现了 AI 生成基因组的实验验证，其中 Evo 2 是一个在 9 万亿个 DNA 碱基对上训练的 400 亿参数模型。

reddit · r/MachineLearning · /u/moschles · 8月9日 15:11

**背景**: 基因组语言模型（gLMs）是在 DNA 序列上训练的大型语言模型，用于模拟复杂的生物功能。Evo 2 是一个基因组基础模型，能够跨 DNA、RNA 和蛋白质执行通用预测和设计任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12805252/">A comprehensive survey of genome language models in ...</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-10176-5">Genome modelling and design across all domains of life with Evo 2</a></li>
<li><a href="https://astrobiology.com/2026/01/12/generative-design-of-novel-bacteriophages-with-genome-language-models/">Generative Design Of Novel Bacteriophages With Genome ...</a></li>

</ul>
</details>

**标签**: `#genomics`, `#machine learning`, `#biological systems`, `#generative design`, `#bacteriophages`

---

<a id="item-5"></a>
## [全球最大单体 AI 算力设施在内蒙古乌兰察布投产](https://www.globaltimes.cn/page/202608/1367666.shtml) ⭐️ 9.0/10

8 月 6 日，远景科技集团宣布“远景乌兰察布星河基地”正式投产，该基地是全球最大的单体 AI 算力设施。 该设施代表了 AI 基础设施发展的重要里程碑，为国产算力集群提供了可复制的方案，并支持“东数西算”战略。 该基地建筑面积 12 万平方米，支持百万 GPU 并行计算，规划总容量达 2GW，绿电占比超 80%。

telegram · zaihuapd · 8月9日 13:06

**背景**: “东数西算”战略是一项国家倡议，旨在通过将工作负载从东部转移到西部来优化数据处理，利用乌兰察布等地区的丰富可再生能源资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E8%BF%9C%E6%99%AF%E6%98%9F%E6%B2%B3%E5%9F%BA%E5%9C%B0/68089868">远景星河基地 - 百度百科</a></li>
<li><a href="https://news.qq.com/rain/a/20260618A04B3F00">远景张雷：启动Mission Gobi AIDC建设计划，让全球戈壁成为下一代智能...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Hardware`, `#Infrastructure`, `#Cloud Computing`, `#Green Energy`

---

<a id="item-6"></a>
## [MiniMax H3 团队办 AMA：将开源 2K 模型与稀疏注意力](https://www.reddit.com/r/StableDiffusion/s/fjM3d7AEV8) ⭐️ 9.0/10

MiniMax H3 team announces open-source plans for a 2K regeneration model and sparse attention implementation while addressing community feedback on quality issues.

telegram · zaihuapd · 8月9日 16:28

**标签**: `#AI`, `#Machine Learning`, `#Open Source`, `#Sparse Attention`, `#Video Generation`

---

<a id="item-7"></a>
## [知情人士：苹果测试长鑫科技存储芯片 用于 iPhone 和 MacBook](https://news.google.com/rss/articles/CBMiYEFVX3lxTE04TmFmbnQzS0FETzh6RjZkb3ZwTDlaTUdXUHp2QTJyTEVTYjdXSDdiSGwxY0tvMXBLUUgxLTZtUU5zUHVoYzh2dURmZ0hYZGtuRXo3RS1pRHRJTmVncEhPQg?oc=5) ⭐️ 9.0/10

据知情人士透露，苹果正在测试中国制造商长鑫存储（CXMT）的存储芯片，用于 iPhone 和 MacBook。 这一举措可能标志着苹果在全球半导体短缺和地缘政治紧张局势下，正寻求供应链多元化的战略转变。 据报道，测试主要针对中国国内市场的芯片，且合作可能需要获得美国政府的批准。

google\_news · 东方财富 · 8月9日 15:22

**背景**: 长鑫存储是一家成立于 2016 年的中国 DRAM 制造商，专注于为移动设备、PC 和服务器生产存储芯片。苹果历史上一直依赖三星和 SK 海力士等供应商，但最近的供应限制促使苹果探索替代来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.cxmt.com/en/">About cxmt - cxmt</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lsOXRMakVSR09PUGZCazB1QkZDZ0FQAQ?hl=en-IN&amp;gl=IN&amp;ceid=IN:en">Google News - Report: Apple tests CXMT memory chips amid supply...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory chips`, `#Apple`, `#CXMT`, `#hardware`

---

<a id="item-8"></a>
## [Claude Code 的自动模式现已成为 Pro、Max 和 Team 计划的默认设置](https://simonwillison.net/2026/Aug/8/auto-mode/#atom-everything) ⭐️ 8.0/10

从 2026 年 8 月 14 日起，Anthropic 将在 Claude Code 的 Pro、Max 和 Team 计划中，为所有新会话默认启用自动模式，这是基于内部测试的成功结果。 这一变化标志着 AI 辅助编码工具的重大转变，朝着更自主的代理行为发展，同时解决了提示注入和意外损坏等关键安全问题。 内部评估显示，自动模式阻止了 89% 的有害操作，而人类审查者仅阻止了 13.6%，第三方测试发现，运行自动模式的 Claude Fable 5、Opus 5 或 Sonnet 5 未受到任何成功的攻击。

rss · Simon Willison · 8月9日 06:36

**背景**: Claude Code 是一款 AI 辅助编码工具，旨在帮助开发者更高效地编写代码。自动模式是一种权限功能，AI 代理会在安全措施的保护下自动做出权限决定，旨在减少因频繁请求人工批准而产生的确认疲劳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://medium.com/@richardhightower/claude-code-auto-mode-escape-permission-fatigue-guide-to-automated-permissions-a122568e1ed6">Claude Code Auto Mode : Escape Permission Fatigue... | Medium</a></li>
<li><a href="https://beamsec.medium.com/prompt-injection-when-your-ai-turns-against-you-75ba5c7447db">Prompt Injection : When Your AI Turns Against You | Medium</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI-assisted coding`, `#Software development`, `#AI safety`, `#Product updates`

---

<a id="item-9"></a>
## [长鑫科技财务转折：从亏损 300 亿到日赚 3 亿](https://news.google.com/rss/articles/CBMiUEFVX3lxTFB0dmVRV0JzZkQ4d0FsWWpYbExaY3ZxbC1GSDhGWHNwMnlVREFqLV9IVS1MU0NsMnZreG1QWTNYdkI1Nld4cUE5dW9HNTBBU1BZ?oc=5) ⭐️ 8.0/10

长鑫科技成功从巨额亏损 300 亿转变为日赚 3 亿，标志着显著的财务复苏。 这一转折凸显了长鑫科技在竞争激烈的 DRAM 市场中的韧性和战略成功，为中国半导体制造商树立了标杆。 复苏归功于长鑫科技的技术进步和生产流程优化，尽管文章未提供具体细节。

google\_news · 凤凰网 · 8月9日 08:57

**背景**: 长鑫科技是中国领先的 DRAM 制造商，以其在半导体制造方面的创新和对中国科技自主发展的贡献而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.icdistributor.cn/index.php?_m=mod_product&amp;_a=view&amp;p_id=156">CXMT 长 鑫 --深圳市砹矽 科 技 有限公司</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/621945568">国产存储芯片部分企业名单盘点 - 知乎</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#memory`, `#manufacturing`, `#business`

---

<a id="item-10"></a>
## [全球最大半导体 ETF 管理人考虑将长鑫科技纳入旗下基金](https://news.google.com/rss/articles/CBMiYkFVX3lxTFBPeGVPMVF0SW9UcjFXZjd3UlA1c0R4b2laVm5oZENfbjFIM0o4eDZMZVlqdWdYR1NCSFRMVDJhVTVKdy1CdEk3ZFVYaHNPakRVUW1NVVp3VXhNTFF6OUFWZmxn?oc=5) ⭐️ 8.0/10

全球最大半导体 ETF 管理人正在考虑将长鑫科技（CXMT）纳入旗下基金，最早可能于 9 月底纳入。 此举将对半导体投资格局产生重大影响，因为长鑫科技是中国领先的 DRAM 制造商，也是全球存储市场的重要参与者。 长鑫科技是中国最大的上市公司之一，也是动态随机存取存储器（DRAM）领域的关键参与者，未来可能被纳入科创板综指等主要指数。

google\_news · 新浪网 · 8月9日 13:25

**背景**: 长鑫科技作为中国领先的 DRAM 制造商，近期成功上市，成为投资者关注半导体行业的重要标的。ETF 为投资者提供了通过一篮子股票（包括半导体公司）获得多元化投资机会的途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.eastmoney.com/a/202607103801814773.html">长鑫科技上市在即 有望纳入哪些指数？何时能借道ETF布局？</a></li>
<li><a href="https://xueqiu.com/4579887327/401921719">长鑫科技 指数纳入路径与ETF跟踪规模两个阶段，8只指数，ETF合计约8,2...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#CXMT`, `#ETF`, `#memory`, `#investment`

---