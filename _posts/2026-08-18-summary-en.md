---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
content_date: 2026-08-17
lang: en
---

> Coverage: 2026-08-17 (Asia/Shanghai calendar day)

> From 128 items, 10 important content pieces were selected

---

1. [ggml-org/llama.cpp released b10455](#item-1) ⭐️ 10.0/10
2. [llama.cpp b10470 release with CI/CD and macOS binaries](#item-2) ⭐️ 9.0/10
3. [AI-Generated Code in GitHub Actions Workflow Led to Snowflake Jira Compromise](#item-3) ⭐️ 9.0/10
4. [Simon Willison Updates Markdown-to-SVG Renderer Tool](#item-4) ⭐️ 9.0/10
5. [Qwen 3.8 27B: Impressive Performance but Overthinking Default](#item-5) ⭐️ 9.0/10
6. [How to make any Sparse Attention / KV Compression look good? \[D\] \[R\]](#item-6) ⭐️ 9.0/10
7. [SineKAN: Kolmogorov-Arnold Networks with Sinusoidal Activation Functions](#item-7) ⭐️ 9.0/10
8. [Tibo Shares Method to Enable 1M Token Context in Codex](#item-8) ⭐️ 9.0/10
9. [超过4万亿！长鑫科技创历史新高 - 同花顺](#item-9) ⭐️ 9.0/10
10. [Meituan Exec Reflects on High Costs of Internal AI Initiative](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ggml-org/llama.cpp released b10455](https://github.com/ggml-org/llama.cpp/releases/tag/b10455) ⭐️ 10.0/10

llama.cpp release b10455 adds SYCL support for AdamW and SGD optimization steps and provides pre-built binaries for macOS, iOS, and Linux.

github · github-actions\[bot\] · Aug 17, 13:47

**Tags**: `#llama.cpp`, `#AI`, `#SYCL`, `#cross-platform`, `#optimization`

---

<a id="item-2"></a>
## [llama.cpp b10470 release with CI/CD and macOS binaries](https://github.com/ggml-org/llama.cpp/releases/tag/b10470) ⭐️ 9.0/10

The llama.cpp project released version b10470, featuring updated CI/CD workflows and macOS binaries for Apple Silicon and Intel. This release improves the reliability of the release process and provides optimized tools for running large language models on macOS, benefiting developers and users. The CI/CD update explicitly pushes release tags before creating releases, ensuring idempotency and reducing reliance on the Releases API. macOS binaries are available for arm64 and x64 architectures, while Linux and Windows builds support various backends like CUDA, Vulkan, and SYCL.

github · github-actions\[bot\] · Aug 17, 21:59

**Background**: llama.cpp is a high-performance library for running large language models \(LLMs\) on consumer hardware. It supports multiple platforms and hardware accelerations, making it a popular choice for running models locally.

**Tags**: `#llama.cpp`, `#AI`, `#macOS`, `#release`, `#CI/CD`

---

<a id="item-3"></a>
## [AI-Generated Code in GitHub Actions Workflow Led to Snowflake Jira Compromise](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 9.0/10

An AI-generated code snippet in a GitHub Actions workflow exploited a template injection vulnerability, allowing attackers to compromise Snowflake&\#x27;s Jira integration. This incident highlights the critical need for robust security practices in CI/CD pipelines, as compromised workflows can provide attackers with direct access to sensitive systems and credentials. The vulnerability was a script injection attack where a GitHub Actions workflow used a template expansion mechanism to execute arbitrary code, bypassing intended security controls.

hackernews · galnagli · Aug 17, 22:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**Background**: GitHub Actions is a CI/CD platform that automates software development tasks. Workflows are defined in YAML files and can execute code, but improper configuration can lead to security vulnerabilities like script injection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sysdig.com/blog/how-threat-actors-are-using-self-hosted-github-actions-runners-as-backdoors">How threat actors are using self-hosted GitHub Actions runners as backdoors | Sysdig</a></li>
<li><a href="https://docs.github.com/en/actions/concepts/security/script-injections">Script injections - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: Community members emphasized the importance of using static analysis tools like zizmor to detect such vulnerabilities and discussed how AI lowers the cost of introducing changes while the cost of reviewing them remains high.

**Tags**: `#GitHub Actions`, `#Security Vulnerability`, `#CI/CD`, `#Static Analysis`, `#AI Safety`

---

<a id="item-4"></a>
## [Simon Willison Updates Markdown-to-SVG Renderer Tool](https://simonwillison.net/2026/Aug/16/markdown-svg-upgrades/) ⭐️ 9.0/10

Simon Willison has enhanced his open-source markdown-svg-renderer tool with new features including a tabbed interface for PNG, JPEG, and MP4 exports, plus the ability to convert animated SVGs into MP4 videos using ffmpeg.wasm in the browser. This tool simplifies sharing complex vector graphics and animations in Markdown documents, making it easier to embed rich visuals in text-based platforms that may not support SVG natively. Users can paste Markdown directly, load content via a CORS-friendly URL or GitHub Gist, and the tool renders SVGs with tabs for PNG, JPEG, MP4, and raw code, leveraging ffmpeg.wasm for video conversion.

rss · Simon Willison · Aug 17, 07:59

**Background**: Markdown is a lightweight markup language used to format text with headers, lists, and links, while SVG \(Scalable Vector Graphics\) is a vector image format that scales without quality loss. CORS \(Cross-Origin Resource Sharing\) allows web pages to access resources from different domains under certain conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://tools.simonwillison.net/markdown-svg-renderer">tools.simonwillison.net/ markdown - svg - renderer</a></li>
<li><a href="https://github.com/simonw/tools/blob/main/markdown-svg-renderer.html">tools/ markdown - svg - renderer .html at main · simonw/tools · GitHub</a></li>
<li><a href="https://devblogs.co/posts/markdown-svg-renderer">markdown - svg - renderer</a></li>

</ul>
</details>

**Tags**: `#Markdown`, `#SVG`, `#Developer Tools`, `#Open Source`, `#Web Development`

---

<a id="item-5"></a>
## [Qwen 3.8 27B: Impressive Performance but Overthinking Default](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 9.0/10

Alibaba&\#x27;s Qwen research lab released Qwen 3.8 27B, an Apache 2 licensed vision-capable LLM with self-reported benchmarks showing improvements over Qwen 3.6 27B and Qwen 3.7-Plus. This model is significant for local AI enthusiasts as it offers strong performance on consumer hardware while maintaining an open license, potentially democratizing access to advanced multimodal AI capabilities. The model defaults to &\#x27;xhigh&\#x27; reasoning effort, causing it to consume excessive tokens and take 21 minutes to generate a simple SVG, though it produces high-quality results when properly configured with increased context length.

rss · Simon Willison · Aug 17, 06:00

**Background**: Qwen 3.7-Plus was a strong closed-weight model from Qwen&\#x27;s lineup, and this new release aims to build on its text backbone while upgrading vision-language capabilities. Apache 2 licensing allows commercial use while maintaining transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.qwencloud.com/models/qwen3.7-plus">Qwen3.7-Plus - QwenCloud</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.7-plus">Qwen3.7-Plus: Multimodal Agent Intelligence</a></li>
<li><a href="https://wavespeed.ai/blog/ai-models/qwen-3-7-plus-model-review/">Qwen 3.7 Plus Review: Context, Multimodality, and Agents</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Qwen`, `#AI`, `#LocalAI`, `#Benchmarking`

---

<a id="item-6"></a>
## [How to make any Sparse Attention / KV Compression look good? \[D\] \[R\]](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 9.0/10

This post discusses techniques to improve the evaluation of sparse attention and KV compression in AI models, emphasizing practical methods to avoid misleading results.

reddit · r/MachineLearning · /u/korec1234 · Aug 17, 20:18

**Tags**: `#sparse-attention`, `#kv-compression`, `#machine-learning`, `#model-evaluation`, `#efficient-attention`

---

<a id="item-7"></a>
## [SineKAN: Kolmogorov-Arnold Networks with Sinusoidal Activation Functions](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 9.0/10

A new SineKAN architecture has been introduced, replacing B-splines with sinusoidal activation functions in Kolmogorov-Arnold Networks, accompanied by an arXiv paper and an open-source GitHub repository. This innovation offers a novel approach to neural network architecture that could potentially improve model expressiveness and efficiency, contributing to the ongoing exploration of alternative activation functions in deep learning. The SineKAN implementation is available on GitHub, and there is also a peer-reviewed publication on MDPI, indicating that the work has been reviewed by the research community.

reddit · r/MachineLearning · /u/jacobgorm · Aug 17, 08:46

**Background**: Kolmogorov-Arnold Networks \(KANs\) are a type of neural network that use B-splines as activation functions. The SineKAN variant replaces these with sinusoidal functions, which are periodic and could offer different properties for function approximation.

**Tags**: `#Kolmogorov-Arnold Networks`, `#SineKAN`, `#Neural Networks`, `#Activation Functions`, `#Open Source`

---

<a id="item-8"></a>
## [Tibo Shares Method to Enable 1M Token Context in Codex](https://x.com/thsottiaux/status/2089082893804896524) ⭐️ 9.0/10

Tibo \(@thsottiaux\) shared a configuration method to enable a 1 million token context window in the Codex client by setting model\_context\_window=1000000 and model\_auto\_compact\_token\_limit=900000 in the ~/.codex/config.toml file. Expanding the context window allows developers to process and analyze significantly larger codebases and documentation, which is crucial for complex software engineering tasks and improving the efficiency of AI-assisted coding workflows. The configuration changes require saving the file and restarting the Codex client, and the same settings can also be applied to a single CLI session via command-line arguments.

telegram · zaihuapd · Aug 17, 08:47

**Background**: Codex CLI is a local coding agent developed by OpenAI that integrates with various code editors like VS Code and Cursor. The context window determines how much conversation history and code can be processed at once, and settings like model\_auto\_compact\_token\_limit control automatic history compaction to manage memory usage.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in ...</a></li>
<li><a href="https://learn.chatgpt.com/docs/config-file/config-advanced">Advanced Configuration | ChatGPT Learn</a></li>
<li><a href="https://kapadiya.net/blog/codex-auto-compact-token-savings/">Reduce Codex Token Usage with Auto-Compaction Settings</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Context Window`, `#Codex`, `#Configuration`

---

<a id="item-9"></a>
## [超过4万亿！长鑫科技创历史新高 - 同花顺](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1Sdm90YjFlY285TGpBdXJHWVBYdi04LTl3ZzMyWkNIZ3VTUUNxSUZqQnRWeGFGakpYNUl5RnRfMGFialoxQTJyellqRlJyRkVPXy1WOUxIS0ZuU3dUemU2Y3dR?oc=5) ⭐️ 9.0/10

ChangXin Memory Technologies \(CXMT\) achieves a record high market capitalization of over 4 trillion RMB.

google\_news · 同花顺 · Aug 17, 13:25

**Tags**: `#semiconductors`, `#memory`, `#chip manufacturing`, `#market cap`, `#CXMT`

---

<a id="item-10"></a>
## [Meituan Exec Reflects on High Costs of Internal AI Initiative](https://weibo.com/1642634100/RdM6hhhpW) ⭐️ 8.0/10

Meituan&\#x27;s core local commerce CEO Wang Puzhong publicly reflected on the company-wide AI initiative, noting that the &\#x27;shrimp farming&\#x27; campaign from February to March caused daily token consumption to exceed 10 million, leading to inflated bills and operational disruptions. This case highlights the significant resource consumption and operational risks associated with large-scale internal AI deployments in enterprises, offering a cautionary tale about the challenges of integrating generative AI into daily business workflows. Wang Puzhong identified four key mismatches—cognition, efficiency, scenario, and assessment—that hinder AI adoption, and announced that starting in April, business units established AI organizations to formalize the transition as a systematic project involving business, organization, and technology.

telegram · zaihuapd · Aug 17, 10:09

**Tags**: `#AI`, `#Enterprise`, `#Meituan`, `#Generative AI`, `#Productivity`

---