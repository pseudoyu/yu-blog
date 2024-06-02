---
title: "周报 #60 - 虫子旁、教育理念与 EpubKit"
date: 2024-06-02T16:30:00+08:00
draft: false
tags: ["review", "life", "nanjing", "nature", "epubkit", "trip", "education", "childhood"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

![weekly_review_20240602](https://image.pseudoyu.com/images/weekly_review_20240602.png)

本篇是对 `2024-05-16` 到 `2024-06-02` 这两周生活的记录与思考。

## 南京游学

![yixi_ticket](https://image.pseudoyu.com/images/yixi_ticket.jpg)

在北京曾看过几次一席的演讲，对他们的风格调性还算喜欢，偶然看到要在南京举办一次亲子游学营，其中有一项安排是参观学姐非常喜欢的一位设计师/作家朱赢椿老师的工作室，于是借了个孩子（我妹）一起报名参加了，因为这两周其实也还没走出四处奔波的疲累，所以原本也没抱有太高的期待，却意外度过了有意思的两天一夜。

### 虫子旁

![zhuyingchun_trip](https://image.pseudoyu.com/images/zhuyingchun_trip.jpg)

大概是由于我有近十年的时间在乡村度过，最开始不是很能理解为什么会有这样一个活动让一群小朋友看虫子，甚至每天工作 debug 的自己也对虫子算不上有太多好感 🤣，但在跟着老师观察各种虫子写的“字”、画的“画”以及吟唱的“乐曲”时，才突然意识到似乎自己已经很久没有好好看过虫子了。

还记得小时候会拿着网兜去捉知了、收集它们褪下的壳珍藏，会在草地里抓蛐蛐来互相争斗，新奇地看着蚂蚁排成队搬运着什么，看到花纹独特的七星瓢虫也会蹲下来观察半天，到了城市后夜晚依然有蝉鸣，在我耳中却只剩噪声和夏日的烦闷。

![zhangyuxuan_speech](https://image.pseudoyu.com/images/zhangyuxuan_speech.jpg)

在《虫子旁》这本书里，老师与随园的虫子为伴，以它们的微观视角看着这个世界，想象着它们的生活琐事，甚至有一个环节是拍了一只小蚂蚁被困在水池中微电影，让队伍中的小朋友们发散想象力画画来拯救它。

或许是我们眼中所需要容纳的东西太多太多，其实它们真实而多彩地生活在我们身旁，却从未被我的目光注视过，随之消失的还有我的童心和对生活的好奇。

![beside_bugs](https://image.pseudoyu.com/images/beside_bugs.jpg)

而学姐的这份童心却似乎以某种方式存在着，会画几队直升机救援队去拯救蚂蚁，也会在老师给她珍藏的《虫子旁》书上签名时提出要画一只毛毛虫，在得偿所愿时还因为追星成功而哭了。

突然想起大半年前的一个午后在学姐家的书架前徘徊想找一本书打发时间时她有推荐过这本和另一本画了各种形态老虎的书，而我随意翻了下就选了另外的、忘了是《加谬手记》还是《未来简史》之类的更为厚重经典的书，时至今日似乎我才慢慢有些体会到这样了解虫子的时刻于她过去人生的重要性。

### 教育理念

![yixi_speech_xuan](https://image.pseudoyu.com/images/yixi_speech_xuan.jpg)

还有一个很有意思的体验是这次游学营最后有一个少年一席演讲环节，每位小朋友需要准备一个主题演讲来分享这两天的所见所思，而我和学姐作为家长席会协助 Brainstorming 和一些指导。

讨论的时间其实只有十几分钟，却非常明显地呈现出了学姐和我教育理念的差异。学姐更多以引导式提问的方式让妹妹一点点发掘几次行程中印象深刻的点和自己想法的变化，而我更倾向于给出更清晰的框架来帮助她整理思路以保障最好的演讲效果。

深切地体会到了人长大后的观念和思维方式常常会是对于自己成长经历中所缺失部分的代偿。

我偶尔会觉得如果童年的许多时刻得到更多的关注和引导会少走一些弯路，对待像是成绩、表演这样会放在聚光灯下评判的事也会更在意结果本身，下意识就会希望她能够在这些方面获取更多的自信和成就感；而学姐或许因为父母是老师，总是会为她规划更多，似乎学生时代的很多事仅需要按部就班完成，也因而少了许多独立和自我探索的机会，因此她会更注重激发妹妹自己的想法和创造力，不论怎样的结果都看作她成长的珍贵体验。

## EpubKit

![epubkit_intro](https://image.pseudoyu.com/images/epubkit_intro.png)

最近几周在参与 [Randy](https://lutaonan.com/) 的产品 [EpubKit](https://epubkit.app/) 的研发工作，在接到他邀请的时候还有些又惊又喜，自己本身是个后端，React 写得半吊子，也还没接触过 Electron，但也很珍惜能够和他亲密合作的机会，产品本身也非常吸引我，于是读了几遍文档，了解了下 IPC 机制后就开始上手写了。

从最开始的新增更新按钮这样的小功能到后面在用户群中收集需求在 GitHub Projects 一项项完成，整个过程非常有趣，也带来了很大的成就感。

而这几周担任开源之夏以及一些训练营项目的导师刚好需要课程资料，于是把之前博客写的区块链/Solidity 相关教程转成了 epub 格式电子书，体验丝滑，也联想到“Eating your own dog food”这一理念，自己参与开发的工具应用恰好满足自己需求的感觉真美好。

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 书籍

- [**海边的卡夫卡**](https://book.douban.com/subject/30144095/)，和《世界尽头与冷酷仙境》相似的双线平行叙事，故事零散地围绕着俄狄浦斯的诅咒、随处可见的隐喻以及少年卡夫卡和老年中田的平淡的旅程故事，各自路途遇到的人、猫却令人印象深刻，都带着不同程度的善和互相救赎，更喜欢中田线。
- [**虫子旁**](https://book.douban.com/subject/35171215/)，去完游学营后开始好奇，里面讲的虫子似乎也都更亲切了些。

#### 收藏

- [Dola - AI 日历助手](https://heydola.com/)

#### 文章

- [运气与努力](https://1byte.io/articles/luck/)

#### 视频

- [vlog #56｜女程序员下班后的学习记录｜调研 Based Rollup｜Taiko 文档｜日常英语学习｜在看《不能承受的生命之轻》｜保持思考与记录](https://www.bilibili.com/video/BV1Kr421L7uD)
- [《代码之外》一周年直播](https://www.youtube.com/watch?v=acxiTIm0CzY)
- [vlog #57 | 女程序员下班后的学习记录｜Rust 学习中｜调研 Substrate｜日常英语学习｜专注自我｜读完《不能承受的生命之轻》](https://www.bilibili.com/video/BV1ei421S7hc)
- [“每天不一定是完美的日子。”](https://www.bilibili.com/video/BV1if421d7uz)

#### 剧集

- [**庆余年 第二季**](http://movie.douban.com/subject/34937650/)，学生时代看过小说且第一季留下的印象很好，还挺期待的，但实际看完实在是有些失望，人设、剧情和节奏都变化很大，还到处穿插着烂梗，实在是对不起这历经五年的“打磨”。
- [**天才：游戏的法则**](http://movie.douban.com/subject/25777620/)，虽然不怎么看综艺但是很喜欢智斗的环节，经推荐周末看了一下，太精彩了。

#### 音乐

- [**Chasing**](https://open.spotify.com/track/2inHbB2phEpzpvJmjJbHGn) by Mameyudoufu
- [**Unsure**](https://open.spotify.com/track/0QUavh8qOxWeGutYZHgymz) by Alan Walker
- [**1 to 10**](https://open.spotify.com/track/23vGlzvoccr0VVm62GTxjG) by Midnight Jogging Club
- [**A Moment**](https://open.spotify.com/track/59wlTaYOL5tDUgXnbBQ3my) Apart by ODESZA
- [**満ちてゆく**](https://open.spotify.com/track/5glPFBAuA1C85tBcVWVzvO) by Fujii Kaze
- [**Spring Snow**](https://open.spotify.com/track/0tCr7DoUBSdtdSl0rxZmct) by 10CM
