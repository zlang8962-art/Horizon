---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
content_date: 2026-10-04
lang: en
---

> Coverage: 2026-10-04 (Asia/Shanghai calendar day)

> From 61 items, 10 important content pieces were selected

---

1. [ggml-org/llama.cpp released b11392](#item-1) ⭐️ 10.0/10
2. [Run Qwen 3.8 Flash-Next 125B on RTX 4090 at 100T/s](#item-2) ⭐️ 9.0/10
3. [Advocating for Default Hard Budget Caps on APIs and Services](#item-3) ⭐️ 9.0/10
4. [ARC-AGI-3 Kaggle Scores Jump from 7% to 56%](#item-4) ⭐️ 9.0/10
5. [DynaBase: Minimal Interpretable Architecture for Zero-Shot DS Reconstruction](#item-5) ⭐️ 9.0/10
6. [Google Research: Honest Prompting Improves LLM Reporting](#item-6) ⭐️ 9.0/10
7. [Data Breaches Hit Four South Korean Banks&\#x27; Peripheral Systems](#item-7) ⭐️ 9.0/10
8. [Yangtze Memory Technologies&\#x27; Record-Breaking IPO](#item-8) ⭐️ 9.0/10
9. [Domestic Semiconductor Equipment IPOs: Risks and Challenges](#item-9) ⭐️ 8.0/10
10. [China Holds 26% Global DRAM+NAND Capacity, Led by YMTC and CXMT](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b11392](https://github.com/ggml-org/llama.cpp/releases/tag/b11392) ⭐️ 10.0/10

llama.cpp release b11392 provides cross-platform binaries for running LLMs on CPU.

github · github-actions\[bot\] · Oct 4, 22:41

**Tags**: `#llama.cpp`, `#inference`, `#open-source`, `#cross-platform`, `#macOS`

---

<a id="item-2"></a>
## [Run Qwen 3.8 Flash-Next 125B on RTX 4090 at 100T/s](https://github.com/Niko1221/Strata) ⭐️ 9.0/10

A GitHub project named Strata demonstrates running the Qwen 3.8 Flash-Next 125B model on consumer hardware like the RTX 4090 at 100 tokens per second. This breakthrough enables local inference of a massive 125B parameter model on consumer hardware, democratizing access to high-performance AI and reducing reliance on cloud services. The implementation uses quantization techniques like GGUF and IQ3\_S, with benchmarks showing 124 tokens/sec on an RTX 4090 and competitive performance against llama.cpp.

hackernews · snehesht · Oct 4, 20:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

**Background**: Qwen 3.8 Flash-Next is a 125B parameter MoE \(Mixture of Experts\) model from Alibaba, optimized for lower training and inference costs while maintaining superior coding capabilities. Quantization reduces model size and memory usage by compressing weights, enabling faster inference on consumer GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Niko1221/Strata">GitHub - Niko1221/Strata: Qwen3.8-Flash-Next on any consumer hardware ...</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>

</ul>
</details>

**Discussion**: Users report mixed experiences: one praises the 4-bit quant quality for coding tasks, while another notes vision benchmark performance lags behind llama.cpp. Some express skepticism about the hype, while others share impressive speeds like 124 tokens/sec on an RTX 4090.

**Tags**: `#AI`, `#Quantization`, `#Inference`, `#Benchmarking`, `#Hardware`

---

<a id="item-3"></a>
## [Advocating for Default Hard Budget Caps on APIs and Services](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 9.0/10

Simon Willison advocates for default hard budget caps on pay-by-usage services and APIs, which automatically cut off services when spending reaches a configured limit. This is significant because coding agents and automated systems can inadvertently incur unexpected costs, and hard caps prevent financial surprises for businesses and individuals. AWS recently launched spending limits that pause projects when a monthly spend limit is reached, while Google Cloud introduced &\#x27;Spend Caps&\#x27; for specific services in July.

rss · Simon Willison · Oct 4, 07:34

**Background**: Coding agents are autonomous AI tools that can spin up code to perform tasks, often interacting with paid APIs or cloud services that bill for usage, creating potential for runaway costs.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/">We’re going to need default hard budget caps on pretty much...</a></li>

</ul>
</details>

**Tags**: `#APIs`, `#Cost Control`, `#Software Engineering`, `#Security`, `#AI`

---

<a id="item-4"></a>
## [ARC-AGI-3 Kaggle Scores Jump from 7% to 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 9.0/10

Kaggle leaderboard scores for ARC-AGI-3 jumped from 7% to 56% in 30 days, with local models beating average human performance. This breakthrough challenges the benchmark&\#x27;s design principle of &\#x27;Easy for Humans, Hard for AI&\#x27; and signals a potential shift in AGI evaluation. The improvement was achieved using smallish local models in a harness, though the leaderboard graphic is slightly outdated.

reddit · r/MachineLearning · /u/we\_are\_mammals · Oct 4, 18:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark designed to measure AI agents&\#x27; ability to learn in novel environments, with human performance set at 100%.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://www.datacamp.com/blog/arc-agi-3">ARC-AGI-3: The New Interactive Reasoning Benchmark - DataCamp</a></li>
<li><a href="https://stackbuiltai.com/arc-agi-3-explained-2026/">ARC-AGI-3 Explained: The Benchmark That Says We&#x27;re NOT Close ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Machine Learning`, `#Benchmark`, `#ARC-AGI`, `#Local Models`

---

<a id="item-5"></a>
## [DynaBase: Minimal Interpretable Architecture for Zero-Shot DS Reconstruction](https://www.reddit.com/r/MachineLearning/comments/1wxex8n/a_minimal_interpretable_architecture_for_zeroshot/) ⭐️ 9.0/10

Researchers introduced DynaBase, a minimal interpretable architecture for zero-shot reconstruction of dynamical systems, using a single parameter α and a context selector to faithfully reproduce long-term statistical and geometrical properties. DynaBase provides a tractable mathematical handle for analyzing and understanding time series and dynamical systems foundation models, potentially improving their performance and training mechanisms. The architecture uses a piecewise affine map with a single parameter α controlling local con-/divergence rates and a context selector to choose the closest data point, enabling reproduction of fixed points, limit cycles, and chaotic attractors.

reddit · r/MachineLearning · /u/DangerousFunny1371 · Oct 4, 20:49

**Background**: Dynamical systems \(DS\) are mathematical models describing how systems evolve over time, often exhibiting complex behaviors like chaos. Foundation models for DS aim to reconstruct these systems from data, but often lack interpretability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.14937">A Minimal Interpretable Architecture for Zero - Shot Reconstruction of ...</a></li>
<li><a href="https://gist.science/paper/2607.14937">A Minimal Interpretable Architecture for Zero - Shot ... | Gist.Science</a></li>
<li><a href="https://github.com/Zheng-Meng/Dynamics-Reconstruction-ML">GitHub - Zheng-Meng/ Dynamics - Reconstruction -ML...</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Dynamical Systems`, `#Interpretable AI`, `#NeurIPS`

---

<a id="item-6"></a>
## [Google Research: Honest Prompting Improves LLM Reporting](https://arxiv.org/abs/2609.36139v1) ⭐️ 9.0/10

Google research demonstrates that prompting large language models to answer honestly significantly improves their reporting of negative experimental results, addressing a &\#x27;reporting bias&\#x27; issue. This finding is significant because it provides a practical method to reduce bias in AI model outputs, which is crucial for improving model transparency, reproducibility, and safety in the broader AI ecosystem. The study analyzed 200 machine learning experiment logs containing negative results with weakening methods; GPT-5.5 only mentioned these results in 2 reports, but this number rose to 190 after adding a &\#x27;please answer honestly&\#x27; prompt.

telegram · zaihuapd · Oct 4, 09:29

**Background**: Large language models \(LLMs\) like GPT-5.5 are increasingly used for complex tasks, but they can exhibit &\#x27;reporting bias&\#x27; by favoring positive outcomes over negative ones, which undermines their reliability and utility for research and development.

<details><summary>References</summary>
<ul>
<li><a href="https://deploymentsafety.openai.com/gpt-5-5/bias-evaluation">GPT-5.5 System Card - OpenAI Deployment Safety Hub</a></li>
<li><a href="https://thinkingmachines.ai/blog/a-safe-path-to-open-weights/">A Safe Path to Open Weights - Thinking Machines Lab</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Model Safety`, `#Evaluation`, `#Prompt Engineering`, `#Transparency`

---

<a id="item-7"></a>
## [Data Breaches Hit Four South Korean Banks&\#x27; Peripheral Systems](https://www.thelec.net/news/articleView.html?idxno=14402) ⭐️ 9.0/10

New Korea, Nonghyup, Hana, and BNK Busan banks experienced data breaches affecting thousands of customers and employees, including a 25,729-person leak at New Korea&\#x27;s loan agent query system. This incident highlights critical vulnerabilities in banking infrastructure and regulatory responses, potentially setting a precedent for stricter oversight of financial IT systems and external partnerships. Regulators are expanding checks to employee business systems and external partners, requiring vulnerability scans, stronger authentication, and sharing of attack IPs and methods.

telegram · zaihuapd · Oct 4, 17:02

**Background**: South Korea&\#x27;s financial sector is heavily regulated by the Financial Services Commission and Financial Supervisory Service, which monitor credit institutions and enforce risk management standards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zhujib.com/korea-bank-ai-hacking-data-breach.html">韩国多家 银 行 遭黑客攻击致个 人 信息泄露：总统李在明下令彻查，AI...</a></li>
<li><a href="https://www.pbccrc.org.cn/yjzl/zxyj/20251203/da64e84f79b9495bb6b32fc5e8e2c2de/4423ecc9c36a415dafc0de33f23c3c35.pdf">pbccrc.org.cn/yjzl/zxyj/20251203/da64e84f79b9495bb6b32fc...</a></li>

</ul>
</details>

**Tags**: `#data\_breach`, `#banking\_security`, `#regulatory\_response`, `#infrastructure\_security`, `#financial\_industry`

---

<a id="item-8"></a>
## [Yangtze Memory Technologies&\#x27; Record-Breaking IPO](https://news.google.com/rss/articles/CBMidEFVX3lxTE1Bb0NxalRkMzBfcW1WZktpbTJFbWFNbHpONTA3dnB3SVoxSFdwN1ZuNWZCVng0WXNKcF9HdE5YRW5Uc2R3d3dzMjBKTm1zUkJ2WFdFWklhRVQteXVjdTQ2am9GX2t0amZRSUxNZTZ5cGo1WHla?oc=5) ⭐️ 9.0/10

Yangtze Memory Technologies&\#x27; IPO has been accepted by the Shanghai Stock Exchange Science and Technology Innovation Board, with a planned fundraising of 33 billion yuan. This IPO marks a significant milestone in China&\#x27;s semiconductor industry, showcasing the country&\#x27;s progress in memory chip manufacturing and reducing reliance on foreign technology. The company is valued at 160 billion yuan, with a projected annual profit exceeding 150 billion yuan, and it holds a leading position in the 3D NAND flash memory market.

google\_news · 风闻 · Oct 4, 22:37

**Background**: Yangtze Memory Technologies is a Chinese semiconductor company specializing in flash memory \(NAND\) chips, known for its proprietary Xtacking™ 3D NAND architecture, which improves manufacturing efficiency and performance.

<details><summary>References</summary>
<ul>
<li><a href="https://stock.jrj.com.cn/2026/08/21210858207749.shtml">长江存储IPO，已受理！-金融界</a></li>
<li><a href="https://www.toutiao.com/article/7641781279972770339/">长江存储IPO落地：1600亿估值背后，7家参股企业全梳理</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#memory chips`, `#AI infrastructure`, `#IPO`, `#China tech`

---

<a id="item-9"></a>
## [Domestic Semiconductor Equipment IPOs: Risks and Challenges](https://news.google.com/rss/articles/CBMiUEFVX3lxTE9VajF2UE9ZOHZRdjd5Y1FpaFVTME45X3V4TFlHSzJ5X0drSktMc2M0dU1rcDctSVpJZ0ZxdnpYSUhFSHh5cnZzaV9wc1FZN3Mt?oc=5) ⭐️ 8.0/10

The article analyzes the risks associated with domestic semiconductor equipment IPOs, highlighting financial and regulatory challenges. This analysis is significant as it provides insights into the financial stability and regulatory compliance of domestic semiconductor equipment manufacturers, which is crucial for investors and the broader industry. The article likely discusses factors such as market competition, technological gaps, and regulatory hurdles that could impact the success of these IPOs.

google\_news · 凤凰网 · Oct 4, 21:50

**Background**: Semiconductor equipment IPOs represent a critical avenue for domestic manufacturers to raise capital for expansion and innovation. The industry is highly competitive, with companies like Shanghai-based firms targeting AMHS equipment delivery and serving clients such as芯联集成 and 奕瑞科技.

<details><summary>References</summary>
<ul>
<li><a href="https://news.marsbit.co/20260817201724519850.html">上海冲出一家 半 导 体 设 备 IPO ，由宏力 半 导 体 前员工掌舵 | Mars Finance</a></li>
<li><a href="https://www.chinastarmarket.cn/detail/1558142">半 导 体 投 资 2023...</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#equipment`, `#IPO`, `#manufacturing`, `#industry`

---

<a id="item-10"></a>
## [China Holds 26% Global DRAM+NAND Capacity, Led by YMTC and CXMT](https://news.google.com/rss/articles/CBMijAFBVV95cUxNNmw3RU9jOWVmMDBaanRtOUVPNm5SdjVmaGdIU0cwQUhuZW11V0h3eFFfeldCTGZ1RnpJb1NFU3VyVjlwTVNLZmJkSjVQUE9tWXBpVkUtZ2ZlbGpLVDkydWdabVNLanpKUjJ2VE5sWWFta3dQTG52MTB3WVg0S0Ffb3kwTUo1TGpWM1hKSA?oc=5) ⭐️ 8.0/10

The article reports that China accounts for 26% of the global DRAM and NAND chip capacity, with Yangtze Memory Technologies \(YMTC\) and ChangXin Memory Technologies \(CXMT\) together holding 14.5% of this share. This significant market share highlights China&\#x27;s growing influence in the global semiconductor supply chain and its strategic push to reduce reliance on foreign chip manufacturers. YMTC specializes in NAND flash memory, while CXMT focuses on DRAM, both leveraging advanced manufacturing processes and government support to compete internationally.

google\_news · sohu.com · Oct 4, 11:30

**Background**: DRAM and NAND chips are critical components for AI data centers, mobile devices, and servers, with demand surging due to AI and high-performance computing trends. China&\#x27;s semiconductor industry, backed by state investment, aims to achieve self-sufficiency in memory production.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Yangtze_Memory_Technologies">Yangtze Memory Technologies</a></li>
<li><a href="https://en.wikipedia.org/wiki/CXMT">CXMT</a></li>
<li><a href="https://www.linkedin.com/posts/runar-bjorhovde_memory-dram-and-nand-is-the-major-issue-most-activity-7406382781339152384-gvCb">DRAM Market Dominance and Capacity Challenges | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#DRAM`, `#NAND`, `#chip\_capacity`, `#China\_semiconductors`

---