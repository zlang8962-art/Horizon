---
layout: default
title: "Horizon Summary: 2026-09-24 (EN)"
date: 2026-09-24
content_date: 2026-09-23
lang: en
---

> Coverage: 2026-09-23 (Asia/Shanghai calendar day)

> From 94 items, 12 important content pieces were selected

---

1. [ggml-org/llama.cpp released b11135](#item-1) ⭐️ 10.0/10
2. [llama.cpp Release b11122 Adds SYCL Fusion Kernels and Cross-Platform Binaries](#item-2) ⭐️ 10.0/10
3. [llm 0.36 adds GPT-6 models and conversation support](#item-3) ⭐️ 10.0/10
4. [Ollama v0.34.4-rc1: Fixes for Model Inference and App Detection](#item-4) ⭐️ 9.0/10
5. [Microsoft Releases ONNX Runtime WebGPU Plugin v0.4.0](#item-5) ⭐️ 9.0/10
6. [Google Announces Gemini 3.8 Text-to-Speech with Voice Cloning](#item-6) ⭐️ 9.0/10
7. [Tokens too cheap to meter](#item-7) ⭐️ 9.0/10
8. [Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war](#item-8) ⭐️ 9.0/10
9. [Qualcomm Announces Snapdragon 8 Elite Extreme Gen 6 Platform](#item-9) ⭐️ 9.0/10
10. [Hacker Group Claims to Have Hacked FBI, Stolen All Employee Data](#item-10) ⭐️ 9.0/10
11. [CXMT Debuts LPDDR6 and Announces G5 Platform Mass Production](#item-11) ⭐️ 9.0/10
12. [Micron Loses German Sales Ban, YMTC Wins First Substantive Injunction](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11135](https://github.com/ggml-org/llama.cpp/releases/tag/b11135) ⭐️ 10.0/10

The llama.cpp project releases version b11135 with a focus on model deduplication and cross-platform binaries.

github · github-actions\[bot\] · Sep 23, 22:05

**Tags**: `#llama.cpp`, `#open-source`, `#AI-inference`, `#model-optimization`, `#cross-platform`

---

<a id="item-2"></a>
## [llama.cpp Release b11122 Adds SYCL Fusion Kernels and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b11122) ⭐️ 10.0/10

The llama.cpp project released version b11122, introducing performance-optimizing fusion kernels for SYCL \(AMD GPU\) and providing pre-compiled binaries for macOS, Linux, iOS, Android, and Windows. This release significantly enhances the efficiency of LLM inference on AMD hardware and expands the project&\#x27;s cross-platform compatibility, directly benefiting developers and users who rely on optimized AI compute. Key updates include extended MMVQ GLU fusion for mixed quantization, new rms\_norm+scale and ssm\_conv+silu fusions, and a wide array of binaries supporting various backends like CUDA, ROCm, Vulkan, and SYCL.

github · github-actions\[bot\] · Sep 23, 16:33

**Background**: llama.cpp is a leading open-source implementation of LLM inference that focuses on efficiency and portability across different hardware architectures.

**Tags**: `#llama.cpp`, `#AI inference`, `#SYCL`, `#performance optimization`, `#open-source`

---

<a id="item-3"></a>
## [llm 0.36 adds GPT-6 models and conversation support](https://simonwillison.net/2026/Sep/22/llm/) ⭐️ 10.0/10

llm 0.36 introduces support for the new OpenAI GPT-6 Sol and Luna models, and allows model plugins to declare conversation support via the \`supports\_conversation = False\` flag. This release expands the library&\#x27;s compatibility with cutting-edge AI models and improves the developer experience by enforcing conversation support constraints, which is crucial for building robust LLM-powered applications. When a model declares \`supports\_conversation = False\`, the library raises \`llm.ConversationNotSupported\` if conversation history is provided, and the \`llm chat\` command rejects such models before starting a session.

rss · Simon Willison · Sep 23, 02:48

**Background**: llm is a Python library for interacting with Large Language Models \(LLMs\), designed to provide a unified interface for various model providers. It is maintained by Simon Willison and is widely used by developers for building LLM-based tools and applications.

**Tags**: `#LLM`, `#OpenAI`, `#Python`, `#Software Release`, `#Developer Tools`

---

<a id="item-4"></a>
## [Ollama v0.34.4-rc1: Fixes for Model Inference and App Detection](https://github.com/ollama/ollama/releases/tag/v0.34.4-rc1) ⭐️ 9.0/10

Ollama v0.34.4-rc1 introduces fixes for intermittent &\#x27;model not found&\#x27; errors, applies structured outputs in a single pass on thinking models, and improves ChatGPT/Codex app detection, along with updates to llama.cpp and MLX. These improvements enhance the reliability and performance of AI model inference, particularly for structured outputs and thinking models, which are critical for applications requiring predictable and type-safe results. The release includes a llama.cpp version update, MLX version bump, and dynamic Gemma 4 image resolution selection, but no major security updates or hardware-specific optimizations beyond MLX improvements.

github · github-actions\[bot\] · Sep 23, 10:24

**Background**: Ollama is a tool for running open-source LLMs locally, while MLX is Apple&\#x27;s array framework for efficient machine learning on Apple silicon, and llama.cpp is a C++ inference engine for GGUF models. Structured outputs ensure models adhere to JSON schemas for predictable results.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple silicon · GitHub</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/ C++ · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Software`, `#Ollama`, `#MLX`, `#llama.cpp`

---

<a id="item-5"></a>
## [Microsoft Releases ONNX Runtime WebGPU Plugin v0.4.0](https://github.com/microsoft/onnxruntime/releases/tag/plugin-ep-webgpu/v0.4.0) ⭐️ 9.0/10

Microsoft has released the ONNX Runtime WebGPU plugin v0.4.0, focusing on kernel performance improvements and expanded operator support. This release enhances the performance of machine learning inference on the web, making it more efficient for developers deploying AI models in browsers. Key improvements include optimized MatMulNBits wide-tile execution using subgroup shuffle, fused activation support for Conv/MatMul, and new operator support for Qwen-3.5 and DeepSeek Engram.

github · edgchen1 · Sep 23, 01:13

**Background**: ONNX Runtime is an open-source machine learning inference accelerator, and the WebGPU plugin enables GPU acceleration in web browsers. WebGPU is a modern graphics API that provides low-level access to GPU hardware for high-performance computing.

<details><summary>References</summary>
<ul>
<li><a href="https://onnxruntime.ai/docs/execution-providers/WebGPU-ExecutionProvider.html">WebGPU | onnxruntime</a></li>
<li><a href="https://github.com/microsoft/onnxruntime/blob/main/plugin-ep-webgpu/README.md">onnxruntime/plugin-ep-webgpu/README.md at main - GitHub</a></li>

</ul>
</details>

**Tags**: `#onnxruntime`, `#webgpu`, `#ai-inference`, `#performance-optimization`, `#gpu-acceleration`

---

<a id="item-6"></a>
## [Google Announces Gemini 3.8 Text-to-Speech with Voice Cloning](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) ⭐️ 9.0/10

Google has introduced the Gemini 3.8 text-to-speech model, featuring advanced voice replication capabilities that can recreate consistent vocal profiles from just a 30-second audio sample. This advancement in voice synthesis technology is significant for content creators and developers, offering more natural and expressive speech generation while addressing ethical concerns through built-in consent verification and watermarking. The model includes SynthID watermarking and C2PA credentials to protect both developers and vocal talent, though availability may vary across Google&\#x27;s consumer, prosumer, and cloud platforms.

hackernews · swolpers · Sep 23, 23:29 · [Discussion](https://news.ycombinator.com/item?id=49817615)

**Background**: Text-to-speech \(TTS\) technology converts written text into spoken audio, with recent advancements focusing on creating more natural and expressive voices. Voice cloning, a subset of TTS, uses AI to replicate specific voices from short audio samples.

**Discussion**: Users expressed frustration over inconsistent AI model availability across Google&\#x27;s platforms, while others discussed the potential of local-first alternatives and the improved control offered by Gemini 3.8&\#x27;s voice library.

**Tags**: `#AI`, `#Google`, `#Text-to-Speech`, `#Voice Cloning`, `#SynthID`

---

<a id="item-7"></a>
## [Tokens too cheap to meter](https://jyn.dev/tokens-too-cheap-to-meter/) ⭐️ 9.0/10

The article explores the trend of LLM token costs dropping to near-zero levels, potentially making them cheaper than traditional tools like grep.

hackernews · teoruiz · Sep 23, 17:21 · [Discussion](https://news.ycombinator.com/item?id=49813482)

**Tags**: `#AI`, `#LLM`, `#Economics`, `#Hardware`, `#Efficiency`

---

<a id="item-8"></a>
## [Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/) ⭐️ 9.0/10

Simon Willison analyzes Anthropic&\#x27;s Claude Opus 5.5 and OpenAI&\#x27;s GPT-6 Sol and Luna, highlighting their competitive pricing and performance.

rss · Simon Willison · Sep 23, 07:46

**Tags**: `#AI Models`, `#OpenAI`, `#Anthropic`, `#Pricing`, `#LLMs`

---

<a id="item-9"></a>
## [Qualcomm Announces Snapdragon 8 Elite Extreme Gen 6 Platform](https://www.qualcomm.com/smartphones/products/8-series/snapdragon-8-elite-extreme-gen-6-mobile-platform) ⭐️ 9.0/10

Qualcomm has launched the Snapdragon 8 Elite Extreme Gen 6 mobile platform, featuring the new Oryon CPU, Adreno GPU, and Hexagon NPU with significant performance gains. This platform represents a major leap in mobile AI and graphics capabilities, setting new benchmarks for next-generation smartphones and enabling more complex on-device applications. The Oryon CPU is the world&\#x27;s first 5 GHz smartphone CPU, while the Adreno GPU offers a 44% performance boost and 40% efficiency improvement, and the Hexagon NPU delivers a 35% speed increase.

telegram · zaihuapd · Sep 23, 08:52

**Background**: Snapdragon 8 Elite Extreme Gen 6 is Qualcomm&\#x27;s latest flagship mobile processor designed for high-end smartphones, integrating advanced AI, graphics, and connectivity technologies.

**Tags**: `#Snapdragon`, `#AI Hardware`, `#Mobile Platform`, `#Chipset`, `#Qualcomm`

---

<a id="item-10"></a>
## [Hacker Group Claims to Have Hacked FBI, Stolen All Employee Data](https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/) ⭐️ 9.0/10

The hacker group ShinyHunters claims to have breached FBI systems and stolen data on all FBI employees and job applicants, including names, addresses, phone numbers, and family information. This breach poses significant risks to national security and personal privacy, potentially enabling harassment, threats, or espionage against FBI personnel and their families. The group claims to have accessed approximately 5,000 FBI employee records and potentially 2TB to 3TB of data, exploiting a zero-day vulnerability in Oracle&\#x27;s PeopleSoft software and Amazon&\#x27;s AWS GovCloud.

telegram · zaihuapd · Sep 23, 13:00

**Background**: ShinyHunters is a notorious black-hat cybercriminal group active since 2019, specializing in large-scale data breaches, extortion, and selling stolen data on the dark web.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/">ShinyHunters claims FBI hack, data theft in PeopleSoft zero-day breach</a></li>
<li><a href="https://www.ic3.gov/PSA/2026/PSA260515">Internet Crime Complaint Center (IC3) | ShinyHunters: Cyber Criminal Group Attacks Learning Management System</a></li>
<li><a href="https://www.docontrol.io/blog/shinyhunters">Who Is ShinyHunters? | Tactics, Top Attacks &amp; How to Protect Your Organization</a></li>

</ul>
</details>

**Tags**: `#Cybersecurity`, `#Data Breach`, `#FBI`, `#Government Security`, `#Data Privacy`

---

<a id="item-11"></a>
## [CXMT Debuts LPDDR6 and Announces G5 Platform Mass Production](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9lVEtXWFNXLV9nZWJaUGhodnVaSmxPbkw5d3lmUlI5SUEyZ21NZ0t6TmhkT2VZSXNMTnBsWHdiYkxFWUExT0lGNA?oc=5) ⭐️ 9.0/10

CXMT showcased LPDDR6 memory and announced mass production of its G5 platform at the 2026 World Manufacturing Convention in Hefei, alongside ByteDance&\#x27;s &\#x27;Doubao Phone&\#x27;. The G5 platform marks a significant advancement in China&\#x27;s domestic memory chip capabilities, potentially reducing reliance on foreign suppliers and strengthening the local semiconductor ecosystem. CXMT developed the G5 platform using a &\#x27;digital twin&\#x27; approach for design, tape-out, and yield management, while LPDDR6 represents the next generation of low-power mobile DRAM with enhanced RAS features.

google\_news · 财联社 · Sep 23, 16:57

**Background**: LPDDR \(Low Power Double Data Rate\) is a DRAM standard for mobile devices that minimizes power consumption through low-voltage operation. CXMT&\#x27;s G5 platform is its fifth-generation DRAM technology, and the &\#x27;Doubao Phone&\#x27; is an AI-native smartphone developed by ByteDance in partnership with nubia \(ZTE\).

<details><summary>References</summary>
<ul>
<li><a href="https://www.cxmt.com/en/news/info_22.html">CXMT Announces Mass Production of 5th-Generation DRAM ...</a></li>
<li><a href="https://news.skhynix.com/en/1c-lpddr6-development-2026/">SK hynix Develops 1c LPDDR6, 6th-Generation 10nm-Class DRAM</a></li>
<li><a href="https://www.techspot.com/news/113928-cxmt-new-dram-platform-could-give-china-memory.html">China&#x27;s CXMT just entered mass production of memory chips ...</a></li>

</ul>
</details>

**Tags**: `#CXMT`, `#LPDDR6`, `#G5 Platform`, `#Memory`, `#AI Hardware`

---

<a id="item-12"></a>
## [Micron Loses German Sales Ban, YMTC Wins First Substantive Injunction](https://news.google.com/rss/articles/CBMiUkFVX3lxTE1YdGNNRXpHRk1oNFFWaXRXTGxzS196ZjR6bHpBd0FsbzhldFV0S0o5OUg2QnpsaldQQUJjeFdsbDA2OFlnUnBIM0QyUG9xOG9Xbmc?oc=5) ⭐️ 9.0/10

A German court has ruled in favor of Yangtze Memory Technologies \(YMTC\), granting the company its first substantive injunction against Micron, which includes a sales ban on certain products. This ruling marks a significant victory for YMTC in its global patent dispute with Micron, potentially shifting the balance of power in the competitive 3D NAND memory market. The injunction was granted based on 3D NAND utility models, and Micron has already announced its intention to appeal the decision, which may affect the immediate enforcement of the ruling.

google\_news · 国际电子商情 · Sep 23, 09:38

**Background**: The dispute between YMTC and Micron escalated in November 2023, involving complex patent litigation over 3D NAND memory technology, a critical component in modern data storage solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://technode.com/2026/09/23/yangtze-memory-micron-3d-nand-patent-injunction/">Yangtze Memory wins first substantive injunction in 3D NAND ...</a></li>
<li><a href="https://ipfray.com/ymtc-wins-two-german-injunctions-against-micron-getting-leverage-in-global-nand-memory-patent-fight-munich-i-regional-court/">YMTC wins two German injunctions against Micron, getting ...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#YMTC`, `#Micron`, `#trade\_dispute`, `#court\_injunction`

---