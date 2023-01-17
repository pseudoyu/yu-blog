---
title: "轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）"
date: 2022-05-24T21:47:47+08:00
draft: false
tags: ["hugo", "cusdis", "railway", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

![cusdis_intro](https://image.pseudoyu.com/images/cusdis_intro.png)

之前写了一篇《[免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)》，讲述了一下我使用 Serverless 和一些开源项目搭建的博客系统，也开了个系列来记录搭建过程。

本篇是关于博客评论系统的解决方案，我最早使用的博客评论系统是~~万恶的~~ [Disqus](https://disqus.com)，一个笨重且会收集用户隐私的知名评论系统，因为加载比较慢，且免费版本经常会附带一些广告，实在难以忍受，于是换成了另一个基于 GitHub issues 的评论系统 [utterances](https://utteranc.es)，它会为每篇文章生成一个 issue，将，用户通过授权 GitHub 登录来对 issue 发表评论。这种方式的好处是只需要授权一个 [utterances-bot](https://github.com/utterances-bot) 来进行管理，无需自己部署服务，维护数据库等。但是用了一段时间后，觉得有几点不足：

1. 基于 GitHub API 进行评论管理，如之后接口变动或对这类利用 issue 进行评论的方式进行限制，会不太稳定
2. 读者必须要授权 GitHub 登录，非技术人员或使用移动端阅读的读者使用起来很不方便
3. 会将 GitHub 仓库弄得较乱，也不方便后续迁移到其他系统

经过一番调研 [Randy](https://lutaonan.com) 的 [Cusdis](https://cusdis.com/) 很合我的心意。Cusdis 是一个注重数据隐私的开源的评论系统，十分轻量，经过 gzipped 后大约只有 5kb，从名字来看也知道开发者也是难以忍受 Disqus，自己做了一个替代版，因此它也是支持 Disqus 历史数据导入的，很贴心。

虽然这是一个开发早期的项目，但是已经提供了电子邮件通知以及通过 Webhook 联动 Telegram 等方式进行评论提醒，对使用者来说很方便进行管理。Cusdis 提供了免费托管服务与自行部署两种方式，如果不想折腾可以直接用作者提供的服务。自行部署则需要服务器与一个 Postgre SQL 实例，我们主要示范一下自行部署方式。

因为在上一篇 《[从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)》 中我使用的是 [Vercel](http://vercel.com/) 和 [Heroku](https://www.heroku.com/) 进行搭建的，作为一个爱折腾的人，这个评论系统我们就用 [Railway](https://railway.app/) 来搭建部署。

Railway 和 Vercel 类似，也是一个 PaaS 平台，能够支持多种语言项目的部署。对于个人项目来说，它每月提供的 5 美元免费额度非常够用，实测了一下，把之前的 [umami 网站数据统计系统](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/) 连同 Postgre SQL 数据库实例部署在 Railway 平台，大约一个月 0.7 美元，对于个人使用来说完全足够。

![railway_price](https://image.pseudoyu.com/images/railway_price.png)

比起 Vercel，它同时支持部署数据库实例，可以将数据库与实例一起部署在单个项目中，减少搭建维护成本。下文会对具体搭建部署流程做个记录，因为官方支持 Railway 一键部署方式，整个搭建流程很顺畅。

## 搭建部署说明

### 使用 Railway 一键部署服务与数据库实例

首先注册一个 Railway 账号，可以用我的[邀请链接](https://railway.app?referralCode=J0F5LQ)。注册登录完成后，点击右上角 New Project 新建项目。

![railway_dashboard](https://image.pseudoyu.com/images/railway_dashboard.png)

然后输入 Cusdis 进行搜索，点击出现的项目即可开始部署。前几步也可以通过点击 [Cusdis 项目仓库](https://github.com/djyde/cusdis) 中的 `Deploy on Railway` 按钮进行一键部署。

![new_cusids_starter](https://image.pseudoyu.com/images/new_cusids_starter.png)

开始部署前，需要手动填入三个环境变量：

![deploy_cusdis_on_railway](https://image.pseudoyu.com/images/deploy_cusdis_on_railway.png)

1. USERNAME: 用来登录的账户
2. PASSWORD: 用来登录的密码
3. JWT_SECRET: 一个随机字符串

其他一些环境变量已经预先设置默认值，请不要自行修改。

1. NEXTAUTH_URL: `${{ RAILWAY_STATIC_URL }}`
2. DB_TYPE: `pgsql`
3. DB_URL: `${{ DATABASE_URL }}`
4. PORT: `3000`

点击部署后，等待完成即可，会自动部署服务并初始化数据库。

![cusdis_deploy_done](https://image.pseudoyu.com/images/cusdis_deploy_done.jpg)

### 配置 Cusdis 脚本至个人博客

部署完成后，点击 cusdis 服务生成的链接，点击访问服务 Dashboard。

![cusdis_login](https://image.pseudoyu.com/images/cusdis_login.png)

此处输入部署前配置的用户名与密码，点击登录。登录完成后，点击 Dashboard，进入项目配置页面。

初次登录会弹窗提示需要配置第一个网站，输入网站名称即可完成添加。后续当我们需要添加网站时，点击侧边栏 New Website，填写网站名称即可完成添加。

![add_new_website](https://image.pseudoyu.com/images/add_new_website.png)

因为我已经配置了自己的网站，所以界面会有之前的评论记录。

![cusdis_dashboard](https://image.pseudoyu.com/images/cusdis_dashboard.png)

下面我们点击上方 Embed Code，复制弹窗中的代码。

![cusdis_embed_code](https://image.pseudoyu.com/images/cusdis_embed_code.jpg)

这部份代码需要根据你所用的博客网站类型不同进行部分修改，具体可参考[官方文档](https://cusdis.com/doc#/) 的 Integration 模块进行配置。

我所用的是 [Hugo](https://gohugo.io)，配置如下：

```html
<div id="cusdis_thread"
  data-host="xxx"
  data-app-id="xxx"
  data-page-id="{{ .File.UniqueID }}"
  data-page-url="{{ .Permalink }}"
  data-page-title="{{ .Title }}"
>
</div>

<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>
<script async defer src="xxx"></script>
```

其中的 `data-host`，`data-app-id` 等都需要以刚复制出的 Embed Code 内容为准。其中 `<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>` 主要实现了汉化，不同语言支持详见[文档 i18n 模块](https://cusdis.com/doc#/advanced/i18n)。

修改后，将其添加到博客的相应位置（一般在最下方），配置部署后，即可看到评论框，呈现效果如下：

![cusdis_display](https://image.pseudoyu.com/images/cusdis_display.png)

### 配置自定义域名

Railway 部署自动生成的域名比较长，且有一些字符，不方便记忆。我们可以在 Railway 中为项目配置自定义域名。

![railway_custom_domain](https://image.pseudoyu.com/images/railway_custom_domain.jpg)

填入想要配置的域名/二级域名后，根据官方提示添加 DNS 解析。

![railway_domain_dns](https://image.pseudoyu.com/images/railway_domain_dns.jpg)

例如，我使用的是 [Cloudflare](https://www.cloudflare.com) 托管的域名，需要先添加一下域名 CNAME 解析。

![cloudflare_domain_dns](https://image.pseudoyu.com/images/cloudflare_domain_dns.jpg)

至此，我们的部署已经完成，可以通过域名访问管理后台，进行评论审核管理等。

### 更新项目

如前文所述，Cusdis 还是一个正在开发成长的项目，我们想第一时间更新作者发布的新功能。Railway 提供了十分便捷的上游分支管理功能，可以设置项目的父项目，点击即可拉取最新更新，很方便。

![railway_update_project](https://image.pseudoyu.com/images/railway_update_project.png)

## 总结

以上就是我们为网站添加 Cusdis 评论系统的全流程，配置完成后无需后续维护，可以便捷地通过看板来进行网站管理与评论审核，且数据存储在 Postgre SQL 数据库实例中，方便导出备份与迁移。这是我的博客搭建部署系列教程之一，请持续关注，希望能对大家有所参考。

## 参考资料

> 1. [Cusdis 项目官网](https://cusdis.com)
> 2. [Railway 官方网站](https://railway.app)
> 3. [搭建 umami 收集个人网站统计数据](https://reorx.com/blog/deploy-umami-for-personal-website/)
