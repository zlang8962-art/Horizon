---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 31 条内容中筛选出 1 条重要资讯。

---

1. [Claude 共享链接遭搜索引擎索引，大量用户隐私外泄](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude 共享链接遭搜索引擎索引，大量用户隐私外泄](https://search.brave.com/search?q=site%3Aclaude.ai%2Fshare&amp;amp;source=android) ⭐️ 8.0/10

Claude 的共享对话链接因缺少 noindex 标签，被 Google、Bing 和 Brave 等搜索引擎索引，导致 API 密钥、财务记录和个人信息等敏感用户数据外泄。Anthropic 已开始移除被索引的内容，但在修复前已有数百条对话可被公开搜索到。 这一漏洞严重影响了分享敏感对话的用户，涉及企业数据、法律咨询和社会安全号码等个人身份信息。该事件凸显了 AI 产品设计中持续存在的安全挑战，以及对用户生成内容实施适当搜索引擎索引控制的重要性。 共享链接缺少 robots.txt 的 noindex 标签，导致搜索引擎爬虫可以索引这些内容。根据 Obsidian Security 的研究，超过 14.3 万条 Claude 对话被 Archive.org 存档，泄露的数据包括 AWS 令牌、风投备忘录、薪资信息和加密货币钱包详情。Google 已屏蔽被索引的内容，但 Brave 和 Bing 仍在继续索引这些链接。

telegram · zaihuapd · 7月26日 11:16

**背景**: 搜索引擎使用 robots.txt 文件和 noindex 等元标签来决定哪些页面应该被抓取和索引。当网站未能正确实施这些控制时，敏感内容可能通过搜索查询被公开发现。大约一年前，ChatGPT 也出现了类似问题，共享对话链接在被快速修复前同样被搜索引擎索引。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://startupfortune.com/claude-shared-chats-have-been-indexed-by-google-and-anyone-with-a-search-bar-can-find-them/">Claude shared chats have been indexed by Google and anyone ...</a></li>
<li><a href="https://thecybersecguru.com/news/claude-shared-chats-google-search-privacy/">Claude Share Links Became Searchable on Google and Bing: What ...</a></li>
<li><a href="https://cybersecuritynews.com/claude-ai-shared-chats/">Claude AI Shared Chats Reportedly Exposed in Google Search ...</a></li>

</ul>
</details>

**社区讨论**: 用户对数据泄露的严重性表示担忧，许多人强调需要立即审查并删除包含敏感信息的共享对话。一些人将此与之前的 ChatGPT 事件进行比较，质疑为何类似漏洞在 AI 平台中不断出现。讨论强调了用户在 AI 工具中主动管理隐私设置的重要性。

**标签**: `#security`, `#privacy`, `#AI`, `#Claude`, `#vulnerability`

---