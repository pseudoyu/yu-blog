---
title: "周报 #78 - NAS、Chromebook 与 Zeabur 折腾小记"
date: 2024-11-04T08:42:00+08:00
draft: false
tags: ["review", "life", "nas", "chromebook", "zeabur"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20241104](https://image.pseudoyu.com/images/weekly_review_20241104.png)

本篇是对 `2024-10-29` 到 `2024-11-03` 这周生活的记录与思考。

最近不知怎的又久违地开始折腾开发环境和设备了。

在 Ares 的技术支持下终于拥有了心心念的 NAS；把闲置已久的 Chromebook 重新装了一下并刷了 Arch Linux，甚至还把 MBP 刷了一个 Asahi Linux（不过作为主力机还是不行，先卸载了，打算回家把家里的台式机刷了）；Zeabur 支持了 Dedicated Server 之后我也把 RSSHub 等比较消耗资源的服务迁移到了 Hetzner 的 CAX-31 Arm 主机上；还有很多有意思的事。

## NAS

![my_nas_omv](https://image.pseudoyu.com/images/my_nas_omv.png)

其实好久之前就对 NAS 很感兴趣，但其实自己看番剧和剧集都是直接在流媒体平台上或者 Infuse 连网盘，对于家庭存储的需求并不那么高，所以一直没下定决心入手。

再加上自己有个 Mac Studio，平时也都是长期开机的，配合上公网 ip 和 Cloudflare Argo Tunnel，其实也已经满足了绝大多数的家用服务需求了。不过由于系统架构的限制等，我在配置 HomeAssistant 的时候网络配置总是有一些奇怪的问题。

有一次跟 Ares 聊到 NAS 的时候，他提到有个自己组好的 NAS 可以出给我（他自己已经迭代了），很是心动，于是找了一个周末来我家里配置完成了，有了技术支持自己少走了无数弯路，一切都完美 work 了。

四盘位（8T 存储外加 8T 的备份），任意热插拔掉两个盘位依然可以正常运作，把之前网盘里的一些照片和影响资料迁移了过来；用的是 [openmediavault](https://www.openmediavault.org/) 这一界面有些古老但是完全够用的系统；使用 Portainer 管理了一些 Docker 服务，16G 内存也基本够用。

## Chromebook 与 Arch Linux

![yu_chromebook_setup](https://image.pseudoyu.com/images/yu_chromebook_setup.png)

两年多前在重温 Teahour 的这期「[#95 - 用 Chromebook 做开发是什么样的体验？](https://teahour.fm/95)」时对瘦客户端开发模式很是着迷，自己还写了一篇「[基于 frp 内网穿透的瘦客户端开发工作流」来实践](https://www.pseudoyu.com/zh/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)」，顺便也种草了 Chromebook 这一国内并不流行的设备，入了一台 2019 款的 Google Pixbook Go（产品线很快就被 Google 砍掉了，所以倒是有点纪念意义的最后一代）。

但其实因为后来远程办公以及依赖了很多 macOS 专属的软件，这台设备的利用率一直很低，最近在清迈看另一个 mentor 把自己的 Chromebook 刷了 [Pop!_OS](https://pop.system76.com/)，很酷，于是想着回来折腾一下。

![btw_i_use_arch](https://image.pseudoyu.com/images/btw_i_use_arch.png)

本来也是想彻底刷成其他 Linux 发行版的，升级了一下发现 ChromeOS 的 UI 和各类交互很舒服，折腾了一下把内置的 Debian 系统换成了 Arch 也很足够我对于 Linux 的需求，不那么“正统”但够用，折腾了一天，达到了很惊喜的体验，用了几个跨平台的方案保障体验几乎是一致的了。

1. **1Password**。前段时间才从 Elpass 换成 1P，浏览器插件、多平台和强大的自动填充让我后悔没早点换了；再加上能够用 ssh agent 功能来进行 git 签名等，再也不用维护多套 gpg keys 了。
2. **x-cmd**。朋友前司的产品，最开始只是想支持体验一下，发现确实满足我的需求，只需要很少的几个命令和配置就能实现一个多设备完全一样的开发环境，也使用 x-cmd 管理了我的 Go, Node.js 等开发环境，很省心。
3. **fydeRhythm**。我现在完全投入双拼，在搜索的时候发现了这一开源项目，作为一个 Chrome 插件安装到 ChromeOS 系统中，也能够在终端和各类应用中原生使用，几乎免配置；Linux 上我使用 fcitx-rime 配置，不过折腾了好久才搞定。
4. **Cursor**。有打包好的 AUR 包可以很方便在 ChromeOS 上一键安装，加上导入配置的功能，改了几个快捷键后完美还原体验。
5. **Chrome**。考虑为了一致体验从 Arc 切换回 Chrome 了，像是 Telegram、Slack、Discord、Follow 这些工作中用到的直接都使用网页版了。
6. **Onedrive**。因为没有了 iCloud，刚好利用上我的 Microsoft 365 带的 1T Onedrive 存储，用于文件传输和同步。
7. **Google Play Store**。Chromebook 很大的一个优势就是可以直接使用 Android 应用，还提供了一些优化，像是 Clash、HBO Max 这些应用都可以作为应用直接打开了。

![yu_chromebook__cursor](https://image.pseudoyu.com/images/yu_chromebook__cursor.jpg)

我其实有很多高性能设备，例如日常在用的 M2 Max 的 MacBook Pro，由于性能和续航达到了一个很不错的平衡，导致我即使出门在外也随时都能打开来进入工作状态，甚至爬山和散步都会背着，有时候其实并不能很放松地出门或是陪伴身边的人，但我又有“电脑分离焦虑症”，不在手边的时候总是担心有什么紧急事务要处理而焦躁不安。

这台 Chromebook 算是一个完美的方案，同时有满血版的 Chrome、Arch 和 Android 系统，性能不强、轻便好看，所有依赖浏览器的工作都完全能胜任，真的要调试工作项目的代码稍微有点卡但也能用，在缓解我焦虑的同时，每次有需求后也多了一步掂量一下，是不是真的紧急到我即使需要更费力地调试也要当下完成，绝大多数情况下我也都会选择等到家了换上主力设备了再处理。

这一点很有意思，其实设备性能已经过剩到并不会制约自己的效率，反而是需要刻意的约束来让我的目光更多转向周遭。

## Zeabur 服务器

我算是 Serverless 平台的重度玩家和 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 的早期用户了，现在自己的很多服务依然部署在 Cloudflare Pages/Workers、[fly.io](https://fly.io/) 和 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 平台上；同时之前也是各种 vps 的折腾爱好者，有好几台搬瓦工的传家宝，再加上前两年有点上头，又新添置了几台，导致利用率很低。

![zeabur_dedicated_servers](https://image.pseudoyu.com/images/zeabur_dedicated_servers.png)

最近正好 [Zeabur](https://zeabur.com?referralCode=pseudoyu) 支持了 Dedicated Server，利用 k3s 外加一些 monitor 服务能够在平台上直接使用自己的服务器进行部署，而关联 GitHub Repo、镜像 build、拉取等高消耗任务则是通过 Zeabur 来进行（目前都是免费的，不知道后面会不会按量计费），不占用服务器本身的资源。

于是把我的 RSSHub 和 Node 节点等一系列服务直接迁移过来了，终于把月账单又控制在 Developer Plan 的 5 刀以内了。

Zeabur 的模板也比较强大，我现在在维护 [RSSHub 的 Zeabur 模板](https://zeabur.com/templates/X46PTP?referralCode=pseudoyu)，可以无须域名等额外配置，一键在 Zeabur 上部署自己的实例；顺便还把之前自己用的 [n8n](https://zeabur.com/templates/IXQJVF?referralCode=pseudoyu)、[Remark42](https://zeabur.com/templates/P0N8GA?referralCode=pseudoyu)、[GoatCounter](https://zeabur.com/templates/VN803S?referralCode=pseudoyu) 等服务都做了模板，欢迎大家直接部署使用。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。并且把 Telegram Channel 消息作为内容源搭建了一个微博客 —— 「[daily.pseudoyu.com](https://daily.pseudoyu.com/)」，可以更方便浏览了。

#### 书籍

- [**素食者**](https://book.douban.com/subject/35534519/)，因为诺奖才了解到的作者，周末得闲才开始读，不长，只有三个篇章。看第一章的时候我正在吃饭（幸好是素食），作者把很多模糊的负面的感受描述得非常具体，以至于我有点反胃，很久都没缓过来，很难得有这样的感受了；后面的剧情走向略有点抽象，但确实加起来四种不同视角却相互关联的方式很奇妙。
- [**献给阿尔吉侬的花束**](https://book.douban.com/subject/26362836/)，最开始的错字报告到后来智商跃升后对这个世界和身边人态度的变化的不解，到后来对自己作为一个“人”过去和现在的探索，再到最后的一切回到原点和结束。他用了几个月的时间快速经历和理解作为“人”的一生，很多人几十年甚至终其一生也没办法回头去接纳过去和真实的自己，无关智慧，只是重新拥有了思考这一能力的他就像是失明的人重新见到光一样珍惜。
- [**红与黑**](https://book.douban.com/subject/35781152/)，从一个视频看到的讲解，关于于连的自尊和因此表现出来的傲慢的描述印象很深，有一种底层市民向上的野心，但由此产生的矛盾、自尊受挫后的疯狂和极端的转换描写得很具体。
- [**小城与不确定性的墙**](https://book.douban.com/subject/37016658/)，读了前几章，感觉跟「世界尽头和冷酷仙境」的设定好相似。

#### 文章

- [从亲密关系中学到的](https://thirdshire.com/relationship/)
- [Threads API - How to authenticate, retrieve tokens](https://blog.nevinpjohn.in/posts/threads-api-public-authentication/)
- [(我的) Golang 错误处理最佳实践](https://xuanwo.io/2020/05-go-error-handling/)
- [Zeabur 使用心得分享](https://blog.kalan.dev/posts/zeabur-review)

#### 视频

- [新手如何从0开始拍出一条有趣的VLOG？｜拍摄&剪辑的小技巧分享～](https://www.bilibili.com/video/BV1xdSoYiEd8)
- [诺奖韩江【素食者】男性视角下的女性丢失了什么](https://www.bilibili.com/video/BV1L31MYqESz)
- [作为中间派：聊聊杨笠与性别](https://www.bilibili.com/video/BV1BWSrYGEMs)

#### 剧集

- [**企鹅人**](http://movie.douban.com/subject/35604181/)，太精彩了。
