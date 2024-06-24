---
title: "周报 #62 - 香港之行、5am club 计划与 Rust 学习"
date: 2024-06-23T16:30:00+08:00
draft: false
tags: ["review", "life", "rust", "hong kong", "trip", "learn"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20240623](https://image.pseudoyu.com/images/weekly_review_20240623.png)

本篇是对 `2024-06-17` 到 `2024-06-23` 这周生活的记录与思考。

去香港参加 Google AI+Web3 活动，面基了组里的很多小伙伴；体验了因订不到房而露宿网吧；打算根据 5am Club 理念调整生活节奏；第二次入门 Rust；还有很多有意思的事。

## 香港之行

![henry_and_kate_at_google](https://image.pseudoyu.com/images/henry_and_kate_at_google.jpg)

这周最有意思的事是去香港参加了 Google 的 Web+AI 的活动，我们项目在其中有一些 talk 和圆桌论坛，刚好也有机会参观了 Google 的香港办公室（以及拿了一些周边）。远程办公之后，其实比较少能有机会和同事们面对面，而这次活动我们组除了一位在美国的同事没法赶到外，其他人都相聚香港，还一起聚餐、打德州以及后面续了一场深圳漫步。

![stay_netbar](https://image.pseudoyu.com/images/stay_netbar.jpg)

很有意思的是由于我和杭州一同来的同事 ares 没有提前订好房，直到零点之后在铜锣湾时代广场四处找酒店，最后选择了去露宿网吧，刚好拿着从 Google 那边领的抱枕，倒也是挺好睡的。

突然想到之前在香港读书赶课程大作业的 due，当最后卡着 ddl 提交后，和小组成员一起买了一堆零食和啤酒在维港闲聊、看日出的经历；也想起之前和朋友去泰国，跟着 Pokémon GO 的地图四处解锁景点；以及去青岛旅行时让出租车司机随便开，带着我绕一圈有趣的地方，这些都是很有趣的人生体验。

我虽然是个 j 人，在大部分时候会制定严密的计划，但也非常享受这份生活的随机性，或许多年之后并不会记得这场 Google 的 talk 有什么有趣的发言，但一定不会忘记这一晚在网吧过夜的记忆画面。

## 5am club 计划

![hangzhou_night](https://image.pseudoyu.com/images/hangzhou_night.jpg)

Robin Sharma 有一本书叫《5am Club》，提出了一个早上五点起床，进行自我提升学习、锻炼以达到最佳状态的概念，虽然对于经常熬夜到三四点甚至更晚的我可能 5am 睡更容易达到，不过依然对这种新的生活方式有些憧憬。

大学有过很长一段时间的极端自律，每天一两点睡、六七点起，似乎有着用不完的精力和时间，在香港读研期间也由于跨专业的焦虑和课业压力，每天六点多起床去图书馆占座，接近 11 点才回到租屋，循环往复却也乐在其中。

但大概是由于工作之后白天的许多时间天然被占据，似乎这样的习惯很快被打破了，为了有更完整的自己的时间，更晚睡，却也更晚起。有阶段性会保持不错的状态，但也容易陷入一些不好的循环，晚上学习状态不好 -> 焦虑 -> 报复性熬夜 -> 第二天起床更晚 -> 白天效率低下 -> 晚上学习状态更不好。

于是想从这周开始进行一下尝试与挑战，倒不一定是严格的五点，只是相对更早，把熬夜的学习时间平移到早上，一直到 11 点左右调整到开始上班的状态。

而由于被隔壁 「[polebug](https://space.bilibili.com/58078997)」 的 study vlog 卷到，也有了一些尝试新领域的学习动力，所以也给自己定了更加有趣的目标，早上最开始学习的是一些跟工作并不直接相关但一直想体验的东西，比如 SwiftUI、Rust 以及使用 langchain 进行一些 AI 应用的开发实践等等，这次也打算直接 learn by getting hands dirty，直接上手一些 side project 或是给开源项目贡献 pr。

## Rust 学习

![rust_bag_2023](https://image.pseudoyu.com/images/rust_bag_2023.jpg)

承上文，打算~~第二次~~入门 Rust，上次入门还是在 22 年，其实还挺认真地学了一阵子，跟着写了一些 demo 项目，还做了学习笔记「[pseudoyu/learn-rust](https://github.com/pseudoyu/learn-rust)」，不过确实工作里没有应用场景，已经忘得差不多了。

组里有个 Rust 狂热爱好者 kally，香港和深圳之行一路在推荐，甚至在我上飞机前还让我下了 YouTube 上的入门视频，~~确实挺好睡的~~。

不过正经地打算重新学习一下，也上手写一些自己的项目，目前的想法是把之前一个通过 RSSHub 来订阅多个平台信息源同步的 go 项目通过 rust 重写一下，以及看看有没有什么好玩的开源项目可以参与。

目前在看 kally 推荐的一些 YouTube Channel 的基础视频，以及很久之前买的极客时间的「Rust 编程第一课」，Rust，启动！

## Telegram Channel 1000 subscribers

![channel_1000_subscribers](https://image.pseudoyu.com/images/channel_1000_subscribers.jpg)

[频道](https://t.me/pseudoyulife) 1000 subscribers 达成！感觉越来越少在推或者其他平台上表达，更喜欢在频道里碎碎念了。

其实分享欲这个东西一直存在，有时候是与自己对话，有时候是和身边的人秉烛夜谈，又有更多的时候想分享给更多人得到一些反馈，只是关闭朋友圈的我似乎已经不太习惯将这些分享到我的周围，所以有很长一段时间 twitter 成为了这个出口，而这一年，博客的读者和频道的关注着才慢慢成为分享的对象，感觉其实现在的节奏下似乎好好听人说话、思考并回应似乎成为了一件弥足珍贵的事，我也时常告诫不要忘记这一点。

也谢谢你们好好听我讲话。

## 其他

### mac

![new_mbp_setup](https://image.pseudoyu.com/images/new_mbp_setup.jpg)

新拿到的 Google Cloud 贴纸贴上了我的 MBP，集邮了！

周中发现 mac 出现了灵异事件，当 slack/zoom 等软件打开麦克风时光标就不受控制，以 2-3 秒一次的频率点左上角菜单栏，像是被远程控制了一样，且其他时候一切正常，去了 Apple 和技术支持小哥一起排查了好一会儿定位到了是新安装的 Bartender 的替代品 iBar 导致的，据评论区说 Barbee 也有这个问题，大家可以参考一下 🫡。

小哥说我复现、排查思路和操作的熟练度可以来这里上班了 🤣 Apple 的用户真的是自适应的。

再加上之前刚有一个电脑被家里另一只小猫饭饭咬坏了屏幕，决定斥巨资给我的 MBP14 补买一个 Apple Care，刚好 7.3 过一年的保，Apple 小哥跟我说一年内补买可以在这个继续上再续三年，感觉很划算，等于多了一年！

### 招聘

顺便发一个我司的招聘：[https://rss3.notion.site/52350e21c7e74a319807a4fcd6adf68e?v=3eb777c3d54f4a6888c405968cee9d69](https://rss3.notion.site/52350e21c7e74a319807a4fcd6adf68e?v=3eb777c3d54f4a6888c405968cee9d69)

目前在招 DevOps Engineer/AI Engineer/Blockchain Engineer，远程办公，工作氛围很好，有疑问可以随时问我，期待未来做同事。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 书籍

- [**索拉里斯星**](https://book.douban.com/subject/35049755/)，与三体的设定类似，索拉里斯星围绕着双星旋转，但是不同于三体的降临或是拯救，索拉里斯星其实或许根本并不关心地球和上面渺小的人类，只是人类单向的自我中心罢了，甚至想用自己更为“高尚”的思想与价值观去改变它，探索也不过只是伪善。。
- [**Normal People**](https://book.douban.com/subject/34453257/)，很喜欢这个英剧，这两天看其他书的时候突然想到了这本，打算补一下原著。
- [**What My Bones Know**](https://book.douban.com/subject/35754687/)，去年看了一小半，这两天想到关于家庭和心理疗愈的问题，就睡前又翻了几页。
- [**阿特拉斯耸耸肩**](https://book.douban.com/subject/33445309/)，读者送的，开始读了。

#### 收藏

- [CS193p - Developing Apps for iOS](https://cs193p.sites.stanford.edu/2023)
- [SwiftUI Tutorials | Apple Developer Documentation](https://developer.apple.com/tutorials/swiftui)

#### 文章

- [How I Use Obsidian](https://macwright.com/2024/06/16/how-i-use-obsidian)
- [给 Hugo 博客的代码区块更换主题](https://blog.douchi.space/blog-code-syntax-highlighting/)

#### 视频

- [vlog #60｜女程序员下班后的学习记录｜啃 Celestia 的文档｜Modular Blockchain｜英语日常练习｜桌面小装修｜入手了新设备](https://www.bilibili.com/video/BV1Jr421F7W9)
- [《博德之门 3》青出于蓝，变革虽大但在某个方面其实是完美的延续【就知道玩游戏】](https://www.bilibili.com/video/BV1CS411A7xw)
- [vlog #61｜女程序员下班后的学习记录｜状态混乱就快去学习吧｜RUST｜在读《被讨厌的勇气》｜运动带给我的变化｜日常英语学习｜TEDTalk](https://www.bilibili.com/video/BV1L1421k7bK)
