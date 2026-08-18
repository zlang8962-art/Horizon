---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
content_date: 2026-08-17
lang: zh
---

> 报道范围：2026-08-17（Asia/Shanghai 自然日）

> 从 128 条内容中筛选出 10 条重要资讯。

---

1. [ggml-org/llama.cpp released b10455](#item-1) ⭐️ 10.0/10
2. [llama.cpp 发布 b10470 版本，包含 CI/CD 更新和 macOS 二进制文件](#item-2) ⭐️ 9.0/10
3. [GitHub Actions 工作流中的 AI 生成代码导致 Snowflake Jira 受损](#item-3) ⭐️ 9.0/10
4. [Simon Willison 更新 Markdown 转 SVG 渲染器工具](#item-4) ⭐️ 9.0/10
5. [Qwen 3.8 27B：性能出色但默认过度思考](#item-5) ⭐️ 9.0/10
6. [How to make any Sparse Attention / KV Compression look good? \[D\] \[R\]](#item-6) ⭐️ 9.0/10
7. [SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络](#item-7) ⭐️ 9.0/10
8. [Tibo 分享在 Codex 中启用百万 Token 上下文的方法](#item-8) ⭐️ 9.0/10
9. [超过 4 万亿！长鑫科技创历史新高 - 同花顺](#item-9) ⭐️ 9.0/10
10. [美团高管反思全员“养虾运动”的高昂成本](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10455](https://github.com/ggml-org/llama.cpp/releases/tag/b10455) ⭐️ 10.0/10

llama.cpp release b10455 adds SYCL support for AdamW and SGD optimization steps and provides pre-built binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · 8月17日 13:47

**标签**: `#llama.cpp`, `#AI`, `#SYCL`, `#cross-platform`, `#optimization`

---

<a id="item-2"></a>
## [llama.cpp 发布 b10470 版本，包含 CI/CD 更新和 macOS 二进制文件](https://github.com/ggml-org/llama.cpp/releases/tag/b10470) ⭐️ 9.0/10

llama.cpp 项目发布了 b10470 版本，包含更新的 CI/CD 工作流和适用于 Apple Silicon 和 Intel 的 macOS 二进制文件。 此次发布改进了发布流程的可靠性，并为在 macOS 上运行大语言模型提供了优化工具，从而惠及开发者和用户。 CI/CD 更新在创建发布之前显式推送发布标签，确保幂等性并减少对 Releases API 的依赖。macOS 二进制文件提供 arm64 和 x64 架构，而 Linux 和 Windows 构建支持多种后端，如 CUDA、Vulkan 和 SYCL。

github · github-actions\[bot\] · 8月17日 21:59

**背景**: llama.cpp 是一个在消费级硬件上运行大语言模型的高性能库。它支持多个平台和硬件加速，使其成为本地运行模型的流行选择。

**标签**: `#llama.cpp`, `#AI`, `#macOS`, `#release`, `#CI/CD`

---

<a id="item-3"></a>
## [GitHub Actions 工作流中的 AI 生成代码导致 Snowflake Jira 受损](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 9.0/10

GitHub Actions 工作流中的 AI 生成代码片段利用了模板注入漏洞，使攻击者能够入侵 Snowflake 的 Jira 集成。 这一事件凸显了 CI/CD 流水线中实施稳健安全实践的必要性，因为受损的工作流可能使攻击者直接访问敏感系统和凭据。 该漏洞是一种脚本注入攻击，GitHub Actions 工作流使用模板扩展机制执行任意代码，绕过了预期的安全控制。

hackernews · galnagli · 8月17日 22:18 · [社区讨论](https://news.ycombinator.com/item?id=49331423)

**背景**: GitHub Actions 是一个 CI/CD 平台，用于自动化软件开发任务。工作流在 YAML 文件中定义，可以执行代码，但配置不当可能导致脚本注入等安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sysdig.com/blog/how-threat-actors-are-using-self-hosted-github-actions-runners-as-backdoors">How threat actors are using self-hosted GitHub Actions runners as backdoors | Sysdig</a></li>
<li><a href="https://docs.github.com/en/actions/concepts/security/script-injections">Script injections - GitHub Docs</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调了使用静态分析工具（如 zizmor）检测此类漏洞的重要性，并讨论了 AI 如何降低引入更改的成本，而审查这些更改的成本却保持高位。

**标签**: `#GitHub Actions`, `#Security Vulnerability`, `#CI/CD`, `#Static Analysis`, `#AI Safety`

---

<a id="item-4"></a>
## [Simon Willison 更新 Markdown 转 SVG 渲染器工具](https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/) ⭐️ 9.0/10

Simon Willison 增强了他的开源 markdown-svg-renderer 工具，新增了 PNG、JPEG 和 MP4 导出的标签页界面，以及使用浏览器中的 ffmpeg.wasm 将动画 SVG 转换为 MP4 视频的功能。 该工具简化了在 Markdown 文档中分享复杂矢量图形和动画的过程，使得在可能不支持 SVG 原生显示的基于文本的平台上嵌入丰富的视觉效果变得更加容易。 用户可以直接粘贴 Markdown，通过 CORS 友好的 URL 或 GitHub Gist 加载内容，工具会将 SVG 渲染为带有 PNG、JPEG、MP4 和原始代码标签页的视图，并利用 ffmpeg.wasm 进行视频转换。

rss · Simon Willison · 8月17日 07:59

**背景**: Markdown 是一种轻量级标记语言，用于使用标题、列表和链接等格式化文本，而 SVG（可缩放矢量图形）是一种矢量图像格式，可以在不失真的情况下缩放。CORS（跨域资源共享）允许网页在特定条件下访问来自不同域的资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tools.simonwillison.net/markdown-svg-renderer">tools.simonwillison.net/ markdown - svg - renderer</a></li>
<li><a href="https://github.com/simonw/tools/blob/main/markdown-svg-renderer.html">tools/ markdown - svg - renderer .html at main · simonw/tools · GitHub</a></li>
<li><a href="https://devblogs.co/posts/markdown-svg-renderer">markdown - svg - renderer</a></li>

</ul>
</details>

**标签**: `#Markdown`, `#SVG`, `#Developer Tools`, `#Open Source`, `#Web Development`

---

<a id="item-5"></a>
## [Qwen 3.8 27B：性能出色但默认过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 9.0/10

阿里巴巴的 Qwen 研究实验室发布了 Qwen 3.8 27B，这是一个 Apache 2 许可的视觉能力大语言模型，其自我报告的基准测试显示性能优于 Qwen 3.6 27B 和 Qwen 3.7-Plus。 该模型对本地 AI 爱好者具有重要意义，因为它在消费级硬件上提供强大性能，同时保持开源许可，可能使高级多模态 AI 能力民主化。 该模型默认为 &\#x27;xhigh&\#x27; 推理强度，导致其消耗过多令牌并花费 21 分钟生成简单的 SVG，尽管在增加上下文长度后正确配置时能产生高质量结果。

rss · Simon Willison · 8月17日 06:00

**背景**: Qwen 3.7-Plus 是 Qwen 系列中的强力闭源模型，此次新发布旨在在其文本骨干基础上升级视觉语言能力。Apache 2 许可证允许商业使用同时保持透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qwencloud.com/models/qwen3.7-plus">Qwen3.7-Plus - QwenCloud</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.7-plus">Qwen3.7-Plus: Multimodal Agent Intelligence</a></li>
<li><a href="https://wavespeed.ai/blog/ai-models/qwen-3-7-plus-model-review/">Qwen 3.7 Plus Review: Context, Multimodality, and Agents</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Qwen`, `#AI`, `#LocalAI`, `#Benchmarking`

---

<a id="item-6"></a>
## [How to make any Sparse Attention / KV Compression look good? \[D\] \[R\]](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 9.0/10

This post discusses techniques to improve the evaluation of sparse attention and KV compression in AI models, emphasizing practical methods to avoid misleading results.

reddit · r/MachineLearning · /u/korec1234 · 8月17日 20:18

**标签**: `#sparse-attention`, `#kv-compression`, `#machine-learning`, `#model-evaluation`, `#efficient-attention`

---

<a id="item-7"></a>
## [SineKAN：使用正弦激活函数的 Kolmogorov-Arnold 网络](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 9.0/10

一种新的 SineKAN 架构被引入，在 Kolmogorov-Arnold 网络中用正弦激活函数替代了 B 样条，并附有 arXiv 论文和开源 GitHub 仓库。 这一创新为神经网络架构提供了新的思路，可能有助于提高模型的表达能力和效率，为深度学习中替代激活函数的探索做出了贡献。 SineKAN 的实现可在 GitHub 上获取，且在 MDPI 上有一篇同行评审的出版物，表明该工作已得到研究社区的评审。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 08:46

**背景**: Kolmogorov-Arnold 网络 \(KAN\) 是一种使用 B 样条作为激活函数的神经网络。SineKAN 变体用正弦函数替代了这些函数，正弦函数是周期性的，可能为函数逼近提供不同的特性。

**标签**: `#Kolmogorov-Arnold Networks`, `#SineKAN`, `#Neural Networks`, `#Activation Functions`, `#Open Source`

---

<a id="item-8"></a>
## [Tibo 分享在 Codex 中启用百万 Token 上下文的方法](https://x.com/thsottiaux/status/2089082893804896524) ⭐️ 9.0/10

Tibo \(@thsottiaux\) 分享了一种在 Codex 客户端中启用百万 Token 上下文窗口的配置方法，即在 ~/.codex/config.toml 文件中设置 model\_context\_window=1000000 和 model\_auto\_compact\_token\_limit=900000。 扩大上下文窗口允许开发人员处理和分析更大的代码库和文档，这对复杂的软件工程任务和提高 AI 辅助编码工作流的效率至关重要。 配置更改需要保存文件并重启 Codex 客户端，并且也可以通过命令行参数将相同的设置应用于单个 CLI 会话。

telegram · zaihuapd · 8月17日 08:47

**背景**: Codex CLI 是由 OpenAI 开发的本地编码代理，可与 VS Code 和 Cursor 等各种代码编辑器集成。上下文窗口决定了可以一次处理多少对话历史和代码，而 model\_auto\_compact\_token\_limit 等设置则控制自动历史压缩以管理内存使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in ...</a></li>
<li><a href="https://learn.chatgpt.com/docs/config-file/config-advanced">Advanced Configuration | ChatGPT Learn</a></li>
<li><a href="https://kapadiya.net/blog/codex-auto-compact-token-savings/">Reduce Codex Token Usage with Auto-Compaction Settings</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Context Window`, `#Codex`, `#Configuration`

---

<a id="item-9"></a>
## [超过 4 万亿！长鑫科技创历史新高 - 同花顺](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1Sdm90YjFlY285TGpBdXJHWVBYdi04LTl3ZzMyWkNIZ3VTUUNxSUZqQnRWeGFGakpYNUl5RnRfMGFialoxQTJyellqRlJyRkVPXy1WOUxIS0ZuU3dUemU2Y3dR?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies \(CXMT\) achieves a record high market capitalization of over 4 trillion RMB.

google\_news · 同花顺 · 8月17日 13:25

**标签**: `#semiconductors`, `#memory`, `#chip manufacturing`, `#market cap`, `#CXMT`

---

<a id="item-10"></a>
## [美团高管反思全员“养虾运动”的高昂成本](https://weibo.com/1642634100/RdM6hhhpW) ⭐️ 8.0/10

美团核心本地商业 CEO 王莆中公开反思了全员“养虾运动”，指出今年 2 至 3 月期间该活动导致每日 Token 消耗超过 1000 万，账单暴涨并干扰了真实经营。 这一案例凸显了大规模内部 AI 部署所伴随的巨大资源消耗和运营风险，为企业在日常业务工作流中整合生成式 AI 的挑战提供了警示。 王莆中指出了阻碍 AI 采用的四大错配——认知、效率、场景和考核，并宣布从 4 月起各事业部成立 AI 组织，将 AI 转型明确为涉及业务、组织和技术的系统工程。

telegram · zaihuapd · 8月17日 10:09

**标签**: `#AI`, `#Enterprise`, `#Meituan`, `#Generative AI`, `#Productivity`

---