---
layout: default
title: "Horizon Summary: 2026-08-04 (ZH)"
date: 2026-08-04
content_date: 2026-08-03
lang: zh
---

> 报道范围：2026-08-03（Asia/Shanghai 自然日）

> 从 134 条内容中筛选出 12 条重要资讯。

---

1. [Andrej Karpathy 更新 micrograd 库](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp 发布版本 b10241](#item-2) ⭐️ 10.0/10
3. [llama.cpp 发布 b10235：Apple Silicon SILU\_BACK 操作与跨平台二进制文件](#item-3) ⭐️ 10.0/10
4. [DNA 分析设备曝漏洞，30 年证据文件面临篡改风险](#item-4) ⭐️ 10.0/10
5. [ComfyUI 原生支持 MiniMax H3，实现开放权重视频生成](#item-5) ⭐️ 9.0/10
6. [AirLLM 70B inference with single 4GB GPU](#item-6) ⭐️ 9.0/10
7. [Simon Willison 发布 condense- 1.0 库](#item-7) ⭐️ 9.0/10
8. [Your agent needs a computer, not a container — introducing @cloudflare/computer](#item-8) ⭐️ 9.0/10
9. [英伟达 170HX 矿卡被破解：最高解锁 80 GB 显存，二手价暴涨](#item-9) ⭐️ 9.0/10
10. [《独家新闻》长鑫存储计划在北京建设第二座芯片厂，正讨论融资--消息 - TradingView](#item-10) ⭐️ 9.0/10
11. [芯报丨长鑫存储增资至约 313.9 亿 - 电子工程专辑](#item-11) ⭐️ 9.0/10
12. [中国的人工智能存储雄心：全球“Co-NAND-DRAM”协同架构](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [Andrej Karpathy 更新 micrograd 库](https://github.com/karpathy/micrograd) ⭐️ 10.0/10

Andrej Karpathy 向他的 micrograd 仓库推送了一个提交，这是一个用于从头构建神经网络的教育库。 这次更新对 AI 教育社区具有重要意义，因为 micrograd 是理解自动微分和神经网络的基础工具。 Micrograd 是一个带有 PyTorch 风格 API 的小型标量自动微分引擎，旨在通过简化复杂概念来辅助教育。

github · karpathy · 8月3日 12:04

**背景**: Micrograd 是一个实现反向传播算法的紧凑型库，用于计算神经网络中的梯度。它常被用作学习者理解深度学习底层原理的起点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/micrograd">GitHub - karpathy/micrograd: A tiny scalar-valued autograd engine and a neural net library on top of it with PyTorch-like API · GitHub</a></li>
<li><a href="https://medium.com/@nico_X/micrograd-the-spelled-out-intro-to-neural-networks-and-backprop-written-walkthrough-a7a6532ff3a4">Micrograd: The Spelled Out Intro to Neural Networks and BackProp — Written Walkthrough | by Nicola Croce | Medium</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#autograd`, `#neural-networks`, `#open-source`, `#python`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp 发布版本 b10241](https://github.com/ggml-org/llama.cpp/releases/tag/b10241) ⭐️ 10.0/10

llama.cpp v10241 修复了 CUDA 数据竞争问题，并添加了双缓冲优化以提升推理性能。

github · github-actions\[bot\] · 8月3日 22:58

**标签**: `#llama.cpp`, `#CUDA`, `#AI inference`, `#software optimization`, `#data-race fix`

---

<a id="item-3"></a>
## [llama.cpp 发布 b10235：Apple Silicon SILU\_BACK 操作与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10235) ⭐️ 10.0/10

llama.cpp 版本 b10235 为 Apple Silicon 引入了新的 SILU\_BACK 操作，并为 macOS、Linux、Android 和 Windows 提供了预编译的二进制文件。 此次发布提升了 Apple Silicon 用户的性能，并通过为多样化的硬件和操作系统提供预构建工具，扩大了可访问性。 此次更新包括为 SILU\_BACK 操作实现的 Metal 后端，并因相关拉取请求而禁用了 macOS 上的 KleidiAI 支持。

github · github-actions\[bot\] · 8月3日 05:02

**背景**: llama.cpp 是一个在消费级硬件上高效运行的大型语言模型（LLM）推理引擎。Metal 后端使用 Apple 的图形 API 来加速 Apple Silicon 芯片上的张量操作。SILU（Sigmoid 线性单元）是神经网络中常见的激活函数，其反向传播对于模型的训练和微调至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/ggml-org/llama.cpp/5.2-metal-backend-%28apple%29">Metal Backend (Apple) | ggml-org/llama.cpp | DeepWiki</a></li>
<li><a href="https://github.com/ggml-org/ggml/blob/master/src/ggml-metal/ggml-metal-ops.cpp">ggml/src/ggml-metal/ggml-metal-ops.cpp at master - GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#macOS`, `#Open Source`, `#Inference`

---

<a id="item-4"></a>
## [DNA 分析设备曝漏洞，30 年证据文件面临篡改风险](https://www.wsj.com/tech/cybersecurity/security-flaw-placed-30-years-of-dna-evidence-at-risk-of-hacking-1932775a) ⭐️ 10.0/10

研究人员发现 Thermo Fisher Scientific DNA 分析设备存在严重漏洞，黑客可在不触发警报的情况下篡改自 1995 年以来的犯罪 DNA 文件。 该漏洞对美国刑事调查中使用的法医证据完整性构成严重威胁，可能危及司法系统的可靠性。 该漏洞利用 AI 生成的代码，使用 Anthropic 的 Claude 仅需约 45 分钟即可成功修改文件，公司已发布带有数字签名的软件更新以缓解风险。

telegram · zaihuapd · 8月3日 13:15

**背景**: Thermo Fisher Scientific 是法医科学中使用的实验室设备和分析仪器的主要供应商，美国超过 200 家实验室可能受此漏洞影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techradar.com/pro/security/weve-been-behind-the-ball-for-so-long-experts-say-dna-samples-from-crime-scene-forensics-can-be-modified-and-even-switched-using-an-ai-tool">&#x27;We’ve been behind the ball for so long&#x27;: Experts say DNA samples from crime-scene forensics can be modified and even switched using an AI tool | TechRadar</a></li>
<li><a href="https://thehackernews.com/2026/08/thermo-fisher-patches-flaw-that-could.html">Thermo Fisher Patches Flaw That Could Make DNA File Tampering Nearly Undetectable</a></li>

</ul>
</details>

**标签**: `#forensics`, `#security`, `#data-integrity`, `#vulnerability`, `#cybersecurity`

---

<a id="item-5"></a>
## [ComfyUI 原生支持 MiniMax H3，实现开放权重视频生成](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui) ⭐️ 9.0/10

ComfyUI 增加了对 MiniMax H3 视频生成模型的原生支持，实现了开放权重的 AI 视频生成，并包含权重剪枝和动态显存卸载等优化。 这一集成通过允许在消费级硬件上本地执行，降低了获取高质量视频生成的门槛，减少了对云 API 的依赖，并使开发者能够更快地迭代。 该模型的调制权重（约占参数的 40%）可以被剪枝并替换为查找表，将内存占用减少 66%（从 123.6 GB 降至 42.5 GB），从而在 RTX 3060 等显卡上实现 2K 视频生成。

hackernews · vblanco · 8月3日 21:34 · [社区讨论](https://news.ycombinator.com/item?id=49155629)

**背景**: ComfyUI 是一个用于 Stable Diffusion 和其他 AI 模型的节点式界面，而 MiniMax H3 是一个支持开放权重的最先进视频生成模型，可实现灵活的部署。

**社区讨论**: 用户报告称尽管在复杂场景下偶尔会出现卡顿，但结果令人印象深刻，有用户在 RTX 4070 Ti Super 上生成 10 秒 480p 视频耗时 10 分钟。

**标签**: `#AI`, `#Video Generation`, `#ComfyUI`, `#Optimization`, `#GPU`

---

<a id="item-6"></a>
## [AirLLM 70B inference with single 4GB GPU](https://github.com/lyogavin/airllm) ⭐️ 9.0/10

AirLLM enables 70B model inference on a single 4GB GPU through advanced memory management techniques.

hackernews · Anon84 · 8月3日 19:15 · [社区讨论](https://news.ycombinator.com/item?id=49154228)

**标签**: `#AI`, `#Machine Learning`, `#GPU`, `#Inference`, `#Memory Management`

---

<a id="item-7"></a>
## [Simon Willison 发布 condense- 1.0 库](https://simonwillison.net/2026/Aug/2/condense-json/#atom-everything) ⭐️ 9.0/10

Simon Willison 正式发布了 condense- 1.0，这是一个用于高效 JSON 数据操作和压缩的 Python 库。 该库通过识别和替换重复的字符串来帮助开发者在 JSON 数据中节省存储空间，这对于大型数据集和日志文件尤为有用。 该库使用特殊的 $r 语法来标记被替换的字符串，并提供 uncondense\_ 函数来恢复原始数据，使还原过程变得简单。

rss · Simon Willison · 8月3日 06:19

**背景**: JSON（JavaScript 对象表示法）是一种轻量级的数据交换格式，广泛用于在 Web 应用程序中存储和传输结构化数据。

**标签**: `#`, `#software-library`, `#data-processing`, `#developer-tools`

---

<a id="item-8"></a>
## [Your agent needs a computer, not a container — introducing @cloudflare/computer](https://blog.cloudflare.com/cloudflare-computer/) ⭐️ 9.0/10

Cloudflare introduces @cloudflare/computer, an agent runtime that dynamically orchestrates between isolates and Linux containers to provide scalable, secure computing environments for AI agents.

rss · Cloudflare Blog · 8月3日 21:15

**标签**: `#AI Agents`, `#Cloudflare`, `#Containerization`, `#Agent Runtime`, `#Software Engineering`

---

<a id="item-9"></a>
## [英伟达 170HX 矿卡被破解：最高解锁 80 GB 显存，二手价暴涨](https://finance.sina.com.cn/tech/roll/2026-08-03/doc-inikzqsf4659769.shtml) ⭐️ 9.0/10

Researchers have successfully hacked Nvidia CMP 170HX mining cards to unlock up to 80GB of VRAM and boost performance, causing a surge in secondary market prices.

telegram · zaihuapd · 8月3日 19:29

**标签**: `#Nvidia`, `#GPU`, `#Hardware Hacking`, `#AI Compute`, `#Security Vulnerability`

---

<a id="item-10"></a>
## [《独家新闻》长鑫存储计划在北京建设第二座芯片厂，正讨论融资--消息 - TradingView](https://news.google.com/rss/articles/CBMid0FVX3lxTE1xQ2RjU3M3djBsa3lON0xuZXBKcngySUxMdVF0dFlVbEtfVGFlc1YyLWE2MHIzOEZ3a2pUV081eEhseThQYWxCLXlHVFdEX3kxcUtYYVEtYk1oLWRfZnlXeEVHR1Aya3ZHQ25VMFRWLS1oQWpRSm04?oc=5) ⭐️ 9.0/10

TradingView reports that CXMT plans to build a second chip factory in Beijing and is discussing financing.

google\_news · TradingView · 8月3日 16:27

**标签**: `#semiconductors`, `#chip manufacturing`, `#CXMT`, `#China`, `#memory`

---

<a id="item-11"></a>
## [芯报丨长鑫存储增资至约 313.9 亿 - 电子工程专辑](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wTkdmcFRzVE5EdkZuMUJrSzdVd3BIS1Q0aWp4eEV4Z2RhY0FFaE1VNDNRZm5OOWVMUGRCQl90akgxTkZPb1JOZ3F3dTUxeVlvaE80?oc=5) ⭐️ 9.0/10

Financial news reporting that CXMT has increased its registered capital to approximately 31.39 billion yuan.

google\_news · 电子工程专辑 · 8月3日 20:30

**标签**: `#semiconductors`, `#memory`, `#investment`, `#hardware`, `#AI\_infrastructure`

---

<a id="item-12"></a>
## [中国的人工智能存储雄心：全球“Co-NAND-DRAM”协同架构](https://news.google.com/rss/articles/CBMikAFBVV95cUxQMWNnYmstd3BKWTRPaEg0RHFET0NCd2NRcnhLbjNIWXpJWEh3UFlMcVZlQjF3UEppVEx5YkI0RTd1OUJXLTRVX09WMnFTMThfQkN1eFdwenRqX01XaW83dmtJTkpIZVFrVzhIMElLREFReWhveFUzMDBHMGJsblZOczNhRERCc2w0eUJzVURfWTM?oc=5) ⭐️ 9.0/10

中国正在追求一种“Co-NAND-DRAM”协同架构以推进其人工智能存储能力，但具体细节尚未披露。 这一举措可能通过解决人工智能工作负载中的关键内存瓶颈，重塑全球半导体格局。 该架构可能结合了 NAND 闪存和 DRAM 技术以平衡存储密度和速度，尽管未提供具体技术细节。

google\_news · VT Markets · 8月3日 21:31

**背景**: DRAM 和 NAND 闪存是互补的存储技术：DRAM 提供高速易失性内存，而 NAND 提供高密度非易失性存储。3D X-DRAM 等创新旨在融合这些优势。中国的推进反映了减少对外国存储供应商依赖的更广泛努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_random-access_memory">Dynamic random-access memory - Wikipedia</a></li>
<li><a href="https://semiconductorinsight.com/blog/memory-at-the-core-of-digital-infrastructure-nand-and-dram/">Memory at the Core of Digital Infrastructure NAND And DRAM</a></li>
<li><a href="https://neosemic.com/">Home - Neo Semiconductor | X-Nand</a></li>

</ul>
</details>

**社区讨论**: 新闻项目中未提供社区评论。

**标签**: `#AI`, `#Hardware`, `#Semiconductors`, `#Storage`, `#China`

---