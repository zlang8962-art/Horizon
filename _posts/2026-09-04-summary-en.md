---
layout: default
title: "Horizon Summary: 2026-09-04 (EN)"
date: 2026-09-04
content_date: 2026-09-03
lang: en
---

> Coverage: 2026-09-03 (Asia/Shanghai calendar day)

> From 95 items, 12 important content pieces were selected

---

1. [pytorch/pytorch released v2.14.0](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10785](#item-2) ⭐️ 10.0/10
3. [llama.cpp v10784 Release: Metal Fixes and Cross-Platform Binaries](#item-3) ⭐️ 10.0/10
4. [Introducing Gemini 3.8 Flash and 3.8 Flash Cyber](#item-4) ⭐️ 10.0/10
5. [Microsoft Defaults Enable Win11 Memory Integrity Protection in October](#item-5) ⭐️ 10.0/10
6. [Microsoft ONNX Runtime v1.28.2 Patch Release](#item-6) ⭐️ 9.0/10
7. [Porting 1993 Amiga Game to Godot Using LLM](#item-7) ⭐️ 9.0/10
8. [K2 Horizon: A connected fleet of six open models](#item-8) ⭐️ 9.0/10
9. [Audacity 4.0 Released with Qt6 UI and JACK Support](#item-9) ⭐️ 9.0/10
10. [llm-gemini 0.34 Adds Support for Gemini 3.8 Flash](#item-10) ⭐️ 9.0/10
11. [Kubernetes v1.37: Scale Workloads to Zero with HorizontalPodAutoscaler](#item-11) ⭐️ 9.0/10
12. [CSEAC 2026: Domestic Semiconductor Equipment Evolving from Usable to User-Friendly](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [pytorch/pytorch released v2.14.0](https://github.com/pytorch/pytorch/releases/tag/v2.14.0) ⭐️ 10.0/10

PyTorch 2.14.0 introduces NVGEMM integration, dynamic shapes, and performance improvements.

github · ethche · Sep 3, 01:40

**Tags**: `#pytorch`, `#ai-compute`, `#software-release`, `#cuda`, `#performance`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10785](https://github.com/ggml-org/llama.cpp/releases/tag/b10785) ⭐️ 10.0/10

llama.cpp release b10785 adds sparse Flash Attention support for Metal.

github · github-actions\[bot\] · Sep 3, 20:19

**Tags**: `#llama.cpp`, `#flash-attention`, `#sparse-attention`, `#metal`, `#ai-compute`

---

<a id="item-3"></a>
## [llama.cpp v10784 Release: Metal Fixes and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10784) ⭐️ 10.0/10

The llama.cpp v10784 release includes a critical fix for Metal dispatch when ne00 equals 1, along with pre-built binaries for macOS, Linux, Android, and Windows across various architectures and hardware backends. This release improves the reliability and usability of llama.cpp, a popular open-source LLM inference engine, by addressing a specific rendering bug and ensuring broad compatibility across different operating systems and hardware. The Metal dispatch fix specifically addresses an issue with glu dispatch when ne00 equals 1, and several builds are marked as disabled, such as macOS Apple Silicon with KleidiAI enabled.

github · github-actions\[bot\] · Sep 3, 19:52

**Background**: llama.cpp is a high-performance, open-source library for running Large Language Models \(LLMs\) on a variety of hardware, including CPUs, GPUs, and specialized accelerators like Apple&\#x27;s Metal and AMD&\#x27;s ROCm.

**Tags**: `#llama.cpp`, `#AI`, `#open-source`, `#macOS`, `#Linux`

---

<a id="item-4"></a>
## [Introducing Gemini 3.8 Flash and 3.8 Flash Cyber](https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/) ⭐️ 10.0/10

Google DeepMind announces the release of two new AI models, Gemini 3.8 Flash and 3.8 Flash Cyber, focusing on efficiency and specialized capabilities.

rss · Google DeepMind News · Sep 3, 00:18

**Tags**: `#AI`, `#Machine Learning`, `#Gemini`, `#DeepMind`, `#LLM`

---

<a id="item-5"></a>
## [Microsoft Defaults Enable Win11 Memory Integrity Protection in October](https://techcommunity.microsoft.com/blog/windows-itpro-blog/expanding-memory-integrity-protection-across-windows-devices/4551984) ⭐️ 10.0/10

Microsoft will default-enable Memory Integrity Protection \(HVCI\) on eligible Windows 11 devices starting October 13, 2024, to block malicious driver hijacking. This change significantly enhances system security by mitigating kernel-mode driver attacks, which are a common vector for malware and ransomware. The feature requires hardware virtualization support, UEFI, and Secure Boot, and incompatible drivers may prevent activation or cause Blue Screen of Death \(BSOD\).

telegram · zaihuapd · Sep 3, 14:09

**Background**: HVCI \(Hypervisor-protected Code Integrity\) uses hardware virtualization to create an isolated environment, ensuring only trusted kernel-mode code and drivers can execute, thereby reducing the risk of malicious code execution.

**Tags**: `#Windows 11`, `#Security`, `#HVCI`, `#Kernel Protection`, `#Driver Security`

---

<a id="item-6"></a>
## [Microsoft ONNX Runtime v1.28.2 Patch Release](https://github.com/microsoft/onnxruntime/releases/tag/v1.28.2) ⭐️ 9.0/10

Microsoft released ONNX Runtime v1.28.2, a patch release that fixes a bug in the Compile API&\#x27;s model serialization, specifically preventing duplicate graph nodes, inputs, outputs, and value information in optimized models. This fix is crucial for developers using the Compile API for model optimization, as it ensures the integrity of serialized models and prevents potential runtime errors or performance degradation in AI inference pipelines. The bug affected models with embedded or external initializers and was addressed in pull request \#32303, ensuring that the Compile API callback serialization works correctly across different execution providers.

github · adrastogi · Sep 3, 09:17

**Background**: ONNX Runtime is a cross-platform, high-performance machine learning inference and training accelerator. The Compile API allows for model optimization by fusing subgraphs into provider-specific representations, which is essential for deploying optimized models in production environments.

<details><summary>References</summary>
<ul>
<li><a href="https://onnxruntime.ai/docs/api/c/struct_ort_compile_api.html">ONNX Runtime: OrtCompileApi Struct Reference</a></li>
<li><a href="https://onnxruntime.ai/docs/performance/model-optimizations/graph-optimizations.html">Graph optimizations | onnxruntime</a></li>

</ul>
</details>

**Tags**: `#onnxruntime`, `#ai-inference`, `#bug-fix`, `#model-serialization`, `#patch-release`

---

<a id="item-7"></a>
## [Porting 1993 Amiga Game to Godot Using LLM](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 9.0/10

A developer successfully ported a 1993 Amiga game from MC68000 assembly to Godot using Claude Fable 5 in July, achieving byte-identical binary output with vasm assembler. This achievement demonstrates the potential of AI to analyze and translate legacy assembly code, offering a new approach for preserving and modernizing retro software. The porting process involved using Claude Fable 5 to assemble code with vasm, resulting in a 108-byte mismatch due to the original game&\#x27;s snapshot-based save mechanism.

hackernews · rabahs · Sep 3, 22:28 · [Discussion](https://news.ycombinator.com/item?id=49550375)

**Background**: The MC68000 is a 32-bit CISC microprocessor architecture used in the Amiga computer, and assembly language programming was common in the early 1990s for game development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikibooks.org/wiki/68000_Assembly">68000 Assembly - Wikibooks, open books for an open world</a></li>

</ul>
</details>

**Discussion**: Community members expressed awe at the developer&\#x27;s dedication to creating the game in 1993 assembly and shared their own experiences with AI-assisted code conversion.

**Tags**: `#AI`, `#Software Engineering`, `#Legacy Code`, `#Game Development`, `#Assembly`

---

<a id="item-8"></a>
## [K2 Horizon: A connected fleet of six open models](https://ifm.ai/blog/k2/) ⭐️ 9.0/10

K2 Horizon introduces a connected fleet of six open models, sparking debate on open-source AI&\#x27;s future and performance benchmarks.

hackernews · karimf · Sep 3, 23:36 · [Discussion](https://news.ycombinator.com/item?id=49551760)

**Tags**: `#open-source-ai`, `#model-performance`, `#ai-ecosystem`, `#developer-tools`, `#safety`

---

<a id="item-9"></a>
## [Audacity 4.0 Released with Qt6 UI and JACK Support](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0) ⭐️ 9.0/10

Audacity 4.0 is released with a new Qt6-based user interface and improved JACK client support, addressing long-standing user issues. This release is significant for open-source audio editing tools as it modernizes the UI framework and improves audio routing capabilities, benefiting both developers and users. The update includes a complete migration to Qt6, which offers better GPU integration and high-resolution display support, along with persistent JACK client functionality.

hackernews · ClydeN · Sep 3, 18:53 · [Discussion](https://news.ycombinator.com/item?id=49548395)

**Background**: JACK Audio Connection Kit is a professional sound server API that provides real-time, low-latency connections for audio and MIDI data between applications. Qt6 is a modern C++ GUI framework that offers improved performance and cross-platform compatibility compared to its predecessor, Qt5.

<details><summary>References</summary>
<ul>
<li><a href="https://jackaudio.org/">Home | JACK Audio Connection Kit</a></li>
<li><a href="https://softwarelogic.co/en/blog/10-reasons-why-migrating-from-qt5-to-qt6-is-worth-it">10 Reasons to Migrate from Qt5 to Qt6 for Desktop Apps</a></li>

</ul>
</details>

**Discussion**: Users express mixed feelings: some praise the technical improvements and clean beta experience, while others criticize the persistent JACK client issue and lack of updates for home studio workflows.

**Tags**: `#open-source`, `#software-development`, `#audio-editing`, `#Qt6`, `#developer-tools`

---

<a id="item-10"></a>
## [llm-gemini 0.34 Adds Support for Gemini 3.8 Flash](https://simonwillison.net/2026/Sep/2/llm-gemini/) ⭐️ 9.0/10

The llm-gemini 0.34 release introduces support for the new Gemini 3.8 Flash model and fixes a bug where async responses failed to record the resolved model version. This update is significant for developers using the llm-gemini library as it provides access to the latest Gemini 3.8 Flash model, which offers improved performance in software engineering and agentic knowledge workflows. Gemini 3.8 Flash supports customizable effort levels to control the mix of quality, cost, and latency, and the library now correctly handles async responses to ensure accurate model version tracking.

rss · Simon Willison · Sep 3, 00:39

**Background**: llm-gemini is a Python library that provides a plugin for the &\#x27;llm&\#x27; project to access Google&\#x27;s Gemini models, allowing developers to integrate generative AI capabilities into their applications. Gemini 3.8 Flash is the latest iteration in the Gemini 3 model family, building on the previous 3.7 Flash model with performance improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber - The Keyword</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Gemini`, `#Python`, `#LLM`, `#Release`

---

<a id="item-11"></a>
## [Kubernetes v1.37: Scale Workloads to Zero with HorizontalPodAutoscaler](https://kubernetes.io/blog/2026/09/02/kubernetes-v1-37-hpa-scale-to-zero-beta/) ⭐️ 9.0/10

Kubernetes v1.37 introduces a beta feature to scale workloads to zero replicas using HorizontalPodAutoscaler, optimizing resource usage at the cost of cold-start time.

rss · Kubernetes Blog · Sep 3, 02:30

**Tags**: `#kubernetes`, `#autoscaling`, `#resource-optimization`, `#devops`, `#cloud-native`

---

<a id="item-12"></a>
## [CSEAC 2026: Domestic Semiconductor Equipment Evolving from Usable to User-Friendly](https://news.google.com/rss/articles/CBMijAFBVV95cUxOYmNYM1ZtcXYwbnpQTmVyenlkQ2tFTWR0bEVTdlRxTmJONDNwRlQ5RXQ1bGNCYUw0eHRMcVprNTd1SEs4ZDlDN210bGVWOG9famU4SzBTN0ROdG9pQ3Yxb2luTWVLN0pGdl8zRzNIdWdWSUhkTWZyc1RSX1NwY0luazlZSHluM25LQm5mdA?oc=5) ⭐️ 9.0/10

At the CSEAC 2026 event, domestic semiconductor equipment manufacturers showcased significant progress in moving from basic functionality to user-friendly designs, marking a deepening iteration in the supply chain. This shift is crucial for reducing reliance on foreign technology and strengthening the domestic semiconductor ecosystem, which directly impacts AI infrastructure and hardware engineering capabilities. The event highlighted improvements in equipment usability and supply chain integration, though specific technical details or product names were not provided in the article.

google\_news · Sohu · Sep 3, 19:01

**Background**: Semiconductor equipment is essential for manufacturing chips, and domestic manufacturers have historically struggled with performance and reliability compared to global leaders like ASML and Applied Materials.

**Tags**: `#semiconductor`, `#chips`, `#supply\_chain`, `#hardware`, `#ai\_infrastructure`

---