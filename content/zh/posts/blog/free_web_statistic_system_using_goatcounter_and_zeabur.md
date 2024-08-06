---
title: "从零开始搭建你的免费博客统计系统（goatcounter + Zeabur/fly.io/vps）"
date: 2024-08-06T07:19:42+08:00
draft: true
tags: ["statistic-system", "serverless", "zeabur", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## 前言

在「[2024 年了，我的博客有了什么变化](https://www.pseudoyu.com/zh/2024/06/29/what_changed_in_my_blog_2024/)」一文中，我介绍了自己使用 Serverless 平台和一些开源项目搭建的博客系统，也开启了这个系列教程来记录搭建和部署全过程。

本篇是关于统计系统的解决方案。

## 统计系统方案

相比起博客本体和评论系统，我在很长的一段时间其实都没有在意过统计系统（~~主要当时也没人看~~），更加没考虑太多 SEO 或是什么其他推广方向上的事，但后来逐渐发现，其实统计下来的数据并不只是一张好看的可以用来发推的图表，其对于博客的选题、内容都有着很大的参考价值。

在博客发展过程中，统计系统方案也经历过几次迭代，其实主流成熟的方案都能够满足基本的需求，即使是免费的 Google Analysis 也完全够用，但我依然因各种原因有过几次迭代，最终使用了当前 GoatCounter 这一方案。

### splitbee

我最初其实使用的是一个免费的工具 splitbee，刚去访问的时候发现貌似已经 404 了，它提供了免费够用的统计额度，有着还不错的界面，并且还支持一些复杂的用户追踪，A/B test 等，但印象里好像只能保留半年的数据，并且月超过 5000 pv 后就需要升级了，所以后来放弃了。

### Cloudflare + Google Search Console

![cloudflare_web_stats](https://image.pseudoyu.com/images/cloudflare_web_stats.png)

去除了 splitbee 之后，很长一段时间我没有部署额外的统计应用，而是用的 Cloudflare 自带的站点统计，但是发现它其实统计的只是网络总流量，有包括爬虫在内的非常多的无效数据，并且没有精确到路径等细节。

![google_search_console](https://image.pseudoyu.com/images/google_search_console.png)

后来了解到了 SEO 这一概念后，又添加了 Google Search Console 这一统计维度，这也是我目前觉得对我创作最有意义的数据，主要呈现的是用户在搜索引擎中触达我博客站点的关键词以及通过搜索点击进入我博客的页面路径。

可以看到，一篇「[Warp，iTerm2 还是 Alacritty？我的终端折腾小记](https://www.pseudoyu.com/zh/category/tools/)」为我带来了源源不断的自然流量，而关于博客搭建、智能合约开发也是大部分从搜索引擎来的自然用户对我博客的第一印象。

### Umami + Supabase + Netlify

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

但是上述两者依然只能看到网站整体的数据，想精确到某篇文章在一段时间的表现或者文章发布后的实时访问数据，依然需要一个统计系统，我在看了 Reorx 的一篇「[搭建 umami 收集个人网站统计数据 | Reorx’s Forge](https://reorx.com/blog/deploy-umami-for-personal-website/)」选择使用了 umami 这一开源、易自部署的统计系统，界面简洁，功能易用，很方便集成到自己的博客系统中。

使用了一年半，一直倒没出现什么问题，，只不过可能因为自己用得比较早，在一次大版本更新的时候数据库 Migration 脚本出现了不兼容的字段更新，其实有点不理解这样量级的开源项目为什么会出现这样的问题，也看到 issue 中有很多其他用户有同样的诉求，但最终并没有给出一个比较好的解决方案。

但是又由于当时自己已经运行了大半年，舍不得之前的数据，于是一直拖着，停留在自己 fork 的一个旧版本，虽然倒也没有对新版本有那么多功能上的诉求，只是有点半强迫症地感觉不舒服。

前段时间在更新博客评论系统的时候，想着干脆就一起更换为更轻量的 goatcounter，并将之前的数据截图作纪念。

### GoatCounter + Zeabur

![goatcounter_stats](https://image.pseudoyu.com/images/goatcounter_stats.png)

这个小众的统计系统是我在看 Reorx 的博客代码更新的时候偶然发现的，一下子被这种 Retro Internet 的风格所吸引，几乎没有任何多余的按钮，功能却很完备，而且使用的是 go 单二进制文件 + sqlite 数据库单文件的架构，轻量而易于部署，于是打算迁移。

其实我自己的 GoatCounter 是部署在 [fly.io](https://fly.io/) 上的，但我在上一篇 Remark42 的文章中已经非常详细地介绍了 fly 的操作说明，不想有太多重复，刚好最近又在重度使用 Zeabur 这一 Serverless 平台，于是本文将以 Zeabur 为例，方式同样适用于其他类似平台。

## GoatCounter 部署说明

GoatCounter + Zeabur 的方案仅牵扯到单个服务，数据库使用的是 sqlite 挂载于 volume 中，Zeabur 本身对于容器应用的部署是需要 Developer Plan 的，但是整体用量和费用都较低，可以部署多个服务，可以酌情选择。

GoatCounter 本身代码开源 —— 「[GitHub - arp242/goatcounter](https://github.com/arp242/goatcounter)」，文档清晰易读，可以根据自己的实际需求进行配置。

### 使用 fly.io 部署

纯免费的方案依然可以参照我提到的这篇「[从零开始搭建你的免费博客评论系统（Remark42 + fly.io）](https://www.pseudoyu.com/zh/2024/07/22/free_commenting_system_using_remark42_and_flyio/)」，仅在 `fly.toml` 配置部分不同，我也提供的我所使用的配置文件 —— 「[fly.toml](https://github.com/pseudoyu/goatcounter-on-fly/blob/master/fly.toml)」供大家参考。

### 使用 Docker 与 docker-compose 部署

有意思的是，因为 goatcounter 的作者很有坚持，觉得这样单文件的应用容器化反而会增加更多维护成本，所以不提供官方镜像，不过自己在 vps 或者 serverless 平台部署有个镜像还是方便一些，所以用 Github Actions 做了一个构建镜像和上传 Docker Hub 的 CI，有需要的可以使用，对应的 Dockerfile 和 Docker Compose 文件也可以参照这个 [Commit](https://github.com/pseudoyu/goatcounter/commit/b98de9873ee331133a39b409fd4bb00cf55c8a05)，或者直接使用 `pseudoyu/goatcounter` 和 `docker-compose.yml` 文件即可。

```yaml
version: '3'

services:
  goatcounter:
    image: pseudoyu/goatcounter
    ports:
      - 8082:8080
    environment:
      - PORT=8080
      - GOATCOUNTER_DB=sqlite3://data/goatcounter.sqlite3
    volumes:
      - ./data:/data
    restart: unless-stopped
```

### 使用 Zeabur 部署

Zeabur 的部署比起 fly.io 简单很多，大部分的操作都可以使用 Web 界面完成。

#### 注册 zeabur

![zeabur_login](https://image.pseudoyu.com/images/zeabur_login.png)

访问 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 官网，并点击右上角，使用 GitHub 账号授权登录。

#### 创建新项目

![zeabur_new_project](https://image.pseudoyu.com/images/zeabur_new_project.png)

进入主界面后，点击右上角 `创建项目` 按钮

## 博客配置 GoatCounter

上文我们完成的 GoatCounter 服务的部署，现在则需要在我们的博文中加入 GoatCounter 统计组件，以我使用的 Hugo 博客为例。

## 总结

这是我的博客搭建部署系列教程之一，如对数据统计系统、博客内搜索等搭建感兴趣，请持续关注，希望能对大家有所参考。
