---
title: "Weekly Review #54 - Drifting Plan, Stolen Wallet, and Home Server"
date: 2024-03-16T05:20:00+08:00
draft: false
tags: ["review", "life", "travel", "computer", "work", "love", "home assistant", "home server"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="'Photograph - Ed Sheeran'" >}}

## Preface

![weekly_review_20240316_cover](https://image.pseudoyu.com/images/weekly_review_20240316_cover.png)

This piece is a record and reflection of my life from `2024-03-01` to `2024-03-16`.

As mentioned in the previous weekly review, I embarked on a drifting plan, which concluded with a nearly two-week journey through "Hangzhou -> Shanghai -> Huzhou -> Nanjing -> Beijing". Mostly confined to Jiangsu and Zhejiang, there weren't any extraordinary landscapes; it was more about people and events. Due to my main wallet being stolen without determining the cause, I reinstalled two primary computers, which provided an opportunity to reorganize my development environment configuration. I set up the Mac Studio at home as a 24/7 Home Server, running constant applications like Home Assistant to control smart home devices - a tinkering process that proved quite interesting. At work, our team's long-awaited Alpha mainnet went live, bringing back a sense of excitement I hadn't felt in a while. There were many other intriguing occurrences as well.

## Drifting Plan

![tianmushan_view](https://image.pseudoyu.com/images/tianmushan_view.jpg)

The first stop of my post-New Year drifting plan was Shanghai. Over the years, I've been there dozens of times, from one or two-month internships to brief stopovers. Usually, these visits were for specific purposes or to meet people. Truly "living" there was a rare opportunity. This time, I didn't choose a bustling area or plan any special outings. Instead, I booked a week-long stay at a rental near a friend and resumed my normal work and study routine.

Occasionally, I'd venture out to nearby commercial areas for food. On weekends, I met up with long-unseen college roommates for meals. The rest of the time, I worked from the hotel, even managing to finish the long-awaited "Westworld" series. Coincidentally, a colleague lived just a kilometer or two away, leading to a small three-person team gathering.

Next, I visited Huzhou, staying at my friend [Xiao](https://twitter.com/gxgexiao)'s place for a week. Our encounter stemmed from a tweet he posted a year ago during his [wanderings across various places](https://www.gexiao.me/2023/07/01/lets-wander/), inviting friends in Hangzhou to meet. At that time, I had just returned to Hangzhou, full of uncertainty and anticipation for my future life. Mustering courage, I arranged a dinner and a stroll by West Lake. Despite it being our first meeting and having little in common, it was genuine and trusting.

Later, he moved to Huzhou. I had planned to visit in August but couldn't make it due to various reasons, which left me feeling regretful. So, I took this drifting opportunity to fulfill that promise. We hiked off-trail in Moganshan, walked along the cliffs of Anji's Cloud Prairie, and visited two digital nomad communes. I was quite drawn to their community atmosphere. This year, I seem to have rediscovered a long-lost sense of relaxation in life, becoming more willing to meet people and experience new things. Life is no longer just about work and study; people and everything related to human connections have become more appealing to me. Due to deeper connections with many "online friends," the boundaries between my online and offline relationships have gradually blurred.

Thanks to the company's "Work Together 1 Hour" every Wednesday, a colleague recommended the hot springs in Tangshan and the forest library in Moganshan. So, I arranged to meet with a senior schoolmate in Nanjing, enjoying a leisurely week and starting to explore some weekend getaway destinations. Life has become more tangible.

## Stolen Wallet and Device Reinstallation

Recently, I reinstalled the systems on both my laptop and home desktop. The catalyst was the unfortunate theft of my main wallet. Based on the blockchain records, it happened around noon on the first day of the Lunar New Year. All assets in the wallet (including some airdrops from participating in open-source projects) were converted to ETH and BNB before being transferred out. The wallet still contained my ENS and some NFTs (~~which the hacker apparently didn't care for~~). The overall financial loss wasn't significant, but because I couldn't pinpoint how the private key was leaked, I had no choice but to reinstall all device environments - a major undertaking.

Since both systems were macOS, the system settings and software aspects were fairly straightforward. I mainly referred to my personal toolbox project "[GitHub - yu-tools](https://github.com/pseudoyu/yu-tools)", but made quite a few subtractions, keeping only the essentials. I discovered that after uninstalling [Rewind](https://www.rewind.ai/), my MacBook Pro's battery life improved significantly - I can now go out almost without needing to bring a charger.

![x-cmd_env_install](https://image.pseudoyu.com/images/x-cmd_env_install.png)

I also took this opportunity to organize my software installation sources, development environment management, and command-line configurations. I tried out the "[x-cmd](https://cn.x-cmd.com/)" project developed by a friend's company.

![zshrc_config](https://image.pseudoyu.com/images/zshrc_config.png)

Combined with ohmyzsh, I simplified my command-line configuration to just a dozen or so lines. Later, I can manage various environments and command-line tools through commands like `x env`, which is very user-friendly.

![x-cmd-env-ls](https://image.pseudoyu.com/images/x-cmd-env-ls.png)

Finally, I used `x env` to manage my Go, Node, and Python development environments, eliminating the need for various steps like installing nvm and setting environment variables. I also experienced enterprise-level customer support (referring to bombarding my friend on Telegram to solve problems 🤣). It will become part of my standard setup in the future, and I'm still in the process of deep exploration.

Additionally, I unified the management of ssh keys and GPG signatures between the two devices. Combined with Elpass for password management and automatic server login, I achieved a seamless experience switching between commuting and staying at home.

## Home Server & Home Assistant

~~Perhaps as I'm getting older~~, I couldn't escape the three great temptations: routers, charging heads, and NAS. For the router, I'm using the Asus AC86U I bought from [STRRL](https://twitter.com/strrlthedev) last year, flashed with the latest Merlin firmware, which is quite sufficient, so I didn't bother with software routers. As for charging heads/chargers, after experiencing the Flashex fully transparent power bank, 100W GaN charger, and Hard Candy Factory mini charger (~~which I'm a bit wary of using now~~), I've cooled off on that front as well.

Finally, I extended my reach towards NAS. After a long chat with Ares, our reliable ops & deep NAS DIY enthusiast in our team, I decided to first use the Mac Studio at home as a Home Server.

![yu_home_assistant_macstudio](https://image.pseudoyu.com/images/yu_home_assistant_macstudio.png)

The first thing I did was connect all the smart devices at home to Home Assistant. However, due to the Apple M1 chip, there was no ready-made official solution. After much tinkering, I finally followed the article "[Run Home Assistant on macOS With a Debian 12 Virtual Machine](https://siytek.com/home-assistant-macos-utm-debian-12/)" to install an Arm architecture Debian virtual machine using UTM. I ran a full version of Home Assistant inside it and used frp to map the interface to the public network. Finally, I operate it directly using the iOS app and web version. The current solution might have issues with the virtual machine's network mode, so I can't add it to the Apple Home App via HomeKit Bridge yet, but being able to link all the Xiaomi, Yeelight, and Petkit pet devices is sufficient for now.

As a Home Server, it maintains 24/7 operation with barely noticeable noise and power consumption. I enabled smb file sharing, ssh remote login, and remote vnc desktop control, and ensured I could access home devices from outside through intranet penetration.

To ensure security and stability, I adopted three different intranet penetration solutions simultaneously:

1. frp
2. Surge Ponte
3. Cloudflare Argo Tunnel

I've been using the first solution for nearly two years, as detailed in the article "[Thin Client Development Workflow Based on frp Intranet Penetration](https://www.pseudoyu.com/en/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)". It requires a public network server but is simple to configure and stable. Currently, I've only retained the ports for ssh and Home Assistant.

The second solution achieves convenient intranet penetration between macOS/iOS devices through the Surge software. You can see its detailed introduction in "[Surge Ponte Guide](https://kb.nssurge.com/surge-knowledge-base/guidelines/ponte)". It requires a proxy line that supports UDP, but is otherwise almost plug-and-play. I use it to access files on the home Mac Studio and some local services, and can also directly access and configure home intranet routers from outside, mainly for personal use.

The third solution was recently added after seeing the article "[Accelerate and Secure Your Website with Cloudflare Argo Tunnel (cloudflared)](https://nova.moe/accelerate-and-secure-with-cloudflared/)". Previously, I had been manually configuring it using the cloudflared command-line tool, which was somewhat troublesome, so I hadn't put it into practice. Recently, Cloudflare integrated it into [Zero Trust](https://developers.cloudflare.com/cloudflare-one/), allowing almost all operations to be configured through the interface. I use it to run some services that need to be exposed to the public network on the home server. For example, the other day I ran a [codellama:70b](https://ollama.com/library/codellama:70b) using [ollama](https://ollama.com/), and then accessed it directly through [ChatKit](https://chatkit.app/). The experience was quite good, just a bit slow in generation, so it was more of a trial run.

Coincidentally, our company's [Alpha mainnet](https://rss3.io/blog/en/introducing-rss3-alpha-mainnet) has just gone live. I plan to run one myself on the Home Server when the public node is available, but can't afford to run it now 🤣.

## VR Driving Lessons

![vr_car_learn](https://image.pseudoyu.com/images/vr_car_learn.png)

Due to some upcoming self-driving needs, I re-enrolled in driving school to start learning. This driving school has VR driving facilities, which I found less intimidating than I had imagined.

## Other Matters

There don't seem to be many other interesting things to mention. I find myself alternating between busyness and anxiety over not being able to do all the things I want to do, but everything is slowly getting better.

GitHub provided a free Copilot license for open source, allowing me to continue freeloading on code completion and Copilot Chat. Combined with Claude 3 Sonnet and the free GPT4 tokens from "[burn.hair](https://burn.hair/register?aff=isWf)", I can now meet all my coding and various other needs.

Oh, and I managed to arrange a meeting with my idol programmer "[Randy](https://lutaonan.com/)" in Beijing at the end of the month!!!

## Interesting Things and Objects

### Input

Although most interesting inputs are automatically synced in the "Yu's Life" Telegram channel, I'll still select a few to list here, making it feel more like a newsletter.

#### Books

- [**The Monk and the Philosopher**](https://book.douban.com/subject/2228297/), some thoughts on religion and philosophy, just started reading a bit as it came up in conversation.
- [**The Red and the Black**](https://book.douban.com/subject/35781152/), saw an interpretation in a video, deeply impressed by the description of Julien's self-esteem and the arrogance it manifests, currently reading.

#### Collections

- [Million Lint is in public beta | Million.js](https://million.dev/blog/lint)
- [Discover Daily by Perplexity](https://discoverdaily.ai/)
- [Ehco Relay](https://ehco-relay.cc/)
- [RSS3 Alpha Mainnet](https://rss3.io/blog/en/introducing-rss3-alpha-mainnet)
- [Velja — Sindre Sorhus](https://sindresorhus.com/velja)

#### Articles

- [The Integral of Happiness – Rainbow Line](https://1q43.blog/post/5322)
- [Why I Love Road Trips | Douban Pea](https://blog.douchi.space/road-trip/)
- [Software Has Eaten The Media](https://www.wheresyoured.at/the-anti-economy/)
- [Risk-free 360% Annual Return? Crypto Arbitrage for Beginners - TARESKY](https://taresky.com/crypto-arbitrage)
- [How NAT traversal works](https://tailscale.com/blog/how-nat-traversal-works)
- [The Collapse and Rebirth of a Six-Year-Old Open Source Project - DIYgod](https://diygod.cc/6-year-of-rsshub)
- [Build an Efficient Daily Quest System with Notion Calendar | Douban Pea](https://blog.douchi.space/notion-calendar-daily-quest/#gsc.tab=0)
- [Run Home Assistant on macOS with a Debian 12 Virtual Machine – Siytek](https://siytek.com/home-assistant-macos-utm-debian-12/)
- [Accelerate and Secure Your Website with Cloudflare Argo Tunnel (cloudflared) | Nova Kwok's Awesome Blog](https://nova.moe/accelerate-and-secure-with-cloudflared/)

#### Videos

- [I've Got It, The Best Way to Change Your Luck is to Get Married!](https://www.bilibili.com/video/BV1cF4m157Cy)
- [study vlog #48 | A New Start at 26 | Programmer's Evening Study Routine | Some Small Gifts Hope You Like](https://www.bilibili.com/video/BV1Lj421Z7Vz)

#### Movies

- [**Monster**](http://movie.douban.com/subject/35797709/), indeed fits the theme Hirokazu Kore-eda wanted to describe, but perhaps with too many metaphors added, it didn't quite convey as intended, also felt a disconnect in the plot and emotional rhythm.
- [**The Pig, the Snake and the Pigeon**](http://movie.douban.com/subject/36151692/), Taiwan certainly has a unique flavor in crime films, the theme and visuals are indeed daring, but it's more of a visually satisfying film, the presentation and changes in character personalities feel somewhat rushed.
- [**Westworld**](http://movie.douban.com/subject/35042913/), still prefer the park parts of the first two seasons, including William's transformation. The latter two seasons, perhaps due to wanting to show too grand a scale of consciousness awakening and self-choice, ended up feeling a bit like playing house.

#### TV Series

- [**Maiko in the Kitchen**](http://movie.douban.com/subject/35727023/), currently watching.

#### Music

- [**Photograph**](https://open.spotify.com/track/1HNkqx9Ahdgi1Ixy2xkKkL) by Ed Sheeran
- [**Mild Surface**](https://open.spotify.com/track/4EP4BmTjXvMGKzhBwKzWu5) by Zhao Dengkai
- [**Different Lives**](https://open.spotify.com/track/7e7JVMegy4WBMnzuZE9Srq) by Fly By Midnight
- [**After the Love Has Gone**](https://open.spotify.com/track/7e7JVMegy4WBMn