---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
content_date: 2026-08-31
lang: zh
---

> 报道范围：2026-08-31（Asia/Shanghai 自然日）

> 从 113 条内容中筛选出 12 条重要资讯。

---

1. [ggml-org/llama.cpp released b10705](#item-1) ⭐️ 10.0/10
2. [NVIDIA TensorRT-LLM v1.3.0rc25 发布，默认启用 KV Cache Manager V2](#item-2) ⭐️ 10.0/10
3. [寒序科技公布 MRAM 推理产品路线，首代 uHBM 片内带宽设计 24 TB/s](#item-3) ⭐️ 10.0/10
4. [长鑫存储已开始小批量生产 HBM3E 内存 - cnBeta.COM](#item-4) ⭐️ 10.0/10
5. [ggml-org/llama.cpp 发布了 b10720 版本](#item-5) ⭐️ 9.0/10
6. [NeurIPS accepted papers leaked? \[D\]](#item-6) ⭐️ 9.0/10
7. [Anthropic 警告木马正在窃取 Claude 会话](#item-7) ⭐️ 9.0/10
8. [长鑫宣布 LPDDR6 内存正式量产](#item-8) ⭐️ 9.0/10
9. [长鑫存储状告五角大楼：一家 DRAM 新贵的法律反击 - or100.cc](#item-9) ⭐️ 9.0/10
10. [Apple caught off guard by AI demand for Mac Mini and Mac Studio](#item-10) ⭐️ 8.0/10
11. [我认为军方军需店的冰箱遭到了黑客攻击](#item-11) ⭐️ 8.0/10
12. [Understanding ChatGPT Work](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10705](https://github.com/ggml-org/llama.cpp/releases/tag/b10705) ⭐️ 10.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

github · github-actions\[bot\] · 8月31日 07:15

**标签**: `#AI`, `#Machine Learning`, `#Software Development`, `#Hardware Acceleration`, `#Open Source`

---

<a id="item-2"></a>
## [NVIDIA TensorRT-LLM v1.3.0rc25 发布，默认启用 KV Cache Manager V2](https://github.com/NVIDIA/TensorRT-LLM/releases/tag/v1.3.0rc25) ⭐️ 10.0/10

NVIDIA/TensorRT-LLM v1.3.0rc25 默认引入 KV Cache Manager V2，以提升 DeepSeek V3、R1、V4、GLM-5、GPT-OSS、Mistral Large 3、Kimi K2/K2.5/K3、MiniMax M2/M3、Nemotron H、Qwen3-Next/3.5/3.8、Gemma 3/4 等多个模型的扩展性和稳定性。 此次发布对 AI 推理优化具有重要意义，因为 KV Cache Manager V2 是推荐架构，能提供更好的性能和稳定性，并且影响广泛流行的开源和商业模型。 此次发布包含大量已知问题，如去中心化服务挂起、生成挂起、B200 GPU 上的内存崩溃、特定配置下的精度损失，以及 MiniMax-M3 MXFP8 和 Kimi K3 96-head MLA 等特定模型的不支持功能。

github · tongyuantongyu · 8月31日 11:24

**背景**: TensorRT-LLM 是 NVIDIA 的高性能 LLM 推理引擎，针对 NVIDIA GPU 进行优化。KV Cache Manager 是一个在生成过程中管理键值对缓存的组件，能提高效率并减少内存使用。

**标签**: `#NVIDIA`, `#TensorRT-LLM`, `#AI Inference`, `#KV Cache`, `#DeepSeek`

---

<a id="item-3"></a>
## [寒序科技公布 MRAM 推理产品路线，首代 uHBM 片内带宽设计 24 TB/s](https://mp.weixin.qq.com/s/adyFanNueXUHKnxr9m64kg) ⭐️ 10.0/10

国内首家 MRAM 磁计算公司寒序科技公布了 uHBM 与 uLPU 推理计算架构，首代 uHBM 片内读带宽设计值 24 TB/s，uLPU 面向 4B 多模态模型提出超 2000 Tokens/s Decode 目标。 这一突破通过利用 MRAM 的持久内存特性，解决了大型语言模型对高速、低延迟推理的关键需求，有望减少数据移动瓶颈并提高 AI 加速器的能效。 SpinPU-ED01 验证芯片已通过第三方检测和 24 小时稳定运行验证，其架构设计将模型权重驻留在 Persistent MRAM 阵列中，并在片内完成矩阵-向量运算，以减少权重重复搬运。

telegram · zaihuapd · 8月31日 21:41

**背景**: 高带宽内存（HBM）是一种下一代内存架构，可实现更快的数据传输和紧凑集成，对于支持大型语言模型和高级图形渲染至关重要。MRAM（磁阻随机存取存储器）是一种基于自旋电子学的存储技术，提供持久存储和高耐用性，使其适合于边缘 AI 硬件，其中需要存储模型权重和中间状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mram-info.com/">MRAM -Info | MRAM Industry Portal</a></li>
<li><a href="https://www.microchipusa.com/electrical-components/ultimate-guide-to-high-bandwidth-memory">Ultimate Guide to High Bandwidth Memory</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**标签**: `#MRAM`, `#AI Accelerators`, `#Hardware Architecture`, `#Inference`, `#uHBM`

---

<a id="item-4"></a>
## [长鑫存储已开始小批量生产 HBM3E 内存 - cnBeta.COM](https://news.google.com/rss/articles/CBMiYEFVX3lxTFB5TVNTY05ndm00OG1mbFVMVjdQTk1BYUpZREJSb25GcmwwMjNYM0tDM2luMlJ0SXpuRkdZQkRpUF94UW5IS1ZxRmV0SlpVN25QdDBzT3Bja0xNSXlUSmdCZQ?oc=5) ⭐️ 10.0/10

长鑫存储已启动 HBM3E 内存的小批量生产。

google\_news · cnBeta.COM · 8月31日 22:41

**标签**: `#HBM3E`, `#AI Memory`, `#Semiconductors`, `#Chips`, `#AI Compute`

---

<a id="item-5"></a>
## [ggml-org/llama.cpp 发布了 b10720 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b10720) ⭐️ 9.0/10

llama.cpp b10720 版本添加了 ROCm radix TOP\_K 优化，并提供了跨平台二进制文件。

github · github-actions\[bot\] · 8月31日 23:28

**标签**: `#llama.cpp`, `#ROCm`, `#AI`, `#cross-platform`, `#optimization`

---

<a id="item-6"></a>
## [NeurIPS accepted papers leaked? \[D\]](https://www.reddit.com/r/MachineLearning/comments/1w2r1f3/neurips_accepted_papers_leaked_d/) ⭐️ 9.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

reddit · r/MachineLearning · /u/Feuilius · 8月31日 03:34

**标签**: `#neurips`, `#machine-learning`, `#data-leak`, `#github`, `#community-discussion`

---

<a id="item-7"></a>
## [Anthropic 警告木马正在窃取 Claude 会话](https://www.searchenginejournal.com/anthropic-warns-hackers-are-stealing-claude-sessions-to-hijack-accounts/587566/) ⭐️ 9.0/10

Anthropic 检测到木马活动正在窃取 Claude 登录会话以劫持用户账户并消耗其使用额度。该公司已强制登出受影响账户并删除保存的付款方式。 这一事件凸显了 AI 服务平台的一个关键安全漏洞，即木马可以绕过双重验证以访问敏感的用户数据和财务信息。 木马包括 Windows 变种如 Vidar、LummaC2、StealC、RedLine 和 Acreed，以及名为 AMOS 的 Mac 木马。建议用户停止使用破解软件，清除 Cookie，并在感染时考虑重装系统。

telegram · zaihuapd · 8月31日 11:22

**标签**: `#security`, `#malware`, `#anthropic`, `#claude`, `#account-hijacking`

---

<a id="item-8"></a>
## [长鑫宣布 LPDDR6 内存正式量产](https://news.google.com/rss/articles/CBMiXEFVX3lxTE85Tk42a1hGZzJCTEhSdTZCN2NEejRfdERuNHBMd1JCS2k4WnYyZFpzWGxKcjRDLWJhaVZWRlBrNU03dE9mQzNRMldxcUFOSzNsYkVHLUVCWmNBOGlJ?oc=5) ⭐️ 9.0/10

长鑫存储（CXMT）正式宣布其 LPDDR6 内存芯片已实现量产，这标志着国内半导体制造取得了重要进展。 LPDDR6 是现代 AI 加速器和高性能计算系统的关键组件，实现量产将加强中国在全球内存供应链中的地位。 虽然提供的内容中没有详细说明具体的技术规格，如数据速率或功耗，但该公告确认了从开发到量产的顺利过渡。

google\_news · 证券时报 · 8月31日 00:00

**背景**: LPDDR（低功耗双倍数据速率）内存是一种专为移动设备和低功耗计算设计的 SDRAM 类型，相比标准 DDR 提供更高的带宽和效率。LPDDR6 代表了最新一代技术，相比 LPDDR5 承诺更快的速度和更低的功耗。

**标签**: `#semiconductors`, `#memory`, `#AI accelerators`, `#hardware`, `#mass production`

---

<a id="item-9"></a>
## [长鑫存储状告五角大楼：一家 DRAM 新贵的法律反击 - or100.cc](https://news.google.com/rss/articles/CBMiREFVX3lxTE9kMHJveGhJeExPcUR1VnZtVnVuZno3VmVmRUpVMzBLcGxxWTMySEVyUkdZaF9jOVRYUU00cnpieE0ybUh1?oc=5) ⭐️ 9.0/10

中国 DRAM 制造商长鑫存储（CXMT）就其被列入黑名单一事，对美国国防部提起诉讼。

google\_news · or100.cc · 8月31日 11:14

**标签**: `#DRAM`, `#semiconductors`, `#national-security`, `#export-controls`, `#legal-dispute`

---

<a id="item-10"></a>
## [Apple caught off guard by AI demand for Mac Mini and Mac Studio](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/) ⭐️ 8.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

hackernews · thm · 8月31日 20:41 · [社区讨论](https://news.ycombinator.com/item?id=49508982)

**标签**: `#Apple`, `#AI`, `#Mac`, `#Hardware`, `#Local AI`

---

<a id="item-11"></a>
## [我认为军方军需店的冰箱遭到了黑客攻击](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) ⭐️ 8.0/10

军方军需店冰箱可能遭受黑客攻击，引发了人们对基础设施安全及配置错误的担忧。

hackernews · jcurbo · 8月31日 19:45 · [社区讨论](https://news.ycombinator.com/item?id=49508506)

**标签**: `#security`, `#infrastructure`, `#industrial systems`, `#military`, `#cybersecurity`

---

<a id="item-12"></a>
## [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

该条资讯的中文内容暂不可用；请查看原文链接获取详情。

rss · Simon Willison · 8月31日 07:59

**标签**: `#AI`, `#Productivity`, `#Software Tools`, `#OpenAI`, `#Developer Experience`

---