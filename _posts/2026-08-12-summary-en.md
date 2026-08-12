---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
content_date: 2026-08-11
lang: en
---

> Coverage: 2026-08-11 (Asia/Shanghai calendar day)

> From 113 items, 12 important content pieces were selected

---

1. [vLLM v0.27.0 Adds Kimi K3, PyTorch 2.13, and New Models](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10353 Fixes Memory Stride Bug in CUDA and Metal](#item-2) ⭐️ 10.0/10
3. [llama.cpp Release b10355 Adds Multi-Output Sampling and Token Speculation](#item-3) ⭐️ 9.0/10
4. [ollama/ollama released v0.32.9](#item-4) ⭐️ 9.0/10
5. [Ollama v0.32.8 Releases Muse Glimmer Model](#item-5) ⭐️ 9.0/10
6. [Stealing Reasoning Traces from Proprietary LLM APIs](#item-6) ⭐️ 9.0/10
7. [London Underground Expands Live Facial Recognition Trial](#item-7) ⭐️ 9.0/10
8. [11.08× Speedup for llama.cpp on macOS VMs via Virtualization.framework](#item-8) ⭐️ 9.0/10
9. [Deep Dive: Intercepting GitHub Copilot Traffic via MitM Proxy](#item-9) ⭐️ 9.0/10
10. [Transformer Weights Manually Set for Exact Arithmetic](#item-10) ⭐️ 9.0/10
11. [苹果被曝正测试长鑫存储芯片 用于在中国市场销售的设备 - cls.cn](#item-11) ⭐️ 9.0/10
12. [CXMT DDR5 Yield Improvement and PC Procurement Strategy Differences](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [vLLM v0.27.0 Adds Kimi K3, PyTorch 2.13, and New Models](https://github.com/vllm-project/vllm/releases/tag/v0.27.0) ⭐️ 10.0/10

vLLM v0.27.0 introduces Kimi K3 support with full-stack integration, upgrades to PyTorch 2.13.0 and Triton 3.7.1, and adds new models like Qwen3.5 and K-EXAONE-2.0-750B-A37B. This release significantly advances AI compute efficiency and model support, enabling better performance on next-gen hardware like NVIDIA Rubin and improving the ecosystem for serving large language models. Key updates include FP8 KV cache support for FlashAttention 4, expanded Model Runner V2 for non-generative workloads, and a new gRPC control plane for the Rust frontend.

github · khluu · Aug 11, 05:18

**Background**: vLLM is a high-performance LLM inference engine optimized for serving large models, with support for various hardware backends and model architectures.

**Tags**: `#AI`, `#LLM`, `#PyTorch`, `#Hardware`, `#OpenSource`

---

<a id="item-2"></a>
## [llama.cpp b10353 Fixes Memory Stride Bug in CUDA and Metal](https://github.com/ggml-org/llama.cpp/releases/tag/b10353) ⭐️ 10.0/10

llama.cpp release b10353 fixes a critical memory stride bug in the CUDA and Metal backends for the ROLL operation, which previously caused silent data corruption when handling non-contiguous memory. This fix is crucial for developers using these backends, as it ensures correct tensor handling and prevents incorrect inference results in AI model execution. The bug occurred because the CUDA and Metal kernels indexed data by element count \(ne\) alone, ignoring memory strides \(nb\), while the CPU backend correctly handled strides. The fix adds contiguity requirements to both backends and includes a test case for permuted inputs.

github · github-actions\[bot\] · Aug 11, 06:00

**Background**: GGML is a custom tensor library used by llama.cpp for efficient machine learning inference. Tensors in GGML can be stored in non-contiguous memory layouts, where the first dimension \(ne\[0\]\) is contiguous, but other dimensions may have strides. The ROLL operation shifts tensor elements, and its correctness depends on proper stride handling.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@yifeiw203/ggml-deep-dive-ii-memory-management-in-context-only-mode-part-1-8397a1055363">GGML Deep Dive II: Memory Management in Context-only Mode | by Yifei Wang | Medium</a></li>
<li><a href="https://gist.github.com/ddh0/9696e1928b31125404d12d0a2da31c42">A Brief Guide to GGML · GitHub</a></li>
<li><a href="https://deepwiki.com/ggml-org/llama.cpp/3.6-memory-management-and-kv-cache">Memory Management and KV Cache | ggml-org/llama.cpp | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#CUDA`, `#Metal`, `#ggml`, `#bugfix`

---

<a id="item-3"></a>
## [llama.cpp Release b10355 Adds Multi-Output Sampling and Token Speculation](https://github.com/ggml-org/llama.cpp/releases/tag/b10355) ⭐️ 9.0/10

The llama.cpp b10355 release introduces multi-output backend sampling and token speculation to enhance LLM inference performance, along with fixes for CPU/GPU distribution and backend sampling mismatches. This update significantly improves inference speed and efficiency for local LLMs, enabling better hardware utilization and supporting broader adoption of open-source AI models on consumer hardware. Key changes include enabling backend sampling with token speculation, clamping mask sums, adding a numeric context parameter for maximum outputs, and fixing Vulkan tests and memory reuse issues.

github · github-actions\[bot\] · Aug 11, 07:15

**Background**: llama.cpp is a high-performance C++ library for running large language models locally, supporting multiple backends like CUDA, Metal, and Vulkan to optimize inference across different hardware platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youngju.dev/blog/llm/2026-03-14-llm-inference-optimization-vllm-tensorrt-speculative-decoding.en">The Complete Guide to LLM Inference Optimization: vLLM...</a></li>
<li><a href="https://predibase.com/blog/llm-inference-benchmarks-predibase-fireworks-vllm">Real-World LLM Inference Benchmarks: How Predibase Built the...</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI inference`, `#C++`, `#Open Source`, `#Local LLM`

---

<a id="item-4"></a>
## [ollama/ollama released v0.32.9](https://github.com/ollama/ollama/releases/tag/v0.32.9) ⭐️ 9.0/10

Ollama v0.32.9 adds the NVIDIA Nemotron 3.5 Lightning MoE model and fixes a Muse Glimmer parser bug.

github · dhiltgen · Aug 11, 21:23

**Tags**: `#ollama`, `#nvidia`, `#moe`, `#llm`, `#open-source`

---

<a id="item-5"></a>
## [Ollama v0.32.8 Releases Muse Glimmer Model](https://github.com/ollama/ollama/releases/tag/v0.32.8) ⭐️ 9.0/10

Ollama v0.32.8 introduces Muse Glimmer, a new model optimized for coding agents and assistants, with support for Apple Silicon and NVIDIA platforms. This release enhances the ecosystem of local AI models by providing a high-performance option for coding agents and assistants, particularly benefiting developers on Apple Silicon. Muse Glimmer supports DFlash and image input via Ollama&\#x27;s MLX engine, with commands like \`ollama run muse-glimmer\` for local execution and integration with frameworks like Claude Code and Pi.

github · github-actions\[bot\] · Aug 11, 07:49

**Background**: MLX is a unified multi-modal engine architecture by LM Studio that leverages Python packages like mlx-lm and mlx-vlm for efficient LLM execution on Apple Silicon M chips.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lmstudio-ai/mlx-engine">GitHub - lmstudio-ai/mlx-engine: LM Studio Apple MLX engine · GitHub</a></li>
<li><a href="https://lmstudio.ai/blog/unified-mlx-engine">Introducing the unified multi-modal `MLX` engine architecture in LM Studio | LM Studio Blog | LM Studio</a></li>
<li><a href="https://github.com/z-lab/dflash">GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub</a></li>

</ul>
</details>

**Tags**: `#ollama`, `#ai-model`, `#apple-silicon`, `#coding-agent`, `#mlx`

---

<a id="item-6"></a>
## [Stealing Reasoning Traces from Proprietary LLM APIs](https://stolen-thoughts.com/) ⭐️ 9.0/10

A technical analysis demonstrates how reasoning traces from proprietary LLM APIs can be extracted and exploited via model replay attacks. This vulnerability highlights significant security risks in LLM APIs, potentially enabling unauthorized access to proprietary reasoning processes and undermining trust in AI systems. The attack involves replaying traces from a frontier model into a weaker sibling model to bypass security controls, while some providers like Opus 4.8 may inadvertently expose reasoning steps.

hackernews · quantumgarbage · Aug 11, 21:22 · [Discussion](https://news.ycombinator.com/item?id=49257876)

**Background**: Reasoning traces are explicit steps in an LLM&\#x27;s output that reveal its internal thought process. Model replay attacks, a type of network attack, involve repeating valid data transmissions to deceive systems. LLM APIs are interfaces that allow developers to interact with language models programmatically.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Replay_attack">Replay attack - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2606.00642v1">Hidden Thoughts Are Not Secret: Reasoning Trace Exposure in LLMs</a></li>
<li><a href="https://m0b.fun/academies/port-swigger/ll-ms/2-exploiting-vulnerabilities-in-llm-ap-is/">2 - Exploiting vulnerabilities in LLM APIs</a></li>

</ul>
</details>

**Discussion**: Community comments debate the ethics of &\#x27;stealing&\#x27; traces, with some arguing it is business as usual since traces are already paid for. Others note that replay attacks across models are a known concept and suggest simpler workarounds like disabling reasoning features.

**Tags**: `#AI`, `#LLM`, `#Security`, `#Model Extraction`, `#API Vulnerabilities`

---

<a id="item-7"></a>
## [London Underground Expands Live Facial Recognition Trial](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 9.0/10

The British Transport Police \(BTP\) has expanded its trial of live facial recognition \(LFR\) technology to several London Underground stations, deploying cameras to scan passengers&\#x27; faces. This expansion raises significant concerns about privacy and civil liberties, as it represents a major step in the deployment of surveillance technology in public spaces. The trial aims to understand how LFR can be used in a targeted, proportionate way with strict safeguards, though privacy groups argue it treats the public like suspects.

hackernews · BlueBerry2001 · Aug 11, 17:40 · [Discussion](https://news.ycombinator.com/item?id=49255496)

**Background**: Facial recognition technology, such as DeepFace, uses deep learning to identify individuals but has faced privacy concerns. Unregulated use can impinge on civil liberties, leading to debates about transparency and consent.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c07r0gvgjxyo">Facial recognition cameras to be trialled at London Tube stations</a></li>
<li><a href="https://www.techradar.com/tech/london-underground-is-trialing-live-face-scanning-from-today-as-privacy-groups-say-it-treats-the-public-like-suspects-heres-how-to-avoid-it">London Underground is trialing live face scanning from... | TechRadar</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepFace">DeepFace - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments reflect a mix of skepticism and outrage, with some arguing that the trial is a moot point due to existing contactless payment systems, while others criticize it as an Orwellian intrusion.

**Tags**: `#privacy`, `#surveillance`, `#facial-recognition`, `#civil-liberties`, `#security`

---

<a id="item-8"></a>
## [11.08× Speedup for llama.cpp on macOS VMs via Virtualization.framework](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐️ 9.0/10

A technical blog post demonstrates an 11.08× speedup for llama.cpp inference on macOS VMs by correcting kernel selection within Apple&\#x27;s Virtualization.framework, resulting in 16.36× faster token generation. This optimization is significant for developers and researchers running large language models on Apple Silicon hardware, as it demonstrates a practical method to maximize performance within the macOS virtualization ecosystem. The performance gain was achieved by fixing a bug where the Virtualization.framework was causing llama.cpp to select the wrong Metal kernels, which is specific to VMs and does not apply to native Apple Silicon execution.

hackernews · frabonacci · Aug 11, 22:50 · [Discussion](https://news.ycombinator.com/item?id=49259339)

**Background**: Apple&\#x27;s Virtualization.framework allows users to run macOS inside a virtual machine on Apple Silicon, and Metal is the graphics and compute API used to leverage the GPU. llama.cpp is a popular, high-performance C++ library for running LLMs.

**Discussion**: Community members clarified that the speedup is specific to Virtualization.framework VMs and not a general improvement for llama.cpp on Apple Silicon, with some users finding the title initially misleading.

**Tags**: `#Apple Silicon`, `#llama.cpp`, `#Virtualization.framework`, `#Metal`, `#LLM Inference`

---

<a id="item-9"></a>
## [Deep Dive: Intercepting GitHub Copilot Traffic via MitM Proxy](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) ⭐️ 9.0/10

The author intercepted GitHub Copilot&\#x27;s network traffic using a Man-in-the-Middle \(MitM\) proxy to analyze model routing, context injection, and telemetry practices in real time. This analysis reveals how AI coding tools collect and use data, highlighting security implications and the importance of understanding telemetry practices in developer tools. The experiment showed that Copilot dynamically routes requests to different models, injects context from recent edits and other files, and collects extensive telemetry data without clear user consent.

hackernews · j0selit0 · Aug 11, 18:40 · [Discussion](https://news.ycombinator.com/item?id=49256057)

**Background**: A MitM proxy acts as an intermediary that can intercept, inspect, and modify encrypted network traffic by presenting itself as a trusted certificate authority, allowing the proxy to decrypt and analyze HTTPS connections.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mitmproxy.org/">mitmproxy - an interactive HTTPS proxy</a></li>
<li><a href="https://www.datadoghq.com/blog/ebpf-guide/">Learn how to use eBPF to create an HTTP protocol tracer .</a></li>

</ul>
</details>

**Discussion**: Users discussed the benefits of using eBPF for network tracing, noted that the Codex client is open source, and debated the importance of curated context versus general LLM performance.

**Tags**: `#GitHub Copilot`, `#AI tools`, `#network security`, `#telemetry`, `#eBPF`

---

<a id="item-10"></a>
## [Transformer Weights Manually Set for Exact Arithmetic](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 9.0/10

A researcher manually set transformer weights to perform exact arithmetic without training, achieving 100% accuracy on multiplication using Torchwright compiler. This demonstrates that transformers can perform exact arithmetic if weights are carefully chosen, challenging the notion that they are inherently bad at arithmetic. The three-digit calculator supports 3,000,000 expressions correctly, and checkpoints support up to 12-digit x 12-digit multiplication, with four versions \(grade-school, hardware-style, scratchpad, brute-force\).

reddit · r/MachineLearning · /u/notforrob · Aug 11, 01:37

**Background**: Transformers are deep learning models that use attention mechanisms to process sequences, and their weights are learned numerical parameters stored in matrices that define transformations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transformer_%28deep_learning%29">Transformer (deep learning) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#arithmetic`, `#weights`, `#Torchwright`, `#compiler`

---

<a id="item-11"></a>
## [苹果被曝正测试长鑫存储芯片 用于在中国市场销售的设备 - cls.cn](https://news.google.com/rss/articles/CBMiSEFVX3lxTFBnQ1NNZnVfTlhNSkViTnhIcjhfY0w2TkZXZEhXVjV2dzN5VFpTRC1HclFfYm5rMV9NOG5mdXo0emQ0NjMxVDdsTA?oc=5) ⭐️ 9.0/10

Apple is reportedly testing CXMT memory chips for devices sold in China.

google\_news · cls.cn · Aug 11, 08:21

**Tags**: `#semiconductors`, `#memory`, `#Apple`, `#CXMT`, `#hardware`

---

<a id="item-12"></a>
## [CXMT DDR5 Yield Improvement and PC Procurement Strategy Differences](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9xR0dUaDZDUDBlTDJ6MHpFeE1NbHNBLXZwRy1oa1lrR2RYZGdiSXRyZEFQcVZDMllGTk9YSnowTjhrZjdqNkxYRllqVnNoUFp1UnQ4?oc=5) ⭐️ 9.0/10

Chinese memory manufacturer CXMT has significantly improved the yield rate of its 17nm DDR5 chips to approximately 90%, allowing for large-scale shipments, while major PC manufacturers are adopting diverse procurement strategies. This progress in DDR5 manufacturing is crucial for the global DRAM market, as it reduces production costs and enables more competitive pricing, while the varying procurement strategies among PC makers reflect the industry&\#x27;s response to supply chain volatility. CXMT&\#x27;s DDR5 yield has risen from 50% at initial mass production to 80-90%, and some products have achieved speeds up to 8600 MT/s, though the article does not specify which PC manufacturers are involved in the procurement strategy discussion.

google\_news · 电子工程专辑 · Aug 11, 09:45

**Background**: DDR5 is the latest generation of DRAM technology, offering higher speeds and capacity compared to previous generations, and yield rates are a critical metric in semiconductor manufacturing as they directly impact production costs and scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://wccftech.com/cxmt-hits-90-yield-on-17nm-ddr5-chips-closing-the-gap-with-micron-others-report/">CXMT Hits 90% Yield on 17nm DDR5 Chips, Closing the Gap With Micron &amp; Others - Report</a></li>
<li><a href="https://www.exportsemi.com/company-post/cxmt-achieves-80-percent-ddr5-yield/">CXMT Achieves 80 Percent DDR5 Yield</a></li>
<li><a href="https://en.sedaily.com/finance/2026/08/08/chinese-chipmaker-cxmt-closes-in-on-korea-hits-top-speed-on">Chinese Chipmaker CXMT Closes In on Korea, Hits Top Speed on US Platforms - Seoul Economic Daily</a></li>

</ul>
</details>

**Tags**: `#DDR5`, `#semiconductor`, `#memory`, `#PC procurement`, `#manufacturing`

---