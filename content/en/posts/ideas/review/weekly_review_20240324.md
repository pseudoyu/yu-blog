---
title: "Weekly Review #55 - Oil Painting Experience, Blog System Upgrade, and Thoughts on Self-Hosting"
date: 2024-03-24T05:20:00+08:00
draft: false
tags: ["review", "life", "painting", "blog", "cusdis", "remark42", "goatcounter", "self-hosting", "flyio"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/fix_you.mp3" caption="'Fix You - Coldplay'" >}}

## Preface

![weekly_review_20240324](https://image.pseudoyu.com/images/weekly_review_20240324.png)

This piece is a record and reflection of my life from `2024-03-17` to `2024-03-24`.

This week, I rekindled much of my enthusiasm for work and learning, completing the long-listed blog comment system and data statistics system migration in my TODO list, giving me a sense of tidying up my desk. Over the weekend, I experienced oil painting for the first time, painting a new avatar for myself, filled with a sense of accomplishment. I resumed my fitness routine, continued learning to drive and registered for the second stage of the driving test. There were many other interesting events as well.

## Oil Painting Experience and New Avatar

My senior and I have vastly different personalities and interests. She has many hobbies I've never ventured into, and what fascinates me often seems to be unknown territory for her. So, we recently set some goals to introduce each other to our own hobbies/skills. I chose double-pinyin input method and programming, with the former already showing significant progress. This week, she took me to an oil painting class.

I'm actually a complete novice when it comes to painting, and never thought I had any aptitude for such artistic pursuits. I was merely curious about what kind of attraction could motivate her to sit in a sketching or oil painting studio for half an afternoon, meticulously working on small details. I was both excited and a bit nervous.

![oil_painting_experience](https://image.pseudoyu.com/images/oil_painting_experience.png)

Normally, beginners wouldn't start with complex subjects like portraits, but I wanted a new avatar. The studio teacher was very accommodating and willing to guide me. We chose a photo focusing mainly on the "head" and began. Drawing the outline, mixing colors, applying paint, adding details based on light and position - everything was more interesting than I had imagined. The combination of a few simple colors could create many layers, and the act of creation itself was as mesmerizing as magic.

![yu_painting](https://image.pseudoyu.com/images/yu_painting.jpg)

The result of an afternoon's work is shown in the image. Though the brushstrokes are novice, it's a work I created with my own brush, holding a unique significance. I've changed my avatar across all platforms to this painting.

## Blog System Upgrade

### Cusdis to Remark42

I previously wrote an article "Lightweight Open-Source Free Blog Comment System Solution (Cusdis + Railway)", discussing how I used the self-hosted open-source [Cusdis](https://cusdis.com/) comment system by [Randy](https://lutaonan.com/). I've been using it since mid-2021, for a full three years now. Apart from some initial troubles with deployment platforms when Heroku and Railway started charging, it has been running steadily.

However, I've encountered some issues during use:

1. Probably due to some modifications in WeChat's built-in browser, the comment component isn't visible when the blog is opened from WeChat chats/dialogues.
2. Although email can be entered, it doesn't support subscribing to comment replies.
3. Comments need to be manually approved by the administrator, but the comment notification TG Bot often fails, causing me to miss comments.

Moreover, as its core functionality hasn't been updated for a long time, it seems a bit rudimentary compared to other more mature comment systems. However, adhering to the principle of "if it works, it's good enough", I hadn't considered migrating/updating. I even participated in some development of Cusdis V2 version during a period when I was learning front-end, but the development group became inactive not long after.

In recent months, because I hardly updated my blog, I didn't receive any notifications from the comment TG Bot. I thought there were no comments until recently when I had to change the Connection String of the Supabase platform hosting the database. I discovered that there were dozens of comments trickling in, some expressing care and encouragement, others inquiring about technical issues. By the time I saw them, it was already a month or two later, which made me quite embarrassed.

Additionally, when changing the database URI, Vercel deployment kept throwing errors. So I decided to migrate from Cusdis. After some research, I chose [Remark42](https://remark42.com/), which [reorx](https://reorx.com/) also selected in his article "Changing Blog Comment Systems".

In terms of configuration options alone, it's considerably richer than Cusdis. I've currently set up several common social account logins (GitHub, Twitter, Telegram, email), allowed anonymous comments, supported email subscription for reply notifications, and also set up TG bot notifications. It's deployed on [fly.io](https://fly.io), with Go single binary + single file database, a very comfortable solution.

Because I had accumulated many comment data before, and Cusdis uses pg while Remark42 uses boltdb single file database, the latter doesn't support remote connections, so I couldn't directly write with SQL statements. I had to first export the required fields to a JSON file through a joined query, then manually execute the Migrator script (and because the official only supports wordpress, disqus and commento, I had to manually implement the conversion logic). Fortunately, it's written in Go, which I'm familiar with. It took me a whole night to finish the [pr](https://github.com/pseudoyu/remark42/pull/1/files)!!!

After the migration, I found that I had accumulated a total of 438 comments over the years. I was surprised myself, but they're all back!!!

### Umami to GoatCounter

With the mindset of "since I've changed the comment system, might as well update the data statistics system that's been a concern", I went ahead and updated it too.

Umami actually hadn't caused any problems, diligently running for a full year and a half until I replaced it. However, possibly because I started using it quite early, during a major version update, there was an incompatible field update in the database Migration script. I don't quite understand why an open-source project of this scale would have such issues. I saw many other users in the issues with similar concerns, but ultimately no good solution was provided.

But because I had been running it for half a year, I was reluctant to lose the previous data. So I kept putting it off, until now I'm still on an old version that I forked. Although I don't have many functional demands for the new version, it just feels a bit uncomfortable, like mild OCD, but I just kept postponing it.

So, taking advantage of this major blog construction, I switched to [goatcounter](https://www.goatcounter.com/). Again, it's a Go single binary + sqlite single file database deployed on fly.io, another very comfortable configuration.

Interestingly, because the author of goatcounter is very persistent, believing that containerizing such single-file applications would actually increase maintenance costs, they don't provide official images. However, having an image is still convenient for deploying on your own VPS or serverless platform, so I used Github Actions to create a CI that pulls the latest code daily, builds the image and uploads it to Docker Hub. If you need it, you can use it. The corresponding Dockerfile and Docker Compose file can be referenced from [this PR](https://github.com/pseudoyu/goatcounter/pull/1/files).

```bash
docker pull pseudoyu/goatcounter
```

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

The frequency of weekly reports in the past half year is worryingly low. Apart from a long article about information management systems, there hasn't been any satisfactory output. So I decided not to migrate the previous visit data (the complexity should also be much higher). Thanks to every cyber friend who clicked into my blog website, screenshot for remembrance.

Recently, I feel like my mood for tinkering with these software/hardware/service configurations has returned, and I also have many blog ideas. The new data will be a new beginning 🫡

![yu_goatcounter_data](https://image.pseudoyu.com/images/yu_goatcounter_data.png)

The biggest motivation for the change was that goatcounter's interface, like my old-school blog theme, perfectly hits my aesthetic sweet spot. I feel like I could stare at this interface forever 🤩 I can't resist this Retro Internet design.

## Some Thoughts on Self-Hosting

I've actually gone through many rounds of tinkering and back-and-forth with VPS and serverless platforms. It may not count as insights, but it's certainly experiential knowledge after deep experience.

I used to be an advocate for serverless. At that time, I would deploy on Vercel/Railway and other PaaS platforms if possible, rather than setting up myself. Being able to achieve stability comparable to large platforms with almost no maintenance costs, I indeed practiced serverless-izing all my services, and it was indeed a worry-free and effortless experience for a long time.

However, after experiencing Heroku and Railway successively changing their charging models midway, and when n8n ran up a bill of over ten dollars a month on Railway, I gradually discovered some drawbacks. Serverless indeed reduced the requirements for maintaining my own servers, but correspondingly, I was also subject to the rules of these platforms.

The charging model is only part of the reason. Compared to renting a well-configured server myself, the cost is actually not bad. It's just that it seems to have tied my services and data to a centralized platform again, giving a sense of insecurity of being at someone else's mercy. And when wanting to migrate to another platform, the platform often doesn't provide a convenient solution. The complexity of tinkering yourself is much higher than directly copying docker-compose files plus mounted volumes between servers.

![vps_service_01](https://image.pseudoyu.com/images/vps_service_01.png)

![vps_service_02](https://image.pseudoyu.com/images/vps_service_02.png)

Therefore, I've put many of my services on the server, running steadily for 430+ days.

![xiao_self_hosted](https://image.pseudoyu.com/images/xiao_self_hosted.png)

A few days ago, when chatting with [reorx](https://reorx.com/) about service deployment solutions, he mentioned that he now prioritizes self-host solutions with sqlite or other similar file databases, which can reduce a lot of maintenance and migration costs and complexity.

Later, I thought about it. Whether on VPS or serverless platforms, it's essentially a choice of self-hosting. What's more needed is to think about the dependencies of the deployed services themselves. For example, many of the instabilities of my previous Cusdis and Umami actually came from the server-side being on PaaS like Vercel and Netlify, while the data was hosted on DaaS like Supabase. A self-use service depending on two platforms simultaneously, any problem with either would lead to service unavailability. What VPS does is just turn this risk into a single point of self-maintenance.

![flyio_services](https://image.pseudoyu.com/images/flyio_services.png)

So I started tinkering again after a long time, deploying Remark42 and GoatCounter on [fly.io](https://fly.io). Because of single binary + file database, the performance consumption is completely within the range of the free plan. I continue to place RSSHub, n8n, image bed and other applications that are relatively more dependent and need to provide external services more centrally on VPS. And I run some services with higher performance or storage consumption on the Home Server and expose them through intranet penetration solutions.

## Other

![applite_overview](https://image.pseudoyu.com/images/applite_overview.png)

I unified the software installed on Mac from various sources. The principle is to reinstall everything that can be installed via brew cask. Previously, when needing to search for command line tools, I didn't feel much, but now with a GUI view, I found that the software sources are indeed much richer than imagined. This method is convenient for management/migration and can relatively ensure the security of software sources 🫡

Switched from RapidAPI to a new API debugging tool [Bruno](https://www.usebruno.com/), pre-ordered its Golden Edition, and the experience has been very good so far.

## Interesting Things

### Input

Although most interesting inputs are automatically synced in the "Yu's Life" Telegram channel, I still select some to list here, feeling more like a newsletter.

#### Books

- [**The Red and the Black**](https://book.douban.com/subject/35781152/), saw an explanation from a video, the description of Julien's self-esteem and the arrogance he displays as a result left a deep impression, currently reading.
- [**Notebooks**](https://book.douban.com/subject/34802764/) by Albert Camus, just started reading.

#### Collections

- [GitHub - milanvarady/Applite](https://github.com/milanvarady/Applite)
- [GitHub - usebruno/bruno](https://github.com/usebruno/bruno)
- [GitHub - plankanban/planka](https://github.com/plankanban/planka)

#### Articles

- [Mental Health in Open Source](https://antfu.me/posts/mental-health-oss)
- [Reunderstanding Heptabase](https://justgoidea.com/posts/2024-009/)
- [Demystifying Docker for JavaScript](https://fly.io/javascript-journal/demystify-docker-js/)

#### Videos

- [In Tokyo, I Only Do Three Things!](https://www.bilibili.com/video/BV131421Q7KT)

#### TV Series

- [**The Three-Body Problem Season 1**](http://movie.douban.com/subject/35196946/), currently watching.
