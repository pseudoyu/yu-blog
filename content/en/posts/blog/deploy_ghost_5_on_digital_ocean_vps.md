---
title: "Ghost 5.0 来了，使用 Digital Ocean 一键部署吧"
date: 2022-05-29T14:21:12+08:00
draft: false
tags: ["blog", "ghost", "digital ocean", "vps", "self-host"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

我是一个静态博客与 Serverless 支持者，自己的[个人博客](https://www.pseudoyu.com)与一些[知识库项目](https://www.pseudoyu.com/blockchain-guide)也都是通过 [hugo](https://gohugo.io) 生成并托管在 [GitHub Pages](https://pages.github.com) 上的。这种方式很方便进行版本管理与部署维护，但对于非技术的人来说，通过命令行 git 操作的方式也有些过于 geek，牵扯到多人协作等场景也不太方便。

上周有个前同事（非技术）让我帮忙搭建一个门户网站，主要展示一下公司信息、发布一些资讯、专题、工具等，出于易用性等考虑，也刚好看到 [Ghost](https://ghost.org) 官方发布了 5.0 版本，支持了很多强大的功能，如邮件订阅、数据分析等，且可以自部署，所以考虑了这个方案，下文记录一下安装与部署流程。

## Ghost 5.0

![ghost_5_intro](https://image.pseudoyu.com/images/ghost_5_intro.jpg)

Ghost 是一个非常老派的博客工具，自 2013 年原型发布以来已经经过了 9 年的发展完善，于最近刚推出 5.0 版本，很适合个人、独立发布平台等。5.0 版本中，有以下特性更新：

* 支持更强大的订阅功能，如订阅分级等
* 支持多个邮件订阅，修改设计更加方便
* 支持发布优惠活动，也有更强大的用户分析面板
* 原生支持视频、博客、GIF、电商产品、NFT 等
* 发布更多新主题
* 优化性能 20%+
* ...

Ghost 官方支持多种部署方式，如 Ghost(Pro) 托管、Docker 镜像、服务器安装等，而因为 Ghost 生成环境依赖 Ubuntu，Node，MySQL 等环境，如果需要自己单独搭建会比较麻烦，且维护成本也较高。经过一番调研，根据官方文档的安装说明，Digital Ocean 是 Ghost 的官方云托管合作伙伴，提供了一键部署安装的方式，简单便捷。

## 安装部署说明

### 域名购买

作为一个对外发布的网站，我们需要购买一个域名并配置解析，指向我们网站所在的服务器，才能让外界以比较方便的方式访问。域名购买平台很多，我用过的有 [Cloudflare](https://www.cloudflare.com)、[NameSilo](https://www.namesilo.com)、[GoDaddy](https://www.godaddy.com) 等，我最后常用的还是 Cloudflare，因为其同时还提供了 CDN、网站数据分析、定制规则等强大功能。

首先我们需要注册一个 Cloudflare 账户，完成并登录后，选择左侧边栏的“注册域”，并搜索自己想注册的域名。

![cloudflare_register_domain](https://image.pseudoyu.com/images/cloudflare_register_domain.png)

选择了心仪的域名后，点击并选择购买时限并填写个人信息。

![cloudflare_register_domain_choose](https://image.pseudoyu.com/images/cloudflare_register_domain_choose.png)

选择付款方式，建议可以选择自动续订，以免忘记续费。

![cloudflare_register_domain_payment](https://image.pseudoyu.com/images/cloudflare_register_domain_payment.png)

类型选择 Personal 即可，并点击完成购买。

![cloudflare_register_done](https://image.pseudoyu.com/images/cloudflare_register_done.png)

等待 Cloudflare 处理后即可查看信息。

![cloudflare_domain](https://image.pseudoyu.com/images/cloudflare_domain.jpg)

### Digital Ocean ssh 配置

因为我们后续需要访问 Digital Ocean 的主机，我们需要先注册一个帐号，并配置我们的 ssh key，以便免密登录。

![digital_ocean_add_key](https://image.pseudoyu.com/images/digital_ocean_add_key.png)

输入我们的 ssh key，点击添加即可。

![digital_ocean_ssh_config](https://image.pseudoyu.com/images/digital_ocean_ssh_config.png)

### 一键创建 Ghost Droplet

如上文所述，Ghost 提供了在 Digital Ocean 上一键创建 Droplet 的支持，我们可以访问[安装说明文档](https://ghost.org/docs/install/)，点击 Digital Ocean 图标进行跳转。

![ghost_use_digital_ocean](https://image.pseudoyu.com/images/ghost_use_digital_ocean.png)

我们也可以在 Digital Ocean 镜像市场中搜索选择，点击右上角创建。

![digital_ocean_market_ghost](https://image.pseudoyu.com/images/digital_ocean_market_ghost.png)

根据官方说明，选择 5 美元/月套餐配置已经足够，后续有更高需求也可以一键扩容（注：如先选择了高配置，无法进行降级）。

![digital_ocean_ghost_config](https://image.pseudoyu.com/images/digital_ocean_ghost_config.png)

选择主机实例地区，我选择的是美国区域，可以根据需求自己选择，并选择上文操作添加到 ssh 配置，方便之后进行访问。

![digital_ocean_ghost_region](https://image.pseudoyu.com/images/digital_ocean_ghost_region.png)

完成配置选择后，我们选择数量、名称并点击 Create Droplet 即可。

![digital_ocean_ghost_create](https://image.pseudoyu.com/images/digital_ocean_ghost_create.png)

等待 Digital Ocean 准备主机，约几分钟就可以完成。

![digital_ocean_ghost_done_hide](https://image.pseudoyu.com/images/digital_ocean_ghost_done_hide.jpg)

### 配置域名解析

因为 Ghost 需要进行 https 配置，且出于方便用户进行访问等考虑，我们需要对新创建的服务器进行 DNS 解析。

登录 Cloudflare，选择我们刚注册的域名，选择左侧 DNS 标签栏，配置 A 解析（一般需要配置 root 解析与 www 解析），其他域名托管网站操作也大同小异。

![cloudflare_dns_config](https://image.pseudoyu.com/images/cloudflare_dns_config.jpg)

### 域名 SSL/TLS 配置（可选）

如果使用 Cloudflare 进行托管，可以选择配置 SSL/TLS 加密模式为完全，可以更加保障安全性。

![cloudflare_ssl_config](https://image.pseudoyu.com/images/cloudflare_ssl_config.png)

### 一键安装 Ghost 服务

完成域名解析后，我们可通过 Digital Ocean 控制台或其他终端工具连接到主机，进行一键安装。

![ghost_one_key_install](https://image.pseudoyu.com/images/ghost_one_key_install.jpg)

Enter 后脚本会自动开始安装服务及各项依赖。

![ghost_start_install](https://image.pseudoyu.com/images/ghost_start_install.png)

安装是命令行交互式，我们仅需要输入两个自定义配置：

- Enter your blog URL
- Enter your email(For SSL Certificate)

这两个地方输入自己的域名与邮箱，等待安装完成即可。

![ghost_install_config](https://image.pseudoyu.com/images/ghost_install_config.jpg)

### 访问网站

等待脚本执行完成后，我们就可以访问 Ghost 网站了。

- https://`{your domain}`/ghost，后台管理界面
- https://`{your domain}`，网站地址

第一次登录会需要注册一个管理员帐号，注册完成后登录即可。

![ghost_login](https://image.pseudoyu.com/images/ghost_login.png)

登录后即可看到非常美观的 Ghost 后台管理页面。

![ghost_dashboard](https://image.pseudoyu.com/images/ghost_dashboard.png)

Ghost 提供了非常多可定制化配置选项，可以根据自己网站的需求进行调整。

![ghost_setting](https://image.pseudoyu.com/images/ghost_setting.png)

## 总结

以上就是我使用 Ghost 官方推荐的 Digital Ocean 托管方式部署自己的 Ghost 网站，Ghost 升级 5.0 后已经能满足大部分网站的需求，且对商业化、数据处理有了更好的支持，对于个人博客和小团队来说都是比较好的选择，希望对大家有所帮助。

## 参考资料

> 1. [Ghost 官网](https://ghost.org)
> 2. [Digital Ocean 官网](https://www.digitalocean.com)
> 3. [免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)
> 4. [从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
> 5. [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)
