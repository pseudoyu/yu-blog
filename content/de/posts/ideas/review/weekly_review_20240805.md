---
title: "Weekly Review #67 - Reshaping My Information Input System with Follow"
date: 2024-08-05T05:30:00+08:00
draft: false
tags: ["review", "life", "tools", "follow", "work", "painting", "programming"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Preface

![weekly_review_20240805](https://image.pseudoyu.com/images/weekly_review_20240805.png)

This piece is a record and reflection of my life from `2024-07-31` to `2024-08-04`.

The most delightful experience this week was trying out Follow, an application that excited me after a long while. I compared it with Readwise and decided to cancel my subscription. I also implemented a self-hosted Web Archive solution, and it felt great to eat my own dog food. I continued working on the wall mural with my senior, and there were many other interesting happenings.

## Reshaping My Information Input System with Follow

### My Information Input System

Long ago, I was a heavy information dependant. Whenever I came across good blogs or news sites, I would quickly add them to my RSS feed sources, grinning at the neatly categorized and tagged list. When I found good newsletters, I would immediately subscribe with my email. The first thing I did every morning was to clear the unread items in Reeder 4, which I was using at the time, and then browse through the newsletter emails one by one.

Initially, it seemed fine. I felt satisfied that I could read all the news and articles I cared about as soon as they were available. But gradually, it became overwhelming. I spent more and more time on it every morning, even forcing myself to digest articles I wasn't interested in. Rather than acquiring information, it became more of a craving for information and a compensation for information anxiety. The effect was there, of course - the information left traces in my brain, but the efficiency of digestion was not high.

After reading the articles "Using Automated Workflows to Aggregate Information Intake and Output" and "Saying No to Newsletters", I made significant adjustments.

In terms of information sources, I unsubscribed from all WeChat official accounts and newsletters, and reduced my RSS feed sources to about 50. Most of the remaining input came from Twitter and other people's Telegram channels, which to some extent avoided information cocoons while keeping the input under control.

Moreover, by using n8n + telegram channel to build an automatic synchronization system for input and output sources, all my filtered information sources are automatically synced to my Telegram channel "Yu's Life", making it convenient for me to view and review. It also serves as a personal sharing channel. The pressure of being public also reversely motivates me to filter information sources more carefully.

However, this solution still has two problems:

1. It still hasn't solved the problem of my scattered information sources. I need to frequently switch between Twitter and various TG Channels, which is easy to distract and I might still miss some messages.
2. I often use the channel as my bookmark to some extent. Sometimes a lot of information is very personal, and as the number of followers of the channel grows, I also have some psychological pressure, worrying about becoming information noise for others.

The emergence of Follow just fills in this gap in my solution.

### Follow

#### Introduction

> Next generation information browser

This is Follow's slogan. Before its release, I merely regarded it as an alternative to RSS readers. Although I was familiar with RSSHub and heavily used my self-deployed instance, I still couldn't imagine how much room for development there could be based on this ancient protocol, until after its release and a few days of intensive use, I gradually understood this concept.

In the current era where RSS has already declined, apart from independent blogs, which are in a similar situation and almost all still retain complete RSS support, most news, information, and various niche websites no longer provide it. RSSHub is then the perfect and almost the only solution, which can convert web information sources including but not limited to Twitter, TG Channel, Bilibili, and NetEase Music playlists into standard RSS format, allowing these information sources to be updated like subscribing to articles.

However, RSSHub is still more of a middleware tool. Even with standardized RSS data, most readers can only process text display, and the handling of audio, video, and images basically stays at the level of treating them as a URL. Therefore, I mostly apply it in my n8n synchronization workflow as a notification, only retaining its title and link, still clicking the source link to jump to the corresponding webpage to view, which often feels a bit disjointed to use.

Follow's biggest feature is naturally the inheritance of RSSHub's "everything can be RSS" philosophy, providing presentation methods for various forms of content such as videos, pictures, blog audio, articles, social media, etc. at the application layer. It really feels like a leap from pure HTML to modern CSS effects after looking at it for a long time. Actually, achieving this step is not a very high technical barrier. Whether it's video iFrame, audio player, or image preview, there are relatively mature components available for use. But Follow is almost the only product that is still focusing on and doing well with this protocol. Sometimes, doing a little better is enough.

#### Experience

![follow_homepage](https://image.pseudoyu.com/images/follow_homepage.png)

As an information browser/reader, the most intuitive and core aspects are the interface and interaction. The combination of DIYGod + Shiyier early on raised my expectations to the fullest, but even the first beta version still amazed me with its completeness and experience. Before this, the most modern one should be Reeder 4, and Follow, even though it's Electron and not pure native, still maintains an extremely exquisite design and interaction.

I've used multiple readers before, including NetNewsWire, Reeder 4, Miniflux, and Readwise Reader, but because the reading experience was often not as good as the original webpage, I mostly chose to jump to the link to view. However, Follow's pages and interactions themselves make me enjoy it. There's also an interesting recent reading history display, where you can see which visitors have read this article, and you can click into their homepage to see their subscriptions, combining social attributes and information source accumulation. I've discovered many personal blogs that I hadn't paid attention to before through this method.

Moreover, due to Follow's deep integration with RSSHub, it can achieve direct subscription to social media by inputting twitter handle, Bilibili uid, and youtube channel name, without having to find the corresponding route in the documentation of the RSSHub website or set up your own instance, which is very user-friendly.

![follow_pic](https://image.pseudoyu.com/images/follow_pic.png)

![follow_video](https://image.pseudoyu.com/images/follow_video.png)

The direct display of videos and pictures is also a highlight. I've seen a user using some designers' Twitter as their source of design inspiration and aesthetic accumulation, which is also a very meaningful application scenario.

Audio/podcasts can be played globally in Follow. For example, in the bottom left corner of the previous screenshots, I was playing an episode of "Beyond Code" simultaneously. This also solves the problem of me having to repeatedly switch between multiple podcast apps like Apple Podcast, Spotify, and Xiaoyuzhou.

You can also conveniently share your subscriptions: <https://web.follow.is/profile/pseudoyu>

There are actually quite a few more designs, such as the Action module and Power tipping, but this article is not a software review but a personal experience, so I won't elaborate too much. You can experience it yourself when it opens up later, keeping some surprises. Next, I want to talk about the comparison with Readwise Reader that I'm currently using, and why I plan to switch to Follow.

#### Readwise Reader -> Follow

![readwise_sub](https://image.pseudoyu.com/images/readwise_sub.png)

I subscribed to Readwise Full membership around September last year. Although it offers a 50% discount for developing countries, it still costs nearly $50 a year. It's comprehensive, but the core functions I use are actually only three points:

1. RSS reader
2. Read later, save articles and highlight annotations
3. Daily Digest

Among them, the first point is the most frequent, as a convenient reader to manage my article subscriptions, etc. It also has a mobile app for reading anytime. However, during use, I found that sometimes the display style and image loading are not very good, and the classification and shortcuts are a bit too complex. It mainly supports articles, which can obviously be completely replaced by Follow (waiting for a mobile app).

I used to use highlight annotations quite often, using plugins to make some notes on some articles and save them to Readwise, then synchronize my articles to Telegram Channel through n8n. But it's actually a bit too dependent on the platform. When I really want to digest those highlighted notes and organize them into some formed ideas or articles, I need to go back to Readwise to view them. Even if I synchronize them to Logseq or Heptabase for organization, it's still not convenient. Especially now that I've switched to Apple Notes as my main and only note-taking tool, I found that directly excerpting/recording some ideas is the most efficient and more likely to generate value. Therefore, the highlighting feature gradually faded out of my note-taking flow.

![save_website](https://image.pseudoyu.com/images/save_website.jpg)

As we all know, read later often evolves into never read later, so my current strategy is to almost never use read later, trying to read it right away as much as possible, with only a very few longer ones temporarily stored, and trying to clear the list on the same day. Now I use the unread mode as the default display in Follow, often browsing through it. When I come across an article that I'm interested in and have read through, I use the star function to save it in my favorites. When I've finished reading and gained something, I use a browser plugin I made + Cloudflare Worker api + n8n to save the article link and source HTML file to the D1 database, achieving Web Archive and automatically syncing to my Telegram Channel.

The third point, Daily Digest, helps me review some of my notes or articles. This is useful but not high-frequency. I haven't researched in detail whether the Follow Action module can do some operations on multiple articles.

Since my core needs can all be transferred to Follow, I decisively unsubscribed from Readwise. I can clearly feel that my information intake volume and quality have also significantly improved in these few days. A good software is actually not just an auxiliary tool, it has a more profound impact on thinking and habits.

## Personal Life Snippets

### Electron Bug

![talk_with_innei](https://image.pseudoyu.com/images/talk_with_innei.jpg)

I just discovered that there's an issue with the Follow client update. Clicking "Click to restart" hides the window instead of quitting it. It's a familiar bug, I wrote exactly the same one when I was writing EpubKit 🤣 I reported it to Shiyier, it's like exchanging Electron illness experiences.

### macOS Desktop Decoration

![macos_widgets](https://image.pseudoyu.com/images/macos_widgets.png)

This is my first attempt at macOS system desktop widgets. It's quite fresh, but I basically switch applications with Raycast shortcuts and hardly ever see the desktop...

### Garage Wall Painting

![car_painting_week2](https://image.pseudoyu.com/images/car_painting_week2.jpg)

Overall progress this week: 20%, it's already taking shape.

My progress this week: painted five or six bricks 🤣

## Interesting Things and Objects

### Input

Although most interesting inputs will be automatically synchronized in the "Yu's Life" Telegram channel, I still select a part to list here, feeling more like a newsletter. And I built a microblog - "daily.pseudoyu.com" using Telegram Channel messages as content source, which is more convenient to browse.

#### Collections

- [pseudoyu | Follow](https://web.follow.is/profile/pseudoyu)
- [DIYgod | Follow](https://web.follow.is/profile/DIYgod)
- [n8n Chinese Tutorial | Simple and Easy-to-Understand Modern Magic](https://n8n.akashio.com/)
- [Dengtab - Stay focused and reduce social media distractions while cultivating small habits.](https://dengtab.com/)
- [SixD - SwiftUI & Interaction Design](https://www.haolunyang.com/sixd)
- [ccbikai/BroadcastChannel](https://github.com/ccbikai/BroadcastChannel)

#### Podcasts

- [Episode 10 | Flower Fruit Mountain Monkey King talks about career choices, how to establish oneself through sales, RV trips, and new life in the UK](https://www.listennotes.com/e/7f2efa4ad8394de79591a3ee2da6a5d1)
- [Ep 48. Exclusive interview with Gao Tian: To be a good Bilibili up-caster, I became a Python core developer](https://www.listennotes.com/e/5e5454656bb146499bef687dcec00e65)

#### Articles

- [Fasting Record](https://blog.douchi.space/intermittent-fasting/#gsc.tab=0)
- [Some Exploration on De-Cloudflare-ization of WebP Cloud Services](https://blog.webp.se/de-cloudflarize-zh/)
- [P5r: Life Changed](https://jesor.me/2024/persona5r-life-changed/)
- [Reflections amid Busyness: Life, Work and Entertainment - Quiet Forest](https://innei.in/notes/175)
- [My Understanding of Cloud Native](https://gist.github.com/sljeff/cce768194a9e68d5279bfde861ff5f76)
- [How Stripe Securely Collects Payments and Avoids Fraud and Card Testing](https://dmesg.app/stripe-fraud.html)

#### Videos

- [Taking a Break from School + Refusing Million-Yuan Annual Salary, Living is Not Just About Achieving Something](https://www.bilibili.com/video/BV1dx4y1x7mz)
- [Learn with me - HTMX and HonoJS](https://www.youtube.com/watch?v=hMcE8E8JjXA)
- [【He Tongxue】You Can Never Go Back to the Summer When You Were 19...](https://www.bilibili.com/video/BV15b42177rL)
- [Becoming a Python Core Developer in 450 Days](https://www.bilibili.com/video/BV1of421972c)
- [After 10 Years, 9 Million](https://www.bilibili.com/video/BV1jT42167Xb)

#### Movies

- [**Drifting**](https://movie.douban.com/subject/35956190/), I really like the cinematography of the highway traffic jam scene at the end, life is nothing but stops and starts.
