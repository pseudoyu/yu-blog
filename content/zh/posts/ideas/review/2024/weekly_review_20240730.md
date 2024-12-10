---
title: "周报 #66 - 10x 工程师、技术热情与个人工具箱"
date: 2024-07-30T20:30:00+08:00
draft: false
tags: ["review", "life", "tools", "epubkit", "work", "painting", "programming"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20240730](https://image.pseudoyu.com/images/weekly_review_20240730.png)

本篇是对 `2024-07-22` 到 `2024-07-30` 这周生活的记录与思考。

经过了异常丰富的 Adventure X 一周活动，算是回归了沉下心写代码的日常。忙于一些工作需求；使用 Cloudflare Worker 继续开发 EpubKit 的 api 部分功能；使用 Go 重构了一年多前就启动但是一直没成型的 side project 后端部分，并开始尝试用 rust 写一个 api server；为自己一个个人工具箱项目「[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)」写了一个 Astro 网页项目「[tools.pseudoyu.com](https://tools.pseudoyu.com/)」；写了 Remark42 部署的教程博客，并经过了一位在搭建博客系统的读者的可行性验证；全家去千岛湖一个水上乐园玩，感觉自己太现充了；尝试水彩画，并启动了车库墙绘项目；还有很多有意思的事。

## 10x 工程师

![randy_10x](https://image.pseudoyu.com/images/randy_10x.png)

Randy 最近上线了一个「[Ask Hackers](https://askhackers.com/)」项目，是一个基于 Hacker News Comments 的搜索工具，感觉从想法萌生到上线推广大概也就一两天，想到了一个叫「10x 工程师」的概念，能够快速将自己的一个想法开发实现，很羡慕。

自己其实前前后后也做了不少工作和个人项目，惭愧地说技术栈接触了不少，都能写一点但也都不深，快速实现和迭代一个产品的能力还是很差，似乎从想法到 Demo/产品之间依然差了一环，也跟 Randy 聊过这个话题，他觉得还是工程经验的问题，他看到某个网站或者 App 的某个效果，基本上能大致猜到实现的方式并复现，而我可能还是得靠去看源码或者咨询 AI 才能勉强做到。

## 技术热情

除此之外，我发现热情和动力也左右着我的行为，可能是由于依然没有找到自己的产品 Idea 和方向，总是感觉自己之前做 side projects 的时候仅仅是在“实现”或是技术练习，吸引我的并不是产品成型本身而是在实现过程中的了解学习和技术能力的提升，对于个人来说无可厚非，但对于一个产品来说似乎是缺少了灵魂，就像第一次见 Randy 时我好奇地问他为什么不再更新 Cusdis 了，有不少 Star，也有包括我在内的很多自部署用户，印象里他说除了经济因素外，更多是由于自己没有动力去做了，没办法为一个自己都不会去用/为之付费的产品付出更多的热情。

其实自己的症结也在于此，似乎依然没有找到会让自己半夜兴奋到睡不着的想法，反倒是在一起开发 EpubKit 时，由于自己也是电子书的多年用户，从自己作为用户的角度出发，能够对产品的迭代有更多想法和热情，也会更有成就感。

自己一定要是产品的第一个用户。

## 个人工具箱项目

![yu_tools_website](https://image.pseudoyu.com/images/yu_tools_website.png)

自己一直是一个各种软硬件的重度折腾爱好者，几乎每一个自己很小众的需求都会花大量的时间挑选出最合适的工具，哪怕检索的时间远远超过了使用工具本身，依然乐在其中。从大学到现在，身边也有无数人会问我类似“有什么推荐的相机/键盘/麦克风/xxx 么”、“我想在手机上做 xxx 有什么推荐的软件么”这类的问题，于是两年多前萌生了自己做一个个人工具箱列表的想法 —— 「[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)」。

最开始只是一个简单的 GitHub 项目和一个 `README.md` 文件，后来慢慢添加了一些分类，并为每个条目增加了一条简短的描述，两年里阶段性更新了几次，没想到竟成为了我 star 最多的一个 repo 了。

之前有看到过自己很喜欢的开发者「[devaslife/Takuya Matsuyama](https://www.craftz.dog/)」做的一个工具箱网站 —— 「[A curated list of the tech I use](https://uses.craftz.dog/)」，为每一个工具拍照并附上使用体验，觉得很有价值，于是也花了一晚上参照他的模板使用 Astro 做了一个网站 —— 「[tools.pseudoyu.com](https://tools.pseudoyu.com/)」，只是会更多地偏向软件和服务，而随着条目增加，也想添加类似「[Ask Hackers](https://askhackers.com/)」的对话搜索功能。

软硬件的拍摄、截图和介绍是个大工程，持续更新中，有需要的朋友可以关注一下。

## 个人生活剪影

### 水彩

![rust_painting](https://image.pseudoyu.com/images/rust_painting.jpg)

某次饭后家人一起尝试在扇子上画水彩，也是全新的体验，挑选了 Rust 小螃蟹，在学姐的亿点指导下完成了这幅作品，很开心！！！

### 车库墙绘

![wall_painting](https://image.pseudoyu.com/images/wall_painting.jpg)

既上次使用 DALL-E 生成了想要在车间墙绘的图之后，这种终于得空开工，进度 30%，但是由于周一晚刚好组会，是学姐和我妹妹画的，带了相机也没来得及用相机记录下完整过程，有些遗憾，下次会多拍一些流程和细节，期待最终效果。

### 捏捏

![nienie_on_desktop](https://image.pseudoyu.com/images/nienie_on_desktop.jpg)

最近或许是察觉了我的忙碌，两只小猫都变得更加黏人，每次写代码时捏捏也都静静趴在桌上，时不时伸个懒腰或者发个嗲，松弛而治愈。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 收藏

- [Hono - Ultrafast web framework for the Edges](https://hono.dev/docs/)
- [Ask Hackers](https://askhackers.com/)
- [OpenMoji](https://openmoji.org/)
- [Vercel AI SDK](https://sdk.vercel.ai/)
- [Open Source Alternatives To Proprietary Software](https://www.opensourcealternative.to/)

#### 书籍

- [**Shape Up**](https://book.douban.com/subject/34945817/)，可汗学院创始人写的关于 GPT 与教育未来的思考与实践，对日常使用 LLMs 有挺多启发的，除了成为搜索引擎一样的工具向外还有很多想象空间。

#### 文章

- [订阅制搜索引擎: Kagi](https://anotherdayu.com/2024/5837/)
- [从零开始搭建你的免费博客评论系统（Remark42 + fly.io）](https://www.pseudoyu.com/zh/2024/07/22/free_commenting_system_using_remark42_and_flyio/)

#### 视频

- [路遇榜一小孩哥，竟要现场给我钱！？](https://www.bilibili.com/video/BV1J4421S7hA)
- [你有能力变得快乐｜推书《蛤蟆先生去看心理医生》](https://www.bilibili.com/video/BV1s8vKegE66)

#### 剧集

- [**去有风的地方**](http://movie.douban.com/subject/35662223/)，吃饭的时候看。

