---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
content_date: 2026-08-11
lang: zh
---

> 报道范围：2026-08-11（Asia/Shanghai 自然日）

> 从 113 条内容中筛选出 12 条重要资讯。

---

1. [vLLM v0.27.0 添加了 Kimi K3、PyTorch 2.13 和新模型](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10353 修复 CUDA 和 Metal 中的内存步长错误](#item-2) ⭐️ 10.0/10
3. [llama.cpp 发布 b10355 版本，新增多输出采样和令牌推测功能](#item-3) ⭐️ 9.0/10
4. [ollama/ollama released v0.32.9](#item-4) ⭐️ 9.0/10
5. [Ollama v0.32.8 发布 Muse Glimmer 模型](#item-5) ⭐️ 9.0/10
6. [从专有 LLM API 窃取推理轨迹](#item-6) ⭐️ 9.0/10
7. [伦敦地铁扩大实时面部识别试验](#item-7) ⭐️ 9.0/10
8. [通过 Virtualization.framework 在 macOS 虚拟机中实现 llama.cpp 11.08 倍加速](#item-8) ⭐️ 9.0/10
9. [深入探究：通过 MitM 代理拦截 GitHub Copilot 流量](#item-9) ⭐️ 9.0/10
10. [手动设置权重实现 Transformer 精确算术运算](#item-10) ⭐️ 9.0/10
11. [苹果被曝正测试长鑫存储芯片 用于在中国市场销售的设备 - cls.cn](#item-11) ⭐️ 9.0/10
12. [长鑫存储 DDR5 良率提升，PC 大厂采购策略差异大](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [vLLM v0.27.0 添加了 Kimi K3、PyTorch 2.13 和新模型](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 10.0/10

vLLM v0.27.0 引入了 Kimi K3 的完整栈支持，升级了 PyTorch 2.13.0 和 Triton 3.7.1，并添加了 Qwen3.5 和 K-EXAONE-2.0-750B-A37B 等新模型。 此次发布显著推进了 AI 计算效率和模型支持，能够在 NVIDIA Rubin 等下一代硬件上实现更好的性能，并改进了大型语言模型服务的生态系统。 关键更新包括为 FlashAttention 4 添加 FP8 KV 缓存支持，扩展 Model Runner V2 以支持非生成式工作负载，并为 Rust 前端添加新的 gRPC 控制平面。

github · khluu · 8月11日 05:18

**背景**: vLLM 是一个高性能的大语言模型推理引擎，专为服务大型模型而优化，支持各种硬件后端和模型架构。

**标签**: `#AI`, `#LLM`, `#PyTorch`, `#Hardware`, `#OpenSource`

---

<a id="item-2"></a>
## [llama.cpp b10353 修复 CUDA 和 Metal 中的内存步长错误](https://github.com/ggml-org/llama.cpp/releases/tag/b10353) ⭐️ 10.0/10

llama.cpp 发布版本 b10353 修复了 CUDA 和 Metal 后端中 ROLL 操作的关键内存步长错误，该错误在处理非连续内存时会导致静默的数据损坏。 此修复对使用这些后端的开发者至关重要，因为它确保了张量的正确处理，并防止 AI 模型执行中出现错误的结果。 该错误发生是因为 CUDA 和 Metal 内核仅按元素数量（ne）进行索引，而忽略了内存步长（nb），而 CPU 后端正确处理了步长。修复方案为两个后端添加了连续性要求，并包含了一个针对置换输入的测试用例。

github · github-actions\[bot\] · 8月11日 06:00

**背景**: GGML 是 llama.cpp 用于高效机器学习推理的自定义张量库。GGML 中的张量可以存储在非连续的内存布局中，其中第一维度（ne\[0\]）是连续的，但其他维度可能有步长。ROLL 操作移动张量元素，其正确性取决于正确的步长处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@yifeiw203/ggml-deep-dive-ii-memory-management-in-context-only-mode-part-1-8397a1055363">GGML Deep Dive II: Memory Management in Context-only Mode | by Yifei Wang | Medium</a></li>
<li><a href="https://gist.github.com/ddh0/9696e1928b31125404d12d0a2da31c42">A Brief Guide to GGML · GitHub</a></li>
<li><a href="https://deepwiki.com/ggml-org/llama.cpp/3.6-memory-management-and-kv-cache">Memory Management and KV Cache | ggml-org/llama.cpp | DeepWiki</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#CUDA`, `#Metal`, `#ggml`, `#bugfix`

---

<a id="item-3"></a>
## [llama.cpp 发布 b10355 版本，新增多输出采样和令牌推测功能](https://github.com/ggml-org/llama.cpp/releases/tag/b10355) ⭐️ 9.0/10

llama.cpp b10355 版本引入了多输出后端采样和令牌推测功能，以提升 LLM 推理性能，同时修复了 CPU/GPU 分布和后端采样不匹配的问题。 此次更新显著提高了本地 LLM 的推理速度和效率，使硬件利用率更高，并促进了开源 AI 模型在消费级硬件上的更广泛采用。 主要变更包括启用带令牌推测的后端采样、钳制掩码总和、添加用于最大输出的数字上下文参数，以及修复 Vulkan 测试和内存重用问题。

github · github-actions\[bot\] · 8月11日 07:15

**背景**: llama.cpp 是一个用于在本地运行大型语言模型的高性能 C++ 库，支持 CUDA、Metal 和 Vulkan 等多种后端，以优化不同硬件平台上的推理性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youngju.dev/blog/llm/2026-03-14-llm-inference-optimization-vllm-tensorrt-speculative-decoding.en">The Complete Guide to LLM Inference Optimization: vLLM...</a></li>
<li><a href="https://predibase.com/blog/llm-inference-benchmarks-predibase-fireworks-vllm">Real-World LLM Inference Benchmarks: How Predibase Built the...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#C++`, `#Open Source`, `#Local LLM`

---

<a id="item-4"></a>
## [ollama/ollama released v0.32.9](https://github.com/ollama/ollama/releases/tag/v0.32.9) ⭐️ 9.0/10

Ollama v0.32.9 adds the NVIDIA Nemotron 3.5 Lightning MoE model and fixes a Muse Glimmer parser bug.

github · dhiltgen · 8月11日 21:23

**标签**: `#ollama`, `#nvidia`, `#moe`, `#llm`, `#open-source`

---

<a id="item-5"></a>
## [Ollama v0.32.8 发布 Muse Glimmer 模型](https://github.com/ollama/ollama/releases/tag/v0.32.8) ⭐️ 9.0/10

Ollama v0.32.8 引入了 Muse Glimmer，这是一个针对编码代理和助手优化的新模型，支持 Apple Silicon 和 NVIDIA 平台。 此次发布通过为编码代理和助手提供高性能的本地 AI 模型选项，增强了生态系统，特别是对 Apple Silicon 上的开发者具有显著益处。 Muse Glimmer 通过 Ollama 的 MLX 引擎支持 DFlash 和图像输入，提供如 \`ollama run muse-glimmer\` 的本地执行命令，并可与 Claude Code 和 Pi 等框架集成。

github · github-actions\[bot\] · 8月11日 07:49

**背景**: MLX 是 LM Studio 推出的统一多模态引擎架构，利用 mlx-lm 和 mlx-vlm 等 Python 包在 Apple Silicon M 芯片上高效执行 LLM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lmstudio-ai/mlx-engine">GitHub - lmstudio-ai/mlx-engine: LM Studio Apple MLX engine · GitHub</a></li>
<li><a href="https://lmstudio.ai/blog/unified-mlx-engine">Introducing the unified multi-modal `MLX` engine architecture in LM Studio | LM Studio Blog | LM Studio</a></li>
<li><a href="https://github.com/z-lab/dflash">GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub</a></li>

</ul>
</details>

**标签**: `#ollama`, `#ai-model`, `#apple-silicon`, `#coding-agent`, `#mlx`

---

<a id="item-6"></a>
## [从专有 LLM API 窃取推理轨迹](https://stolen-thoughts.com/) ⭐️ 9.0/10

技术分析演示了如何从专有 LLM API 提取推理轨迹，并通过模型重放攻击加以利用。 这一漏洞凸显了 LLM API 中的重大安全风险，可能使未经授权的访问成为可能，并破坏对 AI 系统的信任。 该攻击涉及将前沿模型的轨迹重放到较弱的兄弟模型中以绕过安全控制，而像 Opus 4.8 这样的提供商可能会无意中暴露推理步骤。

hackernews · quantumgarbage · 8月11日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=49257876)

**背景**: 推理轨迹是 LLM 输出中的显式步骤，揭示了其内部思维过程。模型重放攻击是一种网络攻击类型，涉及重复有效的数据传输以欺骗系统。LLM API 是允许开发人员以编程方式与语言模型交互的接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Replay_attack">Replay attack - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2606.00642v1">Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs</a></li>
<li><a href="https://m0b.fun/academies/port-swigger/ll-ms/2-exploiting-vulnerabilities-in-llm-ap-is/">2 - Exploiting vulnerabilities in LLM APIs</a></li>

</ul>
</details>

**社区讨论**: 社区评论争论窃取轨迹的伦理问题，一些人认为既然轨迹已经付费，这不过是商业常态。其他人指出跨模型的重放攻击是一个已知概念，并建议禁用推理功能等更简单的变通方法。

**标签**: `#AI`, `#LLM`, `#Security`, `#Model Extraction`, `#API Vulnerabilities`

---

<a id="item-7"></a>
## [伦敦地铁扩大实时面部识别试验](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 9.0/10

英国运输警察局（BTP）已将其实时面部识别（LFR）技术的试验扩展到伦敦地铁的多个车站，部署摄像头扫描乘客的面部。 这一扩展引发了关于隐私和公民自由的重大担忧，因为它代表了监控技术在公共场所部署的重要一步。 该试验旨在了解如何在有严格保障措施的情况下，以有针对性、成比例的方式使用 LFR，尽管隐私团体认为它将公众视为嫌疑人。

hackernews · BlueBerry2001 · 8月11日 17:40 · [社区讨论](https://news.ycombinator.com/item?id=49255496)

**背景**: 面部识别技术（如 DeepFace）使用深度学习来识别个人，但已面临隐私担忧。不受监管的使用可能会侵犯公民自由，从而引发关于透明度和同意的辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c07r0gvgjxyo">Facial recognition cameras to be trialled at London Tube stations</a></li>
<li><a href="https://www.techradar.com/tech/london-underground-is-trialing-live-face-scanning-from-today-as-privacy-groups-say-it-treats-the-public-like-suspects-heres-how-to-avoid-it">London Underground is trialing live face scanning from... | TechRadar</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepFace">DeepFace - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论反映了怀疑和愤怒的混合情绪，一些人认为由于现有的非接触式支付系统，该试验是一个毫无意义的观点，而另一些人则批评它是奥威尔式的入侵。

**标签**: `#privacy`, `#surveillance`, `#facial-recognition`, `#civil-liberties`, `#security`

---

<a id="item-8"></a>
## [通过 Virtualization.framework 在 macOS 虚拟机中实现 llama.cpp 11.08 倍加速](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐️ 9.0/10

一篇技术博客文章通过修正 Apple Virtualization.framework 内部的内核选择问题，展示了在 macOS 虚拟机中 llama.cpp 推理的 11.08 倍加速，使令牌生成速度提高了 16.36 倍。 这一优化对于在 Apple Silicon 硬件上运行大型语言模型的开发者和研究人员具有重要意义，因为它展示了在 macOS 虚拟化生态系统中最大化性能的实用方法。 性能提升是通过修复一个错误实现的，即 Virtualization.framework 导致 llama.cpp 选择了错误的 Metal 内核，这仅适用于虚拟机，并不适用于原生 Apple Silicon 执行。

hackernews · frabonacci · 8月11日 22:50 · [社区讨论](https://news.ycombinator.com/item?id=49259339)

**背景**: Apple 的 Virtualization.framework 允许用户在 Apple Silicon 上运行 macOS 虚拟机，Metal 是用于利用 GPU 的图形和计算 API。llama.cpp 是一个流行的、高性能的用于运行大型语言模型的 C++ 库。

**社区讨论**: 社区成员澄清，加速仅适用于 Virtualization.framework 虚拟机，并非 Apple Silicon 上 llama.cpp 的通用改进，一些用户最初认为标题具有误导性。

**标签**: `#Apple Silicon`, `#llama.cpp`, `#Virtualization.framework`, `#Metal`, `#LLM Inference`

---

<a id="item-9"></a>
## [深入探究：通过 MitM 代理拦截 GitHub Copilot 流量](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) ⭐️ 9.0/10

作者使用中间人（MitM）代理拦截了 GitHub Copilot 的网络流量，以实时分析模型路由、上下文注入和遥测实践。 这项分析揭示了 AI 编码工具如何收集和使用数据，强调了安全影响以及了解开发者工具中遥测实践的重要性。 实验表明，Copilot 会将请求动态路由到不同的模型，从最近的编辑和其他文件中注入上下文，并在没有明确用户同意的情况下收集大量遥测数据。

hackernews · j0selit0 · 8月11日 18:40 · [社区讨论](https://news.ycombinator.com/item?id=49256057)

**背景**: MitM 代理充当中间人，可以通过将自己呈现为受信任的证书颁发机构来拦截、检查和修改加密的网络流量，从而允许代理解密和分析 HTTPS 连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mitmproxy.org/">mitmproxy - an interactive HTTPS proxy</a></li>
<li><a href="https://www.datadoghq.com/blog/ebpf-guide/">Learn how to use eBPF to create an HTTP protocol tracer .</a></li>

</ul>
</details>

**社区讨论**: 用户讨论了使用 eBPF 进行网络跟踪的好处，指出 Codex 客户端是开源的，并辩论了精心策划的上下文与通用 LLM 性能的重要性。

**标签**: `#GitHub Copilot`, `#AI tools`, `#network security`, `#telemetry`, `#eBPF`

---

<a id="item-10"></a>
## [手动设置权重实现 Transformer 精确算术运算](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 9.0/10

研究人员手动设置 Transformer 权重以执行精确算术运算，无需训练，在乘法运算中达到 100%的准确率，使用了 Torchwright 编译器。 这表明如果精心选择权重，Transformer 可以执行精确算术运算，挑战了它们天生不擅长算术的观点。 三位数计算器正确支持 300 万个表达式，检查点支持高达 12 位 x12 位的乘法，包含四个版本（小学算法、硬件风格、草稿板、暴力记忆）。

reddit · r/MachineLearning · /u/notforrob · 8月11日 01:37

**背景**: Transformer 是使用注意力机制处理序列的深度学习模型，其权重是存储在矩阵中的学习数值参数，定义了转换操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_%28deep_learning%29">Transformer (deep learning) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#transformers`, `#arithmetic`, `#weights`, `#Torchwright`, `#compiler`

---

<a id="item-11"></a>
## [苹果被曝正测试长鑫存储芯片 用于在中国市场销售的设备 - cls.cn](https://news.google.com/rss/articles/CBMiSEFVX3lxTFBnQ1NNZnVfTlhNSkViTnhIcjhfY0w2TkZXZEhXVjV2dzN5VFpTRC1HclFfYm5rMV9NOG5mdXo0emQ0NjMxVDdsTA?oc=5) ⭐️ 9.0/10

Apple is reportedly testing CXMT memory chips for devices sold in China.

google\_news · cls.cn · 8月11日 08:21

**标签**: `#semiconductors`, `#memory`, `#Apple`, `#CXMT`, `#hardware`

---

<a id="item-12"></a>
## [长鑫存储 DDR5 良率提升，PC 大厂采购策略差异大](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9xR0dUaDZDUDBlTDJ6MHpFeE1NbHNBLXZwRy1oa1lrR2RYZGdiSXRyZEFQcVZDMllGTk9YSnowTjhrZjdqNkxYRllqVnNoUFp1UnQ4?oc=5) ⭐️ 9.0/10

中国存储器制造商长鑫存储（CXMT）已将 17nm DDR5 芯片的良率显著提升至约 90%，从而实现了大规模出货，同时主要 PC 制造商正采取多样化的采购策略。 DDR5 制造方面的这一进展对全球 DRAM 市场至关重要，因为它降低了生产成本并使价格更具竞争力，同时 PC 制造商之间不同的采购策略反映了行业对供应链波动的应对。 长鑫存储的 DDR5 良率已从初始量产时的 50%提升至 80-90%，部分产品已达到 8600 MT/s 的传输速度，但文章未具体说明哪些 PC 制造商参与了采购策略的讨论。

google\_news · 电子工程专辑 · 8月11日 09:45

**背景**: DDR5 是最新一代的 DRAM 技术，相比前几代提供了更高的速度和容量，而良率是半导体制造中的关键指标，因为它直接影响生产成本和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/cxmt-hits-90-yield-on-17nm-ddr5-chips-closing-the-gap-with-micron-others-report/">CXMT Hits 90% Yield on 17nm DDR5 Chips, Closing the Gap With Micron &amp; Others - Report</a></li>
<li><a href="https://www.exportsemi.com/company-post/cxmt-achieves-80-percent-ddr5-yield/">CXMT Achieves 80 Percent DDR5 Yield</a></li>
<li><a href="https://en.sedaily.com/finance/2026/08/08/chinese-chipmaker-cxmt-closes-in-on-korea-hits-top-speed-on">Chinese Chipmaker CXMT Closes In on Korea, Hits Top Speed on US Platforms - Seoul Economic Daily</a></li>

</ul>
</details>

**标签**: `#DDR5`, `#semiconductor`, `#memory`, `#PC procurement`, `#manufacturing`

---