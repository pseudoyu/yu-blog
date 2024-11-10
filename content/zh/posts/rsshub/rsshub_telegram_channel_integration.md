---
title: "RSSHub 开发实践 #01：Telegram 频道 RSS 订阅实现与部署方案"
date: 2024-11-09T12:46:16+08:00
draft: true
tags: ["RSSHub", "Telegram", "API", "MTProxy", "proxy", "network", "tools"]
categories: ["Programming"]
authors:
- "pseudoyu"
---

## 前言

最近在参与 [Follow](https://follow.is/) 以及 [RSSHub](https://github.com/DIYgod/RSSHub) 这两个开源项目的一些开发维护工作，因为牵扯到与很多订阅源的“斗智斗勇”，有一些很有意思的开发实践，于是开了这个新坑系列记录下来。

本篇是这几周使用 Telegram 官方 API 与 MTProxy 来实现对 TG 频道更新的开发实践与完整配置部署教程。

## RSSHub

![rsshub_homepage](https://image.pseudoyu.com/images/rsshub_homepage.png)

RSS (Really Simple Syndication) 是一个古早的信息聚合标准，它通过统一的数据格式，让用户能够便捷地订阅和获取网站更新。然而，随着社交媒体和移动互联网的兴起，原生支持 RSS 的网站正在减少。

这时，开源项目 RSSHub 应运而生，它秉持着"万物皆可 RSS"的理念，通过开源社区的力量将包括 Telegram、YouTube、播客在内的众多现代内容平台转换为标准的 RSS 格式，让用户能够重新掌控自己的信息获取方式，远离算法推荐的干扰。

## RSSHub Telegram 集成

### Telegram 频道

![follow_telegram_channel](https://image.pseudoyu.com/images/follow_telegram_channel.png)

Follow 中提供了一种便捷的订阅信息源方式，例如用户可以输入对应的 Telegram Channel Name 来订阅某个频道的更新，这样就无须跳转到各个频道里去逐个查看。

![yu_channel_online_preview](https://image.pseudoyu.com/images/yu_channel_online_preview.png)

由于 Telegram 提供了频道的网页预览功能，例如可以通过 [t.me/s/pseudoyulife](https://t.me/s/pseudoyulife) 这一链接直接查看我自己频道的更新，因此 RSSHub 很早之前就实现了通过抓取网页上的内容并转换为 RSS 格式的方式集成了对 Telegram 频道更新的订阅。

![telegram_channel_reorx_preview](https://image.pseudoyu.com/images/telegram_channel_reorx_preview.png)

然而后来许多用户反馈说部分频道抓不到，去测试了一下，发现 Telegram 用一种黑盒的机制来限制了部分频道的网页预览功能，例如我一直在订阅的「[Reorx’s Forge](https://t.me/reorx_share)」以及「[Newlearnerの自留地](https://t.me/NewlearnerChannel)」等频道，当使用 `/s` 来访问页面时会被强制重定向，提示需要打开客户端来查看内容。
