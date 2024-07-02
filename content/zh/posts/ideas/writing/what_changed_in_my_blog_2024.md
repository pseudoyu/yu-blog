---
title: "2024 年了，我的博客有了什么变化"
date: 2024-06-29T13:48:58Z
draft: false
tags: ["hugo", "blog", "writing", "life", "remark42", "goatcounter", "webp cloud", "r2"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

## 前言

在两年前的这一篇「[2022 年了，聊聊我为什么还在写博客](https://www.pseudoyu.com/zh/2022/06/12/why_i_still_write_blog_in_2022/)」，我聊到了我写博客的缘起、初衷和搭建方案。

两年多过去了，初衷仍在，写作也依然坚持下来了，虽没有完成自己所计划的周更，但多少也积淀了些文字。

经历了很多事，似乎渐渐转向了一个「周报博主」，写的内容和风格已经大不同。技术和工具效率主题更少了，分享生活和思考更多了；少了些通宵两天更新四篇技术教程的冲劲，却多了些通过笔触表达情感后的自洽；收到很多关于博客搭建和技术教程的感谢依然会很开心，却也更珍惜和素昧谋面的大家交心的感动。

## 周报博主

可能是有一次开会闲聊 xLog 未来的发展，有位同事突然 cue 我说，你作为一个「周报博主」有什么想法，我一愣，这个称呼倒是第一次听到，翻了翻主页，确实。

之前一直自诩是技术博主、工具效率博主，最后留下内容最多，给大家印象最深的似乎还是周报，也不错。

![weekly_review_group_chat](https://image.pseudoyu.com/images/weekly_review_group_chat.png)

开始写周报似乎是「[Homura](https://x.com/RealAkemiHomura)」组织了一个周报监督小组，当时不论是在推特还是独立博客群体中都还是个小透明，也希望有更多人进行抱团和交流，当时会每周把自己的周报丢到群里，会有互相被卷到，也有对于他人生活状态的关心，很开心。

后来大家都经历了许多生活的工作的变动，群里最后的消息停留在了 23 年 1 月，但那依然是我很快乐的一段时光，也是我后来能继续写周报的动力，因为我知道，即使分享的只是生活的琐碎和一些不成熟的小想法，依然有人在认真读你的文字。

![weekly_view_discuss_with_randy](https://image.pseudoyu.com/images/weekly_view_discuss_with_randy.png)

之前有一次收到 Randy 的催更，他说其实没必要把它定义为周报，不然常常会有压力和束缚，不过我反倒依赖这种输出倒逼输入的模式，这样有了周报作为一个结果导向，才会更有动力把这周过好。

~~虽然我常常重新定义周就是了。~~

## 独立博客

比起编排精美的书刊杂志，我更享受于访问他人的博客网站，站名名称、主题配色、配乐排版都更真实具体地呈现了一个人格化的存在，而在阅读博文时，我也常常会视为一次穿越时空的对话，会想象写下这些文字碎片的作者当时是怎样的心情，有时甚至也会带些顽皮地脑补他是一个怎样的人，此刻在做些什么。

独立博客其实是一个说大不大说小不小的圈子，两年过去，我反倒觉得开始搭博客、写博客的人渐渐变得多了，也有了更多有意思的高质量内容。

相比起其他不论是粉丝积累还是互动都更为方便的成熟内容平台来说，不仅仅是平台和写作形式上的独立（我其实也愿意称在 mastodon 或是 misskey 上认真分享内容的人为独立博客作者），而是思想的独立，即好的文章不止授人知识，还引人思考。

![dubo_1_intro](https://image.pseudoyu.com/images/dubo_1_intro.png)

还跟 Randy 聊到想为独立博客做一些事，以刊物的形式收录这一段时间内读到的好的文章并为之作序推荐，其实已经筹备好了第一期，但由于两个人错峰的忙碌和更专注地做 EpubKit 产品，迟迟未能发布，这也是希望能够在未来某个节点能够持续做下去的事。

## 博客系统

这是两年前写过的几篇关于博客搭建的文章：

- [2022 年了，聊聊我为什么还在写博客](https://www.pseudoyu.com/zh/2022/06/12/why_i_still_write_blog_in_2022/)
- [免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）](https://www.pseudoyu.com/zh/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)
- [Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)
- [从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
- [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)

主要是围绕着我使用 Hugo 这一静态网页生成器（SSG）搭建个人博客及一些周边服务的一些记录，也看到很多人通过各种联系方式加到我说根据这一系列教程成功拥有了自己的博客，很开心能够为博客这一已经有些式微的创作方式做出一些小小的贡献。

当时写的时候对自己的整套方案很满意，然而时隔两年回头看了下。

- **博客本体**：Hugo 本体没变，部署方案: GitHub Pages + Cloudflare CDN -> Cloudflare Pages
- **评论系统**：Cusdis -> Remark42，部署平台：Railway -> Vercel + Supabase -> fly.io
- **统计系统**：Umami -> goatcounter，部署平台：Vercel + Heroku -> Railway -> Netlify + Supabase -> fly.io
- **图床系统**：GitHub + jsDelivr -> 阿里云 OSS -> VPS 上自部署的 Chevereto + PicGo -> Cloudflare R2 + WebP Cloud + PicGo
- **内容搜索**：无 -> Pagefind 静态搜索

更换的原因很多，有些是由于 Heroku 和 Railway 渐渐取消了免费计划，有些是由于开源项目更新少了缺少功能，也有些单纯是自己想折腾一下更轻量些。

想起来当时写这套系列教程的时候主要就是觉得网上能够搜到的方案和教程零散且常常落后，于是想给想搭建博客的读者一站式搭建起来的可行方案，发布后收到了许多人的反馈，有些内容也早该更新，却一直拖到现在才开始重新写，很惭愧。

下文会对当前的方案作一些介绍，后续更新后的系列文章完成后也会追加链接。

### 博客本体

![yu_blog_homepage_20240629](https://image.pseudoyu.com/images/yu_blog_homepage_20240629.png)

我使用 [Hugo](https://gohugo.io/) 这个静态网站生成器来搭建我的个人博客，使用并改造了一个比较 retro 的主题「[hugo-theme-den](https://github.com/shaform/hugo-theme-den)」。

大体的流程可以参看「[Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/zh/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)」这篇文章和「[GitHub - yu-blog](https://github.com/pseudoyu/yu-blog)」这个仓库。

加了一些每天自动更新 About 页面的 GitHub Actions 自动化操作，并且由于 GitHub Pages 托管的网站从国内访问速度几乎不可用了，迁移到了 Cloudflare Pages，免费且体验感好了很多，其他几乎没什么改动了。

其实倒也不是没想过换框架，之前看到「[Owen](https://www.owenyoung.com/)」和「[PJ Wu](https://pinchlime.com/)」使用的 [Zola](https://www.getzola.org/) 就有些眼馋，甚至也有想过像「[槿呈 Goidea](https://justgoidea.com/)」或是「[Innei](https://innei.in/)」一样自己写一个。

不过冷静下来一想，自己现在网站积累了不少文章，要是想要保留原有路径免不了一番折腾，再加上确实很喜欢现在的主题，有什么想法干脆就直接去定制和改动主题了，还是少花一些心力在折腾平台，多写些博文比较重要，不然多少有点买椟还珠之嫌，遂作罢。

### 评论系统

在博客诞生之初直到今年四五月我一直使用的都是 [Cusdis](https://cusdis.com/)，整整用了三年。

时至今日依然是十分值得推荐的方案，轻量，方便自部署，风格也简约好看，搭建教程参看「[轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)」。

不过鉴于 Railway 从去年 8 月起已经取消了 Free Plan，如果依然想完全免费使用，可以使用 Vercel/Netlify/Zeabur 免费部署主项目，并在 [Supabase](https://supabase.com) 上部署一个免费的 PostgreSQL 数据库实例，把链接作为环境变量传入 Cusdis 服务中即可，其他流程大同小异。

![yu_remark42_preview](https://image.pseudoyu.com/images/yu_remark42_preview.png)

最近有一次由于更换数据库 URI 时 Vercel 部署一直报错，再加上确实需要一些新的功能，于是下定决心从 Cusdis 迁移，调研了一圈后选择了 [reorx](https://reorx.com/) 在「[更换博客评论系统](https://reorx.com/blog/blog-commenting-systems/)」一文中最后选定的 [Remark42](https://remark42.com/)。

单纯就配置选项来说比起 cusdis 还是丰富了不少，目前配置了常用的几种社交账号登录（GitHub、Twitter、Telegram、邮箱）、可以匿名评论、支持邮件订阅回复提醒并且也设置了 TG bot 提醒，并且部署在 [fly.io](https://fly.io/)，go 单二进制 + 数据库单文件，很舒服的解决方案，完成博文后会在这里更新教程链接。

### 数据统计系统

我之前自部署了一个 Umami（参看教程「[从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)」不过后来由于 Heroku 取消了免费 Plan，我最后折腾一圈，选择了 Netlify 部署服务 + Supabase 部署 PostgreSQL 数据库实例部署的方式，其余流程依然适用。

![yu_goatcounter_preview](https://image.pseudoyu.com/images/yu_goatcounter_preview.png)

不过一方面因为我部署得比较早，有一个大版本无法升级，以至于一直停留在自己 fork 的一个旧版本上，另一方面确实也渐渐觉得这种服务和数据库需要分离的方式免不了因为平台规则变动而频繁迁移，有些太重了，所以最后改为了 [goatcounter](https://www.goatcounter.com/)，同样是 go 单二进制 + sqlite 数据库单文件部署在 [fly.io](https://fly.io/)，又是很舒服的部署方案，等更新博文后同样会在这里更新教程链接。

![yu_google_console_preview](https://image.pseudoyu.com/images/yu_google_console_preview.png)

另外就是依然使用 [Google Console](https://search.google.com/search-console) 来统计分析我的访客信息与搜索权重。

这个结果很有参考性，我发现一篇关于终端对比的文章「[Warp，iTerm2 还是 Alacritty？我的终端折腾小记](https://www.pseudoyu.com/zh/2022/07/10/my_config_and_beautify_solution_of_macos_terminal/)」让我持续不断地有通过搜索引擎来的访客，另外的就是关于个人博客和搭建的系列文章了。

### 图床系统

两年前我其实还没怎么关注图床的问题，图片都是直接丢在 GitHub 仓库里，并且使用 jsDelivr 作为 CDN 加速（后来国内访问也几乎不可用了），不过随着文章数量增多，常常有身边的朋友告诉我说我的博客图片加载不出来，想着还是要兼顾一下阅读体验，于是调研了一圈方案。

![aliyunoss_invoice](https://image.pseudoyu.com/images/aliyunoss_invoice.jpeg)

先选择了阿里云 OSS 存图，电脑使用 PicGo 上传，方案挺好的，前几个月也没什么问题，直到 23 年初有几篇文章流量比较大，看着月账单上涨的势头，顿感贫穷。

于是在线路还不错的搬瓦工服务器上自建了 Chevereto 图床，同样配合 PicGo 的插件进行上传，稳稳地用了一年半。但自己对于自部署服务的稳定性和数据的珍贵性还是有些大意，前几天服务器突然挂了，内核报错直接无法重启，服务挂了倒还好说，但是我这一年半多的数据没有备份，也无法导出。

工单联系技术支持，一天只回复了我两次，一次让我重启，一次建议我聘请一个网络管理员排查。只能自力更生，翻遍了网上各种方案，折腾了一天终于算是解决了，但这一次的教训让我对与有重要数据的服务部分和自部署稳定程度都有了全新的认识，于是不敢再用原方案。

![yu_webp](https://image.pseudoyu.com/images/yu_webp.png)

最后采用了 [Cloudflare R2](https://www.cloudflare.com/en-gb/developer-platform/r2/) 对象存储来存放图片，每个月 10G 的免费额度很足够，大厂的服务与数据安全也有保障。为了优化用户的访问，又使用了一个「[WebP Cloud](https://webp.se/)」服务对 R2 的图片进行代理，在代理层面进一步减小图片体积，虽然对于国内用户来说速度肯定还是比不上阿里云 OSS 这种线路，但是在不用备案、稳定且免费的综合条件下，这是我能想到的最好的方案了。

![yu_picgo_pics](https://image.pseudoyu.com/images/yu_picgo_pics.png)

在电脑端通过 PicGo 客户端几乎一键上传并生成博客直接可用的 markdown 图片链接，配置完成后使用起来很顺滑。

图床搭建教程见这篇：

- [从零开始搭建你的免费图床系统 （Cloudflare R2 + WebP Cloud + PicGo）](https://www.pseudoyu.com/zh/2024/06/30/free_image_hosting_system_using_r2_webp_cloud_and_picgo/)

**[2024-07-02 更新]**

新写了一篇教程实现了图床添加隐私和版权保护，算是番外篇。

- [使用 WebP 与 Cloudflare WAF 为你的图床添加隐私和版权保护](https://www.pseudoyu.com/zh/2024/07/02/protect_your_image_using_webp_and_cloudflare_waf/)

### 内容搜索

![search_in_my_blog](https://image.pseudoyu.com/images/search_in_my_blog.png)

之前我的博客是没有内容搜索功能的，本来文章也不多，再加上静态博客没有后端，实现起来感觉也不容易，于是一直没支持。但随着后来有时候要查阅自己之前的文章只能用 VS Code 在一堆 markdown 文件中搜索的体验后，觉得还是很有必要的。

调研了一圈使用了 [Pagefind](https://pagefind.app/) 这一项目，基于静态文件的搜索库，无须引入或是托管其他后端服务，我只需要在每次发布博客的 CI 中构建全博客的索引文件，就能够很方便地支持搜索，中文搜索效果相对弱一些，不过也是够用的程度，基本上对主流的博客框架都支持。

这部分可以参照「[如何透過 Pagefind 在 Zola 產生的靜態網站裡加入搜尋功能](https://pinchlime.com/blog/how-to-add-a-search-function-to-zola-generated-static-websites-via-pagefind/)」这篇文章，我也正在着手写基于 GitHub Actions 更详细的教程，后续会更新在这里。

## 总结

2024 年了，我大抵还是个爱好写作的人，从早些年的书评影评、技术教程到现在的生活周记，似乎所见所思只有落笔写下才会转为触手可及的真实。而随着上百篇文章的沉淀，个人博客站点也成为了我在这世界的另一个载体，源于我却又独立于我，有时是随手可拾起的记忆碎片，有时又是自己精神的避难所。

也希望你们能够继续在我的博客中发现一些有趣的东西，或是知识，或是启发，抑或是一点点小小的共鸣，或许在某个时刻，你们也会想拥有自己的博客站点，让自己的所思所想在这个世界上留下一些痕迹，生根、发芽，也希望这套系列教程能够提供一些帮助。
