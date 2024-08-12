---
title: "Weekly Review #05 - Work, Sense of Time Control, and New Friends"
date: 2022-07-31T23:55:54+08:00
draft: false
tags: ["review", "life", "time", "balance", "work", "friendship"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

![bg_computer_room_hellowork](https://image.pseudoyu.com/images/bg_computer_room_hellowork.jpg)

This piece is a record and reflection of my life from July 25, 2022, to July 31, 2022, also the first week back to work after a vacation.

After experiencing a rare "short summer break," I was immediately thrust into the tense preparation of a new project before I had time to adjust my state, which also prompted me to think more about the balance between work and life.

## Work and Sense of Time Control

As I mentioned in a previous article, it has been a year since I ended my student life and entered the workforce. Thanks to the training under extreme pressure from the first project, I have mostly mastered my work responsibilities. Even when faced with impromptu meetings or technical proposal explanations, I can handle them with relative ease.

The greatest advantage of being trusted at work is having a good degree of freedom. As long as I can coordinate and arrange the progress of the entire task well and achieve a good result, there is no need to succumb to meaningless competition. The working hours are fairly normal, and the work pressure of most projects is not particularly high for long periods (mainly because it is B2B business, so we mostly rush to meet delivery milestones). I can also use the saved time to learn other things.

I originally thought this mode was quite good, but recently my state has slowly developed some problems. It feels as if my life is slowly being devoured.

I haven't been able to control the leisure time after work as well as I had originally envisioned. As the days go by, I tend to engage in more mindless leisure activities after work, such as binge-watching dramas or scrolling through some micro-films on Bilibili (occasionally stumbling upon relationship-related content and starting to get emotional).

Sometimes, hours mysteriously pass by, and because I need to go to work the next day, I have no choice but to take some melatonin and sleep. There are even days when I come back home close to 10 pm, thinking I'll lie down for a bit, only to open my eyes again and find it's already past 1 am. I get up and open my computer, but end up not doing much.

As a result, productivity during after-work hours is hard to guarantee. Sometimes, I even force myself to do things. I resonate with a group member's description:

> "I'm now learning with a focus on weekly reports. Every time I want to completely lie down, I think about what to do if I haven't written the weekly review, and then I sit up in shock as if rising from my deathbed."

Reflecting on the reasons for this state, I feel that I still find it difficult to get the improvement I want from work. Instead, it often consumes my spirit, and the time after work is not enough to recover, causing my productivity to be completely destroyed. Although there are indeed no task quantity regulations or external deadlines, I still often have some self-reproach. This is far from the ideal living state I pursue.

I seem to have heard this concept from a podcast: we all need to find the B-side hidden behind the A-side. If we take work projects as an A-side, the B-side is finding some points hidden within it. Whether it's innovation or some new technical attempts, they can give us more subjective willingness to complete them. If we take work itself as an A-side, then we need to think about how to fill the other side of this work that occupies most of our time. It can be learning and improvement, or it can be cultivating a simple hobby.

Of course, changing this state doesn't have a standard solution, and it has never been something that can be easily solved. But it needs to be slowly sorted out anyway. Currently, I'm thinking that my next job will consider more remote work models to better balance my rhythm. I've also been looking into some related information recently.

## New Friends

The surprise this week was meeting several friends I've been following on Twitter for a long time. It started with a discussion about Cloudflare Pages with [STRRL](https://twitter.com/strrlthedev) and adding each other as friends. Later, I joined a small group and met big names like [Homura](https://twitter.com/RealAkemiHomura), [Manjusaka](https://twitter.com/Manjusaka_Lee), [Xinyi](https://twitter.com/_a_wing), and [Xuanwo](https://twitter.com/OnlyXuanwo). We occasionally have some daily exchanges about life and technology.

It seems that after graduation, I rarely actively socialize. I'm unwilling to participate in gatherings with strangers in real life, and I've closed my WeChat Moments entrance for four or five years. I don't know the current situation of my former classmates, making it even more difficult to have any opportunity for communication. I've been in a closed state for a long time. On the contrary, I've been rambling a lot on Twitter since May, and I'm often amazed by the interesting lives and depth of thought of many Twitter friends. But I've always been quietly watching, with very little direct interaction. This time, meeting so many new friends, I'm very happy and surprised. I hope to have more exchanges in the future. Everyone is very nice.

## Learning and Input

This section will record some interesting things I've come across and the progress of my work and study.

### Technical Learning

This week, I first joined a new project and did some environment setup, which involved quite a few Docker-related operations. However, because I've done similar things before, the overall process was quite smooth. Then, because it involves the Cosmos blockchain, I started reading "Blockchain Architecture and Implementation: Detailed Explanation of Cosmos" and made some notes. I'm reading it slowly.

But after a few days, I was assigned to the early preparation of another project. There was a lot of tedious work, and I worked overtime for several consecutive days, but the development progress was not much. I hope the project goes smoothly.

I didn't do much other technical learning this week. CSAPP, contract development, and the newly arrived Go language-related books all need to be pushed forward according to the schedule.

### Input

#### Books

- **Tim Cook: The Genius Who Took Apple to the Next Level**, Although I heard it's mostly a compilation of reports and information, I'm very interested in Apple as a company but have always been unfamiliar with Tim. Perhaps Steve Jobs' halo is too strong, so I want to learn more about him.

#### TV Series

1. **The Most Hated Man on the Internet**, a new Netflix documentary. The mother in the event is strong, confident, and interesting. Compared to the previous documentary about the Nth Room case, it's less heavy and has more of a suspense rhythm. But after watching it late at night, I still feel helpless (or powerless). I just hope this world can have a little more kindness and humanity, even if it's just a little bit better.
2. **Extraordinary Attorney Woo**, the female lead is still very cute, and the main couple is quite shippable.

#### Movies

- **Moon Man**, a standard comedy film for theaters. The music and atmosphere rendering are quite in place. As for the plot, it feels like a low-budget version of The Martian, and the ending is a bit too focused on core values.

#### Anime

- **Summer Time Rendering**, an anime series I look forward to updating every week.

## Tinkering Notes

### Software Tinkering

1. **Arc**, a newly popular browser. I tried it out, and the experience is very different. Currently, I haven't found any major flaws, but it will still mostly serve as an auxiliary browser. After all, I'm too used to Safari.
2. **Arctype**, a database management tool I saw in some recommendation article. The interface is very beautiful, and it can be divided into multiple workspaces. It also has a built-in visualization panel function. I haven't played with it in detail yet. Currently, my main tool is still TablePlus.

After reading [STRRL](https://twitter.com/strrlthedev)'s weekly review last week, I also completely migrated my blog to Cloudflare Pages. The migration experience was very seamless, and the subsequent use feels great. At this point, my serverless blog system consists of:

- GitHub as the source file for the Hugo blog and running some GitHub Actions to automatically update the About page
- Cloudflare Pages hosting the blog, and using the domain hosted on Cloudflare for resolution
- Hosting the Cusdis comment system and Umami data statistics system on Railway and Vercel

### Blog Related

I didn't write many articles this week, but there were some small milestones in the data. First, Google searches reached 1000 clicks.

![blog_google_search_1k](https://image.pseudoyu.com/images/blog_google_search_1k.jpg)

Then, for the first time, the monthly page views reached about 10,000, with over 3,000 visitors.

![blog_umami_10k](https://image.pseudoyu.com/images/blog_umami_10k.png)

I need to continue to work hard and write more.
