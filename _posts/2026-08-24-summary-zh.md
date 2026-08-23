---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
content_date: 2026-08-23
lang: zh
---

> 报道范围：2026-08-23（Asia/Shanghai 自然日）

> 从 72 条内容中筛选出 6 条重要资讯。

---

1. [llama.cpp b10595 添加服务器槽位和多操作系统二进制文件](#item-1) ⭐️ 10.0/10
2. [乌兰察布成为中国 AI 算力热土，承诺容量达 12.5 吉瓦](#item-2) ⭐️ 9.0/10
3. [长江存储科创板 IPO 获受理，拟募资 330 亿元](#item-3) ⭐️ 9.0/10
4. [长鑫存储 2026 年 Q2 DRAM 市场份额达 7%](#item-4) ⭐️ 9.0/10
5. [长鑫科技实现巨额财务逆转](#item-5) ⭐️ 9.0/10
6. [OpenAI 修复 Codex 速率限制并重置付费用户用量](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp b10595 添加服务器槽位和多操作系统二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10595) ⭐️ 10.0/10

llama.cpp b10595 版本通过 LLAMA\_SERVER\_SLOTS\_N\_DIFF 引入了服务器槽位管理，并为 macOS、Linux、iOS、Android 和 Windows 提供了预编译的二进制文件。 此次发布通过更好的资源管理和跨不同操作系统的广泛硬件支持，显著增强了 LLM 推理引擎的灵活性和可访问性。 新的槽位管理功能允许优化 KV 缓存重用，该版本包括针对各种 CPU 架构、CUDA 和 Vulkan 等 GPU 后端以及 ROCm 和 OpenVINO 等专用平台的构建。

github · github-actions\[bot\] · 8月23日 21:44

**背景**: llama.cpp 是一个高性能的纯 C/C++ LLM 推理引擎，支持多种硬件后端并提供 OpenAI 兼容的 API。服务器槽位管理是一种通过在多个并发请求之间重用 KV 缓存来优化资源使用的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md">llama.cpp/tools/server/README.md at master · ggml-org/llama ...</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/13606">Tutorial: KV cache reuse with llama-server - GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区成员讨论了 harness（工具/框架）对 LLM 应用的重要性，将其比作汽车底盘和引擎，并争论了 harness 在 AI 生态系统中的未来作用。

**标签**: `#llama.cpp`, `#AI`, `#Inference`, `#OpenSource`, `#AppleSilicon`

---

<a id="item-2"></a>
## [乌兰察布成为中国 AI 算力热土，承诺容量达 12.5 吉瓦](https://www.wired.com/story/the-unlikely-place-at-the-center-of-chinas-ai-boom/) ⭐️ 9.0/10

乌兰察布自 2016 年以来已开业或开工近 100 个数据中心，承诺总容量达 12.5 吉瓦，其中超七成于过去一年宣布。 这一大规模基础设施建设凸显了中国在 AI 基础设施领域的战略布局，尽管面临环境挑战，但得益于成本优势和邻近北京的地缘优势。 DeepSeek、字节跳动、阿里和小红书等主要企业正在当地自建 AI 数据中心，但该地区面临水资源短缺，约 37% 的电力仍来自煤电。

telegram · zaihuapd · 8月23日 08:55

**背景**: 乌兰察布的吸引力在于其低廉的电价、邻近北京以及寒冷气候对数据中心的自然冷却作用，但水资源短缺和煤炭依赖性构成了重大挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Data Centers`, `#Cloud Computing`, `#DeepSeek`, `#Energy`

---

<a id="item-3"></a>
## [长江存储科创板 IPO 获受理，拟募资 330 亿元](https://news.google.com/rss/articles/CBMiTkFVX3lxTE4xSFNKU1luOGRqcHd3WmlRTW0zNEg5R2RvUDNSNkFsRmxSMGg0d2V0aG5ONXZrYmsySDA4WTY1RjJSV0ZudEtCaWVtSE5kZw?oc=5) ⭐️ 9.0/10

长江存储科技股份有限公司的科创板 IPO 申请已获上交所受理，拟募资 330 亿元。 此次 IPO 是中国半导体行业的重要里程碑，有望提升国内存储芯片产能，减少对外国供应商的依赖。 该公司 2026 年第一季度净利润达 333.79 亿元，净利率超过 70%，预计将在 4-6 个月内正式上市。

google\_news · 观点网 · 8月23日 17:37

**背景**: 长江存储是一家领先的半导体公司，专注于 3D NAND 闪存，以其晶栈技术平台著称，该平台能提升存储密度和可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xueqiu.com/9048045332/406146842">长江存储IPO受理！一季度净利333亿，募资330亿，市值冲4万亿…… 重磅消...</a></li>
<li><a href="https://stock.jrj.com.cn/2026/08/21210858207749.shtml">长江存储IPO，已受理！-金融界</a></li>
<li><a href="https://www.guancha.cn/economy/2026_08_19_827843.shtml">长江存储IPO辅导完成</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory`, `#IPO`, `#Yangtze Memory`, `#chips`

---

<a id="item-4"></a>
## [长鑫存储 2026 年 Q2 DRAM 市场份额达 7%](https://news.google.com/rss/articles/CBMikwJBVV95cUxPSHU2VEtuYm4waXE0c19PRGdrQmRhS2ozeDZJcnlrSnhZUDRzbzZuSWFWLTBreHYzclRXczk4c2VfTVprdUZHaXExc0U1aVotTzZ5enJDUGhHQlZYb1poTnh6RmktZzUxX2c3LTBpUGpjeG9yVndLVUZ0MVFkQVVLVnZ2SEJBMjM1aURuci0wWGF0S3E2OUxyY0QxdFJraDRQZU84bERUb1JIX0laX1lzQXNOY0JLVkgtQUVPX1Qxd3hpRVhZem1CYXpZS0JpUlBJWE5IWTZRcVZrM0tPbC1BcVdXZ085eW5SM0o5X1JQR2xYTllBZTM3bUlmckEzUjJtME9lUjlXdjdwUkNBV0NBWkpxRQ?oc=5) ⭐️ 9.0/10

长鑫存储（CXMT）在 2026 年第二季度占据了全球 DRAM 市场 7%的份额，同时其营收同比增长了 716%。 这一显著增长凸显了长鑫存储作为主要 DRAM 厂商的快速崛起，挑战了全球既定竞争对手，并标志着半导体供应链的重大转变。 公司营收增长是由对其 DRAM 产品的强劲需求推动的，但新闻中未提供具体的产品细节或工艺节点。

google\_news · 新浪财经 · 8月23日 17:28

**背景**: 长鑫存储是一家成立于 2016 年的中国半导体公司，专注于为手机、PC 和服务器生产 DRAM。全球 DRAM 市场由三星、SK 海力士和美光主导，长鑫存储已成为一个关键的挑战者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cxmt.com/en/">ABOUT CXMT - CXMT</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://www.counterpointresearch.com/en/insights/global-dram-and-hbm-market-share">Global DRAM and HBM Market Share: Quarterly</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#semiconductors`, `#memory`, `#market\_share`, `#ChangXin`

---

<a id="item-5"></a>
## [长鑫科技实现巨额财务逆转](https://news.google.com/rss/articles/CBMiVkFVX3lxTE1IVUpxY1hOZHpDXzJrVmNITnVpd1U1SmFBWGJwMzJ3U01uOUlSdGR5VGJlNTRvRXNNazBxaHpLaXJxRXBhZTVnZ2llaGdaeE5nV3E2T1p3?oc=5) ⭐️ 9.0/10

长鑫科技（CXMT）报告了惊人的财务逆转，在短短六个月内从巨额亏损转变为 500 亿元人民币的利润。 这一逆转意义重大，因为它展示了中国国内半导体行业在高度竞争的全球市场中展现出的韧性和战略成功。 该新闻强调了 CXMT 财务轨迹的彻底逆转，标志着该公司复苏和增长战略中的一个重要里程碑。

google\_news · 微博 · 8月23日 11:54

**背景**: 长鑫科技是一家领先的专注于 DRAM 存储芯片制造的中国半导体公司。近年来，由于激烈的全球竞争和供应链压力，该公司面临重大挑战。

**标签**: `#semiconductors`, `#memory`, `#CXMT`, `#chip manufacturing`, `#financial turnaround`

---

<a id="item-6"></a>
## [OpenAI 修复 Codex 速率限制并重置付费用户用量](https://x.com/thsottiaux/status/2091407991736332689) ⭐️ 8.0/10

OpenAI 员工 Tibo 宣布，团队将于明日（8 月 24 日）修复 Codex 速率限制问题，并重置所有付费订阅用户的用量，此前团队发现长会话中使用图片存在效率缺陷，以及 Computer History 功能的 p95 以上用量过高。 此次更新对依赖 Codex 的开发者具有重要意义，因为它解决了性能瓶颈并确保了公平的资源分配，而新的效率方法有望改善整体用户体验和模型行为。 此次修复针对三个具体问题：长会话中使用图片的效率低下、Computer History 功能的 p95 以上用量过高，以及生成对话标题的功能消耗超出预期。一种新的效率方法将于下周实施，用量重置将在太平洋标准时间下午两点（北京时间凌晨五点）左右进行。

telegram · zaihuapd · 8月23日 14:26

**背景**: Codex 是 OpenAI 的代码生成模型，速率限制是为了管理服务器负载和确保公平访问而设定的使用限制。Computer History 功能面向 Pro、Business 和 Enterprise 用户，可在 macOS 上记录应用程序和网页活动，为 ChatGPT 和 Codex 提供上下文。p95 是一个统计指标，表示 95% 的数据点低于该值的性能度量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chatgpt.com/codex/pricing/">Codex Pricing</a></li>
<li><a href="https://help.openai.com/en/articles/20001106-codex-rate-card">ChatGPT Rate Card (Business, Enterprise/Edu credit-based ...</a></li>
<li><a href="https://kingy.ai/news/openai-computer-history/">OpenAI Computer History : How It Works and Key Risks</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#AI Compute`, `#Rate Limits`, `#Developer Tools`

---