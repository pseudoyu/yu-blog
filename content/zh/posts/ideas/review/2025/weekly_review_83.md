---
title: "周报 #83 - 年初收纳（房间、设备、服务、软件）"
date: 2025-01-20T06:48:00+08:00
draft: false
tags: ["review", "life", "device", "service", "software"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/brand_new_day.mp3" caption="《Brand New Day》" >}}

## 前言

![weekly_review_20240120_83](https://image.pseudoyu.com/images/weekly_review_20240120_83.png)

本篇是对 `2025-01-06` 到 `2025-01-12` 这周生活的记录与思考。

这一周整理了自己的房间、抽屉、NAS、线上服务、网络环境等，实现了物理与虚拟空间的断舍离、收纳和优化。

## 房间整理

我大体是一个懒于整理房间或是收纳的人，但由于通常也就是在电脑前工作、学习或是放松，基本上没用到家中的什么空间，所以倒也算不上乱。

但由于最近工作和各种事项日渐忙碌，以及和学姐对于各自独立空间的需求，我开始把自己大部分的生活空间放回到我自己的租屋，也就趁此机会彻底整理了一下，花了大概六七个小时，最终收拾完的时候能够感受到由生活空间的整洁带来的秩序感。

### 网络管理

![yu_home_router](https://image.pseudoyu.com/images/yu_home_router.png)

我租的房子是一个几十平米的 Studio（大开间）户型，不太需要组网之类的，由一台高达主题款的 Asus RT-AX86U 路由器提供所有的网络，也没有怎么刻意折腾网线布局，靠近路由器的地方有一台 DIY 的 NAS 和一台懒猫微服是直接通过网线连接的，剩下所有设备都用的 Wifi 连接，基本上在房间内感受不到网速有什么瓶颈。

宽带是电信的千兆光纤，并且向运营商要了 ipv4 公网 ip，在 NAS 上安装了 [ddns-go](https://github.com/jeessy2/ddns-go) 服务，动态地更新公网 ip 的解析，并且通过路由器层面的端口转发暴露一些必要的网络服务供自己不在家的时候使用；后面觉得公网 ip 直接暴露的方式还是有些不太安全，于是又通过 Tailscale 搭建了一个私有网络并在之前活动便宜囤的一台上海的服务器上自建了一个 Derper，实现所有设备直接的网络联通，目前使用下来感觉是更好的方案（之前也用过 Surge Ponte，不过可能用的时候还比较早期并不算稳定，所以换了方案）。

Asus 的路由器可玩性很高，刷了梅林固件，安装了 Clash 应用，自己写了规则接管和分流了家里的所有设备的网络流量，所以家里的其他设备也都无须再折腾网络代理了。

### 存储管理

![lazy_cat_pic](https://image.pseudoyu.com/images/lazy_cat_pic.png)

我之前其实一直没怎么注意过个人存储的，主要就是靠一个 1T 的三星 T5 SSD 移动硬盘来存一些重要文件，后来又开始用 OneDrive 来云备份，但最近在有了 NAS 和懒猫微服后，又重新整理过自己的整个存储方案。

首先因为 Macbook 是 1T 的，本地会保存大部分重要文件，然后因为通过土耳其区的 Apple Store 购买了 2T 的 iCloud 空间，所以 iCloud 云端也有一个备份；然后会把所有的视频和照片同步到 openmediavault 的 NAS 上（8T RAID 5），懒猫微服上也会有一份（8T RAID 0），这样基本上对所有文件都有些保障（也使用了 rsync 来自动同步更改，不过感觉对于大文件不算稳定，大部分时间还是手动）。

### 数码设备管理

![yu_apple_tv](https://image.pseudoyu.com/images/yu_apple_tv.jpeg)

家里的 Apple TV，直接连着坚果 O1S 投影仪，这款是短焦的，所以直接贴墙使用就能够投出不错的画面，也不用担心遮挡这些，家用还是挺足够的，也默认连着一个 Homepod mini，平时用来当动态墙纸放歌也不错，构成了我的影音区；租的房间里自带了一台电视，连了我的 Nintendo Switch，旁边还有一台 Steam Deck，也可以通过 type-c 线直接连到电视上玩，也算是有了一个独立的游戏区（虽然很少玩了）。

前段时间进行了一波电子设备的断舍离，把 Mac Studio、Chromebook 和不算常用的屏幕、键盘、充电宝等都出了闲鱼，日常办公就只剩一台 14 寸的 MacBook Pro 了，在家里会直连去年买的几硕的 FlipGo 便携显示器，这样就相当于有了一个 14 寸的主屏和两个副屏，出行也直接线一拔，不用像之间一样考虑两台设备的配置、软件统一，开发环境等，反而能更专注一些。

### 宠物设备管理

![A7_04487](https://image.pseudoyu.com/images/A7_04487.jpg)

捏捏很多时候会在我的房间，家里的宠物基本上都是小佩（PetKit）家的，全自动猫砂盆、喂食器和饮水机，真的是让养猫体验 MAX，一个 App 管理所有的；还有一个米家的摄像头观察家里整体的一些情况，其他智能家居暂时都没怎么启用了，不过还是想着折腾一下用 Home Assistant + Home Bridge 把所有的都聚合到 iPhone 的 Home 应用里来一键管理，最近弄一下。

## 相机整理

![camera_a7m3](https://image.pseudoyu.com/images/camera_a7m3.png)

相机现在有三台，2018 年买的 Sony A7M3，前年买的 Sony ZV1 Mark II，和一台刚买的富士 X100VI，也做了很好的分工，A7M3 连着罗德 Wireles Go 麦克风，配合着一个百诺的脚架，常驻着放在办公区背后，减少拍摄视频的筹备流程，基本上能做到随时开录，而有些对着电脑的音频录制、教程则是直接用 Shure MV7 连着电脑来录，希望今年能够更多一点产出；出门的话则是直接带着 ZV1 拍视频，没有其他什么配件，就用自带的机身麦克风外加了一个官方的手柄，基本上随开随录，旅行和日常记录很足够；出门街拍就完全用 X100VI 了。

## 服务整理

### 网络代理

目前最影响日常生活工作体验的就是网络代理了，线路方面自己用 CN2GIA DC6 的一台美国机房搭了一个 trojan 节点，再加上朋友的一台新加坡的 ss 节点，基本上满足了日常需求；然后也有两个机场作为 fallback 和代理一些流媒体，比如 HBO Max，解决一些区域限制问题。

而由于 Mac 和 iPhone 上惯用的是 Surge，而路由器只能用 Clash 规则，常常不方便统一管理，于是用 [Surgio](https://surgio.js.org) 这一规则管理工具通过 GitHub Repo 维护和同步远程规则，更便于管理，自己也日常不断微调分流规则和一些配置项，更适应自己的各类需求。

### 自托管服务

![yu_serveices_2025_01](https://image.pseudoyu.com/images/yu_serveices_2025_01.png)

我的大部分静态网站类服务都在 Cloudflare、Vercel 和 Zeabur 上，而容器类服务则是分布在各种 VPS、独立服务器、NAS 和各种 serverless 平台上，最近整理的时候也作了一大波迁移。

Zeabur 貌似最近计费方式有了一些变化，感觉费用明显上涨，在没新增服务的情况下这个月超了 Developer Plan 5 美元额度不少，所以把一些消耗资源或是流量请求很大的都迁移走了，只保留了一些低消耗但对稳定性要求比较高的服务，例如博客访问统计系统这些。[fly.io](https://fly.io) 因为还有免费额度，上面只跑了我博客的 Remark42 统计服务，也迁移到了最便宜的 IAD 区域，挂载了 3GB 的 Volume，基本上能控制在免费额度之下，持续观察中。

由于之前有个比赛奖品之一是一年期的 AWS 一万多美元的 Credits，所以在机器上使用 Coolify 进行管理，把大部分的自用服务/开发环境放在了一台 8c32g 香港机房的机器上，可以直接使用现成的 Docker Compose 文件进行部署，也可以使用 Webhook 联动 GitHub 触发，基本上满足了我的需求，可玩性和定制化程度都要比 Zeabur 使用 k3s 的方案要高不少，数据库类的应用还很方便直接使用 S3 进行备份，等 AWS Credits 到期后可能也会迁移到 OVH 或者 Hetzner 独服上。

### 软件应用

![yu_app_screen](https://image.pseudoyu.com/images/yu_app_screen.jpeg)

我是一个对软件工具很挑剔的人，不过从今年开始也开始主要降低手机上各类 App 的使用，电脑上也尽量简化了工作量和干扰，开始更多体验和支持一些独立开发者的项目，其他的软件工具等最近在 「[GitHub - pseudoyu/yu-tools](https://github.com/pseudoyu/yu-tools)」会再更新一下，这里主要讲一下 AI 工作的使用。

目前最高频使用也是依赖的是 Cursor Pro（年付了），日常使用它的补全、CMD+K 以及 Composer（Agent）模式进行工作和各类项目，都依赖的 Claude 3.5 Sonnet 模型，已经能协助我完成大部分的工作。另一个年付的是 [STRRL](https://x.com/strrlthedev) 开发的 [Haye AI](https://haye.ai) 项目，日常绑定了一个 CMD+E 快捷键来优化我的一些英文写作，也很偶尔地用它的对话框功能。

GitHub 一直给我续着 Copilot，我使用 [ChatWise](https://chatwise.app) 项目来绑定使用 Claude 3.5 Sonnet 模型来进行一些小的编程类问题的 Chat，也绑定了我在 [NekoAPI](https://nekoapi.com) 和 [burn.hair](https://burn.hair) 上的 API Key 来使用 GPT-4o，ChatWise 还绑定了 [Tavily](https://tavily.com) 的 API Key 来启用 Web Search 功能，可以代替 Perplexity 来使用；另外就是在 Kagi Search 的三个月试用中，作为一个搜索引擎其实倒是没有什么体验上的感知，不过还是有明显地减少我对 AI 生成内容的依赖，其实整体得到的信息质量是有提升的，但是 Kagi Summary 等功能几乎不太用。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。并且把 Telegram Channel 消息作为内容源搭建了一个微博客 —— 「[daily.pseudoyu.com](https://daily.pseudoyu.com/)」，可以更方便浏览了。

#### 收藏

- [GitHub - egoist/sitefetch: Fetch an entire site and save it as a text file (to be used with AI models).](https://github.com/egoist/sitefetch)
- [tldraw computer](https://computer.tldraw.com/)
- [GitHub - phidatahq/phidata: Build multi-modal Agents with memory, knowledge, tools and reasoning.](https://github.com/phidatahq/phidata)
- [Tailscale · Best VPN Service for Secure Networks](https://tailscale.com/)

#### 书籍

- [**控糖革命**](https://book.douban.com/subject/36707112/)，在看。
- [**加缪手记**](https://book.douban.com/subject/34802764/)，看完了一本，他真的很 real 很有意思

#### 文章

- [读《吸引力法则：如何利用心理暗示实现愿望》的记录与思考](https://polebug.github.io/2024/12/18/law_of_attraction/)
- [2024：无为而治](https://polebug.github.io/2024/12/28/2024/)
- [月刊（第 28 期）：AI 没有体验世界的能力](https://blog.ursb.me/posts/weekly-28/)

#### 视频

- [2025 年了，手机能拍电影吗？](https://www.bilibili.com/video/BV1NvrSYtEdW)
- [vlog #86｜新年大扫除之后的晚间学习记录｜还在开发时间管理 APP｜读《荒原狼》《消失的多巴胺》｜在学「哲学导论」，超级有意思✌️｜尝试练习无氧的第一周](https://www.bilibili.com/video/BV1aUrXYLEnh)
- [【谜之声&鲨鲨】今年年初，我们去冰岛办了场婚礼](https://www.bilibili.com/video/BV1tu6HYmEtn)
- [回家 3 天：无根的我在离开的飞机上泪流满面...](https://www.bilibili.com/video/BV1WscJeHEuH)
- [我领奖时，为啥不笑？｜2024 年终总结](https://www.bilibili.com/video/BV18Bc3e6EwY)
- [来了来了！我那些超好用的剪辑技巧](https://www.bilibili.com/video/BV1ric2eZEgf)
- [背包大分享！2025 出门必备相机](https://www.bilibili.com/video/BV1AswAe3ENu)

#### 剧集

- [**去有风的地方**](http://movie.douban.com/subject/35662223/)，每天吃饭的时候看的，感觉还挺喜欢这种没太多 drama，只是比较平静地展示生活日常的日常向的剧了，也有点想去云南看看

#### 游戏

- [**双人成行 It Takes Two**](http://www.douban.com/game/35110438/)，玩了好几关了，感觉难度和游戏性很设计得很折中，我这种手残回合制玩家也能有不错的体验。
