---
layout: default
title: "Horizon Summary: 2026-08-04 (EN)"
date: 2026-08-04
content_date: 2026-08-03
lang: en
---

> Coverage: 2026-08-03 (Asia/Shanghai calendar day)

> From 134 items, 12 important content pieces were selected

---

1. [Andrej Karpathy Updates micrograd Library](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10241](#item-2) ⭐️ 10.0/10
3. [llama.cpp Release b10235: Apple Silicon SILU\_BACK Op &amp; Cross-Platform Binaries](#item-3) ⭐️ 10.0/10
4. [Security Flaw in DNA Analysis Equipment Risks Tampering with 30 Years of Evidence](#item-4) ⭐️ 10.0/10
5. [ComfyUI Adds Native MiniMax H3 Support for Open-Weight Video Generation](#item-5) ⭐️ 9.0/10
6. [AirLLM 70B inference with single 4GB GPU](#item-6) ⭐️ 9.0/10
7. [Simon Willison Releases condense- 1.0 Library](#item-7) ⭐️ 9.0/10
8. [Your agent needs a computer, not a container — introducing @cloudflare/computer](#item-8) ⭐️ 9.0/10
9. [英伟达 170HX 矿卡被破解：最高解锁 80 GB 显存，二手价暴涨](#item-9) ⭐️ 9.0/10
10. [《独家新闻》长鑫存储计划在北京建设第二座芯片厂，正讨论融资--消息 - TradingView](#item-10) ⭐️ 9.0/10
11. [芯报丨长鑫存储增资至约313.9亿 - 电子工程专辑](#item-11) ⭐️ 9.0/10
12. [China&\#x27;s AI Storage Ambition: Global Co-NAND-DRAM Architecture](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [Andrej Karpathy Updates micrograd Library](https://github.com/karpathy/micrograd) ⭐️ 10.0/10

Andrej Karpathy pushed a commit to his micrograd repository, an educational library for building neural networks from scratch. This update is significant for the AI education community as micrograd is a foundational tool for understanding autograd and neural networks. Micrograd is a tiny scalar-valued autograd engine with a PyTorch-like API, designed for educational purposes to simplify complex concepts.

github · karpathy · Aug 3, 12:04

**Background**: Micrograd is a compact library that implements backpropagation, an algorithm for computing gradients in neural networks. It is often used as a starting point for learners to understand deep learning under the hood.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/karpathy/micrograd">GitHub - karpathy/micrograd: A tiny scalar-valued autograd engine and a neural net library on top of it with PyTorch-like API · GitHub</a></li>
<li><a href="https://medium.com/@nico_X/micrograd-the-spelled-out-intro-to-neural-networks-and-backprop-written-walkthrough-a7a6532ff3a4">Micrograd: The Spelled Out Intro to Neural Networks and BackProp — Written Walkthrough | by Nicola Croce | Medium</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#autograd`, `#neural-networks`, `#open-source`, `#python`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10241](https://github.com/ggml-org/llama.cpp/releases/tag/b10241) ⭐️ 10.0/10

llama.cpp v10241 fixes CUDA data-races and adds double-buffering optimizations for improved inference performance.

github · github-actions\[bot\] · Aug 3, 22:58

**Tags**: `#llama.cpp`, `#CUDA`, `#AI inference`, `#software optimization`, `#data-race fix`

---

<a id="item-3"></a>
## [llama.cpp Release b10235: Apple Silicon SILU\_BACK Op &amp; Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10235) ⭐️ 10.0/10

llama.cpp version b10235 introduces a new SILU\_BACK operation for Apple Silicon and provides pre-compiled binaries for macOS, Linux, Android, and Windows. This release enhances performance for Apple Silicon users and expands accessibility by offering pre-built tools for diverse hardware and operating systems. The update includes a Metal backend implementation for the SILU\_BACK operation and disables KleidiAI support for macOS due to a related pull request.

github · github-actions\[bot\] · Aug 3, 05:02

**Background**: llama.cpp is an open-source inference engine for Large Language Models \(LLMs\) that runs efficiently on consumer hardware. The Metal backend uses Apple&\#x27;s graphics API to accelerate tensor operations on Apple Silicon chips. SILU \(Sigmoid Linear Unit\) is a common activation function in neural networks, and its backward pass is crucial for training and fine-tuning models.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/ggml-org/llama.cpp/5.2-metal-backend-%28apple%29">Metal Backend (Apple) | ggml-org/llama.cpp | DeepWiki</a></li>
<li><a href="https://github.com/ggml-org/ggml/blob/master/src/ggml-metal/ggml-metal-ops.cpp">ggml/src/ggml-metal/ggml-metal-ops.cpp at master - GitHub</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#macOS`, `#Open Source`, `#Inference`

---

<a id="item-4"></a>
## [Security Flaw in DNA Analysis Equipment Risks Tampering with 30 Years of Evidence](https://www.wsj.com/tech/cybersecurity/security-flaw-placed-30-years-of-dna-evidence-at-risk-of-hacking-1932775a) ⭐️ 10.0/10

Researchers discovered a critical vulnerability in Thermo Fisher Scientific DNA analysis equipment that allows hackers to tamper with forensic DNA files from approximately 1995 to present without triggering detection alerts. This vulnerability poses a severe threat to the integrity of forensic evidence used in criminal investigations across the United States, potentially compromising the justice system&\#x27;s reliability. The exploit uses AI-generated code, with a successful modification taking only 45 minutes using Anthropic&\#x27;s Claude, and the company has released software updates with digital signatures to mitigate the risk.

telegram · zaihuapd · Aug 3, 13:15

**Background**: Thermo Fisher Scientific is a major supplier of laboratory equipment and analytical instruments used in forensic science, with over 200 laboratories in the US potentially affected by this vulnerability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techradar.com/pro/security/weve-been-behind-the-ball-for-so-long-experts-say-dna-samples-from-crime-scene-forensics-can-be-modified-and-even-switched-using-an-ai-tool">&#x27;We’ve been behind the ball for so long&#x27;: Experts say DNA samples from crime-scene forensics can be modified and even switched using an AI tool | TechRadar</a></li>
<li><a href="https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html">Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable</a></li>

</ul>
</details>

**Tags**: `#forensics`, `#security`, `#data-integrity`, `#vulnerability`, `#cybersecurity`

---

<a id="item-5"></a>
## [ComfyUI Adds Native MiniMax H3 Support for Open-Weight Video Generation](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 9.0/10

ComfyUI has added native support for the MiniMax H3 video generation model, enabling open-weight AI video creation with optimizations like weight pruning and dynamic VRAM offloading. This integration democratizes access to high-quality video generation by allowing local execution on consumer hardware, reducing reliance on cloud APIs and enabling faster iteration for developers. The model&\#x27;s modulation weights \(~40% of parameters\) can be pruned and replaced with a lookup table, reducing memory footprint by 66% \(from 123.6 GB to 42.5 GB\), enabling 2K video generation on GPUs like the RTX 3060.

hackernews · vblanco · Aug 3, 21:34 · [Discussion](https://news.ycombinator.com/item?id=49155629)

**Background**: ComfyUI is a node-based interface for Stable Diffusion and other AI models, while MiniMax H3 is a state-of-the-art video generation model that supports open weights for flexible deployment.

**Discussion**: Users report impressive results despite occasional jank in complex scenarios, with one user noting a 10-minute generation time for a 10-second 480p video on an RTX 4070 Ti Super.

**Tags**: `#AI`, `#Video Generation`, `#ComfyUI`, `#Optimization`, `#GPU`

---

<a id="item-6"></a>
## [AirLLM 70B inference with single 4GB GPU](https://github.com/lyogavin/airllm) ⭐️ 9.0/10

AirLLM enables 70B model inference on a single 4GB GPU through advanced memory management techniques.

hackernews · Anon84 · Aug 3, 19:15 · [Discussion](https://news.ycombinator.com/item?id=49154228)

**Tags**: `#AI`, `#Machine Learning`, `#GPU`, `#Inference`, `#Memory Management`

---

<a id="item-7"></a>
## [Simon Willison Releases condense- 1.0 Library](https://simonwillison.net/2026/Aug/2/condense-json/#atom-everything) ⭐️ 9.0/10

Simon Willison has officially released condense- 1.0, a Python library designed for efficient JSON data manipulation and compression. This library helps developers save storage space in JSON data by identifying and replacing duplicated strings, which is particularly useful for large datasets and log files. The library uses a special $r syntax to mark replaced strings and provides an uncondense\_ function to reverse the process, making it easy to restore original data.

rss · Simon Willison · Aug 3, 06:19

**Background**: JSON \(JavaScript Object Notation\) is a lightweight data interchange format widely used for storing and transmitting structured data in web applications.

**Tags**: `#`, `#software-library`, `#data-processing`, `#developer-tools`

---

<a id="item-8"></a>
## [Your agent needs a computer, not a container — introducing @cloudflare/computer](https://blog.cloudflare.com/cloudflare-computer/) ⭐️ 9.0/10

Cloudflare introduces @cloudflare/computer, an agent runtime that dynamically orchestrates between isolates and Linux containers to provide scalable, secure computing environments for AI agents.

rss · Cloudflare Blog · Aug 3, 21:15

**Tags**: `#AI Agents`, `#Cloudflare`, `#Containerization`, `#Agent Runtime`, `#Software Engineering`

---

<a id="item-9"></a>
## [英伟达 170HX 矿卡被破解：最高解锁 80 GB 显存，二手价暴涨](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 9.0/10

Researchers have successfully hacked Nvidia CMP 170HX mining cards to unlock up to 80GB of VRAM and boost performance, causing a surge in secondary market prices.

telegram · zaihuapd · Aug 3, 19:29

**Tags**: `#Nvidia`, `#GPU`, `#Hardware Hacking`, `#AI Compute`, `#Security Vulnerability`

---

<a id="item-10"></a>
## [《独家新闻》长鑫存储计划在北京建设第二座芯片厂，正讨论融资--消息 - TradingView](https://news.google.com/rss/articles/CBMid0FVX3lxTE1xQ2RjU3M3djBsa3lON0xuZXBKcngySUxMdVF0dFlVbEtfVGFlc1YyLWE2MHIzOEZ3a2pUV081eEhseThQYWxCLXlHVFdEX3kxcUtYYVEtYk1oLWRfZnlXeEVHR1Aya3ZHQ25VMFRWLS1oQWpRSm04?oc=5) ⭐️ 9.0/10

TradingView reports that CXMT plans to build a second chip factory in Beijing and is discussing financing.

google\_news · TradingView · Aug 3, 16:27

**Tags**: `#semiconductors`, `#chip manufacturing`, `#CXMT`, `#China`, `#memory`

---

<a id="item-11"></a>
## [芯报丨长鑫存储增资至约313.9亿 - 电子工程专辑](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wTkdmcFRzVE5EdkZuMUJrSzdVd3BIS1Q0aWp4eEV4Z2RhY0FFaE1VNDNRZm5OOWVMUGRCQl90akgxTkZPb1JOZ3F3dTUxeVlvaE80?oc=5) ⭐️ 9.0/10

Financial news reporting that CXMT has increased its registered capital to approximately 31.39 billion yuan.

google\_news · 电子工程专辑 · Aug 3, 20:30

**Tags**: `#semiconductors`, `#memory`, `#investment`, `#hardware`, `#AI\_infrastructure`

---

<a id="item-12"></a>
## [China&\#x27;s AI Storage Ambition: Global Co-NAND-DRAM Architecture](https://news.google.com/rss/articles/CBMikAFBVV95cUxQMWNnYmstd3BKWTRPaEg0RHFET0NCd2NRcnhLbjNIWXpJWEh3UFlMcVZlQjF3UEppVEx5YkI0RTd1OUJXLTRVX09WMnFTMThfQkN1eFdwenRqX01XaW83dmtJTkpIZVFrVzhIMElLREFReWhveFUzMDBHMGJsblZOczNhRERCc2w0eUJzVURfWTM?oc=5) ⭐️ 9.0/10

China is pursuing a &\#x27;Co-NAND-DRAM&\#x27; architecture to advance its AI storage capabilities, though the specific details remain undisclosed. This initiative could reshape the global semiconductor landscape by addressing critical memory bottlenecks in AI workloads. The architecture likely combines NAND flash and DRAM technologies to balance storage density and speed, though technical specifics are not provided.

google\_news · VT Markets · Aug 3, 21:31

**Background**: DRAM and NAND flash are complementary memory technologies: DRAM offers high-speed volatile memory, while NAND provides high-density non-volatile storage. Innovations like 3D X-DRAM aim to merge these benefits. China&\#x27;s push reflects broader efforts to reduce reliance on foreign memory suppliers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://semiconductorinsight.com/blog/memory-at-the-core-of-digital-infrastructure-nand-and-dram/">Memory at the Core of Digital Infrastructure NAND And DRAM</a></li>
<li><a href="https://neosemic.com/">Home - Neo Semiconductor | X-Nand</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the news item.

**Tags**: `#AI`, `#Hardware`, `#Semiconductors`, `#Storage`, `#China`

---