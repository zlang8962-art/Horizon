---
layout: default
title: "Horizon Summary: 2026-07-26 (EN)"
date: 2026-07-26
lang: en
---

> From 28 items, 2 important content pieces were selected

---

1. [vLLM v0.26.0 Released with Inkling Support and DeepSeek-V4 Optimizations](#item-1) ⭐️ 8.0/10
2. [SGLang v0.5.16 Adds DSPark Speculative Decoding and Inkling 975B MoE Support](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.26.0 Released with Inkling Support and DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 introduces full support for the Inkling model family, significant DeepSeek-V4 performance optimizations across NVIDIA, AMD, and Intel XPU hardware, fp32 lm\_head improvements, and flexible per-KV-cache-group attention backend selection. The release includes 411 commits from 212 contributors, with new model support, speculative decoding enhancements, and matured KV offloading capabilities. As a critical LLM inference engine, vLLM&\#x27;s performance optimizations across multiple hardware vendors and support for emerging models like Inkling and DeepSeek-V4 directly impact deployment efficiency for AI services. The architectural improvements in attention backends and KV offloading enable more flexible and scalable inference solutions for production environments. DeepSeek-V4 optimizations include a specialized routing kernel achieving 2.94% E2E TPOT improvement, fused\_topk\_bias delivering 1.5-2x kernel speedup, and DSpark speculative decoding support on AMD and XPU. The Inkling model family receives comprehensive support including Hopper FA4 relative attention, MTP=1 speculative decoding, LoRA, and ModelOpt NVFP4 quantization. The Rust frontend now supports multimodal video and audio inputs.

github · khluu · Jul 25, 10:38

**Background**: vLLM is a high-throughput, memory-efficient inference engine for large language models that implements PagedAttention for efficient KV-cache management. Speculative decoding is an inference acceleration technique that uses a smaller draft model to propose tokens that are then verified by the target model in parallel. The Inkling model is a 1-trillion parameter multimodal model from Thinking Machines Lab that natively processes text, image, and audio inputs with up to 1M context length. DSpark is a confidence-scheduled speculative decoding framework that addresses acceptance decay issues in parallel draft generation.

<details><summary>References</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-07-15-inkling">TML Inkling on vLLM: Day-0 Support with Optimized Performance</a></li>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative ...</a></li>
<li><a href="https://www.marktechpost.com/2026/06/27/deepseek-releases-dspark-a-speculative-decoding-framework-that-accelerates-deepseek-v4-per-user-generation-60-85-over-mtp-1/">DeepSeek Releases DSpark, a Speculative Decoding Framework ...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM-inference`, `#GPU-optimization`, `#speculative-decoding`, `#AI-infrastructure`

---

<a id="item-2"></a>
## [SGLang v0.5.16 Adds DSPark Speculative Decoding and Inkling 975B MoE Support](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 8.0/10

SGLang v0.5.16 introduces DSPark, a confidence-driven speculative decoding algorithm that dynamically sizes verification windows based on draft confidence, reaching 383.7 tok/s on DeepSeek-V4-Pro with TP8 on Blackwell B300 GPUs. The release also adds Day-0 support for Inkling, a 975B-parameter multimodal MoE model with 1M-token context, hybrid attention \(sliding-window, full, and Mamba2 linear\), and NVFP4 MoE, achieving up to 71.7k tok/s input and 171.0 tok/s per-user decode on Blackwell hardware. DSPark&\#x27;s confidence-driven approach moves beyond fixed-length speculative decoding, offering a more adaptive method that can significantly boost throughput for large-scale LLM inference. Combined with Inkling support and Blackwell GPU optimizations, this release positions SGLang at the forefront of serving next-generation trillion-parameter multimodal models efficiently. DSPark is enabled via --speculative-algorithm DSPARK and SGLANG\_RAGGED\_VERIFY\_MODE=compact, with block size tunable via --speculative-dspark-block-size. The release also makes UnifiedRadixTree the default for SWA, Mamba, and DSA models, introduces a DSA cache layer split that cuts per-rank KV memory by ~74% for GLM-5.2, and removes experimental QServe and FBGEMM FP8 quantization paths \(NVFP4 GEMM now requires FlashInfer\).

github · Qiaolin-Yu · Jul 25, 00:13

**Background**: SGLang is a leading open-source serving framework for large language models, known for its high-performance inference engine and RadixTree-based prefix caching. Speculative decoding is a technique that accelerates autoregressive generation by using a smaller &\#x27;draft&\#x27; model to propose multiple tokens at once, which are then verified in parallel by the larger target model. Blackwell is NVIDIA&\#x27;s latest GPU architecture \(SM100\), offering significant performance improvements for AI workloads. MoE \(Mixture of Experts\) is a model architecture where only a subset of &\#x27;expert&\#x27; sub-networks are activated per input, enabling very large parameter counts with manageable compute costs.

**Tags**: `#LLM-inference`, `#speculative-decoding`, `#SGLang`, `#GPU-optimization`, `#multimodal-models`

---