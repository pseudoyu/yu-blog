---
title: "使用 WebP Cloud 与 Cloudflare WAF 为你的图床添加隐私和版权保护"
date: 2024-07-02T06:12:47+08:00
draft: false
tags: ["image-hosting", "cloudflare", "waf", "webp cloud", "serverless", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## 前言

在「[从零开始搭建你的免费图床系统 （Cloudflare R2 + WebP Cloud + PicGo）](https://www.pseudoyu.com/zh/2024/06/30/free_image_hosting_system_using_r2_webp_cloud_and_picgo/)」一文中，我用 Cloudflare R2 搭建了一个免费的图床系统，并通过 [WebP Cloud](https://webp.se/) 进行图片优化。

在使用 WebP Cloud 的过程中，我发现它还提供了自定义 Proxy User Agent、水印等功能，于是萌生了一个想法，是不是可以通过 WebP Cloud 对我的图床源站链接进行保护，使 WebP Cloud 的代理链接成为访问我所有图片的唯一入口，并统一添加我的专属版权水印。

本文是对这一实践的记录，也算是图床搭建番外篇了。

## 需求分析

![webp_proxy_info](https://image.pseudoyu.com/images/webp_proxy_info.png)

我目前的图床方案是将图片都托管在 Cloudflare R2 上，并且通过 WebP Cloud 这一强大的图片代理工具进行访问优化，但其实使用代理链接 `image.pseudoyu.com` 与源站链接 `images.pseudoyu.com` 都可以访问我的图片，只是前者被优化过，后者则是我保存的原图。

### 隐私保护

事实上我们通过手机、数码相机等设备拍摄的照片都会携带 EXIF(EXchangeable Image File Format) 信息，通常会包含拍摄设备、时间和地点等敏感信息，我们可以通过一些技术方式手动去除这些元数据，但操作十分繁琐且容易遗漏。

![webp_exif_remove](https://image.pseudoyu.com/images/webp_exif_remove.png)

我查阅了一下 WebP Cloud 的文档，发现它果然提供自动擦除 EXIF 信息的功能，无须额外配置操作，但其实访客依然可以可以通过 Cloudflare R2 暴露出的源站信息访问到原图，为了避免这一点，我需要限制用户只能通过 WebP Cloud 代理链接进行请求，访问 Cloudflare R2 源站链接时获取不到任何有用信息。

### 版权保护

![randy_pic_copyright](https://image.pseudoyu.com/images/randy_pic_copyright.png)

之前在推上看到 Randy 自己拍的 desk setup 图被盗用的经历。

而自己也玩一些摄影，虽没什么特别的商业价值，但终究是自己的作品，理应保护版权，因此我想在图片上统一添加自己的版权水印，以防止被他人盗用。

## 实现方案

需求清晰了，其实主要分为两部分：

1. 让用户只能通过 WebP Cloud 代理链接访问到我的图片，禁止直接访问原图链接
2. 在 WebP Cloud 代理层面为所有的图片统一自动添加自己的版权水印，无须手动操作

以下是我的实现方案与详细步骤。

### WebP 自定义 User Agent + Cloudflare WAF

和 [WebP Cloud](https://webp.se/) 的开发者 [Nova Kwok](https://x.com/n0vad3v) 聊了一下，发现 WebP Cloud 提供了自定义「Proxy User Agent」的功能，并推荐在 Cloudflare WAF 中配置对应规则以保护图片安全，文档中有详细说明 -- 「[Security | WebP Cloud Services Docs](https://docs.webp.se/webp-cloud/security/#cloudflare)」。

#### WebP Cloud 配置

当我们访问互联网上的网页或图片链接时，请求通常会包含一个 User Agent 字段，一般包含浏览器版本等信息，网站可针对不同的 User Agent 进行一些特定逻辑处理。

WebP Cloud 默认会使用 `WebP Cloud Services/1.0` 作为值，也就是不论用户访问图片时使用的是什么终端设备和浏览器，请求到 Cloudflare R2 时都会被统一为 WebP Cloud 定义的 User Agent 值，而这个值又是用户可以自定义的。

![webp_custom_user_agent](https://image.pseudoyu.com/images/webp_custom_user_agent.png)

因此，我们登录 WebP Cloud 的控制台，将「Proxy User Agent」字段设置为一个自定义值，如 `pseudoyu.com/1.0`。

#### Cloudflare WAF 配置

![cloudflare_waf_intro](https://image.pseudoyu.com/images/cloudflare_waf_intro.png)

[WAF（Web Application Firewall）](https://developers.cloudflare.com/waf) 是 Cloudflare 提供的一个防火墙服务，可以自定义规则来限制特定请求以保护网站安全，登录 Cloudflare 后在左侧边栏点击「网站」，点击进入需要保护的域名，选择侧边栏「安全性」 - 「WAF」即可免费使用（注：不是最外层的账户级 WAF），免费账户可设定五个自定义规则。

![waf_create_rule](https://image.pseudoyu.com/images/waf_create_rule.png)

点击「创建规则」，进入设置页面。

![user_agent_protection_waf](https://image.pseudoyu.com/images/user_agent_protection_waf.png)

点击「表达式预览」右侧的「编辑表达式」，填入以下规则：

```plaintext
(http.host eq "images.pseudoyu.com") and (http.user_agent ne "pseudoyu.com/1.0") and ((http.request.uri.path contains "jpg") or (http.request.uri.path contains "png") or (http.request.uri.path contains "jpeg") or (http.request.uri.path contains "gif"))
```

要注意的是需要把其中 `pseudoyu.com/1.0` 这部分填入上文在 WebP Cloud 中自定义的 User Agent 值，并且为了防止我在同一域名下的其他自部署服务的图片无法正常显示，我还加了 `(http.host eq "images.pseudoyu.com")`，即只对图床的访问链接生效，其余保持不变即可。

并且在「选择操作」下拉选择「阻止」，这样会匹配我们的规则并阻止特定网络请求，编辑完成后点击「部署/保存」即可。

我使用的是目前 WebP Cloud 官方文档提供的[推荐规则](https://docs.webp.se/webp-cloud/security/#cloudflare)，后续或许会针对新的功能有所调整，可以直接参考文档。

![block_by_waf_example](https://image.pseudoyu.com/images/block_by_waf_example.png)

完成配置后，当我们再次访问以 `images.pseudoyu.com` 开头的源站链接时会被 WAF 拦截，例如：

[images.pseudoyu.com/images/new_mbp_setup.jpg](https://images.pseudoyu.com/images/new_mbp_setup.jpg)

而经 WebP Cloud 代理过的链接则可以正常访问，例如：

[image.pseudoyu.com/images/new_mbp_setup.jpg](https://image.pseudoyu.com/images/new_mbp_setup.jpg)

完美实现了我们的需求。

### 使用 WebP Cloud 为图片添加版权水印

经过了上文的操作，我们已经确保用户只能经过 WebP Cloud 代理链接访问到我们的图片了，接下来就是为图片添加版权水印。

![webp_watermark_feature](https://image.pseudoyu.com/images/webp_watermark_feature.png)

同样是查阅了 WebP Cloud 的文档，发现它在「Visual Effects」模块中提供了「Watermark」功能，可以为图片添加自定义的水印，使用 `Fabric.js` 库实现，提供了可视化编辑的一些选项，还写了一篇有意思的博客 -- 「[使用 Fabric.js 实现实时水印预览](https://blog.webp.se/dashboard-fabric-zh/)」。

![watermark_list_webp](https://image.pseudoyu.com/images/watermark_list_webp.png)

进入 WebP 控制台，选择左侧「Visual Effects」，并点击右上角「Create Watermark」，就可以进行一些自定义水印样式配置了。

![pseudoyu_copyright](https://image.pseudoyu.com/images/pseudoyu_copyright.png)

这是我的配置，即在图片的底部中间添加一个浅灰色的 `@pseudoyu` 字样。

![webp_purge_all_cache](https://image.pseudoyu.com/images/webp_purge_all_cache.png)

需要注意的是，WebP Cloud 会为用户缓存图片数据，因此若想要之前上传的图片也应用水印或更新了新的水印则需要在代理配置中点选「Purge All Cache」来清理缓存。

![apply_watermark_webp](https://image.pseudoyu.com/images/apply_watermark_webp.png)

编辑完水印后，进入代理的详细配置页面，下拉到「Watermark Setting」模块，选取刚创建的水印，点击右上角「Save」即可。

效果就不单独展示了，本文所有配图都通过这种方式添加了水印。

## 总结

![webp_thoughts](https://image.pseudoyu.com/images/webp_thoughts.png)

使用 [WebP Cloud](https://webp.se/) 才第三天，最开始一直以为只是一个类 CDN 图片加速访问工具，经过折腾后发现了很多有意思的地方，并且为个人免费用户提供的 Free Quota 足够到大家拥有更好的图片体验，也就是他们所坚持的「做正确的事」。

团队更多是做一些技术沉淀和实践，写了许多博客 -- 「[WebP Cloud Services Blog](https://blog.webp.se/)」，闲时读读也能感受到他们的热情，最近因为「[周报 \#63 - 不愉快的订花经历、商家和消费者与日渐 AI 化的人](https://www.pseudoyu.com/zh/2024/07/01/weekly_review_20240701/)」这一篇中的经历而在思考「劣币驱逐良币」这一问题，我觉得坚持做正确的事不向商业做过多妥协的团队理应被更多人看到，理应过得更好，我人微言轻，仅以这些教程来让更多的人了解到他们。
