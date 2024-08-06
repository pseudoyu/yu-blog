---
title: "使用 GoatCounter 与 Zeabur 搭建网站数据统计系统"
date: 2024-08-06T19:00:42+08:00
draft: false
tags: ["statistic-system", "serverless", "zeabur", "blog", "goatcounter"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## 前言

在「[2024 年了，我的博客有了什么变化](https://www.pseudoyu.com/zh/2024/06/29/what_changed_in_my_blog_2024/)」一文中，我介绍了自己使用 Serverless 平台和一些开源项目搭建的博客系统，也开启了这个系列教程来记录搭建和部署全过程。

本篇是关于统计系统的解决方案。

## 统计系统方案

相比起博客本体和评论系统，我在很长的一段时间其实都没有在意过统计系统（~~主要当时也没人看~~），更加没考虑太多 SEO 或是什么其他推广方向上的事，但后来逐渐发现，其实统计下来的数据并不只是一张好看的可以用来发推的图表，其对于博客的选题、内容都有着很大的参考价值。

其实主流成熟的方案都能够满足基本的需求，即使是免费的 Google Analytics 也完全够用，但在博客发展过程中，我依然因各种原因有过几次迭代，最终使用了 GoatCounter 这一方案。

### splitbee

我最初使用的是一个免费的工具 splitbee，它提供了免费的基础统计额度，有着还不错的界面，并且还支持一些复杂的用户追踪，A/B test 等，但印象里好像只能保留半年的数据，并且每月超过 5000 pv 后就需要升级了，所以后来放弃了。

### Cloudflare + Google Search Console

![cloudflare_web_stats](https://image.pseudoyu.com/images/cloudflare_web_stats.png)

放弃 splitbee 之后，很长一段时间我没有集成额外的统计应用，而是用的 Cloudflare 自带的站点统计，但是发现它其实统计的只是网络总流量，有包括爬虫在内的非常多的无效数据，并且没有精确到路径等细节。

![google_search_console](https://image.pseudoyu.com/images/google_search_console.png)

后来了解到了 SEO 这一概念后，又添加了 [Google Search Console](https://search.google.com/search-console/about) 这一统计维度，这也是目前觉得对我写博文最有意义的数据，主要呈现的是用户在搜索引擎中触达我博客站点的关键词以及通过搜索点击进入我博客的页面路径。

可以看到，一篇「[Warp，iTerm2 还是 Alacritty？我的终端折腾小记](https://www.pseudoyu.com/zh/category/tools/)」为我带来了许多访客，而关于博客搭建、智能合约开发也是大部分从搜索引擎来的自然用户对我博客的第一印象。

### Umami + Supabase + Netlify

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

但是上述两者依然只能看到网站整体的数据，想精确到某篇文章在一段时间的表现或者文章发布后的实时访问数据，依然需要一个统计系统，我在看了 Reorx 的一篇「[搭建 umami 收集个人网站统计数据 | Reorx’s Forge](https://reorx.com/blog/deploy-umami-for-personal-website/)」选择使用了 umami 这一开源、易自部署的统计系统，界面简洁，功能易用，很方便集成到自己的博客系统中。

使用了一年半，一直倒没出现什么问题，，只不过可能因为自己用得比较早，在一次大版本更新的时候数据库 Migration 脚本出现了不兼容的字段更新，其实有点不理解这样量级的开源项目为什么会出现这样的问题，也看到 issue 中有很多其他用户有同样的诉求，但最终并没有给出一个比较好的解决方案。

但其实最大的问题是一个统计系统依赖了两个平台，部署和维护上都还是有些太重了。当数据库或是 Netlify 任一出现问题或需要迁移时，会带来许多额外的成本。于是前段时间在更新博客评论系统的时候，想着干脆就一起更换为更轻量的 GoatCounter。

### GoatCounter + Zeabur

![goatcounter_stats](https://image.pseudoyu.com/images/goatcounter_stats.png)

这个小众的统计系统是我在看 Reorx 的博客代码更新的时候偶然发现的，一下子被这种 Retro Internet 的风格所吸引，几乎没有任何多余的按钮，功能却很完备，而且使用的是 go 单二进制文件 + sqlite 数据库单文件的架构，轻量而易于部署，于是打算迁移。

其实我自己的 GoatCounter 是部署在 [fly.io](https://fly.io/) 上的，但我在上一篇 Remark42 的文章中已经非常详细地介绍了 fly 的操作说明，不想有太多重复，刚好最近又在重度使用 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 这一 Serverless 平台，于是本文将以 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 为例，方式同样适用于其他类似平台。

我也在下文的 Zeabur 部署方案之后提供了 fly.io 和在 VPS 上使用 docker-compose 部署的配置文件，供大家参考。

## GoatCounter 部署说明

GoatCounter 本身代码开源 —— 「[GitHub - arp242/goatcounter](https://github.com/arp242/goatcounter)」，文档清晰易读，可以根据自己的实际需求进行配置。GoatCounter + Zeabur 的方案仅牵扯到单个服务，数据库使用的是 sqlite 挂载于 volume 中，所以部署起来非常简单。

### 使用 Zeabur 部署

[Zeabur](https://zeabur.com?referralCode=pseudoyu) 对于容器应用的部署是需要 Developer Plan 的，5 美元/月，但是像这样的镜像服务整体用量和费用都较低，每月的额度足够部署非常多服务，可以酌情选择。整体部署流程比起 fly.io 简单很多，所有操作都可以使用 Web 界面完成，不需要额外安装命令行工具等。

#### 注册 zeabur

![zeabur_login](https://image.pseudoyu.com/images/zeabur_login.png)

访问 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 官网，并点击右上角，使用 GitHub 账号授权登录。

#### 创建新项目

![zeabur_new_project](https://image.pseudoyu.com/images/zeabur_new_project.png)

进入主界面后，点击右上角 `创建项目` 按钮。

![zeabur_hk_region](https://image.pseudoyu.com/images/zeabur_hk_region.png)

我选择了香港的 AWS 机房，不同机房的访问速度、性能和价格会有一些差异，可以根据自己的需求进行选择。

#### 配置镜像部署

![zeabur_build](https://image.pseudoyu.com/images/zeabur_build.png)

在下一步中选择 Docker 容器镜像进行部署。

![zeabur_docker_custom_config](https://image.pseudoyu.com/images/zeabur_docker_custom_config.png)

由于我们使用的是自己构建的镜像，官方也没有上线 GoatCounter 模板，因此我们点击选择自定义。

![zeabur_prebuilt_edit_toml](https://image.pseudoyu.com/images/zeabur_prebuilt_edit_toml.png)

这一步可以自己在界面上填写各种配置项，但可能由于我习惯了 fly.io 的文件配置模式，我选择左下角的 `编辑 TOML 文件`，大家也可以直接复制我的配置文件并直接修改。

```toml
name = "yu-goatcounter"

[source]
image = "pseudoyu/goatcounter"

[[ports]]
id = "web"
port = 8080
type = "HTTP"

[[volumes]]
id = "goatcounter-data"
dir = "/data"

[env]
PORT = { default = "8080" , expose = true }
GOATCOUNTER_DB = { default = "sqlite3://data/goatcounter.sqlite3" , expose = true }
```

![zeabur_prebuilt_goatcounter_toml](https://image.pseudoyu.com/images/zeabur_prebuilt_goatcounter_toml.png)

配置好后点击右下角部署按钮即可。

#### 部署完成

![yu-goatcounter_project](https://image.pseudoyu.com/images/yu-goatcounter_project.png)

点击部署后，等待片刻，会有一个生成的项目默认名称，可以在左上角的设置中去修改为可读性较强的名称，如 `yu-goatcounter`。

#### 配置自定义域名

![zeabur_create_domain](https://image.pseudoyu.com/images/zeabur_create_domain.png)

服务部署完成后，我们需要进行域名绑定才能通过公网访问网站，Zeabur 提供了免费的二级域名 `xx.zeabur.app`，也可以绑定自己的域名。

![zeabur_custom_domain](https://image.pseudoyu.com/images/zeabur_custom_domain.png)

其中生成域名可直接使用，无须进行其他配置，如 `goatcounter.zeabur.app`；而如果使用的是自定义域名，则需要在自己域名管理后台添加 CNAME 记录，指向格式为 `xxx.cname.zeabur-dns.com` 的机房地址。

![cloudflare_goatcounter_config](https://image.pseudoyu.com/images/cloudflare_goatcounter_config.png)

例如我的域名托管在 Cloudflare 上，添加的 CNAME 记录如上图所示，有去问过官方，说如果选 AWS HK 机房的话可以不使用 Cloudflare 的代理，速度理论上会更快，可以根据自己的需要酌情配置。

此外，如果你选择的是华为云机房，则需要域名备案并且额外新增一条 TXT 记录，可以根据提示进行操作。

![zeabur_custom_domain_success](https://image.pseudoyu.com/images/zeabur_custom_domain_success.png)

显示绿色则为配置成功，至此我们的 GoatCounter 服务就部署完成了。

#### 数据备份

我们在配置时候有这么一段

```toml
[[volumes]]
id = "goatcounter-data"
dir = "/data"
```

功能是将容器内的 `/data` 目录（即我们的 sqlite 数据库存在的位置）挂载到一个 id 为 `goatcounter-data` 的存储卷，如果不挂载存储卷的话，容器重启或重新部署数据将会丢失。

关于存储卷这一点 Zeabur 的界面上没有很直观的显示和管理操作，以至于我总是怀疑自己的配置是否生效。

![zeabur_add_goatcounter_backup](https://image.pseudoyu.com/images/zeabur_add_goatcounter_backup.png)

研究了半天发现可以先在设置中暂停服务，然后在上面的备份模块新增一个备份，点击下载后可以在本地看到我们备份文件，目录层级如下：

```plaintext
data/
└── goatcounter-data
    └── goatcounter.sqlite3
```

这样则能表示我们的数据成功持久化了，希望 Zeabur 能在界面上有更直观的显示。

### 使用 fly.io 部署

纯免费的方案依然可以参照我提到的这篇「[从零开始搭建你的免费博客评论系统（Remark42 + fly.io）](https://www.pseudoyu.com/zh/2024/07/22/free_commenting_system_using_remark42_and_flyio/)」，仅在 `fly.toml` 配置部分不同，我也提供的我所使用的配置文件 —— 「[fly.toml](https://github.com/pseudoyu/goatcounter-on-fly/blob/master/fly.toml)」供大家参考。

### 使用 Docker 与 docker-compose 部署

有意思的是，因为 goatcounter 的作者很有坚持，觉得这样单文件的应用容器化反而会增加更多维护成本，所以不提供官方镜像，不过自己在 vps 或者 serverless 平台部署有个镜像还是方便一些，所以我使用 Github Actions 做了一个构建镜像和上传 Docker Hub 的 CI，有需要的可以使用，对应的 Dockerfile 和 Docker Compose 文件也可以参照这个 [Commit](https://github.com/pseudoyu/goatcounter/commit/b98de9873ee331133a39b409fd4bb00cf55c8a05)，或者直接使用 `pseudoyu/goatcounter` 和 `docker-compose.yml` 文件即可。

```yaml
version: '3'

services:
  goatcounter:
    image: pseudoyu/goatcounter
    ports:
      - 8080:8080
    environment:
      - PORT=8080
      - GOATCOUNTER_DB=sqlite3://data/goatcounter.sqlite3
    volumes:
      - ./data:/data
    restart: unless-stopped
```

## GoatCounter 配置说明

上文我们完成了 GoatCounter 服务的部署，现在就可以通过我们生成/自定义的域名访问到我们的统计系统服务了，如我是通过 `https://goatcounter.pseudoyu.com` 进行访问的。

![goatcounter_create_user](https://image.pseudoyu.com/images/goatcounter_create_user.png)

第一次登录需要创建一个用户，填写邮箱、密码点击 `Create` 即可。

![goatcounter_dashboard_success](https://image.pseudoyu.com/images/goatcounter_dashboard_success.png)

登录成功后，当前还没有数据，会提示一个脚本，后续在我们博客使用的配置中会用到。

## 博客配置 GoatCounter

跟着上文我们完成了 GoatCounter 服务的部署和基础配置，现在则需要在我们的博文中加入统计组件，以我使用的 Hugo 博客为例。

```html
<script data-goatcounter="https://goatcounter.pseudoyu.com/count"
        async src="//goatcounter.pseudoyu.com/count.js"></script>
```

![add_goatcounter_script_in_hugo](https://image.pseudoyu.com/images/add_goatcounter_script_in_hugo.png)

将上述代码加到我 hugo 主题的 `head` 中即可，如我的 Hugo 主题在 `layouts/partials/head.html` 这一文件，不同主题或是不同 SSG 框架位置有所不同但大同小异。

有一点要注意的是， goatcounter 会忽略来自 `localhost` 的请求以避免在本地预览时造成太多脏数据，因此在本地调试时是看不到数据的，需要部署网页才能看到访问数据。

![final_display_of_goatcounter](https://image.pseudoyu.com/images/final_display_of_goatcounter.png)

收集了数据后的效果大致如上图所示，还可以在 GoatCounter 界面中设置一些配置项、新增网页、查看详细数据等，包括还可以显示每个页面的访问计数等，可以自己根据文档进行探索。

## 总结

至此我们的博客统计系统就搭建完成了！本文是我的博客搭建部署系列教程之一，博客主题体部分都已经完成了，剩下只是一些例如博客内搜索等细节体验优化，希望能对大家有所参考。
