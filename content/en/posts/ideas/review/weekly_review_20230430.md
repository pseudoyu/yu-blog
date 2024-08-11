---
title: "Weekly Review #38 - Foundry Contract Testing, Logseq Task Management, and Surge Ponte Remote Development"
date: 2023-04-30T00:10:03+08:00
draft: false
tags: ["review", "life", "work", "foundry", "solidity", "web3", "pkm", "surge", "surge ponte", "logseq"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

This piece is a record and reflection of my life from `2023-04-19` to `2023-04-30`.

In my previous weekly review, I mentioned a journey across multiple cities. After returning to Hangzhou, I gradually resumed my original life rhythm. I had much more time alone, with plenty of input, reflection, and interesting things to do. However, it seems that I had less time to organize and dialogue with myself, often only realizing the passage of time several days later. I consider myself someone who doesn't rely much on socializing and has strong adaptability, but upon reflection, I might have entrusted my life state too much to the virtual world, feeling an almost disconnected discomfort from reality.

Now I'm on a late-night flight, having taken a short nap, my drowsiness gradually fading. So I decided to take out my laptop and write something. Perhaps due to the lack of internet and external distractions, my thoughts seem clearer.

## Work Atmosphere and Freedom

It's been over a month since I joined the new team. Perhaps because I was constantly on the move for the first two to three weeks, I often didn't have much sense of reality. Now I'm gradually adapting to the rhythm and getting on track. The atmosphere in my group is very good; even when working remotely, I don't feel a sense of alienation. A meeting often goes from work matters to what to eat for takeout and then to what Vlog camera to buy (Sony is the way to go). Even I, usually socially anxious, have gradually become more talkative in the group chat.

Interestingly, due to intensive participation in the Shenzhen team building, Hong Kong Web3 Festival, and a wave of team building in Hangzhou, I've already met nearly 20 colleagues from the company, which is quite remarkable for a fully remote team. I was also lucky to catch the online annual meeting, meeting many interesting colleagues who only existed in Slack dialog boxes before (all kinds of talents). A performance could uncover a rapper, and even playing Tetris could make one feel the differences between people.

After some communication, I made some adjustments to my work content. I can continue to do some smart contract development and chain-related research and exploration simultaneously, and also more deeply participate in the products I like (see who's not using [xLog](https://xlog.app/) and [xSync](https://xsync.app/) yet, specifically you can look at this article "Weekly Review #25 - Personal Information Output and Synchronization System Based on Crossbell"). Although it might require more balance in terms of workload and time, I'm still a bit happy to have this degree of freedom of choice.

## Foundry and Contract Testing

As I started to understand the projects of another group I joined for work, I quite obviously felt that although I had done some chain development and written contracts for half a year before, there was still quite a gap in complexity and development practices. I plan to supplement this area well, so this week I looked at a lot of contracts and research documents, planning to switch from Hardhat to Foundry.

Actually, [Noy](https://twitter.com/Noy_eth) and some other friends had already frantically recommended the Foundry framework to me before, but because the previous project didn't have such high requirements for contract unit testing, and I had relied on writing many tool scripts in js, I had been using Hardhat all along. It wasn't until I really ran some projects and wrote some demo unit tests this time that I felt its huge advantages and instantly defected. The almost dusty Solidity contract development series is finally going to welcome a new update (~~I'm writing it, look at the picture if you don't believe me~~

![foundry_framework_outline](https://image.pseudoyu.com/images/foundry_framework_outline.png)

Actually, there are still very few enterprise-level practices for contracts at present. Also, because some of the contracts I will be doing later are open source, I plan to gradually record some experiences of pitfalls and best practices (the advantage of being full-time open source).

## Logseq and Task Management

As my personal arrangements and work tasks have become more numerous and complex, I have reactivated Logseq as my personal task management tool. I had actually been using Notion as my personal kanban board before, but always felt that the mental burden was too heavy when using it. My severe obsessive-compulsive disorder also constantly made me optimize those task categories and description information, which actually gave me a lot of pressure. I had also used more conventional applications like TickTick and Todoist, but similarly, I still needed to sort out various tasks and tags every day, and it wasn't very convenient to review.

I later discovered the note-taking software Logseq. At first, I actually just treated it as a markdown note-taking software with blocks as the granularity, and also wanted to try out the concept of bidirectional links that always seemed to be mentioned. I got quite used to it, so I gradually migrated my Knowledge Base from Notion over. Later I also tinkered with using SimpRead to synchronize my web page annotations and such, but after a while, I still felt it was a bit troublesome so I abandoned it.

Until I discovered this video by [Randy](https://twitter.com/randyloop), "How I Use Logseq to Manage My Life and Notes", he mentioned using Logseq's Daily Journal to make various notes and TODO management, so you don't need to form a plan first and then present it like with software such as Notion.

![logseq_daily_journal](https://image.pseudoyu.com/images/logseq_daily_journal.png)

Therefore, when you suddenly think of something you want to do, you don't need to create a new task separately in the kanban board or task management software, you just need to add an item in your Daily Journal like writing a note and use simple syntax like TODO, LATER to do simple task management.

However, some tasks span multiple days, and our tasks will be scattered under the Journal of various dates, which is not very conducive to unified management. This is where another powerful feature of Logseq comes in - Query. This feature can be understood as a query with blocks as granularity (just like sql querying a record), filtering through some tags, syntax, and other internal logic to display the blocks we want.

For this part, I referred to Randy's practice and created a Dashboard page that displays various query results. I mainly used the following Queries (the query statements are in parentheses, friends who need them can take them and modify them as needed):

1. In Progress (`{{query (todo now)}}`)
2. Todo (`{{query (todo later)}}`)
3. Writing Plan (`{{query (and (todo later) [[writing]] )}}`)
4. Reading (`{{query (and (todo now) [[books]] )}}`)
5. Read It Later (`{{query (and (todo later) [[books]])}}`)

The presentation results are as follows:

![logseq_dashboard_in_progress](https://image.pseudoyu.com/images/logseq_dashboard_in_progress.png)

![logseq_dashboard_todo](https://image.pseudoyu.com/images/logseq_dashboard_todo.png)

![logseq_dashboard_other_queries](https://image.pseudoyu.com/images/logseq_dashboard_other_queries.png)

Because this is Randy's practice, I won't write a separate blog post to introduce it. I briefly introduced my own usage in the weekly review, those interested can watch his original video.

## Surge Ponte and Remote Development

In terms of tinkering with networks, various hardware devices and systems, I belong to the category of being both unskilled and loving to play. I had explored some best practices for thin client development before, details can be seen in this article:

- [Thin Client Development Workflow Based on frp Intranet Penetration](https://www.pseudoyu.com/en/2022/07/05/access_your_local_devices_using_reverse_proxy_tool_frp/)

The most core and difficult point is how to access devices at home, such as servers, Mac hosts, etc., in an external network environment. In my previous solution, I used the frp tool for intranet penetration. Half a year has passed, it's very stable and is still the first recommended solution.

But when I saw this article "Surge Ponte Development Notes" posted by [Yachen Liu](https://twitter.com/Blankwonder), I was itching to tinker again.

I was going to be out for a few days during the May Day holiday, and thinking that my daily development is done on the host at home, I also wanted to be able to access it when I'm out. Just because I hadn't configured the frp client after reinstalling the system, I thought I might as well try Surge Ponte directly.

So I upgraded to Surge 5 and configured and tinkered with Surge Ponte the night before departure. After a bit of exploration, compared to frp or other similar solutions, I think Surge Ponte has absolute advantages in configuration ease of use and expansion gameplay.

The tinkering with Surge Ponte definitely deserves a detailed blog post, so I won't explain the principles and configuration details in this weekly review. I'll just briefly show the effects of some of the features I'm currently using.

When I turned on the Surge Ponte function on both my 16-inch MBP and the Mac Studio at home (I'm using the NAT traversal via proxy mode, which only needs a line that supports UDP, such as a self-built proxy with the Trojan protocol), I could see them in the registered devices.

![surge_ponte_config](https://image.pseudoyu.com/images/surge_ponte_config.png)

At this point, when the device has enabled permission for remote login, you can directly remotely log in to the host like accessing a cloud service using a command like `ssh [username]@[surgepontename].sgponte`, so it also supports VS Code remote development and such.

![surge_ponte_ssh](https://image.pseudoyu.com/images/surge_ponte_ssh.png)

Of course, this point can also be easily achieved by frp and others, but a more powerful point is that some services we start on the home host can also be directly accessed through a URL like `[surgepontename].sgponte:[port]`. For example, after I remotely connected to the Mac Studio at home via ssh and started a local Next.js web service, which is accessed via `localhost:3000` during local development, now I can directly access it on my MBP via `http://yu-macstudio.sgponte:3000` (although frp can also map services out, it requires writing port mapping rules on the frp client side).

![surge_ponte_servies](https://image.pseudoyu.com/images/surge_ponte_servies.png)

So theoretically, by directly remotely connecting to the host via VS Code to modify code files and using the `[surgepontename].sgponte:[port]` method, you can get a full version of the local debugging experience, taking into account both portability and performance (~~Alright, I'm selling my MBP for an Air~~

Another very practical scenario is that we often have some services that can only be accessed on the local network at home, such as soft router configuration, NAS, Raspberry Pi, etc. At this time, if using frp, each one needs to be configured separately, while Surge Ponte can directly achieve external access by setting DEVICE rules. For example, I can now directly use `http://router.asus.com` to access my home router configuration page from out of town, which is very convenient for remotely managing some resident services at home.

![surge_ponte_router](https://image.pseudoyu.com/images/surge_ponte_router.png)

There are many more interesting applications, such as directly accessing files on home host devices through the smb protocol, etc. The later blog posts will try to cover some interesting application scenarios, interested friends can follow (~~urge for updates~~) the blog posts.

## Nie Nie's Recent Situation

![nie_nie_in_painting](https://image.pseudoyu.com/images/nie_nie_in_painting.jpg)

Senior sister Bo Yi is painting an oil painting for Nie Nie!!! This is just a draft, more details will be added, but I can't help wanting to show it off, it's too beautiful!!!

![nie_nie_and_new_toys_01](https://image.pseudoyu.com/images/nie_nie_and_new_toys_01.jpg)

![nie_nie_and_new_toys_02](https://image.pseudoyu.com/images/nie_nie_and_new_toys_02.jpg)

New cat tree, starting vacation mode in advance!

Planning to take her for neutering after May Day, still a bit nervous, hope everything goes well.

## Interesting Things and Objects

### Input

Although most interesting inputs are automatically synchronized in the "Yu's Life" Telegram channel, I still select some to list here, feeling more like a newsletter.

#### Articles

- [Warp+ Traffic Matching with Surge](https://pepcn.com/surge/warp-liu-liang-da-pei-surge)
- [Application-Specific Blockchains: The Past, Present, and Future](https://medium.com/1kxnetwork/application-specific-blockchains-9a36511c832)
- [AI is Here, What Skills Are Most Worth Learning?](https://mp.weixin.qq.com/s/ifldCMLTSb1Ir-qcyoa5rw)

#### Videos

Similarly, I also record some interesting videos I've watched:

- [How to Launch Your First Open Source Project](https://www.bilibili.com/video/BV1os4y1w78T)
- [Got Scolded Again! Boyfriend's Disneyland Survival Guide](https://www.bilibili.com/video/BV1wm4y127dG)

#### Anime

- **Demon Slayer: Swordsmith Village Arc**, super excited!!! Hope it doesn't disappoint
- **Oshi no Ko**, seems to have quite high discussion, but reportedly a bit sad, watched a little bit of the beginning
