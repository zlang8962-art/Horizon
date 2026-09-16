---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
content_date: 2026-09-15
lang: en
---

> Coverage: 2026-09-15 (Asia/Shanghai calendar day)

> From 65 items, 11 important content pieces were selected

---

1. [ggml-org/llama.cpp released b10969](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10984](#item-2) ⭐️ 9.0/10
3. [Hacking a $20 4G Hotspot into a Texting Device](#item-3) ⭐️ 9.0/10
4. [Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar](#item-4) ⭐️ 9.0/10
5. [On-Device vs Datacenter Inference: Robot Brain Tradeoffs](#item-5) ⭐️ 9.0/10
6. [Cloudflare Workers Now Supports Granular Authorization](#item-6) ⭐️ 9.0/10
7. [Kubernetes v1.37: Memory QoS Graduates to Beta](#item-7) ⭐️ 9.0/10
8. [Trained 44M Parameter Quantized LLM from Scratch, Ships in 19.8 MB](#item-8) ⭐️ 9.0/10
9. [联发科发布天玑9600 Pro](#item-9) ⭐️ 9.0/10
10. [China&\#x27;s Rapid Progress in Domestic Storage Chips](#item-10) ⭐️ 9.0/10
11. [“Project Lily”内幕：人工阅读 ChatGPT 聊天记录](#item-11) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10969](https://github.com/ggml-org/llama.cpp/releases/tag/b10969) ⭐️ 10.0/10

llama.cpp release b10969 adds Ubuntu-CUDA builds to CI, improving cross-platform support for AI model inference.

github · github-actions\[bot\] · Sep 15, 03:50

**Tags**: `#llama.cpp`, `#AI inference`, `#CUDA`, `#CI/CD`, `#open-source`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10984](https://github.com/ggml-org/llama.cpp/releases/tag/b10984) ⭐️ 9.0/10

llama.cpp b10984 adds CUDA support for row-contiguous SUM\_ROWS operations and releases cross-platform binaries.

github · github-actions\[bot\] · Sep 15, 21:41

**Tags**: `#llama.cpp`, `#CUDA`, `#AI inference`, `#open-source`, `#performance`

---

<a id="item-3"></a>
## [Hacking a $20 4G Hotspot into a Texting Device](https://bkovac.github.io/modem-thing/) ⭐️ 9.0/10

A hacker successfully repurposed a cheap $20 4G wireless hotspot into a dedicated texting device by modifying its hardware and adding a repurposed keyboard. This project demonstrates how low-cost hardware can be creatively repurposed to create functional, privacy-focused communication tools, which is significant for users seeking alternatives to smartphones. The project involved chip-level modifications, a battery upgrade, and integration with a repurposed keyboard to enable SMS functionality, with the creator sharing detailed technical steps on GitHub.

hackernews · bobili1234 · Sep 15, 21:20 · [Discussion](https://news.ycombinator.com/item?id=49712102)

**Background**: 4G wireless hotspots are portable devices that provide internet access via cellular networks, often used as backup or primary internet sources. Repurposing them into specialized devices like cyberdecks involves modifying their internal components and software to serve a specific purpose.

**Discussion**: Community members praised the project&\#x27;s creativity and practicality, with some suggesting improvements like adding a larger battery for longer life or running agent systems on the device.

**Tags**: `#hardware-hacking`, `#4g-modem`, `#cyberdeck`, `#battery-life`, `#repurposing`

---

<a id="item-4"></a>
## [Vera Rubin NVL72 Agentic Inference: 67x better Performance per Dollar](https://newsletter.semianalysis.com/p/vera-rubin-nvl72-agentic-inference) ⭐️ 9.0/10

This newsletter analyzes Vera Rubin&\#x27;s NVL72 agentic inference, highlighting 67x better performance per dollar and extreme co-design strategies.

rss · Semianalysis · Sep 15, 06:08

**Tags**: `#AI Compute`, `#Hardware Co-design`, `#Inference Optimization`, `#Performance Metrics`, `#Cost Efficiency`

---

<a id="item-5"></a>
## [On-Device vs Datacenter Inference: Robot Brain Tradeoffs](https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device) ⭐️ 9.0/10

The newsletter analyzes the tradeoffs between on-device and datacenter inference for robot models, comparing Jetson Thor and B300 TCO, and discusses deployment challenges and the &\#x27;Network Wall&\#x27;. This analysis is significant for the robotics industry as it highlights the critical balance between silicon efficiency, deployment costs, and real-time performance constraints for autonomous systems. Boston Dynamics runs robot brains on Google TPUs, but for 96 robots, Jetson Thor offers the lowest TCO at $14.97/hr compared to RTX 6000 Pro \($15.61\) and B300 \($18.63\), while the &\#x27;Network Wall&\#x27; poses latency risks for remote inference.

rss · Semianalysis · Sep 15, 00:37

**Background**: Robot inference requires balancing model size, silicon efficiency, and real-time performance. The &\#x27;Network Wall&\#x27; refers to the latency issues when offloading robot inference to datacenters, which can be unacceptable for time-sensitive tasks like surgery.

<details><summary>References</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/boston-dynamics-runs-robot-brains-on-tpus-rivals-stay-on-jetson">Boston Dynamics runs robot brains on TPUs; rivals stay on Jetson</a></li>
<li><a href="https://nalinraut.github.io/blog/2026/inferential/?trk=public_post_comment-text">Inferential - Centralized Inference Orchestration for Factory Robotics</a></li>
<li><a href="https://www.roboticscenter.ai/state-of-robotics-2026">State of Robotics 2026 | Robotics Center page</a></li>

</ul>
</details>

**Tags**: `#AI inference`, `#on-device computing`, `#hardware efficiency`, `#robotics`, `#semiconductors`

---

<a id="item-6"></a>
## [Cloudflare Workers Now Supports Granular Authorization](https://blog.cloudflare.com/workers-granular-authorization/) ⭐️ 9.0/10

Cloudflare Workers now supports granular authorization, allowing users to scope access to individual Workers and assign narrower Developer Platform roles. This feature significantly improves security by ensuring teammates, CI tokens, and agents have only the access they need to debug, deploy, or monitor safely, addressing a critical need in DevOps and developer tooling. The new roles support resource-level access, and while the wrangler login OAuth flow does not currently support granular authorization, users can authenticate with an account-owned API token to use granular permissions.

rss · Cloudflare Blog · Sep 15, 21:00

**Background**: Cloudflare Workers is a serverless computing platform that allows developers to run JavaScript, TypeScript, and Rust code at the edge. Authorization is the process of controlling access to resources, and granular authorization provides fine-grained control over who can access specific resources.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/workers-granular-authorization/">Give every teammate and agent the right level of access to your Workers | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/workers/authorization/">Roles and permissions · Cloudflare Workers docs</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Developer Tools`, `#Authorization`, `#Security`, `#DevOps`

---

<a id="item-7"></a>
## [Kubernetes v1.37: Memory QoS Graduates to Beta](https://kubernetes.io/blog/2026/09/14/kubernetes-v1-37-memory-qos-graduates-to-beta/) ⭐️ 9.0/10

Kubernetes v1.37 has graduated the Memory QoS feature to Beta and enabled it by default for Linux nodes running cgroup v2. This change improves Linux cgroup v2 memory handling by providing better kernel guidance, which is critical for maintaining stability and performance in containerized environments. The feature is now enabled by default with the MemoryQoS feature gate, but memory throttling and reservation are only applied if explicitly configured via kubelet settings like memoryThrottlingFactor and memoryReservationPolicy.

rss · Kubernetes Blog · Sep 15, 02:30

**Background**: Memory QoS was initially introduced as an Alpha feature in Kubernetes v1.22 and expanded in v1.36 with tiered memory reservation capabilities.

**Tags**: `#Kubernetes`, `#Memory Management`, `#Software Engineering`, `#System Administration`, `#DevOps`

---

<a id="item-8"></a>
## [Trained 44M Parameter Quantized LLM from Scratch, Ships in 19.8 MB](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 9.0/10

A researcher trained SHADOW-50M, a 44M parameter quantized LLM from scratch on 45B tokens, achieving 1,900 tok/s on CPU with a 19.8 MB footprint and 41 MB RAM usage. This breakthrough demonstrates efficient on-device inference with minimal resource requirements, potentially enabling powerful local AI applications on resource-constrained devices. The model uses ternary \{-1,0,+1\} weights, a 73,880-token vocabulary represented by fixed 512-bit fingerprints, and a 159 KB compiled kernel that runs offline and in WebAssembly at ~500 tok/s.

reddit · r/MachineLearning · /u/Final-Data-1410 · Sep 15, 20:59

**Background**: LLM quantization reduces numerical precision \(e.g., from FP16 to INT4/INT8\) to compress model weights, enabling efficient on-device inference. Ternary weights constrain weights to -1, 0, and +1, improving memory efficiency. WebAssembly allows high-performance code execution in browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://localllm.in/blog/quantization-explained">The Complete Guide to LLM Quantization - localllm.in</a></li>
<li><a href="https://grokipedia.com/page/Ternary_Weights">Ternary Weights</a></li>
<li><a href="https://blog.pixelfreestudio.com/how-to-use-webassembly-for-machine-learning-in-the-browser/">How to Use WebAssembly for Machine Learning in the Browser</a></li>

</ul>
</details>

**Tags**: `#quantized-llm`, `#local-ai`, `#software-engineering`, `#machine-learning`, `#webassembly`

---

<a id="item-9"></a>
## [联发科发布天玑9600 Pro](https://www.reuters.com/business/media-telecom/mediatek-launches-new-mobile-chip-using-tsmcs-most-advanced-technology-2026-09-15/) ⭐️ 9.0/10

MediaTek announces the launch of its flagship Dimensity 9600 Pro mobile chip, featuring a 2nm process and an enhanced AI processor.

telegram · zaihuapd · Sep 15, 16:57

**Tags**: `#Semiconductors`, `#Mobile Processors`, `#AI Hardware`, `#Chip Manufacturing`, `#MediaTek`

---

<a id="item-10"></a>
## [China&\#x27;s Rapid Progress in Domestic Storage Chips](https://news.google.com/rss/articles/CBMiTkFVX3lxTFA4MTBxelRNYm9JTUtqeFpuUjdVQVpZMlpMdWxrYVN2WUtQam9pN3Y5R0p3Zno0QUozMXBQdDVDbW5BbXpsUlpTbnBodTNGZw?oc=5) ⭐️ 9.0/10

China has significantly narrowed the technology gap with global leaders in NAND, DRAM, and HBM memory chips. This progress is crucial for China&\#x27;s semiconductor self-sufficiency and reducing reliance on foreign technology. The gap with global leaders is approximately one year for NAND, two years for DRAM, and three years for HBM.

google\_news · 36 Kr · Sep 15, 17:52

**Background**: High Bandwidth Memory \(HBM\) is a 3D-stacked SDRAM technology developed by Samsung, AMD, and SK Hynix, used in GPUs and AI accelerators. China&\#x27;s semiconductor industry, including companies like Yangtze Memory Technologies \(YMTC\) and ChangXin, is rapidly advancing domestic manufacturing capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#HBM`, `#AI hardware`, `#China tech`

---

<a id="item-11"></a>
## [“Project Lily”内幕：人工阅读 ChatGPT 聊天记录](https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/) ⭐️ 8.0/10

404 Media reports that OpenAI employs humans to review ChatGPT conversations for model improvement, raising privacy concerns.

telegram · zaihuapd · Sep 15, 19:56

**Tags**: `#AI`, `#Privacy`, `#OpenAI`, `#Model Evaluation`, `#Data Security`

---