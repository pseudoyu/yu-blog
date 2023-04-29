---
title: "周报 #38 - Foundry 合约测试、Logseq 任务管理与 Surge Ponte 远程开发"
date: 2023-04-30T00:10:03+08:00
draft: false
tags: ["review", "life", "home", "city", "travel", "work", "wuhan", "hongkong", "mayday", "web3", "friend"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

![weekly_review_20230430](https://image.pseudoyu.com/images/weekly_review_20230430.png)

本篇是对 `2023-04-19` 到 `2023-04-30` 这两周生活的记录与思考。

上篇周报提到进行了一场穿越多个城市的旅途，回到杭州后渐渐恢复了原本的生活节奏，独处时间多了许多，输入、思考和所做的有趣的事也有很多，但似乎整理、与自己对话的时间反而变少了，常常会在几天后才意识到时间的流逝。自诩是个不那么依赖社交和适应力比较强的人，想了想可能只是过多地把自己的生活状态寄托于虚拟世界，有一种与现实近乎脱节般的不适感。

现在在一个深夜航班上，小憩了一会儿后困意渐消，于是干脆拿出电脑写点什么，也许是因为没有网络和外部干扰，思绪似乎更加清晰。

## 工作氛围与自由度

加入新的团队不知不觉已经一个月有余了，大概是因为前两三周一直在四处奔波，常常没什么实感，现在才渐渐适应节奏与步入正轨，我所在组的氛围很好，即使是远程也不会感受到疏离感，一次会议常常从工作正事聊到外卖吃什么再聊到 Vlog 相机买什么（Sony 大法好），本来社恐的我也渐渐更多在群里话多了起来。

有趣的是因为密集参加了深圳团建、香港 Web3 Festival 和杭州的一波团建，细数自己已经见过公司的接近 20 位同事了，在一个 fully remote 工作模式的团队还是挺不容易的。还很幸运地赶上了线上年会，见到了很多只存在于 slack 对话框的有趣的同事们（各路神仙），表演个节目能发掘一个 rapper，玩个俄罗斯方块都能感觉到人与人之间的参差。

经过一些沟通，工作内容上做了一些调整，可以同步继续做一些智能合约开发和链相关的研发与探索，也能更深度参与自己喜欢的产品（看看还有谁还没在用 [xLog](https://xlog.app/) 和 [xSync](https://xsync.app/)，具体可以看看这篇「[周报 #25 - 基于 Crossbell 的个人信息输出与同步系统](https://www.pseudoyu.com/zh/2023/01/09/weekly_review_20230109/)」），虽然可能工作量和时间上需要多一些平衡，但还是有点小开心能有这样选择的自由度。

## Foundry 与合约测试

由于工作上开始着手了解加入的另一个组的项目，还蛮明显地感觉到自己之前虽然也做过一些链研发和写了小半年合约，但复杂度和开发实践上都还差挺多的，打算从这一块再好好补补，所以这周看了很多合约和调研文档，打算从 Hardhat 转为 Foundry 了。

其实之前 [Noy](https://twitter.com/Noy_eth) 和一些其他朋友已经向我疯狂推荐了 Foundry 框架，但是由于之前项目对于合约单元测试要求不那么高，自己也依赖于 js 写了很多工具脚本，就一直还在使用 Hardhat，直到这次真的跑了一些项目和写了一些 demo 单元测试，才感觉到它的巨大优势，瞬间叛变。都已经快吃灰的 Solidity 合约开发系列终于也要迎来新的更新了（~~在写了，不信你看图~~

![foundry_framework_outline](https://image.pseudoyu.com/images/foundry_framework_outline.png)

其实目前关于合约的企业级实践还是蛮少的，也由于后面所做一些合约是开源的，打算慢慢记录一些踩坑的经验和最佳实践吧（全职开源的优势了）。

## Logseq 与任务管理

由于现在自己个人安排与工作任务更多也更复杂，重新启用了 Logseq 作为自己的个人任务管理工具。自己其实之前一直在用 Notion 做个人看板，但是使用的时候总觉得心智负担太重，重度强迫症的自己也总是不断去优化那些任务的类别和描述信息，反而给了自己很大的压力。也用过滴答清单和 Todoist 这样稍微常规型的应用，但是同样的还是需要自己每天去梳理各种任务和标签，回溯起来也不算方便。

我后来发现了 Logseq 这一笔记软件。一开始我其实也只是把它当作一个以 block 为粒度的 markdown 笔记软件，也顺便想尝鲜一下双向链接这一总感觉一直在被提到的概念，用得还挺适应的，所以逐渐把 Notion 上自己的 Knowledge Base 都迁移过来了，后来其实也折腾过使用简悦来同步自己的网页标注这些，但是不久后还是觉得有些麻烦所以舍弃了。

直到我发现了 [Randy](https://twitter.com/randyloop) 的这个视频「[我如何使用 Logseq 管理我的生活和笔记](https://www.bilibili.com/video/BV1X44y1K7X1/)」，他提到了使用 Logseq 的 Daily Journal 来做自己的各种笔记与 TODO 管理，这样不需要像 Notion 这类软件那样自己先形成一个规划再呈现出来。

![logseq_daily_journal](https://image.pseudoyu.com/images/logseq_daily_journal.png)

因此当自己突然想起一件想要做的事情时，不需要单独在看板或是任务管理软件里建一条新的任务，只需要像是写一条笔记一样在自己的 Daily Journal 里面随意加上一个条目并且使用 TODO, LATER 这样的简单语法就能够进行简单的任务管理。

不过有些任务会跨越多天，我们的任务也会零散地散落在各个日期的 Journal 下，不是很利于统一管理，这就要使用到 Logseq 另外一个强大的功能了 —— Query，这个功能可以理解成以 block 为粒度的查询（就像是 sql 查询到一条记录那样），通过一些标签、语法等内在逻辑进行筛选，展示出我们想要的 block。

这个部分我参照了 Randy 的实践，创建了一个 Dashboard 页面，里面展示了自己的各种查询结果。我主要使用了如下几个 Query（括号中是其对应的 query 语句，需要的朋友可以自取并且根据需要修改）：

1. In Progress (`{{query (todo now)}}`)
2. Todo (`{{query (todo later)}}`)
3. Writing Plan (`{{query (and (todo later) [[writing]] )}}`)
4. Reading (`{{query (and (todo now) [[books]] )}}`)
5. Read It Later (`{{query (and (todo later) [[books]])}}`)

呈现结果如下：

![logseq_dashboard_in_progress](https://image.pseudoyu.com/images/logseq_dashboard_in_progress.png)

![logseq_dashboard_todo](https://image.pseudoyu.com/images/logseq_dashboard_todo.png)

![logseq_dashboard_other_queries](https://image.pseudoyu.com/images/logseq_dashboard_other_queries.png)

因为这个是 Randy 的实践，我就不单独出博文介绍了，在周报中简单介绍了一下自己的使用方式，大家有兴趣的可以看看他的原视频。

## Surge Ponte 与远程开发

自己在网络、各种硬件设备和系统的折腾上属于又菜又爱玩的类型了，之前也探索过瘦客户端开发的一些最佳实践，详情可以看这篇文章：

- [基于 frp 内网穿透的瘦客户端开发工作流](https://www.pseudoyu.com/zh/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)

其中最核心也是最难的点就是怎么在外部网络环境下访问家里的设备，如服务器、Mac 主机等等。在我之前的方案中使用的是 frp 这一工具进行内网穿透，大半年过去了，很稳，依然是首选推荐的方案。

但是当看到 [Yachen Liu](https://twitter.com/Blankwonder) 发的这篇「[Surge Ponte 研发手记](https://blankwonder.medium.com/surge-ponte-%E7%A0%94%E5%8F%91%E6%89%8B%E8%AE%B0-c145726fc07c)」时，又心痒打算折腾了。

五一假期又要出门在外几天，想着日常开发都是在家里的主机进行的，在外也想要能访问，刚好因为重装了系统还没配置 frp 客户端，想着干脆直接上 Surge Ponte 试试了。

于是赶在出发前一天晚上升级了下 Surge 5 并配置折腾了 Surge Ponte，一番探索下来，比起 frp 或者其他类似的解决方案，我觉得 Surge Ponte 在配置易用性和拓展玩法上有着绝对优势。

Surge Ponte 的折腾绝对值得一篇详细的博文，因此本周报里就不详细讲解原理和配置细节了，只简单展示一下目前我使用到的部分功能效果呈现。

当我在自己的 16 寸 MBP 与家里的 Mac Studio 同时开启了 Surge Ponte 功能（我使用的是 NAT traversal via proxy 的模式，只需要用一个支持 UDP 的线路就可以了，如自建的 Trojan 协议的代理），在已注册设备中就能够看到了。

![surge_ponte_config](https://image.pseudoyu.com/images/surge_ponte_config.png)

这个时候当设备开启了允许远程登录的权限时，就可以像访问云服务一样通过 `ssh [username]@[surgepontename].sgponte` 这样的命令直接远程登录主机，因此也可以支持 VS Code 远程开发等。

![surge_ponte_ssh](https://image.pseudoyu.com/images/surge_ponte_ssh.png)

当然这一点像是 frp 这些也可以轻易做到，而更强大的一点是这时候我们在家里主机上启动的一些服务，也可以通过 `[surgepontename].sgponte:[port]` 这样的网址直接访问。例如我通过 ssh 远程连接到家里的 Mac Studio 后启动了一个本地的 Next.js 网页服务，在本机开发时通过 `localhost:3000` 来访问，现在我可以直接在 MBP 上通过 `http://yu-macstudio.sgponte:3000` 直接访问（虽然 frp 也是能够做到映射服务出来，但是需要在 frp client 端写端口映射规则）。

![surge_ponte_servies](https://image.pseudoyu.com/images/surge_ponte_servies.png)

所以理论上通过 VS Code 直接远程连接主机修改代码文件并且使用 `[surgepontename].sgponte:[port]` 的方式能够获得完整版本地调试的体验，兼顾了便携性和性能（~~好，这就把 MBP 卖了换 Air~~

还有一个很实用的场景就是我们常常会有一些只有在家里的局域网才能访问的服务，如软路由器配置、NAS、树莓派等，这时候如果使用 frp 则需要每个都单独配置，而 Surge Ponte 可以直接通过设定 DEVICE 规则来实现外部访问，如我现在在外地可以直接使用 `http://router.asus.com` 来访问我家里的路由器配置页，这对于远程管理家里的一些常驻服务很方便。

![surge_ponte_router](https://image.pseudoyu.com/images/surge_ponte_router.png)

还有很多好玩的应用，如通过 smb 协议直接访问家里主机设备的文件等等，后面的博文会尽量涵盖一些好玩的应用场景，感兴趣的朋友可以关注（~~催更~~）一下博文。

## 捏捏近况

![nie_nie_in_painting](https://image.pseudoyu.com/images/nie_nie_in_painting.jpg)

博译学姐在给捏捏画油画！！！这个还只是一个初稿，还会再加亿点点细节，但是已经忍不住想展示出来了，太好看了！！！

![nie_nie_and_new_toys_01](https://image.pseudoyu.com/images/nie_nie_and_new_toys_01.jpg)

![nie_nie_and_new_toys_02](https://image.pseudoyu.com/images/nie_nie_and_new_toys_02.jpg)

新的猫爬架，提前开启度假模式！

五一后准备带去绝育了还是有些紧张的，希望一切安好。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 文章

- [Warp+ 流量搭配 Surge](https://pepcn.com/surge/warp-liu-liang-da-pei-surge)
- [Application-Specific Blockchains: The Past, Present, and Future](https://medium.com/1kxnetwork/application-specific-blockchains-9a36511c832)
- [AI 来了，什么技能最值得我们学？](https://mp.weixin.qq.com/s/ifldCMLTSb1Ir-qcyoa5rw)

#### 视频

同样的，也有记录一下看过的有意思的视频：

- [如何启动你的第一个开源项目](https://www.bilibili.com/video/BV1os4y1w78T)
- [又挨骂了！男友迪士尼求生指南](https://www.bilibili.com/video/BV1wm4y127dG)

#### 动漫

- **鬼灭之刃 锻刀村篇**，超级期待！！！希望别崩
- **我推的孩子**，看着讨论度还挺高的，但据说有点刀，看了开头一点点
