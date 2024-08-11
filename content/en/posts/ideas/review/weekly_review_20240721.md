---
title: "Weekly Review #65 - Adventure X Experience, Apple Notes Practice, and EpubKit"
date: 2024-07-21T08:30:00+08:00
draft: false
tags: ["review", "life", "adventurex", "hackathon", "epubkit", "work", "apple notes"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Preface

![weekly_review_20240721](https://image.pseudoyu.com/images/weekly_review_20240721.png)

This piece records and reflects on my life from July 10 to July 21, 2024.

This week and a half has been quite eventful. Work has been somewhat busy. I participated in the Adventure X event, which was a lot of fun. I experimented with the Remix framework and prepared for a workshop. I met with Randy, and together we planned the redesign and subsequent development of EpubKit, essentially holding our own hackathon for us "middle-aged hippies" who couldn't participate in the competition. I switched from Obsidian to Apple Notes, implementing P.A.R.A. I'm planning to paint the walls of my garage. I visited the Apple Store to experience the Apple Vision Pro. And there were many other interesting happenings.

## Adventure X

This was a hackathon event for young developers aged 26 and under. I had heard about it early on but was unfortunately just over the age limit to participate. However, I was invited to be a judge for the "Web 3.0 Development Tools" track sponsored by OpenBuild and to be a workshop instructor on-site, allowing me to observe the entire process.

The event attracted nearly 200 developers, and their energy and passion were palpable (perhaps the 26-year age limit makes sense after all). I also met many familiar faces from Twitter and "Crazy Thursday", and had interesting conversations with several new and old friends.

### Workshop

![adventurex_workshop](https://image.pseudoyu.com/images/adventurex_workshop.jpg)

My main task was to serve as a mentor and workshop instructor, with the theme "Building a Full-Stack AdventureX Badge ÐApp Using Solidity and Remix".

I've given quite a few lessons and workshops in various settings. Initially, I was just helping out Ian's OpenBuild community, as I enjoy writing tutorials and sharing knowledge. But as these opportunities became more frequent, I noticed some changes in myself. I no longer use the same slides to repeat similar content each time. Instead, I treat each occasion as a new learning opportunity for myself, challenging myself to create something interesting within a limited time frame and then teach it. It's a kind of practice of the Feynman learning technique.

For this workshop, I wanted to learn the Remix frontend framework. I wrote a simple ÐApp for claiming event badges. You can experience it at "adventure-x.pseudoyu.com", and the PPT slides are available at "AdventureX_Workshop_20240716.pdf".

Although I knew about this workshop about a month in advance, I inevitably procrastinated until the last couple of days. I spent one evening learning from Randy's "Remix Practical Guide" booklet and completed the UI part. The next evening, I wrote the Solidity contract part and finished the interaction logic between the frontend and the contract, then deployed it online using Zeabur. Procrastination is truly a killer.

But Remix is indeed user-friendly. I achieved the feat of completing an application with zero useEffect and zero useState. I'm considering whether it can completely replace Next.js in various scenarios in the future.

More people showed up on-site than I expected. The workshop ran for twice as long as the planned 45 minutes, ending close to 10 pm. However, it was an interesting experience, and the workshop was quite successful.

### "Middle-aged Hippie" Hackathon

![code_with_randy_hackathon](https://image.pseudoyu.com/images/code_with_randy_hackathon.png)

Randy also came from Guangdong as a guest judge. We both felt that just observing the hackathon atmosphere was a bit too boring, so we decided to work on the redesign of EpubKit together.

We discussed the current operation logic and UI style changes for the entire EpubKit. It was very enjoyable. We spent several hours developing together in the evening, finding a sense of participation as "middle-aged hippies". We also discussed many ideas and division of labor for the future of the product, which I'm looking forward to.

Everyone is welcome to download and experience [EpubKit](https://epubkit.app/) to create your own e-books.

![yu_with_randy](https://image.pseudoyu.com/images/yu_with_randy.jpg)

As someone who doesn't like taking photos, I happened to be captured by the staff while looking at project exhibitions with Randy. It's quite a memorable photo.

## P.A.R.A Practice Based on Apple Notes

Last month, I switched from Logseq, which I had used for two years, to Obsidian. After about a month of practice, I developed more recording habits compared to when I was using Logseq. Although I no longer need to worry about folder hierarchies and such, I still need to overcome the mental burden brought by the chain of "recording ideas in my mind" -> "waiting until I'm at the computer to create a new file and give it a title" -> "organizing ideas and adding tags" -> "writing down the content".

![apple_notes_folders_20240721](https://image.pseudoyu.com/images/apple_notes_folders_20240721.png)

Randy told me about his method of using Apple Notes to record all ideas and notes, and categorizing them through the P.A.R.A hierarchy. I found that when there's no burden of organizing, and you can just open your phone/computer to record ideas anytime without considering format or markdown syntax, there's more desire to record. And being able to record and take action is the core purpose of note-taking.

On Mac, you can use Quick Notes in the bottom right corner for quick recording. On iOS, you can use shortcuts to quickly save fleeting ideas to the Drafts directory. Later, when you have more ideas, you can move them to various directories. It's a simple yet effective practice that doesn't require specifying various tags and categories. When needed, you can just use full-text search.

## Other Matters

### Wall Painting

![car_painting_wall](https://image.pseudoyu.com/images/car_painting_wall.jpg)

After learning oil painting and painting a portrait last time, I found it very interesting. Recently, I decided to challenge myself with something fun again. Together with my senior, we're planning to use acrylic paint to paint an entire cement wall in my father's auto repair shop (I'll be the assistant).

We sent my father's ideas and reference images we found on Instagram to DALL-E, and the generated effect is quite good. I hope we can have the finished product in August 🤩.

### Apple Vision Pro

![apple_vision_pro_experience](https://image.pseudoyu.com/images/apple_vision_pro_experience.jpg)

On Thursday this week, I went to Apple West Lake to experience the Vision Pro. Actually, I had been paying attention to it very early and had watched a lot of reviews. I was quite tempted at one point, but having had the experience of my Quest 2 gathering dust, I was still on the fence.

Coincidentally, the Chinese version was also launched, so I made an appointment for a half-hour experience. From fitting the lenses, explaining the accessories, to experiencing various functions and applications, the experience was better than I imagined. I didn't feel any dizziness or pressure from the weight in the 20 minutes or so.

In actual experience, the interaction was more fluid, natural, and accurate than I imagined. However, there was still quite noticeable noise in the image, and the resolution was not sufficient for an immersive experience, although it was quite impressive. There are still too few supported applications, so it's more of a novelty experience without many application scenarios. The typing experience is poor, so an external keyboard is still needed. Overall, this generation is not worth buying. Perhaps we'll consider it when both the price and the system application layer are more refined in the future.

### ChatGPT Plus -> Claude Pro

![claude_pro_sub](https://image.pseudoyu.com/images/claude_pro_sub.jpg)

Last month, due to high-frequency usage, I resubscribed to ChatGPT Plus while using Claude 3.5 Sonnet under the free quota. I found that Claude's contextual understanding ability and the usability of generated results for code were significantly better than GPT4. So when it expired this week, I decided to switch to a Claude Pro subscription to try it out for another month at the same price.

### Guii Experience

![guii](https://image.pseudoyu.com/images/guii.jpg)

[Guii](https://guii.ai/) was the most interesting project I saw at this Adventure X hackathon. It allows you to interact with the frontend page directly through natural language dialogue, and it will directly modify the source code to achieve interesting effects.

I made a very simple cryptocurrency website through simple dialogue by selecting elements. There are still some bugs, but it's highly playable.

I awarded them the OpenBuild Sponsor track prize, which was well-deserved. I hope it can go online soon 🔥.

## Interesting Things and Objects

### Input

Although most interesting inputs are automatically synchronized in the "Yu's Life" Telegram channel, I still select some to list here, which feels more like a newsletter.

#### Bookmarks

- [Lakr233/NotchDrop](https://github.com/Lakr233/NotchDrop)

#### Books

- [**Brave New Words**](https://book.douban.com/subject/36798526/), written by the founder of Khan Academy about thoughts and practices on GPT and the future of education. It provides many inspirations for daily use of LLMs. Beyond becoming a tool like search engines, there's still a lot of room for imagination.
- [**The Gig Economy**](https://book.douban.com/subject/36191471/), a book I thought of from the discussion about Radish Run. It explores the social divisions caused by technological acceleration, but more from the perspective of workers. I read it for a while in the afternoon, and the narrative style is also very comfortable.

#### Articles

- [A Ordinary Person in the Mortal World](https://www.boyilu.com/normal-people)
- [Elaborating on the Work Rhythm of Independent Creators](https://limboy.me/posts/indie-creator-routine/)
- [Local-First: A Different Developer Experience](https://leonzhao.cn/posts/2024-07-17-local-first-developer-x)
- [Sal Khan is pioneering innovation in education…again | Bill Gates](https://www.gatesnotes.com/Brave-New-Words)

#### Videos

- [The Best Choice for Beginner Photographers in 2024? | SONY ZV-E10M2 Review](https://www.bilibili.com/video/BV15w4m1Y72a)
- [How Do I Edit VLOG? 💻✨ | Full Post-production Process Revealed: Color Grading Techniques, Where to Find BGM, Quick Subtitling Methods~](https://www.bilibili.com/video/BV1Yz421B7nV)

#### Music

- [**Spring Breeze for Ten Miles**](https://open.spotify.com/track/0glre0pXcbXmVDWH5ZUKVs) by Mr. Deer Band
