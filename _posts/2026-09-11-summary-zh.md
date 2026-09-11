---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
content_date: 2026-09-10
lang: zh
---

> 报道范围：2026-09-10（Asia/Shanghai 自然日）

> 从 80 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp 发布 b10893 版本，增加测试容差并提供预编译二进制文件](#item-1) ⭐️ 10.0/10
2. [llama.cpp v b10892 发布，包含更新二进制文件和测试更改](#item-2) ⭐️ 10.0/10
3. [microsoft/onnxruntime released v1.29.1](#item-3) ⭐️ 9.0/10
4. [Shopify 回归原生 Swift 和 Kotlin 开发](#item-4) ⭐️ 9.0/10
5. [Rust is tier-1 language at Microsoft](#item-5) ⭐️ 9.0/10
6. [AI 开发首个通过微信通话传播的零点击蠕虫](#item-6) ⭐️ 9.0/10
7. [1.1.1.1 now supports post-quantum DNSSEC, all 2,420 bytes of it](#item-7) ⭐️ 9.0/10
8. [Kubernetes v1.37 引入节点生命周期条件](#item-8) ⭐️ 9.0/10
9. [🤖 DeepSeek V4.1 Flash：更强、更快、更普惠](#item-9) ⭐️ 9.0/10
10. [DeepSelect：面向 DSA 与采样器的 TopK 内核](#item-10) ⭐️ 9.0/10
11. [募资 330 亿！长江存储 IPO 受理 这十大设备龙头实锤进入供应链 - 新浪网](#item-11) ⭐️ 9.0/10
12. [中国 DRAM 厂商 CXMT 启动 IPO 流程，计划募资 295 亿元人民币](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp 发布 b10893 版本，增加测试容差并提供预编译二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10893) ⭐️ 10.0/10

llama.cpp 发布 b10893 版本，增加了对 Add 融合测试的容差，并为 macOS、Linux、Android 和 Windows 提供了针对各种架构和硬件后端的预编译二进制文件。 此次发布对开源 AI 推理生态系统具有重要意义，因为它通过为广泛的平台和硬件配置提供现成的二进制文件，提高了测试的稳定性，并使该库更加易于使用。 此次发布包含针对 Add 融合测试的具体调整，并为 macOS、Linux、Android 和 Windows 提供了广泛的预编译二进制文件，支持 CUDA、Vulkan、ROCm 和 SYCL 等后端，尽管目前 macOS Apple Silicon 的 KleidiAI 支持已被禁用。

github · github-actions\[bot\] · 9月10日 20:40

**背景**: llama.cpp 是一个流行的开源库，用于在消费级硬件上运行大型语言模型（LLM），以其高效性和跨平台支持而闻名。它允许用户在本地运行模型，而无需使用云服务。

**标签**: `#llama.cpp`, `#AI-inference`, `#open-source`, `#software-release`, `#optimization`

---

<a id="item-2"></a>
## [llama.cpp v b10892 发布，包含更新二进制文件和测试更改](https://github.com/ggml-org/llama.cpp/releases/tag/b10892) ⭐️ 10.0/10

llama.cpp 项目发布了 b10892 版本，主要变更包括在 test-backend-ops.cpp 中移除 SYCL 特殊处理，并为 macOS、Linux、Android 和 Windows 提供了针对不同架构和硬件后端的预编译二进制文件。 此版本通过提供跨平台的优化大型语言模型实现，显著影响了 AI 计算生态系统，使开发者能够在多样化的硬件配置上高效部署模型。 此次更新包含针对 CPU、GPU（CUDA、Vulkan、ROCm、OpenVINO、SYCL）以及 Windows 上 OpenCL Adreno 等专用后端的二进制文件，同时 macOS Apple Silicon 的 KleidiAI 构建版本在本发布中被禁用。

github · github-actions\[bot\] · 9月10日 19:54

**背景**: llama.cpp 是一个用于运行大型语言模型的高性能 C++ 库，因其高效性和对多种硬件加速器的支持，被广泛用于在消费级硬件和边缘设备上进行推理。

**标签**: `#llama.cpp`, `#AI`, `#Open Source`, `#Software Engineering`, `#Performance`

---

<a id="item-3"></a>
## [microsoft/onnxruntime released v1.29.1](https://github.com/microsoft/onnxruntime/releases/tag/v1.29.1) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · adrastogi · 9月10日 13:26

**标签**: `#onnxruntime`, `#groupqueryattention`, `#kv-cache`, `#ai-inference`, `#performance`

---

<a id="item-4"></a>
## [Shopify 回归原生 Swift 和 Kotlin 开发](https://shopify.engineering/back-to-native) ⭐️ 9.0/10

Shopify 正将其移动开发栈从 React Native 回归到原生 Swift 和 Kotlin，以提高性能和可维护性。 这一举措凸显了公司重新评估跨平台框架、转而支持原生开发以获得更好优化和长期成本效率的趋势。 这一决定受到大语言模型的影响，它使迁移过程更快、更高效，尽管核心技术工作是在大语言模型广泛采用之前完成的。

hackernews · fnthawar2 · 9月10日 22:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 允许在 iOS 和 Android 之间共享代码，但与原生开发相比，它通常会引入性能开销和维护挑战。大语言模型最近已成为协助代码迁移和重构的工具，可能减少此类转换所需的时间和精力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/elca-it/experimenting-llm-assisted-software-migrations-a-java-spring-case-study-ddde48c4d95d">Experimenting LLM-assisted software migrations: a Java Spring case study | by Hugo Hof | ELCA IT | Medium</a></li>
<li><a href="https://studiokrew.com/blog/react-native-vs-swift-kotlin/">React Native vs Swift and Kotlin in 2025: Which Should You ...</a></li>

</ul>
</details>

**社区讨论**: 开发者对 Shopify 的决定表示认可，指出大语言模型可以加速迁移，但原生开发对于平台特定优化仍然至关重要。

**标签**: `#mobile-development`, `#react-native`, `#native-development`, `#llm-assisted-migration`, `#software-engineering`

---

<a id="item-5"></a>
## [Rust is tier-1 language at Microsoft](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · mmastrac · 9月10日 21:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**标签**: `#Rust`, `#Software Engineering`, `#Microsoft`, `#Programming Languages`, `#Migration`

---

<a id="item-6"></a>
## [AI 开发首个通过微信通话传播的零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm，这是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫，无需用户交互即可劫持账户。 这一突破展示了 AI 如何加速漏洞研究和漏洞利用开发，可能降低创建复杂恶意软件的门槛。 利用 AI，团队在约两天内发现了漏洞并编写了首个远程代码执行（RCE）漏洞利用程序，并在一周内完成了蠕虫开发，这以前需要数月时间。

rss · Simon Willison · 9月10日 08:56

**背景**: 零点击漏洞利用是一种无需任何用户交互即可获得系统未授权访问的攻击类型，常用于监视或间谍活动。远程代码执行（RCE）是一种关键漏洞，允许攻击者在远程机器上执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/security/what-is-remote-code-execution/">What is remote code execution?</a></li>
<li><a href="https://www.securview.com/ai-security-essentials/zero-click-exploit">Zero Click Exploit : Definition and Key Concepts</a></li>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls</a></li>

</ul>
</details>

**标签**: `#AI-security-research`, `#Zero-click-exploit`, `#WeChat`, `#RCE`, `#AI-research`

---

<a id="item-7"></a>
## [1.1.1.1 now supports post-quantum DNSSEC, all 2,420 bytes of it](https://blog.cloudflare.com/post-quantum-dnssec-1111/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Cloudflare Blog · 9月10日 21:00

**标签**: `#DNSSEC`, `#Post-Quantum Cryptography`, `#Cloudflare`, `#Security`, `#Software Engineering`

---

<a id="item-8"></a>
## [Kubernetes v1.37 引入节点生命周期条件](https://kubernetes.io/blog/2026/09/09/kubernetes-v1-37-node-lifecycle-conditions/) ⭐️ 9.0/10

Kubernetes v1.37 引入了五个新的节点生命周期条件：DrainInProgress（排空进行中）、Drained（已排空）、MaintenancePlanned（计划维护）、MaintenanceInProgress（维护进行中）和 GracefulNodeShutdownInProgress（优雅节点关机进行中），以更好地描述排空和维护等节点状态。 这些条件提供了一种共享的、由 Kubernetes 拥有的描述节点状态的方式，提高了集群的可靠性，并使管理员更容易在维护操作期间理解和管理工作节点健康状态。 每个条件都使用 status（True/False/Unknown）、reason 和 message 字段来报告当前状态，其中 MaintenancePlanned 表示未来的变更，GracefulNodeShutdownInProgress 表示优雅关机正在进行中。

rss · Kubernetes Blog · 9月10日 02:30

**背景**: Kubernetes 使用各种机制（如就绪状态、污点和 Pod 状态）来描述节点条件，但之前缺乏统一的方式来信号化维护或排空状态，通常依赖提供商特定的 API 或手动注释。

**标签**: `#Kubernetes`, `#DevOps`, `#Node Management`, `#Software Engineering`, `#Cluster Administration`

---

<a id="item-9"></a>
## [🤖 DeepSeek V4.1 Flash：更强、更快、更普惠](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月10日 13:54

**标签**: `#DeepSeek`, `#AI Model`, `#API Pricing`, `#Machine Learning`, `#Software Development`

---

<a id="item-10"></a>
## [DeepSelect：面向 DSA 与采样器的 TopK 内核](https://github.com/deepseek-ai/DeepSelect) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月10日 15:28

**标签**: `#DeepSeek`, `#TopK Kernel`, `#Sparse Attention`, `#AI Compute`, `#Performance Optimization`

---

<a id="item-11"></a>
## [募资 330 亿！长江存储 IPO 受理 这十大设备龙头实锤进入供应链 - 新浪网](https://news.google.com/rss/articles/CBMilAFBVV95cUxQNVVnNjlwYWRBdGR3ZDVtZFQ0RFpZcWU2bm4zRDVMRy1TZ2RUbEdwRk45dTkyUmFGQnd0ZkhJMEVWak41UVZwekJnTlZOY1JlRE1IaW01eVlLMXJOb2V0bEQ1cDVncWg2TC1Wc0drejdrendrbTJDajBYcmhJY0FmSlRvSnk5YnhvSUY3NXlIWGN4TWt3?oc=5) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

google\_news · 新浪网 · 9月10日 10:02

**标签**: `#semiconductors`, `#IPO`, `#Yangtze Memory`, `#memory`, `#hardware`

---

<a id="item-12"></a>
## [中国 DRAM 厂商 CXMT 启动 IPO 流程，计划募资 295 亿元人民币](https://news.google.com/rss/articles/CBMijgFBVV95cUxNcTUxQTAySVlIb0NoTGpCR09pbWtqbWowVlE1ZXNuX1B5SWpsRHp2ZUdfUmlTNWlpUzkwcHNhMVI1R2IyQzdYdFF3dmNiZTZVSkF3bWJYQmlqTUJ2UG9LS0t6V0luNGJ6VWhSVWxUZy05eEhKYk0yOUdXZWxielR6ZnEwUWdYOUVncndiUll3?oc=5) ⭐️ 9.0/10

中国 DRAM 厂商 CXMT 已正式启动 IPO 流程，计划募资约 295 亿元人民币，旨在成为全球第四大内存芯片制造商。 这一举措意义重大，因为它凸显了中国半导体公司在全球内存市场中的日益增长的影响力，而内存市场对于 AI 硬件和数据中心基础设施至关重要。 该公司上半年营收同比增长 873%至 1503 亿元人民币，归母净利润达 776 亿元，显示出强劲的财务表现。

google\_news · cnnews.chosun.com · 9月10日 04:23

**背景**: DRAM（动态随机存取存储器）是一种临时存储数据的计算机内存，对于运行应用程序和 AI 工作负载至关重要。CXMT 是一家中国国有支持的半导体公司，与三星和 SK 海力士等全球巨头竞争。

**标签**: `#DRAM`, `#Semiconductors`, `#IPO`, `#AI Hardware`, `#Memory`

---