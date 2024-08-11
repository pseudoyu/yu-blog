---
title: "Weekly Review #31 - Open Source, Front-end Development and ChatGPT Practice"
date: 2023-02-20T21:51:11+08:00
draft: false
tags: ["review", "life", "home", "cat", "beer", "programing", "chatgpt", "open-source", "ai", "front-end", "nextjs", "prisma"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/christmas_song_english_version.mp3" caption="'Christmas Song (English Cover) - Matt Cab'" >}}

## Preface

This piece is a record and reflection of my life from February 13, 2023 to February 20, 2023.

This week was exceptionally full with work and various personal projects. Although I wasn't truly busy to the point of having no time to sleep, I developed an inexplicable sense of anxiety and low mood, often leading to a tendency for revenge bedtime procrastination. Looking at my phone's sleep record, I averaged less than 3 hours of sleep per day.

This week, Valentine's Day triggered some emotions through the Douban Movie Calendar, reminding me of past events. I made up my mind to tinker a bit and bought ChatGPT Plus, which, combined with GitHub Copilot, saved me a lot of repetitive work. Because I've been fiddling with this recently, I even went to BoYi's financial live streaming room to popularize AIGC and ChatGPT for an hour - my live streaming debut, quite a novel experience. On the weekend, feeling too depressed, I went to the Sea Dive Bar with friends for some drinks, a rare moment of relaxation. My previous side project was severely delayed, leading to almost two sleepless nights over the weekend, frantically writing front-end code. I joined the development team for Cusdis v2 and wrote my first feature. Strangely, as a backend developer, my first PR for a relatively large open-source project turned out to be for Next.js, which was quite unexpected. There were many other interesting things as well.

## Open Source and Front-end Learning

Although I seem to be quite active on GitHub, Twitter, and my blog, due to my relatively short work experience and my current job not being open-source in nature, I haven't really participated in any large open-source projects in terms of code contributions. Instead, I've gained quite a few stars for some Markdown and course assignment projects, which often makes me feel a bit embarrassed.

So at the beginning of this year, I set some goals to participate in various forms of open-source projects that interest me. This included setting an open-source budget for myself last week (see "Weekly Review #30 - Open Source Budget, Writing Aspirations, and Humility Towards Technology"). I also raised some issues for RSS3, which is a good start.

An interesting thing happened when I saw Randy on Twitter looking for partners to develop Cusdis v2. I've been using Cusdis for almost two years now (i.e., the comment system for this blog), and I really like this simple yet powerful system. I've also helped some friends create or solve some deployment and usage issues, almost becoming a walking advertisement for it.

Although I'm not a front-end developer, I was so interested that I joined the TG chat. Randy is truly a pure technologist and very friendly. After I briefly stated my situation and thoughts, he asked me to pull the latest code first and get it running before we talked further (suddenly feeling like an interview).

I briefly looked at the code structure and commands. Because I had been using the JavaScript-based Hardhat framework for writing Solidity, and had learned about TypeScript when studying front-end later, I was quite familiar with package installation management and some basic commands. The only difference was switching from yarn to pnpm. After tinkering with the environment a bit and starting a PostgreSQL instance on the server using Docker, I got it running (later I found out that local sqlite would have been sufficient, no need for such a roundabout way).

Then he asked me to look at the current basic functions and see which part I was more interested in. So I started slowly reading the code and even raised some v1 version bugs to him (which were quickly fixed, showing powerful execution). Then work projects got busy, so I didn't start writing, but during this time I read a small book on Next.js development written by Randy:

- [Next.js Application Development Practice](https://nextjs-in-action-cn.taonan.lu/)

This book is really super good. It's the clearest explanation I've seen on code practices since I started writing Next.js. It covers best practices such as Query, Mutation, and using Query Invalidation to force data refresh, and also recommends Prisma, a super useful ORM library. The theoretical explanations at the beginning are very clear and easy to understand, and there are two example projects attached at the end, which are very worth reading.

![side_project_api_structure](https://image.pseudoyu.com/images/side_project_api_structure.png)

After reading this book, I abandoned the Go backend of my half-done Side Project and spent an entire weekend restructuring the backend logic implementation part in the Next.js api module using Prisma to connect to the PostgreSQL database. At first, I felt a bit uncomfortable, looking at the code in that little book and modifying it accordingly for user management and authentication. Later, the other functions became more handy, and it was also a relatively complete practice. I must praise the combination of Next.js + TailwindCSS + Prisma for bringing a very good development experience, very suitable for independently developing some projects.

After two days of intense coding over the weekend, my confidence in front-end implementation also grew considerably. So I went to Randy to take on a development task. The function wasn't complicated, just using Mutation to implement the logic for users to save the Webhook connection configuration needed for comment notifications, and adding some loading states and toast notifications. But it was still a good start.

![chat_with_randy_01](https://image.pseudoyu.com/images/chat_with_randy_01.png)

I encountered some problems during the implementation and consulted him, and he gave patient answers. Finally, I completed this PR in the evening.

- [feat: save webhook settings logic \(with loading and toast\) by pseudoyu · Pull Request \#241 · djyde/cusdis](https://github.com/djyde/cusdis/pull/241/commits/914888031bc69628f061fd55a76d8c07402173a5)

![chat_with_randy_02](https://image.pseudoyu.com/images/chat_with_randy_02.png)

This kind of experience is quite interesting. Trying to participate in open source when I had hardly written any front-end projects, I received help and guidance from developers I greatly admire. Sometimes being proactive can lead to unexpected gains. However, thinking that as a blockchain backend developer, my first contribution to a relatively large open-source project and my first functional PR turned out to be front-end, it's quite a peculiar experience.

If you're interested, you can try [Cusdis](https://cusdis.co). I've also written an article about deployment before, which you can refer to:

- [Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway) · Pseudoyu](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)

## ChatGPT

I was an early beta tester for GitHub Copilot, and was amazed the first time I used it. I couldn't believe AI could already do so much in terms of code. I've been using it continuously since then, for about a year and a half now. Later, I also frequently used DeepL's machine translation, which I feel is much better quality than Google Translate, and it has helped me complete many open-source translation projects. After that came Notion AI, but because I later completely moved from Notion to Logseq, I just tried it out and then set it aside. Similar to this is Craft, an online note-taking software I bought during Black Friday, which also has a built-in assistant to optimize text. But the most heavyweight of all is undoubtedly ChatGPT, which was launched at the end of last year.

I remember it was launched around the end of November, and I started experiencing it in early December after getting a phone verification code from Ni in Australia. At that time, I often used it to ask code questions, and it could basically give fairly accurate answers. But because I actually prefer the more seamless approach of GitHub Copilot, and didn't want to organize a bunch of language to ask questions every time and then paste the code back for editing, I played with it for a while and then set it aside, only occasionally opening it to look at some new technologies.

![chatgpt_assistant_usage](https://image.pseudoyu.com/images/chatgpt_assistant_usage.png)

Last week, I happened to see [Zili](https://twitter.com/hzlzh) using ChatGPT as an assistant, which was very tempting. After some tinkering with virtual credit cards and such, I finally got the Plus membership. The not-so-cheap expense of $20 a month made me start to sort out my daily usage needs. In the end, I divided programming code questions, Japanese learning, Chinese-English translation, search engine, copywriting optimization and other needs into multiple dialogue boxes for use. Every day it's like having a bunch of little assistants, quite lively.

Recently, I've had a lot of front-end work to do. Although I've taken courses and studied before, there are still many details I'm not very clear about. At this time, asking questions to ChatGPT and filtering the correct answers from its responses and digesting them into my own knowledge is actually quite effective. It's also very practical, and often proposes novel implementation ideas. Language learning should be the same principle, but I haven't had time to properly test the effect of Japanese learning. If it's interesting later, I might record some dialogues.

## Interesting Things and Objects

### Input

Although most interesting inputs are automatically synchronized in the "Yu's Life" Telegram channel, I still select some to list here, which feels more like a newsletter.

#### Articles

- [Next.js Application Development Practice](https://nextjs-in-action-cn.taonan.lu/)
- [After 14 Years in the Industry, I Still Find Programming Difficult | Piglei](https://www.piglei.com/articles/programming-is-still-hard-after-14-years/)
- [Big Company Disease in the Toilet - hayami's blog](https://hayami.typlog.io/bullshitjobs)
- [Re:Play Issue 25 - Romantic to Death](https://newsletter.replay.cafe/re-play-25-lang-man-zhi-si/)
- [The 4 Levels of Personal Knowledge Management - Forte Labs](https://fortelabs.com/blog/the-4-levels-of-personal-knowledge-management/)
- [Real-world Engineering Challenges #8: Breaking up a Monolith](https://newsletter.pragmaticengineer.com/p/real-world-eng-8)
- [Readme Driven Development](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html)

#### Podcasts

Here are some podcasts I've been listening to:

- [ep.2 Sea Dive Bar: The World is Sinking, We Need to Build - Paipai Zuo | Little Universe](https://www.xiaoyuzhoufm.com/episode/63146f53e50e37575adb1cbe)
- [Vol. 84 Digital Lychee: Licensed Software Ecosystem, Independent Development and Remote Work - Maple Words (Podcast) | Listen Notes](https://www.listennotes.com/zh-hans/podcasts/%E6%9E%AB%E8%A8%80%E6%9E%AB%E8%AF%AD/vol-84-%E6%95%B0%E7%A0%81%E8%8D%94%E6%9E%9D-%E6%AD%A3%E7%89%88%E8%BD%AF%E4%BB%B6%E7%94%9F%E6%80%81%E7%8B%AC%E7%AB%8B%E5%BC%80%E5%8F%91%E4%B8%8E%E8%BF%9C%E7%A8%8B%E5%8A%9E%E5%85%AC-Y-Uq0g5CrZM/)
- [ChatGPT's Breakout and the Anxiety of the Big Shots - Tech Stew (Podcast) | Listen Notes](https://www.listennotes.com/zh-hans/podcasts/%E7%A7%91%E6%8A%80%E4%B9%B1%E7%82%96/chatgpt%E7%9A%84%E5%87%BA%E5%9C%88%E4%B8%8E%E5%A4%A7%E4%BD%AC%E4%BB%AC%E7%9A%84%E7%84%A6%E8%99%91-WgOpJNm435Z/)
- [#20 Annual Splurge Episode 2022 - Binary Radio (podcast) | Listen Notes](https://www.listennotes.com/podcasts/%E4%BA%8C%E5%88%86%E7%94%B5%E5%8F%B0/20-%E4%B8%80%E5%B9%B4%E4%B8%80%E5%BA%A6%E8%B4%A5%E5%AE%B6%E8%8A%82%E7%9B%AE-2022-Wz84cHdvN-u/)

#### Videos

Similarly, I've also recorded some interesting videos I've watched:

- [Valentine's Day 8.0 | Music, the World's Most Universal Love Letter](https://www.bilibili.com/video/BV1PG4y1P7vm/)
- [You're Just One Flirty Line Away from Love, Teaching You How to Use Love Pickup Lines Correctly](https://www.bilibili.com/video/BV1JA411z7KM/)
- [How I Coded An Entire Website Using ChatGPT - YouTube](https://www.youtube.com/watch?v=ng438SIXyW4)

## Personal Life Snapshots

### Sea Dive Bar

![sea_bar_outside](https://image.pseudoyu.com/images/sea_bar_outside.jpg)

![sea_bar_wine](https://image.pseudoyu.com/images/sea_bar_wine.jpg)

Over the weekend, I went to the Sea Dive Bar with friends. It's a small bar in a hutong, crowded but not noisy, with its own kind of liveliness. Inside, there's a big sign that says "Someone's Diving". I had a long chat with a friend who happened to be in Beijing on a business trip, which eased some of the gloomy emotions I'd been carrying this week. I need to adjust well for the new week.

### Nie Nie

![my_lovely_nie_nie_01](https://image.pseudoyu.com/images/my_lovely_nie_nie_01.png)

> I had some drinks at the "Sea Dive Bar" and got home around 1 AM, falling asleep soon after. I just opened my eyes groggily to find Nie Nie seemingly sniffing at my face intently, occasionally touching me tentatively with her little paw. It took my brain (after rebooting) a while to realize she was worried about whether I was still alive. I hurriedly opened my phone in the dark to snap a picture, suddenly feeling a bit of long-lost warmth and dependence.

![my_lovely_nie_nie_02](https://image.pseudoyu.com/images/my_lovely_nie_nie_02.png)

> She must know she's adorable!

### Valentine's Day

![valentine_douban](https://image.pseudoyu.com/images/valentine_douban.png)

I have to say, the person selecting films for the Douban Movie Calendar is quite thoughtful. They put "Love Like a Bouquet" on Valentine's Day, with the caption:

> Love is like a party, it will end someday.
