---
title: "Weekly Review #25 - Personal Information Output and Synchronization System Based on Crossbell (Refactored)"
date: 2023-01-09T19:12:56+08:00
draft: false
tags: ["review", "life", "home", "mood", "miniflux", "rss", "information", "serverless", "pkm", "system", "xlog", "xsync", "crossbell"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

This is a record and reflection of my life from January 1, 2023 to January 9, 2023.

This is the first weekly review of 2023. Although the New Year feels like it was just yesterday, the first week of January has already ended. Perhaps my psychological perception of time has become increasingly dull.

During the New Year, I wrote a rather detailed annual summary, recounting the various events of the past year. After finishing, I realized the length had exceeded my expectations. Additionally, I hadn't yet clarified my thoughts on new year plans and expectations, so I skipped that part. Therefore, I'll take this opportunity in this first weekly review of the new year to set some modest goals. Some are small habit formations, while others are long-term plans full of uncertainties. I don't know if I'll be able to fulfill them all in the coming year, but listing them out will provide some motivation and serve as a form of self-monitoring.

After staying at home for nearly two months, I finally decided to go out on the weekend to have dinner at a friend's house, enjoying a happy day (otherwise I felt like I had forgotten how to talk to people face-to-face). Although the photo success rate was questionable, I managed to edit the photos and publish two photography collections. I organized my various software and hardware services (an annual ritual, always feeling that I'll have more motivation to start anew after organizing). While organizing, I remembered some previous small projects and set up a website to run [IPFS version of ZLibrary](https://zlib.pseudoyu.com/), which unexpectedly garnered attention, scaring me into optimizing the server and network routes overnight. And many other interesting things happened.

## Personal Service Restructuring

### Service Management

Like previous years, I started the year by organizing my various services. I discovered that I now have as many as 20, with half of them being serverless. My skill in utilizing free resources has greatly improved this year. For easier management, I set up a monitoring service using the open-source Uptime Kuma, binding it to a Telegram Bot for alerts, which gave me much more peace of mind.

![uptime_kuma_yu_services](https://image.pseudoyu.com/images/uptime_kuma_yu_services.png)

Interestingly, I always found managing websites on servers troublesome. Every time I needed to migrate or change services, it was always a headache. So I hosted most of my services on Railway, Vercel, Supabase, and other Serverless platforms. Since most are personal services without high configuration requirements, as long as they're safe and stable, it's enough. I hadn't bothered with Nginx reverse proxy, https certificates, and such.

As I mentioned before, I've been helping an anime-loving friend with Bilibili livestream management and technical support. I thought about using a free Oracle Japan machine specifically for livestream monitoring and automatic recording. Sometimes my friend also needs to be able to view and download directly, so naturally, a memorable domain name, access speed under domestic network conditions, download bandwidth, etc., all need to be considered. Serverless services were far from sufficient (and not very cost-effective), so I explored some solutions and chose [Nginx Proxy Manager](https://nginxproxymanager.com/), a convenient reverse proxy tool.

![npm_yu_dashboard](https://image.pseudoyu.com/images/npm_yu_dashboard.png)

I deployed it on a BandwagonHost machine with a good network connection (CN2 GIA) to host my various services, ensuring a decent access experience. It can also directly issue https certificates for my `*.pseudoyu.com` subdomains through wildcard matching and automatic renewal, which is very convenient. Combined with the aforementioned monitoring, I've been using it for a week now, and it's quite comfortable.

The official documentation is clear and detailed, and with the user-friendly container service management method of docker-compose, it's quick to get started. However, I might still consider creating a tutorial later to provide reference for friends who want to host small services like blogs.

### RSS Input

In 2022, I mostly focused on blog output and my Telegram channel, without putting much thought into input and synchronization across various platforms. This led to an accumulation of RSS subscriptions, and newsletters also became somewhat overwhelming. I wasn't able to properly filter my input information sources. So I deleted NetNewsWire, which I had been using for a long time, and set up a more lightweight Miniflux using Railway + Supabase as my main reader. I also filtered my RSS information sources, limiting them to 52, almost all personal blogs. I will continue to optimize and adjust in the future.

![miniflux_yu_page](https://image.pseudoyu.com/images/miniflux_yu_page.png)

Although Miniflux provides a decent reading experience, I actually prefer clicking into the original article. I always feel that for personal blogs, it's not just about the content; the website's style design, some related articles and themes are all integral parts of the blogger, which can bring a more complete reading enjoyment.

For me, the RSS reader serves more as a first-step aggregation tool. Since Miniflux is a web-based service, it can't provide very timely notifications. As I heavily rely on Telegram every day, I set up my own Telegram notification based on [RSS to Telegram Bot](https://github.com/Rongronggg9/RSS-to-Telegram-Bot) to push updates from these information sources to me. When I see some interesting titles, I make a mental note and then go to Miniflux to read and check them all at once when I have free time.

![yu_rss_to_tg_bot](https://image.pseudoyu.com/images/yu_rss_to_tg_bot.png)

This way, I'm less likely to miss articles I want to read, and it doesn't cause too much information buildup. This setup has been working very well so far. Incidentally, seeing various weekly reviews every weekend also has a significant prompting effect (~~I went out to play on Sunday, reasonably delayed the update~~).

### Telegram Output

I also set up my own n8n synchronization service based on Railway + Supabase to synchronize my input from various platforms to my channel. For a detailed description, you can refer to this article "[\[Weekly Review #12 - Cyber Space, Self-Definition and Boundaries\](https://www.pseudoyu.com/en/2022/09/19/weekly_review_20220919/)".

Previously, the platform was based on [Reorx's](https://github.com/reorx) solution with some of my own adjustments, but I hadn't added more information sources, and there were fewer domestic sources.

Although I currently rarely share on various domestic platforms, it's still part of myself. Additionally, I added Sspai as a publishing channel for some of my work efficiency articles. So after my friend [Tujunjie](https://blog.tujunjie.com/) recommended the integration of RSSHub and n8n, I deployed a set of [RSSHub](https://github.com/DIYgod/RSSHub) services on my server to try it out. I immediately found it to be an impressive solution and quickly added synchronization support for NetEase Cloud Music, Weibo, Bilibili, and Sspai to my Telegram information flow channel, making the content more enriched.

### Crossbell Synchronization

Although platforms like Twitter and Telegram are relatively large, they are still centralized products. With the recent various upheavals, I always feel uneasy about using Telegram as the final station for aggregating these information sources, especially when I often almost accidentally click to delete all messages when trying to delete a single message (strange user experience). Therefore, the synchronization and export of information is also a very important link.

The Side Project I mentioned before is also doing something like this, but as a Web3 practitioner, I've naturally been eyeing blockchain-based solutions for a long time. In fact, my graduation project was a [ÐApp for data ownership protection based on Ethereum and IPFS](https://github.com/pseudoyu/uright), but that paper-thin Demo project naturally couldn't meet my various needs, and the code was written so messily that I had no desire to refactor it. So I started looking for on-chain solutions.

I had been following [Crossbell](https://crossbell.io/) for a long time, and by some strange coincidence, I got to know quite a few friends from [RSS3](https://rss3.io/). But my previous impression of Crossbell was still limited to the [CrossSync](https://crosssync.app/) browser plugin that [Diygod](https://diygod.me/) posted on Twitter, which was based on this chain. At that time, I opened the link on my phone, and it wasn't convenient to associate the wallet, so I put it aside.

So I thought about visiting the official website, and to my surprise, I found that there were already several applications like [xLog](https://xlog.app/), [xSync](https://xsync.app/), [xChar](https://xchar.app/), [xFeed](https://crossbell.io/feed), etc. The xSync that I was most concerned about happened to support Telegram Channel, perfectly matching my needs.

#### xLog Synchronous Blog Publishing

So I started a series of configurations and decorations. First, I synchronized my personal reflection-related blog posts to xLog. The visual effect and experience are good, and it's very convenient to follow and comment based on the Crossbell address.

This is my xLog access address: [xlog.pseudoyu.com](https://xlog.pseudoyu.com/). Interested friends can also follow it. However, due to considerations of customization level, various historical article migration routing issues, changes in my various data statistics services, etc., it's still more of a synchronization distribution channel for now. I don't plan to completely migrate my blog over for the time being.

![yu_xlog_homepage](https://image.pseudoyu.com/images/yu_xlog_homepage.png)

The built-in [NFT showcase](https://xlog.pseudoyu.com/nft) is very nice, probably integrated with [Unidata](https://unidata.app/). I had wanted to integrate it into my Hugo blog before, but never got around to it (~~having a ready-made one made me even lazier~~).

![yu_xlog_nft](https://image.pseudoyu.com/images/yu_xlog_nft.png)

#### xSync Automatic Synchronization of Telegram and Twitter

I was really excited when I saw that xSync could synchronize Telegram Channel data. It didn't require any modifications to make another backup and archive of my aggregated channel, and I quickly configured it. ~~I suddenly felt the urge to abandon my own Side Project~~.

![yu_xsync_homepage](https://image.pseudoyu.com/images/yu_xsync_homepage.png)

However, it's a bit regrettable that only part of the historical data was synchronized. There doesn't seem to be an option for manual backup synchronization of data from before the integration, and I don't know if there's a configuration item or future feature that can solve this. If any RSS3 friends know of a solution, please let me know. Thanks!

After everything is configured, you can view all your messages through xChar. It's a perfect solution. This is my xCharacter personal homepage: [xchar.app/pseudoyu](https://xchar.app/pseudoyu), where you can also view my information flow.

![yu_xchar_profile](https://image.pseudoyu.com/images/yu_xchar_profile.png)

Another small anecdote is that when I saw that I needed to put `pseudoyu@crossbell` in the profile, I smiled. When I was doing my graduation project on copyright protection ÐApp, I used the Oraclize API in the Solidity contract to access off-chain data, which also grabbed the unique identifier from the YouTube description as proof of account ownership. It gave me a strange sense of familiarity, haha. I'll have a chance to study the code later.

This Crossbell-based information input and output solution can be said to have restructured my original personal management system. I hope to make some of my own attempts based on this system.

## New Year's Plans

It seems that listing some annual plans has become an unwritten habit every year, but in so many years of my past, there have been few that I've actually followed through and achieved. This year, I've added more public expression channels, which seems to give me more motivation to practice.

I previously read [Xuanwo's](https://xuanwo.io/) article "[2022-37: Public workflow based on Github](https://xuanwo.io/reports/2022-37/)", and after a bit of research on GitHub Projects, I found it to be simple yet sufficient. Although I usually do some basic GTD based on Logseq, it's still difficult to use as a kanban board. I'll try it this year, and also give myself some corresponding pressure.

It's hard to control the granularity of New Year's plans, so I'll just go with the flow. I won't write those big and empty ones anymore. It's more about some indicators. Some are ideas for free exploration, some are long-term goals, and some are short-term things to accomplish. I've adopted a checkbox format. Maybe I'll continue to add more as I think of them later. I'll come back to check and review when I complete them or during the year-end summary of the new year.

- [ ] Take good care of Nini, protect her well
- [ ] Go to Japan or return to Hong Kong for work / a remote job that I enjoy / a work mode with satisfactory freedom, choose one according to priority
- [ ] Travel to at least 6 cities I've never been to, preferably meeting long-lost friends, though not many
- [ ] Persist in writing weekly reviews, complete 48 pieces
- [ ] Update at least 48 original blog posts besides weekly reviews, mainly technical
- [ ] Go out to take more photos, update at least 12 pieces in the newly opened photography collection column (I've already rushed two kpi posts on New Year's Day), and study composition, color, and post-processing in depth
- [ ] Contribute at least 12 translated articles to GoCN
- [ ] Publish 10 articles on Sspai, earn money for cat food
- [ ] Start being a Bilibili up and Youtuber, publish at least 10 videos, can't be too shallow
- [ ] Persist in exercising/running at least four days a week (Ring Fit Adventure or Keep also counts), will also record check-ins in weekly reviews
- [ ] Persist in practicing guitar, record at least 3 songs and publish them
- [ ] Pick up skateboarding skills again, practice at least twice a week
- [ ] Read at least 24 meaningful books, but can't gulp them down, need to publish my thoughts on platforms like Douban
- [ ] Japanese N2 certificate, preparation for some future plans in Japan, will open a separate module in the weekly review to check in on learning progress, might cram for the July exam, ~~if not, try again in December~~
- [ ] CKAD certificate, prepared halfway last year, but forgot to register and purchase the exam later, without pressure, I indeed became lazy
- [ ] Contribute code to more open source projects, don't require quantity, but hope to have more meaningful submissions
- [ ] Write a showcase website for my open source toolbox project "[Yu Tools](https://github.com/pseudoyu/yu-tools)", and write usage experiences for the software and hardware items in it (a big project), continuously optimize and iterate
- [ ] Improve the open source guide project "[Blockchain Guide](https://guide.pseudoyu.com/)", cover more of the blockchain underlying and Web3-related project experiences and engineering experiences from work and study over the past year, shamefully, most of the articles were written when I was studying for my master's in Hong Kong
- [ ] Successfully launch and continuously optimize the Side Project startup project I'm doing with friends
- [ ] Explore more interesting technologies, continue to enjoy them
- [ ] Meet more interesting people
- [ ] Live on well

## Personal Life Snippets

Since the severe epidemic in Beijing in November, I've been living at home for two months. Perhaps I have decent physical defense attributes (referring to sending the only bit of medicine I had on hand to a friend at the time, relying purely on not going out to isolate from the virus) and luck points (ordering takeout as usual every day, and even having property management come to my home to deal with a water leak for an afternoon), I've managed to remain negative until now, already in the final round.

But the consequence is that friends who have already recovered and turned negative are traveling everywhere, while I'm still fully armed just to take out the trash, let alone dare to travel far. So I spent these two months with my cat.

Although I'm indeed staying at home, as the epidemic opened up, there seemed to be no end in sight. So my mindset became more relaxed. This weekend, I was invited (~~not really, just using the pretext of visiting with my cat~~) to go to senior Bo Yi's house for dinner. I breathed in the not-so-fresh air outside (~~after all, it's Beijing~~), and also ate home-cooked meals that I hadn't had in a long time. I lounged around all day, but felt content and happy.

![wonderful_meal_with_boyi](https://image.pseudoyu.com/images/wonderful_meal_with_boyi.jpg)

I plan to return to Hangzhou on January 18th. Actually, in 2022, my time at home was not short compared to recent years. With various adjusted holidays and vacations, it added up to about a month before and after going home. It's just that the epidemic often recurred, and I didn't have the chance to return to my hometown. Two years ago in January, my grandmother passed away, and I was stuck in Hong Kong due to the epidemic and couldn't go home. Last Spring Festival, I was stranded in Beijing again due to a sudden outbreak. It's time to go back and see. As I grow older, I go to more and more places, but home seems to be getting farther and farther away.

I've been hesitating about going home for a while, worried about any changes, but still want to go back and see. However, in this situation, I'm not comfortable leaving my cat with a pet hotel or unfamiliar people. Later, when I casually mentioned this during a meeting, I found a solution. I decided to have Nini stay at the home of my project's small leader. His daughter has been eyeing a cat for a long time. After settling this, I finally felt relieved.

With all this trouble, I'm likely to get infected. Knowing this, senior Bo Yi gave me a luxurious anti-epidemic gift package, which was touching.

![medicines_from_boyi](https://image.pseudoyu.com/images/medicines_from_boyi.jpg)

Then a while ago, when senior Bo Yi was at Lingyin Temple, she made a wish for me: "May 2023 allow you to do what you like and explore more hobbies as you wish." She also brought me a beautiful Buddhist bracelet. I unilaterally declare her the best senior in the world. I hope the new year will be good for her too.

Suddenly I remembered that when I was in university, I wore a Buddhist bracelet from Lingyin Temple that Ni gave me for more than a year, until the string was almost worn out and the beads were about to fall off before I put it away. I strangely felt that I was indeed luckier that year. Sometimes maybe you just need some peace of mind.

I will go back to fulfill the wish, a double wish.

![wonderful_gift_with_boyi](https://image.pseudoyu.com/images/wonderful_gift_with_boyi.jpg)

## Other

This section will record some of my inputs and outputs, as well as other things I find interesting.

This week, I watched two very touching videos on Bilibili. One is from my favorite Up主 "[Xiaolu Lawrence](https://space.bilibili.com/37029661)" titled "[This is my most hardworking year, but it made the company shrink by half | 2022 Year-end Summary](https://www.bilibili.com/video/BV1Mx4y1G7zW)". I had some thoughts:

> I've been watching for several consecutive years, and always watch this reserved year-end summary column many, many times.

> I've felt empathy when I was at the same stage, being moved by some videos; I've been happy for many, many days when Lu-ge replied to and encouraged my dynamic; More often, he accompanied me through one night after another, waking up to continue living with effort. Perhaps due to familiarity, the slight pause when first opening the new studio door, the choke when saying "because the support of family was once your confidence", the BGM of the bouquet, the bitter laugh when reviewing this year, all made my emotions fluctuate and tears fall.

> "It's not that you've changed as you've grown up, but that you've grown up, and the world has begun to reveal all its truths to you". Perhaps the often-described youthfulness and student air about me is just the overdraft of the luck I've experienced in the past, and the protection of those around me, allowing me to talk about myself again and again in my weekly reports, longing for beauty again and again. And in 2022, everything has returned to the starting point. Fortunately, I still retain the habit of "recording" and haven't lost the ability to "feel". Small, but precious.

> "This year, I've lost too much, too much. Any small death and collapse becomes unbearable". Yes, 2022 was just too difficult, indescribable. In the new year, I have to struggle to live alone.

> Thank you, Lu-ge, for your companionship and the emotions you've brought over the past year. In the new year, let's keep going!

There's also a very sharp Up主 "[Lao Jiang Ju Kao Pu](https://space.bilibili.com/119801456)" with "[Say goodbye to the indescribable and unnecessary year - My New Year's Address](https://www.bilibili.com/video/BV17M411y7es)". My thoughts:

> I really like Lao Jiang's thinking and narrative style, plain, sincere but bold and not lacking in sharpness. It's the best New Year's address I've seen.

> 2022 just passed like this, many things can't be said, many things are happening, many things will never happen again, indescribable is probably the best description.

## Summary

The first week of 2023, this year is off to a pretty good start.