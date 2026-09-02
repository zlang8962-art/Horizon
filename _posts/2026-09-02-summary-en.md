---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
content_date: 2026-09-01
lang: en
---

> Coverage: 2026-09-01 (Asia/Shanghai calendar day)

> From 109 items, 12 important content pieces were selected

---

1. [ggml-org/llama.cpp released b10738](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10737](#item-2) ⭐️ 10.0/10
3. [Virtualizor Update Infrastructure BGP Hijacked, Root Backdoor Injected](#item-3) ⭐️ 10.0/10
4. [ChangXin Memory Begins Mass Production Trials for HBM3E](#item-4) ⭐️ 10.0/10
5. [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC](#item-5) ⭐️ 9.0/10
6. [Python 3.15.0 Candidate 2 Released for Testing](#item-6) ⭐️ 9.0/10
7. [Introducing wrapture](#item-7) ⭐️ 9.0/10
8. [Cloudflare Saves Petabytes of Cache Storage with Zstandard and Pingora](#item-8) ⭐️ 9.0/10
9. [Kubernetes v1.37: Storage Version Migration Enabled by Default](#item-9) ⭐️ 9.0/10
10. [YOLO26-RGB: Repurposing Depth-Backbone for Image Deraining](#item-10) ⭐️ 9.0/10
11. [Latent Reasoning Landscape in 2026: Mapping BDH-CQ, HRM/TRM, Coconut \[D\]](#item-11) ⭐️ 9.0/10
12. [长鑫存储LPDDR6正式量产，国产高端移动内存实现全球首发，存储芯片国产化迎来里程碑突破 - 新浪财经](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10738](https://github.com/ggml-org/llama.cpp/releases/tag/b10738) ⭐️ 10.0/10

llama.cpp release b10738 adds SYCL support for host-pinned memory limits and provides new binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Sep 1, 22:40

**Tags**: `#llama.cpp`, `#AI inference`, `#SYCL`, `#open-source`, `#machine-learning`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10737](https://github.com/ggml-org/llama.cpp/releases/tag/b10737) ⭐️ 10.0/10

llama.cpp b10737 includes fixes for Qwen4exp, CUDA stability, and sequence state management with added tests.

github · github-actions\[bot\] · Sep 1, 22:03

**Tags**: `#llama.cpp`, `#AI inference`, `#CUDA`, `#software engineering`, `#bug fixes`

---

<a id="item-3"></a>
## [Virtualizor Update Infrastructure BGP Hijacked, Root Backdoor Injected](https://www.virtualizor.com/blog/security-incident-bgp-hijacking/) ⭐️ 10.0/10

Virtualizor&\#x27;s update infrastructure was compromised via BGP hijacking between August 28 and 30, 2026, allowing attackers to inject a malicious update that installed a root backdoor. This incident highlights a critical vulnerability in software supply chain security, demonstrating how attackers can bypass code-level defenses by compromising distribution infrastructure, which poses a severe risk to all users relying on the affected platform. The attack was confirmed to have affected only a small number of hypervisors that updated during the hijacking window, with independent forensics revealing the malicious package installed root SSH keys, a Java payload, and a persistent service.

telegram · zaihuapd · Sep 1, 14:05

**Background**: BGP hijacking is a network attack where an attacker announces false routing information to divert traffic, and a root backdoor is a stealthy malware component that provides unauthorized administrative access to a system.

**Tags**: `#BGP Hijacking`, `#Supply Chain Security`, `#Rootkit`, `#Virtualization`, `#Infrastructure Security`

---

<a id="item-4"></a>
## [ChangXin Memory Begins Mass Production Trials for HBM3E](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9HRkJCeFM3RFBUR1hueUdYeGF5bDlJNVN4cU5CSWd2bzdJLTh5OXFIRG9kX0VuSzcteTNWUXhyNVJqemNWMnpuM3N5UmVPM1JXdkNJ?oc=5) ⭐️ 10.0/10

ChangXin Memory Technologies has initiated mass production trials for HBM3E high-bandwidth memory, with potential large-scale production expected within weeks. HBM3E is critical for AI compute infrastructure, significantly improving performance and efficiency for AI accelerators and data centers. The trials involve advanced packaging and 3D-stacked DRAM technology, though specific technical parameters like bandwidth or pin speed are not yet disclosed.

google\_news · 电子工程专辑 · Sep 1, 17:55

**Background**: High Bandwidth Memory \(HBM\) is a 3D-stacked SDRAM technology used in AI accelerators to provide higher bandwidth than conventional memory. HBM3E, the latest generation, offers up to 1180 GB/s per stack and is used by major manufacturers like SK hynix, Samsung, and Micron.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://blogs.sw.siemens.com/semiconductor-packaging/2026/04/24/hbm3e-hbm4-ic-design-guide/">HBM3e and HBM4: IC design guide for next-generation high ...</a></li>
<li><a href="https://www.micron.com/products/memory/hbm/hbm3e">HBM3E | Micron Technology Inc.</a></li>

</ul>
</details>

**Tags**: `#HBM3E`, `#AI Compute`, `#Semiconductors`, `#Memory`, `#Chips`

---

<a id="item-5"></a>
## [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 9.0/10

A small ARC transformer trained from scratch in 1.5 hours achieved high performance on the ARC benchmark, outperforming many large language models that typically require enormous compute resources. This result challenges the prevailing assumption that tackling complex problems requires massive LLMs and training costs, suggesting that efficient architectures and training techniques can achieve comparable results with far less compute. The model used modern architectural improvements like SwiGLU activation functions and RMS normalization, along with increased data diversity and shuffling, to achieve its performance without training on test labels.

hackernews · porridgeraisin · Sep 1, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49519939)

**Background**: ARC \(Abstraction and Reasoning Corpus\) is a benchmark designed to test AI&\#x27;s ability to perform abstract reasoning and pattern recognition on novel tasks, often used to evaluate the generalization capabilities of AI systems.

**Discussion**: The author clarified that this is not an LLM but a small transformer trained from scratch, and addressed criticisms about training on eval puzzles, emphasizing that ARC is a metalearning benchmark where learning from eval puzzles is intended.

**Tags**: `#transformer`, `#LLM`, `#AI compute`, `#ARC benchmark`, `#training efficiency`

---

<a id="item-6"></a>
## [Python 3.15.0 Candidate 2 Released for Testing](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 9.0/10

Hugo van Kemenade announced the availability of Python 3.15.0 candidate 2, the second release candidate for the upcoming Python 3.15.0 release scheduled for October. This release candidate is significant for the Python ecosystem as it marks the final testing phase before the stable release, allowing developers to identify and fix potential issues. The release manager strongly encourages maintainers of third-party projects to prepare their projects for Python 3.15 and publish Python 3.15 wheels on PyPI to ensure compatibility with the final release.

rss · Simon Willison · Sep 1, 22:59

**Background**: Release candidates are near-final versions of software intended to identify and fix bugs before the official stable release. Python 3.15 is the next major version of the Python programming language, following 3.14.

**Tags**: `#Python`, `#Software Development`, `#Release Candidate`, `#Developer Tools`, `#Python 3.15`

---

<a id="item-7"></a>
## [Introducing wrapture](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 9.0/10

Wrapture is a Python library for wrapping functions to trace and override behavior, useful for testing and observability.

rss · Simon Willison · Sep 1, 07:59

**Tags**: `#Python`, `#Testing`, `#Observability`, `#Tracing`, `#Monkeypatching`

---

<a id="item-8"></a>
## [Cloudflare Saves Petabytes of Cache Storage with Zstandard and Pingora](https://blog.cloudflare.com/cache-transcoding/) ⭐️ 9.0/10

Cloudflare prototyped using Zstandard compression and Pingora to optimize cache storage efficiency within their infrastructure. This optimization allows Cloudflare to store more content with the same hardware, directly impacting storage costs and scalability. The approach involves integrating Zstandard compression into the cache layer using Pingora, a Rust-based proxy.

rss · Cloudflare Blog · Sep 1, 20:59

**Background**: Cache storage is a critical component of content delivery networks \(CDNs\) like Cloudflare, which serve content globally. Efficient storage reduces hardware needs and operational costs.

**Tags**: `#cache-optimization`, `#compression`, `#software-engineering`, `#performance`, `#cloud-native`

---

<a id="item-9"></a>
## [Kubernetes v1.37: Storage Version Migration Enabled by Default](https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/) ⭐️ 9.0/10

Kubernetes v1.37 GA enables storage version migration by default to manage API resource schema evolution.

rss · Kubernetes Blog · Sep 1, 02:30

**Tags**: `#kubernetes`, `#software-engineering`, `#api-stability`, `#cloud-native`, `#devops`

---

<a id="item-10"></a>
## [YOLO26-RGB: Repurposing Depth-Backbone for Image Deraining](https://www.reddit.com/r/MachineLearning/comments/1w4fxln/yolo26rgb_repurposing_yolo26s_depthtrained/) ⭐️ 9.0/10

The author repurposed the depth-trained backbone and neck of YOLO26 for image deraining, replacing the 1-channel depth head with a new RGBHead decoder while keeping the CSPDarknet backbone and PAN-FPN neck unchanged. This work demonstrates the architectural transferability of a depth-estimation model to a dense-regression task like image restoration, offering insights into effective weight initialization strategies for multi-task learning. The RGBHead uses a residual output style and LayerNorm, while the backbone and neck retain BatchNorm; the model was trained on ClearView&\#x27;s mixed synthetic+real rain dataset and released in nano \(5.25M\) and small \(12.13M\) scales.

reddit · r/MachineLearning · /u/Naive-Explanation940 · Sep 1, 23:52

**Background**: YOLO26 is a computer vision model that includes a depth-estimation head trained on a dense-regression task; this post explores whether the features learned by its backbone can be effectively transferred to a different dense-regression task like image deraining.

**Tags**: `#machine-learning`, `#computer-vision`, `#model-transfer`, `#deep-learning`, `#deraining`

---

<a id="item-11"></a>
## [Latent Reasoning Landscape in 2026: Mapping BDH-CQ, HRM/TRM, Coconut \[D\]](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 9.0/10

This post categorizes five families of latent reasoning architectures, highlighting BDH-CQ \(Engdahl et al., 2026\) as a breakthrough that surpasses previous cost-accuracy Pareto frontiers on ARC-AGI-1 while maintaining latent reasoning behavior up to 600B parameters. Latent reasoning represents a paradigm shift from token-stream limitations, potentially enabling more efficient AGI development by moving beyond verbalized chain-of-thought to continuous hidden states. BDH-CQ builds on the Dragon hatchling architecture, where demonstrations write directly into a recurrent memory and test inputs are solved via iterative computation in a continuous latent space, distinguishing it by its in-context acquisition method.

reddit · r/MachineLearning · /u/Typical-Scene-5794 · Sep 1, 23:14

**Background**: Chain-of-thought \(CoT\) methods verbalize reasoning steps, but recent research shows they can produce logically flawed or fabricated steps. Latent reasoning architectures like Coconut and CALM instead operate on continuous hidden states or compressed vectors, enabling more efficient reasoning beyond token-by-token generation.

<details><summary>References</summary>
<ul>
<li><a href="https://towardsdatascience.com/coconut-a-framework-for-latent-reasoning-in-llms/">Coconut: A Framework for Latent Reasoning in LLMs | Towards Data Science</a></li>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a Continuous Latent Space</a></li>
<li><a href="https://arxiv.org/abs/2510.27688">[2510.27688] Continuous Autoregressive Language Models Continuous Autoregressive Language Models - arXiv.org GitHub - shaochenze/calm: Official implementation of ... Continuous Autoregressive Language Models - OpenReview GitHub - audreybonee/ContinuousAutoregressiveLM: Official ... Continuous Autoregressive Language Models Continuous Autoregressive Language Models | Chenze Shao</a></li>

</ul>
</details>

**Tags**: `#latent reasoning`, `#AI architectures`, `#machine learning`, `#chain-of-thought`, `#AGI`

---

<a id="item-12"></a>
## [长鑫存储LPDDR6正式量产，国产高端移动内存实现全球首发，存储芯片国产化迎来里程碑突破 - 新浪财经](https://news.google.com/rss/articles/CBMif0FVX3lxTFBkZW9tMnB3eWp2bHdUX3FaWm82eW8ySjN0SzU4UVY3WHE0b2VodGhPZTBiS3pvNHc0dkNXRHU3bGswdnhkdC11ZVVmZXEwcjBuYXlyWkpFQ0NaaldGZzlReTlIQTdUd1FTZWw0djBja0xhUUFsTnEzei1tQk1Uc1E?oc=5) ⭐️ 9.0/10

长鑫存储宣布LPDDR6内存正式量产，标志着国产存储芯片在高端移动内存领域实现全球首发。

google\_news · 新浪财经 · Sep 1, 20:01

**Tags**: `#semiconductors`, `#memory`, `#LPDDR6`, `#China`, `#AI hardware`

---