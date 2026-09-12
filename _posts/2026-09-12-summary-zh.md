---
layout: default
title: "Horizon Summary: 2026-09-12 (ZH)"
date: 2026-09-12
content_date: 2026-09-11
lang: zh
---

> 报道范围：2026-09-11（Asia/Shanghai 自然日）

> 从 84 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp b10906 修复服务器推测并重构草稿参数](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10902](#item-2) ⭐️ 10.0/10
3. [Kubernetes v1.37：用于原地 Pod 调整大小的调度器抢占功能（Alpha 版）](#item-3) ⭐️ 10.0/10
4. [从头训练 210M DiT：关于注意力和损失的全新观察](#item-4) ⭐️ 10.0/10
5. [GitLab 修复 CVSS 10.0 漏洞：自建实例或遭未授权读取服务器文件](#item-5) ⭐️ 10.0/10
6. [microsoft/onnxruntime released v1.30.0](#item-6) ⭐️ 9.0/10
7. [不要忽视 wrapture](#item-7) ⭐️ 9.0/10
8. [github-to-sqlite 2.9.1 修复 sqlite-utils 4.x 兼容性问题](#item-8) ⭐️ 9.0/10
9. [Introducing automatic remediation policies with Cloudflare CASB](#item-9) ⭐️ 9.0/10
10. [GitHub Copilot 初学者指南：使用 Diff、终端和浏览器](#item-10) ⭐️ 9.0/10
11. [Kimi Code 上线 K2.8 Preview，性能接近 K3](#item-11) ⭐️ 9.0/10
12. [长鑫存储启动第四代 HBM3 试产](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10906 修复服务器推测并重构草稿参数](https://github.com/ggml-org/llama.cpp/releases/tag/b10906) ⭐️ 10.0/10

llama.cpp 版本 b10906 修复了在处理图像后发生的服务器推测错误，并重构了草稿参数，以阐明它们作为位置而非令牌计数的作用。 此修复对于维护推测解码的完整性至关重要，推测解码是一种用于加速 LLM 推理的技术，并确保服务器在不同上下文中正确跟踪令牌位置。 该修复影响所有草稿器，包括 DFlash，并涉及将参数 &\#x27;n\_past&\#x27; 重命名为 &\#x27;pos0&\#x27; 以避免与令牌计数语义混淆。该版本还提供了适用于 macOS、Linux、Android 和 Windows 的可重现二进制文件，并支持各种硬件后端，如 CUDA、Vulkan 和 ROCm。

github · github-actions\[bot\] · 9月11日 18:40

**背景**: 推测解码是一种无损推理优化技术，它使用较小的“草稿”模型来提议令牌，然后由较大的基础模型进行验证。在 llama.cpp 中，“草稿器”组件实现了这种机制，而“n\_past”参数通常跟踪迄今为止生成的令牌数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/speculators">GitHub - vllm-project/speculators: A unified library for building, evaluating, and storing speculative decoding algorithms for LLM inference in vLLM · GitHub</a></li>
<li><a href="https://arxiv.org/html/2411.01076v4">When Speculation Spills Secrets: Side Channels via Speculative Decoding in LLMs</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#open-source`, `#inference`, `#bug-fix`, `#server`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10902](https://github.com/ggml-org/llama.cpp/releases/tag/b10902) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 9月11日 13:53

**标签**: `#llama.cpp`, `#OpenCL`, `#AI inference`, `#Cross-platform`, `#Open-source`

---

<a id="item-3"></a>
## [Kubernetes v1.37：用于原地 Pod 调整大小的调度器抢占功能（Alpha 版）](https://kubernetes.io/blog/2026/09/10/kubernetes-v1-37-scheduler-preemption-for-in-place-pod-resize-alpha/) ⭐️ 10.0/10

Kubernetes v1.37 引入了用于原地 Pod 调整大小的调度器抢占功能，这是一个 Alpha 特性，由 InPlacePodVerticalScalingSchedulerPreemption 功能门控制。 该功能解决了原地 Pod 调整大小引入的一个关键调度缺口，允许高优先级工作负载抢占低优先级工作负载以释放资源，这对于在生产集群中维护应用程序的稳定性和效率至关重要。 调度器现在可以感知运行中 Pod 的延迟调整大小请求，并可以主动抢占低优先级 Pod，以为高优先级原地调整大小腾出空间，这与之前请求无限期延迟的行为不同。

rss · Kubernetes Blog · 9月11日 02:30

**背景**: 原地 Pod 调整大小功能于 v1.35 毕业，允许在不中断应用程序的情况下动态调整 CPU 和内存分配。然而，如果运行中 Pod 的扩展请求超过节点容量，Kubelet 会将其标记为“延迟”，而调度器之前缺乏干预的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/">Pod Priority and Preemption | Kubernetes</a></li>
<li><a href="https://kubernetes.io/docs/concepts/scheduling-eviction/">Scheduling, Preemption and Eviction | Kubernetes</a></li>

</ul>
</details>

**标签**: `#Kubernetes`, `#Scheduler`, `#Resource Management`, `#DevOps`, `#Cloud Native`

---

<a id="item-4"></a>
## [从头训练 210M DiT：关于注意力和损失的全新观察](https://www.reddit.com/r/MachineLearning/comments/1wdfmvq/training_a_210m_texttoimage_dit_from_scratch_on/) ⭐️ 10.0/10

作者在单张 RTX PRO 6000 GPU 上用 3.5 天从头训练了一个 2.1 亿参数的文本到图像扩散 Transformer，揭示了三个新测量结果：学习到的空注意力槽成为主导的汇点，流匹配损失充当健康信号而非质量信号，训练时的步长偏移优于翻倍步数。 这份技术报告为从业者提供了可复现的测量结果和权衡，为未来的模型训练策略和硬件利用提供了具体的见解。 该模型在交叉注意力中使用 16 个注册令牌加上 2 个学习到的键/值槽，其中槽在训练中期接收约 90% 的注意力质量；流匹配损失与保留损失保持三位小数一致，同时保留的 FID 从 33.7 提升到 27.0。

reddit · r/MachineLearning · /u/IvanMikhnenkov · 9月11日 21:00

**背景**: 扩散 Transformer \(DiT\) 将 Transformer 架构与扩散过程相结合，通过逐渐去噪潜在表示来生成图像。注册令牌是辅助令牌，通过吸收高范数伪影并提供明确的汇点行为来帮助稳定注意力机制，类似于语言模型中的汇点令牌。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2412.12391v1">Efficient Scaling of Diffusion Transformers for Text-to-Image Generation</a></li>
<li><a href="https://arxiv.org/abs/2412.12391">Efficient Scaling of Diffusion Transformers for Text-to-Image Generation</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/diffusion-transformers-dits/">Diffusion Transformers (DiTs) - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#diffusion-models`, `#transformers`, `#training`, `#hardware`, `#practical-value`

---

<a id="item-5"></a>
## [GitLab 修复 CVSS 10.0 漏洞：自建实例或遭未授权读取服务器文件](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) ⭐️ 10.0/10

GitLab 发布了关键补丁，以修复一个严重的 CVSS 10.0 漏洞，该漏洞允许未认证的用户读取任意服务器文件。

telegram · zaihuapd · 9月11日 19:05

**标签**: `#GitLab`, `#Security Vulnerability`, `#Patch Release`, `#CVSS 10.0`, `#Self-hosted`

---

<a id="item-6"></a>
## [microsoft/onnxruntime released v1.30.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.0) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · tianleiwu · 9月11日 00:55

**标签**: `#AI inference`, `#ONNX Runtime`, `#generative AI`, `#performance optimization`, `#Go bindings`

---

<a id="item-7"></a>
## [不要忽视 wrapture](https://simonwillison.net/2026/Sep/11/wrapture/) ⭐️ 9.0/10

一个新的 Python monkey patching 库 wrapture 正在获得关注，因为它在测试和可观测性方面非常有用。

rss · Simon Willison · 9月11日 21:51

**标签**: `#Python`, `#Software Engineering`, `#Monkey Patching`, `#Testing`, `#Observability`

---

<a id="item-8"></a>
## [github-to-sqlite 2.9.1 修复 sqlite-utils 4.x 兼容性问题](https://simonwillison.net/2026/Sep/11/github-to-sqlite/) ⭐️ 9.0/10

github-to-sqlite 2.9.1 版本专门解决并修复了与 sqlite-utils 4.x 版本的兼容性问题。 此修复对于依赖这两个工具来管理和分析 GitHub 数据的开发者至关重要，确保他们的工作流程保持连续性。 发布说明引用了问题 \#85，确认该兼容性问题已在此次次要更新中得到识别和解决。

rss · Simon Willison · 9月11日 08:28

**背景**: github-to-sqlite 是一个用于将 GitHub 数据转换为 SQLite 数据库的 Python 工具，而 sqlite-utils 则是一个增强 SQLite 功能的配套库。两者都是开发者生态系统中流行的开源实用程序。

**标签**: `#sqlite`, `#github`, `#developer-tools`, `#open-source`, `#database`

---

<a id="item-9"></a>
## [Introducing automatic remediation policies with Cloudflare CASB](https://blog.cloudflare.com/casb-policies/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Cloudflare Blog · 9月11日 21:00

**标签**: `#Cloudflare`, `#CASB`, `#Security Automation`, `#SaaS Security`, `#DevOps`

---

<a id="item-10"></a>
## [GitHub Copilot 初学者指南：使用 Diff、终端和浏览器](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/) ⭐️ 9.0/10

GitHub 推出了一款新的 Copilot 应用，允许初学者通过并排查看 Diff、运行终端命令和预览 Web 应用来管理 AI 生成的代码。 该应用通过将必要工具集成到统一界面中，简化了 AI 编码工作流程，提高了开发者的生产力并减少了上下文切换。 Diff 面板以绿色高亮显示添加内容，以红色高亮显示删除内容，而该应用为仓库、编码会话和问题提供了一个统一的工作空间。

rss · GitHub Blog · 9月11日 05:31

**背景**: GitHub Copilot 是一个直接在编辑器中提供代码建议的 AI 编码助手。新的桌面应用将 Web、CLI 和 IDE 的功能整合到一个界面中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/">GitHub Copilot app for Beginners: Using the diff, terminal, and browser - The GitHub Blog</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI coding agent · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/GitHub">GitHub - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#AI Tools`, `#Developer Experience`, `#Code Review`, `#Productivity`

---

<a id="item-11"></a>
## [Kimi Code 上线 K2.8 Preview，性能接近 K3](https://www.kimi.com/code/docs/kimi-code/whats-new.html) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

telegram · zaihuapd · 9月11日 17:00

**标签**: `#AI Model`, `#Code Assistant`, `#Long Context`, `#Software Development`, `#Safety Features`

---

<a id="item-12"></a>
## [长鑫存储启动第四代 HBM3 试产](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5VeDEtemlwbHdOZjBteWwxR3VCM214Y212N0dGdDlzVVh2VXlWSngwWlpvQXVpWUNBcVdTb3hBTTJXekR2WFhjS0JpMkl2dw?oc=5) ⭐️ 9.0/10

长鑫存储据报已启动第四代高带宽内存（HBM3）的试产。 HBM3 是 AI 加速器的关键组件，长鑫进入这一市场将增强中国的半导体能力。 该新闻重点在于试产的启动，但提供的内容中没有详细说明具体的技术规格或良率。

google\_news · 观点网 · 9月11日 11:17

**背景**: 高带宽内存（HBM）是一种为极致速度而设计的 3D 堆叠 SDRAM 技术，用于 AI GPU。HBM3 是比早期版本具有更高带宽和容量的先进迭代产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theaicipher.com/hbm-high-bandwidth-memory-explained/">HBM Explained : The Memory Bottleneck Behind Every AI GPU</a></li>
<li><a href="https://www.mexc.com/learn/article/what-is-hbm-why-high-bandwidth-memory-matters-for-ai-stocks/1">What Is HBM? Why High-Bandwidth Memory Matters for AI Stocks</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#HBM3`, `#AI memory`, `#semiconductors`, `#memory technology`, `#AI accelerators`

---