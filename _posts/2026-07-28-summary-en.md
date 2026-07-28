---
layout: default
title: "Horizon Summary: 2026-07-28 (EN)"
date: 2026-07-28
lang: en
---

> From 42 items, 11 important content pieces were selected

---

1. [llama.cpp b10155 adds MiMo-V2.5 audio input support](#item-1) ⭐️ 10.0/10
2. [llama.cpp Release b10154 Adds Device Detection and Cross-Platform Binaries](#item-2) ⭐️ 10.0/10
3. [llama.cpp Release b10151 Adds SYCL and Cross-Platform Support](#item-3) ⭐️ 10.0/10
4. [llama.cpp b10150 adds weight backend offloading and cross-platform binaries](#item-4) ⭐️ 10.0/10
5. [llama.cpp b10149 release: bug fix and cross-platform binaries](#item-5) ⭐️ 10.0/10
6. [Moonshot AI Releases Kimi K3: World&\#x27;s First Open-Source 2.8T Parameter Model](#item-6) ⭐️ 10.0/10
7. [llama.cpp Release b10152 Optimizes GPU Layer Distribution for MTP Blocks](#item-7) ⭐️ 9.0/10
8. [Benchmarking Opus 5 on SlopCodeBench](#item-8) ⭐️ 9.0/10
9. [Cloudflare Open-Sources Privacy Proxy CLI Tool](#item-9) ⭐️ 9.0/10
10. [Practical GitHub Copilot workflow for software development](#item-10) ⭐️ 9.0/10
11. [Fast2 Remote Code Execution Vulnerability \(RCE\) Reported](#item-11) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10155 adds MiMo-V2.5 audio input support](https://github.com/ggml-org/llama.cpp/releases/tag/b10155) ⭐️ 10.0/10

llama.cpp release b10155 introduces support for MiMo-V2.5 audio input, a model based on Residual Vector Quantization \(RVQ\), along with a GGUF converter for MiMo audio. This release significantly expands the capabilities of the llama.cpp inference engine by integrating a novel audio model, enabling developers to process multimodal inputs more efficiently across diverse platforms. The release includes pre-built binaries for macOS, Linux, Android, and Windows, supporting various hardware backends like CUDA, Vulkan, and ROCm, while the KleidiAI implementation for macOS Apple Silicon is currently disabled.

github · github-actions\[bot\] · Jul 27, 21:59

**Background**: MiMo-V2.5 is a multimodal model developed by Xiaomi that supports text, image, video, and audio inputs, and it is available on platforms like DeepInfra with an OpenAI-compatible API. Residual Vector Quantization \(RVQ\) is a technique used in generative models to improve data fidelity by increasing the number of quantization steps.

<details><summary>References</summary>
<ul>
<li><a href="https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition">Speech Recognition（MiMo-V2.5-ASR） - Xiaomi</a></li>
<li><a href="https://deepinfra.com/blog/mimo-v2-5-on-deepinfra">MiMo-V2.5 Is Now Available on DeepInfra</a></li>
<li><a href="https://arxiv.org/abs/2412.10208">[2412.10208] Efficient Generative Modeling with Residual Vector Quantization-Based Tokens</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#Audio`, `#OpenSource`, `#Inference`

---

<a id="item-2"></a>
## [llama.cpp Release b10154 Adds Device Detection and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10154) ⭐️ 10.0/10

The llama.cpp project released version b10154, introducing a new common\_print\_available\_devices\(\) function for device detection and providing pre-built binaries for macOS, Linux, Android, and Windows across various architectures and hardware backends. This release significantly enhances the usability and portability of llama.cpp, a de facto standard for local LLM inference, by making it easier for users to detect available hardware and run models on diverse platforms without needing to compile from source. The release includes binaries for Apple Silicon \(arm64\), Intel \(x64\), and various Linux distributions, with support for multiple acceleration backends such as CUDA, Vulkan, OpenVINO, and SYCL, while the KleidiAI integration for Apple Silicon is currently disabled.

github · github-actions\[bot\] · Jul 27, 16:59

**Background**: llama.cpp is a high-performance C/C++ inference engine for running Llama and compatible models in the GGUF format, widely used as the core of local LLM tools like Ollama and LM Studio. It optimizes inference across different hardware, including Apple Silicon and GPUs, to enable efficient local AI processing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/ kleidiai : This repository is a read-only mirror of...</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#Inference`, `#Cross-platform`, `#Apple-Silicon`

---

<a id="item-3"></a>
## [llama.cpp Release b10151 Adds SYCL and Cross-Platform Support](https://github.com/ggml-org/llama.cpp/releases/tag/b10151) ⭐️ 10.0/10

The llama.cpp project released version b10151, which introduces parallel SYCL build optimizations and provides cross-platform binaries for macOS, Linux, and iOS. This release significantly advances AI compute efficiency by parallelizing SYCL invocations and ensures broader accessibility through cross-platform binaries for diverse hardware architectures. The release includes binaries for macOS \(Apple Silicon and Intel\), Linux \(Ubuntu with CPU, Vulkan, ROCm, OpenVINO, and SYCL support\), iOS \(XCFramework\), Android, and Windows \(CPU, OpenCL, CUDA, Vulkan, OpenVINO, SYCL, and HIP\).

github · github-actions\[bot\] · Jul 27, 13:24

**Background**: SYCL is a royalty-free, cross-platform abstraction layer that enables single-source development for heterogeneous processors using standard C++. It allows developers to write code that runs on CPUs, GPUs, and FPGAs with a unified programming model.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SYCL">SYCL - Wikipedia</a></li>
<li><a href="https://www.khronos.org/sycl/">SYCL - C++ Single-source Heterogeneous Programming for ...</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#open-source`, `#AI`, `#local-LLM`, `#cross-platform`

---

<a id="item-4"></a>
## [llama.cpp b10150 adds weight backend offloading and cross-platform binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10150) ⭐️ 10.0/10

The llama.cpp project released version b10150, introducing weight backend offloading logic and fixes for DSV4 graphs, along with pre-built binaries for macOS, Linux, iOS, Windows, and Android. This release significantly improves the efficiency and portability of running large language models on diverse hardware, making it easier for developers to deploy AI inference across different operating systems and device architectures. The update includes a new logic for offloading operations to the weight&\#x27;s backend and specific fixes for DSV4 graphs, while macOS Apple Silicon binaries with KleidiAI are currently disabled due to a related pull request.

github · github-actions\[bot\] · Jul 27, 12:45

**Background**: llama.cpp is a popular, high-performance C++ library for running large language models \(LLMs\) efficiently on consumer hardware. It supports various backends like CUDA, Vulkan, and ROCm to accelerate inference on GPUs and other accelerators.

**Tags**: `#llama.cpp`, `#AI inference`, `#cross-platform`, `#GPU offloading`, `#macOS`

---

<a id="item-5"></a>
## [llama.cpp b10149 release: bug fix and cross-platform binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10149) ⭐️ 10.0/10

The llama.cpp project released version b10149, which removes an unnecessary synchronization in the test-save-load-state test suite and provides pre-built binaries for multiple platforms including macOS, Linux, Android, and Windows. This release is significant for the open-source AI community as it maintains the stability and reliability of the llama.cpp inference engine, which is widely used as the core for local LLM tools like Ollama and LM Studio. The update includes a specific bug fix in the test suite and offers extensive binary support across different architectures and hardware accelerators like CUDA, Vulkan, and ROCm, while the KleidiAI integration for Apple Silicon remains disabled.

github · github-actions\[bot\] · Jul 27, 11:45

**Background**: llama.cpp is an open-source C/C++ inference engine designed to run large language models in the GGUF format, serving as a foundational component for many local AI applications and tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#open-source`, `#AI-inference`, `#cross-platform`, `#bug-fix`

---

<a id="item-6"></a>
## [Moonshot AI Releases Kimi K3: World&\#x27;s First Open-Source 2.8T Parameter Model](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 10.0/10

Moonshot AI has officially open-sourced the Kimi K3 model on HuggingFace, featuring a massive 2.8 trillion parameters and 104 billion active parameters, making it the first open 3T-level model. This release is significant as it provides a highly capable, open-source alternative to proprietary models, enabling developers to build and deploy advanced AI applications without vendor lock-in. Kimi K3 uses a novel Kimi Delta Attention \(KDA\) architecture and Attention Residuals within the Stable LatentMoE framework, activating 16 of 896 experts per token, and supports text, image, and video understanding with a 1 million token context window.

telegram · zaihuapd · Jul 27, 15:15

**Background**: Large Language Models \(LLMs\) like Kimi K3 are trained on vast datasets to understand and generate human-like text. Open-source models allow anyone to inspect, modify, and deploy them, fostering innovation and transparency in the AI ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention : Kimi Delta Attention | Jianyu Huang’s Blog</a></li>
<li><a href="https://apidog.com/blog/kimi-k3-vs-kimi-k2-7-code/">Kimi K3 vs Kimi K2.7 Code: What Actually Changed</a></li>

</ul>
</details>

**Tags**: `#open-source-llm`, `#large-language-model`, `#model-architecture`, `#huggingface`, `#moonshot-ai`

---

<a id="item-7"></a>
## [llama.cpp Release b10152 Optimizes GPU Layer Distribution for MTP Blocks](https://github.com/ggml-org/llama.cpp/releases/tag/b10152) ⭐️ 9.0/10

The llama.cpp project has released version b10152, which introduces an optimization for the distribution of Multi-Token Prediction \(MTP\) blocks across GPU layers to ensure that the front layers remain on the GPU. This optimization is significant for improving the efficiency of Large Language Model \(LLM\) inference by better utilizing GPU resources, which directly impacts performance and cost for developers and users relying on llama.cpp for AI workloads. The release includes a wide range of pre-built binaries for different platforms and hardware backends, such as CUDA, Vulkan, ROCm, and OpenVINO, but the macOS Apple Silicon build with KleidiAI support is currently disabled due to an unresolved issue.

github · github-actions\[bot\] · Jul 27, 14:13

**Background**: llama.cpp is a popular, high-performance C++ library for running Large Language Models \(LLMs\) efficiently on various hardware, including CPUs and GPUs, and it provides cross-platform binaries to simplify deployment.

**Tags**: `#llama.cpp`, `#AI`, `#GPU`, `#Inference`, `#Software`

---

<a id="item-8"></a>
## [Benchmarking Opus 5 on SlopCodeBench](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md) ⭐️ 9.0/10

A benchmark of Claude Opus 5 on SlopCodeBench shows its strong performance in coding tasks and practical improvements over previous versions. This benchmark is significant as it evaluates coding agents in a way that mirrors real-world software development, highlighting the importance of maintainability and iterative improvements. SlopCodeBench consists of 36 problems and 196 checkpoints where agents repeatedly extend their solutions, unlike prior iterative benchmarks.

hackernews · dhorthy · Jul 27, 22:37 · [Discussion](https://news.ycombinator.com/item?id=49076391)

**Background**: SlopCodeBench evaluates coding agents by simulating real-world software development through repeated requirement changes and extensions. Each problem is a sequence of checkpoints that agents must navigate.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scbench.ai/">SlopCodeBench</a></li>
<li><a href="https://arxiv.org/abs/2603.24755">[2603.24755] SlopCodeBench : Benchmarking How Coding Agents...</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Users praised the benchmark for its focus on non-functional requirements and longitudinal aspects of production code. Some expressed curiosity about raw test results and suggested experiments with feature implementation order.

**Tags**: `#AI`, `#Benchmarking`, `#Software Engineering`, `#Coding Agents`, `#Model Evaluation`

---

<a id="item-9"></a>
## [Cloudflare Open-Sources Privacy Proxy CLI Tool](https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/) ⭐️ 9.0/10

Cloudflare has open-sourced pvcli, a command-line tool that mimics curl for testing privacy protocols such as OHTTP. This tool simplifies the testing of privacy protocols, which is crucial for developers building secure and private web applications. pvcli is designed to handle complex privacy protocols like OHTTP, making it easier for developers to verify privacy implementations.

rss · Cloudflare Blog · Jul 27, 13:00

**Background**: Oblivious HTTP \(OHTTP\) is an IETF protocol that separates the sender of an HTTP request from its content using public key encryption and a proxy. This ensures privacy by decoupling who is making the request from what is being sent.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_HTTP">Oblivious HTTP - Wikipedia</a></li>
<li><a href="https://support.mozilla.org/en-US/kb/ohttp-explained">Oblivious HTTP ( OHTTP ) explained | Mozilla Support</a></li>
<li><a href="https://blog.cloudflare.com/stronger-than-a-promise-proving-oblivious-http-privacy-properties/">Stronger than a promise: proving Oblivious HTTP privacy properties</a></li>

</ul>
</details>

**Tags**: `#CLI`, `#Open Source`, `#Privacy`, `#OHTTP`, `#Cloudflare`

---

<a id="item-10"></a>
## [Practical GitHub Copilot workflow for software development](https://github.blog/ai-and-ml/github-copilot/the-harness-is-all-you-need-mostly/) ⭐️ 9.0/10

GitHub has introduced a practical workflow for using GitHub Copilot in software development, focusing on prototyping, planning, implementation, and review. This workflow helps developers streamline their AI-assisted development process, reducing the need to constantly chase new AI tools and focusing on effective implementation. The workflow covers the entire software development lifecycle, from initial prototyping to final code review, ensuring a structured approach to AI-assisted coding.

rss · GitHub Blog · Jul 27, 18:00

**Background**: GitHub Copilot is an AI-powered code completion tool that assists developers by suggesting code snippets and entire functions based on context. It integrates directly into popular code editors like VS Code, making it a widely adopted tool in modern software development. The concept of a &\#x27;harness&\#x27; in this context refers to a structured workflow or framework that maximizes the utility of AI tools without requiring developers to constantly adapt to new technologies.

**Tags**: `#GitHub Copilot`, `#Software Development`, `#AI Tools`, `#Workflow`, `#Prototyping`

---

<a id="item-11"></a>
## [Fast2 Remote Code Execution Vulnerability \(RCE\) Reported](https://mp.weixin.qq.com/s/LJaul1jNjK9pXRAkoUiMEA) ⭐️ 9.0/10

Changting Technology disclosed a critical RCE vulnerability in Fast2 on July 27, allowing attackers to bypass AutoType type checking via malicious JSON data and execute arbitrary code on versions 2.0.62 and earlier. This vulnerability is significant because Fast2 is a widely used Java JSON library, and its critical RCE flaw poses a severe risk to software infrastructure and data security across the Java ecosystem. The project maintainers confirmed the security issue but have not released a formal patch for any published versions, and the full exploit details remain undisclosed; until a fix is available, users are advised to completely disable AutoType.

telegram · zaihuapd · Jul 27, 10:31

**Background**: Fast is a popular Java library for parsing and generating JSON, and its AutoType feature allows automatic type conversion but can be exploited if not properly secured, leading to deserialization-based attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-34162">NVD - CVE-2026-34162</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#java`, `#fast2`, `#RCE`

---