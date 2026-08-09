---
layout: default
title: "Horizon Summary: 2026-08-10 (EN)"
date: 2026-08-10
content_date: 2026-08-09
lang: en
---

> Coverage: 2026-08-09 (Asia/Shanghai calendar day)

> From 72 items, 10 important content pieces were selected

---

1. [llama.cpp b10332 Release with CI Fix and Pre-built Binaries](#item-1) ⭐️ 10.0/10
2. [llama.cpp v0.3.33 Release: CPU Backend Fix and Cross-Platform Binaries](#item-2) ⭐️ 9.0/10
3. [Noise-aware Training Reveals Threshold-like Accuracy Collapse in Analog Hardware](#item-3) ⭐️ 9.0/10
4. [First Generative Design of Viable Bacteriophage Genomes](#item-4) ⭐️ 9.0/10
5. [World&\#x27;s Largest Single AI Computing Facility Launches in Ulanqab](#item-5) ⭐️ 9.0/10
6. [MiniMax H3 团队办 AMA：将开源 2K 模型与稀疏注意力](#item-6) ⭐️ 9.0/10
7. [Apple Tests CXMT Memory Chips for iPhones and MacBooks](#item-7) ⭐️ 9.0/10
8. [Auto Mode Default in Claude Code for Pro, Max, and Team Plans](#item-8) ⭐️ 8.0/10
9. [CXMT&\#x27;s Financial Turnaround: From 30 Billion Loss to 3 Billion Daily Profit](#item-9) ⭐️ 8.0/10
10. [Global Largest Semiconductor ETF Manager Considers Adding CXMT](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp b10332 Release with CI Fix and Pre-built Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10332) ⭐️ 10.0/10

The llama.cpp project released version b10332, removing the GGML\_HIP\_ROCWMMA\_FATTN flag from the CI pipeline and providing pre-built binaries for macOS, Linux, Windows, and Android across various architectures. This release improves the stability and compatibility of llama.cpp, a widely used open-source tool for running Large Language Models \(LLMs\) locally, by fixing a specific CI issue and offering ready-to-use binaries for developers and users. The release includes pre-built binaries for macOS \(Apple Silicon and Intel\), Linux \(Ubuntu with CPU, Vulkan, ROCm, OpenVINO, and SYCL support\), Windows \(CPU, OpenCL Adreno, CUDA 12/13, Vulkan, OpenVINO, SYCL, and HIP\), Android \(arm64 CPU\), and openEuler, with KleidiAI support disabled for macOS.

github · github-actions\[bot\] · Aug 9, 18:48

**Background**: llama.cpp is a high-performance C++ library for running LLMs locally, optimized for various hardware backends like CUDA, ROCm, and Vulkan. GGML\_HIP\_ROCWMMA\_FATTN is a flag that enables the rocWMMA library for enhanced Flash Attention performance on AMD GPUs, particularly RDNA3+ or CDNA architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/15021">Performance of llama.cpp on AMD ROCm ( HIP ) · ggml -org llama.cpp...</a></li>
<li><a href="https://www.banandre.com/blog/amd-rdna3-faster-llamacpp-performance-rocm-optimizations">AMD RDNA3 Users Finally Get Decent llama.cpp... - Banandre</a></li>
<li><a href="https://www.amd.com/en/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html">Trillion-Parameter LLM on an AMD Ryzen™ AI Max+ Cluster</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#open-source`, `#AI`, `#machine-learning`, `#local-inference`

---

<a id="item-2"></a>
## [llama.cpp v0.3.33 Release: CPU Backend Fix and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10333) ⭐️ 9.0/10

The llama.cpp v0.3.33 release \(b10333\) includes a critical fix for a missing Q5\_0 dispatch in the SpaceMiT backend and provides pre-built binaries for macOS, Linux, and iOS. This release is significant for AI developers and users as it improves the reliability of LLM inference on specific hardware architectures and makes the software more accessible across different operating systems. The SpaceMiT backend fix addresses a specific issue with Q5\_0 quantization, and the release offers extensive binary support including CPU, Vulkan, CUDA, ROCm, and OpenVINO backends for various platforms.

github · github-actions\[bot\] · Aug 9, 19:21

**Background**: llama.cpp is a popular C/C++ library for running Large Language Models \(LLMs\) efficiently on consumer hardware. It supports various quantization formats like Q5\_0 to reduce memory usage and optimize performance. The SpaceMiT backend is a specific implementation for SpacemiT&\#x27;s RISC-V CPUs, and KleidiAI is an ARM-optimized library for AI micro-kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases: ggml-org/llama.cpp - GitHub</a></li>
<li><a href="https://github.com/spacemit-com">spacemit.com · GitHub</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI inference`, `#software release`, `#CPU backend`, `#cross-platform`

---

<a id="item-3"></a>
## [Noise-aware Training Reveals Threshold-like Accuracy Collapse in Analog Hardware](https://www.reddit.com/r/MachineLearning/comments/1vjmw53/noiseaware_training_for_analog_hardware_accuracy/) ⭐️ 9.0/10

A Reddit post reports experimental findings showing that accuracy in analog in-memory compute degrades abruptly at a threshold rather than smoothly, and noise-aware training shifts this threshold significantly. This finding is significant for the analog compute ecosystem as it challenges the assumption of smooth degradation and highlights the need for hardware-aware training strategies to maintain model performance. The experiment showed accuracy dropping from 83% to 64% and then to near-random levels, while noise-aware training improved performance from 61% to 39% at matched noise levels, suggesting the optimizer finds flatter minima.

reddit · r/MachineLearning · /u/Georgiou1226 · Aug 9, 18:55

**Background**: Analog in-memory compute is gaining attention as an energy-efficient alternative to digital compute, but it suffers from inherent noise and variability that can degrade model accuracy. Hardware-aware training methods aim to mitigate these issues by simulating noise during training.

<details><summary>References</summary>
<ul>
<li><a href="https://prismix.dev/news/3bf841047f18">Noise-aware training for analog hardware: accuracy collapses ...</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-56595-2">The inherent adversarial robustness of analog in-memory ...</a></li>
<li><a href="https://aihwkit.readthedocs.io/en/latest/hwa_training.html">Analog Hardware-aware Training - Read the Docs</a></li>

</ul>
</details>

**Discussion**: The author invites the community to discuss whether the flat-minima explanation is correct or if other factors drive the performance gap, and asks about research on optimizing directly for noise robustness.

**Tags**: `#analog-compute`, `#noise-robustness`, `#hardware-software-co-design`, `#machine-learning`, `#in-memory-compute`

---

<a id="item-4"></a>
## [First Generative Design of Viable Bacteriophage Genomes](https://www.reddit.com/r/MachineLearning/comments/1vjj4pr/r_generative_design_of_novel_bacteriophages_with/) ⭐️ 9.0/10

Researchers report the first generative design of viable bacteriophage genomes using frontier genome language models Evo 1 and Evo 2, resulting in 16 novel phages with substantial evolutionary novelty. This breakthrough demonstrates the potential of AI to design functional biological systems at the whole-genome scale, opening new avenues for synthetic biology and biotechnology applications. The study used the lytic phage ΦX174 as a design template and achieved experimental validation of AI-generated genomes, with Evo 2 being a 40-billion-parameter model trained on 9 trillion DNA base pairs.

reddit · r/MachineLearning · /u/moschles · Aug 9, 15:11

**Background**: Genome language models \(gLMs\) are large language models trained on DNA sequences to model complex biological functions. Evo 2 is a genomic foundation model capable of generalist prediction and design tasks across DNA, RNA, and proteins.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12805252/">A comprehensive survey of genome language models in ...</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-10176-5">Genome modelling and design across all domains of life with Evo 2</a></li>
<li><a href="https://astrobiology.com/2026/01/12/generative-design-of-novel-bacteriophages-with-genome-language-models/">Generative Design Of Novel Bacteriophages With Genome ...</a></li>

</ul>
</details>

**Tags**: `#genomics`, `#machine learning`, `#biological systems`, `#generative design`, `#bacteriophages`

---

<a id="item-5"></a>
## [World&\#x27;s Largest Single AI Computing Facility Launches in Ulanqab](https://www.globaltimes.cn/page/202608/1367666.shtml) ⭐️ 9.0/10

On August 6, Envision Group announced the official launch of the &\#x27;Envision Ulanqab Galaxy Base,&\#x27; which is the world&\#x27;s largest single AI computing facility. This facility represents a significant milestone in AI infrastructure development, offering a scalable solution for domestic computing clusters and supporting the &\#x27;East Data West Computing&\#x27; strategy. The base covers 120,000 square meters, supports parallel computing with millions of GPUs, and has a total capacity of 2GW, with over 80% of its power coming from green energy.

telegram · zaihuapd · Aug 9, 13:06

**Background**: The &\#x27;East Data West Computing&\#x27; strategy is a national initiative to optimize data processing by shifting workloads from the east to the west, leveraging the abundant renewable energy resources in regions like Ulanqab.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/%E8%BF%9C%E6%99%AF%E6%98%9F%E6%B2%B3%E5%9F%BA%E5%9C%B0/68089868">远景星河基地 - 百度百科</a></li>
<li><a href="https://news.qq.com/rain/a/20260618A04B3F00">远景张雷：启动Mission Gobi AIDC建设计划，让全球戈壁成为下一代智能...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Hardware`, `#Infrastructure`, `#Cloud Computing`, `#Green Energy`

---

<a id="item-6"></a>
## [MiniMax H3 团队办 AMA：将开源 2K 模型与稀疏注意力](https://www.reddit.com/r/StableDiffusion/s/fjM3d7AEV8) ⭐️ 9.0/10

MiniMax H3 team announces open-source plans for a 2K regeneration model and sparse attention implementation while addressing community feedback on quality issues.

telegram · zaihuapd · Aug 9, 16:28

**Tags**: `#AI`, `#Machine Learning`, `#Open Source`, `#Sparse Attention`, `#Video Generation`

---

<a id="item-7"></a>
## [Apple Tests CXMT Memory Chips for iPhones and MacBooks](https://news.google.com/rss/articles/CBMiYEFVX3lxTE04TmFmbnQzS0FETzh6RjZkb3ZwTDlaTUdXUHp2QTJyTEVTYjdXSDdiSGwxY0tvMXBLUUgxLTZtUU5zUHVoYzh2dURmZ0hYZGtuRXo3RS1pRHRJTmVncEhPQg?oc=5) ⭐️ 9.0/10

Apple is reportedly testing memory chips from Chinese manufacturer ChangXin Memory Technologies \(CXMT\) for use in iPhones and MacBooks. This move could signal Apple&\#x27;s strategic shift to diversify its supply chain amid global semiconductor shortages and geopolitical tensions. The testing reportedly focuses on chips for the Chinese domestic market, and cooperation may require approval from the U.S. government.

google\_news · 东方财富 · Aug 9, 15:22

**Background**: CXMT is a Chinese DRAM manufacturer founded in 2016, specializing in memory chips for mobile devices, PCs, and servers. Apple has historically relied on suppliers like Samsung and SK Hynix, but recent supply constraints have prompted exploration of alternative sources.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.cxmt.com/en/">About cxmt - cxmt</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lsOXRMakVSR09PUGZCazB1QkZDZ0FQAQ?hl=en-IN&amp;gl=IN&amp;ceid=IN:en">Google News - Report: Apple tests CXMT memory chips amid supply...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#Apple`, `#CXMT`, `#hardware`

---

<a id="item-8"></a>
## [Auto Mode Default in Claude Code for Pro, Max, and Team Plans](https://simonwillison.net/2026/Aug/8/auto-mode/#atom-everything) ⭐️ 8.0/10

Starting August 14, 2026, Anthropic is making auto mode the default setting for new sessions in Claude Code for Pro, Max, and Team plans, following successful internal testing. This change represents a significant shift in AI-assisted coding tools, moving towards more autonomous agent behavior while addressing critical safety concerns like prompt injection and accidental damage. Internal evaluations show auto mode blocked 89% of harmful actions compared to only 13.6% of human reviewers, and third-party testing found zero successful attacks against Claude Fable 5, Opus 5, or Sonnet 5 running auto mode.

rss · Simon Willison · Aug 9, 06:36

**Background**: Claude Code is an AI-assisted coding tool that helps developers write code more efficiently. Auto mode is a permissions feature where the AI agent makes permission decisions automatically with safeguards, designed to reduce confirmation fatigue from constant human approval requests.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://medium.com/@richardhightower/claude-code-auto-mode-escape-permission-fatigue-guide-to-automated-permissions-a122568e1ed6">Claude Code Auto Mode : Escape Permission Fatigue... | Medium</a></li>
<li><a href="https://beamsec.medium.com/prompt-injection-when-your-ai-turns-against-you-75ba5c7447db">Prompt Injection : When Your AI Turns Against You | Medium</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#AI-assisted coding`, `#Software development`, `#AI safety`, `#Product updates`

---

<a id="item-9"></a>
## [CXMT&\#x27;s Financial Turnaround: From 30 Billion Loss to 3 Billion Daily Profit](https://news.google.com/rss/articles/CBMiUEFVX3lxTFB0dmVRV0JzZkQ4d0FsWWpYbExaY3ZxbC1GSDhGWHNwMnlVREFqLV9IVS1MU0NsMnZreG1QWTNYdkI1Nld4cUE5dW9HNTBBU1BZ?oc=5) ⭐️ 8.0/10

CXMT has successfully transformed from a massive loss of 30 billion to generating 3 billion in daily revenue, marking a significant financial recovery. This turnaround highlights CXMT&\#x27;s resilience and strategic success in the competitive DRAM market, setting a benchmark for Chinese semiconductor manufacturers. The recovery is attributed to CXMT&\#x27;s technological advancements and optimized production processes, though specific details are not provided in the article.

google\_news · 凤凰网 · Aug 9, 08:57

**Background**: CXMT \(ChangXin Memory Technologies\) is a leading Chinese DRAM manufacturer, known for its innovation in semiconductor manufacturing and contribution to China&\#x27;s tech self-reliance.

<details><summary>References</summary>
<ul>
<li><a href="http://www.icdistributor.cn/index.php?_m=mod_product&amp;_a=view&amp;p_id=156">CXMT 长 鑫 --深圳市砹矽 科 技 有限公司</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/621945568">国产存储芯片部分企业名单盘点 - 知乎</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#DRAM`, `#memory`, `#manufacturing`, `#business`

---

<a id="item-10"></a>
## [Global Largest Semiconductor ETF Manager Considers Adding CXMT](https://news.google.com/rss/articles/CBMiYkFVX3lxTFBPeGVPMVF0SW9UcjFXZjd3UlA1c0R4b2laVm5oZENfbjFIM0o4eDZMZVlqdWdYR1NCSFRMVDJhVTVKdy1CdEk3ZFVYaHNPakRVUW1NVVp3VXhNTFF6OUFWZmxn?oc=5) ⭐️ 8.0/10

The global largest semiconductor ETF manager is considering adding ChangXin Memory Technologies \(CXMT\) to its fund, with the earliest possible inclusion date being late September. This move would significantly impact the semiconductor investment landscape, as CXMT is a leading Chinese DRAM manufacturer and a major player in the global memory market. CXMT is China&\#x27;s largest publicly listed company following its IPO and is a key player in the dynamic random-access memory \(DRAM\) sector, with potential inclusion in major indices like the STAR Market Composite Index.

google\_news · 新浪网 · Aug 9, 13:25

**Background**: CXMT, a leading Chinese DRAM manufacturer, recently went public, making it a focal point for investors seeking exposure to the semiconductor industry. ETFs provide a way for investors to gain diversified exposure to a basket of stocks, including semiconductor companies.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.eastmoney.com/a/202607103801814773.html">长鑫科技上市在即 有望纳入哪些指数？何时能借道ETF布局？</a></li>
<li><a href="https://xueqiu.com/4579887327/401921719">长鑫科技 指数纳入路径与ETF跟踪规模两个阶段，8只指数，ETF合计约8,2...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#CXMT`, `#ETF`, `#memory`, `#investment`

---