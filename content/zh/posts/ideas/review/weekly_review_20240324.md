---
title: "周报 #55 - 油画体验、博客系统升级与对 self-hosting 的思考"
date: 2024-03-24T05:20:00+08:00
draft: false
tags: ["review", "life", "painting", "blog", "cusdis", "remark42", "goatcounter", "self-hosting", "flyio"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/fix_you.mp3" caption="《Fix You - Coldplay》" >}}

## 前言

![weekly_review_20240324](https://image.pseudoyu.com/images/weekly_review_20240324.png)

本篇是对 `2024-03-17` 到 `2024-03-24` 这周生活的记录与思考。

这周重拾了很多工作学习的热情，把 TODO 里列了很久的博客评论系统和数据统计系统迁移做完了，有种整理规置了书桌的舒心感；周末第一次体验了油画，给自己画了一个新头像，成就感满满；恢复了健身；继续学车并报考了科目二；还有很多有意思的事。

## 油画体验与新头像

我和学姐性格和喜好迥异，她有许多我不曾涉足的兴趣爱好，而我着迷的似乎往往也是她未知的领域，于是我们前段时间有立一些 flag 说带对方体验自己的爱好/技能，我定的是双拼和编程这两项，目前双拼已经卓有成效；她则是在这周带我去上了一节油画课。

我对画画其实确实是零基础，也从不觉得自己和这些艺术搭边的爱好有什么关联，只是好奇于究竟是怎样的吸引力能促使她常常在素描或是油画画室坐上大半个下午打磨着一些小细节，期待之余还有些紧张。

![oil_painting_experience](https://image.pseudoyu.com/images/oil_painting_experience.png)

按理说初学者不太会从人像这样的复杂主题开始，只是想要换一个新头像，画室的老师也很 nice 地愿意辅导，选了一张以“头”为主的照片就开始了，画轮廓、调色、上色、根据光线和位置加细节，一切比想象得更加有趣，几种简单的颜色组合能够幻化出很多的层次，创造本身也如同魔术一样令人心驰神往。

![yu_painting](https://image.pseudoyu.com/images/yu_painting.jpg)

一个下午的成果如图，笔触生涩，却是我用自己的画笔创造出来的作品，也有着与众不同的意义，换了全平台的头像。

## 博客系统升级

### Cusdis -> Remark42

之前写过一篇「[轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)」，有讲过我博客使用的是自部署的 [Randy](https://lutaonan.com/) 开源的 [Cusdis](https://cusdis.com/) 评论系统，从 2021 年中就开始使用了，到现在整整三年了，除了最开始的时候因为 Heroku、Railway 相继收费而折腾了一下部署平台外，一直都稳稳地运行着。

不过我在使用中也有遇到一些问题：

1. 大概是由于微信内置浏览器做了一些魔改，在博客从微信聊天/对话打开是看不到评论组件的
2. 尽管可以输入邮箱，但并不支持订阅评论回复
3. 需要管理员手动审核评论，但评论提醒的 TG Bot 时常失效而错过评论

另外因为其核心功能已经许久没有什么更新，比起其他较为成熟的评论系统也显得有些简陋，不过由于我也秉持着够用即可的原则，一直没动迁移/更新的念头，只有在其中一阵子在学前端时还参与了一些 Cusdis V2 版本的开发，不过也没做多久开发小群就不再活跃了。

而最近几个月因为博客几乎没怎么更新，也没收到评论 TG Bot 的提醒，一直以为是没人评论，直到最近数据库托管的 Supabase 平台需要更换一下 Connection String，我才发现原来陆陆续续有几十条评论，有的是关心和鼓励，也有的是咨询一些技术问题，但看到的时候也已经是一两个月后了，还挺不好意思的。

再加上更换数据库 URI 时 Vercel 部署一直报错，于是下定决心从 Cusdis 迁移，调研了一圈后选择了和 [reorx](https://reorx.com/) 在「[更换博客评论系统](https://reorx.com/blog/blog-commenting-systems/)」一文中最后选定的 [Remark42](https://remark42.com/)。

单纯就配置选项来说比起 cusdis 还是丰富了不少，目前配置了常用的几种社交账号登录（GitHub、Twitter、Telegram、邮箱）、可以匿名评论、支持邮件订阅回复提醒并且也设置了 TG bot 提醒，并且部署在 [fly.io](https://fly.io/)，go 单二进制 + 数据库单文件，很舒服的解决方案。

而因为之前积攒了很多评论数据，因为 Cusdis 使用的是 pg 而 Remark42 使用的是 boltdb 单文件数据库，后者不支持远程连接，没法直接 sql 语句写入，只能先联表查询导出需要字段的 json 文件，再手动执行 Migrator 脚本（而因为官方只支持 wordpress、disqus 和 commento 这三个，于是还得手动实现转换逻辑），幸好是熟悉的 go 写的，花了一晚上终于肝完了 [pr](https://github.com/pseudoyu/remark42/pull/1/files)！！！

迁移完才发现这些年一共积攒了 438 条评论，自己都惊到了，都回来了！！！

### Umami -> GoatCounter

本着既然连评论系统都换了的心态，干脆把一直也是个心结的数据统计系统也更新了。

Umami 其实一直用得倒没出现什么问题，直到我更换时尽职地跑了整整一年半，只不过可能因为自己用得比较早，在一次大版本更新的时候数据库 Migration 脚本出现了不兼容的字段更新，其实有点不理解这样量级的开源项目为什么会出现这样的问题，也看到 issue 中有很多其他用户有同样的诉求，但最终并没有给出一个比较好的解决方案。

但是又由于自己已经运行了大半年，舍不得之前的数据，于是一直拖着，直到现在还停留在自己 fork 的一个旧版本，虽然倒也没有对新版本有那么多功能上的诉求，只是有点半强迫症地感觉不舒服，但也就拖着。

于是趁着这次博客大施工，就顺便换为了 [goatcounter](https://www.goatcounter.com/)，同样是 go 单二进制 + sqlite 数据库单文件部署在 fly.io，又是很舒服的配置。

有意思的是，因为 goatcounter 的作者很有坚持，觉得这样单文件的应用容器化反而会增加更多维护成本，所以不提供官方镜像，不过自己在 vps 或者 serverless 平台部署有个镜像还是方便一些，所以用 Github Actions 做了一个 CI 每天拉取最新代码、构建镜像和上传 Docker Hub，有需要的可以使用，对应的 Dockerfile 和 Docker Compose 文件也可以参照[这个 PR](https://github.com/pseudoyu/goatcounter/pull/1/files)。

```bash
docker pull pseudoyu/goatcounter
```

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

这半年的周报输出频率堪忧，除了一篇关于信息管理系统的长文外也没有什么满意的输出，所以决定之前的访问数据就不作迁移了（复杂度应该也高很多），感谢每一位点进我博客网站的赛博朋友们，截图以作留念。

最近感觉折腾这些软硬件/服务配置的心情回归了，也有了很多博客想法，新的数据就当作一个新的开始了 🫡

![yu_goatcounter_data](https://image.pseudoyu.com/images/yu_goatcounter_data.png)

更换的一个最大动力还是 goatcounter 的界面跟我的古早博客主题一样完美卡在我的审美点上，感觉我能一直盯着这个界面看 🤩 无法抗拒这种 Retro Internet 设计。

## 关于 self-hosting 的一些思考

其实我对于 vps 和 serverless 平台经历过许多次的折腾和反复，算不上心得，但确实是深度体验后的经验之谈了。

曾经的我算是 serverless 的拥趸，当时几乎是能在 Vercel/Railway 等 PaaS 平台部署的绝不自己搭建，能在几乎没有运维成本的前提下还能获得媲美大平台的稳定性，也确实践行了把自己的各项服务都 serverless 化了，确实经历过很长一段时间的省心省力。

然而随着经历过 HeroKu 和 Railway 相继中途改变收费模式，以及 n8n 在 Railway 上跑出单月十几刀的账单时，才也逐渐发现一些弊端，serverless 确实是减少了对于自己运维服务器的要求，但相对应地也要受制于这些平台的规则。

收费模式其实只是一部分缘由，比起自己租赁一台配置不错的服务器，成本倒是还好，只是似乎又将自己的服务和数据绑定在一个中心化平台了，会有一种任人宰割的不安全感；而当想要迁移到另一个平台时，往往平台不会给出较为方便的解决方案，自己去折腾的操作复杂度比起服务器之间 docker-compose 文件外加挂载 volume 直接复制要高不少。

![vps_service_01](https://image.pseudoyu.com/images/vps_service_01.png)

![vps_service_02](https://image.pseudoyu.com/images/vps_service_02.png)

因此也把自己的很多服务都放在服务器上，稳定地跑了 430+ 天。

![xiao_self_hosted](https://image.pseudoyu.com/images/xiao_self_hosted.png)

而前几天和 [reorx](https://reorx.com/) 聊到服务部署方案时，他提到了现在会优先考虑 sqlite 或其他同类文件数据库的 self-host 方案，能够减少许多维护和迁移的成本和复杂度。

后来我想了想，其实不管是在 vps 还是 serverless 平台，本质上都是 self-hosting 的选择，其实更多需要的是思考部署的服务依赖本身，如我之前 Cusdis、Umami 很多不稳定性来源其实是在服务端在 Vercel、Netlify 这样的 PaaS，而数据却托管在 Supabase 这样的 DaaS，一个自用的服务同时依赖两个平台，任何一方出了问题都会导致服务不可用，vps 所做的其实也不过是把这样的风险变为单点自己维护而已。

![flyio_services](https://image.pseudoyu.com/images/flyio_services.png)

于是又久违地开始折腾，把 Remakr42 与 GoatCounter 都部署在了 [fly.io](https://fly.io/) 上，因为单二进制+文件数据库，性能消耗完全在 free plan 的范围内；而把 RSSHub、n8n、图床等相对依赖更重且需要对外提供服务的应用还是继续更集中地放在 vps 上；而把一些性能或存储消耗较高的服务则是跑在 Home Server 上并且通过内网穿透方案来暴露。

## 其他

![applite_overview](https://image.pseudoyu.com/images/applite_overview.png)

把 Mac 从各个来源安装的软件都统一了一下，原则就是能 brew cask 安装的都重新安装，之前命令行需要自行搜索没什么感觉，现在有了 GUI 查看后发现确实软件源比想象得丰富很多，这种方式便于管理/迁移且相对能保障软件的来源安全性 🫡

从 RapidAPI 切换到一个新的 API 调试工具 [Bruno](https://www.usebruno.com/)，预购了它的 Golden Edition，目前使用起来体验很不错。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 书籍

- [**红与黑**](https://book.douban.com/subject/35781152/)，从一个视频看到的讲解，关于于连的自尊和因此表现出来的傲慢的描述印象很深，正在看。
- [**加缪手记**](https://book.douban.com/subject/34802764/)，刚开始看。

#### 收藏

- [GitHub - milanvarady/Applite](https://github.com/milanvarady/Applite)
- [GitHub - usebruno/bruno](https://github.com/usebruno/bruno)
- [GitHub - plankanban/planka](https://github.com/plankanban/planka)

#### 文章

- [Mental Health in Open Source](https://antfu.me/posts/mental-health-oss)
- [重新理解 Heptabase](https://justgoidea.com/posts/2024-009/)
- [Demystifying Docker for JavaScript](https://fly.io/javascript-journal/demystify-docker-js/)

#### 视频

- [去东京，我只做三件事！](https://www.bilibili.com/video/BV131421Q7KT)

#### 剧集

- [**三体 第一季**](http://movie.douban.com/subject/35196946/)，在看。
