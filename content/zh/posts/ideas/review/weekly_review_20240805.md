---
title: "周报 #67 - 使用 follow 重塑我的信息输入系统"
date: 2024-08-05T05:30:00+08:00
draft: false
tags: ["review", "life", "tools", "follow", "work", "painting", "programming"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20240805](https://image.pseudoyu.com/images/weekly_review_20240805.png)

本篇是对 `2024-07-31` 到 `2024-08-04` 这周生活的记录与思考。

这一周最开心的是体验到了 follow，久违的一款让我有兴奋感的应用，对比了 Readwise，并决定退掉订阅；做了一套自部署的 Web Archive 方案，eat your own dog food 的感觉真好；继续和学姐一起做墙绘；还有很多有意思的事。

## 使用 follow 重塑我的信息输入系统

### 我的信息输入系统

很久之前自己其实是一个信息重度依赖者，遇到好的博客/资讯网站，迅速加到 RSS 订阅源中，看着分类/标签井然有序的列表傻乐；遇到好的 newsletter，也马上用邮箱订阅；每天早上第一件事就是把当时还在用的 Reeder 4 未读清空，再将 newsletter 中的邮件一条条浏览。

起初其实还行，似乎自己关心的一些资讯和文章都能第一时间读到，有一种满足感，但逐渐就有些过载了，每天早上花在上面的时间越来越多，即使并不感兴趣的文章也会花费一些时间去消化，与其说是获取信息，倒不如说是一种信息渴求和对信息焦虑的代偿，效果自然是有的，信息都在大脑中留下了痕迹，但消化效率并不高。

在阅读了「[使用自动化工作流聚合信息摄入和输出](https://reorx.com/blog/sharing-my-footprints-automation/)」和「[对 Newsletter 说不](https://diygod.cc/say-no-to-newsletter)」这两篇文章后，我做出了很大的调整。

信息源方面，我退订了所有公众号和 newsletter，并将 RSS 订阅源缩减到 50 个左右，剩下的大部分输入都来自于 Twitter、他人的 Telegram 频道等，在把输入控制在一定量级，且一定程度上避免信息茧房。

并且由于使用 n8n + telegram channel 构建了一个输入、输出源的自动同步系统，会把我所有筛选过的信息源自动同步到我的 Telegram 频道「[Yu's Life](https://t.me/pseudoyulife)」中，方便自己查看和回顾，顺便也作为一个个人分享渠道了，而因为有了公开的压力，也反向推动我更认真地筛选信息源。

但这个方案依然存在两个问题：

1. 依然没能解决我信息源分散的问题，我需要频繁在 Twitter 和各个 TG Channel 之间切换，很容易分心并且依然可能会错过一些消息
2. 我常常把频道作为我某种程度上的收藏夹，有时候很多信息很个人化，随着频道的关注者越来越多，我也会有一些心理压力，担心成为他人的信息噪音

而 follow 的出现恰好填补上了我方案的这一环。

### follow

#### 介绍

> Next generation information browser

这是 follow 的 slogon，发布之前我也仅仅是把它作为一个 RSS 阅读器的 Alternative，虽然我也很熟悉 RSSHub 且自己部署了实例重度使用，但依然很难想象基于这一古早的协议还能有多大的发挥空间，直到发布和几天高强度使用后，才逐渐理解这一理念。

在 RSS 早已式微的当下，除了独立博客这一处境差不多的古早形式几乎都还保留着完整的 RSS 支持外，大部分新闻、资讯和各种小众网站都已经不再提供了，RSSHub 则是完美的且几乎是唯一的解决方案了，可以将包括但不限于 Twitter、TG Channel、Bilibili 和网易云歌单的一些网页信息源转换为标准 RSS 格式，可以像订阅文章一样获取这些信息源的更新。

然而，RSSHub 终究还是更中间层一点的工具，即使有了标准的 RSS 数据，大部分阅读器依然只能处理文本显示，对于音视频图片的处理基本上只停留在当作一个 url 这一程度，因此我更多也是应用在自己的 n8n 同步工具流中作为通知，只保留其 title 与链接，依然是点击源链接跳转会对应的网页查看，使用起来常常有些割裂。

follow 最大的特点自然还是传承于 RSSHub 的「万物皆可 RSS」理念，在应用层对视频、图片、博客音频、文章、社交媒体等多种形式的内容都提供了呈现方式，确实有一种看久了 purl html 突然飞跃到加了现代化 css 效果的感觉。其实技术层面做到这一步算不上有太高的壁垒，不论是视频 iFrame、音频播放器或是图片预览都有比较成熟的组件可以使用，但 follow 几乎是唯一一个依然在针对这一协议做且做好这一步的产品。有时候，做好一点就足够了。

#### 体验

![follow_homepage](https://image.pseudoyu.com/images/follow_homepage.png)

作为一个信息浏览器/阅读器，最直观且核心的就是界面和交互了，DIYGod + 拾一两位的组合早早把我的期待值拉满，但即使是内测的第一版，其完成度和体验也依然让我感到惊艳，在此之前最现代化的应该要数 Reeder 4 了，而 follow 即使是 Electron 而不是纯原生，也依然保持了极其精致的设计和交互。

我之前用过 NetNewsWire、Reeder 4、Miniflux 和 Readwise Reader 等多款阅读器，但由于阅读体验常常还不如原网页，我大多还是会选择跳转链接查看，而 follow 的页面和交互则本身就让我享受其中，还有一个很有意思的最近阅读记录显示，可以看到自己这篇文章有哪些访客，还可以点进主页去看他们的订阅源，兼具了社交属性和信息源的积累，我就通过这种方式发现了很多之前没关注到的个人博客。

另外，由于 follow 和 RSSHub 深度集成，可以实现输入 twitter handle，B 站 uid 以及 youtube channel name 之类的来直接订阅社交媒体，而不用自己去文档找 RSSHub 网站的对应路由，也不需要自己去搭建实例，非常友好。

![follow_pic](https://image.pseudoyu.com/images/follow_pic.png)

![follow_video](https://image.pseudoyu.com/images/follow_video.png)

而针对视频和图片的直接显示也是一大亮点，还看到有一个使用者将一些设计师的 Twitter 作为自己的设计灵感源和审美积累，也是很有意义的应用场景。

而音频/播客则可以在 follow 中全局播放，例如前几张截图的左下角，我就是同步在播放「[代码之外](https://beyondcodefm.com/)」的一期节目，这也解决了我需要在 Apple Podcast、Spotify 和小宇宙等多个播客应用之间反复横跳的问题。

另外也可以比较方便地分享自己的订阅：<https://web.follow.is/profile/pseudoyu>

其实还有不少设计，如 Action 模块、Power 打赏等，但本文并不是一篇软件测评而是个人体验向，所以就不过多展开了，等后续开放了大家可以自己去体验一下，保留一些惊喜感。下面想谈谈和我目前所在使用的 Readwise Reader 的对比，以及我为什么打算转换到 follow。

#### Readwise Reader -> follow

![readwise_sub](https://image.pseudoyu.com/images/readwise_sub.png)

我大概是去年 9 月订阅了 Readwise Full 会员，虽然为发展中国家提供了 50% 的 discount，但依然需要接近 50 刀一年的费用，它大而全，但我使用的核心功能其实只有三点：

1. rss 阅读器
2. 稍后读、 保存文章与划线标注
3. Daily Digest

其中第一点是最高频的，作为一个很方便的阅读器来管理自己的文章等订阅，也有移动端 app 可以随时看，但在使用中发现有时候显示样式和图片加载比较一般，而分类、快捷键又有点太繁复，且主要支持的还是文章，显而易见可以被 follow 完全替代（蹲一个移动端）。

划线标注之前用得比较多，会使用插件在一些文章做一些笔记，并保存到 Readwise 中，再通过 n8n 将我的文章同步到 Telegram Channel 中，但其实有些过于依赖平台了，在我真正想要消化那些划线笔记整理成一些成型的想法或是文章时则需要回到 Readwise 中去查看，即使同步到 Logseq 或是 Heptabase 中整理依然不算方便，尤其是现在转向 Apple Notes 作为自己的主力且唯一笔记工具后，发现有一些想法直接摘录/记录下来才是效率最高也更容易产生价值的，因此划词这一点渐渐淡出了我的笔记流。

![save_website](https://image.pseudoyu.com/images/save_website.jpg)

众所周知，稍后读通常都会演变为稍后再也不读，所以我现在的策略是几乎不用稍后读，尽量当下就读完，只有极少数比较长的会暂存一下，也尽量在当天清空 list。我现在则是在 follow 中以未读为默认显示模式，时常会浏览一下，遇到感兴趣且通读了的文章会使用 star 功能，保存在收藏夹中，读完有所收获的时候则会通过一个自己做的浏览器插件 + Cloudflare Worker api + n8n 将文章链接及源 html 文件保存到 D1 数据库，实现 Web Archive 并自动同步到我的 Telegram Channel 中。

而第三点 Daily Digest 则是会帮助我回顾一些自己的笔记或是文章，这一点有用但并不高频，还没细研究 follow Action module 能不能针对多篇文章做一些操作。

由于我的核心需求都可以转移到 follow 中，于是果断退订了 Readwise。其实能明显地感受到这几天我的信息摄入量和质量也显著提高了，一个好的软件其实并不仅仅是辅助工具，是会对思维与习惯产生更深远的影响。

## 个人生活剪影

### Electron Bug

![talk_with_innei](https://image.pseudoyu.com/images/talk_with_innei.jpg)

刚发现 follow 客户端更新有个问题，点击「Click to restart」窗口 hide 了而不是 quit，熟悉的 bug，之前写 EpubKit 我写过一模一样的 🤣 报给了拾一，属于 electron 病情交流了。

### macOS 桌面装修

![macos_widgets](https://image.pseudoyu.com/images/macos_widgets.png)

第一次尝试 macOS 系统的桌面小组件，还挺新鲜的，不过我基本都是 Raycast 快捷键切换应用，几乎看不到桌面...

### 车库墙绘

![car_painting_week2](https://image.pseudoyu.com/images/car_painting_week2.jpg)

本周总体进度：20%，已经初具雏形了。

本周我的进度：画了五六块砖 🤣

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。并且把 Telegram Channel 消息作为内容源搭建了一个微博客 —— 「[daily.pseudoyu.com](https://daily.pseudoyu.com/)」，可以更方便浏览了。

#### 收藏

- [pseudoyu | Follow](https://web.follow.is/profile/pseudoyu)
- [DIYgod | Follow](https://web.follow.is/profile/DIYgod)
- [n8n 中文教程 | 简单易懂的现代魔法](https://n8n.akashio.com/)
- [Dengtab - Stay focused and reduce social media distractions while cultivating small habits.](https://dengtab.com/)
- [SixD - SwiftUI & Interaction Design](https://www.haolunyang.com/sixd)
- [ccbikai/BroadcastChannel](https://github.com/ccbikai/BroadcastChannel)

#### 播客

- [第 10 集 | 花果山大圣聊职业选择、如何靠销售立足、房车之旅、以及英国的新生活](https://www.listennotes.com/e/7f2efa4ad8394de79591a3ee2da6a5d1)
- [Ep 48. 专访高天：为了当好 B 站 up 主，我成为了 Python 核心开发者](https://www.listennotes.com/e/5e5454656bb146499bef687dcec00e65)

#### 文章

- [断食记](https://blog.douchi.space/intermittent-fasting/#gsc.tab=0)
- [WebP Cloud Services 在去 Cloudflare 化上的一点摸索](https://blog.webp.se/de-cloudflarize-zh/)
- [P5r: Life Changed](https://jesor.me/2024/persona5r-life-changed/)
- [忙碌中的思索：生活、工作与娱乐 - 静かな森](https://innei.in/notes/175)
- [我理解的云原生](https://gist.github.com/sljeff/cce768194a9e68d5279bfde861ff5f76)
- [Stripe 如何安全收款并避免盗刷与测卡](https://dmesg.app/stripe-fraud.html)

#### 视频

- [休学+拒绝百万年薪，不是有所成就才算活着](https://www.bilibili.com/video/BV1dx4y1x7mz)
- [Learn with me - HTMX and HonoJS](https://www.youtube.com/watch?v=hMcE6E8JjXA)
- [【何同学】你再也回不到 19 岁的夏天了...](https://www.bilibili.com/video/BV15b42177rL)
- [450 天成为 Python 核心开发者](https://www.bilibili.com/video/BV1of421972c)
- [10 年后，900 万了](https://www.bilibili.com/video/BV1jT42167Xb)

#### 电影

- [**走走停停**](https://movie.douban.com/subject/35956190/)，很喜欢最后高速堵车那段的镜头语言，人生不过走走停停。
