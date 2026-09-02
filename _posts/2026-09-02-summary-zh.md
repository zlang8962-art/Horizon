---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
content_date: 2026-09-01
lang: zh
---

> 报道范围：2026-09-01（Asia/Shanghai 自然日）

> 从 109 条内容中筛选出 12 条重要资讯。

---

1. [ggml-org/llama.cpp 发布了 b10738 版本](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp 发布了 b10737 版本](#item-2) ⭐️ 10.0/10
3. [Virtualizor 更新设施遭 BGP 劫持，恶意更新植入 root 后门](#item-3) ⭐️ 10.0/10
4. [长鑫存储开始试产 HBM3E](#item-4) ⭐️ 10.0/10
5. [小型 Transformer 在 1.5 小时内训练完成，在 ARC 基准测试中击败许多 LLM](#item-5) ⭐️ 9.0/10
6. [Python 3.15.0 候选版本 2 发布供测试](#item-6) ⭐️ 9.0/10
7. [Introducing wrapture](#item-7) ⭐️ 9.0/10
8. [Cloudflare 使用 Zstandard 和 Pingora 节省 PB 级缓存存储](#item-8) ⭐️ 9.0/10
9. [Kubernetes v1.37：默认启用存储版本迁移](#item-9) ⭐️ 9.0/10
10. [YOLO26-RGB：将深度训练的主干网络重新用于图像去雨](#item-10) ⭐️ 9.0/10
11. [2026 年潜在推理全景：映射 BDH-CQ、HRM/TRM、椰子\[D\]](#item-11) ⭐️ 9.0/10
12. [长鑫存储 LPDDR6 正式量产，国产高端移动内存实现全球首发，存储芯片国产化迎来里程碑突破 - 新浪财经](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布了 b10738 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b10738) ⭐️ 10.0/10

llama.cpp b10738 版本增加了对 SYCL 的支持，用于限制主机固定内存，并为 macOS、iOS 和 Linux 提供了新的二进制文件。

github · github-actions\[bot\] · 9月1日 22:40

**标签**: `#llama.cpp`, `#AI inference`, `#SYCL`, `#open-source`, `#machine-learning`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp 发布了 b10737 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b10737) ⭐️ 10.0/10

llama.cpp b10737 版本修复了 Qwen4exp、CUDA 稳定性以及序列状态管理方面的问题，并新增了相关测试。

github · github-actions\[bot\] · 9月1日 22:03

**标签**: `#llama.cpp`, `#AI inference`, `#CUDA`, `#software engineering`, `#bug fixes`

---

<a id="item-3"></a>
## [Virtualizor 更新设施遭 BGP 劫持，恶意更新植入 root 后门](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 10.0/10

Virtualizor 的更新基础设施在 2026 年 8 月 28 日至 30 日遭 BGP 路由劫持，攻击者凭有效 TLS 证书投递恶意更新包，植入 root 后门。 此次事件凸显了软件供应链安全的重大漏洞，表明攻击者可以通过劫持分发基础设施绕过代码层面的防御，这对所有依赖受影响平台用户构成严重风险。 经确认，此次攻击仅影响在劫持窗口期内更新的少量 hypervisor，独立取证显示恶意包会写入 root SSH 密钥、安装 Java 载荷并建立持久化服务。

telegram · zaihuapd · 9月1日 14:05

**背景**: BGP 劫持是一种网络攻击，攻击者通过宣告虚假的路由信息来转移流量，而 root 后门是一种隐蔽的恶意软件组件，可为系统提供未经授权的管理员访问权限。

**标签**: `#BGP Hijacking`, `#Supply Chain Security`, `#Rootkit`, `#Virtualization`, `#Infrastructure Security`

---

<a id="item-4"></a>
## [长鑫存储开始试产 HBM3E](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9HRkJCeFM3RFBUR1hueUdYeGF5bDlJNVN4cU5CSWd2bzdJLTh5OXFIRG9kX0VuSzcteTNWUXhyNVJqemNWMnpuM3N5UmVPM1JXdkNJ?oc=5) ⭐️ 10.0/10

长鑫存储已开始试产 HBM3E 高带宽内存，预计数周内将实现大规模量产。 HBM3E 对 AI 计算基础设施至关重要，能显著提升 AI 加速器和数据中心的性能和效率。 试产涉及先进的封装技术和 3D 堆叠 DRAM 技术，但尚未披露具体的带宽或引脚速度等技术参数。

google\_news · 电子工程专辑 · 9月1日 17:55

**背景**: 高带宽内存（HBM）是一种用于 AI 加速器的 3D 堆叠 SDRAM 技术，能提供比传统内存更高的带宽。最新的 HBM3E 每堆栈带宽高达 1180 GB/s，由 SK 海力士、三星和美光等主要制造商使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://blogs.sw.siemens.com/semiconductor-packaging/2026/04/24/hbm3e-hbm4-ic-design-guide/">HBM3e and HBM4: IC design guide for next-generation high ...</a></li>
<li><a href="https://www.micron.com/products/memory/hbm/hbm3e">HBM3E | Micron Technology Inc.</a></li>

</ul>
</details>

**标签**: `#HBM3E`, `#AI Compute`, `#Semiconductors`, `#Memory`, `#Chips`

---

<a id="item-5"></a>
## [小型 Transformer 在 1.5 小时内训练完成，在 ARC 基准测试中击败许多 LLM](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 9.0/10

一个在 1.5 小时内从头训练的小型 ARC Transformer 在 ARC 基准测试中表现出色，击败了许多通常需要巨大计算资源的大型语言模型。 这一结果挑战了处理复杂问题需要大规模 LLM 和训练成本的普遍假设，表明高效的架构和训练技术可以用更少的计算资源实现相当的结果。 该模型使用了现代架构改进，如 SwiGLU 激活函数和 RMS 归一化，以及增加数据多样性和打乱，在不使用测试标签训练的情况下实现了其性能。

hackernews · porridgeraisin · 9月1日 17:52 · [社区讨论](https://news.ycombinator.com/item?id=49519939)

**背景**: ARC（抽象推理语料库）是一个旨在测试 AI 在新颖任务上进行抽象推理和模式识别能力的基准测试，常用于评估 AI 系统的泛化能力。

**社区讨论**: 作者澄清这不是 LLM，而是从头训练的小型 Transformer，并回应了关于在评估谜题上训练的批评，强调 ARC 是一个元学习基准，从评估谜题中学习是预期的。

**标签**: `#transformer`, `#LLM`, `#AI compute`, `#ARC benchmark`, `#training efficiency`

---

<a id="item-6"></a>
## [Python 3.15.0 候选版本 2 发布供测试](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 9.0/10

Hugo van Kemenade 宣布了 Python 3.15.0 候选版本 2 的可用性，这是即将于 10 月发布的 Python 3.15.0 的第二个候选版本。 这个候选版本对 Python 生态系统具有重要意义，因为它标志着稳定发布前的最终测试阶段，允许开发人员识别并修复潜在问题。 发布经理强烈鼓励第三方项目的维护人员在 Python 3.15 上准备他们的项目，并在 PyPI 上发布 Python 3.15 的轮子，以确保与最终版本的兼容性。

rss · Simon Willison · 9月1日 22:59

**背景**: 候选版本是软件的准最终版本，旨在在正式稳定发布之前识别和修复错误。Python 3.15 是 Python 编程语言的下一个主要版本，紧随 3.14 之后。

**标签**: `#Python`, `#Software Development`, `#Release Candidate`, `#Developer Tools`, `#Python 3.15`

---

<a id="item-7"></a>
## [Introducing wrapture](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Simon Willison · 9月1日 07:59

**标签**: `#Python`, `#Testing`, `#Observability`, `#Tracing`, `#Monkeypatching`

---

<a id="item-8"></a>
## [Cloudflare 使用 Zstandard 和 Pingora 节省 PB 级缓存存储](https://blog.cloudflare.com/cache-transcoding/) ⭐️ 9.0/10

Cloudflare 原型测试了使用 Zstandard 压缩和 Pingora 来优化其基础设施内的缓存存储效率。 这种优化使 Cloudflare 能够在相同硬件上存储更多内容，直接影响存储成本和可扩展性。 该方法涉及使用基于 Rust 的代理 Pingora 将 Zstandard 压缩集成到缓存层中。

rss · Cloudflare Blog · 9月1日 20:59

**背景**: 缓存存储是 Cloudflare 等内容交付网络 \(CDN\) 的关键组件，用于全球内容分发。高效的存储可以减少硬件需求和运营成本。

**标签**: `#cache-optimization`, `#compression`, `#software-engineering`, `#performance`, `#cloud-native`

---

<a id="item-9"></a>
## [Kubernetes v1.37：默认启用存储版本迁移](https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/) ⭐️ 9.0/10

Kubernetes v1.37 正式版默认启用了存储版本迁移，以管理 API 资源架构的演进。

rss · Kubernetes Blog · 9月1日 02:30

**标签**: `#kubernetes`, `#software-engineering`, `#api-stability`, `#cloud-native`, `#devops`

---

<a id="item-10"></a>
## [YOLO26-RGB：将深度训练的主干网络重新用于图像去雨](https://www.reddit.com/r/MachineLearning/comments/1w4fxln/yolo26rgb_repurposing_yolo26s_depthtrained/) ⭐️ 9.0/10

作者将 YOLO26 的深度训练主干网络和颈部网络重新用于图像去雨，用新的 RGBHead 解码器替换了 1 通道的深度头，同时保持 CSPDarknet 主干网络和 PAN-FPN 颈部网络不变。 这项工作展示了深度估计模型的架构可迁移性，能够迁移到图像去雨等密集回归任务，为多任务学习的有效权重初始化策略提供了见解。 RGBHead 采用残差输出方式和 LayerNorm，而主干网络和颈部网络保留 BatchNorm；该模型在 ClearView 的混合合成+真实雨数据集上训练，并发布了 nano（5.25M）和 small（12.13M）两种规模。

reddit · r/MachineLearning · /u/Naive-Explanation940 · 9月1日 23:52

**背景**: YOLO26 是一个计算机视觉模型，包含一个在密集回归任务上训练的深度估计头；本文探讨了其主干网络学习到的特征是否可以有效地迁移到图像去雨等其他密集回归任务。

**标签**: `#machine-learning`, `#computer-vision`, `#model-transfer`, `#deep-learning`, `#deraining`

---

<a id="item-11"></a>
## [2026 年潜在推理全景：映射 BDH-CQ、HRM/TRM、椰子\[D\]](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 9.0/10

本文将潜在推理架构分为五个家族，重点介绍了 BDH-CQ（Engdahl 等人，2026 年），该架构在 ARC-AGI-1 上超越了以往的成本-精度帕累托前沿，同时保持了高达 600B 参数的潜在推理行为。 潜在推理代表了从 token 流限制的范式转变，通过超越语言化的思维链转向连续隐藏状态，可能实现更高效的 AGI 开发。 BDH-CQ 建立在 Dragon hatchling 架构之上，演示直接写入循环记忆，测试输入通过连续潜在空间中的迭代计算解决，其区别在于上下文获取方法。

reddit · r/MachineLearning · /u/Typical-Scene-5794 · 9月1日 23:14

**背景**: 思维链（CoT）方法会语言化推理步骤，但最近的研究表明它们可能产生逻辑缺陷或编造的步骤。潜在推理架构如 Coconut 和 CALM 则操作于连续隐藏状态或压缩向量，使得推理超越逐 token 生成，更加高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://towardsdatascience.com/coconut-a-framework-for-latent-reasoning-in-llms/">Coconut: A Framework for Latent Reasoning in LLMs | Towards Data Science</a></li>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a Continuous Latent Space</a></li>
<li><a href="https://arxiv.org/abs/2510.27688">[2510.27688] Continuous Autoregressive Language Models Continuous Autoregressive Language Models - arXiv.org GitHub - shaochenze/calm: Official implementation of ... Continuous Autoregressive Language Models - OpenReview GitHub - audreybonee/ContinuousAutoregressiveLM: Official ... Continuous Autoregressive Language Models Continuous Autoregressive Language Models | Chenze Shao</a></li>

</ul>
</details>

**标签**: `#latent reasoning`, `#AI architectures`, `#machine learning`, `#chain-of-thought`, `#AGI`

---

<a id="item-12"></a>
## [长鑫存储 LPDDR6 正式量产，国产高端移动内存实现全球首发，存储芯片国产化迎来里程碑突破 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTFBkZW9tMnB3eWp2bHdUX3FaWm82eW8ySjN0SzU4UVY3WHE0b2VodGhPZTBiS3pvNHc0dkNXRHU3bGswdnhkdC11ZVVmZXEwcjBuYXlyWkpFQ0NaaldGZzlReTlIQTdUd1FTZWw0djBja0xhUUFsTnEzei1tQk1Uc1E?oc=5) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

google\_news · 新浪财经 · 9月1日 20:01

**标签**: `#semiconductors`, `#memory`, `#LPDDR6`, `#China`, `#AI hardware`

---