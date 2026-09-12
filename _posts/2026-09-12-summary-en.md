---
layout: default
title: "Horizon Summary: 2026-09-12 (EN)"
date: 2026-09-12
content_date: 2026-09-11
lang: en
---

> Coverage: 2026-09-11 (Asia/Shanghai calendar day)

> From 84 items, 12 important content pieces were selected

---

1. [llama.cpp b10906 fixes server speculation and refactors draft parameters](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10902](#item-2) ⭐️ 10.0/10
3. [Kubernetes v1.37: Scheduler Preemption for In-Place Pod Resize \(Alpha\)](#item-3) ⭐️ 10.0/10
4. [Training 210M DiT from Scratch: Novel Attention and Loss Observations](#item-4) ⭐️ 10.0/10
5. [GitLab 修复 CVSS 10.0 漏洞：自建实例或遭未授权读取服务器文件](#item-5) ⭐️ 10.0/10
6. [microsoft/onnxruntime released v1.30.0](#item-6) ⭐️ 9.0/10
7. [Don&\#x27;t sleep on wrapture](#item-7) ⭐️ 9.0/10
8. [github-to-sqlite 2.9.1 Fixes sqlite-utils 4.x Compatibility](#item-8) ⭐️ 9.0/10
9. [Introducing automatic remediation policies with Cloudflare CASB](#item-9) ⭐️ 9.0/10
10. [GitHub Copilot App for Beginners: Using Diff, Terminal, and Browser](#item-10) ⭐️ 9.0/10
11. [Kimi Code 上线 K2.8 Preview，性能接近 K3](#item-11) ⭐️ 9.0/10
12. [ChangXin Memory Starts HBM3 Trial Production](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10906 fixes server speculation and refactors draft parameters](https://github.com/ggml-org/llama.cpp/releases/tag/b10906) ⭐️ 10.0/10

llama.cpp version b10906 fixes a server speculation bug that occurred after processing an image and refactors the draft parameters to clarify their role as positions rather than token counts. This fix is critical for maintaining the integrity of speculative decoding, a technique used to accelerate LLM inference, and ensures that the server correctly tracks token positions across different contexts. The fix affects all drafters, including DFlash, and involves renaming the parameter &\#x27;n\_past&\#x27; to &\#x27;pos0&\#x27; to avoid confusion with token count semantics. The release also provides reproducible binaries for macOS, Linux, Android, and Windows with support for various hardware backends like CUDA, Vulkan, and ROCm.

github · github-actions\[bot\] · Sep 11, 18:40

**Background**: Speculative decoding is a lossless inference optimization technique that uses a smaller &\#x27;draft&\#x27; model to propose tokens, which are then verified by a larger base model. In llama.cpp, the &\#x27;drafter&\#x27; component implements this mechanism, and the &\#x27;n\_past&\#x27; parameter typically tracks the number of tokens generated so far.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/speculators">GitHub - vllm-project/speculators: A unified library for building, evaluating, and storing speculative decoding algorithms for LLM inference in vLLM · GitHub</a></li>
<li><a href="https://arxiv.org/html/2411.01076v4">When Speculation Spills Secrets: Side Channels via Speculative Decoding in LLMs</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#open-source`, `#inference`, `#bug-fix`, `#server`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10902](https://github.com/ggml-org/llama.cpp/releases/tag/b10902) ⭐️ 10.0/10

llama.cpp release b10902 adds OpenCL A8 Q4\_0 mm binary kernel support and provides cross-platform binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Sep 11, 13:53

**Tags**: `#llama.cpp`, `#OpenCL`, `#AI inference`, `#Cross-platform`, `#Open-source`

---

<a id="item-3"></a>
## [Kubernetes v1.37: Scheduler Preemption for In-Place Pod Resize \(Alpha\)](https://kubernetes.io/blog/2026/09/10/kubernetes-v1-37-scheduler-preemption-for-in-place-pod-resize-alpha/) ⭐️ 10.0/10

Kubernetes v1.37 introduces scheduler preemption for in-place Pod resize as an Alpha feature, controlled by the InPlacePodVerticalScalingSchedulerPreemption feature gate. This feature addresses a critical scheduling gap introduced by in-place Pod resizing, allowing higher-priority workloads to preempt lower-priority ones to free up resources, which is essential for maintaining application stability and efficiency in production clusters. The scheduler is now aware of deferred resize requests on running Pods and can actively preempt lower-priority Pods to make room for the higher-priority in-place resizes, unlike the previous behavior where requests were indefinitely deferred.

rss · Kubernetes Blog · Sep 11, 02:30

**Background**: In-place Pod resize, graduated to GA in v1.35, allows dynamic adjustment of CPU and memory allocations without disrupting applications. However, if a running Pod&\#x27;s scale-up request exceeds the node&\#x27;s capacity, the Kubelet marks it as &\#x27;Deferred&\#x27;, and the scheduler previously lacked the context to intervene.

<details><summary>References</summary>
<ul>
<li><a href="https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/">Pod Priority and Preemption | Kubernetes</a></li>
<li><a href="https://kubernetes.io/docs/concepts/scheduling-eviction/">Scheduling, Preemption and Eviction | Kubernetes</a></li>

</ul>
</details>

**Tags**: `#Kubernetes`, `#Scheduler`, `#Resource Management`, `#DevOps`, `#Cloud Native`

---

<a id="item-4"></a>
## [Training 210M DiT from Scratch: Novel Attention and Loss Observations](https://www.reddit.com/r/MachineLearning/comments/1wdfmvq/training_a_210m_texttoimage_dit_from_scratch_on/) ⭐️ 10.0/10

The author trained a 210M-parameter text-to-image diffusion transformer from scratch in 3.5 days on a single RTX PRO 6000 GPU, revealing three novel measurements: learned null attention slots become the dominant sink, flow-matching loss acts as a health signal rather than quality signal, and a training-time timestep shift outperforms doubling steps. This technical report provides reproducible measurements and trade-offs for practitioners, offering concrete insights into attention mechanisms and loss dynamics that can inform future model training strategies and hardware utilization. The model uses 16 register tokens plus 2 learned key/value slots in cross-attention, where the slots receive ~90% of attention mass by mid-training; flow-matching loss stayed equal to held-out loss to three decimals while held-out FID improved from 33.7 to 27.0.

reddit · r/MachineLearning · /u/IvanMikhnenkov · Sep 11, 21:00

**Background**: Diffusion Transformers \(DiTs\) combine transformer architectures with diffusion processes to generate images by gradually denoising latent representations. Register tokens are auxiliary tokens that help stabilize attention mechanisms by absorbing high-norm artifacts and providing explicit sink behavior, similar to sink tokens in language models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2412.12391v1">Efficient Scaling of Diffusion Transformers for Text-to-Image Generation</a></li>
<li><a href="https://arxiv.org/abs/2412.12391">Efficient Scaling of Diffusion Transformers for Text-to-Image Generation</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/diffusion-transformers-dits/">Diffusion Transformers (DiTs) - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#diffusion-models`, `#transformers`, `#training`, `#hardware`, `#practical-value`

---

<a id="item-5"></a>
## [GitLab 修复 CVSS 10.0 漏洞：自建实例或遭未授权读取服务器文件](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-3-2-released/) ⭐️ 10.0/10

GitLab released critical patches to fix a severe CVSS 10.0 vulnerability allowing unauthenticated users to read arbitrary server files.

telegram · zaihuapd · Sep 11, 19:05

**Tags**: `#GitLab`, `#Security Vulnerability`, `#Patch Release`, `#CVSS 10.0`, `#Self-hosted`

---

<a id="item-6"></a>
## [microsoft/onnxruntime released v1.30.0](https://github.com/microsoft/onnxruntime/releases/tag/v1.30.0) ⭐️ 9.0/10

ONNX Runtime 1.30.0 enhances generative AI inference with CUDA, WebGPU, and CPU improvements, plus new Go bindings.

github · tianleiwu · Sep 11, 00:55

**Tags**: `#AI inference`, `#ONNX Runtime`, `#generative AI`, `#performance optimization`, `#Go bindings`

---

<a id="item-7"></a>
## [Don&\#x27;t sleep on wrapture](https://simonwillison.net/2026/Sep/11/wrapture/) ⭐️ 9.0/10

A new Python monkey patching library called wrapture is gaining traction for its utility in testing and observability.

rss · Simon Willison · Sep 11, 21:51

**Tags**: `#Python`, `#Software Engineering`, `#Monkey Patching`, `#Testing`, `#Observability`

---

<a id="item-8"></a>
## [github-to-sqlite 2.9.1 Fixes sqlite-utils 4.x Compatibility](https://simonwillison.net/2026/Sep/11/github-to-sqlite/) ⭐️ 9.0/10

The github-to-sqlite 2.9.1 release specifically addresses and resolves a compatibility issue with sqlite-utils version 4.x. This fix is crucial for developers who rely on both tools to manage and analyze GitHub data, ensuring their workflows remain uninterrupted. The release notes reference issue \#85, confirming that the compatibility problem has been identified and addressed in this minor update.

rss · Simon Willison · Sep 11, 08:28

**Background**: github-to-sqlite is a Python tool designed to convert GitHub data into SQLite databases, while sqlite-utils is a companion library that enhances SQLite functionality. Both are popular open-source utilities in the developer ecosystem.

**Tags**: `#sqlite`, `#github`, `#developer-tools`, `#open-source`, `#database`

---

<a id="item-9"></a>
## [Introducing automatic remediation policies with Cloudflare CASB](https://blog.cloudflare.com/casb-policies/) ⭐️ 9.0/10

Cloudflare CASB introduces an automation engine to automatically remediate SaaS risks through event-driven logic.

rss · Cloudflare Blog · Sep 11, 21:00

**Tags**: `#Cloudflare`, `#CASB`, `#Security Automation`, `#SaaS Security`, `#DevOps`

---

<a id="item-10"></a>
## [GitHub Copilot App for Beginners: Using Diff, Terminal, and Browser](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/) ⭐️ 9.0/10

GitHub has released a new Copilot app that allows beginners to manage AI-generated code by viewing diffs, running terminal commands, and previewing web apps side by side. This app streamlines the AI coding workflow by integrating essential tools into a unified interface, improving developer productivity and reducing context switching. The diff panel highlights additions in green and deletions in red, while the app provides a unified workspace for repositories, coding sessions, and issues.

rss · GitHub Blog · Sep 11, 05:31

**Background**: GitHub Copilot is an AI coding assistant that provides code suggestions directly in the editor. The new desktop app consolidates features from the web, CLI, and IDEs into a single interface.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/">GitHub Copilot app for Beginners: Using the diff, terminal, and browser - The GitHub Blog</a></li>
<li><a href="https://github.com/features/copilot">GitHub Copilot · Your AI coding agent · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/GitHub">GitHub - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#AI Tools`, `#Developer Experience`, `#Code Review`, `#Productivity`

---

<a id="item-11"></a>
## [Kimi Code 上线 K2.8 Preview，性能接近 K3](https://www.kimi.com/code/docs/kimi-code/whats-new.html) ⭐️ 9.0/10

Kimi Code releases K2.8 Preview with K3-level performance, 1M context, and enhanced safety features.

telegram · zaihuapd · Sep 11, 17:00

**Tags**: `#AI Model`, `#Code Assistant`, `#Long Context`, `#Software Development`, `#Safety Features`

---

<a id="item-12"></a>
## [ChangXin Memory Starts HBM3 Trial Production](https://news.google.com/rss/articles/CBMiTkFVX3lxTE5VeDEtemlwbHdOZjBteWwxR3VCM214Y212N0dGdDlzVVh2VXlWSngwWlpvQXVpWUNBcVdTb3hBTTJXekR2WFhjS0JpMkl2dw?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies has reportedly initiated trial production of its fourth-generation High Bandwidth Memory \(HBM3\). HBM3 is a critical component for AI accelerators, and ChangXin&\#x27;s entry into this market strengthens China&\#x27;s semiconductor capabilities. The news focuses on the start of trial production, though specific technical specifications or yield rates are not detailed in the provided content.

google\_news · 观点网 · Sep 11, 11:17

**Background**: High Bandwidth Memory \(HBM\) is a 3D-stacked SDRAM technology designed for extreme speed, used in AI GPUs. HBM3 is an advanced iteration offering higher bandwidth and capacity than earlier versions.

<details><summary>References</summary>
<ul>
<li><a href="https://theaicipher.com/hbm-high-bandwidth-memory-explained/">HBM Explained : The Memory Bottleneck Behind Every AI GPU</a></li>
<li><a href="https://www.mexc.com/learn/article/what-is-hbm-why-high-bandwidth-memory-matters-for-ai-stocks/1">What Is HBM? Why High-Bandwidth Memory Matters for AI Stocks</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#HBM3`, `#AI memory`, `#semiconductors`, `#memory technology`, `#AI accelerators`

---