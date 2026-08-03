---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
content_date: 2026-08-02
lang: zh
---

> 报道范围：2026-08-02（Asia/Shanghai 自然日）

> 从 101 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp b10228 版本新增 DeepseekV4 MTP 和 DSpark 支持](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10225 发布：MiMo V2 MTP 优化与多平台二进制文件](#item-2) ⭐️ 10.0/10
3. [长鑫存储 LPDDR6 接近研发验证尾声 设计规格速率达 12800Mbps - 观点网](#item-3) ⭐️ 10.0/10
4. [Karpathy 的 Pelican：AI 生成物理世界基准测试](#item-4) ⭐️ 9.0/10
5. [datasette-apps 0.2a0：Datasette Agent 的新调试工具](#item-5) ⭐️ 9.0/10
6. [OpenAI 的 Astra 模型解决了十个长期存在的数学问题](#item-6) ⭐️ 9.0/10
7. [CausalVLBench：大型视觉语言模型视觉因果推理基准测试](#item-7) ⭐️ 9.0/10
8. [寻求将学术教科书图表转换为可编辑资产的管道](#item-8) ⭐️ 9.0/10
9. [AI 芯片每 9 个月翻番，2028 年底全球将达 2 亿颗](#item-9) ⭐️ 9.0/10
10. [苹果限制漏洞报告提交数量，应对 AI 生成低质量安全报告激增](#item-10) ⭐️ 9.0/10
11. [长鑫突围：追赶三星、美光](#item-11) ⭐️ 9.0/10
12. [长鑫科技估值超过 3 万亿](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10228 版本新增 DeepseekV4 MTP 和 DSpark 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10228) ⭐️ 10.0/10

llama.cpp 项目发布了 b10228 版本，引入了对 DeepseekV4 MTP 和 DSpark 推测解码的支持，并提供了 macOS、iOS 和 Linux 的预编译二进制文件。 此次发布通过支持 DSpark 等高级推测解码技术，显著增强了 llama.cpp 的推理能力，从而提高了 DeepSeek-V4 模型的生成速度和吞吐量。 该版本提供了广泛的跨平台二进制文件，支持 macOS、iOS、Linux 和 Windows，并兼容 CUDA、Vulkan、ROCm 和 OpenVINO 等多种硬件加速器，但 macOS Apple Silicon 的 KleidiAI 版本目前已被禁用。

github · github-actions\[bot\] · 8月2日 21:28

**背景**: llama.cpp 是一个高性能的开源大型语言模型推理引擎，针对 CPU 和 GPU 执行进行了优化。DeepseekV4 MTP（多 Token 预测）是 vLLM 中用于高效模型加载的技术，而 DSpark 则是一种推测解码方法，通过从草稿模型接受更多 Token 来加速生成过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/issues/25096">Feature Request: DSpark confidence-scheduled verification &amp; semi-autoregressive drafting · Issue #25096 · ggml-org/llama.cpp</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/25167">Support DeepSeek DSpark speculative decoding · ggml-org/llama.cpp · Discussion #25167</a></li>
<li><a href="https://docs.vllm.ai/en/stable/api/vllm/model_executor/models/deepseek_v4_mtp/">deepseek _ v 4 _ mtp - vLLM</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#Open Source`, `#Machine Learning`, `#Cross Platform`

---

<a id="item-2"></a>
## [llama.cpp b10225 发布：MiMo V2 MTP 优化与多平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10225) ⭐️ 10.0/10

llama.cpp 项目发布了 b10225 版本，引入了新的模型加载优化，仅在需要时加载 MiMo V2 MTP 张量，并为 macOS、Linux、iOS、Android 和 Windows 提供了预编译二进制文件。 此次发布通过减少不必要的内存使用显著提高了大型语言模型的运行效率，并为多种平台提供了现成的二进制文件，使开发者和用户更容易部署 AI 推理。 该优化专门针对 MiMo V2 MTP 张量，尽管 macOS Apple Silicon 的 KleidiAI 支持已禁用，但该版本包含了广泛的平台特定构建版本，包括 Windows 的 CUDA 12 和 13 支持。

github · github-actions\[bot\] · 8月2日 16:30

**背景**: llama.cpp 是一个在消费级硬件上运行大型语言模型（LLM）的高性能 C++ 库，以其效率和跨平台支持而闻名。MiMo V2 MTP 是某些 AI 模型中使用的张量格式，而 KleidiAI 是一个针对 AI 性能优化的 ARM 微内核库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/kleidiai">Arm KleidiAI: Helping AI frameworks elevate ...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI inference`, `#software engineering`, `#open-source`, `#machine learning`

---

<a id="item-3"></a>
## [长鑫存储 LPDDR6 接近研发验证尾声 设计规格速率达 12800Mbps - 观点网](https://news.google.com/rss/articles/CBMiTkFVX3lxTFBPZHQ5cy0tckxfTldsZm1SdEwwOEplTWpwekozZEtIMDk4OGlSYTgyNm9rZGpVNVJHU0c4M3Q1bWh4ZlUydmJHSG9FWXdhQQ?oc=5) ⭐️ 10.0/10

长鑫存储（CXMT）的 LPDDR6 内存产品已接近研发验证阶段，其设计规格的传输速率达到了 12800Mbps。

google\_news · 观点网 · 8月2日 21:13

**标签**: `#semiconductors`, `#memory`, `#LPDDR6`, `#AI hardware`, `#CXMT`

---

<a id="item-4"></a>
## [Karpathy 的 Pelican：AI 生成物理世界基准测试](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 9.0/10

Andrej Karpathy 展示了一个名为 Pelican 的新基准测试，其中 Claude Opus 5 模型使用 100 万个 token 预算（约 10 美元）生成了《指环王》第一段的 3D Three.js 渲染图。 该项目代表了 AI 测试从简单提示词向复杂物理世界基准测试的转变，这能更好地暴露 AI 对物理世界的理解，并有助于衡量未来的进展。 生成的代码是程序化的，略显粗糙，但成功放置和排列了 3D 元素来讲述故事，标志着从简单图像生成任务的转变。

hackernews · delichon · 8月2日 12:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: Andrej Karpathy 是 OpenAI 的联合创始人之一和特斯拉 AI 总监，他加入 Anthropic 领导前沿 LLM 研究。Pelican 基准测试是试图超越使用简单提示词（如“在自行车上画一只鹈鹕的 svg”）来测试 LLM 的一种尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xcancel.com/karpathy/status/2083749667410727319">Andrej Karpathy (@karpathy): &quot;We&#x27;re starting to leave the territory where you&#x27;d test an LLM by e.g. &quot;create an svg of pelican on a bicycle&quot;. As one idea to generalize it, I was interested what Opus 5 would do if I gave it the first paragraph of the Lord of the Rings, a 1M token budget (~$10) and asked for three js render of it. Opus went off for ~2 hours and wrote 5500 lines of code that (procedurally) rendered the story. It&#x27;s kind of janky but fun. But it&#x27;s a bit mindboggling that the LLM has to place and</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/08/60861644/andrej-karpathy-says-ai-has-moved-beyond-simple-prompts-after-claude-opus-builds-3d-lord-of-the-rings-world">Andrej Karpathy Says AI Has Moved Beyond Simple Prompts After Claude Opus Builds 3D Lord of the Rings Wor - Benzinga</a></li>
<li><a href="https://simonwillison.net/2025/Feb/6/andrej-karpathy/">A quote from Andrej Karpathy | Simon Willison’s Weblog</a></li>

</ul>
</details>

**社区讨论**: 用户讨论了项目的可复现性，指出与 Simon 的 pelican 不同，提示词是不可见的。其他人讨论了这种基准测试如何更好地暴露物理理解能力，以及 Anthropic 模型似乎专门针对 Three.js 代码生成进行了调优。

**标签**: `#AI`, `#Machine Learning`, `#Reproducibility`, `#Benchmarks`, `#Generative AI`

---

<a id="item-5"></a>
## [datasette-apps 0.2a0：Datasette Agent 的新调试工具](https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything) ⭐️ 9.0/10

datasette-apps 0.2a0 版本为 Datasette Agent 引入了两个新工具：\`app\_debug\(\)\` 用于不可见地测试应用，\`app\_list\(\)\` 用于列出用户有权编辑的应用。 这些工具通过实现应用的自动化测试和管理，增强了软件开发工作流，使开发者更容易确保应用的可靠性和访问控制。 \`app\_debug\(\)\` 工具使用一个 \`opacity: 0\` 和 \`pointer-events: none\` 的不可见 iframe 在沙盒环境中执行 JavaScript，允许进行冒烟测试和元素测量。

rss · Simon Willison · 8月2日 05:23

**背景**: Datasette Agent 是一个用于探索和查询 Datasette 数据的 AI 助手，而 Datasette Apps 是托管在 Datasette 本身内的单文件 HTML 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette / datasette - agent : An LLM-powered agent for...</a></li>
<li><a href="https://datasette.io/blog/2026/datasette-apps/">Host applications inside Datasette with Datasette ... - Datasette Blog</a></li>

</ul>
</details>

**标签**: `#datasette`, `#developer-tools`, `#software-engineering`, `#testing`, `#agent`

---

<a id="item-6"></a>
## [OpenAI 的 Astra 模型解决了十个长期存在的数学问题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 9.0/10

据报道，OpenAI 的内部模型 Astra 解决了十个未解决的数学问题，每个问题在 GPT-5.6 Sol 代币价格上的花费不到 2000 美元。 这一突破展示了 AI 解决数学和理论计算机科学中复杂、长期问题的潜力，标志着 AI 推理能力的重要一步。 结果可在开源仓库中以 Lean 4 形式化提供，包含描述解决方案的论文以及重建推理过程的 LLM 生成 PDF。

rss · Simon Willison · 8月2日 04:34

**背景**: Lean 4 是一种用于形式化数学证明的证明助手和交互式定理证明器，确保数学推理的严谨性和可验证性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/tech/9qjs9782">OpenAI Astra Model Solves Ten Open Problems · Digg</a></li>
<li><a href="https://github.com/openai/ten-proofs">GitHub - openai / ten - proofs : Lean certificates accompanying proofs in...</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT - 5 . 6 Sol - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI`, `#Mathematics`, `#OpenAI`, `#Research`, `#Computing`

---

<a id="item-7"></a>
## [CausalVLBench：大型视觉语言模型视觉因果推理基准测试](https://www.reddit.com/r/MachineLearning/comments/1vdd7ty/r_causalvlbench_benchmarking_visual_causal/) ⭐️ 9.0/10

CausalVLBench 是一个新基准，旨在评估大型视觉语言模型（VLM）的视觉因果推理能力，涵盖因果结构推断、干预目标预测和反事实预测等任务。 该基准通过聚焦因果推理，解决了 VLM 评估中的一个关键空白，这对于理解视觉数据中的因果关系和提高模型可靠性至关重要。 CausalVLBench 在三个因果任务上测试了八个视觉语言模型家族，揭示了显著的推理差距，并挑战了当前的机器学习能力。

reddit · r/MachineLearning · /u/moschles · 8月2日 17:07

**背景**: 因果推理涉及识别因果关系，这是预测和决策中使用的基本认知过程。大型视觉语言模型（VLM）结合了视觉和文本理解，但在因果推断等复杂推理任务上往往表现不佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2506.11034v2">CausalVLBench : Benchmarking Visual Causal Reasoning in Large...</a></li>
<li><a href="https://www.remio.ai/post/causalvlbench-pushes-visual-ai-beyond-recognition-and-exposes-a-reasoning-gap">CausalVLBench Pushes Visual AI Beyond Recognition, and Exposes...</a></li>
<li><a href="https://huggingface.co/papers/2506.11034">Paper page - CausalVLBench : Benchmarking Visual Causal...</a></li>

</ul>
</details>

**标签**: `#Large Vision-Language Models`, `#Benchmarking`, `#Causal Reasoning`, `#AI Evaluation`, `#Computer Vision`

---

<a id="item-8"></a>
## [寻求将学术教科书图表转换为可编辑资产的管道](https://www.reddit.com/r/MachineLearning/comments/1vdlj8j/looking_for_the_right_pipeline_to_convert/) ⭐️ 9.0/10

一位开发者正在寻求关于构建人工辅助管道的建议，以检测、分割并清理扫描的学术教科书页面中的图表，将其转换为用于前端渲染的结构化数字表示。 该项目解决了数字化教育内容的挑战，能够实现交互式和可定制的图表渲染，从而提升学习体验并支持文档理解系统。 工作流程包括图表检测、通过图像修复移除标签以及存储几何数据，重点在于低成本推理和人工循环校正以确保准确性。

reddit · r/MachineLearning · /u/Afraid\_Reviewer · 8月2日 23:50

**背景**: 文档理解管道通常结合多个机器学习模型进行布局分析、文本检测和分割，而基于区域的分割和形态学标记等技术有助于将文本与非文本区域分开。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mdpi.com/2078-2489/17/2/165">Decoding Technical Diagrams: A Survey of AI Methods for Image Content Extraction and Understanding</a></li>
<li><a href="https://arxiv.org/html/2410.21721v1">DiffSTR: Controlled Diffusion Models for Scene Text Removal</a></li>
<li><a href="https://www.paddleocr.ai/v3.3.1/en/version3.x/pipeline_usage/doc_understanding.html">Document Understanding Pipeline - PaddleOCR Documentation</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#document processing`, `#AI pipeline`, `#image segmentation`, `#frontend integration`

---

<a id="item-9"></a>
## [AI 芯片每 9 个月翻番，2028 年底全球将达 2 亿颗](https://www.nytimes.com/interactive/2026/07/29/technology/ai-chips-data-center-boom.html) ⭐️ 9.0/10

Epoch AI 估算，全球 AI 芯片数量每 9 个月翻一番，到 2028 年底将达约 2 亿颗，是当前的 10 倍。 这种指数级增长凸显了 AI 基础设施在全球经济中的关键作用，并凸显了围绕 AI 芯片制造主导权的激烈地缘政治竞争。 IDC 预测，2029 年全球 AI 基础设施投资将突破 1 万亿美元，去年为 3180 亿美元，而美国控制着全球约 80% 的 AI 算力。

telegram · zaihuapd · 8月2日 09:01

**背景**: AI 芯片需求的激增是由“规模定律”驱动的，该定律认为算力越大，AI 能力越强。这一趋势进一步受到科技巨头大规模基础设施投资和围绕 AI 主导权的地缘政治竞争的推动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nai500.com/blog/2026/06/three-canadian-stocks-tapping-into-the-1-trillion-ai-data-center-boom/">Three Canadian Stocks Tapping Into the $ 1 Trillion AI Data... | NAI 500</a></li>
<li><a href="https://min.news/en/tech/4f27e17c066c990e2774e293b637316d.html">UN: Nearly $ 1 trillion invested in AI this year, but the benefits go to...</a></li>

</ul>
</details>

**标签**: `#AI Chips`, `#Infrastructure`, `#Scale Law`, `#Geopolitics`, `#Data Centers`

---

<a id="item-10"></a>
## [苹果限制漏洞报告提交数量，应对 AI 生成低质量安全报告激增](https://www.ft.com/content/4532122d-90f2-4433-9df6-ca99d8a141d2?syn-25a6b1a6=1) ⭐️ 9.0/10

苹果已限制研究人员可同时提交的漏洞报告数量，并设置了 30 天的冷却期，以应对借助 AI 模型（如 ChatGPT）生成的低质量安全报告激增的情况。 这一举措凸显了 AI 对网络安全日益增长的影响，因为像 ChatGPT 这样的 AI 工具能够快速识别漏洞，迫使公司在增加发现速度的同时加强质量控制。 意大利安全初创公司 Bynario 报告称，其使用 ChatGPT 在三周内于最新 macOS 中发现了 50 多个漏洞，包括可让攻击者完全控制电脑的提权漏洞链，但因提交限额无法向苹果报告。苹果也在使用 Anthropic 和 OpenAI 的 AI 工具加强自身防御，最近的系统安全更新修复的漏洞数量约为以往的五倍。

telegram · zaihuapd · 8月2日 13:50

**背景**: 漏洞报告是一个关键过程，安全研究人员识别并披露软件漏洞以供厂商修复。像 ChatGPT 这样的 AI 工具正越来越多地被用于自动化漏洞发现，但它们也可能生成低质量或不相关的报告，从而压垮报告系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bynar.io/">Bynario — Autonomous Vulnerability Detection &amp; Remediation</a></li>
<li><a href="https://www.linkedin.com/posts/bynario_binaryanalysis-vulnerabilityresearch-appsec-activity-7391821616457973760-NmpY">#binaryanalysis #vulnerabilityresearch #appsec #cybersecurityainews...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Security`, `#AI`, `#Vulnerability`, `#macOS`

---

<a id="item-11"></a>
## [长鑫突围：追赶三星、美光](https://news.google.com/rss/articles/CBMiYEFVX3lxTE13ZXBIeHZuVENzWUY3YkxCWkc4NGNxOG1zRjRsUWt4Vm9BcWJaM1FLeTVKcjJWWjNTcUI5MmcxUE5UOG5Ta2xsXzdscmVNdENUTVVza1FzZXhBUW1jTC11Ug?oc=5) ⭐️ 9.0/10

长鑫存储在半导体制造方面取得了快速进展，缩小了与三星、美光等全球巨头的差距。 这一突破意义重大，标志着中国国内半导体行业迈出了重要一步，可能打破由国际巨头主导的全球存储器市场。 长鑫存储的主流工艺节点为 19nm（DDR4）和 16nm（DDR5），而国际领先者处于 12-14nm，技术成熟度差距为 1-2 代。

google\_news · eastmoney.com · 8月2日 19:28

**背景**: DRAM（动态随机存取存储器）是计算机和 AI 系统中的关键组件。长鑫是中国领先的 DRAM 制造商，与三星、SK 海力士和美光等成熟的全球玩家竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cdn.sputniknews.cn/20260529/1071576052.html">长 鑫 过会：“从0到1”的 突 破 ，而非“从1到10”的成熟 - 2026年5月29...</a></li>
<li><a href="https://m.21jingji.com/article/20260727/herald/f6684379ebff86249c147c0a06b22ebd.html">长 鑫 科 技 科创板首秀：市值 突 破 3万亿元，A股迎“ 存 储 ”新标杆 - 21财经</a></li>
<li><a href="https://post.smzdm.com/p/aognp867/">存 储 江湖 ｜ 长 鑫 存 储 ：在巨头垄断的DRAM市场，撕开一道口子_CPU...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory chips`, `#AI hardware`, `#manufacturing`, `#industry analysis`

---

<a id="item-12"></a>
## [长鑫科技估值超过 3 万亿](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBlUE1xWGlydEZlRE4yVUN4SHFhOFlhc0VUektLeTZ5cnp4ajZxN2JqcXVuVlNsanVFWGUtcm5mSXZjWklTQXVOU3Jwam9LNWQy?oc=5) ⭐️ 9.0/10

长鑫科技（CXMT）将 IPO 定价定为每股 8.66 元人民币，这意味着其上市估值约为 5791.9 亿元人民币。 这一估值凸显了长鑫科技在中国半导体行业中的关键作用，并使其有望成为全球 DRAM 领域的领军企业。 此次 IPO 计划筹集约 295 亿元人民币，发行后估值估计约为 2950 亿元人民币，反映了投资者的强烈信心。

google\_news · 凤凰网 · 8月2日 19:20

**背景**: 长鑫科技成立于 2016 年，为手机、电脑和服务器制造 DRAM 芯片。该公司是中国半导体市场的重要参与者，预计该市场到 2034 年的复合年增长率将达到 8.6%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.binance.com/en/square/post/344907979167714">#changxintechsetsipopriceatcny8.66 AI Hardware Boom</a></li>
<li><a href="https://www.caproasia.com/2026/07/28/china-488-billion-dram-semiconductor-company-changxin-memory-technologies-cxmt-founder-zhu-yiming-age-54-personal-fortune-increased-to-16-billion-from-5-billion-after-changxin-memory-technologi/">China $488 Billion DRAM Semiconductor Company ChangXin ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3818972597142664">Can the AI Trend Propel ChangXin Memory Technologies to...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory chips`, `#CXMT`, `#China technology`, `#hardware`

---