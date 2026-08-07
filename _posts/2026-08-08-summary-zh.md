---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
content_date: 2026-08-07
lang: zh
---

> 报道范围：2026-08-07（Asia/Shanghai 自然日）

> 从 102 条内容中筛选出 12 条重要资讯。

---

1. [llama.cpp b10301 版本发布：修复 CUDA 问题并提供多平台预编译二进制文件](#item-1) ⭐️ 10.0/10
2. [Datasette 1.0a38 修复了严重的 SQL 注入漏洞](#item-2) ⭐️ 10.0/10
3. [SK 海力士确认采用晶圆键合技术的 375 层 V10 NAND 闪存](#item-3) ⭐️ 10.0/10
4. [sub2api OAuth 漏洞允许仅凭邮箱接管账户](#item-4) ⭐️ 10.0/10
5. [让 Postgres 在分析场景下提速 300 倍](#item-5) ⭐️ 9.0/10
6. [据报道 2027 年内存容量已售罄](#item-6) ⭐️ 9.0/10
7. [Datasette 0.65.3 回溯移植 SQL 注入安全修复](#item-7) ⭐️ 9.0/10
8. [DeepMind 的战略失误使 Google Cloud Platform 受益](#item-8) ⭐️ 9.0/10
9. [Cloudflare 推出针对机器人和代理的持续信任评估](#item-9) ⭐️ 9.0/10
10. [Cloudflare 将 Workers AI 和 AI Gateway 统一为单一控制平面](#item-10) ⭐️ 9.0/10
11. [在安卓手机上训练的 MLP 分类器](#item-11) ⭐️ 9.0/10
12. [Bad Apple 视频的改进神经网络压缩](#item-12) ⭐️ 9.0/10

---

<a id="item-1"></a>
## [llama.cpp b10301 版本发布：修复 CUDA 问题并提供多平台预编译二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10301) ⭐️ 10.0/10

llama.cpp 的 b10301 版本修复了 CUDA 中未使用变量和函数的警告，同时为 macOS、iOS、Linux、Android 和 Windows 提供了多种架构的预编译二进制文件。 此次发布通过解决 CUDA 兼容性问题并确保广泛的硬件支持，显著提高了 llama.cpp（一个领先的开源 LLM 推理引擎）的可用性和性能。 CUDA 修复解决了编译器警告，该版本还包括禁用的 macOS Apple Silicon KleidiAI 支持，以及针对不同平台和加速器（如 Vulkan、ROCm 和 OpenVINO）的广泛二进制选项。

github · github-actions\[bot\] · 8月7日 17:59

**背景**: llama.cpp 是一个用于在本地运行大语言模型的开源库，常被用作 Ollama 和 LM Studio 等工具的核心。CUDA 是 Nvidia 的并行计算平台，用于为 AI 任务提供 GPU 加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cuda_framework">Cuda framework</a></li>
<li><a href="https://github.com/ARM-software/kleidiai">GitHub - ARM-software/kleidiai: This repository is a read-only mirror of https://gitlab.arm.com/kleidi/kleidiai · GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI`, `#open-source`, `#CUDA`, `#macOS`

---

<a id="item-2"></a>
## [Datasette 1.0a38 修复了严重的 SQL 注入漏洞](https://simonwillison.net/2026/Aug/6/datasette/#atom-everything) ⭐️ 10.0/10

Datasette 1.0a38 修复了一个关键的 SQL 注入漏洞，该漏洞影响使用 Datasette 权限系统提供混合公开和私有表的实例。 对于暴露私有表的系统管理员来说，这一安全修复至关重要，因为它可以防止通过 SQL 注入攻击未经授权访问敏感数据。 该漏洞允许访问公开表的用户执行 SQL 注入攻击，绕过限制读取私有表数据。管理员应建议在受影响的数据库上禁用 &\#x27;execute-sql&\#x27; 权限。

rss · Simon Willison · 8月7日 02:24

**背景**: Datasette 是一个用于探索和发布数据的开源工具，具有权限系统来控制对数据库和表的访问。身份验证系统允许管理员根据用户角色限制访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/latest/authentication.html">Authentication and permissions - Datasette documentation</a></li>
<li><a href="https://simonw.substack.com/p/a-new-sql-powered-permissions-system">A new SQL-powered permissions system in Datasette 1.0a20</a></li>

</ul>
</details>

**标签**: `#datasette`, `#security`, `#sql-injection`, `#developer-tools`, `#data-centric`

---

<a id="item-3"></a>
## [SK 海力士确认采用晶圆键合技术的 375 层 V10 NAND 闪存](https://www.gelonghui.com/live/2599953) ⭐️ 10.0/10

SK 海力士在 FMS 2026 峰会上宣布，其新一代 V10 NAND 闪存采用 375 层堆叠设计，并成为该公司首款采用晶圆键合技术的 NAND 产品。 这一进展对半导体行业具有重要意义，因为它推动了 3D NAND 堆叠的极限，并引入了晶圆键合技术，这对未来高密度存储解决方案至关重要。 V10 NAND 的每瓦性能相比前代 321 层 V9 产品提升了 2.5 倍，专为需要兼顾能效和性能的 AI 基础设施环境而优化。

telegram · zaihuapd · 8月7日 20:19

**背景**: 3D NAND 闪存通过垂直堆叠存储单元来提高密度，SK 海力士的 V9 是 321 层 4D NAND。晶圆键合是一种将两个半导体晶圆连接起来的技术，能够实现先进封装和更高的层数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.163.com/dy/article/KV4PG1NG0550WHYR.html">SK海力士V10 NAND 采用 375 层 堆 叠 设计 2026年内量产_手机网易网</a></li>
<li><a href="https://www.chinaflashmarket.com/a/183951">375 层 ！ SK海力士下一代 NAND 年底前量产_CFM 闪 存 市场</a></li>

</ul>
</details>

**标签**: `#NAND Flash`, `#Semiconductors`, `#AI Infrastructure`, `#SK Hynix`, `#Wafer Bonding`

---

<a id="item-4"></a>
## [sub2api OAuth 漏洞允许仅凭邮箱接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 10.0/10

sub2api v0.1.171 及之前版本存在一个 CVSS 8.8 的高危 OAuth 账户接管漏洞，攻击者仅需知道受害者注册邮箱，无需密码或验证码、无需用户交互，即可通过接口将自己的 OAuth 身份绑定到受害者账户。 该漏洞影响重大，因为它允许攻击者完全控制账户，包括 API 密钥、账单余额和订阅配额，对 sub2api 服务的用户构成严重风险，并凸显了 OAuth 实现中可能影响类似系统的关键缺陷。 攻击者利用 pending session 流程中 existingUser 分支不校验密码和验证码的缺陷，将目标用户 ID 设为受害者后完成 OAuth 身份绑定，此后攻击者每次 OAuth 登录均会解析为受害者账户。

telegram · zaihuapd · 8月7日 22:59

**背景**: OAuth 是一种开放授权标准，允许用户在不共享密码的情况下授予第三方应用程序对其账户的有限访问权限，但授权流程中的配置错误可能导致严重的安全漏洞，如账户接管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Wei-Shaw/sub2api/security/advisories/GHSA-vc2q-289v-74g3">Password Reset Poisoning via Host Header Trust Issue Leading to Account Takeover · Advisory · Wei-Shaw/sub2api · GitHub</a></li>
<li><a href="https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow">Lab: Authentication bypass via OAuth implicit flow | Web Security Academy</a></li>
<li><a href="https://gaya3-r.medium.com/account-takeover-using-oauth-misconfiguration-3fab424317c1">Account takeover using OAuth Misconfiguration | by gayatri r | Medium</a></li>

</ul>
</details>

**标签**: `#OAuth`, `#Security`, `#Account Takeover`, `#Vulnerability`, `#sub2api`

---

<a id="item-5"></a>
## [让 Postgres 在分析场景下提速 300 倍](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 9.0/10

作者实现了 pgrust，这是一个基于 Rust 的 Postgres 扩展，通过批处理、算子融合和 SIMD 技术将分析查询速度提升了 300 倍。 这一突破解决了 Postgres 在分析场景下的传统性能瓶颈，使其在处理数据密集型工作负载时更具竞争力。 优化过程包括形式化验证和差分模糊测试以确保正确性，证明了超过 1000 个面向用户的功能在 pgrust 和 Postgres 中具有相同的逻辑。

hackernews · poly2it · 8月7日 19:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: SIMD（单指令多数据）允许 CPU 并行处理多个数据元素，而算子融合通过合并顺序操作来减少内存流量。批处理通过以组为单位处理数据来提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@enerzai/optimium-101-3-optimium-utilized-operator-fusion-the-attack-was-super-effective-f2fc43d47d9b">Optimium 101 (3): Optimium utilized Operator Fusion ! | Medium</a></li>
<li><a href="https://www.starrocks.io/blog/deep-dive-how-starrocks-built-a-high-performance-vectorized-engine/index.html">Deep Dive: How StarRocks Built a High- Performance Vectorized Engine</a></li>

</ul>
</details>

**社区讨论**: 社区成员对技术深度表示兴奋，但也提出了关于采用的担忧，指出信任和长期稳定性是超越性能的关键因素。

**标签**: `#Postgres`, `#Query Optimization`, `#SIMD`, `#Software Engineering`, `#Database Performance`

---

<a id="item-6"></a>
## [据报道 2027 年内存容量已售罄](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 9.0/10

一份报告显示，2027 年的内存容量已全部售罄，这主要是由 AI 应用的高需求和生产限制推动的。 这种短缺凸显了内存对 AI 基础设施的关键作用，以及扩大生产以满足日益增长的计算需求的挑战。 HBM 生产消耗的晶圆容量远高于标准 DRAM，HBM3E 生产相同数量的比特大约需要 DDR5 三倍的晶圆供应。

hackernews · inigyou · 8月7日 15:58 · [社区讨论](https://news.ycombinator.com/item?id=49207236)

**背景**: 高带宽内存（HBM）是一种用于 AI 加速器和高性能 GPU 的 3D 堆叠内存技术。其垂直堆叠和高速度接口使其成为 AI 工作负载的关键，但制造限制制约了其可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://oretonstorage.com/blog/as-hbm-demand-surges-with-ai-growth-ddr-supply-dynamics-are-shifting-we-analyze-wafer-allocation-packaging-bottlenecks-and-dram-pricing-implications">How HBM Production Is Constraining DDR Supply</a></li>

</ul>
</details>

**社区讨论**: 用户讨论了内存短缺对其设置的影响，一些人注意到价格上涨，另一些人则对 AI 日益增长的内存需求表示担忧。

**标签**: `#HBM`, `#DRAM`, `#AI`, `#Memory`, `#Semiconductors`

---

<a id="item-7"></a>
## [Datasette 0.65.3 回溯移植 SQL 注入安全修复](https://simonwillison.net/2026/Aug/6/datasette-2/#atom-everything) ⭐️ 9.0/10

Datasette 0.65.3 从版本 1.0a38 回溯移植了一个 SQL 注入安全修复，解决了在同时提供公共和私有表的实例中的漏洞。 这个安全修复对于运行具有混合访问权限的 Datasette 的用户至关重要，因为它可以防止潜在的数据泄露和未经授权的数据库操作。 该修复解决了在使用动态字段名进行查询时出现的 SQL 注入漏洞，可能涉及参数化查询或输入验证的改进。

rss · Simon Willison · 8月7日 02:22

**背景**: Datasette 是一个用于探索和发布数据的开源工具，它将 SQLite 数据库视为只读，以最大限度地减少 SQL 注入等安全风险。1.0a38 中的安全问题影响了具有混合公共和私有表的实例，其中 Datasette 权限系统可能被利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/latest/sql_queries.html">Running SQL queries - Datasette documentation</a></li>
<li><a href="https://simonwillison.net/2026/Aug/6/datasette/">Release: datasette 1.0a38</a></li>

</ul>
</details>

**标签**: `#datasette`, `#security`, `#sql-injection`, `#software-release`, `#python`

---

<a id="item-8"></a>
## [DeepMind 的战略失误使 Google Cloud Platform 受益](https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking) ⭐️ 9.0/10

随着 DeepMind 的战略重心转移，Google Cloud Platform \(GCP\) 正在获得市场份额，这导致了资源的重新分配。 这种转变凸显了 AI 行业中短期金融化与长期创新之间的张力，对竞争对手和投资者具有重大影响。 GCP 目前产生 2000 亿美元的外部销售，利润率高，而 DeepMind 的自营业务仍仅为 120 亿美元，表明了明确的管理优先级。

rss · Semianalysis · 8月7日 10:32

**背景**: 谷歌于 2014 年收购 DeepMind 以获得研究能力和声望，但最近的战略失误优先考虑了 GCP 的财务表现而非前沿 AI 领导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking">or why DeepMind &#x27;s long term failure is GCP &#x27;s short term gain</a></li>
<li><a href="https://beneficial.cloud/attracting-ai-talent-lessons-from-google-deepmind-s-acquisit">Attracting AI Talent: Lessons from DeepMind</a></li>
<li><a href="https://startupshortcut.com/knowledge-base/how-google-deepmind-mastered-ai-for-strategic-growth-and-innovation">How Google DeepMind Drove AI Growth &amp; Innovation | StartupShortcut</a></li>

</ul>
</details>

**标签**: `#AI Compute`, `#Google Cloud`, `#DeepMind`, `#Strategic Analysis`, `#AI Infrastructure`

---

<a id="item-9"></a>
## [Cloudflare 推出针对机器人和代理的持续信任评估](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/) ⭐️ 9.0/10

Cloudflare 正将机器人防御从单次风险评估转向持续信任评估，引入了 BotBase 和 Precursor 等系统来评估良好和不良行为，并提供 Precursor Trace 模拟工具来评估光标移动。 这种向持续信任评估的转变提高了区分真实用户和自动化工具的检测精度，无需依赖激进的挑战，从而减少合法用户的不必要中断，并提高机器人开发者的运营成本。 Precursor 在浏览器中运行持续验证，以检测在单个请求中看似合法但在会话中表现出非人类模式的自动化工具，而 BotBase 和 Precursor 则监控整个会话中的用户行为以捕获复杂的机器人。

rss · Cloudflare Blog · 8月7日 21:01

**背景**: 传统的机器人防御通常依赖单次风险评估，但 Cloudflare 的新方法使用持续客户端信号和会话长分析来更好地区分人类和机器，这与持续自适应信任解决方案的更广泛趋势相一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/good-and-bad-agentic-behaviors/">Unveiling good and bad behaviors on the Agentic Internet | Cloudflare Blog</a></li>
<li><a href="https://blog.cloudflare.com/introducing-precursor/">Introducing Precursor: detecting agentic behavior with continuous client-side signals | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-challenges/precursor/">Precursor · Cloudflare challenges docs</a></li>

</ul>
</details>

**标签**: `#bot-mitigation`, `#ai-security`, `#cloudflare`, `#trust-evaluation`, `#simulation`

---

<a id="item-10"></a>
## [Cloudflare 将 Workers AI 和 AI Gateway 统一为单一控制平面](https://blog.cloudflare.com/workers-ai-gateway-unification/) ⭐️ 9.0/10

Cloudflare 将 Workers AI 和 AI Gateway 统一为单一控制平面，为开发者提供跨托管 GPU 和外部 AI 提供商的统一可观测性、计费和动态路由功能。 这种统一简化了构建弹性 AI 应用的过程，通过集中管理和优化资源分配，这对大规模采用 AI 的企业至关重要。 统一控制平面引入了统一绑定和模型优先路由，实现了 AI 模型和提供商的无缝集成与动态选择。

rss · Cloudflare Blog · 8月7日 21:00

**背景**: AI 控制平面是一个关键层，通过执行策略、确保合规性并在模型和代理之间提供可见性来治理 AI 交互。动态路由通过根据输入和上下文动态选择最佳模型或提供商来提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/workers-ai-gateway-unification/">Unifying Workers AI and AI Gateway into a single AI control plane | Cloudflare Blog</a></li>
<li><a href="https://www.linkedin.com/pulse/rise-ai-control-planes-governing-models-agents-scale-mahmoud-abufadda-d1f5f">The Rise of AI Control Planes : Governing Models, Agents and...</a></li>
<li><a href="https://www.areebi.com/ai-control-plane">AI Control Plane - Areebi | Areebi</a></li>

</ul>
</details>

**标签**: `#AI Gateway`, `#Workers AI`, `#Cloudflare`, `#AI Control Plane`, `#Developer Tools`

---

<a id="item-11"></a>
## [在安卓手机上训练的 MLP 分类器](https://www.reddit.com/r/MachineLearning/comments/1vhwwfr/imagenet1k_classifier_trained_entirely_on_an/) ⭐️ 9.0/10

研究人员使用 PyTorch 和 Termux 在安卓手机上训练了一个小型 MLP 分类器，在缩放后的 Imagenet-1k 数据集上实现了 4.59%的 Top-1 验证准确率。 这证明了在设备上训练的可行性，可能使移动设备上的隐私保护和资源高效的机器学习应用成为可能。 该模型使用 50 万个参数，在 30 分钟内使用 Dimensity 9300+ CPU 的 4 个 Cortex-X4 核心，在 32x32 图像上训练 5 个 epoch，并使用 PyArrow 处理数据集。

reddit · r/MachineLearning · /u/Tall\_Abrocoma\_3533 · 8月7日 18:30

**背景**: Termux 是安卓的终端模拟器，通过 PyTorch 等包扩展功能，而 Imagenet-1k 是用于图像分类基准测试的标准数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Building_Android_applications_in_Termux_using_Gradle">Building Android applications in Termux using Gradle</a></li>
<li><a href="https://arrow.apache.org/docs/python/generated/pyarrow.dataset.Dataset.html">pyarrow . dataset . Dataset — Apache Arrow v25.0.0</a></li>

</ul>
</details>

**标签**: `#on-device-ml`, `#mobile-computing`, `#pytorch`, `#edge-ai`, `#hardware-software-co-design`

---

<a id="item-12"></a>
## [Bad Apple 视频的改进神经网络压缩](https://www.reddit.com/r/MachineLearning/comments/1vhvfws/improved_compression_of_bad_apple_into_a_neural/) ⭐️ 9.0/10

作者通过使用不同的批量采样器和将整个视频的像素输入，改进了基于神经网络的&\#x27;Bad Apple&\#x27;视频压缩模型，在保持相同的 4x512 宽正弦层和 792,257 参数的情况下，实现了更忠实的视频重现。 这一进展展示了隐式神经表示在视频压缩中的潜力，提供了关于模型架构和训练策略的见解，可能有助于 AI 驱动的媒体压缩领域的更广泛发展。 使用 GPT5.6 重新实现的模型在全帧率模式下质量较差，因为它无法学习运动并产生无意义的中间帧，尽管低速率版本保持了高保真度。

reddit · r/MachineLearning · /u/cpldcpu · 8月7日 17:06

**背景**: 隐式神经表示（如 SIREN 网络）将数据编码为连续函数，能够从稀疏输入中实现高保真重建，并越来越多地与传统编解码器一起用于视频压缩任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>
<li><a href="https://reelmind.ai/blog/neural-network-video-compression-technology">Neural Network Video Compression Technology | ReelMind</a></li>

</ul>
</details>

**标签**: `#neural-networks`, `#video-compression`, `#machine-learning`, `#siren-network`, `#gpt5.6`

---