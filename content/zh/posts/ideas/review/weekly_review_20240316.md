---
title: "周报 #54 - 漂流计划、钱包被盗与 Home Server"
date: 2024-03-16T05:20:00+08:00
draft: false
tags: ["review", "life", "travel", "computer", "work", "love", "home assistant", "home server"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20240316](https://image.pseudoyu.com/images/weekly_review_20240316.png)

本篇是对 `2023-03-01` 到 `2024-03-16` 这两周生活的记录与思考。

如上篇周报所述，我开启了一段漂流计划，最后以「杭州 -> 上海 -> 湖州 -> 南京 -> 北京」这样近两周的旅程告一段落，几乎都处在江浙，没什么特殊的风景，更多还是关于人和事；由于主钱包被盗且没找出原因，重装了两台主力电脑，也刚好重新整理开发环境配置；把家里的 Mac Studio 作为 7/24 的 Home Server，跑了 Home Assistant 等常驻应用控制智能家居，折腾却也有趣；工作上组里忙了许久的 Alpha 主网上线，久违的兴奋感；还有很多有意思的事。

## 漂流计划

![tianmushan_view](https://image.pseudoyu.com/images/tianmushan_view.jpg)

年后开启的漂流计划第一站是上海，这些年前前后后去过大概也有几十次了，有过一两个月实习的长居也有偶尔的短暂停留，通常都是有事要办或是有人要见，真正“生活”可能还是少有的机会，没选什么繁华的区域，也没安排什么特别出行的计划，只是选了个离朋友还算接近的地点定了一周的民宿，就又回归了正常工作学习的节奏。

偶尔下楼到周遭的商圈觅食，到了周末也和许久未见的大学舍友约饭，剩余时间依旧宅在酒店里工作，顺便还刷完了 mark 已久的「西部世界」，很巧的是刚好有个同事住在离我一两公里的地方，于是也有了一次小小的三人团建。

接下来去了趟湖州，在朋友 [Xiao](https://twitter.com/gxgexiao) 家里住了一周。和他的相逢是源自一年前的某天他在[各地巡游溜达](https://www.gexiao.me/2023/07/01/lets-wander/)的时候发了一条在杭州的朋友可以约见面的推文，彼时的我刚回杭，对未来的生活充满着许多的未知和期待，鼓起勇气约了一次晚饭和西湖边漫步，虽然是第一次见面并且也没什么交集，却真诚而信任。

后来他搬到了湖州，我 8 月曾约了一次相见却因为种种缘由而没能成行，有些遗憾，于是趁着这次漂流赴约。在莫干山走野路上山，在安吉云上草原的悬崖上漫步，也去了两个数字游民公社参观，对他们的社区氛围很是心动。感觉今年的我似乎找到了一种久违的生活上的松弛感，会更愿意去见一些人和体验一些事，生活也不仅仅是工作和学习，人和与人有关的一切都对我产生了更多的吸引力，也由于和许多“网友”有了更深的链接，自己线上和线下的关系也变得逐渐模糊。

得益于公司每周三的「Work Together 1 Hour」，一位同事推荐了汤山的温泉和莫干山的森林书屋，于是和学姐相约在南京会和，度过了惬意的一周，也开始探索一些周末行的去处，生活变得更加具体。

## 钱包被盗与设备重装

最近把自己的笔记本和家里的台式都重装了一下系统，起因是自己的主钱包不幸被盗了。看链上记录大概是年初一的中午，钱包里所有资产（包括一些参与开源项目的空投）都被转为 ETH 和 BNB 后转走了，钱包里还有自己的 ens 和一些 NFT（~~不过黑客看不上所以还留着就是了~~），整体的金钱损失不大，但因为找不出是哪里泄漏的私钥，不得不将所有设备环境都重装一遍，可以说是个大工程。

因为都是 macOS 系统，所以系统设置和软件方面倒是轻车熟路，主体还是参照我的个人工具箱项目「[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)」，但在这个基础上做了不少的减法，更多只保留了刚需的一些，发现把 [Rewind](https://www.rewind.ai/) 卸载后我的 MacBook Pro 续航恢复了很多，出门几乎可以不用带充电器了。

![x-cmd_env_install](https://image.pseudoyu.com/images/x-cmd_env_install.png)

另外也正好趁机整理了自己的软件安装来源、开发环境管理和命令行配置等，正好尝试了朋友公司开发的「[x-cmd](https://cn.x-cmd.com/)」项目。

![zshrc_config](https://image.pseudoyu.com/images/zshrc_config.png)

配合 ohmyzsh 把自己的命令行配置简化到了短短的十几行，后面都可以通过 `x env` 等命令来管理各种环境和命令行工具，很易用。

![x-cmd-env-ls](https://image.pseudoyu.com/images/x-cmd-env-ls.png)

最后使用 `x env` 来管理了自己的 Go、Node、Python 开发环境，免去了各种需要自己安装 nvm、设置环境变量等步骤，也体验到了企业级客户支持（指遇到问题直接 tg 轰炸朋友来解决 🤣），后面也会成为自己的装机标配，还在持续深度体验中。

另外就是把 ssh key、GPG 签名等在两台设备之间统一管理了，配合 Elpass 进行密码管理和服务器自动登录，获得了通勤和宅家无缝切换的体验。

## Home Server & Home Assistant

~~大概是年纪慢慢上来了~~，终究逃不过路由器、充电头、NAS 这三大魔咒。路由器用了去年从 [STRRL](https://twitter.com/strrlthedev) 哥哥那淘来的 Asus AC86U，刷了新版梅林固件，很够用，就没再折腾软路由什么的了；充电头/充电器则是在体验了闪极全透明充电宝、100W 氮化镓充电头和硬糖工厂小电拼（~~现在有点不敢用了~~）后也退烧了。

终于还是把魔爪伸向了 NAS，在跟我们组可靠的运维 & NAS 深度 DIY 玩家 Ares 聊了好一阵子，决定先把家里的 Mac Studio 作为一个 Home Server。

![yu_home_assistant_macstudio](https://image.pseudoyu.com/images/yu_home_assistant_macstudio.png)

首先做的是把家里的智能设备都连上 Home Assistant，但是由于是 Apple M1 芯片，没有现成的官方解决方案，在折腾了好一番后，最终参照「[Run Home Assistant on macOS With a Debian 12 Virtual Machine](https://siytek.com/home-assistant-macos-utm-debian-12/)」这一篇文章使用 UTM 安装了一个 Arm 架构的 Debian 的虚拟机，在里面跑了满血版 Home Assistant，并且用 frp 把接口映射到了公网，最后使用 iOS app 以及网页版本直接进行操作，目前的方案可能因为虚拟机网络模式问题，目前没办法通过 HomeKit Bridge 添加到 Apple 的家庭 App 中，不过能够把所有的小米、Yeelight 和小佩宠物设备链接起来，目前阶段也已经够用了。

另外作为一个 Home Server，保持了 7/24 小时常驻，在噪音和耗电上都几乎无感，开启了 smb 文件共享、ssh 远程登录和远程 vnc 桌面控制，并且通过内网穿透保障我在外面也能够访问到家里的设备。

为了保障安全性和稳定性，我同时采用了三种不同的内网穿透方案。

1. frp
2. Surge Ponte
3. Cloudflare Argo Tunnel

第一种方案我已经使用了近两年，在「[基于 frp 内网穿透的瘦客户端开发工作流](https://www.pseudoyu.com/zh/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)」一文中有很详细的介绍，要求有个公网服务器，但配置简单且稳定，目前我只是保留了 ssh 与 Home Assistant 的端口。

第二种方案则是通过 Surge 软件在 macOS/iOS 设备之间便捷地实现内网穿透，可以在「[Surge Ponte Guide](https://kb.nssurge.com/surge-knowledge-base/guidelines/ponte)」看到其详细介绍，需要有支持 UDP 的代理线路，除此之外几乎开箱即用，我用其来访问家里 Mac Studio 的文件和本地的一些服务，也可以在外部直接访问配置家里内网路由器等，更多是自用。

而第三种方案则是最近看到「[使用 Cloudflare Argo Tunnel\(cloudflared\) 来加速和保护你的网站](https://nova.moe/accelerate-and-secure-with-cloudflared/)」文章时才新加的，之前都是通过 cloudflared 命令行工具手动配置的，多少还是有些麻烦于是没实践，最近 Cloudflare 把它集成到了 [Zero Trust](https://developers.cloudflare.com/cloudflare-one/) 中，几乎可以在界面完成各种操作配置，我用来在家里服务器运行一些需要对外暴露的公网服务，例如前几天使用 [ollama](https://ollama.com/) 跑了一个 [codellama:70b](https://ollama.com/library/codellama:70b)，然后再通过 [ChatKit](https://chatkit.app/) 直接访问，体验很不错，就是生成得太慢了，所以也就尝尝鲜。

刚好最近我们厂的[Alpha 主网](https://rss3.io/blog/en/introducing-rss3-alpha-mainnet)上线了，打算等后面公益节点的时候用 Home Server 自己跑一个，现在跑不起 🤣。

## VR 学车

![vr_car_license](https://image.pseudoyu.com/images/vr_car_license.png)

因为即将要有一些自驾的需求，又重新报名了驾校开始学习，这次的驾校有 VR 练车设施，没有自己想象得那么抗拒了。

## 其他

其他似乎没有太多有意思的事，处在忙碌和想做的事做不完而焦虑的反复中，不过一切也都在慢慢变好。

GitHub 给了 Copilot 的开源免费 License，可以继续白嫖代码补全和 Copilot Chat，配合上 Claude 3 Sonnet 和在「[burn.hair](https://burn.hair/register?aff=isWf)」中白嫖的 GPT4 Token，已经能够满足我所有的代码和各类需求。

哦对，还约到了我的偶像程序员「[Randy](https://lutaonan.com/)」月底在北京见面！！！

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 书籍

- [**The Monk and the Philosopher**](https://book.douban.com/subject/2228297/)，关于宗教和哲学的一些思考，聊到所以刚开始看一点。
- [**红与黑**](https://book.douban.com/subject/35781152/)，从一个视频看到的讲解，关于于连的自尊和因此表现出来的傲慢的描述印象很深，正在看。

#### 收藏

- [Million Lint is in public beta | Million.js](https://million.dev/blog/lint)
- [Discover Daily by Perplexity](https://discoverdaily.ai/)
- [Ehco Relay](https://ehco-relay.cc/)
- [RSS3 Alpha Mainnet](https://rss3.io/blog/en/introducing-rss3-alpha-mainnet)
- [Velja — Sindre Sorhus](https://sindresorhus.com/velja)

#### 文章

- [幸福的积分 – 虹线](https://1q43.blog/post/5322)
- [我为什么喜欢 road trip | 椒盐豆豉](https://blog.douchi.space/road-trip/)
- [Software Has Eaten The Media](https://www.wheresyoured.at/the-anti-economy/)
- [无风险年化 360%？小白也能懂的 Crypto 套利 - TARESKY](https://taresky.com/crypto-arbitrage)
- [How NAT traversal works](https://tailscale.com/blog/how-nat-traversal-works)
- [一个六岁开源项目的崩溃与新生 - DIYgod](https://diygod.cc/6-year-of-rsshub)
- [用 Notion Calendar 打造高效 daily quest 系统 | 椒盐豆豉](https://blog.douchi.space/notion-calendar-daily-quest/#gsc.tab=0)
- [Run Home Assistant on macOS with a Debian 12 Virtual Machine – Siytek](https://siytek.com/home-assistant-macos-utm-debian-12/)
- [使用 Cloudflare Argo Tunnel\(cloudflared\) 来加速和保护你的网站 | Nova Kwok's Awesome Blog](https://nova.moe/accelerate-and-secure-with-cloudflared/)

#### 视频

- [我悟了，原来最好的转运方式是结婚！](https://www.bilibili.com/video/BV1cF4m157Cy)
- [study vlog #48 | 26 岁新的开始｜程序员晚间日常学习｜一些小礼物希望你们喜欢](https://www.bilibili.com/video/BV1Lj421Z7Vz)

#### 电影

- [**怪物**](http://movie.douban.com/subject/35797709/)，确实符合是枝裕和想要去描述的主题，但是可能加上了太多隐喻的部分，反倒是没能很传达到，也感受到剧情和情绪节奏的割裂。
- [**周处除三害**](http://movie.douban.com/subject/36151692/)，台湾拍犯罪倒是确实是别有风味，主题和画面也确实很敢，不过更多还是视觉的爽片吧，对人物人格的呈现和变化展现得有些仓促。
- [**西部世界**](http://movie.douban.com/subject/35042913/)，还是更喜欢第一二季的乐园 part，包括威廉的变化，后两季可能也是由于想要展现太过宏大的意识觉醒和自我选择，反倒是有些过家家。

#### 剧集

- [**舞伎家的料理人**](http://movie.douban.com/subject/35727023/)，在看。

#### 音乐

- [**Photograph**](https://open.spotify.com/track/1HNkqx9Ahdgi1Ixy2xkKkL) by Ed Sheeran
- [**温和表面**](https://open.spotify.com/track/4EP4BmTjXvMGKzhBwKzWu5) by 趙登凱
- [**Different Lives**](https://open.spotify.com/track/7e7JVMegy4WBMnzuZE9Srq) by Fly By Midnight
- [**After the Love Has Gone**](https://open.spotify.com/track/7e7JVMegy4WBMnzuZE9Srq) by Earth, Wind & Fire
- [**IN THIS WORLD - feat. 坂本龍一 Vocal : 満島ひかり**](https://open.spotify.com/track/5FMRUnWOXZXXtTjaxpMxl3) by Mondo Grosso
