---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
content_date: 2026-09-15
lang: zh
---

> 报道范围：2026-09-15（Asia/Shanghai 自然日）

> 从 65 条内容中筛选出 11 条重要资讯。

---

1. [ggml-org/llama.cpp 发布版本 b10969](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10984](#item-2) ⭐️ 9.0/10
3. [将 20 美元的 4G 热点改装成短信设备](#item-3) ⭐️ 9.0/10
4. [Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar](#item-4) ⭐️ 9.0/10
5. [端侧与数据中心推理：机器人大脑的权衡](#item-5) ⭐️ 9.0/10
6. [Cloudflare Workers 现支持细粒度授权](#item-6) ⭐️ 9.0/10
7. [Kubernetes v1.37：内存服务质量（QoS）升级为 Beta](#item-7) ⭐️ 9.0/10
8. [从头训练 44M 参数量化 LLM，模型大小仅 19.8 MB](#item-8) ⭐️ 9.0/10
9. [联发科发布天玑 9600 Pro](#item-9) ⭐️ 9.0/10
10. [中国国产存储芯片追赶速度惊人](#item-10) ⭐️ 9.0/10
11. [“Project Lily”内幕：人工阅读 ChatGPT 聊天记录](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布版本 b10969](https://github.com/ggml-org/llama.cpp/releases/tag/b10969) ⭐️ 10.0/10

llama.cpp 版本 b10969 在 CI 中添加了 Ubuntu-CUDA 构建，提高了 AI 模型推理的跨平台支持。

github · github-actions\[bot\] · 9月15日 03:50

**标签**: `#llama.cpp`, `#AI inference`, `#CUDA`, `#CI/CD`, `#open-source`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10984](https://github.com/ggml-org/llama.cpp/releases/tag/b10984) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月15日 21:41

**标签**: `#llama.cpp`, `#CUDA`, `#AI inference`, `#open-source`, `#performance`

---

<a id="item-3"></a>
## [将 20 美元的 4G 热点改装成短信设备](https://bkovac.github.io/modem-thing/) ⭐️ 9.0/10

一名黑客成功将一个廉价的 20 美元 4G 无线热点改装成专用的短信设备，通过修改硬件并添加一个回收利用的键盘来实现。 该项目展示了如何创造性地重新利用低成本硬件来创建功能齐全、注重隐私的通信工具，这对寻求智能手机替代品的用户具有重要意义。 该项目涉及芯片级修改、电池升级以及与回收利用键盘的集成，以启用短信功能，创作者在 GitHub 上分享了详细的技术步骤。

hackernews · bobili1234 · 9月15日 21:20 · [社区讨论](https://news.ycombinator.com/item?id=49712102)

**背景**: 4G 无线热点是通过蜂窝网络提供互联网访问的便携式设备，常被用作备用或主要互联网来源。将它们改装成专用设备（如 cyberdeck）涉及修改其内部组件和软件以实现特定功能。

**社区讨论**: 社区成员称赞了该项目的创意和实用性，有些人建议增加更大的电池以延长续航时间，或在设备上运行代理系统。

**标签**: `#hardware-hacking`, `#4g-modem`, `#cyberdeck`, `#battery-life`, `#repurposing`

---

<a id="item-4"></a>
## [Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Semianalysis · 9月15日 06:08

**标签**: `#AI Compute`, `#Hardware Co-design`, `#Inference Optimization`, `#Performance Metrics`, `#Cost Efficiency`

---

<a id="item-5"></a>
## [端侧与数据中心推理：机器人大脑的权衡](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 9.0/10

该通讯分析了机器人模型的端侧与数据中心推理之间的权衡，比较了 Jetson Thor 和 B300 的总拥有成本（TCO），并讨论了部署挑战和“网络墙”问题。 这一分析对机器人行业具有重要意义，因为它强调了自主系统中硅效率、部署成本和实时性能约束之间的关键平衡。 波士顿动力在 Google TPU 上运行机器人大脑，但对于 96 台机器人，Jetson Thor 的总拥有成本（TCO）最低，为每小时 14.97 美元，而 RTX 6000 Pro 为 15.61 美元，B300 为 18.63 美元，同时“网络墙”对远程推理构成了延迟风险。

rss · Semianalysis · 9月15日 00:37

**背景**: 机器人推理需要在模型大小、硅效率和实时性能之间取得平衡。“网络墙”指的是将机器人推理卸载到数据中心时出现的延迟问题，这对于手术等时间敏感的任务来说可能是不可接受的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/boston-dynamics-runs-robot-brains-on-tpus-rivals-stay-on-jetson">Boston Dynamics runs robot brains on TPUs; rivals stay on Jetson</a></li>
<li><a href="https://nalinraut.github.io/blog/2026/inferential/?trk=public_post_comment-text">Inferential - Centralized Inference Orchestration for Factory Robotics</a></li>
<li><a href="https://www.roboticscenter.ai/state-of-robotics-2026">State of Robotics 2026 | Robotics Center page</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#on-device computing`, `#hardware efficiency`, `#robotics`, `#semiconductors`

---

<a id="item-6"></a>
## [Cloudflare Workers 现支持细粒度授权](https://blog.cloudflare.com/workers-granular-authorization/) ⭐️ 9.0/10

Cloudflare Workers 现支持细粒度授权，允许用户将访问范围限定到单个 Workers 并分配更窄的 Developer Platform 角色。 此功能通过确保团队成员、CI 令牌和代理仅拥有调试、部署或监控所需的安全访问权限，显著提高了安全性，解决了 DevOps 和开发者工具中的一个关键需求。 新角色支持资源级访问，虽然 wrangler 登录 OAuth 流程目前不支持细粒度授权，但用户可以使用账户拥有的 API 令牌进行身份验证以使用细粒度权限。

rss · Cloudflare Blog · 9月15日 21:00

**背景**: Cloudflare Workers 是一个允许开发者在边缘运行 JavaScript、TypeScript 和 Rust 代码的无服务器计算平台。授权是控制资源访问的过程，而细粒度授权则提供对谁可以访问特定资源的精细控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/workers-granular-authorization/">Give every teammate and agent the right level of access to your Workers | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/workers/authorization/">Roles and permissions · Cloudflare Workers docs</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Developer Tools`, `#Authorization`, `#Security`, `#DevOps`

---

<a id="item-7"></a>
## [Kubernetes v1.37：内存服务质量（QoS）升级为 Beta](https://kubernetes.io/blog/2026/09/14/kubernetes-v1-37-memory-qos-graduates-to-beta/) ⭐️ 9.0/10

Kubernetes v1.37 将内存服务质量（QoS）功能升级为 Beta 并默认启用，适用于运行 cgroup v2 的 Linux 节点。 这一改进通过提供更好的内核指导来优化 Linux cgroup v2 内存处理，对于维持容器化环境中的稳定性和性能至关重要。 该功能现在通过 MemoryQoS 特性门控默认启用，但内存限制和预留仅在通过 kubelet 设置（如 memoryThrottlingFactor 和 memoryReservationPolicy）显式配置时才会应用。

rss · Kubernetes Blog · 9月15日 02:30

**背景**: 内存服务质量（QoS）最初作为 Alpha 功能引入 Kubernetes v1.22，并在 v1.36 中扩展了分级内存预留功能。

**标签**: `#Kubernetes`, `#Memory Management`, `#Software Engineering`, `#System Administration`, `#DevOps`

---

<a id="item-8"></a>
## [从头训练 44M 参数量化 LLM，模型大小仅 19.8 MB](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 9.0/10

研究人员从头训练了 SHADOW-50M，这是一个在 450 亿个 token 上训练的 44M 参数量化 LLM，在 CPU 上以 1,900 tok/s 的速度运行，模型大小仅 19.8 MB，内存使用约 41 MB。 这一突破展示了在资源受限设备上实现高效本地推理的潜力，最小化资源需求，可能推动强大的本地 AI 应用的发展。 该模型使用三进制\{-1,0,+1\}权重，词汇表包含 73,880 个 token，由固定的 512 位指纹表示，并配备一个 159 KB 的编译内核，可在离线环境和 WebAssembly 中以约 500 tok/s 的速度运行。

reddit · r/MachineLearning · /u/Final-Data-1410 · 9月15日 20:59

**背景**: LLM 量化通过降低数值精度（例如从 FP16 到 INT4/INT8）来压缩模型权重，从而实现高效的本地推理。三进制权重将权重限制为-1、0 和+1，提高了内存效率。WebAssembly 允许在浏览器中执行高性能代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://localllm.in/blog/quantization-explained">The Complete Guide to LLM Quantization - localllm.in</a></li>
<li><a href="https://grokipedia.com/page/Ternary_Weights">Ternary Weights</a></li>
<li><a href="https://blog.pixelfreestudio.com/how-to-use-webassembly-for-machine-learning-in-the-browser/">How to Use WebAssembly for Machine Learning in the Browser</a></li>

</ul>
</details>

**标签**: `#quantized-llm`, `#local-ai`, `#software-engineering`, `#machine-learning`, `#webassembly`

---

<a id="item-9"></a>
## [联发科发布天玑 9600 Pro](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月15日 16:57

**标签**: `#Semiconductors`, `#Mobile Processors`, `#AI Hardware`, `#Chip Manufacturing`, `#MediaTek`

---

<a id="item-10"></a>
## [中国国产存储芯片追赶速度惊人](https://news.google.com/rss/articles/CBMiTkFVX3lxTFA4MTBxelRNYm9JTUtqeFpuUjdVQVpZMlpMdWxrYVN2WUtQam9pN3Y5R0p3Zno0QUozMXBQdDVDbW5BbXpsUlpTbnBodTNGZw?oc=5) ⭐️ 9.0/10

中国在 NAND、DRAM 和 HBM 存储芯片领域已大幅缩小与全球领先者的技术差距。 这一进展对中国实现半导体自主可控、减少对外国技术的依赖至关重要。 与全球领先者的差距约为：NAND 约 1 年，DRAM 约 2 年，HBM 约 3 年。

google\_news · 36 Kr · 9月15日 17:52

**背景**: 高带宽内存（HBM）是一种由三星、AMD 和 SK 海力士开发的 3D 堆叠 SDRAM 技术，广泛应用于 GPU 和 AI 加速器。中国的半导体产业，包括长江存储（YMTC）和长鑫存储等公司，正在快速推进国产制造能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory chips`, `#HBM`, `#AI hardware`, `#China tech`

---

<a id="item-11"></a>
## [“Project Lily”内幕：人工阅读 ChatGPT 聊天记录](https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/) ⭐️ 8.0/10

404 Media 报道称 OpenAI 雇佣人类审查 ChatGPT 对话以改进模型，这引发了隐私担忧。

telegram · zaihuapd · 9月15日 19:56

**标签**: `#AI`, `#Privacy`, `#OpenAI`, `#Model Evaluation`, `#Data Security`

---