---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
content_date: 2026-08-02
lang: en
---

> Coverage: 2026-08-02 (Asia/Shanghai calendar day)

> From 101 items, 12 important content pieces were selected

---

1. [llama.cpp b10228 adds DeepseekV4 MTP and DSpark support](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10225 Release: MiMo V2 MTP Optimization and Multi-Platform Binaries](#item-2) ⭐️ 10.0/10
3. [长鑫存储LPDDR6接近研发验证尾声 设计规格速率达12800Mbps - 观点网](#item-3) ⭐️ 10.0/10
4. [Karpathy&\#x27;s Pelican: AI Generates Physical World Benchmarks](#item-4) ⭐️ 9.0/10
5. [datasette-apps 0.2a0: New Debugging Tools for Datasette Agent](#item-5) ⭐️ 9.0/10
6. [OpenAI&\#x27;s Astra Model Solves Ten Long-Standing Math Problems](#item-6) ⭐️ 9.0/10
7. [CausalVLBench: Benchmarking Visual Causal Reasoning in Large VLMs](#item-7) ⭐️ 9.0/10
8. [Seeking Pipeline for Converting Academic Textbook Figures to Editable Assets](#item-8) ⭐️ 9.0/10
9. [AI Chip Count to Double Every 9 Months, Reaching 200 Million by End of 2028](#item-9) ⭐️ 9.0/10
10. [Apple Limits Vulnerability Report Submissions to Counter AI-Generated Low-Quality Reports](#item-10) ⭐️ 9.0/10
11. [ChangXin&\#x27;s Breakout: Catching Up to Samsung and Micron](#item-11) ⭐️ 9.0/10
12. [ChangXin Memory Technologies Valuation Exceeds 3 Trillion Yuan](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10228 adds DeepseekV4 MTP and DSpark support](https://github.com/ggml-org/llama.cpp/releases/tag/b10228) ⭐️ 10.0/10

The llama.cpp project released version b10228, introducing support for DeepseekV4 MTP and DSpark speculative decoding, along with pre-built binaries for macOS, iOS, and Linux. This release significantly enhances the inference capabilities of llama.cpp by supporting advanced speculative decoding techniques like DSpark, which can improve generation speed and throughput for DeepSeek-V4 models. The release includes extensive cross-platform binaries for macOS, iOS, Linux, and Windows, supporting various hardware accelerators like CUDA, Vulkan, ROCm, and OpenVINO, while the macOS Apple Silicon build with KleidiAI is currently disabled.

github · github-actions\[bot\] · Aug 2, 21:28

**Background**: llama.cpp is a high-performance, open-source inference engine for large language models, optimized for CPU and GPU execution. DeepseekV4 MTP \(Multi-Token Prediction\) is a technique used in vLLM for efficient model loading, while DSpark is a speculative decoding method that accelerates generation by accepting more tokens from a draft model.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/issues/25096">Feature Request: DSpark confidence-scheduled verification &amp; semi-autoregressive drafting · Issue #25096 · ggml-org/llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/25167">Support DeepSeek DSpark speculative decoding · ggml-org/llama.cpp · Discussion #25167</a></li>
<li><a href="https://docs.vllm.ai/en/stable/api/vllm/model_executor/models/deepseek_v4_mtp/">deepseek _ v 4 _ mtp - vLLM</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI`, `#Open Source`, `#Machine Learning`, `#Cross Platform`

---

<a id="item-2"></a>
## [llama.cpp b10225 Release: MiMo V2 MTP Optimization and Multi-Platform Binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10225) ⭐️ 10.0/10

The llama.cpp project released version b10225, introducing a new model loading optimization that loads MiMo V2 MTP tensors only when needed, along with pre-built binaries for macOS, Linux, iOS, Android, and Windows. This release significantly improves the efficiency of running large language models by reducing unnecessary memory usage and provides ready-to-use binaries for a wide range of platforms, making it easier for developers and users to deploy AI inference. The optimization specifically targets the MiMo V2 MTP tensors, and while KleidiAI support for macOS Apple Silicon is disabled, the release includes extensive platform-specific builds, including CUDA 12 and 13 support for Windows.

github · github-actions\[bot\] · Aug 2, 16:30

**Background**: llama.cpp is a high-performance C++ library for running large language models \(LLMs\) on consumer hardware, known for its efficiency and cross-platform support. MiMo V2 MTP is a tensor format used in some AI models, and KleidiAI is an ARM-optimized micro-kernel library for AI performance.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/kleidiai">Arm KleidiAI: Helping AI frameworks elevate ...</a></li>

</ul>
</details>

**Tags**: `#llama.cpp`, `#AI inference`, `#software engineering`, `#open-source`, `#machine learning`

---

<a id="item-3"></a>
## [长鑫存储LPDDR6接近研发验证尾声 设计规格速率达12800Mbps - 观点网](https://news.google.com/rss/articles/CBMiTkFVX3lxTFBPZHQ5cy0tckxfTldsZm1SdEwwOEplTWpwekozZEtIMDk4OGlSYTgyNm9rZGpVNVJHU0c4M3Q1bWh4ZlUydmJHSG9FWXdhQQ?oc=5) ⭐️ 10.0/10

CXMT&\#x27;s LPDDR6 memory is nearing verification with a design speed of 12800Mbps.

google\_news · 观点网 · Aug 2, 21:13

**Tags**: `#semiconductors`, `#memory`, `#LPDDR6`, `#AI hardware`, `#CXMT`

---

<a id="item-4"></a>
## [Karpathy&\#x27;s Pelican: AI Generates Physical World Benchmarks](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 9.0/10

Andrej Karpathy demonstrated a new benchmark called Pelican, where the Claude Opus 5 model generated a 3D Three.js rendering of the first paragraph of &\#x27;The Lord of the Rings&\#x27; using a 1M token budget \(~$10\). This project represents a shift in AI testing from simple prompts to complex physical world benchmarks, which could better expose an AI&\#x27;s understanding of the physical world and help measure future progress. The generated code was procedural and somewhat &\#x27;janky&\#x27;, but it successfully placed and arranged 3D elements to tell a story, marking a departure from simple image generation tasks.

hackernews · delichon · Aug 2, 12:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: Andrej Karpathy, a former OpenAI founding member and Tesla AI director, joined Anthropic to lead frontier LLM research. The Pelican benchmark is an attempt to move beyond testing LLMs with simple prompts like &\#x27;create an svg of pelican on a bicycle&\#x27;.

<details><summary>References</summary>
<ul>
<li><a href="https://xcancel.com/karpathy/status/2083749667410727319">Andrej Karpathy (@karpathy): &quot;We&#x27;re starting to leave the territory where you&#x27;d test an LLM by e.g. &quot;create an svg of pelican on a bicycle&quot;. As one idea to generalize it, I was interested what Opus 5 would do if I gave it the first paragraph of the Lord of the Rings, a 1M token budget (~$10) and asked for three js render of it. Opus went off for ~2 hours and wrote 5500 lines of code that (procedurally) rendered the story. It&#x27;s kind of janky but fun. But it&#x27;s a bit mindboggling that the LLM has to place and</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/08/60861644/andrej-karpathy-says-ai-has-moved-beyond-simple-prompts-after-claude-opus-builds-3d-lord-of-the-rings-world">Andrej Karpathy Says AI Has Moved Beyond Simple Prompts After Claude Opus Builds 3D Lord of the Rings Wor - Benzinga</a></li>
<li><a href="https://simonwillison.net/2025/Feb/6/andrej-karpathy/">A quote from Andrej Karpathy | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Discussion**: Users debated the reproducibility of the project, noting that unlike Simon&\#x27;s pelican, the prompt was not visible. Others discussed how this type of benchmark better exposes physical understanding and how Anthropic models seem specifically tuned for Three.js code generation.

**Tags**: `#AI`, `#Machine Learning`, `#Reproducibility`, `#Benchmarks`, `#Generative AI`

---

<a id="item-5"></a>
## [datasette-apps 0.2a0: New Debugging Tools for Datasette Agent](https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything) ⭐️ 9.0/10

The datasette-apps 0.2a0 release introduces two new tools for Datasette Agent: \`app\_debug\(\)\` for testing apps invisibly and \`app\_list\(\)\` for listing editable apps. These tools enhance the software development workflow by enabling automated testing and management of Datasette Apps, making it easier for developers to ensure app reliability and access control. The \`app\_debug\(\)\` tool uses an invisible iframe with \`opacity: 0\` and \`pointer-events: none\` to execute JavaScript in a sandboxed environment, allowing smoke testing and element measurement.

rss · Simon Willison · Aug 2, 05:23

**Background**: Datasette Agent is an AI assistant for exploring and querying data in Datasette, while Datasette Apps are single-file HTML applications hosted inside Datasette itself.

<details><summary>References</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette / datasette - agent : An LLM-powered agent for...</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-apps/">Host applications inside Datasette with Datasette ... - Datasette Blog</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#developer-tools`, `#software-engineering`, `#testing`, `#agent`

---

<a id="item-6"></a>
## [OpenAI&\#x27;s Astra Model Solves Ten Long-Standing Math Problems](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 9.0/10

OpenAI&\#x27;s internal model Astra reportedly solved ten unsolved mathematical problems, spending less than $2,000 on GPT-5.6 Sol token prices for each. This breakthrough demonstrates the potential of AI to tackle complex, long-standing problems in mathematics and theoretical computer science, marking a significant step in AI reasoning capabilities. The results are available in an open-source repository with Lean 4 formalizations, a paper describing the solutions, and an LLM-generated PDF reconstructing the reasoning process.

rss · Simon Willison · Aug 2, 04:34

**Background**: Lean 4 is a proof assistant and interactive theorem prover used for formalizing mathematical proofs, ensuring rigor and verifiability in mathematical reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://digg.com/tech/9qjs9782">OpenAI Astra Model Solves Ten Open Problems · Digg</a></li>
<li><a href="https://github.com/openai/ten-proofs">GitHub - openai / ten - proofs : Lean certificates accompanying proofs in...</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT - 5 . 6 Sol - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mathematics`, `#OpenAI`, `#Research`, `#Computing`

---

<a id="item-7"></a>
## [CausalVLBench: Benchmarking Visual Causal Reasoning in Large VLMs](https://www.reddit.com/r/MachineLearning/comments/1vdd7ty/r_causalvlbench_benchmarking_visual_causal/) ⭐️ 9.0/10

CausalVLBench is a new benchmark designed to evaluate visual causal reasoning capabilities in large vision-language models \(VLMs\), covering tasks like causal structure inference, intervention target prediction, and counterfactual prediction. This benchmark addresses a critical gap in VLM evaluation by focusing on causal reasoning, which is essential for understanding cause-effect relationships in visual data and improving model reliability. CausalVLBench tests eight vision-language model families across three causal tasks, revealing significant reasoning gaps and challenging current machine learning capabilities.

reddit · r/MachineLearning · /u/moschles · Aug 2, 17:07

**Background**: Causal reasoning involves identifying cause-effect relationships, a fundamental cognitive process used in predictions and decision-making. Large vision-language models \(VLMs\) combine visual and textual understanding but often struggle with complex reasoning tasks like causal inference.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2506.11034v2">CausalVLBench : Benchmarking Visual Causal Reasoning in Large...</a></li>
<li><a href="https://www.remio.ai/post/causalvlbench-pushes-visual-ai-beyond-recognition-and-exposes-a-reasoning-gap">CausalVLBench Pushes Visual AI Beyond Recognition, and Exposes...</a></li>
<li><a href="https://huggingface.co/papers/2506.11034">Paper page - CausalVLBench : Benchmarking Visual Causal...</a></li>

</ul>
</details>

**Tags**: `#Large Vision-Language Models`, `#Benchmarking`, `#Causal Reasoning`, `#AI Evaluation`, `#Computer Vision`

---

<a id="item-8"></a>
## [Seeking Pipeline for Converting Academic Textbook Figures to Editable Assets](https://www.reddit.com/r/MachineLearning/comments/1vdlj8j/looking_for_the_right_pipeline_to_convert/) ⭐️ 9.0/10

A developer is seeking advice on building a human-assisted pipeline to detect, segment, and clean figures from scanned academic textbook pages, converting them into structured digital representations for frontend rendering. This project addresses the challenge of digitizing educational content, enabling interactive and customizable figure rendering that can enhance learning experiences and support document understanding systems. The workflow involves figure detection, label removal via image inpainting, and storing geometry data, with a focus on low-cost inference and human-in-the-loop correction for accuracy.

reddit · r/MachineLearning · /u/Afraid\_Reviewer · Aug 2, 23:50

**Background**: Document understanding pipelines often combine multiple ML models for layout analysis, text detection, and segmentation, while techniques like region-based segmentation and morphological labeling help separate text from non-text regions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mdpi.com/2078-2489/17/2/165">Decoding Technical Diagrams: A Survey of AI Methods for Image Content Extraction and Understanding</a></li>
<li><a href="https://arxiv.org/html/2410.21721v1">DiffSTR: Controlled Diffusion Models for Scene Text Removal</a></li>
<li><a href="https://www.paddleocr.ai/v3.3.1/en/version3.x/pipeline_usage/doc_understanding.html">Document Understanding Pipeline - PaddleOCR Documentation</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#document processing`, `#AI pipeline`, `#image segmentation`, `#frontend integration`

---

<a id="item-9"></a>
## [AI Chip Count to Double Every 9 Months, Reaching 200 Million by End of 2028](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html) ⭐️ 9.0/10

Epoch AI estimates that the global number of AI chips will double every nine months, reaching approximately 200 million by the end of 2028, a tenfold increase from the current 20 million. This exponential growth underscores the critical role of AI infrastructure in the global economy and highlights the intensifying geopolitical competition for AI chip manufacturing dominance. IDC forecasts global AI infrastructure investment to exceed $1 trillion by 2029, up from $318 billion last year, while the US controls about 80% of global AI computing power.

telegram · zaihuapd · Aug 2, 09:01

**Background**: The surge in AI chip demand is driven by the &\#x27;scale law,&\#x27; which posits that larger compute resources lead to stronger AI capabilities. This trend is further accelerated by tech giants&\#x27; massive infrastructure investments and the geopolitical race for AI dominance.

<details><summary>References</summary>
<ul>
<li><a href="https://nai500.com/blog/2026/06/three-canadian-stocks-tapping-into-the-1-trillion-ai-data-center-boom/">Three Canadian Stocks Tapping Into the $ 1 Trillion AI Data... | NAI 500</a></li>
<li><a href="https://min.news/en/tech/4f27e17c066c990e2774e293b637316d.html">UN: Nearly $ 1 trillion invested in AI this year, but the benefits go to...</a></li>

</ul>
</details>

**Tags**: `#AI Chips`, `#Infrastructure`, `#Scale Law`, `#Geopolitics`, `#Data Centers`

---

<a id="item-10"></a>
## [Apple Limits Vulnerability Report Submissions to Counter AI-Generated Low-Quality Reports](https://www.ft.com/content/4532122d-90f2-4433-9df6-ca99d8a141d2?syn-25a6b1a6=1) ⭐️ 9.0/10

Apple has limited the number of vulnerability reports researchers can submit simultaneously and introduced a 30-day cooling period to address the surge in low-quality reports generated by AI models like ChatGPT. This move highlights the growing impact of AI on cybersecurity, as AI tools like ChatGPT can rapidly identify vulnerabilities, forcing companies to balance increased discovery with quality control. Italian security startup Bynario reported finding over 50 vulnerabilities in macOS using ChatGPT within three weeks, including a privilege escalation chain, but could not submit them due to Apple&\#x27;s limits. Apple is also using AI tools from Anthropic and OpenAI to enhance its own defenses, with recent security updates fixing approximately five times more flaws than usual.

telegram · zaihuapd · Aug 2, 13:50

**Background**: Vulnerability reporting is a critical process where security researchers identify and disclose software flaws to vendors for patching. AI tools like ChatGPT are increasingly being used to automate the discovery of vulnerabilities, but they can also generate low-quality or irrelevant reports, overwhelming the reporting systems.

<details><summary>References</summary>
<ul>
<li><a href="https://bynar.io/">Bynario — Autonomous Vulnerability Detection &amp; Remediation</a></li>
<li><a href="https://www.linkedin.com/posts/bynario_binaryanalysis-vulnerabilityresearch-appsec-activity-7391821616457973760-NmpY">#binaryanalysis #vulnerabilityresearch #appsec #cybersecurityainews...</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Security`, `#AI`, `#Vulnerability`, `#macOS`

---

<a id="item-11"></a>
## [ChangXin&\#x27;s Breakout: Catching Up to Samsung and Micron](https://news.google.com/rss/articles/CBMiYEFVX3lxTE13ZXBIeHZuVENzWUY3YkxCWkc4NGNxOG1zRjRsUWt4Vm9BcWJaM1FLeTVKcjJWWjNTcUI5MmcxUE5UOG5Ta2xsXzdscmVNdENUTVVza1FzZXhBUW1jTC11Ug?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies \(CXMT\) has achieved rapid progress in semiconductor manufacturing, narrowing the gap with global giants like Samsung and Micron. This breakthrough is significant as it marks a major step for China&\#x27;s domestic semiconductor industry, potentially disrupting the global memory market dominated by international players. CXMT&\#x27;s mainstream process nodes are 19nm \(DDR4\) and 16nm \(DDR5\), while international leaders are at 12-14nm, indicating a 1-2 generation gap in technology maturity.

google\_news · eastmoney.com · Aug 2, 19:28

**Background**: DRAM \(Dynamic Random Access Memory\) is a critical component in computers and AI systems. ChangXin is a leading Chinese DRAM manufacturer competing against established global players like Samsung, SK Hynix, and Micron.

<details><summary>References</summary>
<ul>
<li><a href="https://cdn.sputniknews.cn/20260529/1071576052.html">长 鑫 过会：“从0到1”的 突 破 ，而非“从1到10”的成熟 - 2026年5月29...</a></li>
<li><a href="https://m.21jingji.com/article/20260727/herald/f6684379ebff86249c147c0a06b22ebd.html">长 鑫 科 技 科创板首秀：市值 突 破 3万亿元，A股迎“ 存 储 ”新标杆 - 21财经</a></li>
<li><a href="https://post.smzdm.com/p/aognp867/">存 储 江湖 ｜ 长 鑫 存 储 ：在巨头垄断的DRAM市场，撕开一道口子_CPU...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#AI hardware`, `#manufacturing`, `#industry analysis`

---

<a id="item-12"></a>
## [ChangXin Memory Technologies Valuation Exceeds 3 Trillion Yuan](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBlUE1xWGlydEZlRE4yVUN4SHFhOFlhc0VUektLeTZ5cnp4ajZxN2JqcXVuVlNsanVFWGUtcm5mSXZjWklTQXVOU3Jwam9LNWQy?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies \(CXMT\) has set its IPO price at CNY 8.66 per share, implying a listing valuation of approximately CNY 579.19 billion. This valuation highlights CXMT&\#x27;s critical role in China&\#x27;s semiconductor industry and its potential to become a global DRAM powerhouse. The IPO aims to raise about 29.5 billion yuan, with the post-issuance valuation estimated at around 295 billion yuan, reflecting strong investor confidence.

google\_news · 凤凰网 · Aug 2, 19:20

**Background**: CXMT, founded in 2016, manufactures DRAM chips for mobile phones, PCs, and servers. The company is a key player in China&\#x27;s semiconductor market, which is expected to grow at a CAGR of 8.6% through 2034.

<details><summary>References</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/344907979167714">#changxintechsetsipopriceatcny8.66 AI Hardware Boom</a></li>
<li><a href="https://www.caproasia.com/2026/07/28/china-488-billion-dram-semiconductor-company-changxin-memory-technologies-cxmt-founder-zhu-yiming-age-54-personal-fortune-increased-to-16-billion-from-5-billion-after-changxin-memory-technologi/">China $488 Billion DRAM Semiconductor Company ChangXin ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3818972597142664">Can the AI Trend Propel ChangXin Memory Technologies to...</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#CXMT`, `#China technology`, `#hardware`

---