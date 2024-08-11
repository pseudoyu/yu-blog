---
title: "Weekly Review #02 - Work, Anxiety and Growth"
date: 2022-07-03T12:54:39+08:00
draft: false
tags: ["review", "life", "work", "responsibility", "growth"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

![raspberry_pi](https://image.pseudoyu.com/images/raspberry_pi.jpg)

It's been a full year since I started working in Beijing after my internship.

I've always been a person with an inexplicable sense of ritual. At this juncture, I frequently reflect on my thoughts, gains, anxieties, and regrets from this past year. I often wonder, on this day a year ago, what would that nervous yet expectant version of myself have hoped to gain from the year ahead?

So, in this piece, let's discuss work, anxiety, and growth.

## On Work

### Starting the Job

I wasn't particularly diligent in my job search, perhaps because even in Beijing, there weren't many blockchain companies to choose from. While quarantining in a hotel in Shenzhen after returning from Hong Kong, I only participated in about five or six interviews, though some left quite an impression.

One company had no conventional process. The first round involved sharing my screen with an American interviewer, spending two hours writing, testing, and deploying an ERC20 Token smart contract. The second round required writing a system-level scheduled task using a Shell script. Another company asked many questions about EVM low-level optimization and how to avoid infinite loops in contracts.

The company I ultimately chose had two technical leaders jointly conducting the interview. One asked questions related to Go language, while the other inquired about Hyperledger Fabric and Ethereum (I later learned he was a former developer from the IBM Fabric team). We also discussed many topics related to future development directions, lasting nearly an hour and a half, followed by a half-hour algorithm test.

I genuinely enjoy and cherish opportunities to gain new engineering knowledge from interviews or to communicate relatively equally with interviewers. It allows me to learn quickly or at least gain some clarity on directions.

After arriving in Beijing, I attended an HR interview and officially joined as an intern, thus beginning my first formal technical internship.

### Internship

Upon first encountering a technical position, the initial trepidation outweighed the novelty. I lacked confidence in transitioning from theoretical knowledge in school to practical enterprise engineering. I had only studied Go language for a few months to prepare for interviews and had never even participated in writing a production application.

As a newcomer to the CRUD realm, I started by writing business interfaces under the guidance of our leader, Brother Cheng, to familiarize myself with the work. We mainly developed a BaaS platform, writing seven interfaces over two weeks, repeatedly testing and optimizing complex SQL queries. I also fully experienced the git commit standards, code review, and code merging processes. It was quite an enjoyable process, seeing my code running in production projects and quickly applying various learned knowledge in work to get real-time feedback, as well as a team working together towards a common goal and milestone.

After completing the main development work for this project, I wanted to do some chain-related development. So I applied to participate in another group's project on optimizing the performance of a self-developed chain smart contract execution engine. However, unfamiliar with Java, I could only attempt to write some tests while studying and researching the theory. This was the blog post I recorded at the time, "Ethereum MPT (Merkle Patricia Tries) Explained in Detail". It was during this period that I realized how quickly those dry algorithm principles from LeetCode would actually be put to use.

Perhaps due to being an intern, the work pace wasn't very fast, leaving plenty of time to explore interesting fields or technologies. I wrote the following blog posts to record my learnings:

1. [Introduction and Architecture of Blockchain-as-a-Service (BaaS) Platform](https://www.pseudoyu.com/en/2021/09/07/blockchain_baas_platform/)
2. [Distributed Systems and Blockchain Consensus Mechanisms](https://www.pseudoyu.com/en/2021/09/08/blockchain_consensus/)
3. [Cross-Chain Technology Principles and Practice](https://www.pseudoyu.com/en/2021/09/06/blockchain_crosschain/)
4. [Source Code Analysis of BitXHub Cross-Chain Plugin (Fabric)](https://www.pseudoyu.com/en/2021/09/09/blockchain_crosschain_bitxhub/)

Interestingly, because the company didn't have an internal content publishing platform, I often submitted articles to our competitors' blockchain technology blog platforms during this period and received learning feedback from their core technical personnel. I benefited greatly in the cross-chain area, which also made me feel the openness of technology.

At this point, I hadn't decided whether to stay, and I had some contact with other desirable companies. However, soon after, I participated in another cross-chain project with another leader, Brother Tao. As I interacted with him more, I saw the enthusiasm and infinite possibilities of a technologist. We both loved tinkering with various novel tools and technologies, often sharing with each other. Knowing that I often felt anxious about lacking sufficient engineering experience and ability, he involved me in various project practices, sometimes even leading me in pair programming on weekends.

He is a core developer of [Hyperledger Cello](https://github.com/hyperledger/cello) and encouraged me to participate in open source. A sentence he said at the time still remains vivid in my memory. The gist was that as a technologist, besides completing one work task after another, one always needs to have several labels in their technical career, such as "core contributor to a certain open source project" and so on. I also need to continuously strive to find my own labels. This point deeply influenced me, and in subsequent work and study, I began to continuously pay attention to and slowly participate in the open source community.

An irreplaceable leader became a more significant factor influencing my choice, so without much hesitation, I stayed.

### Work

Soon after, I participated in what was strictly my first complete project, which also occupied most of my first year of work - a underlying cross-chain project.

Perhaps due to my previous after-hours study and understanding of cross-chain, I inexplicably became the project leader just as I transitioned from intern to probationary employee. I participated in technical solution discussions, early system design, underlying chain development and modification, development process standardization, use of DevOps environments, explanations and demonstrations, as well as project delivery-related documentation and communication work. This brought pressure and anxiety I had never anticipated at the start of my work, but it also brought about my rapid growth.

Daytime meetings could last half a day, leaving only evenings to concentrate on writing code. Staying up late or even all night became the norm to meet project milestones. Technical difficulties could stall progress for days, yet I had to juggle other development task schedules simultaneously. Accompanying this were many emotional suppressions and loss of control over life rhythms.

But when I truly completed the final delivery of this project with the team, that sense of joy and achievement was unprecedented. This might have special significance for me. From my undergraduate English major to studying abroad and switching to computer science, I often felt frustrated during many course studies and questioned more than once whether I could continue on this path. Although the process of this project was bumpy, we ultimately succeeded, which gave me tremendous confidence.

### Interactions

It's worth mentioning the mode of interaction between people after starting work. I seem to have never shed that student air about me, always communicating in a rather direct and candid manner whether facing leaders, colleagues, or project partners. When my life experienced some changes in May, team members took on more work responsibilities to allow me time to adjust. A client leader from a recently completed project would call me for three to four hours to comfort me. And a leader from another ongoing project was helping me apply for a business trip to ease my mood a bit. Work isn't actually as dull as those anxiety-inducing articles describe. I've always felt that regardless of the environment or occasion, relationships and interactions are mutual. Treating others sincerely can indeed equally gain some trust and sincerity in return.

### Gains, Challenges, and Changes

![dev_guide](https://image.pseudoyu.com/images/dev_guide.png)

A year has passed, and the second project is about to end. I've learned a lot from this year and wanted to leave something for the department in my own way, so I decided to write a technical guide. In addition to development specifications, it also includes some of my learning records about blockchain over the past few years, as well as some practical records learned from work. These are all things I had hoped to learn when I first entered this job, and I hope to tell new members about them.

![dev_guide_content](https://image.pseudoyu.com/images/dev_guide_content.png)

Although only a year has passed in my work, with much room for improvement and growth in technology and experience, I've become somewhat confused about direction. I want to delve into underlying blockchain technology, polish the company's or personal products, and participate more in open source construction. But work often leaves me exhausted by project delivery deadlines, making it difficult to have complete time for learning and research. This is a challenge I need to overcome and adjust in my future career.

Fortunately, another leader, Brother Kai, pays great attention to open source and underlying technology. Our occasional exchanges have pointed out some directions for me. There's still much to learn and improve upon; the road of technology is long, with great responsibility and a long way to go.

## Conclusion

The above is my summary of work at this point in time. I'm gradually enjoying organizing and recording my life, work, and state of mind in this way. I hope that when I look back on this year I'm experiencing in the next year, I'll see more changes and growth in myself. Let's encourage each other.