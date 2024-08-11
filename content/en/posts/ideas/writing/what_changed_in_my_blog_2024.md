---
title: "In 2024, What Changes Have Come to My Blog"
date: 2024-06-29T13:48:58Z
draft: false
tags: ["hugo", "blog", "writing", "life", "remark42", "goatcounter", "webp cloud", "r2"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

## Preface

Two years ago, in the post ["It's 2022, Let's Talk About Why I'm Still Blogging"](https://www.pseudoyu.com/en/2022/06/12/why_i_still_write_blog_in_2022/), I discussed the origins, intentions, and setup of my blog.

More than two years have passed. The original intention remains, and the writing has persevered, though I haven't achieved the weekly updates I planned. Nevertheless, I've accumulated a fair amount of written work.

Having experienced much, I seem to have gradually transformed into a "weekly review blogger," with content and style that have greatly changed. There are fewer posts about technology and productivity tools, and more sharing of life and reflections. Gone are the days of staying up for two nights to update four technical tutorials; instead, there's a sense of self-reconciliation after expressing emotions through writing. I still feel happy receiving thanks for blog setup and technical tutorials, but I cherish even more the heartfelt exchanges with strangers.

## Weekly Review Blogger

Perhaps it was during a casual meeting discussion about xLog's future development when a colleague suddenly cued me, asking what thoughts I had as a "weekly review blogger." I was taken aback, hearing this title for the first time. Scrolling through my homepage, indeed, it fit.

I used to consider myself a tech blogger, a productivity tool blogger, but in the end, the content that remained the most, leaving the deepest impression on everyone, seems to be the weekly reviews. Not bad.

![weekly_review_group_chat](https://image.pseudoyu.com/images/weekly_review_group_chat.png)

The start of writing weekly reviews seems to have been when "Homura" organized a weekly review supervision group. At that time, I was still a nobody in both Twitter and independent blogging circles, hoping for more group support and communication. I would throw my weekly review into the group, sometimes feeling motivated by others, sometimes concerned about others' life states. It was a happy time.

Later, everyone experienced many changes in life and work. The last message in the group stayed at January 2023, but that remains a very happy period for me. It's also the motivation for me to continue writing weekly reviews because I know that even if I'm only sharing the trivialities of life and some immature little ideas, there are still people reading my words carefully.

![weekly_view_discuss_with_randy](https://image.pseudoyu.com/images/weekly_view_discuss_with_randy.png)

Previously, I received an update reminder from Randy. He said there's no need to define it as a weekly review, as it often brings pressure and constraints. However, I rely on this output-driven input mode. With the weekly review as a result-oriented goal, I have more motivation to live the week well.

~~Although I often redefine what a week is.~~

## Independent Blogging

Compared to beautifully arranged books and magazines, I enjoy visiting others' blog websites more. The site name, theme color, music arrangement all more authentically present a personalized existence. When reading blog posts, I often view it as a dialogue across time and space, imagining the author's mood when writing these word fragments. Sometimes I even playfully imagine what kind of person they are and what they might be doing at this moment.

Independent blogging is actually a circle that's neither big nor small. Two years have passed, and I feel that more people are starting to set up blogs and write blogs, and there's more interesting, high-quality content.

Compared to other mature content platforms that are more convenient for accumulating fans and interaction, it's not just independence in terms of platform and writing form (I'm actually willing to call those who share content seriously on Mastodon or Misskey independent bloggers), but independence of thought. Good articles not only impart knowledge but also provoke thought.

![dubo_1_intro](https://image.pseudoyu.com/images/dubo_1_intro.png)

I also chatted with Randy about wanting to do something for independent blogging, like compiling good articles read during a period of time in the form of a periodical and writing a preface to recommend them. Actually, the first issue has been prepared, but due to the busy schedules of both of us and a more focused effort on the EpubKit product, it hasn't been released yet. This is also something I hope to continue doing at some point in the future.

## Blog System

These are a few articles I wrote about blog setup two years ago:

- [It's 2022, Let's Talk About Why I'm Still Blogging](https://www.pseudoyu.com/en/2022/06/12/why_i_still_write_blog_in_2022/)
- [Free Personal Blog System Setup and Deployment Solution (Hugo + GitHub Pages + Cusdis)](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)
- [Hugo + GitHub Action, Build Your Blog Automatic Publishing System](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)
- [Build a Free Personal Blog Data Analysis System from Scratch (umami + Vercel + Heroku)](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
- [Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)

These mainly revolved around my records of using Hugo, a static website generator (SSG), to build a personal blog and some peripheral services. I've also seen many people contact me saying they successfully have their own blogs following this series of tutorials. I'm very happy to make a small contribution to blogging, a form of creation that has somewhat declined.

I was very satisfied with my entire set of solutions when I wrote them, but looking back after two years.

- **Blog Body**: Hugo itself hasn't changed, deployment solution: GitHub Pages + Cloudflare CDN -> Cloudflare Pages
- **Comment System**: Cusdis -> Remark42, deployment platform: Railway -> Vercel + Supabase -> fly.io
- **Statistics System**: Umami -> goatcounter, deployment platform: Vercel + Heroku -> Railway -> Netlify + Supabase -> fly.io
- **Image Hosting System**: GitHub + jsDelivr -> Alibaba Cloud OSS -> Self-hosted Chevereto on VPS + PicGo -> Cloudflare R2 + WebP Cloud + PicGo
- **Content Search**: None -> Pagefind static search

There are many reasons for the changes. Some are due to Heroku and Railway gradually canceling their free plans, some are due to open-source projects updating less and lacking features, and some are simply because I wanted to tinker around to make things lighter.

I remember when I wrote this series of tutorials, it was mainly because I felt that the solutions and tutorials that could be found online were scattered and often outdated. So I wanted to provide a one-stop solution for readers who wanted to set up a blog. After publication, I received feedback from many people. Some content should have been updated long ago, but I've been putting it off until now to start rewriting, which I feel quite ashamed about.

The following text will introduce the current solution, and links to the updated series of articles will be added later when completed.

### Blog Body

![yu_blog_homepage_20240629](https://image.pseudoyu.com/images/yu_blog_homepage_20240629.png)

I use [Hugo](https://gohugo.io/), this static website generator, to build my personal blog, using and modifying a rather retro theme "hugo-theme-den".

The general process can be referred to in the article ["Hugo + GitHub Action, Build Your Blog Automatic Publishing System"](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/) and the repository ["GitHub - yu-blog"](https://github.com/pseudoyu/yu-blog).

I added some GitHub Actions automated operations to update the About page daily, and because websites hosted on GitHub Pages became almost inaccessible from within China, I migrated to Cloudflare Pages, which is free and provides a much better experience. There haven't been many other changes.

It's not that I haven't thought about changing frameworks. I was quite envious when I saw "Owen" and "PJ Wu" using [Zola](https://www.getzola.org/), and I even thought about writing one myself like "Goidea" or "Innei".

But when I calmed down and thought about it, I've accumulated quite a few articles on my current website, and if I wanted to keep the original paths, it would inevitably involve a lot of tinkering. Plus, I really like the current theme, so I might as well just customize and modify the theme directly if I have any ideas. It's better to spend less effort on tinkering with platforms and write more blog posts, otherwise it might be a bit like valuing the casket over the jewels, so I gave up on the idea.

### Comment System

From the inception of the blog until April or May this year, I had been using [Cusdis](https://cusdis.com/) consistently for three years.

To this day, it's still a highly recommendable solution - lightweight, easy to self-deploy, and with a simple and attractive style. For setup instructions, refer to ["Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)"](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/).

However, given that Railway has canceled its Free Plan since August last year, if you still want to use it completely free, you can use Vercel/Netlify/Zeabur to deploy the main project for free, and deploy a free PostgreSQL database instance on [Supabase](https://supabase.com), passing the link as an environment variable into the Cusdis service. The rest of the process is largely similar.

![yu_remark42_preview](https://image.pseudoyu.com/images/yu_remark42_preview.png)

Recently, due to a persistent Vercel deployment error when changing the database URI, plus the need for some new features, I finally decided to migrate from Cusdis. After researching for a while, I chose [Remark42](https://remark42.com/), which was ultimately selected by [reorx](https://reorx.com/) in his article ["Changing Blog Comment Systems"](https://reorx.com/blog/blog-commenting-systems/).

In terms of configuration options alone, it's quite a bit richer than Cusdis. Currently, I've configured several common social account logins (GitHub, Twitter, Telegram, email), anonymous commenting is supported, email subscription for reply notifications is available, and I've also set up TG bot notifications. It's deployed on [fly.io](https://fly.io/), with a single Go binary + single file database, a very comfortable solution. I'll update the tutorial link here once the blog post is completed.

**[2024-07-22 Update]**

For details on setting up the comment system, see this post:

- [Build Your Free Blog Comment System from Scratch (Remark42 + fly.io)](https://www.pseudoyu.com/en/2024/07/22/free_commenting_system_using_remark42_and_flyio/)

### Data Statistics System

I previously self-deployed Umami (refer to the tutorial ["Build a Free Personal Blog Data Analysis System from Scratch (umami + Vercel + Heroku)"](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)), but later, due to Heroku canceling its free Plan, I tinkered around and chose to deploy the service on Netlify + deploy a PostgreSQL database instance on Supabase. The rest of the process remains applicable.

![yu_goatcounter_preview](https://image.pseudoyu.com/images/yu_goatcounter_preview.png)

However, on one hand, because I deployed it quite early, there was a major version that couldn't be upgraded, causing me to stay on an old version I forked. On the other hand, I gradually felt that this kind of service and database separation inevitably led to frequent migrations due to platform rule changes, which felt a bit too heavy. So finally, I switched to [goatcounter](https://www.goatcounter.com/), which is also deployed on [fly.io](https://fly.io/) with a single Go binary + SQLite database file, another very comfortable deployment solution. I'll update the tutorial link here once the blog post is updated.

![yu_google_console_preview](https://image.pseudoyu.com/images/yu_google_console_preview.png)

Additionally, I still use [Google Console](https://search.google.com/search-console) to analyze and statistics my visitor information and search weight.

These results are quite informative. I found that an article comparing terminals ["Warp, iTerm2, or Alacritty? My Terminal Tinkering Notes"](https://www.pseudoyu.com/en/2022/07/10/my_config_and_beautify_solution_of_macos_terminal/) continuously brings me visitors through search engines. The other popular articles are the series about personal blogs and setup.

**[2024-08-06 Update]**

For details on setting up the website data statistics system, see this post:

- [Setting Up a Website Statistics System Using GoatCounter and Zeabur](https://www.pseudoyu.com/en/2024/08/06/deploy_web_statistics_system_using_goatcounter_and_zeabur/)

### Image Hosting System

Two years ago, I hadn't really paid much attention to the issue of image hosting. All images were directly thrown into the GitHub repository and used jsDelivr as a CDN for acceleration (which later became almost inaccessible from within China). However, as the number of articles increased, friends often told me that they couldn't load the images on my blog. Thinking about improving the reading experience, I researched various solutions.

![aliyunoss_invoice](https://image.pseudoyu.com/images/aliyunoss_invoice.jpeg)

I first chose Alibaba Cloud OSS for image storage, using PicGo for uploading on the computer. The solution was quite good, and there were no problems for the first few months, until early 2023 when a few articles had relatively high traffic. Seeing the upward trend of the monthly bill, I suddenly felt poor.

So I set up a Chevereto image hosting on a Bandwagon server with good connectivity, still using PicGo's plugin for uploading. It was used steadily for a year and a half. But I was a bit careless about the stability of self-hosted services and the preciousness of data. A few days ago, the server suddenly went down, with a kernel error that prevented rebooting. The service being down was one thing, but I had no backup of my year and a half of data and couldn't export it.

I contacted technical support through a work order, but they only replied twice in a day, once telling me to restart, and once suggesting I hire a network administrator to investigate. I could only rely on myself. After scouring the internet for various solutions and tinkering for a day, I finally managed to solve it. But this lesson gave me a whole new understanding of the importance of services with critical data and the stability of self-hosting, so I dared not use the original solution anymore.

![yu_webp](https://image.pseudoyu.com/images/yu_webp.png)

Finally, I adopted [Cloudflare R2](https://www.cloudflare.com/en-gb/developer-platform/r2/) object storage to store images. The 10GB free quota per month is more than enough, and the service and data security of a big company are also guaranteed. To optimize user access, I also used a "WebP Cloud" service to proxy the images in R2, further reducing image size at the proxy level. Although the speed for domestic users is certainly not comparable to Alibaba Cloud OSS in terms of connectivity, under the comprehensive conditions of not requiring filing, stability, and being free, this is the best solution I could think of.

![yu_picgo_pics](https://image.pseudoyu.com/images/yu_picgo_pics.png)

On the desktop, I can almost one-click upload through the PicGo client and generate markdown image links directly usable for the blog. After configuration, it's very smooth to use.

For the image hosting setup tutorial, see this post:

- [Build Your Free Image Hosting System from Scratch (Cloudflare R2 + WebP Cloud + PicGo)](https://www.pseudoyu.com/en/2024/06/30/free_image_hosting_system_using_r2_webp_cloud_and_picgo/)

**[2024-07-02 Update]**

I've written a new tutorial on implementing privacy and copyright protection for image hosting, which can be considered a bonus chapter.

- [Adding Privacy and Copyright Protection to Your Image Hosting Using WebP and Cloudflare WAF](https://www.pseudoyu.com/en/2024/07/02/protect_your_image_using_webp_and_cloudflare_waf/)

### Content Search

![search_in_my_blog](https://image.pseudoyu.com/images/search_in_my_blog.png)

Previously, my blog didn't have a content search function. Initially, there weren't many articles, and since it's a static blog without a backend, it seemed difficult to implement. So I never supported it. But as I sometimes needed to refer to my previous articles and could only search through a bunch of markdown files using VS Code, I felt it was quite necessary.

After researching, I used [Pagefind](https://pagefind.app/), a search library based on static files. It doesn't require introducing or hosting other backend services. I only need to build an index file for the entire blog in the CI every time I publish a blog post, and it can easily support searching. The Chinese search effect is relatively weak, but it's sufficient. It basically supports most mainstream blog frameworks.

This part can be referenced from the article ["How to Add a Search Function to Zola-Generated Static Websites via Pagefind"](https://pinchlime.com/blog/how-to-add-a-search-function-to-zola-generated-static-websites-via-pagefind/).

## Conclusion

In 2024, I'm still largely a person who loves writing, from book and movie reviews, technical tutorials in earlier years to current life weekly reviews. It seems that what I see and think only becomes tangible reality when put into words. And with the accumulation of hundreds of articles, my personal blog site has become another carrier of me in this world, originating from me yet independent of me. Sometimes it's a memory fragment that can be picked up at will, sometimes it's a spiritual sanctuary for myself.

I also hope that you can continue to discover some interesting things in my blog, be it knowledge, inspiration, or a little bit of resonance. Perhaps at some moment, you too will want to have your own blog site, to leave some traces of your thoughts in this world, to take root and sprout. I hope this series of tutorials can provide some help.