---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
content_date: 2026-08-01
lang: en
---

> Coverage: 2026-08-01 (Asia/Shanghai calendar day)

> From 143 items, 12 important content pieces were selected

---

1. [llama.cpp b10218 adds MiniCPM-V 4.6 downsample support](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10214](#item-2) ⭐️ 10.0/10
3. [NVIDIA TensorRT-LLM v1.3.0rc23 Released with DeepSeek V4 and API Updates](#item-3) ⭐️ 10.0/10
4. [Don’t stop early: Case-folding source code at memory speed](#item-4) ⭐️ 10.0/10
5. [OpenAI&\#x27;s Astra Model Achieves Breakthroughs in Ten Long-Standing Math Problems](#item-5) ⭐️ 10.0/10
6. [长鑫存储大突破！国产LPDDR6量产前重要一步 - Sohu](#item-6) ⭐️ 10.0/10
7. [RipGrep musl binaries occasionally segfault during very-large searches](#item-7) ⭐️ 9.0/10
8. [Canada Signs UN Cybercrime Convention Amid Privacy Concerns](#item-8) ⭐️ 9.0/10
9. [Stateless MCP 2.0 Revives Interest in Model Context Protocol](#item-9) ⭐️ 9.0/10
10. [llm-mcp-client 0.1a0: A New Tool for Model Context Protocol](#item-10) ⭐️ 9.0/10
11. [Kubernetes v1.37 Sneak Peek: Planned Deprecations and Changes](#item-11) ⭐️ 9.0/10
12. [Developer Trains Encoder-Only Transformer to Predict Blood Sugar](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10218 adds MiniCPM-V 4.6 downsample support](https://github.com/ggml-org/llama.cpp/releases/tag/b10218) ⭐️ 10.0/10

llama.cpp release b10218 introduces MiniCPM-V 4.6 downsample support via pull request \#25993 and provides pre-built binaries for macOS \(Apple Silicon and Intel\) and iOS. This release significantly expands the project&\#x27;s multimodal capabilities, enabling high-resolution image processing for MiniCPM-V 4.6 models, and makes the software immediately accessible to developers on Apple platforms. The downsample mode is integrated into the GGUF file format, and the mtmd\_image\_preprocessor\_llava\_uhd component is built to handle high-resolution image preprocessing, though the KleidiAI optimization for macOS is currently disabled.

github · github-actions\[bot\] · Aug 1, 20:46

**Background**: llama.cpp is a leading open-source project for running large language models locally, and GGUF is its standard binary format for distributing quantized models, which supports various hardware backends like CUDA, Vulkan, and ROCm.

<details><summary>References</summary>
<ul>
<li><a href="https://korshunov.ai/en/article/15575-llama-cpp-b10218-adds-minicpmv46-downsample-support/">llama.cpp b10218 adds minicpmv 46 downsample support · korshunov.ai</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#open-source`, `#local-llm`, `#multimodal`, `#macos`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10214](https://github.com/ggml-org/llama.cpp/releases/tag/b10214) ⭐️ 10.0/10

llama.cpp v0.5.0 release adds n\_embd\_head feature and provides cross-platform binaries for macOS, Linux, and iOS.

github · github-actions\[bot\] · Aug 1, 04:46

**Tags**: `#llama.cpp`, `#AI`, `#C++`, `#cross-platform`, `#LLM`

---

<a id="item-3"></a>
## [NVIDIA TensorRT-LLM v1.3.0rc23 Released with DeepSeek V4 and API Updates](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc23) ⭐️ 10.0/10

NVIDIA has released TensorRT-LLM v1.3.0rc23, which adds support for DeepSeek V4 models and introduces multi-process HTTP frontend capabilities for the classic IPC executor path. This release is significant for AI developers as it enhances the framework&\#x27;s compatibility with cutting-edge models like DeepSeek V4 and improves the scalability of inference serving through multi-process support. The update also addresses several GPU-specific bugs, including issues with DeepSeek-R1 NVFP4 multi-GPU setups and CUDA graph capture failures, while improving KV cache management and performance optimizations.

github · mikeiovine · Aug 1, 02:55

**Background**: TensorRT-LLM is NVIDIA&\#x27;s high-performance inference engine designed to optimize large language models on NVIDIA GPUs, providing tools for model conversion, optimization, and deployment.

**Tags**: `#TensorRT-LLM`, `#GPU`, `#DeepSeek`, `#CUDA`, `#AI-Compute`

---

<a id="item-4"></a>
## [Don’t stop early: Case-folding source code at memory speed](https://github.blog/engineering/architecture-optimization/dont-stop-early-case-folding-source-code-at-memory-speed/) ⭐️ 10.0/10

GitHub engineers optimize case-folding source code to achieve &gt;45 GiB/s performance using branch-free loops and byte-space arithmetic.

rss · GitHub Blog · Aug 1, 00:00

**Tags**: `#software-optimization`, `#performance-tuning`, `#branch-free`, `#byte-space-arithmetic`, `#github-engineering`

---

<a id="item-5"></a>
## [OpenAI&\#x27;s Astra Model Achieves Breakthroughs in Ten Long-Standing Math Problems](https://openai.com/index/ten-advances-in-mathematics/) ⭐️ 10.0/10

OpenAI&\#x27;s next-generation model Astra has achieved new results in ten long-standing mathematical and theoretical computer science problems, including high-dimensional sphere packing, non-Sophie Germain prime existence, and Connes rigidity conjecture counterexamples. This breakthrough demonstrates the potential of AI as a collaborative tool in advanced mathematics, marking a significant step in the evolution of AI-assisted research and could influence future methodologies in theoretical sciences. The proofs were generated by the AI model at a cost of approximately $2,000 and were then organized and formally verified by humans using the Lean theorem prover, with OpenAI clarifying that the AI generated the arguments while humans handled the organization and formalization.

telegram · zaihuapd · Aug 1, 15:59

**Background**: Lean is a proof assistant and functional programming language based on the calculus of constructions, widely used for formally verifying mathematical proofs and ensuring their correctness through rigorous type theory.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://math.ucsd.edu/seminar/connes-rigidity-conjecture">On Connes&#x27; rigidity conjecture | Department of Mathematics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes">Safe and Sophie Germain primes - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mathematics`, `#OpenAI`, `#Research`, `#Machine Learning`

---

<a id="item-6"></a>
## [长鑫存储大突破！国产LPDDR6量产前重要一步 - Sohu](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOLTVoZmNPSm5qeVlfXzluRF9McnhleG5XZmtUajVtNWFQNU1tdWY4VUUtMWlUNk5vX0p3enRqYTUtV3YwZjNOb2l3TTFrVjZuVGVHNlFOLTFVbklBLWtYeFN2MmgwSmwxSG1hZFZkZGZVdFJLUWZOMkV2OGFMMUs0Z3dIcWtYZldS?oc=5) ⭐️ 10.0/10

Sohu reports a major breakthrough for CXMT in the production of domestic LPDDR6 memory.

google\_news · Sohu · Aug 1, 20:05

**Tags**: `#LPDDR6`, `#semiconductors`, `#memory`, `#AI hardware`, `#chip manufacturing`

---

<a id="item-7"></a>
## [RipGrep musl binaries occasionally segfault during very-large searches](https://github.com/BurntSushi/ripgrep/issues/3494) ⭐️ 9.0/10

A technical discussion on ripgrep musl binaries segfaulting during large searches, focusing on allocator performance and filesystem I/O bottlenecks.

hackernews · throwaway2037 · Aug 1, 20:34 · [Discussion](https://news.ycombinator.com/item?id=49133889)

**Tags**: `#ripgrep`, `#musl`, `#performance`, `#allocator`, `#filesystem`

---

<a id="item-8"></a>
## [Canada Signs UN Cybercrime Convention Amid Privacy Concerns](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/) ⭐️ 9.0/10

Canada has signed the United Nations Convention against Cybercrime, joining 76 other participants as of May 2026. The treaty could expand state surveillance powers, raising significant privacy and security implications for individuals and organizations. The convention, adopted in December 2024, aims to facilitate international cooperation in enforcing cybercrime laws and sharing electronic evidence.

hackernews · iamnothere · Aug 1, 22:19 · [Discussion](https://news.ycombinator.com/item?id=49134694)

**Background**: The UN Cybercrime Convention, also known as the Hanoi Convention, is the first comprehensive global treaty on cybercrime, proposed by Russia in 2017.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Convention_against_Cybercrime">United Nations Convention against Cybercrime - Wikipedia</a></li>
<li><a href="https://www.unodc.org/unodc/en/cybercrime/convention/home.html">United Nations Convention against Cybercrime</a></li>
<li><a href="https://www.hrw.org/news/2025/10/24/joint-statement-on-the-signing-of-the-un-convention-on-cybercrime">Joint Statement on the Signing of the UN Convention on Cybercrime | Human Rights Watch</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Canada&\#x27;s move aligns with its pattern of signing most UN agreements, while others highlighted the limited impact of signing without ratification.

**Tags**: `#cybersecurity`, `#privacy`, `#international law`, `#surveillance`, `#Canada`

---

<a id="item-9"></a>
## [Stateless MCP 2.0 Revives Interest in Model Context Protocol](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

The Model Context Protocol \(MCP\) 2.0, released on July 28, 2026, introduces a stateless protocol core that simplifies client and server implementation compared to the previous stateful version. This change reduces complexity and improves scalability for AI agent frameworks, making it easier to audit and control tools while enabling smaller models to drive them effectively. The new stateless MCP uses a single HTTP request instead of two, eliminating the need for session IDs and server-side state management, as demonstrated in the release candidate blog post.

rss · Simon Willison · Aug 1, 07:13

**Background**: MCP is an open standard for connecting AI applications like Claude and ChatGPT to external tools and data sources, introduced by Anthropic in November 2024. It was initially popular but later overshadowed by Anthropic&\#x27;s Skills feature.

<details><summary>References</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol (MCP) - Anthropic</a></li>
<li><a href="https://arstechnica.com/ai/2026/07/with-a-stateless-makeover-new-mcp-spec-targets-enterprise-scale/">With a stateless makeover, new MCP spec targets enterprise scale - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#LLM`, `#AI Agents`, `#Software Building`, `#Model Context Protocol`

---

<a id="item-10"></a>
## [llm-mcp-client 0.1a0: A New Tool for Model Context Protocol](https://simonwillison.net/2026/Jul/31/llm-mcp-client/#atom-everything) ⭐️ 9.0/10

llm-mcp-client 0.1a0 is a new open-source release that provides a client for the Model Context Protocol \(MCP\), enabling LLMs to interact with external tools and data sources. This release is significant for developers working with LLMs as it simplifies integrating AI systems with external tools, aligning with the growing trend of standardized AI protocols. The tool raises llm\_mcp\_client.MCPToolError for MCP errors, which the LLM passes back as an error message, and supports local development with \`uv run pytest\`.

rss · Simon Willison · Aug 1, 07:03

**Background**: The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 to standardize how LLMs integrate with external tools and data sources, enabling secure, two-way connections.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://github.com/simonw/llm-mcp-client">GitHub - simonw/ llm - mcp - client : Access tools from MCP servers as...</a></li>

</ul>
</details>

**Tags**: `#llm`, `#model-context-protocol`, `#open-source`, `#developer-tools`, `#ai`

---

<a id="item-11"></a>
## [Kubernetes v1.37 Sneak Peek: Planned Deprecations and Changes](https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/) ⭐️ 9.0/10

Kubernetes v1.37 introduces planned deprecations and removals, including the deprecation of the kubectl run --filename/-f flag, the prohibition of static pods referencing Secrets or ConfigMaps, and the deprecation of kube-proxy&\#x27;s ipvs mode. These changes are significant for maintaining and upgrading Kubernetes clusters, as they reflect the project&\#x27;s focus on improving overall health and guiding users toward better practices and features. The kubectl run --filename/-f flag is being deprecated because pods are now built purely from CLI arguments, and static pods can no longer reference Secrets or ConfigMaps due to a bug fix. The ipvs mode for kube-proxy is deprecated and will be disabled by default in v1.40 and removed entirely in v1.43.

rss · Kubernetes Blog · Aug 1, 00:00

**Background**: Kubernetes is an open-source container orchestration platform that automates deployment, scaling, and management of containerized applications. Deprecations and removals are part of the project&\#x27;s lifecycle to ensure long-term maintainability and adoption of newer features.

<details><summary>References</summary>
<ul>
<li><a href="https://kubernetes.io/blog/2026/07/31/kubernetes-v1-37-sneak-peek/">Kubernetes v1.37 Sneak Peek | Kubernetes</a></li>
<li><a href="https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands">Kubectl Reference Docs</a></li>
<li><a href="https://kubernetes.io/docs/reference/kubectl/kubectl/">kubectl | Kubernetes</a></li>

</ul>
</details>

**Tags**: `#Kubernetes`, `#Software Development`, `#Cloud-Native`, `#DevOps`, `#Kubectl`

---

<a id="item-12"></a>
## [Developer Trains Encoder-Only Transformer to Predict Blood Sugar](https://www.reddit.com/r/MachineLearning/comments/1vc1txc/i_have_trained_a_model_to_predict_my_blood_sugar_p/) ⭐️ 9.0/10

A developer trained an encoder-only transformer model to predict blood glucose levels using past and future health data, with multiple model variants and variants. This project demonstrates the practical application of machine learning in healthcare, specifically for diabetes management, and highlights the potential of transformer architectures in time-series prediction. The model uses BERT-style bidirectional attention with future blood glucose masked, employs DILATE and pinball loss functions, and is trained on multiple datasets including Ohiot1dm and Azt1d.

reddit · r/MachineLearning · /u/0xdeadf1sh · Aug 1, 04:09

**Background**: Blood glucose prediction is crucial for managing diabetes, and machine learning models can help users anticipate fluctuations. The encoder-only transformer architecture, similar to BERT, is well-suited for processing sequential data.

**Tags**: `#machine-learning`, `#transformer`, `#healthcare`, `#prediction-model`, `#diabetes`

---