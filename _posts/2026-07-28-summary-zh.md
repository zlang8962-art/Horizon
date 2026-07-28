---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 42 条内容中筛选出 11 条重要资讯。

---

1. [llama.cpp b10155 添加 MiMo-V2.5 音频输入支持](#item-1) ⭐️ 10.0/10
2. [llama.cpp 发布 b10154 版本，新增设备检测并提供跨平台二进制文件](#item-2) ⭐️ 10.0/10
3. [llama.cpp 发布 b10151 版本，新增 SYCL 优化与跨平台支持](#item-3) ⭐️ 10.0/10
4. [llama.cpp b10150 添加权重后端卸载和跨平台二进制文件](#item-4) ⭐️ 10.0/10
5. [llama.cpp b10149 发布：修复漏洞并提供跨平台二进制文件](#item-5) ⭐️ 10.0/10
6. [月之暗面发布 Kimi K3：全球首个开源 2.8 万亿参数模型](#item-6) ⭐️ 10.0/10
7. [llama.cpp 发布 b10152 版本，优化 MTP 块的 GPU 层分布](#item-7) ⭐️ 9.0/10
8. [在 SlopCodeBench 上测试 Opus 5](#item-8) ⭐️ 9.0/10
9. [Cloudflare 开源隐私代理 CLI 工具](#item-9) ⭐️ 9.0/10
10. [用于软件开发的实用 GitHub Copilot 工作流](#item-10) ⭐️ 9.0/10
11. [Fast2 曝远程代码执行漏洞（RCE），现有版本尚未修复](#item-11) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10155 添加 MiMo-V2.5 音频输入支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10155) ⭐️ 10.0/10

llama.cpp 发布 b10155 版本，引入了对基于残差向量量化（RVQ）的 MiMo-V2.5 音频输入的支持，并提供了 MiMo 音频的 GGUF 转换器。 此次发布通过集成一种新颖的音频模型，显著扩展了 llama.cpp 推理引擎的功能，使开发者能够在各种平台上更高效地处理多模态输入。 该版本提供了针对 macOS、Linux、Android 和 Windows 的预编译二进制文件，支持 CUDA、Vulkan 和 ROCm 等多种硬件后端，但 macOS Apple Silicon 的 KleidiAI 实现目前已被禁用。

github · github-actions\[bot\] · 7月27日 21:59

**背景**: MiMo-V2.5 是小米开发的一种支持文本、图像、视频和音频输入的多模态模型，可在 DeepInfra 等平台通过兼容 OpenAI 的 API 使用。残差向量量化（RVQ）是一种用于生成模型的技术，通过增加量化步骤的深度来提高数据保真度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition">Speech Recognition（MiMo-V2.5-ASR） - Xiaomi</a></li>
<li><a href="https://deepinfra.com/blog/mimo-v2-5-on-deepinfra">MiMo-V2.5 Is Now Available on DeepInfra</a></li>
<li><a href="https://arxiv.org/abs/2412.10208">[2412.10208] Efficient Generative Modeling with Residual Vector Quantization-Based Tokens</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#Audio`, `#OpenSource`, `#Inference`

---

<a id="item-2"></a>
## [llama.cpp 发布 b10154 版本，新增设备检测并提供跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10154) ⭐️ 10.0/10

llama.cpp 项目发布了 b10154 版本，引入了新的 common\_print\_available\_devices\(\) 函数用于设备检测，并为 macOS、Linux、Android 和 Windows 提供了针对不同架构和硬件后端的预编译二进制文件。 此次发布通过简化硬件检测流程并提供跨平台预编译版本，显著提升了 llama.cpp 的易用性和可移植性，使其作为本地 LLM 推理事实标准的地位更加稳固。 该版本提供了针对 Apple Silicon \(arm64\)、Intel \(x64\) 和多种 Linux 发行版的二进制文件，支持 CUDA、Vulkan、OpenVINO 和 SYCL 等多种加速后端，但 Apple Silicon 的 KleidiAI 集成目前处于禁用状态。

github · github-actions\[bot\] · 7月27日 16:59

**背景**: llama.cpp 是一个高性能的 C/C++ 推理引擎，用于在 GGUF 格式下运行 Llama 及兼容模型，被广泛用作 Ollama 和 LM Studio 等本地 LLM 工具的核心。它针对包括 Apple Silicon 和 GPU 在内的不同硬件进行了优化，以实现高效的本地 AI 处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/ kleidiai : This repository is a read-only mirror of...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#Inference`, `#Cross-platform`, `#Apple-Silicon`

---

<a id="item-3"></a>
## [llama.cpp 发布 b10151 版本，新增 SYCL 优化与跨平台支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10151) ⭐️ 10.0/10

llama.cpp 项目发布了 b10151 版本，该版本引入了并行 SYCL 构建优化，并为 macOS、Linux 和 iOS 提供了跨平台二进制文件。 该版本通过并行化 SYCL 调用显著提高了 AI 计算效率，并通过为多种硬件架构提供跨平台二进制文件确保了更广泛的可访问性。 该版本提供了 macOS（Apple Silicon 和 Intel）、Linux（Ubuntu 支持 CPU、Vulkan、ROCm、OpenVINO 和 SYCL）、iOS（XCFramework）、Android 和 Windows（CPU、OpenCL、CUDA、Vulkan、OpenVINO、SYCL 和 HIP）的二进制文件。

github · github-actions\[bot\] · 7月27日 13:24

**背景**: SYCL 是一个免版税的跨平台抽象层，它使用标准 C++ 启用异构处理器的单源开发。它允许开发人员使用统一的编程模型编写在 CPU、GPU 和 FPGA 上运行的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SYCL">SYCL - Wikipedia</a></li>
<li><a href="https://www.khronos.org/sycl/">SYCL - C++ Single-source Heterogeneous Programming for ...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#open-source`, `#AI`, `#local-LLM`, `#cross-platform`

---

<a id="item-4"></a>
## [llama.cpp b10150 添加权重后端卸载和跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10150) ⭐️ 10.0/10

llama.cpp 项目发布了 b10150 版本，引入了权重后端卸载逻辑和 DSV4 图修复，并提供了适用于 macOS、Linux、iOS、Windows 和 Android 的预编译二进制文件。 此次发布显著提高了在不同硬件上运行大型语言模型的效率和可移植性，使开发者更容易在多种操作系统和设备架构上部署 AI 推理。 此次更新包括将操作卸载到权重后端的新逻辑以及对 DSV4 图的具体修复，同时由于相关拉取请求，目前禁用了带有 KleidiAI 的 macOS Apple Silicon 二进制文件。

github · github-actions\[bot\] · 7月27日 12:45

**背景**: llama.cpp 是一个流行的、高性能的 C++ 库，用于在消费级硬件上高效运行大型语言模型（LLM）。它支持各种后端，如 CUDA、Vulkan 和 ROCm，以在 GPU 和其他加速器上加速推理。

**标签**: `#llama.cpp`, `#AI inference`, `#cross-platform`, `#GPU offloading`, `#macOS`

---

<a id="item-5"></a>
## [llama.cpp b10149 发布：修复漏洞并提供跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10149) ⭐️ 10.0/10

llama.cpp 项目发布了 b10149 版本，该版本移除了 test-save-load-state 测试套件中不必要的同步操作，并为 macOS、Linux、Android 和 Windows 等多个平台提供了预编译的二进制文件。 此次发布对开源 AI 社区具有重要意义，因为它维护了 llama.cpp 推理引擎的稳定性和可靠性，该引擎被广泛用作 Ollama 和 LM Studio 等本地 LLM 工具的核心。 此次更新包括测试套件中的特定漏洞修复，并在不同架构和硬件加速器（如 CUDA、Vulkan 和 ROCm）上提供了广泛的二进制支持，同时针对 Apple Silicon 的 KleidiAI 集成仍处于禁用状态。

github · github-actions\[bot\] · 7月27日 11:45

**背景**: llama.cpp 是一个开源的 C/C++ 推理引擎，旨在运行 GGUF 格式的大型语言模型，是许多本地 AI 应用和工具的基础组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#open-source`, `#AI-inference`, `#cross-platform`, `#bug-fix`

---

<a id="item-6"></a>
## [月之暗面发布 Kimi K3：全球首个开源 2.8 万亿参数模型](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 10.0/10

月之暗面在 HuggingFace 上正式开源了 Kimi K3 模型，总参数量达到 2.8 万亿，激活参数 104B，是全球首个开放的 3T 级别模型。 这一发布意义重大，因为它提供了一个强大的开源替代方案，使开发者能够在不依赖厂商的情况下构建和部署先进的 AI 应用。 Kimi K3 采用 Kimi Delta Attention（KDA）与 Attention Residuals（AttnRes）新架构，基于 Stable LatentMoE 框架，896 个专家中每 token 激活 16 个，并原生支持文本、图像与视频理解，上下文窗口达 100 万 token。

telegram · zaihuapd · 7月27日 15:15

**背景**: 大型语言模型（LLM）如 Kimi K3 是在庞大的数据集上训练的，旨在理解和生成类人文本。开源模型允许任何人检查、修改和部署它们，从而推动 AI 生态系统的创新和透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention : Kimi Delta Attention | Jianyu Huang’s Blog</a></li>
<li><a href="https://apidog.com/blog/kimi-k3-vs-kimi-k2-7-code/">Kimi K3 vs Kimi K2.7 Code: What Actually Changed</a></li>

</ul>
</details>

**标签**: `#open-source-llm`, `#large-language-model`, `#model-architecture`, `#huggingface`, `#moonshot-ai`

---

<a id="item-7"></a>
## [llama.cpp 发布 b10152 版本，优化 MTP 块的 GPU 层分布](https://github.com/ggml-org/llama.cpp/releases/tag/b10152) ⭐️ 9.0/10

llama.cpp 项目发布了 b10152 版本，该版本引入了对多 token 预测（MTP）块在 GPU 层间分布的优化，以确保前几层保持在 GPU 上。 这一优化对于提高大语言模型（LLM）推理效率具有重要意义，通过更好地利用 GPU 资源，直接影响了依赖 llama.cpp 处理 AI 工作负载的开发人员和用户的性能和成本。 该版本提供了针对不同平台和硬件后端（如 CUDA、Vulkan、ROCm 和 OpenVINO）的广泛预构建二进制文件，但由于未解决的问题，目前禁用了支持 KleidiAI 的 macOS Apple Silicon 构建版本。

github · github-actions\[bot\] · 7月27日 14:13

**背景**: llama.cpp 是一个流行的、高性能的 C++ 库，用于在各种硬件（包括 CPU 和 GPU）上高效运行大语言模型（LLM），并提供跨平台二进制文件以简化部署。

**标签**: `#llama.cpp`, `#AI`, `#GPU`, `#Inference`, `#Software`

---

<a id="item-8"></a>
## [在 SlopCodeBench 上测试 Opus 5](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md) ⭐️ 9.0/10

在 SlopCodeBench 上对 Claude Opus 5 进行基准测试，显示其在编码任务中的强大表现以及对先前版本的实用改进。 这一基准测试具有重要意义，因为它以模拟现实软件开发的方式评估编码代理，突出了可维护性和迭代改进的重要性。 SlopCodeBench 包含 36 个问题和 196 个检查点，其中代理会重复扩展其解决方案，这与先前的迭代基准测试不同。

hackernews · dhorthy · 7月27日 22:37 · [社区讨论](https://news.ycombinator.com/item?id=49076391)

**背景**: SlopCodeBench 通过重复的需求变更和扩展来模拟现实世界的软件开发，从而评估编码代理。每个问题都是一个检查点序列，代理必须依次通过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scbench.ai/">SlopCodeBench</a></li>
<li><a href="https://arxiv.org/abs/2603.24755">[2603.24755] SlopCodeBench : Benchmarking How Coding Agents...</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 用户称赞该基准测试关注生产代码的非功能性需求和纵向方面。一些人表达了对原始测试结果的好奇，并建议进行功能实现顺序的实验。

**标签**: `#AI`, `#Benchmarking`, `#Software Engineering`, `#Coding Agents`, `#Model Evaluation`

---

<a id="item-9"></a>
## [Cloudflare 开源隐私代理 CLI 工具](https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/) ⭐️ 9.0/10

Cloudflare 开源了 pvcli，这是一个模仿 curl 的命令行工具，用于测试隐私协议，如 OHTTP。 该工具简化了隐私协议的测试，这对构建安全、私密的 Web 应用程序的开发者至关重要。 pvcli 旨在处理复杂的隐私协议，如 OHTTP，使开发者更容易验证隐私实现。

rss · Cloudflare Blog · 7月27日 13:00

**背景**: Oblivious HTTP \(OHTTP\) 是一种 IETF 协议，它使用公钥加密和代理将 HTTP 请求的发送者与其内容分离。这通过解耦谁在发起请求以及发送了什么内容，确保了隐私性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_HTTP">Oblivious HTTP - Wikipedia</a></li>
<li><a href="https://support.mozilla.org/en-US/kb/ohttp-explained">Oblivious HTTP ( OHTTP ) explained | Mozilla Support</a></li>
<li><a href="https://blog.cloudflare.com/stronger-than-a-promise-proving-oblivious-http-privacy-properties/">Stronger than a promise: proving Oblivious HTTP privacy properties</a></li>

</ul>
</details>

**标签**: `#CLI`, `#Open Source`, `#Privacy`, `#OHTTP`, `#Cloudflare`

---

<a id="item-10"></a>
## [用于软件开发的实用 GitHub Copilot 工作流](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/) ⭐️ 9.0/10

GitHub 介绍了一种在软件开发中使用 GitHub Copilot 的实用工作流，重点在于原型设计、规划、实施和审查。 该工作流帮助开发人员简化 AI 辅助开发流程，减少不断追逐新 AI 工具的需求，并专注于有效的实施。 该工作流涵盖了整个软件开发生命周期，从初步原型设计到最终代码审查，确保了对 AI 辅助编码的结构化方法。

rss · GitHub Blog · 7月27日 18:00

**背景**: GitHub Copilot 是一种基于上下文建议代码片段和整个函数的 AI 驱动代码补全工具，可协助开发人员。它直接集成到 VS Code 等流行代码编辑器中，使其成为现代软件开发中广泛采用的工具。在此背景下，“Harness”一词指的是一种结构化工作流或框架，可在无需开发人员不断适应新技术的情况下，最大化 AI 工具的效用。

**标签**: `#GitHub Copilot`, `#Software Development`, `#AI Tools`, `#Workflow`, `#Prototyping`

---

<a id="item-11"></a>
## [Fast2 曝远程代码执行漏洞（RCE），现有版本尚未修复](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 9.0/10

长亭科技于 7 月 27 日披露 Fast2 存在严重远程代码执行漏洞，攻击者可通过恶意 JSON 数据绕过 AutoType 类型校验并执行任意代码，影响 2.0.62 及以前版本。 该漏洞意义重大，因为 Fast2 是广泛使用的 Java JSON 库，其严重远程代码执行缺陷对软件基础设施和数据安全构成了重大风险。 项目维护者已确认安全问题，但尚未为任何已发布版本发布正式补丁，完整利用细节尚未公开；在修复版本推出前，建议彻底禁用 AutoType。

telegram · zaihuapd · 7月27日 10:31

**背景**: Fast 是一个流行的 Java JSON 解析和生成库，其 AutoType 功能允许自动类型转换，但如果未正确保护，可能会被利用导致基于反序列化的攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-34162">NVD - CVE-2026-34162</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#java`, `#fast2`, `#RCE`

---