---
title: "周报 #31 - 开源、前端开发与 ChatGPT 实践"
date: 2023-02-20T21:51:11+08:00
draft: false
tags: ["review", "life", "home", "cat", "beer", "programing", "chatgpt", "open-source", "ai", "front-end", "nextjs", "prisma"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/christmas_song_english_version.mp3" caption="《クリスマスソング (English Cover) - Matt Cab》" >}}

## 前言

![weekly_review_20230220_photo](https://image.pseudoyu.com/images/weekly_review_20230220_photo.png)

本篇是对 `2023-02-13` 到 `2023-02-20` 这周生活的记录与思考。

这一周工作和各种自己的项目安排异常满，虽然其实也不是真的忙到一点睡觉的时间都没有，但是因为有了很多莫名的焦虑感和低迷情绪，导致常常有些报复性熬夜的倾向，看了看手机给我记录的每天平均睡眠不足 3 小时。

这周情人节被豆瓣电影日历触发了一些心绪，想到了一些过去的事；下定决心折腾了一下买了 ChatGPT Plus，配合上 GitHub Copilot，节省了很多重复性的工作；因为最近一直在折腾这个，还去博译学姐的财经直播间里科普了一个小时 AIGC 和 ChatGPT，直播首秀，很新奇的体验；周末因为实在太压抑，和朋友去跳海酒馆喝了点酒，是难得的放松时刻；之前的 Side Project 疯狂拖延，到了周末几乎通宵两天，疯狂写前端；参加了 Cusdis v2 的开发团队，也写了第一个功能，作为一个后端给第一个比较大的开源项目提的 PR 居然是 Next.js 的，有点离奇；还有很多有意思的事。

## 开源与前端学习

虽然自己好像还是挺活跃在 GitHub、推特和博客的，但是因为其实工作年限比较短，而且当前工作也还并不是开源性质的，所以其实并没有怎么以代码贡献的方式参与过什么大型的开源项目，倒是几个 Markdown 和课程作业项目拿了不少 star，让我常常有些不太好意思。

所以今年年初也还是立了一些 Flag，多多以各种形式参与一些自己感兴趣的开源项目，包括在上周自己还给自己定了一个开源预算（详见『[周报 #30 - 开源预算、写作初心与对技术的谦卑](https://www.pseudoyu.com/en/2023/02/12/weekly_review_20230212/)』），也给 RSS3 提了一些 Issues，算是一个好的开始了。

有一个挺有意思的事是看到 [Randy](https://lutaonan.com/) 在推特上找一起开发 Cusdis v2 版本的伙伴，我用 [Cusdis](https://cusdis.com/) 已经接近两年了（即本博客的评论系统），非常喜欢这样简约且强大的系统，也帮一些朋友创建或是解决了一些部署和使用的问题，也差不多是移动的广告牌了。

虽然我不是前端，但因为太感兴趣了还是加了 TG 聊了一下，Randy 真的是个很纯粹的技术人，也很友好，我简单陈述了自己的情况和想法后，他让我先拉一下最新代码，能跑起来再聊（顿时有点面试的感觉）。

我粗略看了一下代码结构与命令，因为之前写 Solidity 一直用的是基于 JavaScript 的 Hardhat 框架，而后面学前端的时候也了解了 TypeScript，所以对包安装管理、一些基础命令还是比较熟悉的，只是从 yarn 换成了 pnpm，折腾了一下环境，在服务器上用 Docker 启动了一个 PostgreSQL 实例，就运行起来了（后来发现其实本地 sqlite 就可以了，不用绕那么大一圈）。

然后就是让我看了一下现在的基础功能，看看对哪一块比较感兴趣，于是我开始慢慢看代码，并且还提了一些 v1 版本的 Bug 给他（迅速都修复了，强大的执行力），接着工作项目很忙，就没开始写，但是期间看了一本 Randy 写的 Next.js 开发的小书:

- [Next.js 应用开发实践](https://nextjs-in-action-cn.taonan.lu/)

这本书真的超级好，是我写 Next.js 以来在代码实践上讲得最清楚的资料了，其中有 Query、Mutation 和通过 Query Invalidation 来强制刷新数据等最佳实践，也推荐了 Prisma 这个超好用的 ORM 库，前面的理论讲解很清晰易懂，后面还附了两个实例项目，非常值得一看。

![side_project_api_structure](https://image.pseudoyu.com/images/side_project_api_structure.png)

看完这本书后，我废弃了做了一半的 Side Project 的 Go 后端，花了一整个周末把后端逻辑实现部分在 Next.js 的 api 模块用 Prisma 连接 PostgreSQL 数据库的方式重构了，刚开始写的时候有些不太习惯，在用户管理和鉴权这一块一边看着那本小书的代码一边照着修改，后面的其他功能就比较顺手了，也算是一个比较完整的实践了，称赞一下 Next.js + TailwindCSS + Prisma 的组合带来了非常好的开发体验，很适合独立开发一些项目。

而经过了周末两天的狂写代码，对前端这一块实现上的信心也增长了不少，于是找 Randy 去领了开发任务，功能不复杂，就是使用 Mutation 实现用户保存评论提醒所需要的 Webhook 连接配置的逻辑，并且加上一些加载中状态、toast 提示等效果，但也是一个还不错的开端。

![chat_with_randy_01](https://image.pseudoyu.com/images/chat_with_randy_01.png)

实现过程还遇到一些问题请教了他，也给了很耐心的解答。最后终于在晚上完成了这个 PR。

- [feat: save webhook settings logic \(with loading and toast\) by pseudoyu · Pull Request \#241 · djyde/cusdis](https://github.com/djyde/cusdis/pull/241/commits/914888031bc69628f061fd55a76d8c07402173a5)

![chat_with_randy_02](https://image.pseudoyu.com/images/chat_with_randy_02.png)

其实这种体验还蛮有意思的，自己在几乎没写过前端项目的时候去尝试参与开源，得到了很敬佩的开发者的帮助和引导，可能有时候主动一些也会有意料之外的收获。不过想到自己作为一个区块链后端开发，加入的第一个比较大的开源项目和提的第一个功能性 PR 居然是前端的，也是奇妙的体验了。

大家有兴趣可以尝试一下 [Cusdis](https://cusdis.co)，之前也写过一篇部署介绍的文章可以参考：

- [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway） · Pseudoyu](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)

## ChatGPT

自己最早就是 GitHub Copilot 内测玩家，第一次用上就惊叹不已，原来 AI 在代码这一块就已经能做到这样的程度了，后面也持续在使用，大概也有一年多了；后来也同样高频用到的是 DeepL 的机器翻译，质量感觉比 Google 翻译好很多，也辅助我完成了很多开源的翻译项目；再之后就是 Notion AI 了，不过因为后来完全从 Notion 转移到了 Logseq，所以尝了个鲜就搁置一旁了；同类的还有之前黑五买的 Craft，一个在线笔记软件，也内置了小助手来优化文本；而最最重磅级的当属去年年末推出的 ChatGPT 了。

我记得约 11 月底推出，我在 12 月初找在澳洲的倪接了个手机验证码开始体验了。当时就常常用来问一些代码问题，基本上都能给出比较准确的回答，但由于自己其实还是更偏向于 GitHub Copilot 这种比较无感的方式，而并不想每次都组织一堆语言去问问题，再粘贴代码回来编辑，所以玩了一阵子其实也就搁置了，只是在学一些新技术的时候偶尔打开看看。

![chatgpt_assistant_usage](https://image.pseudoyu.com/images/chatgpt_assistant_usage.png)

而上周偶然看到[自力](https://twitter.com/hzlzh)使用 ChatGPT 作为小助手的用法，很心动，经过一番虚拟信用卡之类的折腾终于搞定了 Plus 会员，20 美元一个月的的不菲开销让我开始梳理自己的日常使用需求，最后把编程代码问题、日语学习、中英翻译、搜索引擎、文案优化等需求分成了多个对话框进行使用，每天像是有一堆小助手一样，可热闹。

最近有不少写前端的事，之前虽然也看过课学习过，但是还是有很多细节不算很清楚，这时候面向 ChatGPT 提问和从它的回答中过滤正解以及消化为自己的知识其实也还蛮有效的，而且很偏实战，也会提出不少新颖的实现思路，语言学习应该也是同理，但还没来得及好好测试日语学习的效果，后面如果有意思可以记录一下对话。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 『[Yu's Life](https://t.me/pseudoyulife)』Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 文章

- [Next.js 应用开发实践](https://nextjs-in-action-cn.taonan.lu/)
- [入行 14 年，我还是觉得编程很难 | Piglei](https://www.piglei.com/articles/programming-is-still-hard-after-14-years/)
- [马桶里的大厂病 - hayami's blog](https://hayami.typlog.io/bullshitjobs)
- [Re:Play Issue 25 - 浪漫至死](https://newsletter.replay.cafe/re-play-25-lang-man-zhi-si/)
- [The 4 Levels of Personal Knowledge Management - Forte Labs](https://fortelabs.com/blog/the-4-levels-of-personal-knowledge-management/)
- [Real-world Engineering Challenges \#8: Breaking up a Monolith](https://newsletter.pragmaticengineer.com/p/real-world-eng-8)
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)

#### 播客

记录了一些自己在听的播客：

- [ep.2 跳海酒馆：世界在下沉，我们要建造 - 牌牌坐 | 小宇宙](https://www.xiaoyuzhoufm.com/episode/63146f53e50e37575adb1cbe)
- [Vol. 84 数码荔枝: 正版软件生态、独立开发与远程办公 - 枫言枫语 \(播客\) | Listen Notes](https://www.listennotes.com/zh-hans/podcasts/%E6%9E%AB%E8%A8%80%E6%9E%AB%E8%AF%AD/vol-84-%E6%95%B0%E7%A0%81%E8%8D%94%E6%9E%9D-%E6%AD%A3%E7%89%88%E8%BD%AF%E4%BB%B6%E7%94%9F%E6%80%81%E7%8B%AC%E7%AB%8B%E5%BC%80%E5%8F%91%E4%B8%8E%E8%BF%9C%E7%A8%8B%E5%8A%9E%E5%85%AC-Y-Uq0g5CrZM/)
- [ChatGPT 的出圈与大佬们的焦虑 - 科技乱炖 \(播客\) | Listen Notes](https://www.listennotes.com/zh-hans/podcasts/%E7%A7%91%E6%8A%80%E4%B9%B1%E7%82%96/chatgpt%E7%9A%84%E5%87%BA%E5%9C%88%E4%B8%8E%E5%A4%A7%E4%BD%AC%E4%BB%AC%E7%9A%84%E7%84%A6%E8%99%91-WgOpJNm435Z/)
- [\#20 一年一度败家节目 2022 - 二分电台 \(podcast\) | Listen Notes](https://www.listennotes.com/podcasts/%E4%BA%8C%E5%88%86%E7%94%B5%E5%8F%B0/20-%E4%B8%80%E5%B9%B4%E4%B8%80%E5%BA%A6%E8%B4%A5%E5%AE%B6%E8%8A%82%E7%9B%AE-2022-Wz84cHdvN-u/)

#### 视频

同样的，也有记录一下看过的有意思的视频：

- [情人节 8.0｜音乐，是世界上最通用的情书](https://www.bilibili.com/video/BV1PG4y1P7vm/)
- [你离爱情只差一句骚话，教你正确使用爱情骚话](https://www.bilibili.com/video/BV1JA411z7KM/)
- [How I Coded An Entire Website Using ChatGPT - YouTube](https://www.youtube.com/watch?v=ng438SIXyW4)

## 个人生活剪影

### 跳海酒馆

![sea_bar_outside](https://image.pseudoyu.com/images/sea_bar_outside.jpg)

![sea_bar_wine](https://image.pseudoyu.com/images/sea_bar_wine.jpg)

周末和朋友去了跳海酒馆，一个在胡同里的小小的酒吧，拥挤但算不上嘈杂，却别有一番热闹，里面写着大大的“有人跳海”四个字。和恰巧来北京出差的朋友畅聊了很久，连这周带着些阴霾的情绪也缓解了不少，新的一周也要好好调整。

### 捏捏

![my_lovely_nie_nie_01](https://image.pseudoyu.com/images/my_lovely_nie_nie_01.png)

> 去『跳海酒馆』喝了点酒，到家已经大概 1 点，没多久就昏睡过去。刚迷迷糊糊睁眼发现捏捏似乎凑在我的脸上努力闻着什么，时不时还用小爪子试探性地碰一下，脑子（重启后）转了好一会儿才反应过来她是在担心我是不是还活着。黑暗中慌忙打开手机抓拍了一张，顿时感受到了些许久违的温暖和依靠。

![my_lovely_nie_nie_02](https://image.pseudoyu.com/images/my_lovely_nie_nie_02.png)

> 她一定知道自己很可爱！

### 情人节

![valentine_douban](https://image.pseudoyu.com/images/valentine_douban.png)

不得不说豆瓣电影日历的选片人还是有点心思的，情人节放花束般的恋爱，然后配上一句：

> 恋爱就像派对，总有一天会结束。
