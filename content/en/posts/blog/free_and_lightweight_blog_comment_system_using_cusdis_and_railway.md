---
title: "Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)"
date: 2022-05-24T21:47:47+08:00
draft: false
tags: ["hugo", "cusdis", "railway", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here, After Us - Mayday》" >}}

## Preface

![cusdis_intro](https://image.pseudoyu.com/images/cusdis_intro.png)

Previously, I wrote an article titled "Free Personal Blog System Setup and Deployment Solution (Hugo + GitHub Pages + Cusdis)," detailing my blog system built using Serverless and some open-source projects. I also started a series to document the setup process.

This article focuses on the blog comment system solution. The earliest comment system I used was the ~~notorious~~ [Disqus](https://disqus.com), a cumbersome system known for collecting user privacy data. Due to its slow loading and frequent advertisements in the free version, it became unbearable. So, I switched to another comment system based on GitHub issues called [utterances](https://utteranc.es). It generates an issue for each article and allows users to comment on the issue by authorizing GitHub login. The advantage of this method is that it only requires authorizing a [utterances-bot](https://github.com/utterances-bot) for management, without the need for self-deployment of services or database maintenance. However, after using it for a while, I found several shortcomings:

1. It relies on the GitHub API for comment management. If there are future API changes or restrictions on using issues for comments, it may become unstable.
2. Readers must authorize GitHub login, which is inconvenient for non-technical users or those reading on mobile devices.
3. It clutters the GitHub repository and makes it difficult to migrate to other systems in the future.

After some research, [Randy's](https://lutaonan.com) [Cusdis](https://cusdis.com/) caught my attention. Cusdis is an open-source comment system that prioritizes data privacy and is extremely lightweight, with a gzipped size of only about 5kb. From its name, you can tell that the developer was also frustrated with Disqus and created an alternative version. Therefore, it also supports importing historical data from Disqus, which is very thoughtful.

Although this is an early-stage project, it already provides email notifications and comment alerts through Webhook integration with Telegram, making it convenient for users to manage. Cusdis offers both free hosted services and self-hosted options. If you don't want to bother with setup, you can directly use the service provided by the author. Self-hosting requires a server and a PostgreSQL instance. We will mainly demonstrate the self-hosted approach.

In my previous article "Building a Free Personal Blog Analytics System from Scratch (umami + Vercel + Heroku)," I used [Vercel](http://vercel.com/) and [Heroku](https://www.heroku.com/) for setup. As someone who enjoys tinkering, we'll use [Railway](https://railway.app/) to build and deploy this comment system.

Railway is similar to Vercel, also a PaaS platform that supports deployment of projects in multiple languages. For personal projects, its $5 monthly free quota is more than enough. After testing, deploying the previous [umami website analytics system](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/) along with a PostgreSQL database instance on the Railway platform costs about $0.7 per month, which is completely sufficient for personal use.

![railway_price](https://image.pseudoyu.com/images/railway_price.png)

Compared to Vercel, it also supports deploying database instances, allowing you to deploy the database and instance together in a single project, reducing setup and maintenance costs. The following will record the specific setup and deployment process, which is very smooth due to official support for one-click deployment on Railway.

**[2024-06-30 Update]**

Given that Railway has discontinued its Free Plan since August last year, if you still want to use it completely free of charge, you can use Vercel/Netlify/Zeabur to deploy the main project for free, and deploy a free PostgreSQL database instance on Supabase, passing the connection as an environment variable to the Cusdis service. The rest of the process remains largely the same.

## Setup and Deployment Instructions

### One-Click Deployment of Service and Database Instance Using Railway

First, register for a Railway account. You can use my [invitation link](https://railway.app?referralCode=J0F5LQ). After registration and login, click on New Project in the upper right corner to create a project.

![railway_dashboard](https://image.pseudoyu.com/images/railway_dashboard.png)

Then search for Cusdis and click on the appearing project to start deployment. The first few steps can also be done by clicking the `Deploy on Railway` button in the [Cusdis project repository](https://github.com/djyde/cusdis) for one-click deployment.

![new_cusids_starter](https://image.pseudoyu.com/images/new_cusids_starter.png)

Before starting deployment, you need to manually enter three environment variables:

![deploy_cusdis_on_railway](https://image.pseudoyu.com/images/deploy_cusdis_on_railway.png)

1. USERNAME: Account for login
2. PASSWORD: Password for login
3. JWT_SECRET: A random string

Other environment variables have been preset with default values, please do not modify them:

1. NEXTAUTH_URL: `${{ RAILWAY_STATIC_URL }}`
2. DB_TYPE: `pgsql`
3. DB_URL: `${{ DATABASE_URL }}`
4. PORT: `3000`

Click deploy and wait for completion. It will automatically deploy the service and initialize the database.

![cusdis_deploy_done](https://image.pseudoyu.com/images/cusdis_deploy_done.jpg)

### Configuring Cusdis Script for Personal Blog

After deployment, click on the link generated by the cusdis service to access the service Dashboard.

![cusdis_login](https://image.pseudoyu.com/images/cusdis_login.png)

Enter the username and password configured before deployment and click login. After logging in, click Dashboard to enter the project configuration page.

On first login, a pop-up will prompt you to configure the first website. Enter the website name to complete the addition. In the future, when we need to add a website, click New Website in the sidebar and fill in the website name to complete the addition.

![add_new_website](https://image.pseudoyu.com/images/add_new_website.png)

Since I have already configured my own website, the interface will show previous comment records.

![cusdis_dashboard](https://image.pseudoyu.com/images/cusdis_dashboard.png)

Next, click on Embed Code at the top and copy the code in the pop-up window.

![cusdis_embed_code](https://image.pseudoyu.com/images/cusdis_embed_code.jpg)

This part of the code needs to be modified partially according to the type of blog website you use. Refer to the Integration module in the [official documentation](https://cusdis.com/doc#/) for specific configuration.

I use [Hugo](https://gohugo.io), and the configuration is as follows:

```html
<div id="cusdis_thread"
  data-host="xxx"
  data-app-id="xxx"
  data-page-id="{{ .File.UniqueID }}"
  data-page-url="{{ .Permalink }}"
  data-page-title="{{ .Title }}"
>
</div>

<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>
<script async defer src="xxx"></script>
```

The `data-host`, `data-app-id`, etc., need to be based on the content of the Embed Code just copied. The `<script defer src="https://cusdis.com/js/widget/lang/zh-cn.js"></script>` mainly implements Chinese localization. For support of different languages, see the [documentation i18n module](https://cusdis.com/doc#/advanced/i18n).

After modification, add it to the appropriate position of your blog (usually at the bottom). After configuration and deployment, you can see the comment box. The presentation effect is as follows:

![cusdis_display](https://image.pseudoyu.com/images/cusdis_display.png)

### Configuring Custom Domain

The domain automatically generated by Railway deployment is quite long and contains some characters, making it difficult to remember. We can configure a custom domain for the project in Railway.

![railway_custom_domain](https://image.pseudoyu.com/images/railway_custom_domain.jpg)

After entering the desired domain/subdomain, add DNS resolution according to the official instructions.

![railway_domain_dns](https://image.pseudoyu.com/images/railway_domain_dns.jpg)

For example, I use a domain hosted by [Cloudflare](https://www.cloudflare.com), so I need to add a CNAME DNS record for the domain first.

![cloudflare_domain_dns](https://image.pseudoyu.com/images/cloudflare_domain_dns.jpg)

At this point, our deployment is complete, and we can access the management backend through the domain to perform comment review and management.

### Updating the Project

As mentioned earlier, Cusdis is still a developing project, and we want to update the new features released by the author as soon as possible. Railway provides a very convenient upstream branch management function, allowing you to set the parent project for the project and click to pull the latest updates, which is very convenient.

![railway_update_project](https://image.pseudoyu.com/images/railway_update_project.png)

## Conclusion

The above is the complete process of adding the Cusdis comment system to our website. After configuration, no subsequent maintenance is required. You can conveniently manage your website and review comments through the dashboard. The data is stored in a PostgreSQL database instance, making it easy to export, backup, and migrate. This is one of my blog setup and deployment series tutorials. Please stay tuned, and I hope it can be of reference to everyone.

## References

> 1. [Cusdis Project Official Website](https://cusdis.com)
> 2. [Railway Official Website](https://railway.app)
> 3. [Deploy umami to collect personal website statistics](https://reorx.com/blog/deploy-umami-for-personal-website/)