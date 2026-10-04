---
layout: default
title: "Horizon Summary: 2026-10-04 (EN)"
date: 2026-10-04
content_date: 2026-10-03
lang: en
---

> Coverage: 2026-10-03 (Asia/Shanghai calendar day)

> From 52 items, 10 important content pieces were selected

---

1. [llama.cpp Release b11376 Fixes Flaky f16 Addition](#item-1) ⭐️ 10.0/10
2. [Microsoft ONNX Runtime v1.28.3 Patch Release](#item-2) ⭐️ 9.0/10
3. [Kolibri: A Sovereign Open-Weight Model](#item-3) ⭐️ 9.0/10
4. [Huawei&\#x27;s Tau Law Commercialized in Kirin 9050 Pro Chip](#item-4) ⭐️ 9.0/10
5. [Build Custom Video Pipelines with Cloudflare Stream and Workers](#item-5) ⭐️ 9.0/10
6. [OpenAI Safety Leader David Robinson Resigns](#item-6) ⭐️ 9.0/10
7. [Yangtze Memory IPO: 33 Billion RMB Fundraising Plan](#item-7) ⭐️ 9.0/10
8. [Chinese DRAM Manufacturer CXMT Files for IPO to Raise 29.5 Billion Yuan](#item-8) ⭐️ 9.0/10
9. [FTL: A New Cloud Operating System](#item-9) ⭐️ 8.0/10
10. [Google Antigravity Adds Opus 5.5 and Sonnet 5.5 Models](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp Release b11376 Fixes Flaky f16 Addition](https://github.com/ggml-org/llama.cpp/releases/tag/b11376) ⭐️ 10.0/10

The llama.cpp project released version b11376 to fix a flaky f16 addition operation and provides pre-built binaries for macOS, iOS, and Linux. This update improves the stability and reliability of local large language model inference, which is crucial for developers and users relying on llama.cpp for AI workloads. The fix addresses the flaky ADD\_ADD f16 operation by using a fused ADD tolerance mechanism, and the release includes extensive pre-built binaries for various platforms and hardware accelerators.

github · github-actions\[bot\] · Oct 3, 21:25

**Background**: llama.cpp is a C/C++ library designed for efficient local inference of large language models \(LLMs\) and vision language models \(VLMs\) across diverse hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases: ggml-org/llama.cpp - GitHub</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#Local LLM`, `#Software Engineering`, `#Open Source`

---

<a id="item-2"></a>
## [Microsoft ONNX Runtime v1.28.3 Patch Release](https://github.com/microsoft/onnxruntime/releases/tag/v1.28.3) ⭐️ 9.0/10

Microsoft released ONNX Runtime v1.28.3, a patch release addressing critical memory-safety vulnerabilities and model-validation bugs, including heap buffer overflow and out-of-bounds read issues. This release is significant for AI inference reliability as it fixes critical security vulnerabilities that could impact systems running machine learning models, ensuring safer and more stable execution environments. Key fixes include heap buffer overflow when reusing packed sub-byte buffers, out-of-bounds reads in ConvTransposeWithDynamicPads, and hardened shape inference for contrib operators like GroupQueryAttention and SparseAttention.

github · adrastogi · Oct 3, 04:48

**Background**: ONNX Runtime is a high-performance machine learning inference engine developed by Microsoft that executes models in the Open Neural Network Exchange \(ONNX\) format, widely used for deploying AI models across various platforms.

**Tags**: `#onnxruntime`, `#machine-learning`, `#memory-safety`, `#bug-fixes`, `#inference`

---

<a id="item-3"></a>
## [Kolibri: A Sovereign Open-Weight Model](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) ⭐️ 9.0/10

Aleph Alpha releases Kolibri, a sovereign open-weight model with detailed technical documentation and community-hosted benchmarks.

hackernews · bastitx · Oct 3, 17:36 · [Discussion](https://news.ycombinator.com/item?id=49942706)

**Tags**: `#AI`, `#Open Source`, `#Machine Learning`, `#Model Training`, `#Sovereign AI`

---

<a id="item-4"></a>
## [Huawei&\#x27;s Tau Law Commercialized in Kirin 9050 Pro Chip](https://pandabrief.com/archive/20261003.html) ⭐️ 9.0/10

Huawei has successfully commercialized its Tau Law algorithm within the Kirin 9050 Pro chip, marking a significant milestone in semiconductor design. This breakthrough highlights advancements in AI computing infrastructure and challenges traditional semiconductor scaling principles. The Tau Law replaces geometric scaling with time-domain compression, introducing high-frequency pulsed heat loads that pose thermal engineering challenges.

rss · PandaBrief - China Semiconductors · Oct 3, 15:57

**Background**: Huawei&\#x27;s Tau Law is a suite of advanced semiconductor design principles that propose time-domain scaling as a new guiding principle for semiconductor evolution, distinct from Moore&\#x27;s Law.

<details><summary>References</summary>
<ul>
<li><a href="https://chinascoop.org/huaweis-tau-law/">Huawei’s Tau Law - chinascoop.org</a></li>
<li><a href="https://www.huawei.com/en/news/2026/5/ieee-iscas-tau-scaling">HUAWEI Presents the Tau (τ) Scaling Law, Enabling ...</a></li>
<li><a href="https://semiconreport.org/en/articles/huawei-tau-scaling-law-reshapes-semiconductor-supply-chains">Huawei Tau Scaling Law Analysis: How to Bypass Export ...</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9050 Pro`, `#Tau Law`, `#AI Computing`, `#Semiconductors`

---

<a id="item-5"></a>
## [Build Custom Video Pipelines with Cloudflare Stream and Workers](https://blog.cloudflare.com/streamline/) ⭐️ 9.0/10

Cloudflare introduces &\#x27;Streamline&\#x27;, a solution that demonstrates how to build long-running, continuous video processing pipelines by combining Cloudflare Workers, Durable Objects, and a containerized media engine. This development empowers developers to create sophisticated video workflows on the edge, potentially reducing latency and costs compared to traditional server-based processing, and aligns with the growing trend of serverless computing for media tasks. The solution leverages Durable Objects for stateful management and Workers for compute, while the containerized media engine handles the actual video processing tasks, offering a flexible and scalable architecture.

rss · Cloudflare Blog · Oct 3, 00:13

**Background**: Cloudflare Workers are serverless functions that run on the edge, while Durable Objects are stateful counterparts that provide long-lived storage and compute capabilities within the serverless environment. Serverless video processing is an emerging paradigm that simplifies deployment and management of video workflows by abstracting away infrastructure concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/durable-objects/">Overview · Cloudflare Durable Objects docs</a></li>
<li><a href="https://www.cloudflare.com/products/durable-objects/">Cloudflare Durable Objects - Stateful Serverless Functions</a></li>

</ul>
</details>

**Tags**: `#cloudflare`, `#video-processing`, `#serverless`, `#durable-objects`, `#devops`

---

<a id="item-6"></a>
## [OpenAI Safety Leader David Robinson Resigns](https://www.businessinsider.com/safety-leader-david-robinson-resigns-from-openai-2026-10) ⭐️ 9.0/10

OpenAI&\#x27;s safety team leader, David Robinson, resigned on October 3, citing risks from iterative deployment and specific safety incidents like AI agent bypasses. This departure highlights ongoing challenges in AI safety alignment and could signal shifts in OpenAI&\#x27;s deployment strategies or internal safety culture. Robinson previously led policy planning and OpenAI&\#x27;s system card transparency efforts, including the development of model &\#x27;system cards&\#x27;.

telegram · zaihuapd · Oct 3, 20:20

**Background**: Iterative deployment is an OpenAI safety philosophy where AI systems are released and updated in stages to manage risks. System cards are transparency documents that detail a model&\#x27;s capabilities and safety measures.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/safety/how-we-think-about-safety-alignment/">How we think about safety and alignment | OpenAI</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-iterative-deployment-openai-ai-safety-strategy">What Is Iterative Deployment ? OpenAI&#x27;s Strategy for Releasing AI ...</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#OpenAI`, `#Machine Learning`, `#Policy`, `#Incident Report`

---

<a id="item-7"></a>
## [Yangtze Memory IPO: 33 Billion RMB Fundraising Plan](https://news.google.com/rss/articles/CBMiVEFVX3lxTFBoVUhVUVJtMFFMRkxLaFYzUnFFNlo2NzB0Y25XVW10N1VqOGVmQ2pHOHB3eF9jNWZEWnN6ekpjdjNzdEtkcVYxeFZqRmdvR1JDUmVuMA?oc=5) ⭐️ 9.0/10

Yangtze Memory Technologies has filed for a listing on the STAR Market of the Shanghai Stock Exchange, seeking to raise 33 billion RMB through the issuance of 1.98 to 2.43 billion shares. This IPO marks a significant milestone in China&\#x27;s semiconductor industry, as Yangtze Memory is a key player in domestic NAND flash memory production and aims to strengthen the AI computing infrastructure supply chain. The company&\#x27;s IPO application was accepted by the Shanghai Stock Exchange on August 21, 2026, and it is expected to be valued at 160 billion RMB, with potential annual profits exceeding 150 billion RMB by 2026.

google\_news · huxiu.com · Oct 3, 22:12

**Background**: Yangtze Memory is a leading Chinese manufacturer of NAND flash memory, competing with other domestic companies like CXMT \(ChangXin Memory Technologies\) to reduce reliance on foreign suppliers. The STAR Market is a special board of the Shanghai Stock Exchange designed to support innovative technology companies.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/2075275771065716869">长江存储330亿元IPO：2026年利润或超1500亿元，2万亿估值贵不贵</a></li>
<li><a href="https://finance.sina.com.cn/stock/estate/integration/2026-07-30/doc-inikrfcz4946333.shtml">长江存储IPO倒计时 湖北科投的十年投资答卷_新浪财经_新浪网</a></li>

</ul>
</details>

**Discussion**: The IPO has sparked discussions about the valuation of Yangtze Memory, with some analysts questioning whether the 2 trillion RMB market cap is justified given its profit projections.

**Tags**: `#semiconductors`, `#chip manufacturing`, `#IPO`, `#Yangtze Memory`, `#Wuhan chip industry`

---

<a id="item-8"></a>
## [Chinese DRAM Manufacturer CXMT Files for IPO to Raise 29.5 Billion Yuan](https://news.google.com/rss/articles/CBMijgFBVV95cUxNcTUxQTAySVlIb0NoTGpCR09pbWtqbWowVlE1ZXNuX1B5SWpsRHp2ZUdfUmlTNWlpUzkwcHNhMVI1R2IyQzdYdFF3dmNiZTZVSkF3bWJYQmlqTUJ2UG9LS0t6V0luNGJ6VWhSVWxUZy05eEhKYk0yOUdXZWxielR6ZnEwUWdYOUVncndiUll3?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies \(CXMT\), the world&\#x27;s fourth-largest DRAM manufacturer, has initiated the IPO process to raise approximately 29.5 billion yuan. This move highlights China&\#x27;s growing ambition in the semiconductor industry and could intensify competition in the global DRAM market, potentially impacting pricing and supply chains for AI hardware. Founded in 2016, CXMT specializes in DRAM production and aims to list on China&\#x27;s STAR Market, leveraging its products like LPDDR5/5X to challenge established players.

google\_news · 朝鮮日報中文版 · Oct 3, 15:44

**Background**: DRAM \(Dynamic Random Access Memory\) is a critical component for mobile devices, PCs, and servers, including AI workloads. CXMT, headquartered in Hefei, Anhui, has been expanding its market share, now controlling around 7.7% of the global DRAM market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.cxmt.com/en/">About cxmt - cxmt</a></li>
<li><a href="https://finance.yahoo.com/quote/688825.SS/">CXMT Corporation (688825.SS) Stock Price, News... - Yahoo Finance</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#Semiconductors`, `#AI Hardware`, `#IPO`, `#China`

---

<a id="item-9"></a>
## [FTL: A New Cloud Operating System](https://ftl-os.org/) ⭐️ 8.0/10

FTL is a new hybrid kernel-based operating system project that allows users to maximize software architecture flexibility, with version 0.1.0 recently shipped. This project addresses the security risks of shared kernels in Linux containers by providing hardware-based isolation for each container, potentially making lightweight containers as secure as virtual machines. FTL treats the operating system as a shared library, enabling developers to build isolated userspace OS instances inside containers while maintaining full Linux binary compatibility.

hackernews · romac · Oct 3, 23:02 · [Discussion](https://news.ycombinator.com/item?id=49944912)

**Background**: Traditional Linux containers share a kernel, which can be a security liability. FTL addresses this by giving each container its own isolated userspace OS instance, inspired by the limitations of shared kernels in cloud-native environments.

<details><summary>References</summary>
<ul>
<li><a href="https://seiya.me/blog/introducing-ftl">Introducing FTL: A new operating system for clouds</a></li>
<li><a href="https://news.lavx.hu/article/ftl-builds-operating-systems-as-libraries-for-cloud-containers">FTL builds operating systems as libraries for cloud containers</a></li>
<li><a href="https://byteiota.com/ftl-cloud-os-ships-linux-containers-get-vm-isolation/">FTL Cloud OS Ships: Linux Containers Get VM Isolation</a></li>

</ul>
</details>

**Discussion**: Community members are exploring FTL&\#x27;s architecture and hardware constraints, with some questioning its scalability and professional maturity compared to established systems like GNU.

**Tags**: `#operating-systems`, `#cloud-native`, `#software-engineering`, `#open-source`, `#developer-tools`

---

<a id="item-10"></a>
## [Google Antigravity Adds Opus 5.5 and Sonnet 5.5 Models](https://www.reddit.com/r/google_antigravity/comments/1wwfcav/google_finally_added_opus_55_and_sonnet_55_on) ⭐️ 8.0/10

Google Antigravity has introduced the Opus 5.5 and Sonnet 5.5 models, with third-party model access restricted to paid Pro and Ultra tiers after November 2. This update impacts developers using Google Antigravity by limiting access to advanced AI models, potentially affecting workflows and requiring subscription upgrades for full functionality. The Opus 5.5 model is designed for complex tasks requiring careful judgment, while Sonnet 5.5 offers a faster, lower-cost alternative with similar performance in coding benchmarks.

telegram · zaihuapd · Oct 3, 14:32

**Background**: Google Antigravity is an AI-powered IDE that integrates Gemini for code suggestions and autonomous agent orchestration. The Opus and Sonnet models are part of Anthropic&\#x27;s Claude family, with Sonnet 5.5 being a faster, cheaper option compared to Opus 5.5.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity</a></li>
<li><a href="https://antigravity.google/">Google Antigravity</a></li>

</ul>
</details>

**Tags**: `#AI Models`, `#Google`, `#Software Updates`, `#Paid Tiers`, `#Model Release`

---