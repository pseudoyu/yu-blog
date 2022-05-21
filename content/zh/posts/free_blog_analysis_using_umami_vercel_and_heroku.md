---
title: "从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）"
date: 2022-05-21T16:56:47+08:00
draft: false
tags: ["hugo", "umami", "heroku", "vercel", "blog"]
categories: ["Tools"]
authors:
- "Arthur"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

![umami_dashboard_white](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_dashboard_white.png)

之前写了一篇《[免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）](https://www.pseudoyu.com/zh/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)》，讲述了一下我使用 Serverless 和一些开源项目搭建的博客系统，也开了个系列来记录搭建过程。

前几天看到 [Reorx](https://reorx.com) 写的一篇 《[搭建 umami 收集个人网站统计数据](https://reorx.com/blog/deploy-umami-for-personal-website/)》，他介绍了 [umami](https://umami.is) 这个项目，并使用 [Railway](https://railway.app) 进行无服务搭建部署。

只不过我因为之前部署 [Cusdis](https://cusdis.com) 的时候使用的是 [Heroku](https://www.heroku.com/) 提供的免费 Postgres 数据库服务并用 [Vercel](http://vercel.com/) 进行部署，于是在部署 umami 的时候还是想沿用原来的平台，减少搭建和维护成本。

下文会对具体搭建部署流程做个记录，因为官方支持一键部署方式，整个搭建流程很顺畅。

## 搭建部署说明

### 使用 Heroku 创建 Postgres 数据库

#### 创建 Postgres 数据库

首先注册一个 Heroku 账号，登录成功后，点击右上角按钮创建一个新的应用。

![cretae_app_in_heroku_1](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/cretae_app_in_heroku_1.png)

输入实例名称，地区可以自行选择，我选择的是 United States，点击创建。

![cretae_app_in_heroku_2](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/cretae_app_in_heroku_2.png)

创建完成后，在 Resources Tab 的 Adds-on 中搜索选择 Postgres 数据库。

![add_heroku_postgres](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/add_heroku_postgres.png)

选择 Free Plan 即可，Heroku 中的 Postgres 数据库是免费的，可以持续使用，免去了搭建维护成本。

![heroku_postgres_plan](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/heroku_postgres_plan.png)

创建完成后，在 Setting 中查看 `DATABASE_URL`，后面部署要用到。

![postgres_data_url](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/postgres_data_url.jpeg)

点击新增的 Postgres add-on 跳转进行设置。

![postgres_addon_details](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/postgres_addon_details.png)

进入后，选择 Setting 页面的 View Credentials，并且记录配置参数。

![heroku_credentials](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/heroku_credentials.png)

![postgres_settings](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/postgres_settings.jpeg)

#### 初始化 Postgres 数据库

因为需要初始化数据库，我使用的是 DataGrip 数据库管理工具进行连接，比较方便，也可以通过 Heroku CLI 进行连接和配置。

![postgres_config](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/postgres_config.jpeg)

umami 需要通过官方提供的 [umami/sql/schema.postgresql.sql](https://github.com/mikecao/umami/blob/master/sql/schema.postgresql.sql) 脚本进行初始化。

![postgres_init_script](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/postgres_init_script.png)

执行完成后，数据库有了五张表与初始化数据，可以进行后续部署工作。

### 使用 Vercel 一键部署 umami 服务

#### 部署 umami 服务

创建好数据库实例之后，可以通过 Vercel 一键部署 umami 服务了。

访问 [umami 官方文档](https://umami.is) 的 [Running on Vercel](https://umami.is/docs/running-on-vercel) 模块，有操作说明与一键部署脚本。

![running_on_vercel](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/running_on_vercel.png)

点击一键部署按钮后，会跳转至 Vercel 的一键部署页面，创建 umami 的 Github 仓库。

![vercel_create_umami_repo](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/vercel_create_umami_repo.png)

接下来需要填入之前在部署 Heroku Postgres 实例时记录到 `DATABASE_URL` 参数地址，并且需要填写一个自定义字符串 `HASH_SLAT`。

![vercel_config_umami](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/vercel_config_umami.png)

点击 Deploy 进行部署，等待几分钟后部署完成即可。

![vercel_deploy](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/vercel_deploy.png)

![vecel_deploy_done](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/vecel_deploy_done.png)

#### 访问 umami 服务

部署完成后，点击 Dashboard 或分配的 Vercel 域名访问服务，可以看到 umami 的登录界面。

![umami_login](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_login.png)

初次登录输入默认用户名 `admin` 与默认密码 `umami`，登录成功后，会跳转至 umami 的管理页面，登录后可以点击右上角头像自行修改密码。

![umami_change_password](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_change_password.png)

#### 配置个人网站至 umami 服务

完成基础帐号配置后，点击侧边栏网站 Tab，点击添加网站。

![umami_add_website_1](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_add_website_1.png)

填写网站基本信息，如果勾选共享链接可以生成一个可公开访问的网址，我把它添加了一个书签放在 iPad 主屏幕上，作为一个数据看板也很不错。

![umami_add_website_2](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_add_website_2.png)

#### 配置 umami 脚本至个人博客网站

网站创建完成，获取 umami 脚本。

![get_umami_script](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/get_umami_script.jpeg)

获取后，在个人网站添加 umami 脚本。我使用的是静态博客 Hugo，在主题中的 `<head>` 标签内添加。

![set_umami_script](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/set_umami_script.jpeg)

配置完成部署，即可开始追踪网站数据。

![umami_dashboard_white](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_dashboard_white.png)

#### 配置自定义脚本名称

使用官方的 `umami.js` 脚本名称，可能会被一些过滤规则拦截，因此我们可以自定义脚本名称，实现更准确地网站数据追踪。

官方也提供了便捷的修改方式，可以在 Vercel 中已经部署的 umami 服务中增加 `TRACKER_SCRIPT_NAME` 环境变量，配置为自定义名称。

![umami_script_environment_varible](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/umami_script_environment_varible.png)

配置完成后重新部署，再在个人网站脚本中更改脚本名称即可。

![change_umami_script](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/change_umami_script.jpeg)

#### 配置自定义域名

如果不想要使用 Vercel 提供的 `vercel.app` 域名，可以在 Vercel 中添加自定义域名，按照 Vercel 官方指引对域名提供商进行 `CANME` 等配置。

![set_custom_domain](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/set_custom_domain.png)

例如，我使用的是 [Cloudflare](https://www.cloudflare.com) 托管的域名，需要先添加一下域名解析。

![cloudflare_canme_config](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/cloudflare_canme_config.png)

根据官方说明，Cloudflare 还需要添加一个页面规则，配置完成后即可完成自定义域名配置。

![cloudflare_page_rule](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/cloudflare_page_rule.png)

## 总结

以上就是我们为网站添加 umami 网站统计服务的全流程，配置完成后无需后续维护，可以便捷地通过看板来进行网站数据追踪。这是我的博客搭建部署系列教程之一，请持续关注，希望能对大家有所参考。

## 参考资料

> 1. [umami](https://umami.is)
> 2. [搭建 umami 收集个人网站统计数据](https://reorx.com/blog/deploy-umami-for-personal-website/)
> 3. [Vercel 官方网站](http://vercel.com)
> 4. [Heroku 官方网站](https://www.heroku.com)