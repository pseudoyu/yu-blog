---
title: "Personal Information Retrieval and Knowledge Management System (Heptabase + Logseq + Readwise)"
date: 2023-09-05T02:38:39+08:00
draft: false
tags: ["pkm", "information", "note-taking", "logseq", "heptabase", "readwise", "xlog", "xsync", "productivity", "tools"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

![yu_blog_my_pkm_system](https://image.pseudoyu.com/images/yu_blog_my_pkm_system.png)

I seem to have always had a tendency to view myself as a machine, often observing myself from an outsider's perspective, integrating various modules, and constantly tinkering and optimizing. When a certain behavioral pattern or habit I've built suddenly proves useful at a particular moment, I feel a sense of delight. Conversely, when external influences or my own state disrupt the system, I experience a profound discomfort from the breakdown of order.

As an efficiency tool enthusiast, my personal knowledge management and information management can be said to be the most important part of myself. I actually had no intention of writing this article, as there are too many precedents and practices before me, and I'm only making minor adjustments and optimizations based on the work of others. I often lack the confidence to share, but this week I rebuilt and optimized my knowledge management system, and I'm very happy about it. I had an urge to document it, and although I initially intended to just mention it briefly in my weekly review, I found myself unable to stop writing. Thus, this article came into being.

In fact, I've often mentioned information output in my weekly reports before, so this article will also cover some previous content and finally supplement the parts about information acquisition and knowledge management. It will serve as a comprehensive collection. Regarding the theoretical aspects, such as the "Feynman Learning Technique" and the "Luhmann's Zettelkasten Method," there are already many excellent introductory articles, so I won't spend space introducing them here. Instead, I will focus more on describing the software tools I use in practice, hoping it will be helpful to everyone.

## Information Acquisition and Management

I'm not sure when it started, but I can clearly feel my dependence on information from the online world. Perhaps unlike gaming addiction or the oft-criticized short video algorithm "opium," my dependence is not mechanical scrolling or an escape from anxiety, but a craving for information acquisition that has even internalized into a way of life. Because I have confidence in my ability to filter and digest information, I haven't actually spent much effort on input sources and organization.

However, as I've come into contact with and become interested in more and more fields, information has continuously accumulated. Sometimes, just browsing and reading through it all has exceeded my memory capacity. Often, this information is scattered in my notes or in some corner of my mind, and has not become an internalized part of me. It's also difficult to recall or retrieve later. So, I've re-examined my method of information acquisition.

### Information Source Classification

My sources of information can be broadly categorized as follows:

1. Random thoughts
2. Information flow
3. Focused reading

#### Random Thoughts

![logseq_random_thoughts](https://image.pseudoyu.com/images/logseq_random_thoughts.png)

In daily life, work, study, or at any random moment, I sometimes have random thoughts that are unrelated to what I'm currently doing or are flights of fancy, but might be useful at some point in the future. Since I'm rarely far from my computer for most of the time, I usually record these in Logseq's Journal. Sometimes I might temporarily send them to a WeChat group with only myself in it or to Telegram's Saved Messages, and later add them to Logseq.

#### Information Flow

From the moment I wake up every day, I'm enveloped by information flows from various platforms. Relying on the online world inevitably involves struggling with social media and algorithms. On one hand, we need to avoid being troubled by excessive anxiety-inducing information or the "Peer Pressure" from our social circles. On the other hand, we also need to be wary of the information cocoons constructed by algorithms. To be honest, this is quite difficult to achieve. Even though I more or less have some ability to restrain myself and filter information, and am consciously trying to do so, it's still hard to avoid having my thoughts disturbed or guided by it.

I eventually adopted a simple yet effective approach - turning off the WeChat Moments entrance and most app notifications, and limiting the number of follows on platforms that are primarily for information acquisition rather than social interaction (such as Bilibili, Weibo, etc.) to within 100. If I add new ones, I filter and optimize the previous follows to reduce irrelevant content interference. Based on these actions, I use RSS subscriptions, which might seem a bit old-fashioned, but I only subscribe to fewer than 50 websites, most of which are blogs or personal websites, and I regularly filter them to reduce my daily feeds. However, I scan the titles or briefly browse almost all the articles in this feeds list.

![readwise_reader_feeds](https://image.pseudoyu.com/images/readwise_reader_feeds.png)

Initially, I set up my own Miniflux service to fetch this, and used an [RSS-to-Telegram-Bot](https://github.com/Rongronggg9/RSS-to-Telegram-Bot) to push notifications. Recently, after starting to use [Readwise Reader](https://read.readwise.io/) and finding the experience very good, I migrated this part over. I use a management mode built into Readwise Reader, divided into three categories:

1. Later
2. Shortlist
3. Archive

I scan the Feeds panel every day, and add interesting articles to Later as a read-it-later list. Of course, from past experience, items in read-it-later lists often become "never read later" if left for too long. So, I'm very restrained when filtering, only adding articles I'm very interested in and will read immediately when I have time, and requiring myself to clear the Later list in the evening.

We also get pushed information from various corners of social media and the internet, among which I'm particularly concerned about these categories:

1. Interesting viewpoints/tweet threads
2. Articles of interest
3. Useful resources

If it's some interesting viewpoints or comments, I usually don't add them to the corresponding List, Favorites, etc. of the software, but instead copy their content to Logseq's Journal and tag them accordingly. Actually, many softwares (including Readwise Reader) provide ways to save tweet threads or other convenient methods to save tweets, but I prefer to copy and organize them myself, recording them in a few sentences rather than just saving a link. This seemingly deliberate increase in steps allows me to review these viewpoints one more time, avoiding being influenced by strongly guided or emotional viewpoints, and is more conducive to digesting information and internalizing it into my own thoughts.

![readwise_chrome_extension](https://image.pseudoyu.com/images/readwise_chrome_extension.png)

If it's some articles I'm interested in, I read or save them using Readwise's Chrome extension. For this part, I require myself to tag and add notes to every article, with the notes mainly describing why I want to read this article.

![readwise_chrome_extension_highlight](https://image.pseudoyu.com/images/readwise_chrome_extension_highlight.png)

Among these, if it's just articles that need to be skimmed or for information gathering, I add them to the Later list. For in-depth reading, I add them to the Shortlist, and must highlight some meaningful parts, and try to add my own comments and thoughts to the highlights. All of this can be done directly in the plugin, which is very convenient.

![pinboard_bookmark](https://image.pseudoyu.com/images/pinboard_bookmark.png)

If it's some useful websites, documents, code, software or other resource-type information, I use [Pinboard](https://pinboard.in/), a very old but useful bookmark management tool to save them. Similarly, I use a browser extension to save them, and also add tags and brief descriptions. In about a year, I've accumulated 455 bookmarks, most of which I can quickly retrieve through tags and names when I need to use them.

For video sites and the like, I mostly use likes or favorites, on one hand to show support for the creators, and on the other hand to sync them to my personal Telegram channel "[Yu's Life](https://t.me/pseudoyulife)" through some automation tools, and mark them with corresponding tags. However, most videos are not very information-efficient, so they are more for interesting or exploratory content.

#### Focused Reading

Apart from these passively pushed information flows mentioned above, we also have many specific topic or field-related information needs that require us to actively read some books, reports, etc.

![wechat_reader_sync_readwise](https://image.pseudoyu.com/images/wechat_reader_sync_readwise.png)

For this part, I originally used Kindle or read physical books more, and manually made some records in Logseq. But after [Randy](https://lutaonan.com/) launched the [Notepal](https://notepal.randynamic.org/) tool, I started using WeChat Reading. It has many readable book resources, and I also use it to import books in mobi or epub format. The reading experience is quite good.

![wechat_reader_to_readwise](https://image.pseudoyu.com/images/wechat_reader_to_readwise.png)

It's also very convenient to make some notes and annotations. Due to cross-platform synchronization, it's easy to periodically sync to Readwise through the Notepal browser extension, and the effect is also very good (the above image is synced over). This also provides more motivation to read some books in fragmented time.

### Information Management

In the previous section, I sorted out some channels and systems for information acquisition, but these are still scattered information. To make them part of our own knowledge and thinking, we still need more processes of organization, digestion, and precipitation. But with so many platforms involved, searching and organizing is not convenient, and it's also quite difficult to establish associations between information. Inspired by the book "Building a Second Brain" that I'm currently reading, I mainly did the following two things:

1. Borrowed and modified P.A.R.A as my global Tag classification system
2. Built a Second Brain using Logseq and Heptabase

#### Global Tag System

![pama_framework](https://image.pseudoyu.com/images/pama_framework.jpg)

P.A.R.A is a framework proposed by the author, which stands for:

- Projects, related to ongoing projects
- Areas, specific domains
- Resources, resources that might be used in the future
- Archives, completed projects

Based on these four types, I added a "Thoughts" to categorize some of my random ideas.

![logseq_tag_system](https://image.pseudoyu.com/images/logseq_tag_system.png)

My implementation idea is to use these five types as my global first-level Tags, while more specific projects, domains, industries can be used as second-level, third-level Tags, such as `Projects/writing/pkm`, `Areas/blockchain`, `Thoughts/weekly-review`, etc. Logseq provides a very powerful multi-layer Tag system, which automatically layers according to `/`, facilitating retrieval and making classification clear at a glance. After modifying some of my existing Tags, the effect is as follows:

![para_logseq_graph](https://image.pseudoyu.com/images/para_logseq_graph.png)

#### Second Brain Based on Heptabase + Logseq

I've been using Logseq as my knowledge management system all along. Recently, I saw that [P.J. Wu](https://twitter.com/WuPingJu) joined Heptabase, and learned more about this platform, so I incorporated it into my knowledge management system, using it together with Logseq to build my second brain. As long as we follow the Tag system mentioned above, the two platforms don't need additional associations to manage information independently.

![logseq_sync_readwise_sample_page](https://image.pseudoyu.com/images/logseq_sync_readwise_sample_page.png)

Among them, Logseq, as a note-taking system that combines simple task management and bidirectional links, is very suitable for precipitating these information flows and some initial ideas produced after my reading, such as highlights and comment notes. Since Logseq has an official Readwise plugin, it's very convenient to automatically synchronize my highlights and notes from WeChat Reading and online articles as Logseq pages, and associate them with Journal through time. This way, I can intuitively see my past readings and thoughts when I write some reviews every day/week. For example, the above text is some highlights and notes I made using the Readwise Chrome extension on his website while reading [Justin Yan's](https://twitter.com/MapleShadow) article "[Everyone has only 24 hours a day, I hope my choices are really my choices](https://justinyan.me/post/5790)", which was automatically synchronized to Logseq, and tagged with some tags and properties according to my configuration.

Logseq is very suitable for information organization and review, but when I need to research a certain field/concept, organize the context of reading books, or output a blog post, it seems a bit thin. Its information is scattered in each day's Journal in units of blocks, associated and jumped through bidirectional links or tags, which is not convenient for some direct visual association, and also requires oneself to be clear enough about keywords and tags in the early stage, still having some cognitive burden. So for this part, I use Heptabase for management.

Heptabase can be seen as a fully functional whiteboard note-taking tool. [P.J. Wu](https://twitter.com/WuPingJu) has many [high-quality introductory articles](https://pinchlime.com/tags/heptabase/) about Heptabase, which you can read to learn more. In simple terms, it is mainly divided into the following three levels:

- Map
- Whiteboard
- Card

![heptabase_map_overview](https://image.pseudoyu.com/images/heptabase_map_overview.png)

Among them, Map can be seen as the entire space of our Second Brain, which can contain various whiteboards. I created five whiteboards as the first-level Tags.

![heptabase_whiteboard_overview](https://image.pseudoyu.com/images/heptabase_whiteboard_overview.png)

Cards represent individual ideas or independent information points in our brains. We can organize our knowledge through the association between cards and the hierarchy between whiteboards and cards.

When I was writing the tutorial for the Foundry smart contract development framework, I first laid out some scattered knowledge points or experiences and lessons encountered in practice as individual whiteboards on the Foundry whiteboard (which is the fourth-level sub-whiteboard under `Projects` - `Blockchain` - `Smart Contract`). When a certain knowledge point is sufficient, I would make some Section groupings and line connections between whiteboards.

It also provides native integration with Readwise, allowing us to directly select some highlights and notes from certain articles or books in Readwise as cards and introduce them into the whiteboard in the right sidebar, establishing some associations for them. It's very similar to the process of our brain organizing scattered information or brainstorming, perfectly meeting my needs.

![heptabase_chiangmai_trip](https://image.pseudoyu.com/images/heptabase_chiangmai_trip.png)

I currently also use it to make some travel guides, putting information points from Xiaohongshu and other people's strategy posts as individual cards on the travel planning whiteboard, and then organizing them through associations and groupings, which is very neat.

## Information Output

My output mainly includes the following parts:

1. Notes/Viewpoints/Daily Life
2. Long Articles
3. Thematic Research
4. Information Flow

### Notes/Viewpoints/Daily Life

![yu_twitter_profile](https://image.pseudoyu.com/images/yu_twitter_profile.png)

Among them, Twitter "[pseudo_yu](https://twitter.com/pseudo_yu)" is my main channel for unstructured information output. Sometimes it's some ideas about new technology, feelings about work, emotions about meeting friends, or a cute cat picture, all of which constitute my output and also correspond to the quick production of those random thoughts in my input.

The friends I met on Twitter have also brought me a lot of warmth.

### Long Articles

![yu_blog_homepage](https://image.pseudoyu.com/images/yu_blog_homepage.png)

My most important output platform is my personal blog "[Pseudoyu](https://www.pseudoyu.com/)". Currently, the weekly review is my main outlet, and occasionally there are also some themed or special blog posts about technology or productivity tools.

### Thematic Research

Outputting a blog post, due to considerations of audience, wording, expression, and completeness, actually has a certain cognitive burden and a longer cycle. In the process of conducting thematic research in specific fields, I mostly put learning materials and some demos in GitHub repositories or in some corner of Logseq notes. Sometimes, after a long time, I have to relearn them. Now I put them more in a whiteboard in Heptabase, which can store many small knowledge points and further summarize and refine them in subsequent creations. So I can actually share this whiteboard after it has a basic framework, which allows for more communication with others and can also be helpful to friends who are learning the same thing.

### Information Flow Output

![yu_telegram_channel_screenshot](https://image.pseudoyu.com/images/yu_telegram_channel_screenshot.png)

I set up my own n8n synchronization service to collect my scattered information input and output on various platforms, and I also post my thoughts on movies, books, and other thoughts in my Telegram channel "[Yu's Life](https://t.me/pseudoyulife)". I also follow some channels and groups to get some information or meet like-minded people, and occasionally forward manually. The main platforms I synchronize are:

- Blog, which now looks more like a life log.
- YouTube, I'm also a heavy user, watching a lot of technical tutorials and digital information, and occasionally there's a lot of interesting content.
- Bilibili, mainly retaining some bloggers I've been following for many years, watching travel vlogs more, only viewing dynamics and not the homepage or hot topics.
- Pinboard, a bookmark and website saving management tool, which I heavily rely on.
- Instapaper, managing read-it-later items, mainly saving some high-quality or long articles.
- GitHub, also browsing daily, looking at some good projects, and managing Stars with lists.
- Spotify, marking good songs.
- Douban, recording my books, TV series, movies, anime, and games. I'm also a heavy user, and I'm trying to write my own review for every work I've watched/played.

## Data Backup

Although platforms like Twitter and Telegram are already quite large, they are still centralized products. Plus, with all the recent turmoil, I'm always uneasy about using Telegram as the final station for aggregating these information sources, especially since I often almost accidentally click to delete all messages when deleting messages (strange interaction experience). Therefore, the synchronization and export of information is also a very important part. I use the [xLog](https://xlog.app/) and [xSync](https://xsync.app/) services under the Crossbell ecosystem for on-chain backup of my blog and information from various platforms.

### xLog

![yu_xlog_profile](https://image.pseudoyu.com/images/yu_xlog_profilea6f9af1d5482abc7.png)

The visual effect and experience are quite good, and it's easy to follow and comment based on the Crossbell address. It includes features like NFT showcase and personal portfolio. This is my [xLog access address](https://xlog.pseudoyu.com/), interested friends can also follow. However, currently, considering the degree of customization, various historical article migration routing issues, changes in my own data statistics services, etc., it's still more of a synchronization distribution channel.

### xSync

![yu_sync_profile](https://image.pseudoyu.com/images/yu_sync_profile.png)

xSync can synchronize platforms like Twitter, Telegram Channel, etc. Without any invasive modifications, it can make a second backup and archive of my aggregated channel. In the future, I can view my various messages through xChar, which is a perfect solution. This is my xChar personal homepage: [xChar](https://xchar.app/pseudoyu), and you can also view my information flow through [xFeed](https://xfeed.app/u/pseudoyu).

## Conclusion

> it is probably a mistake, in the end, to ask software to improve our thinking.

[Casey Newton](https://www.theverge.com/authors/casey-newton) said so in a recent article "[Why note-taking apps don't make us smarter](https://www.theverge.com/2023/8/25/23845590/note-taking-apps-ai-chat-distractions-notion-roam-mem-obsidian)". Indeed, these systems or software tools can ultimately only assist us in information management and output, and cannot replace our thinking. However, building a knowledge management system, while pleasing ourselves, can also make thinking more efficient. Pleasing oneself is the way to reach others, thereby producing more valuable output.

I hope this article can be helpful to everyone.