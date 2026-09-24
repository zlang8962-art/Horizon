---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
content_date: 2026-09-23
lang: zh
---

> 报道范围：2026-09-23（Asia/Shanghai 自然日）

> 从 94 条内容中筛选出 12 条重要资讯。

---

1. [ggml-org/llama.cpp released b11135](#item-1) ⭐️ 10.0/10
2. [llama.cpp 发布 b11122 版本，新增 SYCL 融合内核并支持跨平台二进制文件](#item-2) ⭐️ 10.0/10
3. [llm 0.36 版本新增 GPT-6 模型与对话支持](#item-3) ⭐️ 10.0/10
4. [Ollama v0.34.4-rc1：模型推理与应用检测的修复](#item-4) ⭐️ 9.0/10
5. [微软发布 ONNX Runtime WebGPU 插件 v0.4.0](#item-5) ⭐️ 9.0/10
6. [Google 推出具备语音克隆功能的 Gemini 3.8 文本转语音模型](#item-6) ⭐️ 9.0/10
7. [Tokens too cheap to meter](#item-7) ⭐️ 9.0/10
8. [Claude Opus 5.5、GPT-6 Sol、GPT-6 Luna 及新一轮价格战](#item-8) ⭐️ 9.0/10
9. [高通发布骁龙 8 Elite Extreme Gen 6 平台](#item-9) ⭐️ 9.0/10
10. [黑客声称入侵 FBI，掌握全体员工及申请者数据](#item-10) ⭐️ 9.0/10
11. [长鑫科技首展 LPDDR6 并官宣 G5 平台量产](#item-11) ⭐️ 9.0/10
12. [美光在德国一审被判禁售，长江存储拿到首个实质性禁令](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11135](https://github.com/ggml-org/llama.cpp/releases/tag/b11135) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月23日 22:05

**标签**: `#llama.cpp`, `#open-source`, `#AI-inference`, `#model-optimization`, `#cross-platform`

---

<a id="item-2"></a>
## [llama.cpp 发布 b11122 版本，新增 SYCL 融合内核并支持跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b11122) ⭐️ 10.0/10

llama.cpp 项目发布了 b11122 版本，引入了针对 SYCL（AMD GPU）的性能优化融合内核，并为 macOS、Linux、iOS、Android 和 Windows 提供了预编译的二进制文件。 此次发布显著提升了在 AMD 硬件上进行大语言模型推理的效率，并扩展了项目的跨平台兼容性，直接受益于依赖优化 AI 计算的开发者和用户。 主要更新包括扩展了混合量化类型的 MMVQ GLU 融合，以及新增的 rms\_norm+scale 和 ssm\_conv+silu 融合，并提供了支持多种后端（如 CUDA、ROCm、Vulkan 和 SYCL）的广泛二进制文件。

github · github-actions\[bot\] · 9月23日 16:33

**背景**: llama.cpp 是一个领先的大语言模型推理开源实现，专注于在不同硬件架构上的效率和可移植性。

**标签**: `#llama.cpp`, `#AI inference`, `#SYCL`, `#performance optimization`, `#open-source`

---

<a id="item-3"></a>
## [llm 0.36 版本新增 GPT-6 模型与对话支持](https://simonwillison.net/2026/Sep/22/llm/) ⭐️ 10.0/10

llm 0.36 版本引入了对新的 OpenAI GPT-6 Sol 和 Luna 模型的支持，并允许模型插件通过 \`supports\_conversation = False\` 标志声明对话支持。 此次发布扩展了该库与前沿 AI 模型的兼容性，并通过强制执行对话支持约束来改善开发者的体验，这对于构建健壮的 LLM 驱动应用程序至关重要。 当模型声明 \`supports\_conversation = False\` 时，如果提供了对话历史，库会抛出 \`llm.ConversationNotSupported\` 异常，并且 \`llm chat\` 命令会在会话开始前拒绝此类模型。

rss · Simon Willison · 9月23日 02:48

**背景**: llm 是一个用于与大型语言模型（LLM）交互的 Python 库，旨在为各种模型提供商提供统一的接口。它由 Simon Willison 维护，被广泛用于构建基于 LLM 的工具和应用程序。

**标签**: `#LLM`, `#OpenAI`, `#Python`, `#Software Release`, `#Developer Tools`

---

<a id="item-4"></a>
## [Ollama v0.34.4-rc1：模型推理与应用检测的修复](https://github.com/ollama/ollama/releases/tag/v0.34.4-rc1) ⭐️ 9.0/10

Ollama v0.34.4-rc1 修复了间歇性的“模型未找到”错误，在思考模型上单次应用结构化输出，并改进了 ChatGPT/Codex 应用检测，同时更新了 llama.cpp 和 MLX。 这些改进提高了 AI 模型推理的可靠性和性能，特别是针对结构化输出和思考模型，这对于需要可预测和类型安全结果的应用至关重要。 该版本包括 llama.cpp 版本更新、MLX 版本升级以及动态 Gemma 4 图像分辨率选择，但没有重大安全更新或除 MLX 改进之外的硬件特定优化。

github · github-actions\[bot\] · 9月23日 10:24

**背景**: Ollama 是一个在本地运行开源大语言模型的工具，MLX 是 Apple 用于在 Apple 硅芯片上进行高效机器学习的数组框架，llama.cpp 是用于 GGUF 模型的 C++ 推理引擎。结构化输出确保模型遵循 JSON 模式以获得可预测的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/ C++ · GitHub</a></li>

</ul>
</details>

**标签**: `#AI`, `#Software`, `#Ollama`, `#MLX`, `#llama.cpp`

---

<a id="item-5"></a>
## [微软发布 ONNX Runtime WebGPU 插件 v0.4.0](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.4.0) ⭐️ 9.0/10

微软发布了 ONNX Runtime WebGPU 插件 v0.4.0，重点改进了内核性能并扩展了操作符支持。 此次发布增强了在 Web 上进行机器学习推理的性能，使开发者在浏览器中部署 AI 模型时更加高效。 主要改进包括使用子组洗牌优化的 MatMulNBits 宽瓦片执行、为 Conv/MatMul 提供融合激活支持，以及对 Qwen-3.5 和 DeepSeek Engram 的新操作符支持。

github · edgchen1 · 9月23日 01:13

**背景**: ONNX Runtime 是一个开源的机器学习推理加速器，WebGPU 插件可在 Web 浏览器中启用 GPU 加速。WebGPU 是一种现代图形 API，为高性能计算提供对 GPU 硬件的低级访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onnxruntime.ai/docs/execution-providers/WebGPU-ExecutionProvider.html">WebGPU | onnxruntime</a></li>
<li><a href="https://github.com/microsoft/onnxruntime/blob/main/plugin-ep-webgpu/README.md">onnxruntime/plugin-ep-webgpu/README.md at main - GitHub</a></li>

</ul>
</details>

**标签**: `#onnxruntime`, `#webgpu`, `#ai-inference`, `#performance-optimization`, `#gpu-acceleration`

---

<a id="item-6"></a>
## [Google 推出具备语音克隆功能的 Gemini 3.8 文本转语音模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 9.0/10

Google 推出了 Gemini 3.8 文本转语音模型，具备先进的语音复制功能，仅需 30 秒的音频样本即可重现一致的语音档案。 这项语音合成技术的进步对内容创作者和开发者具有重要意义，提供了更自然、更具表现力的语音生成，同时通过内置的同意验证和水印技术解决了伦理问题。 该模型包含 SynthID 水印和 C2PA 凭证，以保护开发者和配音人才，尽管其可用性可能因 Google 的消费者、专业消费者和云平台而异。

hackernews · swolpers · 9月23日 23:29 · [社区讨论](https://news.ycombinator.com/item?id=49817615)

**背景**: 文本转语音（TTS）技术将书面文本转换为语音，最近的进展集中在创造更自然、更具表现力的声音上。语音克隆是 TTS 的一个子集，利用 AI 从短音频样本中复制特定声音。

**社区讨论**: 用户对 Google 各平台间 AI 模型可用性不一致表示沮丧，而其他人则讨论了本地优先替代方案的潜力以及 Gemini 3.8 语音库提供的改进控制。

**标签**: `#AI`, `#Google`, `#Text-to-Speech`, `#Voice Cloning`, `#SynthID`

---

<a id="item-7"></a>
## [Tokens too cheap to meter](https://jyn.dev/tokens-too-cheap-to-meter/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · teoruiz · 9月23日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=49813482)

**标签**: `#AI`, `#LLM`, `#Economics`, `#Hardware`, `#Efficiency`

---

<a id="item-8"></a>
## [Claude Opus 5.5、GPT-6 Sol、GPT-6 Luna 及新一轮价格战](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Simon Willison 分析了 Anthropic 的 Claude Opus 5.5 和 OpenAI 的 GPT-6 Sol 及 Luna，强调了它们在定价和性能上的竞争优势。

rss · Simon Willison · 9月23日 07:46

**标签**: `#AI Models`, `#OpenAI`, `#Anthropic`, `#Pricing`, `#LLMs`

---

<a id="item-9"></a>
## [高通发布骁龙 8 Elite Extreme Gen 6 平台](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-elite-extreme-gen-6-mobile-platform) ⭐️ 9.0/10

高通推出了骁龙 8 Elite Extreme Gen 6 移动平台，该平台搭载了全新的 Oryon CPU、Adreno GPU 和 Hexagon NPU，并带来了显著的性能提升。 该平台代表了移动 AI 和图形能力的重大飞跃，为新一代智能手机设定了新的基准，并能够支持更复杂的本地应用。 Oryon CPU 是全球首款 5 GHz 手机 CPU，而 Adreno GPU 提供了 44% 的性能提升和 40% 的能效改进，Hexagon NPU 则实现了 35% 的提速。

telegram · zaihuapd · 9月23日 08:52

**背景**: 骁龙 8 Elite Extreme Gen 6 是高通为高端智能手机设计的最新旗舰移动处理器，集成了先进的 AI、图形和连接技术。

**标签**: `#Snapdragon`, `#AI Hardware`, `#Mobile Platform`, `#Chipset`, `#Qualcomm`

---

<a id="item-10"></a>
## [黑客声称入侵 FBI，掌握全体员工及申请者数据](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 9.0/10

黑客组织 ShinyHunters 声称已入侵多个与美国联邦调查局（FBI）相关的服务，并窃取了所有 FBI 员工及求职申请者的数据，包括姓名、住址、电话号码以及配偶等家属信息。 此次数据泄露可能被用于跟踪、骚扰甚至威胁 FBI 员工及其家属，也可能对美国执法和情报系统构成严重的安全与反情报风险。 该组织提供的一份包含约 5,000 名所谓 FBI 员工的样本显示，数据可能包括姓名、住址、电话号码，以及配偶等家属信息。据 BleepingComputer 报道，黑客声称窃取了 2TB 到 3TB 的数据，包括现任和前任 FBI 员工、求职申请者以及其他内部记录。

telegram · zaihuapd · 9月23日 13:00

**背景**: ShinyHunters 是一个臭名昭著的黑帽黑客组织，自 2019 年以来一直活跃，专门从事大规模数据泄露、勒索以及在暗网上出售被盗数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>
<li><a href="https://www.ic3.gov/PSA/2026/PSA260515">Internet Crime Complaint Center (IC3) | ShinyHunters: Cyber Criminal Group Attacks Learning Management System</a></li>
<li><a href="https://www.docontrol.io/blog/shinyhunters">Who Is ShinyHunters? | Tactics, Top Attacks &amp; How to Protect Your Organization</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Data Breach`, `#FBI`, `#Government Security`, `#Data Privacy`

---

<a id="item-11"></a>
## [长鑫科技首展 LPDDR6 并官宣 G5 平台量产](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9lVEtXWFNXLV9nZWJaUGhodnVaSmxPbkw5d3lmUlI5SUEyZ21NZ0t6TmhkT2VZSXNMTnBsWHdiYkxFWUExT0lGNA?oc=5) ⭐️ 9.0/10

长鑫科技在合肥 2026 世界制造业大会上首展了 LPDDR6 内存，并官宣了其 G5 平台的量产，同时亮相了字节跳动的“豆包手机”。 G5 平台的量产标志着中国国产内存芯片能力的重大进步，可能减少对外国供应商的依赖，并加强本地半导体生态系统。 长鑫科技采用“数字孪生”方法开发 G5 平台，用于设计、流片和良率管理，而 LPDDR6 代表了具有增强 RAS 功能的下一代低功耗移动 DRAM。

google\_news · 财联社 · 9月23日 16:57

**背景**: LPDDR（低功耗双倍数据速率）是一种用于移动设备的 DRAM 标准，通过低电压操作最大限度地减少功耗。长鑫科技的 G5 平台是其第五代 DRAM 技术，而“豆包手机”是字节跳动与努比亚（中兴）合作开发的 AI 原生智能手机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxmt.com/en/news/info_22.html">CXMT Announces Mass Production of 5th-Generation DRAM ...</a></li>
<li><a href="https://news.skhynix.com/en/1c-lpddr6-development-2026/">SK hynix Develops 1c LPDDR6, 6th-Generation 10nm-Class DRAM</a></li>
<li><a href="https://www.techspot.com/news/113928-cxmt-new-dram-platform-could-give-china-memory.html">China&#x27;s CXMT just entered mass production of memory chips ...</a></li>

</ul>
</details>

**标签**: `#CXMT`, `#LPDDR6`, `#G5 Platform`, `#Memory`, `#AI Hardware`

---

<a id="item-12"></a>
## [美光在德国一审被判禁售，长江存储拿到首个实质性禁令](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1YdGNNRXpHRk1oNFFWaXRXTGxzS196ZjR6bHpBd0FsbzhldFV0S0o5OUg2QnpsaldQQUJjeFdsbDA2OFlnUnBIM0QyUG9xOG9Xbmc?oc=5) ⭐️ 9.0/10

德国法院裁定支持长江存储（YMTC），授予该公司针对美光的首个实质性禁令，其中包括对特定产品的销售禁令。 这一裁决标志着长江存储在与美光的全球专利纠纷中取得重大胜利，可能改变 3D NAND 存储器市场的竞争格局。 禁令是基于 3D NAND 实用新型授予的，美光已宣布计划上诉，这可能会影响该裁决的立即执行。

google\_news · 国际电子商情 · 9月23日 09:38

**背景**: 长江存储与美光的纠纷于 2023 年 11 月升级，涉及针对 3D NAND 存储技术的复杂专利诉讼，这是现代数据存储解决方案中的关键组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://technode.com/2026/09/23/yangtze-memory-micron-3d-nand-patent-injunction/">Yangtze Memory wins first substantive injunction in 3D NAND ...</a></li>
<li><a href="https://ipfray.com/ymtc-wins-two-german-injunctions-against-micron-getting-leverage-in-global-nand-memory-patent-fight-munich-i-regional-court/">YMTC wins two German injunctions against Micron, getting ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#YMTC`, `#Micron`, `#trade\_dispute`, `#court\_injunction`

---