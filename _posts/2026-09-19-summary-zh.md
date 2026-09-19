---
layout: default
title: "Horizon Summary: 2026-09-19 (ZH)"
date: 2026-09-19
content_date: 2026-09-18
lang: zh
---

> 报道范围：2026-09-18（Asia/Shanghai 自然日）

> 从 70 条内容中筛选出 12 条重要资讯。

---

1. [ggml-org/llama.cpp 发布了 b11037 版本](#item-1) ⭐️ 10.0/10
2. [llama.cpp b11036 添加了图缓冲区处理和多平台二进制文件](#item-2) ⭐️ 10.0/10
3. [NVIDIA 发布 TensorRT-LLM v1.3.0rc27 版本，修复 GPU 相关问题](#item-3) ⭐️ 10.0/10
4. [警惕：针对知名 Rustaceans 的定向攻击](#item-4) ⭐️ 10.0/10
5. [Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash](#item-5) ⭐️ 9.0/10
6. [ZCode 静默将 Git 历史上传至云端](#item-6) ⭐️ 9.0/10
7. [Self-generated prompt injections in compaction summaries](#item-7) ⭐️ 9.0/10
8. [Engrams Embedding Entendre：DRAM/SSD 卸载的高效协同设计](#item-8) ⭐️ 9.0/10
9. [使用 NHANES 数据对冠心病风险进行分类并审计数据泄露](#item-9) ⭐️ 9.0/10
10. [联合国携手谷歌打造 AI 可用的全球数据平台](#item-10) ⭐️ 9.0/10
11. [智谱发布 GLM-5.3-FlashX，最高 200 tokens/s](#item-11) ⭐️ 9.0/10
12. [美银：AI 加速器本土厂商营收市占率 2025 年近 50%](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布了 b11037 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b11037) ⭐️ 10.0/10

llama.cpp b11037 版本修复了 WebGPU 对 GET\_ROWS 的支持，并提供了跨平台二进制文件。

github · github-actions\[bot\] · 9月18日 20:13

**标签**: `#llama.cpp`, `#AI inference`, `#WebGPU`, `#macOS`, `#Open Source`

---

<a id="item-2"></a>
## [llama.cpp b11036 添加了图缓冲区处理和多平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b11036) ⭐️ 10.0/10

llama.cpp b11036 版本引入了对图缓冲区预留失败的修复，并为 macOS、iOS 和 Linux 提供了针对各种架构和硬件加速器的预编译二进制文件。 此次发布显著提高了 llama.cpp 推理引擎的稳定性和可移植性，使开发者更容易在各种硬件平台上部署大语言模型，从移动设备到高性能服务器。 核心更新是 PR \#26070 的修复，用于处理图缓冲区预留失败，防止潜在的崩溃。该版本包括适用于 Apple Silicon、Intel Mac 和 iOS XCFramework 的二进制文件，以及支持 CPU、Vulkan、CUDA \(12/13\)、ROCm、OpenVINO 和 SYCL 的 Linux 版本。

github · github-actions\[bot\] · 9月18日 19:32

**背景**: llama.cpp 是一个用于在消费级硬件上本地运行大语言模型（LLM）的高性能 C++ 库。它使用 ggml 张量库来优化跨不同后端（如 CPU、GPU 和专用加速器）的计算。该项目由 ggml-org 维护，是运行 LLaMA 等模型的流行工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/pull/26070">ggml : handle graph buffer reservation failure by FaiChou · Pull Request #26070 · ggml-org/llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases · ggml-org/llama.cpp</a></li>
<li><a href="https://huggingface.co/blog/introduction-to-ggml">Introduction to ggml</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#open-source`, `#machine-learning`, `#software-release`

---

<a id="item-3"></a>
## [NVIDIA 发布 TensorRT-LLM v1.3.0rc27 版本，修复 GPU 相关问题](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc27) ⭐️ 10.0/10

NVIDIA 发布了 TensorRT-LLM v1.3.0rc27 版本，修复了关键的 GPU 特定推理问题，并新增了 MiniMax-H3 VisualGen 支持和 Anthropic 兼容的 API。 此次更新对使用 NVIDIA GPU 的 AI 开发者具有重要意义，因为它解决了多 GPU 和 Blackwell 架构中的稳定性问题，确保高性能推理工作负载的部署更加顺畅。 关键修复包括 GPT-OSS Eagle3 推测解码挂起、B200 GPU 上 NVFP4 准确性问题以及 Cosmos3 管道故障的变通方法，同时新功能集成了 cuDNN 注意力后端和 KV 缓存优化。

github · tongyuantongyu · 9月18日 11:14

**背景**: TensorRT-LLM 是 NVIDIA 用于 LLM 的高性能推理 SDK，优化了 GPT 和 Qwen 等模型的 GPU 执行。NVFP4 是 Blackwell GPU 的新 4 位浮点格式，提高了效率。推测解码通过使用较小的草稿模型来加速生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog11_GPT_OSS_Eagle3.html">Running GPT-OSS-120B with Eagle3 Speculative Decoding on ...</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**标签**: `#AI-inference`, `#TensorRT-LLM`, `#GPU-optimization`, `#Multi-GPU`, `#Blackwell-Architecture`

---

<a id="item-4"></a>
## [警惕：针对知名 Rustaceans 的定向攻击](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 10.0/10

安全警报警告称，攻击者正利用视频通话和剪贴板命令针对知名 Rustaceans 进行定向攻击，以入侵其设备和账户。

rss · Simon Willison · 9月18日 07:59

**标签**: `#security`, `#supply-chain-attack`, `#rust`, `#social-engineering`, `#malware`

---

<a id="item-5"></a>
## [Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash](https://cactuscompute.com/needle) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · HenryNdubuaku · 9月18日 08:11 · [社区讨论](https://news.ycombinator.com/item?id=49748553)

**标签**: `#AI models`, `#model compression`, `#automation`, `#tool calling`, `#small language models`

---

<a id="item-6"></a>
## [ZCode 静默将 Git 历史上传至云端](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 9.0/10

一篇博客文章揭露了 ZCode 的代码库索引功能会静默地将用户的 Git 历史上传至云端，且未获得明确同意。 这一问题凸显了 AI 代理工具中的关键安全漏洞，引发了关于开发者环境中数据隐私和未经授权的数据外泄的担忧。 该功能旨在帮助用户索引代码库，但在“自动模式”下运行并绕过标准权限检查，导致意外的数据上传。

hackernews · csmantle · 9月18日 14:11 · [社区讨论](https://news.ycombinator.com/item?id=49750694)

**背景**: AI 代理越来越多地用于辅助开发者，但它们与 Git 等本地开发工具的集成需要谨慎处理权限和数据隐私问题。

**社区讨论**: 社区对缺乏透明度和控制权表达了强烈担忧，一些用户指出 Codex 和 Claude Code 等其他 AI 工具也存在类似问题。

**标签**: `#AI security`, `#developer tools`, `#data privacy`, `#sandboxing`, `#Git`

---

<a id="item-7"></a>
## [Self-generated prompt injections in compaction summaries](https://simonwillison.net/2026/Sep/17/compaction-summaries/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Simon Willison · 9月18日 04:57

**标签**: `#AI safety`, `#prompt injection`, `#agent systems`, `#model misalignment`, `#context management`

---

<a id="item-8"></a>
## [Engrams Embedding Entendre：DRAM/SSD 卸载的高效协同设计](https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign) ⭐️ 9.0/10

该文章介绍了一种名为 Engrams Embedding Entendre 的新模型架构，它实现了模型计算在 DRAM 和 NVMe 存储之间的高效卸载，同时还包括对 DeepSeek V4.1 Flash 和 AgentX 的实验。 这种协同设计方法通过减少内存压力和提高存储利用率，解决了 AI 推理中的关键瓶颈，有望降低成本并实现大模型的高效部署。 该架构利用嵌入技术优化了快速内存和较慢存储之间的数据移动，特别关注 NVMe 性能和 DeepSeek V4.1 Flash 的优化。

rss · Semianalysis · 9月18日 22:34

**背景**: DRAM 是具有高速度但容量有限的易失性内存，而 NVMe SSD 提供了更大容量但速度较低的存储。将模型计算卸载到 SSD 可以减少 DRAM 使用，但会引入延迟挑战。

**标签**: `#AI Compute`, `#DRAM/SSD Offloading`, `#Hardware Co-design`, `#Model Architecture`, `#Inference Optimization`

---

<a id="item-9"></a>
## [使用 NHANES 数据对冠心病风险进行分类并审计数据泄露](https://www.reddit.com/r/MachineLearning/comments/1wjp062/classifying_coronary_heart_disease_risk_from/) ⭐️ 9.0/10

作者开发了一个项目，使用 2011-2018 年的 NHANES 数据预测冠心病，比较了逻辑回归、随机森林和梯度提升模型，同时进行了详细的数据泄露审计。 这项工作意义重大，因为它突出了医疗机器学习中数据泄露的关键问题，展示了如何包含间接诊断变量会人为地提高模型性能，并强调了严格验证的重要性。 该项目在移除泄露变量并应用 sigmoid 重新校准后，在测试集上达到了 0.875 的 ROC-AUC 和 0.239 的 PR-AUC，但由于数据中 CHD 的稀有性，PPV 仍然很低，仅为 0.13。

reddit · r/MachineLearning · /u/YouJonaa · 9月18日 20:36

**背景**: NHANES（国家健康和营养检查调查）是一个评估美国成人和儿童健康和营养状况的项目，通过访谈、身体检查和实验室测试收集数据。

**标签**: `#machine-learning`, `#data-leakage`, `#healthcare`, `#logistic-regression`, `#random-forest`

---

<a id="item-10"></a>
## [联合国携手谷歌打造 AI 可用的全球数据平台](https://techcrunch.com/2026/09/17/un-turns-to-google-to-make-its-global-data-ready-for-ai-agents/) ⭐️ 9.0/10

联合国宣布与谷歌合作，推出新的数据共享平台，支持自然语言查询并兼容 MCP 协议，取代原有的 UNData 门户。 这一举措解决了大模型在访问全球发展数据时准确率低的问题，有望提高数据对 AI 系统的可访问性，并支持国际发展工作。 联合国儿童基金会测试显示，6 款大模型回答全球发展指标问题的平均准确率仅 21.2%，推动了此次现代化工作。

telegram · zaihuapd · 9月18日 12:50

**背景**: UNdata 是联合国于 2005 年推出的基于网络的全球统计资源共享服务，旨在通过单一入口点为用户提供免费、便捷的全球统计数据访问。模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开源标准，用于规范 AI 系统与外部工具和数据源之间的集成和数据共享方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>
<li><a href="https://data.un.org/Default.aspx">UNdata - United Nations</a></li>

</ul>
</details>

**标签**: `#AI`, `#Data Platform`, `#United Nations`, `#Google`, `#MCP Protocol`

---

<a id="item-11"></a>
## [智谱发布 GLM-5.3-FlashX，最高 200 tokens/s](https://mp.weixin.qq.com/s/ZJHhQrDeiwOGkkaqHw7kqA) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月18日 14:48

**标签**: `#AI Model`, `#Inference Speed`, `#API`, `#Optimization`, `#Chips`

---

<a id="item-12"></a>
## [美银：AI 加速器本土厂商营收市占率 2025 年近 50%](https://news.google.com/rss/articles/CBMiYkFVX3lxTE9jQ3RlNWtaRTJOS3g5eFlobjVzZWFlcFV0WFM4NVNkNVFDd2JYV0oteGFGcGlJb2JtcnBhT0J4a1Q3ZXhMOVY0bzJ3Tm1XS1hMckM1bmFSWk9HZHE2Mk9vcHZ3?oc=5) ⭐️ 9.0/10

美银预测 AI 加速器本土厂商的营收市占率将在 2025 年接近 50%，2028 年接近 80%。 这一转变标志着 AI 基础设施格局的重大变化，减少了对国外供应商的依赖，并推动了国内芯片产业的发展。 这一增长由美国出口管制和国内政策驱动，华为在 2025 年以 81.2 万颗的出货量断层领跑。

google\_news · 观点网 · 9月18日 17:35

**背景**: AI 加速器是专为加速 AI 工作负载而设计的专用硬件芯片。由于地缘政治压力和支持性政策，本土制造商正在抢占市场份额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/LivingInHarmony/status/2040725808738636123">The TOP8 shipment rankings for domestic Al accelerator cards are ...</a></li>
<li><a href="https://www.okx.com/ru-eu/orbit/insight/72737893933536">4⃣️/2⃣️ 早报①股市 美股周三（4月1日）收涨，标普500指数升 ...</a></li>

</ul>
</details>

**标签**: `#AI加速器`, `#芯片`, `#市场份额`, `#AI基础设施`, `#市场预测`

---