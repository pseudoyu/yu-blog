---
title: "Weekly Review #26 - Blog, Custom Keyboard and New Server"
date: 2023-01-15T19:57:33+08:00
draft: false
tags: ["review", "life", "home", "cat", "hugo", "pagefind", "open-source"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

This is a record and reflection of my life from January 10, 2023 to January 15, 2023.

The holiday season is approaching, though I don't have much of a sense of ritual for the New Year. Last year, I spent over a week playing through "Pokémon Legends: Arceus" and revisiting "Fire Emblem: Three Houses". On New Year's Day, I made hot pot and had a video call with my family, and just like that, the year passed. However, since I've decided to go home this year, with arrangements for fostering Nini and various plans for the New Year, I haven't been able to relax much. I'm trying to finish many things in advance to free up some time to spend with my family.

Work-wise, I've had an average week. The recently launched requirements had a few minor issues in the details, forcing my leader and me to work overtime to address them. There's also a new feature that needs to be launched before the New Year, but testing isn't complete yet, with only two or three days left. The project I'm working on with friends has also encountered some problems. The friend originally responsible for the frontend had to leave, so I had to take over his part. The launch will be delayed, and I won't be able to truly relax during the New Year. It's quite an adjustment.

Because Nini will be fostered at a colleague's house, I took her to the vet for a check-up today, just to be safe, and also had her nails trimmed. The doctor said she's very healthy, and the previous minor ailments have basically recovered. He also praised me for taking good care of her, which made me happy. However, thinking about the fostering still makes me reluctant and worried. I'll come back early after the New Year, after all, now that I have something to be concerned about.

I accepted a rather intriguing interview, received an incredibly cute keyboard, continued to optimize my blog a bit (~~just optimizing the theme instead of writing articles~~), and many other interesting things happened.

## Interesting Things and Objects

### Blog Tinkering

My current version of my personal blog has been running for nearly three years now. Previously, I had used solutions like setting up WordPress on my own server, but later, due to lack of stability and difficulties in data migration, I switched to the once-and-for-all solution of Hugo static blog + GitHub automatic deployment + Cloudflare hosting. For details, you can check out "[Why I'm Still Blogging in 2022](https://www.pseudoyu.com/en/2022/06/12/why_i_still_write_blog_in_2022/)" and "[Deploy Your Blog Using Hugo and GitHub Action](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)".

The reason I chose Hugo, apart from the somewhat inexplicable but not particularly useful sense of familiarity due to my main job being Go development, is primarily because of the theme I'm currently using, "[den](https://github.com/shaform/hugo-theme-den)". This is a theme written by a Taiwanese developer himself. At the time, he was considering switching from [Pelican](https://github.com/getpelican/pelican) to [Hugo](https://gohugo.io/) due to factors like build speed, but he liked his original theme, so he recreated it himself. You can read more about it in his post "[Migrating from Pelican and WordPress to Hugo](https://city.shaform.com/zh/2018/07/22/migrate-from-pelican-and-wordpress-to-hugo/)".

I started following his blog for tech and personal thoughts output around 2018, and I can say that to a large extent, my later article style and thought patterns were greatly influenced by him. This theme, which carries a bit of the old internet style, perfectly matched my aesthetics, so after some tinkering, I set it up and have been using it until now.

Since it's primarily for personal use, although this theme is very aesthetically pleasing and minimalist, there are still some missing features. So over the three years of use, I've been constantly patching and modifying it according to my own needs. Last year, I also submitted PRs for my modifications to RSS Feeds, related articles, and friend links. Some of them were merged into the main branch after some communication, while a few are still pending (~~too lazy~~).

Recently, I discovered the [Pagefind](https://pagefind.app/) web search solution on [P.J. Wu's](https://twitter.com/WuPingJu) blog. After some research, I integrated it into my blog, and the effect is quite good.

![pagefind_and_hugo_2](https://image.pseudoyu.com/images/pagefind_and_hugo_2.png)

It adopts the approach of pre-generating article index files instead of real-time retrieval, which makes it very fast and doesn't require additional backend services, making it very suitable for static blog deployment solutions. For an introduction to Pagefind and its usage, you can check out [P.J. Wu's](https://twitter.com/WuPingJu) article "[How to Add a Search Function to Zola-generated Static Websites via Pagefind](https://pinchlime.com/blog/how-to-add-a-search-function-to-zola-generated-static-websites-via-pagefind/)", although it's about integrating into the Zola blog framework and publishing through Netlify, the principle is similar. As for the integration method for Hugo, I'll write an article after I've tinkered with the configuration. You can preview it at [this address](https://www.pseudoyu.com/en/search), or click on "Search" in the navigation bar (I've added a back-to-top function, you can click to return directly).

I integrated it into my original GitHub CI automatic publishing workflow, and the experience is seamless. I also integrated a search page UI through Hugo's shortcode method for use, which is very powerful. I'll also submit a PR to the theme repository to support this, to see if there's any demand in this area.

However, after using it, I found some issues with Chinese support. It can't segment words very well. For example, searching for "区块链" (blockchain) directly won't match, but changing it to "区块 链" (block chain), manually segmenting the words, will give the desired effect. I've noted the search method on the page, ~~it's not unusable after all~~. We'll see if there are better solutions in the future.

![pagefind_and_hugo_1](https://image.pseudoyu.com/images/pagefind_and_hugo_1.png)

Interestingly, my blog tinkering for this week was supposed to end here, but suddenly GitHub emailed me about a PR and comments. A stranger had forked my blog and made some style adjustments and modifications, adding some features. Later, he even sent me his improved CSS file for reference.

![github_blog_pr](https://image.pseudoyu.com/images/github_blog_pr.png)

Originally, these were just some solutions for personal use, and I often found myself happily tinkering with the theme for an afternoon without writing a word. I didn't expect that some people would notice, appreciate, and adopt it, and even solve many of my problems in return. It feels quite wonderful, and I'm starting to feel the joy of open source or working in public. There are always some unexpected gains. So last night, I spent some time tinkering, fixing several style issues that had been problematic for a while but I hadn't fixed or paid attention to, and even added a back-to-top button effect. I was quite happy about it.

### Server

As mentioned in a previous weekly review, after figuring out how to set up reverse proxy for my server using [Nginx Proxy Manager](https://nginxproxymanager.com/), I launched several commonly used services and sites, such as the previously mentioned [zlib.pseudoyu.com](https://zlib.pseudoyu.com/) book search service. Because it received some attention and was included in some groups and channels, I wanted to continue maintaining it to ensure service stability and access speed. However, previously, these were all low-performance machines that were running at full capacity with just a few services. So, taking advantage of Bandwagon Host's launch of a new decent plan, I got a few machines: 2C2G + 40G hard drive + CN2GIA DC6 line, which is completely sufficient for long-term stable operation of some services.

![yu_services_vps](https://image.pseudoyu.com/images/yu_services_vps.png)

I also had some other machines before, running some of my basic services, with some small applications set up for friends to use. This time, I organized everything well, migrating all services to one machine. Here, I have to praise Docker and docker-compose management methods - the data migration was so seamless. After migrating everything, it only took up about half of the resources, which is great.

Because I now have more machines (a happy problem), I also found an open-source monitoring service for management. It gives me a feeling of being a cyber capitalist, supervising these machines to work hard and not slack off.

![yu_server_status](https://image.pseudoyu.com/images/yu_server_status.png)

### Desktop Setup and Keyboard

Perhaps because I don't play games, I'm not actually a hardcore keyboard enthusiast. I can hardly tell the difference between different switches and keycaps, and I've mostly used Mac's built-in scissor-switch keyboards before without feeling any discomfort.

It was probably around the end of 2020 when she asked me if there was anything I'd always wanted but couldn't quite bring myself to buy. After thinking for a long time, I said HHKB. Actually, it was more out of curiosity than practical need, and the retro design of the old-style battery compartment was completely in line with my aesthetics.

A few days later, I received it. It was the HHKB Professional Hybrid Type-S silent version, with an old IBM-style color scheme. The electrostatic capacitive feel, combined with its compact size, I really liked it. It also coordinated very well on the desktop.

![keyboard_hhkb_type_s_1](https://image.pseudoyu.com/images/keyboard_hhkb_type_s_1.jpg)

Every morning before starting to study and work, I always arrange my environment a bit, carefully placing the keyboard. This keyboard has accompanied me from Hong Kong to Beijing, and I even bring it every time I go out to a coffee shop. At first, it might have just been a habit, but gradually it became a kind of ritual. It seems to have added some joy to coding and writing.

![keyboard_hhkb_type_s_2](https://image.pseudoyu.com/images/keyboard_hhkb_type_s_2.jpg)

After using it for over a year, because I really liked the feel of the electrostatic capacitive switches, I couldn't help but want to try the remaining few classics. So, also as a gift, I received a RealForce PFU limited edition 87-key keyboard. This one also looks very nice, with a metallic feel in low light environments. However, perhaps because I was used to the special key layout of the HHKB, suddenly switching to an 87-key layout often felt a bit uncomfortable. So it ended up being used more by her for gaming. Anyway, a keyboard can't save my clumsy gaming skills.

![realforce_pfu_87](https://image.pseudoyu.com/images/realforce_pfu_87.jpg)

The RealForce was later left idle. And I really couldn't get used to large-sized keyboards anymore, so I sent it to Ni, who was in Australia. (Come to think of it, my first mechanical keyboard was also a gift from him, a Cherry, though I forgot which switch it had. I used it at home for almost a year when I was still using Windows, and it was quite nice.)

Although HHKB and RealForce seem to be more well-known, in my personal experience, the most exquisitely crafted and best in terms of quality among the three classics of electrostatic capacitive keyboards is actually the Leopold FC660C that I acquired in the middle of last year. The color scheme and typing feel are more comfortable, truly making one enjoy the experience. It subsequently became the main keyboard for my home desktop.

![keyboard_leopold_fc660c](https://image.pseudoyu.com/images/keyboard_leopold_fc660c.jpg)

Actually, at this point, my keyboard usage needs were fully met, and I didn't have much energy to pursue the ultimate or play with customization. However, one late night, I came across "[【Self-made】I Made a Modular Mechanical Keyboard!【Soft Core】](https://www.bilibili.com/video/BV19V4y1J7Hx)" by Zhihui Jun, a keyboard redesigned and defined from circuit hardware to firmware code, all done by himself. Who could resist that?

During the National Day holiday, I happened to see that he had launched a co-branded keyboard with Bilibili. I ordered it without hesitation. Indeed, the pink color is very attractive. This is also my first custom keyboard in a sense.

![keyboard_hello_word_75](https://image.pseudoyu.com/images/keyboard_hello_word_75.jpg)

Then came several months of long waiting, and finally it arrived in my hands this week. I have to say, both the appearance and the feel are excellent. I quickly changed my desktop layout and happily typed away for a week. Maybe appearance is the primary productivity after all. I feel like my article and code output increased this week. Xiaoyu commented, "How come your whole persona changed just because of a new keyboard?"

![chat_with_xiaoyu_about_keyboard](https://image.pseudoyu.com/images/chat_with_xiaoyu_about_keyboard.png)

I don't have a collection habit, nor do I want to pursue the ultimate feel or custom solutions. It's just that I've always had a great desire to tinker with things that I interact with daily, like desktop arrangements, computers, keyboards, and software tools. Even if it's just a few seconds of speed improvement or a little bit of mood enhancement, it's something worth doing for me.

## Personal Life Snapshots

### Learning

I didn't study Japanese... Failed the first week of check-ins!

### Output

In terms of output, I translated an article for GoCN: "[Go 1.20 New Changes! Part One: Language Features](https://www.pseudoyu.com/en/2023/01/12/golang_120_language_changes/)"; after posting last week's review, I met quite a few new friends, and this week I also posted several tweets about blog setup; I have an article scheduled with Sspai, but I'm not sure when I'll write it.

### Input

#### Books

- **What I Talk About When I Talk About Running**, I started reading this book in October, but various things happened in between and I fell behind on my reading progress. Recently, I've been slowly reading it in my spare time. I really love Murakami's style of speaking, and I want to read all of his books.

#### Anime

- **Mob Psycho 100**, I watched it once a few years ago and thought the setting was interesting, but didn't really appreciate it in depth. Recently, I wanted to revisit it. The first season has a lot of origins, bonds, and changes of the main characters. While being a funny daily life anime, it also gives people a lot of ideas and thoughts. I binge-watched the second and third seasons. If the first season only described some bonds, the second and third seasons brought me too much emotion. The growth of characters, the changes in people around them, despite the setting of being espers, they constantly self-deny in daily life and self-accept under the influence of people around them. I like the side conversation scene between Mob and Reigen after the press conference the most, emotions are already unspoken.
- **Bungo Stray Dogs**, I've heard about it for a long time, just started following it.
- **The Three-Body Problem**, I guess the mentality of following the drama adaptation is to see what kind of psychedelic operation you can have.
