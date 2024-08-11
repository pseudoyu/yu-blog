---
title: "Free Personal Blog System Setup and Deployment Solution (Hugo + Cloudflare Pages + Cusdis)"
date: 2022-03-24T01:19:28+08:00
draft: false
tags: ["hugo", "github", "github action", "cusdis", "vercel", "cloudflare", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

[Pseudoyu](https://www.pseudoyu.com) is my personal blog website. Initially built using [WordPress](https://wordpress.com/) on my Vultr VPS, it was later migrated to a Tencent Cloud server and registered for improved access speed. However, the publishing process remained cumbersome, and server maintenance incurred significant long-term expenses.

Thus, I continuously explored solutions that could ensure optimal access experience both domestically and internationally while being hosted on platforms that streamline deployment and publishing processes. I've been constantly refining my blog system setup and publishing workflow. To date, I'm quite satisfied with my comprehensive solution. Although initial deployment and setup require some configuration, subsequent updates and maintenance are quite convenient. Therefore, this article will provide a complete record of this free, open-source personal blog system setup and deployment solution, hoping it proves helpful to others.

**[2024-06-30 Update]**

Two years have passed, and many solutions in this article are now outdated (though still usable). I've updated a series of new articles detailing my latest blog solution as of June 2024, which may serve as a reference for you.

- [What Changed in My Blog in 2024](https://www.pseudoyu.com/en/2024/06/29/what_changed_in_my_blog_2024/)

## Solution

### Blog Platform

There are already many mature blog platforms available, such as the aforementioned WordPress. While powerful, it's somewhat heavy for personal blog sites and ~~not cool enough~~. After extensive research, I ultimately chose [Hugo](https://gohugo.io), a static website generator.

Hugo is a blogging tool implemented in Go. It uses Markdown for article editing, automatically generates static site files, supports rich theme configurations, and allows plugin embeddings like comment systems through JavaScript, offering high customization. Besides Hugo, there are options like Gatsby, Jekyll, Hexo, Ghost, etc. Their implementations and usage are quite similar, so you can choose based on your preferences.

![yu_blog_homepage_20240629](https://image.pseudoyu.com/images/yu_blog_homepage_20240629.png)

Because the [hugo-theme-den](https://github.com/shaform/hugo-theme-den) in Hugo's open-source community perfectly matched my aesthetic, I chose Hugo and made some personal customizations and configurations based on this theme to meet my needs.

### Blog Hosting

Static blogs need to be hosted on a platform for external access. This could be your own VPS, or serverless platforms like [Cloudflare Pages](https://pages.cloudflare.com/), [GitHub Pages](https://pages.github.com), or [Vercel](http://vercel.com), the latter two of which can be associated with GitHub repositories.

I chose GitHub Pages. It's completely free and seamlessly integrates with GitHub code repositories, meeting my needs for blog source file backup and version control. It also allows for various CI/CD functionalities through the powerful and equally free [GitHub Actions](https://github.com/features/actions), such as automatically building and generating blog static files and pushing them to the GitHub Pages repository for deployment after submitting/updating blog source files. It can also be combined with scheduled tasks to update self-introduction pages and other features.

**[2024-06-30 Update]**

As my domain is already hosted on Cloudflare, I tried Cloudflare Pages, a static website hosting service launched by Cloudflare. It's completely free (at least I haven't exceeded the free quota yet) and can directly connect to GitHub code repositories. It provides mainstream website building tools like Next.js, Astro, Hugo, etc., enabling automated deployment functions like GitHub Pages and offering better access routes. It's currently a better solution.

### Blog Domain

We can configure our own domain through domain name resolution, such as my website which resolves to [pseudoyu.com](https://www.pseudoyu.com).

~~My domain was purchased on [NameSilo](https://www.namesilo.com) and accelerated via CDN on the [Cloudflare](https://www.cloudflare.com) platform, improving access experience and implementing domain redirection and other features. I'll elaborate on blog access optimization separately later.~~

**[2022-05-29 Update]**

For easier management, I later migrated my NameSilo domain to Cloudflare. You can directly purchase on Cloudflare. The tutorial is included in "[Deploy Your Blog Using Hugo and GitHub Action](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)".

### Visitor Analytics

As a continuously updated and operated blog platform, we're naturally curious about which articles have the highest readership, which keywords are most frequently searched, etc., helping us focus on creating and sharing more valuable content. There are many similar tools available. I chose [splitbee](https://splitbee.io) and [Google Search Console](https://search.google.com/search-console) to analyze my visitor information and search weight. Additionally, [Cloudflare](https://www.cloudflare.com) can also analyze network traffic, although it's less relevant than the former two due to much unrelated network traffic like crawlers.

![splitbee_statistics](https://image.pseudoyu.com/images/splitbee_statistics.png)

![google_console_performance](https://image.pseudoyu.com/images/google_console_performance.png)

![cloudflare_statistics](https://image.pseudoyu.com/images/cloudflare_statistics.png)

**[2022-05-21 Update]**

In addition to the above direct service platforms, I also deployed an open-source service [umami](https://umami.is) as an alternative to [Google Analytics](https://analytics.google.com), achieving real-time monitoring of visitor data. The tutorial is: "[Build a Free Personal Blog Data Analysis System from Scratch (umami + Vercel + Heroku)](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)".

**[2024-06-30 Update]**

Later, I switched to self-hosting "[goatcounter](https://www.goatcounter.com/)", a new data analytics service.

### Comment System

A blog system naturally needs a comment system. While platforms like WordPress have built-in comment plugins, static blogs need to integrate with some comment systems. I initially chose the third-party [Disqus](https://disqus.com), which is simple to use but comes with many advertisements and isn't minimalist enough. Later, I chose [Randy](https://lutaonan.com)'s [Cusdis](https://cusdis.com), a lightweight open-source comment system solution (the name itself seems inspired by the frustration with Disqus). I self-hosted it through Vercel and linked it to [Heroku](https://www.heroku.com)'s free [PostgreSQL](https://www.postgresql.org) database for comment data storage, achieving a free, stable comment system that also supports email notifications and Telegram Bot alerts/quick replies.

![cusdis_overview](https://image.pseudoyu.com/images/cusdis_overview.png)

**[2022-05-24 Update]**

The tutorial for deploying Cusdis on the Railway platform has been updated: "[Free and Lightweight Blog Comment System Solution (Cusdis + Railway)](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)".

**[2024-06-30 Update]**

Later, I switched to self-hosting "[Remark42](https://remark42.com/)", a new comment system.

### Image Management

Articles published daily may involve many images. Storing images in the static blog source project repository would make the project too large and difficult to reuse and manage. Therefore, I also chose GitHub as an image hosting tool and used the [PicGo](https://molunerfinn.com/PicGo/) client for image bed management. Before uploading, I use [TinyPNG](https://tinypng.com) for compression and [jsDelivr](https://www.jsdelivr.com) service to accelerate the GitHub image bed. This way, all images can be stored in the GitHub image bed repository and embedded in articles as external links.

**[2024-06-30 Update]**

Later, I used a set of image bed solutions: Cloudflare R2 + WebP Cloud proxy optimization + PicGo.

## Publishing Process

Typically, publishing a blog on GitHub Pages requires generating static site file directories locally with the `hugo` command, `cd` to the `public` directory, and using commands like `git add`, `git commit`, `git push` to submit to the GitHub Pages repository, achieving blog publication. Because each update requires repeating these operations, and blog source Markdown files cannot be well backed up and version controlled.

Therefore, I established a blog source file repository and implemented an automated publishing process through GitHub Actions. You only need to upload the Hugo blog source files to the GitHub repository, which will automatically trigger CI to generate static site files and push them to the GitHub Pages repository.

**[2022-05-29 Update]**

The tutorial for Hugo setup and GitHub Action configuration has been updated: "[Deploy Your Blog Using Hugo and GitHub Action](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)".

**[2024-06-30 Update]**

Added Cloudflare Pages deployment solution: "[Deploy Your Blog Using Hugo and GitHub Action](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)".

Publishing Process

## Conclusion

The above is my personal blog solution. The initial setup is somewhat cumbersome, but after some tinkering, it perfectly meets my needs. Regarding the detailed steps of the entire process, ~~I will explain in multiple articles, please stay tuned~~, hoping it can be helpful to everyone.

**[2022-06-02 Update]**

The core parts of the tutorial series have been completed:

- [Build a Free Personal Blog Data Analysis System from Scratch (umami + Vercel + Heroku)](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
- [Free and Lightweight Blog Comment System Solution (Cusdis + Railway)](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)
- [Deploy Your Blog Using Hugo and GitHub Action](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)

Additionally, if you don't want to use static blogs like Hugo, you can also set up a blog quite easily using Ghost:

- [Ghost 5.0 Is Here, Deploy It on Digital Ocean with One Click](https://www.pseudoyu.com/en/2022/05/29/deploy_ghost_5_on_digital_ocean_vps/)

## References

> 1. [Hugo Official Website](https://gohugo.io)
> 2. [hugo-theme-den Theme Repository](https://github.com/shaform/hugo-theme-den)
> 3. [GitHub Pages Official Website](https://pages.github.com)
> 4. [GitHub Action Official Website](https://github.com/features/actions)
> 5. [Vercel Official Website](http://vercel.com)
> 6. [Cusdis Official Website](https://cusdis.com)
> 7. [Heroku Official Website](https://www.heroku.com)
> 8. [PicGo Official Website](https://molunerfinn.com/PicGo/)
> 9. [splitbee Official Website](https://splitbee.io)
> 10. [Google Search Console Official Website](https://search.google.com/search-console)
> 11. [Cloudflare Official Website](https://www.cloudflare.com)
