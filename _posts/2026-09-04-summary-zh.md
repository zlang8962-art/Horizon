---
layout: default
title: "Horizon Summary: 2026-09-04 (ZH)"
date: 2026-09-04
content_date: 2026-09-03
lang: zh
---

> 报道范围：2026-09-03（Asia/Shanghai 自然日）

> 从 95 条内容中筛选出 12 条重要资讯。

---

1. [pytorch/pytorch 发布了 v2.14.0 版本](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp 发布了 b10785 版本](#item-2) ⭐️ 10.0/10
3. [llama.cpp v10784 发布：Metal 修复与跨平台二进制文件](#item-3) ⭐️ 10.0/10
4. [介绍 Gemini 3.8 Flash 和 3.8 Flash Cyber](#item-4) ⭐️ 10.0/10
5. [微软 10 月默认启用 Win11 内存完整性保护](#item-5) ⭐️ 10.0/10
6. [Microsoft ONNX Runtime v1.28.2 补丁版本](#item-6) ⭐️ 9.0/10
7. [使用 LLM 将 1993 年的 Amiga 游戏移植到 Godot](#item-7) ⭐️ 9.0/10
8. [K2 Horizon: A connected fleet of six open models](#item-8) ⭐️ 9.0/10
9. [Audacity 4.0 发布，包含 Qt6 界面和 JACK 支持](#item-9) ⭐️ 9.0/10
10. [llm-gemini 0.34 添加对 Gemini 3.8 Flash 的支持](#item-10) ⭐️ 9.0/10
11. [Kubernetes v1.37：使用 HorizontalPodAutoscaler 将工作负载扩展为零](#item-11) ⭐️ 9.0/10
12. [CSEAC 2026 现场直击：国产半导体设备从“能用”到“好用”](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [pytorch/pytorch 发布了 v2.14.0 版本](https://github.com/pytorch/pytorch/releases/tag/v2.14.0) ⭐️ 10.0/10

PyTorch 2.14.0 引入了 NVGEMM 集成、动态形状以及性能改进。

github · ethche · 9月3日 01:40

**标签**: `#pytorch`, `#ai-compute`, `#software-release`, `#cuda`, `#performance`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp 发布了 b10785 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b10785) ⭐️ 10.0/10

llama.cpp 版本 b10785 为 Metal 增加了稀疏 Flash Attention 支持。

github · github-actions\[bot\] · 9月3日 20:19

**标签**: `#llama.cpp`, `#flash-attention`, `#sparse-attention`, `#metal`, `#ai-compute`

---

<a id="item-3"></a>
## [llama.cpp v10784 发布：Metal 修复与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10784) ⭐️ 10.0/10

llama.cpp v10784 版本发布，包含 Metal 在 ne00 等于 1 时的调度修复，以及针对 macOS、Linux、Android 和 Windows 的多种架构和硬件后端的预编译二进制文件。 此次发布通过解决特定的渲染错误并确保在不同操作系统和硬件上的广泛兼容性，提高了 llama.cpp 这一流行的开源 LLM 推理引擎的可靠性和易用性。 Metal 调度修复专门解决了 ne00 等于 1 时的 glu 调度问题，并且多个构建版本被标记为禁用，例如启用了 KleidiAI 的 macOS Apple Silicon。

github · github-actions\[bot\] · 9月3日 19:52

**背景**: llama.cpp 是一个高性能的开源库，用于在各种硬件上运行大型语言模型（LLM），包括 CPU、GPU 和 Apple Metal、AMD ROCm 等专用加速器。

**标签**: `#llama.cpp`, `#AI`, `#open-source`, `#macOS`, `#Linux`

---

<a id="item-4"></a>
## [介绍 Gemini 3.8 Flash 和 3.8 Flash Cyber](https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/) ⭐️ 10.0/10

Google DeepMind 宣布发布两款新的 AI 模型，即 Gemini 3.8 Flash 和 3.8 Flash Cyber，重点在于效率和专用功能。

rss · Google DeepMind News · 9月3日 00:18

**标签**: `#AI`, `#Machine Learning`, `#Gemini`, `#DeepMind`, `#LLM`

---

<a id="item-5"></a>
## [微软 10 月默认启用 Win11 内存完整性保护](https://techcommunity.microsoft.com/blog/windows-itpro-blog/expanding-memory-integrity-protection-across-windows-devices/4551984) ⭐️ 10.0/10

微软计划从 2024 年 10 月 13 日起，对符合条件的 Windows 11 设备默认启用内存完整性保护（HVCI），以拦截恶意驱动劫持。 这一变化通过缓解内核模式驱动攻击，显著增强了系统安全性，因为恶意软件和勒索软件常利用底层驱动作为攻击向量。 该功能需要硬件虚拟化支持、UEFI 和 Secure Boot，不兼容的驱动程序可能阻止启用，或在极少数情况下导致蓝屏（BSOD）。

telegram · zaihuapd · 9月3日 14:09

**背景**: HVCI（受 hypervisor 保护的代码完整性）利用硬件虚拟化创建隔离环境，确保只有受信任的内核模式代码和驱动程序才能执行，从而降低恶意代码执行的风险。

**标签**: `#Windows 11`, `#Security`, `#HVCI`, `#Kernel Protection`, `#Driver Security`

---

<a id="item-6"></a>
## [Microsoft ONNX Runtime v1.28.2 补丁版本](https://github.com/microsoft/onnxruntime/releases/tag/v1.28.2) ⭐️ 9.0/10

Microsoft 发布了 ONNX Runtime v1.28.2，这是一个补丁版本，修复了 Compile API 中模型序列化的一个错误，具体是防止优化模型中出现重复的图节点、输入、输出和值信息。 此修复对于使用 Compile API 进行模型优化的开发者至关重要，因为它确保了序列化模型的完整性，并防止 AI 推理管道中出现潜在的运行时错误或性能下降。 该错误影响了具有嵌入式或外部初始化器的模型，并在拉取请求 \#32303 中得到了解决，确保 Compile API 回调序列化在不同执行提供程序上正常工作。

github · adrastogi · 9月3日 09:17

**背景**: ONNX Runtime 是一个跨平台、高性能的机器学习推理和训练加速器。Compile API 允许通过将子图融合为特定于提供程序的表示来进行模型优化，这对于在生产环境中部署优化模型至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onnxruntime.ai/docs/api/c/struct_ort_compile_api.html">ONNX Runtime: OrtCompileApi Struct Reference</a></li>
<li><a href="https://onnxruntime.ai/docs/performance/model-optimizations/graph-optimizations.html">Graph optimizations | onnxruntime</a></li>

</ul>
</details>

**标签**: `#onnxruntime`, `#ai-inference`, `#bug-fix`, `#model-serialization`, `#patch-release`

---

<a id="item-7"></a>
## [使用 LLM 将 1993 年的 Amiga 游戏移植到 Godot](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 9.0/10

一位开发者在 7 月使用 Claude Fable 5 成功将一款 1993 年的 Amiga 游戏从 MC68000 汇编语言移植到 Godot，使用 vasm 汇编器实现了与原始游戏二进制文件字节一致的输出。 这一成就展示了 AI 分析和翻译遗留汇编代码的潜力，为复古软件的保存和现代化提供了一种新方法。 移植过程涉及使用 Claude Fable 5 通过 vasm 汇编代码，由于原始游戏的基于快照的保存机制，导致出现了 108 字节的差异。

hackernews · rabahs · 9月3日 22:28 · [社区讨论](https://news.ycombinator.com/item?id=49550375)

**背景**: MC68000 是一种在 Amiga 计算机上使用的 32 位 CISC 微处理器架构，汇编语言编程在 20 世纪 90 年代初的游戏开发中很常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikibooks.org/wiki/68000_Assembly">68000 Assembly - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**社区讨论**: 社区成员对开发者在 1993 年使用汇编语言创建游戏的奉献精神表示钦佩，并分享了他们自己使用 AI 辅助代码转换的经验。

**标签**: `#AI`, `#Software Engineering`, `#Legacy Code`, `#Game Development`, `#Assembly`

---

<a id="item-8"></a>
## [K2 Horizon: A connected fleet of six open models](https://ifm.ai/blog/k2/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · karimf · 9月3日 23:36 · [社区讨论](https://news.ycombinator.com/item?id=49551760)

**标签**: `#open-source-ai`, `#model-performance`, `#ai-ecosystem`, `#developer-tools`, `#safety`

---

<a id="item-9"></a>
## [Audacity 4.0 发布，包含 Qt6 界面和 JACK 支持](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0) ⭐️ 9.0/10

Audacity 4.0 发布，包含新的基于 Qt6 的用户界面和改进的 JACK 客户端支持，解决了长期存在的用户问题。 此次发布对开源音频编辑工具具有重要意义，因为它现代化了 UI 框架并改进了音频路由功能，使开发者和用户都受益。 此次更新包括完全迁移到 Qt6，这提供了更好的 GPU 集成和高分辨率显示支持，以及持久的 JACK 客户端功能。

hackernews · ClydeN · 9月3日 18:53 · [社区讨论](https://news.ycombinator.com/item?id=49548395)

**背景**: JACK 音频连接套件是一个专业音频服务器 API，可为应用程序之间的音频和 MIDI 数据提供实时、低延迟的连接。与前一版本 Qt5 相比，Qt6 是一个现代化的 C++ GUI 框架，提供更好的性能和跨平台兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jackaudio.org/">Home | JACK Audio Connection Kit</a></li>
<li><a href="https://softwarelogic.co/en/blog/10-reasons-why-migrating-from-qt5-to-qt6-is-worth-it">10 Reasons to Migrate from Qt5 to Qt6 for Desktop Apps</a></li>

</ul>
</details>

**社区讨论**: 用户表达了不同的看法：有些人称赞技术改进和干净的测试版体验，而另一些人则批评持久的 JACK 客户端问题以及未更新家庭工作室工作流程。

**标签**: `#open-source`, `#software-development`, `#audio-editing`, `#Qt6`, `#developer-tools`

---

<a id="item-10"></a>
## [llm-gemini 0.34 添加对 Gemini 3.8 Flash 的支持](https://simonwillison.net/2026/Sep/2/llm-gemini/) ⭐️ 9.0/10

llm-gemini 0.34 版本引入了对新的 Gemini 3.8 Flash 模型的支持，并修复了异步响应无法记录已解析模型版本的 bug。 此次更新对使用 llm-gemini 库的开发者具有重要意义，因为它提供了对最新的 Gemini 3.8 Flash 模型的访问权限，该模型在软件工程和代理知识工作流程中提供了性能提升。 Gemini 3.8 Flash 支持可自定义的努力级别，以控制质量、成本和延迟的混合，该库现在正确处理异步响应以确保准确的模型版本跟踪。

rss · Simon Willison · 9月3日 00:39

**背景**: llm-gemini 是一个 Python 库，为 &\#x27;llm&\#x27; 项目提供了一个插件，用于访问 Google 的 Gemini 模型，使开发人员能够在其应用程序中集成生成式 AI 功能。Gemini 3.8 Flash 是 Gemini 3 模型系列的最新迭代，建立在之前的 3.7 Flash 模型之上，并进行了性能改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber - The Keyword</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#Python`, `#LLM`, `#Release`

---

<a id="item-11"></a>
## [Kubernetes v1.37：使用 HorizontalPodAutoscaler 将工作负载扩展为零](https://kubernetes.io/blog/2026/09/02/kubernetes-v1-37-hpa-scale-to-zero-beta/) ⭐️ 9.0/10

Kubernetes v1.37 引入了一个 beta 功能，允许使用 HorizontalPodAutoscaler 将工作负载扩展为零副本，以优化资源使用，但代价是冷启动时间。

rss · Kubernetes Blog · 9月3日 02:30

**标签**: `#kubernetes`, `#autoscaling`, `#resource-optimization`, `#devops`, `#cloud-native`

---

<a id="item-12"></a>
## [CSEAC 2026 现场直击：国产半导体设备从“能用”到“好用”](https://news.google.com/rss/articles/CBMijAFBVV95cUxOYmNYM1ZtcXYwbnpQTmVyenlkQ2tFTWR0bEVTdlRxTmJONDNwRlQ5RXQ1bGNCYUw0eHRMcVprNTd1SEs4ZDlDN210bGVWOG9famU4SzBTN0ROdG9pQ3Yxb2luTWVLN0pGdl8zRzNIdWdWSUhkTWZyc1RSX1NwY0luazlZSHluM25LQm5mdA?oc=5) ⭐️ 9.0/10

在 CSEAC 2026 现场，国产半导体设备制造商展示了从基础功能向用户友好型设计的重要进展，标志着供应链迭代进入深水区。 这一转变对于减少对外国技术的依赖并加强国内半导体生态系统至关重要，这直接影响到 AI 基础设施和硬件工程能力。 活动强调了设备可用性和供应链整合的改进，尽管文章未提供具体的技术细节或产品名称。

google\_news · Sohu · 9月3日 19:01

**背景**: 半导体设备对于芯片制造至关重要，与 ASML 和 Applied Materials 等全球领导者相比，国内制造商在性能和可靠性方面一直面临挑战。

**标签**: `#semiconductor`, `#chips`, `#supply\_chain`, `#hardware`, `#ai\_infrastructure`

---