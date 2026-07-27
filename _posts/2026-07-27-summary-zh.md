---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 37 条内容中筛选出 10 条重要资讯。

---

1. [vLLM v0.26.0 发布：推理性能大幅优化并支持新模型](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10142 新增 MiniMax-M3 视觉支持与稀疏注意力优化](#item-2) ⭐️ 9.0/10
3. [llama.cpp b10141 发布，提供跨平台预编译二进制文件](#item-3) ⭐️ 9.0/10
4. [美国公民因 GrapheneOS 手机在边境被搜查时自动擦除数据遭起诉](#item-4) ⭐️ 9.0/10
5. [Go 团队推出 go/analysis 框架实现模块化静态分析](#item-5) ⭐️ 9.0/10
6. [调查揭示转售大模型 API 令牌的地下中继市场](#item-6) ⭐️ 9.0/10
7. [本科毕设：纯 ARM64 汇编从零实现 YOLO26n 模型推理](#item-7) ⭐️ 9.0/10
8. [开源 4B 模型在瑞典医学问答中接近 o3 水平准确率](#item-8) ⭐️ 9.0/10
9. [长鑫科技完成 A 股史上最大 IPO，有望成市值最高公司](#item-9) ⭐️ 9.0/10
10. [高通确认骁龙 8 Elite Gen 6 将迎两位数涨价](#item-10) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布：推理性能大幅优化并支持新模型](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 10.0/10

vLLM v0.26.0 新增对 Inkling 模型家族的完整支持，包括 Hopper FA4 相对注意力机制、分段 CUDA 图以及 NVFP4 量化，同时针对 DeepSeek-V4 进行了显著性能优化，在 NVIDIA、AMD ROCm 和 XPU 平台上实现了 2.94% 的端到端 TPOT 提升和 1.5-2 倍的内核加速。该版本还新增了按 KV 缓存组灵活选择注意力后端的功能、成熟的带分层二级存储的 KV 卸载机制，以及支持多模态视频和音频输入的 Rust 前端。 该版本通过跨多个硬件厂商提供具体、可复现的性能提升，显著推进了生产级 LLM 服务基础设施的发展，使组织能够在多样化的 GPU 生态系统中更高效地部署大模型。多厂商优化策略和先进量化支持在保持推理质量的同时降低了部署成本，使高性能 AI 服务在规模化应用中更加普及且经济高效。 该版本包含来自 212 位贡献者（61 位新贡献者）的 411 次提交，其中 DeepSeek-V4 的专用路由内核实现了 2.94% 的端到端 TPOT 提升，fused\_topk\_bias 带来了 1.5-2 倍的内核加速。新功能包括通过 head\_dtype 支持 fp32 lm\_head 以提高生成精度、针对 Olmo/Olmo2 和 MistralLarge3 的 Transformers 5.13.0 后端迁移，以及用于推测解码的运行时草稿权重更新。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个高吞吐量、内存高效的大语言模型推理和服务引擎，已成为生产级 LLM 部署的标准选择。该项目采用 PagedAttention 等技术实现高效的 KV 缓存管理、持续批处理以最大化 GPU 利用率，以及各种量化方法在保持模型质量的同时减少内存占用。CUDA 图是 NVIDIA 的一项技术，可将 GPU 操作捕获到可重用的执行图中，减少内核启动开销并提高 LLM 解码等重复性工作的推理延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/stable/design/cuda_graphs/">CUDA Graphs - vLLM Documentation</a></li>
<li><a href="https://docs.vllm.ai/en/stable/api/vllm/models/inkling/nvidia/ops/fa4_rel_attention/">fa 4 _rel_ attention - vLLM</a></li>
<li><a href="https://www.spheron.network/blog/tensorrt-model-optimizer-modelopt-quantization-guide/">NVIDIA TensorRT Model Optimizer (ModelOpt): FP8, INT4, and FP4 Quantization Guide (2026) | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#LLM serving`, `#GPU optimization`, `#open-source`, `#model deployment`

---

<a id="item-2"></a>
## [llama.cpp b10142 新增 MiniMax-M3 视觉支持与稀疏注意力优化](https://github.com/ggml-org/llama.cpp/releases/tag/b10142) ⭐️ 9.0/10

llama.cpp b10142 版本为 MiniMax-M3 模型引入了初步的视觉支持，包括视觉塔实现、针对稀疏层的 Flash Attention 稀疏注意力，以及重写的 CUDA 原生索引器操作，该操作将缓慢的 CPU 运算分解为 GPU+CPU 协同运算，在长上下文场景下实现了大幅加速。该版本还将 4-way 和解码路径统一为每层单次 Flash Attention 调用，并新增了多流支持。 MiniMax-M3 是一个前沿级多模态模型，拥有 100 万上下文窗口，采用专有稀疏注意力架构，将其引入 llama.cpp 使得本地高效推理一个集编程、智能体和多模态能力于一体的模型成为可能。为此版本开发的稀疏注意力和 CUDA 优化也惠及更广泛的 llama.cpp 生态系统，展示了如何处理包含路由专家、GQA 和稀疏注意力模式的复杂现代架构。 由于架构更新，此更改之前生成的所有 GGUF 文件都需要重新生成。纯文本移植复用了 MiniMax-M2 风格的 GQA（带逐头 QK-norm）、DeepSeek-V3 风格的前导密集层和路由/共享专家，以及 swigluoai 激活函数，而视觉塔和 MTP 头在初步实现中被移除。稀疏注意力在不支持时会回退到密集注意力，上下文移位被禁用，但支持提示缓存。

github · github-actions\[bot\] · 7月27日 00:20

**背景**: llama.cpp 是领先的开源 C++ 推理引擎，用于在消费级硬件上本地运行大型语言模型，通过 GGUF 格式支持广泛的模型架构。MiniMax-M3 是 MiniMax 推出的多模态模型，拥有 100 万 token 上下文窗口，采用 MiniMax 稀疏注意力（MSA）这一专有机制，选择性地关注相关 token 而非对整个上下文计算注意力。稀疏注意力是现代大语言模型中使用的一种技术，通过学习保留哪些历史 token 来降低标准注意力的二次计算成本，从而实现超长序列的高效处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M 3 - Coding &amp; Agentic Frontier, 1M Context, Multimodal</a></li>
<li><a href="https://ollama.com/library/minimax-m3">MiniMax M 3 : Coding &amp; Agentic Frontier. 1M context window.</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/visual-attention-variants">A Visual Guide to Attention Variants in Modern LLMs</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#inference`, `#open-source`, `#cuda`, `#vision-models`

---

<a id="item-3"></a>
## [llama.cpp b10141 发布，提供跨平台预编译二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10141) ⭐️ 9.0/10

llama.cpp b10141 版本已发布，提供 macOS（Apple Silicon 和 Intel）、iOS、Linux（x64、arm64、s390x、Vulkan）、Android 和 Windows（包括 CUDA 12.4、CUDA 13.3、Vulkan、ROCm、OpenVINO、SYCL 和 HIP 变体）的预编译二进制文件。该版本修复了 Android 构建问题（\#26150），并提供了 UI 包供用户使用。 作为本地大语言模型推理的事实标准，llama.cpp 广泛的跨平台支持使开发者和最终用户能够在各种硬件上运行大语言模型，无需手动编译。Vulkan、CUDA、ROCm 和 SYCL 等 GPU 加速后端的加入，确保了在消费级和企业级硬件生态系统中实现高效推理。 该版本提供了多种 GPU 后端的二进制文件，包括 CUDA 12.4 和 13.3、Vulkan、ROCm 7.2、OpenVINO 2026.2.1、SYCL（FP32/FP16）以及适用于 AMD Radeon 的 HIP。macOS Apple Silicon 的 KleidiAI 支持目前已禁用（PR \#23780），openEuler 构建也已禁用（PR \#23705）。

github · github-actions\[bot\] · 7月26日 23:03

**背景**: llama.cpp 是一个用于本地运行大语言模型的开源 C/C++ 库，与 GGML 张量库共同开发。它是 Ollama 和 LM Studio 等流行工具的核心推理引擎，支持量化模型格式（GGUF），可在消费级硬件上实现高效推理。该项目通过 CUDA（NVIDIA）、Vulkan（跨平台 GPU）、ROCm（AMD）和 SYCL（Intel）等后端提供广泛的硬件加速支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/kleidiai">Arm KleidiAI: Helping AI frameworks elevate ...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#LLM inference`, `#open-source AI`, `#cross-platform binaries`, `#edge AI`

---

<a id="item-4"></a>
## [美国公民因 GrapheneOS 手机在边境被搜查时自动擦除数据遭起诉](https://www.techspot.com/news/113236-us-prosecutors-charge-atlanta-man-after-grapheneos-phone.html) ⭐️ 9.0/10

一名亚特兰大的美国公民在边境搜查时输入胁迫 PIN 码，导致其 GrapheneOS 手机自动擦除数据，目前面临联邦指控。此案引发了关于在美国边境使用隐私保护安全功能的法律后果的广泛讨论。 此案凸显了隐私增强技术与政府边境安全权力之间日益加剧的紧张关系，可能为美国法律如何对待胁迫 PIN 码和设备擦除行为树立先例。这影响了所有使用高级隐私工具并经常国际旅行的人，尤其是经过美国边境检查站的用户。 GrapheneOS 包含胁迫 PIN 码功能，在受到胁迫时输入特定 PIN 码会擦除设备数据。社区成员讨论了替代方案，如 VeraCrypt 的诱饵操作系统功能、在过境前擦除设备并在之后从加密备份恢复，或携带空白手机以避免引起怀疑。

hackernews · eecc · 7月26日 22:21 · [社区讨论](https://news.ycombinator.com/item?id=49063022)

**背景**: GrapheneOS 是一个基于 Android 的开源、注重隐私的移动操作系统，以其强大的安全加固功能（包括胁迫 PIN 码）而闻名。胁迫 PIN 码是一种隐蔽的身份验证机制，在受到胁迫时输入会触发隐藏操作（如擦除数据或触发静默警报）。美国边境特工在入境口岸拥有广泛的电子设备搜查权，拒绝解锁设备可能导致拘留或设备被扣押。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Duress_PIN">Duress PIN</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS : the private and secure mobile OS</a></li>

</ul>
</details>

**社区讨论**: 评论者强调，虽然输入胁迫 PIN 码看似简单的操作，但美国法律会考虑行为意图，这意味着用户可能因故意销毁证据而面临指控。一些人建议使用 VeraCrypt 的诱饵操作系统或在过境前擦除设备、之后从云端备份恢复等替代方案。还有人指出，在边境采取任何隐私保护行为都可能招致额外审查，无论其是否合法。

**标签**: `#privacy`, `#security`, `#GrapheneOS`, `#border-security`, `#legal-implications`

---

<a id="item-5"></a>
## [Go 团队推出 go/analysis 框架实现模块化静态分析](https://pkg.go.dev/golang.org/x/tools/go/analysis) ⭐️ 9.0/10

Go 团队的 go/analysis 框架提供了一个标准化接口，用于构建可在 linter、IDE 和构建系统等各种工具中复用的模块化静态分析器。它允许开发者创建自定义代码质量检查器，并与现有 Go 工具无缝集成。 该框架显著降低了创建自定义 linter 和架构检查的门槛，使团队能够自动执行编码标准并捕获错误。对于手动代码审查不足的大型代码库尤其有价值，而 LLM 的最新进展使得生成分析器逻辑变得更加容易。 主要 API 类型是 Analyzer，它静态描述分析函数，包括名称、文档、标志以及对其他分析器的依赖。该框架支持与命令行工具、编辑器、Bazel 等构建系统以及代码审查平台的集成。

hackernews · AbuAssar · 7月26日 12:21 · [社区讨论](https://news.ycombinator.com/item?id=49057398)

**背景**: Go 中的静态分析涉及在不执行代码的情况下检查源代码，以查找潜在错误、强制执行样式规则或验证架构约束。go/analysis 包是 golang.org/x/tools 的一部分，为 go vet 等工具提供基础。模块化设计意味着各个分析器可以在不同的驱动程序中组合和复用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pkg.go.dev/golang.org/x/tools/go/analysis">analysis package - golang.org/x/tools/go/analysis - Go Packages</a></li>
<li><a href="https://news.ycombinator.com/item?id=49057398">Go Analysis Framework: modular static analysis by go team | Hacker News</a></li>
<li><a href="https://medium.com/@adzimzf/behind-the-scene-golang-static-analysis-e0059686351d">Behind the scene Golang Static Analysis | by Adzimzf | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反馈不一，有人指出这不是新技术，而是对现有框架的重新关注。SpiceDB 等实践者报告了成功使用该框架将隐性知识编码为自动化检查的经验，LLM 使分析器创建变得容易 10 倍。一些用户赞赏 Go 整体的工具生态系统，包括强制格式化和全面的 linting 功能。

**标签**: `#Go`, `#static-analysis`, `#developer-tools`, `#linting`, `#code-quality`

---

<a id="item-6"></a>
## [调查揭示转售大模型 API 令牌的地下中继市场](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 9.0/10

Matt Lenhard 的一项调查揭露了一个主要在中国运营的地下中继市场，转售商将窃取、滥用或折扣获取的大模型 API 密钥汇集起来，以低价出售令牌访问权限。该市场依赖 one-api 及其分支 new-api 等开源 API 代理工具，在受损凭证池之间进行请求负载均衡。 这一地下经济凸显了大模型供应商和开发者面临的重大安全与欺诈风险，因为缺乏保护的端点和薄弱的 API 密钥控制可能导致因拒付和滥用而造成巨额财务损失。这迫切需要对 API 密钥进行更严格的管理，包括设置硬性消费上限，以防止转售商为获取廉价算力或用于模型蒸馏的数据而进行剥削。 转售商通过滥用免费试用、通过未受保护的支持机器人进行代理，或使用被盗信用卡和拒付攻击来实现折扣定价。开源工具 one-api 和 new-api 虽然用于负载均衡是合法的，但正被武器化以汇集这些非法获取的密钥，并向寻求规避地域限制或收集训练数据的买家分发访问权限。

rss · Simon Willison · 7月26日 19:30

**背景**: 大模型 API 密钥是授予对专有语言模型访问权限的凭证，通常按令牌使用量计费。像 one-api 这样的开源 API 网关和代理允许开发者管理多个密钥并在它们之间进行请求负载均衡，这对于合法的速率限制管理很有用，但也可能被滥用于汇集被盗或共享的凭证。“中继市场”指的是汇集这些密钥以提供折扣 API 访问的做法，通常在法律灰色地带或 outright 欺诈中运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/songquanpeng/one-api/blob/main/README.en.md">one-api/README.en.md at main · songquanpeng/one-api</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论反映了开发者对暴露大模型端点所带来财务风险的强烈担忧，许多人附和作者呼吁供应商对 API 密钥实施严格的硬性消费上限。讨论还大量涉及 one-api 等工具的双重用途性质，承认其合法实用性的同时，谴责其被用于欺诈和令牌转售。

**标签**: `#LLM API abuse`, `#token reselling`, `#API security`, `#fraud`, `#open-source proxies`

---

<a id="item-7"></a>
## [本科毕设：纯 ARM64 汇编从零实现 YOLO26n 模型推理](https://www.reddit.com/r/MachineLearning/comments/1v6w394/i_implemented_the_yolo26n_model_inference_from/) ⭐️ 9.0/10

一个本科毕业设计项目完全使用 ARM64 汇编语言和 C 语言从零实现了 YOLO26n 目标检测推理，未依赖任何现有推理框架，目标平台为树莓派 4 上的边缘 AI 推理。该实现集成了 ARM NEON SIMD、Winograd 卷积、优化的 GEMM 微内核、缓存感知分块、算子融合，以及专为推理流水线设计的自定义二进制内存布局。 该项目罕见地、完全透明地展示了现代神经网络推理引擎在最底层硬件上的运作方式，涵盖了边缘 AI 部署中的核心技术，如 SIMD 向量化、Winograd 卷积和算子融合。它展示了 ARM 平台上软硬件协同设计的实践，并揭示了在资源受限设备上手工优化推理时所面临的真实性能权衡与差距。 该实现支持 YOLO26n 的关键组件，包括 Conv、C3K2、SPPF、C2PSA、PSA、BottleNeck 和 Detect 模块，模型参数被提取并重组为针对推理流水线优化的自定义二进制格式。作者指出，虽然实现能够产出正确的目标检测结果，但实际性能提升低于最初预期，项目已在 GitHub 上开源以征求社区反馈。

reddit · r/MachineLearning · /u/Forward\_Confusion902 · 7月26日 06:43

**背景**: YOLO26n 是 YOLO 系列实时目标检测模型的最新版本之一，其架构增强包括带快捷连接的 SPPF 模块、C2PSA 自注意力模块和 C3K2 模块。ARM NEON 是 ARM 处理器的 SIMD（单指令多数据）指令集扩展，能够在单个 CPU 周期内并行处理多个数据点，对于加速边缘设备上的神经网络推理至关重要。Winograd 卷积是一种算法技术，可减少小滤波器卷积所需的乘法运算次数，常用于 CNN 推理引擎中以数值精度换取计算速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.10369">[2201.10369] Winograd Convolution for Deep Neural Networks: Efficient Point Selection</a></li>
<li><a href="https://developer.arm.com/documentation/102467/latest/">Learn the architecture - Optimizing C code with Neon intrinsics</a></li>
<li><a href="https://docs.ultralytics.com/guides/yolo-architecture">YOLO Architecture Explained | Ultralytics Docs</a></li>

</ul>
</details>

**标签**: `#ARM64`, `#inference-optimization`, `#YOLO`, `#edge-AI`, `#SIMD`

---

<a id="item-8"></a>
## [开源 4B 模型在瑞典医学问答中接近 o3 水平准确率](https://www.reddit.com/r/MachineLearning/comments/1v71wds/openweight_4b_models_approach_o3level_medical/) ⭐️ 9.0/10

一项实证研究表明，Gemma4-E4B 和 Qwen3.5-4B 等小型开源 4B 模型在启用推理功能后，于 MedQA-SWE 瑞典医学执照考试中准确率高达 87%，接近 o3 的 88%得分，且无需任何后训练。作者还展示了 S-GRPO 论文中的

reddit · r/MachineLearning · /u/AccomplishedCat4770 · 7月26日 11:58

**标签**: `#LLM evaluation`, `#open-weight models`, `#medical QA`, `#reasoning models`, `#SFT`

---

<a id="item-9"></a>
## [长鑫科技完成 A 股史上最大 IPO，有望成市值最高公司](https://www.bloomberg.com/news/articles/2026-07-26/memory-frenzy-primes-china-champion-cxmt-for-historic-debut?srnd=phx-technology) ⭐️ 9.0/10

中国 DRAM 制造商长鑫科技在上海证券交易所科创板完成 666 亿元人民币（约 98 亿美元）IPO，为 2010 年以来 A 股最大规模上市，初始市值约 5800 亿元。上市首日股价暴涨 471.59%至 49.5 元/股，公司市值飙升至约 3.3 万亿元。 此次 IPO 表明投资者对中国半导体自主化战略（尤其是被三星、SK 海力士和美光主导的存储芯片领域）充满信心。长鑫科技的估值和上市表现凸显了 DRAM 作为 AI 计算基础设施的战略重要性，以及中国更广泛的技术独立目标。 IPO 发行价为 8.66 元/股，散户认购超额 212 倍，冻结资金约 7.07 万亿元。华西证券分析师预计公司市值有望达 5 万亿元，2028 年营收或增至 5727 亿元；公司预计 2026 年上半年净利润 500 亿至 570 亿元，实现大幅扭亏。

telegram · zaihuapd · 7月26日 07:31

**背景**: DRAM（动态随机存取存储器）是一种易失性存储器，广泛用于计算机、智能手机和数据中心，用于处理过程中的临时数据存储。IDM（设计制造一体化）模式意味着公司自主完成从芯片设计到制造的全部流程，不同于将生产外包的 Fabless 公司。长鑫科技成立于 2016 年，总部位于安徽合肥，是中国最大的国产 DRAM 制造商，也是在美国技术限制背景下中国减少对外国存储芯片供应商依赖的关键企业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E9%95%BF%E9%91%AB%E5%AD%98%E5%82%A8">长鑫存储 - 维基百科，自由的百科全书</a></li>
<li><a href="https://finance.sina.com.cn/cj/2026-07-27/doc-inikezxh8496410.shtml">长鑫科技开盘暴涨471%，总市值3.3万亿！__ 财经头条</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#semiconductor`, `#IPO`, `#China`, `#memory`

---

<a id="item-10"></a>
## [高通确认骁龙 8 Elite Gen 6 将迎两位数涨价](https://wccftech.com/qualcomm-snapdragon-8-elite-gen-6-price-hike-supplier-costs/) ⭐️ 9.0/10

高通已通知客户，由于供应商成本持续上涨，9 月 1 日后发货的产品将实施两位数涨价，这将直接影响将在 9 月 22 日骁龙峰会上亮相的骁龙 8 Elite Gen 6 及 Gen 6 Pro 芯片。受台积电单价约 3 万美元的 2nm 晶圆、DRAM 短缺以及 LPDDR6 和 UFS 5.0 的整合推动，Pro 版芯片单价可能超过 300 美元。 此次涨价将大幅提高旗舰智能手机的物料成本，可能使 SoC、内存和存储的组合成本达到每部约 600 美元，迫使手机厂商要么提高消费者售价，要么在其他方面削减成本。这也表明向台积电 2nm 工艺以及新一代内存和存储标准的过渡比以往任何一代都更加昂贵，可能会减缓这些技术在中端设备中的普及速度。 标准版（非 Pro 版）预计涨幅相对有限，将被更多厂商采用，而 Pro 版超过 300 美元的单价使其仅适用于超高端旗舰机型。LPDDR6 全新的双子通道架构和 UFS 5.0 高达 9.5 Gbps 的顺序写入速度进一步加剧了成本压力，这些都增加了组件开支。

telegram · zaihuapd · 7月26日 10:20

**背景**: 台积电的 2nm 工艺（N2）代表了半导体制造的下一个重要节点，采用全环绕栅极（GAA）晶体管架构以提升能效和性能。LPDDR6 由 JEDEC 于 2025 年 7 月发布，引入了包含四个 24 位子通道的双子通道内存架构，有效带宽较 LPDDR5X 提升一倍。UFS 5.0 是新一代移动存储标准，三星宣称其顺序写入速度高达 9.5 Gbps，相比 UFS 4.0 的 4.2 GB/s 读取速度有显著提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.jedec.org/news/pressreleases/jedec%C2%AE-releases-new-lpddr6-standard-enhance-mobile-and-ai-memory-performance">JEDEC® Releases New LPDDR6 Standard to Enhance Mobile and AI Memory Performance | JEDEC</a></li>
<li><a href="https://lemmy.eco.br/post/24120782">Samsung announces UFS 5 . 0 storage , and it may be in your next...</a></li>

</ul>
</details>

**标签**: `#Qualcomm`, `#Snapdragon`, `#semiconductor`, `#TSMC`, `#pricing`

---