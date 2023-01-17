---
title: "免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）"
date: 2022-03-24T01:19:28+08:00
draft: false
tags: ["hugo", "github", "github action", "cusdis", "vercel", "cloudflare", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## 前言

[Pseudoyu](https://www.pseudoyu.com) 是我的个人博客网站，最早使用 [WordPress](https://wordpress.com/) 搭建在自己的 Vultr vps 上，因为网络访问比较慢所以迁移到了腾讯云服务器上并且进行备案，虽然访问速度有提升，但是发布博客的流程很繁琐，服务器的维护长期也是一笔不小的开支。

因此，一直在探索能够既能保障国内外访问体验，又能够托管在一些平台上，实现部署和发布流程的最优化体验。后来也一直不断在改善博客系统搭建和发布流程，迄今为止对自己的全流程解决方案还是比较满意的，虽然部署和搭建上需要进行一些配置，但后续更新维护都很方便，因此，本文将这套免费、开源的个人博客系统搭建及部署解决方案进行全流程记录，希望对大家有所帮助。

## 解决方案

### 博客平台

目前已经有很多比较成熟的博客平台，如前文所提到的 WordPress，虽然功能强大，但对于个人博客站点来说有些太重了，~~也不够酷~~，经过一番调研，最后选择了 [Hugo](https://gohugo.io) 这个静态网站生成器。

Hugo 是用 Go 实现的博客工具，采用 Markdown 进行文章编辑，自动生成静态站点文件，支持丰富的主题配置，也可以通过 js 嵌入像是评论系统等插件，高度定制化。除了 Hugo 外， 还有 Gatsby、Jekyll、Hexo、Ghost 等选择，实现和使用都差不多，可以根据自己的偏好进行选择。

![pseudoyu_homepage](https://image.pseudoyu.com/images/pseudoyu_homepage.png)

因为 Hugo 开源社区中 [hugo-theme-den](https://github.com/shaform/hugo-theme-den) 完全在我的审美上，所以我选择了 Hugo 并在这个主题基础上进行了一些个人定制化改造和配置，满足了自己的需求。

### 博客托管

静态博客需要托管在一个平台上才能够实现外部访问，可以是自己的 vps 主机，也可以是 [GitHub Pages](https://pages.github.com)，或者是 [Vercel](http://vercel.com) 这样的 Serverless 平台，后两者都可以通过 GitHub 仓库进行关联。

我选择了 GitHub Pages 这种方式，完全免费且和 GitHub 代码仓库无缝对接，能够满足我博客源文件备份和版本管理的需求，还可以通过强大且同样免费的 [GitHub Action](https://github.com/features/actions) 实现各种 CI/CD 的功能，如提交/更新博客源文件后自动构建生成博客静态文件并推送到 GitHub Pages 仓库进行部署，还可以配合一些定时任务实现自我介绍页面更新等功能。

### 博客域名

使用 GitHub Pages 生成网站会自动分配一个 xxx.github.io 的默认域名，通过这个域名就可以直接对生成的博客网站进行访问，也可以通过域名解析配置自己的域名，如我的网站就是解析了 [pseudoyu.com](https://www.pseudoyu.com) 这个域名。

我的域名是在 [NameSilo](https://www.namesilo.com) 购买的，并通过 [Cloudflare](https://www.cloudflare.com) 平台进行 CDN 加速，提升访问体验，并实现了域名重定向等功能，关于博客访问优化这一点后续会单独讲解。

**[2022-05-29 更新]**

我后来为了方便管理，把 NameSilo 域名迁移到了 Cloudflare，大家可以直接在 Cloudflare 上购买，教程包含在《[Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)》中。

### 访客分析

作为一个持续更新运营的博客平台，我们一定很好奇我们哪篇文章阅读量最高、哪个关键词检索最频繁等，帮助我们专注在更有价值的内容创作与分享上，类似的工具也很多，我选择了 [splitbee](https://splitbee.io) 与 [Google Console](https://search.google.com/search-console) 来统计分析我的访客信息与搜索权重，此外，[Cloudflare](https://www.cloudflare.com) 也能够对网络流量进行分析，不过因为有很多网络无关流量，如爬虫等，所以参考性没有前两者强。

![splitbee_statistics](https://image.pseudoyu.com/images/splitbee_statistics.png)

![google_console_performance](https://image.pseudoyu.com/images/google_console_performance.png)

![cloudflare_statistics](https://image.pseudoyu.com/images/cloudflare_statistics.png)

**[2022-05-21 更新]**

除了上述直接服务的平台外，我还部署了一个可代替 [Google Analytics](https://analytics.google.com) 的开源服务 [umami](https://umami.is)，实现了访客数据的实时监控，教程为：《[从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)》。

### 评论系统

一个博客系统当然需要评论系统，像 WordPress 这种自身具备了评论插件，而静态博客则需要自己对接一些评论系统，我最开始选择的是第三方的 [Disqus](https://disqus.com)，简单易用，但是会自带很多广告推广，也不够简约，后来选择了 [Randy](https://lutaonan.com) 的 [Cusdis](https://cusdis.com)，一个轻量级的开源评论系统解决方案（从名字看也是深受 Disqus 其害忍不住自己开坑了哈哈），我通过 Vercel 自建，并链接了 [Heroku](https://www.heroku.com) 的免费 [PostgreSQL](https://www.postgresql.org) 数据库进行评论数据存储，实现了免费、稳定的评论系统，还支持邮件推送、Telegram Bot 提醒/快捷回复等功能。

![cusdis_overview](https://image.pseudoyu.com/images/cusdis_overview.png)

**[2022-05-24 更新]**

Cusdis 部署在 Railway 平台教程已更新：《[轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)》。

### 图片管理

日常发布的文章中可能会涉及很多图片，将图片存储在静态博客源项目仓库中的话会使项目过于庞大，并且很难二次使用和管理，因此，我同样选择了 GitHub 作为图床工具，并使用 [PicGo](https://molunerfinn.com/PicGo/) 客户端进行图床管理，在上传前使用 [TinyPNG](https://tinypng.com) 进行压缩，并使用 [jsDelivr](https://www.jsdelivr.com) 服务为 GitHub 图床进行加速，这样就可以将所有图片存储在 GitHub 图床仓库，文章中以外链的方式嵌入图片。

## 发布流程

通常 GitHub Pages 发布博客需要本地 `hugo` 命令生成静态站点文件目录，`cd` 到 `public` 目录，并使用 `git add`、`git commit`、`git push` 等命令提交到 GitHub Pages 仓库，实现博客的发布，因为每次更新都需要进行重复操作，且博客源 Markdown 文件无法进行很好的备份和版本管理。

因此，我建立了一个博客源文件仓库，通过 GitHub Action 实现了一套自动化发布流程，仅需将 Hugo 博客源文件上传至 GitHub 仓库，会自动触发 CI 生成静态站点文件并推送到 GitHub Pages 仓库。

**[2022-05-29 更新]**

Hugo 搭建与 GitHub Action 配置教程已更新：《[Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)》

## 总结

以上就是我的个人博客解决方案，前期搭建有些繁琐，但一番折腾后，完美实现了我的需求，关于整个过程的详细步骤，~~我将会分多篇文章进行讲解，请持续关注~~，希望能够对大家有所帮助。

**[2022-06-02 更新]**

系列教程核心部分已完成：

- [从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
- [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)
- [Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)

除此之外，如果不想使用 Hugo 这类静态博客，还可以通过 Ghost 来比较方便地搭建一下：

- [Ghost 5.0 来了，使用 Digital Ocean 一键部署吧](https://www.pseudoyu.com/zh/2022/05/29/deploy_ghost_5_on_digital_ocean_vps/)

## 参考资料

> 1. [Hugo 官方网站](https://gohugo.io)
> 2. [hugo-theme-den 主题仓库](https://github.com/shaform/hugo-theme-den)
> 3. [GitHub Pages 官方网站](https://pages.github.com)
> 4. [GitHub Action 官方网站](https://github.com/features/actions)
> 5. [Vercel 官方网站](http://vercel.com)
> 6. [Cusdis 官方网站](https://cusdis.com)
> 7. [Heroku 官方网站](https://www.heroku.com)
> 8. [PicGo 官方网站](https://molunerfinn.com/PicGo/)
> 9. [splitbee 官方网站](https://splitbee.io)
> 10. [Google Console 官方网站](https://search.google.com/search-console)
> 11. [Cloudflare 官方网站](https://www.cloudflare.com)
