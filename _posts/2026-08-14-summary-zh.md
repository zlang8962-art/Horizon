---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
content_date: 2026-08-13
lang: zh
---

> 报道范围：2026-08-13（Asia/Shanghai 自然日）

> 从 100 条内容中筛选出 12 条重要资讯。

---

1. [DeepSeek V4 Pro 0813 模型权重在 Hugging Face 上发布](#item-1) ⭐️ 10.0/10
2. [ggml-org/llama.cpp released b10410](#item-2) ⭐️ 9.0/10
3. [llama.cpp b10405：HIP 浮点精度修复与跨平台二进制文件](#item-3) ⭐️ 9.0/10
4. [ollama/ollama released v0.32.10](#item-4) ⭐️ 9.0/10
5. [DeepSeek Harness：AI 智能体框架开发者预览版](#item-5) ⭐️ 9.0/10
6. [Spaghettifying DRAM：利用内存子系统漏洞的新型攻击](#item-6) ⭐️ 9.0/10
7. [Simon Willison 发布 alchemy-utils 0.1a1](#item-7) ⭐️ 9.0/10
8. [Cloudflare 证书透明度监控现已正式发布](#item-8) ⭐️ 9.0/10
9. [City2Graph：用于城市异构图分析的 Python 库](#item-9) ⭐️ 9.0/10
10. [DeepMind 推出手语转文字模型 SL2T，首次落地 Pixel 11 键盘与实时字幕](#item-10) ⭐️ 9.0/10
11. [DeepSeek-V4-Pro 正式版上线，API 将实行峰谷定价](#item-11) ⭐️ 9.0/10
12. [长江存储首次跻身全球第三大市场份额](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Pro 0813 模型权重在 Hugging Face 上发布](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 10.0/10

DeepSeek V4 Pro 0813 模型权重现已可在 Hugging Face 上获取，此前它仅通过 OpenRouter 以 API 形式发布。 此次发布允许开发者在本地运行该模型，促进了除 API 访问之外的更广泛采用和实验。 该模型包含 1.7 万亿参数，需要 893 GB 存储空间，且在不同推理级别下视觉输出存在显著差异。

rss · Simon Willison · 8月13日 07:59

**背景**: DeepSeek 是一家以低成本、开源权重大语言模型（如 DeepSeek-R1）闻名的中国 AI 公司。该公司此前已以开源许可证发布了多个模型，支持社区驱动开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/docs/quickstart">OpenRouter Quickstart Guide</a></li>
<li><a href="https://openrouter.ai/openrouter">OpenRouter API and Models | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#Model Release`, `#Weights`, `#API`

---

<a id="item-2"></a>
## [ggml-org/llama.cpp released b10410](https://github.com/ggml-org/llama.cpp/releases/tag/b10410) ⭐️ 9.0/10

llama.cpp release b10410 adds SYCL fp16 promotion and provides binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · 8月13日 23:52

**标签**: `#llama.cpp`, `#open-source`, `#AI-inference`, `#SYCL`, `#GPU-acceleration`

---

<a id="item-3"></a>
## [llama.cpp b10405：HIP 浮点精度修复与跨平台二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10405) ⭐️ 9.0/10

llama.cpp 版本 b10405 移除了 HIP 构建中的不安全浮点优化，以确保符合 IEEE 754 标准，并引入了为 macOS、iOS、Linux、Android 和 Windows 提供的预编译二进制文件。 此版本对使用 AMD GPU 的开发者至关重要，因为符合 IEEE 标准的修复可以防止在 RDNA3.5 硬件上进行推测解码时的行为不一致，确保跨平台的可重现和数值安全的推理。 此次更新禁用了 macOS Apple Silicon 和 ROCm 7.14 构建的 KleidiAI 支持，同时为 Linux 和 Windows 提供了包括 Vulkan、OpenVINO、SYCL 和 CUDA 12/13 在内的广泛选项。

github · github-actions\[bot\] · 8月13日 15:32

**背景**: llama.cpp 是一个在消费级硬件上运行大语言模型（LLM）的高性能 C++ 库。HIP 是 AMD 的 GPU 编程 API，而 IEEE 754 是确保不同硬件间数值结果一致的浮点运算标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html">Low precision floating point types — HIP 7.14.60850 Documentation</a></li>

</ul>
</details>

**标签**: `#AI`, `#llama.cpp`, `#GPU`, `#macOS`, `#Linux`

---

<a id="item-4"></a>
## [ollama/ollama released v0.32.10](https://github.com/ollama/ollama/releases/tag/v0.32.10) ⭐️ 9.0/10

Ollama v0.32.10 release includes performance optimizations, bug fixes, and a new contributor.

github · github-actions\[bot\] · 8月13日 06:36

**标签**: `#ollama`, `#machine-learning`, `#software-release`, `#performance`, `#bug-fix`

---

<a id="item-5"></a>
## [DeepSeek Harness：AI 智能体框架开发者预览版](https://deepseek.com/harness/en/) ⭐️ 9.0/10

DeepSeek Harness 现已作为开发者预览版发布，这是一个开源的 AI 智能体框架，支持可追踪的模型执行和动态插件功能。 该框架通过提供模型训练、推理和智能体工作流所需的工具，满足了 AI 计算和软件开发的关键需求，并通过可追踪性和热重载等功能提供了实用价值。 该框架采用“万物皆插件”的架构，支持仅追加的会话日志以记录所有模型交互，目前以 MIT 许可证发布，预计存在一些不完善之处。

hackernews · bjin · 8月13日 20:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**背景**: AI 智能体框架是帮助开发者构建能够执行复杂任务的自主 AI 系统的工具。DeepSeek Harness 是开源 AI 开发工具的更广泛趋势的一部分，专注于提高智能体工作流中的透明度和灵活性。

**社区讨论**: 开发者预览版因其可追踪功能获得了积极反馈，用户指出它允许检查所有模型交互，而某些美国模型则对追踪信息进行加密。一些用户对插件疲劳表示担忧，而另一些人则强调了其使用 Cordis v4 系统进行动态插件管理的特点。

**标签**: `#AI`, `#Agent Framework`, `#Developer Tools`, `#Open Source`, `#DeepSeek`

---

<a id="item-6"></a>
## [Spaghettifying DRAM：利用内存子系统漏洞的新型攻击](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

研究人员推出了一种名为“Spaghettifying DRAM”的新型 DRAM 攻击，利用内存子系统中的漏洞获得对系统内存的显著控制权。 这种攻击展示了 DRAM 控制器和内存子系统之间的高度互联性，揭示了现代计算硬件的关键安全影响。 该攻击针对 2013 年的 AMD Jaguar 架构，需要 ring-0 访问权限，且关于其对 Zen 3 等较新 CPU 家族的适用性信息有限。

hackernews · matt\_d · 8月13日 22:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM（动态随机存取存储器）是一种用于计算机临时存储数据的易失性存储器类型。内存子系统包括 DRAM 控制器，负责管理 CPU 和内存之间的数据传输，由于专有固件和刷新要求，其复杂性往往很高。

**社区讨论**: 社区成员对 Christopher Domas 的配套 Black Hat 演讲表示兴奋，而其他人则讨论了 DRAM 复杂性的增加以及对 Xbox 和 PlayStation 等游戏主机的潜在影响。

**标签**: `#DRAM`, `#security`, `#hardware`, `#attack`, `#AMD`

---

<a id="item-7"></a>
## [Simon Willison 发布 alchemy-utils 0.1a1](https://simonwillison.net/2026/Aug/13/alchemy-utils/) ⭐️ 9.0/10

Simon Willison 发布了 alchemy-utils 0.1a1，这是一个 Python 库，为 DuckDB 导出和 CSV 导入提供了性能优化。 此次发布对处理大型数据集的数据专业人士和开发者具有重要意义，因为它提高了常见数据操作任务的效率。 该库专注于优化 DuckDB 导出和 CSV 导入的性能，这是数据工作流中的关键操作。

rss · Simon Willison · 8月13日 11:03

**背景**: DuckDB 是一个用于分析工作负载的进程内 SQL OLAP 数据库管理系统，而 CSV（逗号分隔值）是一种用于存储表格数据的广泛使用的文件格式。Python 的内置 csv 模块提供了读取和写入 CSV 文件的基本功能，但对于大型数据集，性能可能会成为瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/docs/current/guides/performance/overview">Performance Guide – DuckDB</a></li>
<li><a href="https://duckdb.org/docs/lts/guides/performance/how_to_tune_workloads">Tuning Workloads – DuckDB</a></li>

</ul>
</details>

**标签**: `#python`, `#duckdb`, `#csv`, `#performance`, `#open-source`

---

<a id="item-8"></a>
## [Cloudflare 证书透明度监控现已正式发布](https://blog.cloudflare.com/certificate-transparency-monitoring-ga/) ⭐️ 9.0/10

Cloudflare 宣布证书透明度监控现已正式发布，该功能移除了关于为您的域名颁发的证书的例行邮件。 这一变化简化了安全警报管理，确保只有非例行的证书事件才会触发通知，帮助管理员专注于真正的威胁。 该功能是一个可选工具，允许域名所有者双重检查为其域名颁发的 SSL/TLS 证书，在不过度使用户被噪音淹没的情况下提高安全监督。

rss · Cloudflare Blog · 8月13日 21:00

**背景**: 证书透明度（CT）是一项互联网安全标准，要求证书颁发机构将新颁发的证书提交到公开的、防篡改的日志中，使域名所有者能够监控和审计证书的颁发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://certificate.transparency.dev/">Certificate Transparency : Certificate Transparency</a></li>
<li><a href="https://cloudflare-docs-7ou.pages.dev/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/">Certificate Transparency Monitoring · Cloudflare SSL/TLS docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_Transparency">Certificate Transparency - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#certificate-transparency`, `#tls`, `#monitoring`, `#cloudflare`

---

<a id="item-9"></a>
## [City2Graph：用于城市异构图分析的 Python 库](https://www.reddit.com/r/MachineLearning/comments/1vn8oya/city2graph_a_python_library_for_heterogeneous/) ⭐️ 9.0/10

City2Graph 是一个新发布的 Python 库，用于将地理空间数据转换为可直接分析的异构图，以支持 GeoAI 和城市空间分析，相关论文已发表在《计算机、环境与城市系统》期刊上。 该库填补了城市数据与图神经网络之间的空白，使得更复杂的空间分析和 GeoAI 应用得以实现，这些应用以前难以构建。 它支持从 OpenStreetMap/Overture Maps 获取形态图，通过 DuckDB 加载交通数据，处理流动数据，并提供多种邻近性指标，并能无缝集成到 PyTorch Geometric 中。

reddit · r/MachineLearning · /u/Tough\_Ad\_6598 · 8月13日 19:59

**背景**: 异构图是指具有多种节点和边类型的网络，常用于推荐系统和社交网络。PyTorch Geometric 是一个流行的构建图神经网络的库。Delaunay 三角剖分是一种从点数据创建网格的几何技术，常用于城市分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tobilg/duckdb-gtfs">GitHub - tobilg/ duckdb - gtfs : Loading and analyzing GTFS Schedule...</a></li>
<li><a href="https://pytorch-geometric.readthedocs.io/en/latest/notes/heterogeneous.html">Heterogeneous Graph Learning — pytorch_geometric documentation</a></li>
<li><a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0218877">A formal model of neighborhood representation and applications in urban building aggregation supported by Delaunay triangulation | PLOS One</a></li>

</ul>
</details>

**标签**: `#GeoAI`, `#Graph Neural Networks`, `#Python Library`, `#Urban Systems`, `#Spatial Analysis`

---

<a id="item-10"></a>
## [DeepMind 推出手语转文字模型 SL2T，首次落地 Pixel 11 键盘与实时字幕](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 9.0/10

DeepMind 发布了大规模多语言手语转文字模型 SL2T，并将其集成到 Pixel 11 设备的 Gboard 和 Live Transcribe 中，以实现实时美国手语（ASL）翻译。 这一突破性进展通过实现实时交流，解决了听障人士的重大无障碍鸿沟，标志着手语 AI 首次进入主流消费级硬件。 SL2T 在 50 多种手语数据上训练超过 10 万小时，在 FLEURS-ASL 基准上达到 70 BLEURT 分数，并采用隐私优先的姿态估计技术，仅处理手部和身体关键点而不读取原始视频。

telegram · zaihuapd · 8月13日 16:55

**背景**: 虽然语音 AI 工具如语音转文字和翻译已成为主流，但全球 70 万听障人士使用的 200 多种手语长期以来在技术上一直被忽视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://en.cryptonomist.ch/2026/08/13/sign-language-ai-translation-slt2/">Sign Language AI Translation: Google&#x27;s Breakthrough with SL2T ...</a></li>
<li><a href="https://www.unite.ai/google-deepmind-brings-sign-language-translation-to-phones-with-sl2t/">Google DeepMind Brings Sign Language Translation to Phones ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Sign Language`, `#Privacy`, `#Mobile`, `#DeepMind`

---

<a id="item-11"></a>
## [DeepSeek-V4-Pro 正式版上线，API 将实行峰谷定价](https://api-docs.deepseek.com/zh-cn/updates) ⭐️ 9.0/10

DeepSeek-V4-Pro 正式版已同步上线 APP、网页端和 API，模型增强 Agent 能力并原生支持 Responses API 格式。API 将实行峰谷定价，新价格于 2026 年 8 月 17 日 0 时生效，闲时价格为高峰时段一半。 此次发布对 AI 开发者影响重大，通过提供成本效益高的定价模型和先进的 Agent 能力，可能加速软件开发生态中代理工作流的采用。 模型支持低、高、高三档思考模式，并兼容 Codex。DeepSeek 还发布了 Harness，这是一个采用 MIT 协议开源的代理框架，由 Cordis 元框架驱动，采用插件式架构。

telegram · zaihuapd · 8月13日 19:12

**背景**: DeepSeek 是一家以开发大型语言模型而闻名的 AI 研究公司。Cordis 框架是一种用于构建模块化代理系统的时空组合性元框架。Responses API 是 AI 代理交互的标准格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/11027/deepseek-harness-mit-claude-code-rival">DeepSeek Harness v0.1: Open-Source MIT Rival to Claude Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#API`, `#Pricing`, `#Model Release`

---

<a id="item-12"></a>
## [长江存储首次跻身全球第三大市场份额](https://news.google.com/rss/articles/CBMickFVX3lxTE1IRTNLRE42azI1TWFaWDdEbTRudEtHd1RaMFBxZlp2QXpGUGloeTZ0U2tvcFpRRXo2MGpzWmdnQ0NMSEtxVEtjZkF4RzdIRU4xSjVXbngzVkJ2OUdySmRTUkZjamZFbFNwNS1WYlZSd2pvdw?oc=5) ⭐️ 9.0/10

长江存储（YMTC）首次跻身全球 NAND 闪存市场份额第三名，实现了历史性突破。 这一成就标志着中国半导体自主战略的重要一步，减少了对国外供应商的依赖，并强化了国内供应链。 该公司的成功凸显了中国内存制造商在全球市场的竞争力日益增强。

google\_news · 央广网 · 8月13日 18:57

**背景**: 长江存储是中国领先的半导体公司，专注于 NAND 闪存的生产。全球 NAND 闪存市场长期以来由韩国和日本公司主导，但近年来中国公司正在迅速抢占市场份额。

**标签**: `#semiconductors`, `#memory`, `#China`, `#AI hardware`, `#industry analysis`

---