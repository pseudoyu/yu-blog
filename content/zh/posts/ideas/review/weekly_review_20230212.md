---
title: "周报 #30 - 开源预算、写作初心与对技术的谦卑"
date: 2023-02-12T19:41:33+08:00
draft: false
tags: ["review", "life", "home", "cat", "writing", "technology", "music", "spotify", "open-source"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/christmas_song_english_version.mp3" caption="《クリスマスソング (English Cover) - Matt Cab》" >}}

## 前言

![weekly_review_20230213_photo](https://image.pseudoyu.com/images/weekly_review_20230213_photo.png)

本篇是对 `2023-02-07` 到 `2023-02-12` 这周生活的记录与思考。

这一周工作上不算有太多进展，却感觉年后的时间感觉过得尤其快，明明好像也没做什么有价值的事，却处于一种忙碌之中。但额外的项目部分终于开始投入不小的时间在处理了，离原本的预期有些偏差，也带来了一些焦虑，算是在慢慢排解。

这周受公司运营之托写了一篇关于 Cosmos 的文章，在写作和发布过程中倒是有些心态上的警醒，也引发了自己对于写作初心与对技术的谦卑的一些思考。

周末去了国家大剧院听了场音乐会，之前一直想听交响乐不过少有机会，终于解锁了周末新去处；周末和我目前评论系统 [Cusdis](https://cusdis.com/) 的作者 [Randy](https://lutaonan.com/) 聊了一下（顺便报了几个 bug），感觉是个很纯粹的技术人，希望在 Cusdis v2 版本的开发中自己也能有所贡献；还有很多有意思的事。

## 开源预算

在 [Randy](https://lutaonan.com/) 的一篇文章『[我给自己设立了每月 $20 的开源捐赠预算](https://lutaonan.com/blog/my-oss-donation-budget/)』中看到他对于开源项目的理念与态度，觉得很有意思，也引发了我想为自己也设立一个同样的开源预算的想法。

目前的设定是每月至少 $20（约 130 元人民币）或等价值的预算，根据自己的日常使用与技术栈灵活选择，我会选择以下项目进行捐赠：

- 对我有启发的独立博客作者与开发者
- 我在做 side projects 时常用且解决了很切实问题的项目
- 我高频使用的一些有趣的开源工具与服务

目前我捐赠的项目为：

- [Reorx](https://github.com/reorx)，一个我很欣赏的开发者，他的独立博客、对于工具的态度与探索以及开发的一些项目都让我获益良多，我的『[Yu's Life](https://t.me/pseudoyulife)』频道就是 fork 于他的『[Reorx’s Footprints](https://t.me/reorx_share)』，在大半年的时间里重塑了我的信息输入输出流，最近刚发布的『[GitHub - jsoncv](https://github.com/reorx/jsoncv)』也恰好在我重构简历时帮了大忙。
- [immersive-translate](https://github.com/immersive-translate/immersive-translate)，是 [owen](https://www.owenyoung.com/) 主导开发的一款沉浸式翻译插件，是一个很有趣的工具，且 owen 在非常勤劳地开发 v2 版本，我早早加入了团队，目前也在认领一些需求进行开发，在团队讨论得知需要一些服务器时，提供了两台。

可以在 [GitHub Sponsor](https://github.com/pseudoyu?tab=sponsoring) 看到我对哪些项目和个人进行了捐赠。

## 写作初心

自己其实一直以来还算喜欢写作，尤其是这大半年的输出达到了还不错的频率和质量，因为长期写博客也认识了不少朋友，甚至偶尔也能得到一些不错的机会。但随着自己的文字功底随着积累增长，也常常得到一些挺正向的反馈，却似乎有时候会陷入一种写作的陷阱。最近发生的一件事让我有些警醒。

公司的媒体运营在年前跟我约了一篇稿件，主题并不限制，大致方向是有关公司业务技术的就可以，因为当时时间还多，就先应承了，但过年期间也就搁置了。回北京返工后被催稿时才记起，但又不想很敷衍了事，所以选择了一个 Cosmos 底层链和共识分析的大主题，花了一晚上写完了。

其实交稿时还没什么，因为大部分知识点也是出自于对一本书籍的梳理总结，想着可能只会是一些细节微调，然而交到一位精于底层链的 leader 手上审核时，却有了如下对话。

![zgtech_cosmos_article_review_kai](https://image.pseudoyu.com/images/zgtech_cosmos_article_review_kai.png)

查看了用于审稿的分享链接，发现他在我的文章一些存疑的细节中做了十分详尽的标注，很多部分还带论文与引用。

![zgtech_cosmos_article_review_3](https://image.pseudoyu.com/images/zgtech_cosmos_article_review_3.png)

起初只是觉得，自己是不是有些过于盲目相信所读的书籍与知识点了，而少了一些应有的怀疑与求证精神。

又深思了一下整件事发生的全过程，发现是自己的心态产生一些微妙的改变。自己似乎一直以来是挺擅长驾驭文字的，有时候是梳理总结一些知识点并以一种易读有趣的方式呈现，有时候是通过文字表达和呈现自己的一些想法与思考。

文字似乎成为了自己习惯的表达方式，也因为有了不少正向反馈，所以似乎有一些失了本心。写作本身源于对生活与一些事物、技术的探究与呈现，其次才是分享与为他人创造价值，自己似乎慢慢有些把分享这件事作为了一种目的。

论语中有一句话：

> “质胜文则野，文胜质则史。文质彬彬，然后君子。” —— 《论语·雍也篇》

其实蛮适用于写作的。当质（写作中的干货）太多而文（文采/技巧）太少，则少了一些吸引人看下去的乐趣，也失去了写作的魅力；而文胜过质则容易虚浮，缺乏实质性的内容，则失去了写作的意义。只有文和质兼具，才可以说是一篇好的文章。

我想我或多或少会担心自己向文胜过质的方向倾斜，好在有这次的事及时警醒，后面也会更加谨慎对待自己的文字。

## 对技术的谦卑

这其实又关联到一个挺值得探讨的话题，即对技术的谦卑之心。

我想处于这个行业的人或多或少都能意识到技术的无止境，编程入门或是以之为业其实只是一个开始，有太多值得敬佩的人，也有太多有趣的技术。

我其实是带着滤镜进入这个行业的，在还是一个英语专业本科生的时候对这个行业和职业充满了太多幻想与期待，因此如愿从事了开发工作后，就时常提醒自己一定要对技术有着谦卑之心。

因为看到了太多前后端都很强的开源大佬称自己为“会写一点后端的前端”或是“做点大家喜欢的小玩意”，很喜欢这样的态度，技术本身是乐趣与实现自己想法的一些手段，而不是需要拿出来炫耀的工具，对技术需要抱有这样的一种理念，才能不断学习成长。

## 有趣的事与物

### 软件

之前自己其实一直用 Apple Music 居多，但是有些操作逻辑实在是有点无语，歌单功能形同虚设，而且由于接口的一些封闭性，很难获取自己的数据。因此，即使我的 Telegram 频道其实原本就配置了 Spotify 点赞歌曲的自动同步，每次都是在 Apple Music 听到好听的歌后，去 Spotify 搜索，且由于免费版本的广告和试听切歌限制等很麻烦，所以其实很少同步自己的一些歌。

![spotfiy_service_family](https://image.pseudoyu.com/images/spotfiy_service_family.png)

![spotfiy_service_family_mail](https://image.pseudoyu.com/images/spotfiy_service_family_mail.png)

最近和倪、占的 iCloud Family 正在迁移逃离云上贵州，停掉了原本的服务，对比了一下港区价格发现还不如直接迁移到 Spotify 了，于是快乐地拥有了 Spotify Premium 了，体验起来舒服很多了，再加上之前看了『[串流先锋](https://movie.douban.com/subject/35500137/)』剧集，总有一种奇妙的参与感！

再加上占在香港办宽带送的 Netflix 家庭会员，影音娱乐这一块现在有了很无缝的体验！

### 输入

虽然大部分有意思的输入会在 『[Yu's Life](https://t.me/pseudoyulife)』Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 文章

- [黑客与顾客：开源软件能商业化吗？ | 夜天之书](https://www.tisonkun.org/2023/02/05/hackers-and-customers/index.html)
- [ChatGPT 是網路上的一個模糊 JPEG 文件](https://foxhsiao.medium.com/chatgpt-%E6%98%AF%E7%B6%B2%E8%B7%AF%E4%B8%8A%E7%9A%84%E4%B8%80%E5%80%8B%E6%A8%A1%E7%B3%8A%E7%9A%84jpeg%E6%96%87%E4%BB%B6-aaee3723db1f)
- [我看 ChatGPT: 为啥谷歌掉了千亿美金 | 酷 壳 - CoolShell](https://coolshell.cn/articles/22398.html)
- [The 4 Levels of Personal Knowledge Management - Forte Labs](https://fortelabs.com/blog/the-4-levels-of-personal-knowledge-management/)
- [The latest gossip on BFT consensus - Tendermint](https://arxiv.org/pdf/1807.04938.pdf)
- [HotStuff: BFT Consensus in the Lens of Blockchain](https://arxiv.org/pdf/1803.05069.pdf)

#### 播客

记录了一些自己在听的播客：

- [10. 情人节前，让我们回顾恋爱日剧的黄金时代 - | Listen Notes](https://www.listennotes.com/podcasts/%E8%BE%B9%E8%A7%92%E8%81%8A/10-%E6%83%85%E4%BA%BA%E8%8A%82%E5%89%8D%E8%AE%A9%E6%88%91%E4%BB%AC%E5%9B%9E%E9%A1%BE%E6%81%8B%E7%88%B1%E6%97%A5%E5%89%A7%E7%9A%84%E9%BB%84%E9%87%91%E6%97%B6%E4%BB%A3-mCUhvzVsEi7/)

#### 视频

同样的，也有记录一下看过的有意思的视频：

- [你对 AI 的理解可能从根儿上就错了【关于 AI 的一些元问题】](https://www.bilibili.com/video/BV14s4y1Y7nu)
- [功绩社会生产抑郁症患者和厌世者？](https://www.bilibili.com/video/BV1WM411Y7Jk)
- [公开呼吁取关？！一条视频席卷全国，衣戈猜想走红真的是偶然吗？](https://www.bilibili.com/video/BV1WD4y1N7jJ/)
- [我办的音乐比赛炸出了这么多大佬? [图一乐作品 PICK]](https://www.bilibili.com/video/BV15Y411B7Jt)
- [重启 20 年前的索尼监视器和游戏主机，需要几步？](https://www.bilibili.com/video/BV1i8411T7cn)

### 输出

#### 博客

- [Cosmos 区块链架构与 Tendermint 共识机制 · Pseudoyu](https://www.pseudoyu.com/zh/2023/02/10/cosmos_introduction_and_explaination/)

## 个人生活剪影

### 生活

这周大部分时间在公司，所以格外期待周末的到来。

周六的时候和博译学姐去国家大剧院听了一场贝多芬的音乐会，之前我总是会去三里屯那边的爱乐汇轻音乐团去听一些小型的主题演出，像是宫崎骏、爱乐之城与百年经典等专题，小小的空间气氛很好，不过当时就也想着感受一下交响乐的震撼，终于得偿所愿！

![beethoven_symphony_concert_ticket](https://image.pseudoyu.com/images/beethoven_symphony_concert_ticket.jpg)

![beethoven_symphony_concert_live](https://image.pseudoyu.com/images/beethoven_symphony_concert_live.jpg)

很有意思的是看完音乐会出来后就买了莫扎特的胸针（谁让他更可爱），还发表了如下茶言茶语。

![beethoven_symphony_concert_tweet](https://image.pseudoyu.com/images/beethoven_symphony_concert_tweet.png)

> 今日份茶言茶语。“刚听完贝多芬专场音乐会转头就买了莫扎特的胸针，他会不会伤心啊？”

在发完推后还很巧合地认识了相同时空同在国家大剧院的推友 [Noy](https://twitter.com/Noy_eth)，发现也是做 web3 开发相关的，周末也爱去看一些剧和音乐会，约了面基，之后可以一起去看了！

还有一个小惊喜就是我们在大剧院落座路过一个外国帅哥时，他说了一句“I love his hair”，来自陌生人的友好就很开心。现在顶着一头蓝色长发真的越来越二次元了，回头率 300%。

### 捏捏

#### 叫我起床的捏捏

因为我不起床开罐头而直接爬上被子给我一拳的捏捏。

![my_very_cute_nie_nie_on_bed_01](https://image.pseudoyu.com/images/my_very_cute_nie_nie_on_bed_01.jpg)

![my_very_cute_nie_nie_on_bed_02](https://image.pseudoyu.com/images/my_very_cute_nie_nie_on_bed_02.jpg)

#### 撒娇的捏捏

最近捏捏又特别会撒娇，经常在桌子上歪头杀。

![my_very_cute_nie_nie_on_mac_01](https://image.pseudoyu.com/images/my_very_cute_nie_nie_on_mac_01.jpg)

![my_very_cute_nie_nie_on_mac_02](https://image.pseudoyu.com/images/my_very_cute_nie_nie_on_mac_02.jpg)

跟朋友分享后，捏捏以一猫之力拉高了别人家的小猫吃猫粮的标准，哈哈。

![my_very_cute_nie_nie_on_mac_tg_chat](https://image.pseudoyu.com/images/my_very_cute_nie_nie_on_mac_tg_chat.png)
