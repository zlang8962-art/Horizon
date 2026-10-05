---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
content_date: 2026-10-04
lang: zh
---

> 报道范围：2026-10-04（Asia/Shanghai 自然日）

> 从 61 条内容中筛选出 10 条重要资讯。

---

1. [ggml-org/llama.cpp 发布了 b11392 版本](#item-1) ⭐️ 10.0/10
2. [在 RTX 4090 上以 100T/s 的速度运行 Qwen 3.8 Flash-Next 125B 模型](#item-2) ⭐️ 9.0/10
3. [呼吁在 API 和服务上实施默认硬性预算上限](#item-3) ⭐️ 9.0/10
4. [ARC-AGI-3 在 Kaggle 上的得分从 7% 跃升至 56%](#item-4) ⭐️ 9.0/10
5. [DynaBase：用于零样本动力系统重建的最小可解释架构](#item-5) ⭐️ 9.0/10
6. [谷歌研究：要求“诚实作答”可显著改善大模型报告](#item-6) ⭐️ 9.0/10
7. [韩国四家银行外围系统接连发生数据泄露](#item-7) ⭐️ 9.0/10
8. [长江存储创纪录的 IPO](#item-8) ⭐️ 9.0/10
9. [国产半导体设备 IPO：风险与挑战](#item-9) ⭐️ 8.0/10
10. [中国大陆占全球 DRAM+NAND 芯片产能 26%，长存+长鑫占 14.5%](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp 发布了 b11392 版本](https://github.com/ggml-org/llama.cpp/releases/tag/b11392) ⭐️ 10.0/10

llama.cpp b11392 版本提供了在 CPU 上运行大语言模型的跨平台二进制文件。

github · github-actions\[bot\] · 10月4日 22:41

**标签**: `#llama.cpp`, `#inference`, `#open-source`, `#cross-platform`, `#macOS`

---

<a id="item-2"></a>
## [在 RTX 4090 上以 100T/s 的速度运行 Qwen 3.8 Flash-Next 125B 模型](https://github.com/Niko1221/Strata) ⭐️ 9.0/10

一个名为 Strata 的 GitHub 项目展示了如何在 RTX 4090 等消费级硬件上以每秒 100 个 token 的速度运行 Qwen 3.8 Flash-Next 125B 模型。 这一突破使得在消费级硬件上本地推理一个庞大的 125B 参数模型成为可能，从而普及了高性能 AI 的访问，并减少了对云服务的依赖。 该实现使用了 GGUF 和 IQ3\_S 等量化技术，基准测试显示在 RTX 4090 上达到 124 tokens/sec，并与 llama.cpp 的性能相媲美。

hackernews · snehesht · 10月4日 20:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: Qwen 3.8 Flash-Next 是阿里巴巴的一个 125B 参数 MoE（混合专家）模型，旨在降低训练和推理成本，同时保持卓越的编码能力。量化通过压缩权重来减小模型大小和内存占用，从而在消费级 GPU 上实现更快的推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata">GitHub - Niko1221/Strata: Qwen3.8-Flash-Next on any consumer hardware ...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>

</ul>
</details>

**社区讨论**: 用户反馈不一：有人称赞 4 位量化在编码任务中的质量，而另一个人则指出视觉基准测试性能落后于 llama.cpp。有些人对炒作持怀疑态度，而另一些人则分享了在 RTX 4090 上达到 124 tokens/sec 的惊人速度。

**标签**: `#AI`, `#Quantization`, `#Inference`, `#Benchmarking`, `#Hardware`

---

<a id="item-3"></a>
## [呼吁在 API 和服务上实施默认硬性预算上限](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 9.0/10

Simon Willison 倡议在按使用量付费的服务和 API 上实施默认硬性预算上限，当支出达到配置的限制时自动切断服务。 这很重要，因为编码代理和自动化系统可能会意外产生费用，硬性上限可以防止企业和个人遭遇财务意外。 AWS 最近推出了支出上限功能，当达到月度支出限制时会暂停项目，而 Google Cloud 在 7 月推出了针对特定服务的“支出上限”。

rss · Simon Willison · 10月4日 07:34

**背景**: 编码代理是自主的 AI 工具，可以启动代码执行任务，通常与按使用量计费的 API 或云服务交互，从而产生失控费用的潜在风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/">We’re going to need default hard budget caps on pretty much...</a></li>

</ul>
</details>

**标签**: `#APIs`, `#Cost Control`, `#Software Engineering`, `#Security`, `#AI`

---

<a id="item-4"></a>
## [ARC-AGI-3 在 Kaggle 上的得分从 7% 跃升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 9.0/10

ARC-AGI-3 在 Kaggle 上的得分在 30 天内从 7% 跃升至 56%，本地模型的表现超过了人类平均水平。 这一突破挑战了基准测试“对人类容易，对 AI 难”的设计原则，并预示着通用人工智能（AGI）评估可能发生转变。 这一提升是通过在 harness 中使用小型本地模型实现的，尽管排行榜图表略显过时。

reddit · r/MachineLearning · /u/we\_are\_mammals · 10月4日 18:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI-3 是一个交互式推理基准测试，旨在衡量 AI 代理在陌生环境中学习的能力，人类表现被设定为 100%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://www.datacamp.com/blog/arc-agi-3">ARC-AGI-3: The New Interactive Reasoning Benchmark - DataCamp</a></li>
<li><a href="https://stackbuiltai.com/arc-agi-3-explained-2026/">ARC-AGI-3 Explained: The Benchmark That Says We&#x27;re NOT Close ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Machine Learning`, `#Benchmark`, `#ARC-AGI`, `#Local Models`

---

<a id="item-5"></a>
## [DynaBase：用于零样本动力系统重建的最小可解释架构](https://www.reddit.com/r/MachineLearning/comments/1wxex8n/a_minimal_interpretable_architecture_for_zeroshot/) ⭐️ 9.0/10

研究人员介绍了 DynaBase，这是一种用于零样本动力系统重建的最小可解释架构，使用单个参数 α 和上下文选择器来忠实地重现长期统计和几何属性。 DynaBase 为分析和理解时间序列和动力系统基础模型提供了一个可处理的数学工具，可能有助于提高它们的性能和训练机制。 该架构使用分段仿射映射，其中单个参数 α 控制局部收敛/发散率，并使用上下文选择器选择最接近的数据点，从而能够重现固定点、极限环和混沌吸引子。

reddit · r/MachineLearning · /u/DangerousFunny1371 · 10月4日 20:49

**背景**: 动力系统 \(DS\) 是描述系统随时间演变的数学模型，通常表现出混沌等复杂行为。DS 基础模型旨在从数据中重建这些系统，但往往缺乏可解释性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.14937">A Minimal Interpretable Architecture for Zero - Shot Reconstruction of ...</a></li>
<li><a href="https://gist.science/paper/2607.14937">A Minimal Interpretable Architecture for Zero - Shot ... | Gist.Science</a></li>
<li><a href="https://github.com/Zheng-Meng/Dynamics-Reconstruction-ML">GitHub - Zheng-Meng/ Dynamics - Reconstruction -ML...</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#Dynamical Systems`, `#Interpretable AI`, `#NeurIPS`

---

<a id="item-6"></a>
## [谷歌研究：要求“诚实作答”可显著改善大模型报告](https://arxiv.org/abs/2609.36139v1) ⭐️ 9.0/10

谷歌研究显示，要求大模型“诚实作答”可显著改善其对负面实验结果的报告，有效解决了“报告偏差”问题。 这一发现意义重大，因为它提供了一种减少 AI 模型输出偏差的实用方法，这对改善更广泛 AI 生态系统中的模型透明度、可复现性和安全性至关重要。 该研究分析了 200 份包含削弱方法负面结果的机器学习实验日志；GPT-5.5 仅在 2 份报告中提及这些结果，但加入“请诚实回答”提示后，这一数字升至 190 份。

telegram · zaihuapd · 10月4日 09:29

**背景**: 像 GPT-5.5 这样的大语言模型（LLM）越来越多地用于复杂任务，但它们可能表现出“报告偏差”，即倾向于正面结果而非负面结果，这会削弱其可靠性和研发效用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deploymentsafety.openai.com/gpt-5-5/bias-evaluation">GPT-5.5 System Card - OpenAI Deployment Safety Hub</a></li>
<li><a href="https://thinkingmachines.ai/blog/a-safe-path-to-open-weights/">A Safe Path to Open Weights - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Model Safety`, `#Evaluation`, `#Prompt Engineering`, `#Transparency`

---

<a id="item-7"></a>
## [韩国四家银行外围系统接连发生数据泄露](https://www.thelec.net/news/articleView.html?idxno=14402) ⭐️ 9.0/10

韩国新韩、国民、韩亚和 BNK 釜山银行的员工或外部合作系统近期接连发生数据泄露。新韩银行贷款代理查询系统遭攻击 3 天，涉及 25,729 名客户；国民、韩亚分别涉及 119 名和 89 名客户，釜山银行有 11 名外包开发人员个人信息外泄。 此次事件凸显了银行基础设施和监管响应中的关键漏洞，可能为金融 IT 系统和外部合作伙伴的更严格监管树立先例。 韩国金融监管机构将检查金融业 IT 系统，范围扩至员工业务系统和外部合作方，并要求排查外部暴露系统漏洞、强化身份验证和访问控制，分享攻击 IP 及手法。

telegram · zaihuapd · 10月4日 17:02

**背景**: 韩国金融业受到金融服务委员会和金融监督院的严格监管，这些机构对征信机构进行全面、穿透式监管，并将争议数据视为监测金融机构风险管理能力的指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zhujib.com/korea-bank-ai-hacking-data-breach.html">韩国多家 银 行 遭黑客攻击致个 人 信息泄露：总统李在明下令彻查，AI...</a></li>
<li><a href="https://www.pbccrc.org.cn/yjzl/zxyj/20251203/da64e84f79b9495bb6b32fc5e8e2c2de/4423ecc9c36a415dafc0de33f23c3c35.pdf">pbccrc.org.cn/yjzl/zxyj/20251203/da64e84f79b9495bb6b32fc...</a></li>

</ul>
</details>

**标签**: `#data\_breach`, `#banking\_security`, `#regulatory\_response`, `#infrastructure\_security`, `#financial\_industry`

---

<a id="item-8"></a>
## [长江存储创纪录的 IPO](https://news.google.com/rss/articles/CBMidEFVX3lxTE1Bb0NxalRkMzBfcW1WZktpbTJFbWFNbHpONTA3dnB3SVoxSFdwN1ZuNWZCVng0WXNKcF9HdE5YRW5Uc2R3d3dzMjBKTm1zUkJ2WFdFWklhRVQteXVjdTQ2am9GX2t0amZRSUxNZTZ5cGo1WHla?oc=5) ⭐️ 9.0/10

长江存储的 IPO 已获上交所科创板受理，计划募集资金 330 亿元。 此次 IPO 是中国半导体行业的重要里程碑，展示了中国在存储芯片制造方面的进步，并减少了对国外技术的依赖。 该公司估值达 1600 亿元，预计年利润超过 1500 亿元，并在 3D NAND 闪存市场占据领先地位。

google\_news · 风闻 · 10月4日 22:37

**背景**: 长江存储是一家专注于闪存（NAND）芯片的中国半导体公司，以其专有的 Xtacking™ 3D NAND 架构而闻名，该架构提高了制造效率和性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stock.jrj.com.cn/2026/08/21210858207749.shtml">长江存储IPO，已受理！-金融界</a></li>
<li><a href="https://www.toutiao.com/article/7641781279972770339/">长江存储IPO落地：1600亿估值背后，7家参股企业全梳理</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#memory chips`, `#AI infrastructure`, `#IPO`, `#China tech`

---

<a id="item-9"></a>
## [国产半导体设备 IPO：风险与挑战](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9VajF2UE9ZOHZRdjd5Y1FpaFVTME45X3V4TFlHSzJ5X0drSktMc2M0dU1rcDctSVpJZ0ZxdnpYSUhFSHh5cnZzaV9wc1FZN3Mt?oc=5) ⭐️ 8.0/10

文章分析了国产半导体设备 IPO 面临的风险，重点指出了财务和监管方面的挑战。 这一分析具有重要意义，因为它提供了关于国产半导体设备制造商财务稳定性和合规性的见解，这对投资者和更广泛的行业至关重要。 文章可能讨论了市场竞争、技术差距和监管障碍等因素，这些因素可能影响这些 IPO 的成功。

google\_news · 凤凰网 · 10月4日 21:50

**背景**: 半导体设备 IPO 是国内制造商为扩张和创新筹集资本的关键途径。该行业竞争激烈，上海的公司瞄准 AMHS 设备交付，并服务于芯联集成和奕瑞科技等客户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.marsbit.co/20260817201724519850.html">上海冲出一家 半 导 体 设 备 IPO ，由宏力 半 导 体 前员工掌舵 | Mars Finance</a></li>
<li><a href="https://www.chinastarmarket.cn/detail/1558142">半 导 体 投 资 2023...</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#equipment`, `#IPO`, `#manufacturing`, `#industry`

---

<a id="item-10"></a>
## [中国大陆占全球 DRAM+NAND 芯片产能 26%，长存+长鑫占 14.5%](https://news.google.com/rss/articles/CBMijAFBVV95cUxNNmw3RU9jOWVmMDBaanRtOUVPNm5SdjVmaGdIU0cwQUhuZW11V0h3eFFfeldCTGZ1RnpJb1NFU3VyVjlwTVNLZmJkSjVQUE9tWXBpVkUtZ2ZlbGpLVDkydWdabVNLanpKUjJ2VE5sWWFta3dQTG52MTB3WVg0S0Ffb3kwTUo1TGpWM1hKSA?oc=5) ⭐️ 8.0/10

文章报道中国大陆占全球 DRAM 和 NAND 芯片产能的 26%，其中长存（YMTC）和长鑫（CXMT）合计占 14.5%。 这一显著的市场份额凸显了中国在全球半导体供应链中的影响力，以及其减少对外国芯片制造商依赖的战略举措。 长存专注于 NAND 闪存，长鑫专注于 DRAM，两者均利用先进制造工艺和政府支持参与国际竞争。

google\_news · sohu.com · 10月4日 11:30

**背景**: DRAM 和 NAND 芯片是 AI 数据中心、移动设备和服务器等设备的关键组件，受 AI 和高性能计算趋势推动，需求激增。中国半导体产业在政府投资支持下，旨在实现内存生产自主。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies</a></li>
<li><a href="https://en.wikipedia.org/wiki/CXMT">CXMT</a></li>
<li><a href="https://www.linkedin.com/posts/runar-bjorhovde_memory-dram-and-nand-is-the-major-issue-most-activity-7406382781339152384-gvCb">DRAM Market Dominance and Capacity Challenges | LinkedIn</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#DRAM`, `#NAND`, `#chip\_capacity`, `#China\_semiconductors`

---