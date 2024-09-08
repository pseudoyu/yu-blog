---
title: "周报 #72 - 滑板体验、Rust Conf 与 Follow 公测（含邀请码）"
date: 2024-09-08T16:00:00+08:00
draft: false
tags: ["review", "life", "rust", "follow", "tool"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20240903](https://image.pseudoyu.com/images/weekly_review_20240903.png)

本篇是对 `2024-09-03` 到 `2024-09-08` 这周生活的记录与思考。

去上海参加了 Rust Conf 2024，度过了两天，收获了很多周边，现场在同事的指导下重构我的用 Rust 写的 Api Server；Follow 进一步扩大了公测规模，要到了 10 个邀请码，会在本篇的评论区发放；还有很多有意思的事。

## Lake 游戏

![lake_pic_01](https://image.pseudoyu.com/images/lake_pic_01.jpg)

虽然团队的项目已经在上一周顺利上线了，似乎依然有不少需要忙的任务，工作时间偏晚，再加上早上要晨跑，工作状态和睡眠之间的界限比较模糊，有时候躺着很久都睡不着。持续了接近几天后，整个人有些提不起精神，于是决定晚上在 [Lake](https://store.steampowered.com/app/1118240/Lake/) 游戏中送送信放松一下。

![lake_recommendation](https://image.pseudoyu.com/images/lake_recommendation.jpg)

好久之前就在 Randy 的一条推文了解到它，作为「[Life is Strange 系列](https://store.steampowered.com/curator/36149206)」这类游戏的爱好者，对于这种更生活化、平静却又引发思考的游戏一直很感兴趣。

如我在「[周报 #70 - 消失的附近，Burnout 与 Boreout](https://www.pseudoyu.com/zh/2024/09/01/weekly_review_20240901/)」中所说的那样，早早离开家乡的我现在也几乎没什么还在联系的童年玩伴了，小镇风景和我记忆里的村落当然也是天差地别，却依然被能够在各个小屋、邻居家亲切打招呼，倾听他们故事的感觉心生向往，或许这样的生活方式比起繁华的都市更加让人变得具体而知足。

不要问我一个程序员下班的时候还要扮演一个程序员下班/休假，我之前下班还玩「Shenzhen I/O」模拟程序员上班 🤡...

## 滑板体验课

我从小时候开始玩了十几年轮滑，几年前也曾学过一小阵子滑板，不过不算很系统，一直很想精进一下，后面也可以习惯滑板上路。

因为只是一小时的体验课，教练更多从滑行、放板、收板和转体的一些入门动作开始，纠正了挺多之前自己玩时候的不规范动作，慢慢也习惯了在板上的感觉。后面有两次因为想尝试下陡坡而狠狠摔了两跤，疼但却反而更有了一些运动后的压力释放感，也更感知到这一运动的魅力。

不过系统性的课程还挺贵的，可能考虑先自己再玩一阵子，10 月去清迈旅居的时候去找当地的教练学。

~~摔太惨就不放图了。~~

## RSSHub 部署迁移

![rsshub_hits](https://image.pseudoyu.com/images/rsshub_hits.png)

前几天因为不小心同步 OneDrive 和 iCloud 的时候用了自己 VPS 搭的代理，主力机器流量被刷完了，导致自建的 RSSHub 也停了。因为作为公益公开实例挂在 RSSHub 官网上，想着还是维护一下，于是转移到了另一台闲置的 2C2G 的机子上，发现机器瞬间被打爆了，看了下平均每分钟 100+ 次请求...

研究了一下发现 Zeabur 的模板没法通过 WebSocket 来访问 `browserless/chrome` 服务，现在用的镜像也并不内置 `Puppeteer`，很多网站没办法抓取，以至于很多路由失效，于是改了一下，发布了一个 Zeabur 模板，现在支持一键部署带 `Puppeteer` 的 RSSHub 实例了 —— 「[RSSHub (With Puppeteer)](https://zeabur.com/templates/X46PTP?referralCode=pseudoyu)」，欢迎一键部署。

然后自己部署了一份，也算是为 RSS 事业做贡献了。

## Rust Conf

![rust_conf_pics](https://image.pseudoyu.com/images/rust_conf_pics.jpg)

> 这次没怎么拍照，偷了同事的周边图。

似乎每年都有那么一两个月会更“现充”地参与各种线下活动，和远程办公的同事/朋友们相聚。在参加完 ETHShenzhen 不久后，我又约了一些同事朋友来上海一起参加 Rust Conf，度过了有趣的两天一夜。

搜刮了一圈周边，去看了几个感兴趣的 Talk，和新老朋友浅聊一会儿，最后还是聚众在会场的一角 Review 和修改我写的 Rust 烂代码，学到了。

早上刚到就京东下单了一本「Rust 程序设计」，刚送到在酒店大厅开始学了...

## 个人生活剪影

### 偶遇的有趣设计

![interesting_tre_huzhou](https://image.pseudoyu.com/images/interesting_tre_huzhou.jpg)

上周去湖州莫干山尝试了一下林间木屋，本身体验普普通通，但在返程时见到的一个有趣的大眼树却印象深刻，感觉在车窗的滤镜下有很日系。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。并且把 Telegram Channel 消息作为内容源搭建了一个微博客 —— 「[daily.pseudoyu.com](https://daily.pseudoyu.com/)」，可以更方便浏览了。

#### 书籍

- [**Rust 程序设计（第 2 版）**](https://book.douban.com/subject/36547630/)。

#### 文章

- [Founder Mode](https://paulgraham.com/foundermode.html)
- [Introduction to TON Technology and Tact Programming](https://blog.laisky.com/p/ton-tact/)

#### 视频

- [《黑神话悟空》对中国游戏的最大意义是什么？【就知道玩游戏】](https://www.bilibili.com/video/BV1fnHReYEok)
- [小，但好用！你的掌上新玩具｜大疆 NEO 上手](https://www.bilibili.com/video/BV1DpH2eFEcB)

#### 音乐

- [**Stillness**](https://open.spotify.com/track/0kyErLRQKL8DXVP3rSqA4e) by A-Sun

## Follow 公测特别活动

在之前的一篇「[周报 #67 - 使用 follow 重塑我的信息输入系统](https://www.pseudoyu.com/zh/2024/08/05/weekly_review_20240805/)」讲了我使用 Follow 这一应用的体验，依然十分惊艳。

一个多月过去了，依然是我每天都高频打开的软件，软件也迭代了不少新功能和亿点细节，慢慢也开始扩大公测规模了。

我向 Diygod 要了 10 个邀请码来作为博客/频道读者的福利。

### 参与方式

在本篇文章下评论你关于阅读、信息流、RSS 使用或关于周报的相关想法，我会在北京时间 9.9 日 22:00 挑选 10 位发放邀请码，我会在评论区和 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道公布名单，选中的用户可以联系 [pseudoyu@connect.hku.hk](mailto:pseudoyu@connect.hku.hk) 或任意我的社交平台私信。

活动后也可继续留言，如果我后续能拿到更多名额（~~或者我努力签到赚 Token~~），也会继续在评论区发放，欢迎参与。
