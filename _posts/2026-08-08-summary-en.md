---
layout: default
title: "Horizon Summary: 2026-08-08 (EN)"
date: 2026-08-08
content_date: 2026-08-07
lang: en
---

> Coverage: 2026-08-07 (Asia/Shanghai calendar day)

> From 102 items, 12 important content pieces were selected

---

1. [llama.cpp b10301 Release Adds CUDA Fix and Cross-Platform Binaries](#item-1) ⭐️ 10.0/10
2. [Datasette 1.0a38 Fixes Critical SQL Injection Vulnerability](#item-2) ⭐️ 10.0/10
3. [SK Hynix Confirms 375-Layer V10 NAND with Wafer Bonding](#item-3) ⭐️ 10.0/10
4. [sub2api OAuth Vulnerability Allows Account Takeover via Email](#item-4) ⭐️ 10.0/10
5. [Making Postgres 300x Faster for Analytics](#item-5) ⭐️ 9.0/10
6. [2027 Memory Capacity Reportedly Sold Out](#item-6) ⭐️ 9.0/10
7. [Datasette 0.65.3 Backports SQL Injection Security Fix](#item-7) ⭐️ 9.0/10
8. [DeepMind&\#x27;s Strategic Failures Benefit Google Cloud Platform](#item-8) ⭐️ 9.0/10
9. [Cloudflare Introduces Continuous Trust Evaluation for Bots and Agents](#item-9) ⭐️ 9.0/10
10. [Cloudflare Unifies Workers AI and AI Gateway into a Single Control Plane](#item-10) ⭐️ 9.0/10
11. [MLP Classifier Trained on Android Phone](#item-11) ⭐️ 9.0/10
12. [Improved Neural Network Compression of Bad Apple Video](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10301 Release Adds CUDA Fix and Cross-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10301) ⭐️ 10.0/10

The b10301 release of llama.cpp fixes CUDA warnings for unused variables and functions, while providing pre-built binaries for macOS, iOS, Linux, Android, and Windows across various architectures. This release significantly improves the usability and performance of llama.cpp, a leading open-source LLM inference engine, by addressing CUDA compatibility issues and ensuring broad hardware support. The CUDA fix addresses compiler warnings, and the release includes disabled KleidiAI support for macOS Apple Silicon, alongside extensive binary options for different platforms and accelerators like Vulkan, ROCm, and OpenVINO.

github · github-actions\[bot\] · Aug 7, 17:59

**Background**: llama.cpp is an open-source library for running large language models locally, often used as the core of tools like Ollama and LM Studio. CUDA is Nvidia&\#x27;s parallel computing platform enabling GPU acceleration for AI tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cuda_framework">Cuda framework</a></li>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/kleidiai: This repository is a read-only mirror of https://gitlab.arm.com/kleidi/kleidiai · GitHub</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#open-source`, `#CUDA`, `#macOS`

---

<a id="item-2"></a>
## [Datasette 1.0a38 Fixes Critical SQL Injection Vulnerability](https://simonwillison.net/2026/Aug/6/datasette/#atom-everything) ⭐️ 10.0/10

Datasette 1.0a38 fixes a critical SQL injection vulnerability that affects instances serving mixed public and private tables with Datasette&\#x27;s permissions system. This security fix is significant for administrators who expose private tables, as it prevents unauthorized access to sensitive data through SQL injection attacks. The vulnerability allowed users with access to public tables to execute SQL injection attacks, bypassing restrictions to read private table data. Administrators are advised to disable the &\#x27;execute-sql&\#x27; permission on affected databases.

rss · Simon Willison · Aug 7, 02:24

**Background**: Datasette is an open-source tool for exploring and publishing data, featuring a permissions system to control access to databases and tables. The authentication system allows administrators to restrict access based on user roles.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.datasette.io/en/latest/authentication.html">Authentication and permissions - Datasette documentation</a></li>
<li><a href="https://simonw.substack.com/p/a-new-sql-powered-permissions-system">A new SQL-powered permissions system in Datasette 1.0a20</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#security`, `#sql-injection`, `#developer-tools`, `#data-centric`

---

<a id="item-3"></a>
## [SK Hynix Confirms 375-Layer V10 NAND with Wafer Bonding](https://www.gelonghui.com/live/2599953) ⭐️ 10.0/10

SK Hynix announced at FMS 2026 that its new V10 NAND flash memory uses a 375-layer stacking design and is the company&\#x27;s first product to incorporate wafer bonding technology. This advancement is significant for the semiconductor industry as it pushes the boundaries of 3D NAND stacking and introduces wafer bonding, which is crucial for future high-density memory solutions. The V10 NAND achieves 2.5x performance per watt compared to its predecessor, the 321-layer V9, and is specifically optimized for AI infrastructure environments requiring a balance of energy efficiency and performance.

telegram · zaihuapd · Aug 7, 20:19

**Background**: 3D NAND flash memory stacks memory cells vertically to increase density, with SK Hynix&\#x27;s V9 being a 321-layer 4D NAND. Wafer bonding is a technique used to join two semiconductor wafers, enabling advanced packaging and higher layer counts.

<details><summary>References</summary>
<ul>
<li><a href="https://m.163.com/dy/article/KV4PG1NG0550WHYR.html">SK海力士V10 NAND 采用 375 层 堆 叠 设计 2026年内量产_手机网易网</a></li>
<li><a href="https://www.chinaflashmarket.com/a/183951">375 层 ！ SK海力士下一代 NAND 年底前量产_CFM 闪 存 市场</a></li>

</ul>
</details>

**Tags**: `#NAND Flash`, `#Semiconductors`, `#AI Infrastructure`, `#SK Hynix`, `#Wafer Bonding`

---

<a id="item-4"></a>
## [sub2api OAuth Vulnerability Allows Account Takeover via Email](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 10.0/10

sub2api versions prior to v0.1.171 contain a critical OAuth account takeover vulnerability \(CVSS 8.8\) that allows attackers to bind their OAuth identity to a victim&\#x27;s account using only the victim&\#x27;s email address, without requiring a password, verification code, or user interaction. This vulnerability is highly significant because it enables complete account control, including API keys, billing balances, and subscription quotas, posing a severe risk to users of the sub2api service and highlighting critical flaws in OAuth implementation that could affect similar systems. The exploit leverages a flaw in the pending session flow where the existingUser branch fails to validate passwords and verification codes, allowing attackers to set the target user ID to the victim and complete OAuth identity binding, after which all OAuth logins are parsed as the victim&\#x27;s account.

telegram · zaihuapd · Aug 7, 22:59

**Background**: OAuth is an open standard for authorization that allows users to grant third-party applications limited access to their accounts without sharing passwords, but misconfigurations in the authorization flow can lead to severe security vulnerabilities like account takeover.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Wei-Shaw/sub2api/security/advisories/GHSA-vc2q-289v-74g3">Password Reset Poisoning via Host Header Trust Issue Leading to Account Takeover · Advisory · Wei-Shaw/sub2api · GitHub</a></li>
<li><a href="https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow">Lab: Authentication bypass via OAuth implicit flow | Web Security Academy</a></li>
<li><a href="https://gaya3-r.medium.com/account-takeover-using-oauth-misconfiguration-3fab424317c1">Account takeover using OAuth Misconfiguration | by gayatri r | Medium</a></li>

</ul>
</details>

**Tags**: `#OAuth`, `#Security`, `#Account Takeover`, `#Vulnerability`, `#sub2api`

---

<a id="item-5"></a>
## [Making Postgres 300x Faster for Analytics](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 9.0/10

The author implemented pgrust, a Rust-based extension for Postgres, achieving 300x speedup for analytics queries through batching, operator fusion, and SIMD. This breakthrough addresses Postgres&\#x27;s traditional performance limitations in analytics, potentially making it a more competitive option for data-heavy workloads. The optimization involved formal verification and differential fuzz testing to ensure correctness, proving over 1000 user-facing functions have identical logic in both pgrust and Postgres.

hackernews · poly2it · Aug 7, 19:00 · [Discussion](https://news.ycombinator.com/item?id=49208535)

**Background**: SIMD \(Single Instruction, Multiple Data\) allows CPUs to process multiple data elements in parallel, while operator fusion reduces memory traffic by merging sequential operations. Batching improves efficiency by processing data in groups rather than individually.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@enerzai/optimium-101-3-optimium-utilized-operator-fusion-the-attack-was-super-effective-f2fc43d47d9b">Optimium 101 (3): Optimium utilized Operator Fusion ! | Medium</a></li>
<li><a href="https://www.starrocks.io/blog/deep-dive-how-starrocks-built-a-high-performance-vectorized-engine/index.html">Deep Dive: How StarRocks Built a High- Performance Vectorized Engine</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about the technical depth but raised concerns about adoption, noting that trust and longevity are critical factors beyond performance.

**Tags**: `#Postgres`, `#Query Optimization`, `#SIMD`, `#Software Engineering`, `#Database Performance`

---

<a id="item-6"></a>
## [2027 Memory Capacity Reportedly Sold Out](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 9.0/10

A report indicates that memory capacity for the year 2027 is fully sold out, driven by high demand from AI applications and production constraints. This shortage highlights the critical role of memory in AI infrastructure and the challenges in scaling production to meet growing computational needs. HBM production consumes significantly more wafer capacity than standard DRAM, with HBM3E requiring approximately three times the wafer supply of DDR5 for the same number of bits.

hackernews · inigyou · Aug 7, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49207236)

**Background**: High Bandwidth Memory \(HBM\) is a 3D-stacked memory technology used in AI accelerators and high-performance GPUs. Its vertical stacking and high-speed interfaces make it essential for AI workloads, but manufacturing constraints limit its scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://oretonstorage.com/blog/as-hbm-demand-surges-with-ai-growth-ddr-supply-dynamics-are-shifting-we-analyze-wafer-allocation-packaging-bottlenecks-and-dram-pricing-implications">How HBM Production Is Constraining DDR Supply</a></li>

</ul>
</details>

**Discussion**: Users discuss the impact of memory shortages on their setups, with some noting price increases and others expressing concerns about AI&\#x27;s growing memory demands.

**Tags**: `#HBM`, `#DRAM`, `#AI`, `#Memory`, `#Semiconductors`

---

<a id="item-7"></a>
## [Datasette 0.65.3 Backports SQL Injection Security Fix](https://simonwillison.net/2026/Aug/6/datasette-2/#atom-everything) ⭐️ 9.0/10

Datasette 0.65.3 back-ports a SQL Injection security fix from version 1.0a38, addressing vulnerabilities in instances serving mixed public and private tables. This security fix is critical for users running Datasette with mixed access permissions, as it prevents potential data breaches and unauthorized database manipulation. The fix addresses SQL injection vulnerabilities that arise when dynamic field names are used in queries, likely involving parameterized queries or input validation improvements.

rss · Simon Willison · Aug 7, 02:22

**Background**: Datasette is an open-source tool for exploring and publishing data, treating SQLite databases as read-only to minimize security risks like SQL injection. The security issue in 1.0a38 affected instances with mixed public and private tables, where the Datasette permissions system could be exploited.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.datasette.io/en/latest/sql_queries.html">Running SQL queries - Datasette documentation</a></li>
<li><a href="https://simonwillison.net/2026/Aug/6/datasette/">Release: datasette 1.0a38</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#security`, `#sql-injection`, `#software-release`, `#python`

---

<a id="item-8"></a>
## [DeepMind&\#x27;s Strategic Failures Benefit Google Cloud Platform](https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking) ⭐️ 9.0/10

Google Cloud Platform \(GCP\) is gaining market share as DeepMind&\#x27;s strategic focus shifts away from frontier AI competitiveness, leading to a reallocation of resources. This shift highlights the tension between short-term financialization and long-term innovation in the AI industry, with significant implications for competitors and investors. GCP now generates $200 billion in external sales with high margins, while DeepMind&\#x27;s first-party business remains at $12 billion, indicating a clear management priority.

rss · Semianalysis · Aug 7, 10:32

**Background**: Google acquired DeepMind in 2014 to gain research capacity and prestige, but recent strategic missteps have prioritized GCP&\#x27;s financial performance over frontier AI leadership.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking">or why DeepMind &#x27;s long term failure is GCP &#x27;s short term gain</a></li>
<li><a href="https://beneficial.cloud/attracting-ai-talent-lessons-from-google-deepmind-s-acquisit">Attracting AI Talent: Lessons from DeepMind</a></li>
<li><a href="https://startupshortcut.com/knowledge-base/how-google-deepmind-mastered-ai-for-strategic-growth-and-innovation">How Google DeepMind Drove AI Growth &amp; Innovation | StartupShortcut</a></li>

</ul>
</details>

**Tags**: `#AI Compute`, `#Google Cloud`, `#DeepMind`, `#Strategic Analysis`, `#AI Infrastructure`

---

<a id="item-9"></a>
## [Cloudflare Introduces Continuous Trust Evaluation for Bots and Agents](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/) ⭐️ 9.0/10

Cloudflare is shifting bot mitigation from point-in-time risk assessment to continuous trust evaluation, introducing systems like BotBase and Precursor to assess good and bad behaviors, and offering a Precursor Trace simulation tool to evaluate cursor movements. This shift to continuous trust evaluation improves detection precision for distinguishing real users from automation without relying on aggressive challenges, benefiting legitimate users by reducing unnecessary interruptions and raising the cost for bot developers. Precursor runs ongoing verification in the browser to detect automation that appears legitimate in individual requests but exhibits non-human patterns across a session, while BotBase and Precursor monitor user behavior across entire sessions to catch sophisticated bots.

rss · Cloudflare Blog · Aug 7, 21:01

**Background**: Traditional bot mitigation often relies on point-in-time risk assessments, but Cloudflare&\#x27;s new approach uses continuous client-side signals and session-long analysis to better distinguish humans from machines, aligning with broader trends in continuous adaptive trust solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/good-and-bad-agentic-behaviors/">Unveiling good and bad behaviors on the Agentic Internet | Cloudflare Blog</a></li>
<li><a href="https://blog.cloudflare.com/introducing-precursor/">Introducing Precursor: detecting agentic behavior with continuous client-side signals | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-challenges/precursor/">Precursor · Cloudflare challenges docs</a></li>

</ul>
</details>

**Tags**: `#bot-mitigation`, `#ai-security`, `#cloudflare`, `#trust-evaluation`, `#simulation`

---

<a id="item-10"></a>
## [Cloudflare Unifies Workers AI and AI Gateway into a Single Control Plane](https://blog.cloudflare.com/workers-ai-gateway-unification/) ⭐️ 9.0/10

Cloudflare has unified Workers AI and AI Gateway into a single control plane, providing developers with unified observability, billing, and dynamic routing across managed GPUs and external AI providers. This unification simplifies building resilient AI applications by centralizing management and improving resource allocation, which is critical for enterprises adopting AI at scale. The unified control plane introduces unified bindings and model-first routing, enabling seamless integration and dynamic selection of AI models and providers.

rss · Cloudflare Blog · Aug 7, 21:00

**Background**: An AI control plane is a critical layer that governs AI interactions by enforcing policies, ensuring compliance, and providing visibility across models and agents. Dynamic routing enhances efficiency by dynamically selecting the optimal model or provider based on input and context.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/workers-ai-gateway-unification/">Unifying Workers AI and AI Gateway into a single AI control plane | Cloudflare Blog</a></li>
<li><a href="https://www.linkedin.com/pulse/rise-ai-control-planes-governing-models-agents-scale-mahmoud-abufadda-d1f5f">The Rise of AI Control Planes : Governing Models, Agents and...</a></li>
<li><a href="https://www.areebi.com/ai-control-plane">AI Control Plane - Areebi | Areebi</a></li>

</ul>
</details>

**Tags**: `#AI Gateway`, `#Workers AI`, `#Cloudflare`, `#AI Control Plane`, `#Developer Tools`

---

<a id="item-11"></a>
## [MLP Classifier Trained on Android Phone](https://www.reddit.com/r/MachineLearning/comments/1vhwwfr/imagenet1k_classifier_trained_entirely_on_an/) ⭐️ 9.0/10

A researcher trained a small MLP classifier on an Android phone using PyTorch and Termux, achieving Top-1 validation accuracy of 4.59% on a downscaled Imagenet-1k dataset. This demonstrates the feasibility of on-device training for edge AI, potentially enabling privacy-preserving and resource-efficient machine learning applications on mobile devices. The model used 500K parameters, trained on 32x32 images for 5 epochs in 30 minutes using the Dimensity 9300+ CPU&\#x27;s 4 Cortex-X4 cores, with PyArrow for dataset handling.

reddit · r/MachineLearning · /u/Tall\_Abrocoma\_3533 · Aug 7, 18:30

**Background**: Termux is a terminal emulator for Android that extends functionality with packages like PyTorch, while Imagenet-1k is a standard dataset for image classification benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Building_Android_applications_in_Termux_using_Gradle">Building Android applications in Termux using Gradle</a></li>
<li><a href="https://arrow.apache.org/docs/python/generated/pyarrow.dataset.Dataset.html">pyarrow . dataset . Dataset — Apache Arrow v25.0.0</a></li>

</ul>
</details>

**Tags**: `#on-device-ml`, `#mobile-computing`, `#pytorch`, `#edge-ai`, `#hardware-software-co-design`

---

<a id="item-12"></a>
## [Improved Neural Network Compression of Bad Apple Video](https://www.reddit.com/r/MachineLearning/comments/1vhvfws/improved_compression_of_bad_apple_into_a_neural/) ⭐️ 9.0/10

The author improved a neural network-based video compression model for the &\#x27;Bad Apple&\#x27; video by using a different batch sampler and feeding pixels across the entire video, achieving more faithful reproduction with the same 4x512 wide sine layers and 792,257 parameters. This advancement demonstrates the potential of implicit neural representations for video compression, offering insights into model architecture and training strategies that could benefit the broader field of AI-driven media compression. The model, reimplemented using GPT5.6, suffers from poor quality in full-frame-rate mode as it cannot learn motion and produces nonsensical intermediate frames, though the low-rate version maintains high fidelity.

reddit · r/MachineLearning · /u/cpldcpu · Aug 7, 17:06

**Background**: Implicit neural representations, such as SIREN networks, encode data as continuous functions, enabling high-fidelity reconstruction from sparse inputs, and are increasingly used in video compression tasks alongside traditional codecs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>
<li><a href="https://reelmind.ai/blog/neural-network-video-compression-technology">Neural Network Video Compression Technology | ReelMind</a></li>

</ul>
</details>

**Tags**: `#neural-networks`, `#video-compression`, `#machine-learning`, `#siren-network`, `#gpt5.6`

---