---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 28 条内容中筛选出 2 条重要资讯。

---

1. [vLLM v0.26.0 发布：支持 Inkling 模型并优化 DeepSeek-V4 性能](#item-1) ⭐️ 8.0/10
2. [SGLang v0.5.16 新增 DSPark 推测解码与 Inkling 975B MoE 模型支持](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 发布：支持 Inkling 模型并优化 DeepSeek-V4 性能](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 新增了对 Inkling 模型家族的完整支持，针对 NVIDIA、AMD 和 Intel XPU 硬件进行了 DeepSeek-V4 性能优化，改进了 fp32 lm\_head，并支持按 KV-cache 组灵活选择注意力后端。本次发布包含来自 212 位贡献者的 411 次提交，新增模型支持、推测解码增强以及成熟的 KV 卸载功能。 作为关键的 LLM 推理引擎，vLLM 在多个硬件厂商上的性能优化以及对 Inkling 和 DeepSeek-V4 等新兴模型的支持，直接影响 AI 服务的部署效率。注意力后端和 KV 卸载方面的架构改进为生产环境提供了更灵活、可扩展的推理解决方案。 DeepSeek-V4 优化包括专用路由内核实现 2.94% E2E TPOT 改进、fused\_topk\_bias 实现 1.5-2 倍内核加速，以及在 AMD 和 XPU 上支持 DSpark 推测解码。Inkling 模型家族获得全面支持，包括 Hopper FA4 相对注意力、MTP=1 推测解码、LoRA 和 ModelOpt NVFP4 量化。Rust 前端现在支持多模态视频和音频输入。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个高吞吐量、内存高效的大语言模型推理引擎，实现了用于高效 KV-cache 管理的 PagedAttention。推测解码是一种推理加速技术，使用较小的草稿模型提议 token，然后由目标模型并行验证。Inkling 模型是 Thinking Machines Lab 开发的 1 万亿参数多模态模型，可原生处理文本、图像和音频输入，上下文长度可达 100 万。DSpark 是一个置信度调度的推测解码框架，解决了并行草稿生成中的接受率衰减问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance</a></li>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative ...</a></li>
<li><a href="https://www.marktechpost.com/2026/06/27/deepseek-releases-dspark-a-speculative-decoding-framework-that-accelerates-deepseek-v4-per-user-generation-60-85-over-mtp-1/">DeepSeek Releases DSpark, a Speculative Decoding Framework ...</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM-inference`, `#GPU-optimization`, `#speculative-decoding`, `#AI-infrastructure`

---

<a id="item-2"></a>
## [SGLang v0.5.16 新增 DSPark 推测解码与 Inkling 975B MoE 模型支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 推出了 DSPark，一种基于置信度的推测解码算法，可根据草稿置信度动态调整验证窗口大小，在 Blackwell B300 GPU 上以 TP8 部署 DeepSeek-V4-Pro 时达到 383.7 tok/s。该版本还新增了对 Inkling 的 Day-0 支持，这是一个拥有 975B 参数、1M token 上下文的多模态 MoE 模型，采用混合注意力机制（滑动窗口、全注意力与 Mamba2 线性注意力）及 NVFP4 MoE，在 Blackwell 硬件上输入吞吐高达 71.7k tok/s，单用户解码速度达 171.0 tok/s。 DSPark 基于置信度的方法突破了传统固定长度推测解码的限制，提供了一种更自适应的方式，可显著提升大规模 LLM 推理的吞吐量。结合对 Inkling 的支持以及 Blackwell GPU 优化，该版本使 SGLang 在高效服务下一代万亿参数多模态模型方面处于领先地位。 DSPark 通过 --speculative-algorithm DSPARK 和 SGLANG\_RAGGED\_VERIFY\_MODE=compact 启用，块大小可通过 --speculative-dspark-block-size 调整。该版本还将 UnifiedRadixTree 设为 SWA、Mamba 和 DSA 模型的默认选项，引入了 DSA 缓存层分割功能，使 GLM-5.2 每 rank 的 KV 内存减少约 74%，并移除了实验性的 QServe 和 FBGEMM FP8 量化路径（NVFP4 GEMM 现在需要 FlashInfer）。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: SGLang 是一个领先的大语言模型开源推理框架，以其高性能推理引擎和基于 RadixTree 的前缀缓存而闻名。推测解码是一种加速自回归生成的技术，它使用较小的

**标签**: `#LLM-inference`, `#speculative-decoding`, `#SGLang`, `#GPU-optimization`, `#multimodal-models`

---