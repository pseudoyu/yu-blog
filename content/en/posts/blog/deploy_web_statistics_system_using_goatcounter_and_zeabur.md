---
title: "Setting up a Website Analytics System with GoatCounter and Zeabur"
date: 2024-08-06T19:00:42+08:00
draft: false
tags: ["statistic-system", "serverless", "zeabur", "blog", "goatcounter"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

In my article "[What Changed in My Blog in 2024](https://www.pseudoyu.com/en/2024/06/29/what_changed_in_my_blog_2024/)", I introduced the blog system I built using Serverless platforms and some open-source projects. I also started this series of tutorials to document the entire process of setup and deployment.

This article focuses on the analytics system solution.

## Analytics System Solution

Compared to the blog itself and the commenting system, I hadn't paid much attention to an analytics system for a long time (~~mainly because there weren't many readers back then~~). I hadn't considered much about SEO or other promotional aspects. However, I gradually discovered that the data collected is not just a pretty chart to post on Twitter; it has great reference value for blog topic selection and content.

In fact, mainstream mature solutions can meet basic needs. Even the free Google Analytics is more than enough. However, during the development of my blog, I still went through several iterations for various reasons, and finally settled on GoatCounter as my solution.

### splitbee

Initially, I used a free tool called splitbee. It provided free basic analytics quota, had a nice interface, and supported complex user tracking, A/B testing, etc. But as I recall, it only retained data for half a year, and required an upgrade after exceeding 5000 page views per month, so I abandoned it later.

### Cloudflare + Google Search Console

![cloudflare_web_stats](https://image.pseudoyu.com/images/cloudflare_web_stats.png)

After abandoning splitbee, for a long time, I didn't integrate any additional analytics applications. Instead, I used Cloudflare's built-in site statistics. However, I found that it only tracked total network traffic, including a lot of ineffective data such as crawlers, and lacked details down to the path level.

![google_search_console](https://image.pseudoyu.com/images/google_search_console.png)

Later, after learning about the concept of SEO, I added [Google Search Console](https://search.google.com/search-console/about) as another analytics dimension. This is currently the data I find most meaningful for my blog writing. It mainly presents the keywords users use to reach my blog site in search engines and the page paths they click through from search results to enter my blog.

As you can see, an article titled "[Warp, iTerm2, or Alacritty? My Terminal Tinkering Notes](https://www.pseudoyu.com/en/category/tools/)" brought me many visitors, while topics about blog setup and smart contract development are also the first impressions of my blog for most natural users coming from search engines.

### Umami + Supabase + Netlify

![yu_umami_record](https://image.pseudoyu.com/images/yu_umami_record.png)

However, the above two methods still only show overall website data. To precisely track the performance of a specific article over a period or real-time access data after an article is published, an analytics system is still needed. After reading Reorx's article "[Deploy umami to collect personal website statistics | Reorx's Forge](https://reorx.com/blog/deploy-umami-for-personal-website/)", I chose to use umami, an open-source, easily self-deployable analytics system. It has a clean interface, user-friendly features, and is easy to integrate into one's own blog system.

I used it for a year and a half without any problems. However, possibly because I started using it quite early, during a major version update, there was an incompatible field update in the database migration script. I found it a bit hard to understand why such a level of open-source project would have this kind of issue. I also saw many other users with the same concerns in the issues, but ultimately no good solution was provided.

But the biggest problem was that an analytics system relied on two platforms, which was too heavy in terms of deployment and maintenance. When either the database or Netlify encountered problems or needed migration, it would bring many additional costs. So when I updated my blog's commenting system recently, I thought I might as well switch to the lighter GoatCounter.

### GoatCounter + Zeabur

![goatcounter_stats](https://image.pseudoyu.com/images/goatcounter_stats.png)

I stumbled upon this niche analytics system while checking Reorx's blog code updates. I was immediately attracted by its Retro Internet style. It has almost no superfluous buttons, yet the functionality is very complete. Moreover, it uses a go single binary file + sqlite single file database architecture, which is lightweight and easy to deploy. So I decided to migrate.

Actually, my own GoatCounter is deployed on [fly.io](https://fly.io/), but I've already explained the operation instructions for fly in great detail in my previous article about Remark42. I didn't want to repeat too much. Coincidentally, I've been heavily using [Zeabur](https://zeabur.com?referralCode=pseudoyu), a Serverless platform, recently. So this article will use [Zeabur](https://zeabur.com?referralCode=pseudoyu) as an example, though the method is equally applicable to other similar platforms.

I've also provided configuration files for fly.io deployment and docker-compose deployment on VPS after the Zeabur deployment solution for reference.

## GoatCounter Deployment Instructions

GoatCounter's code itself is open-source - "[GitHub - arp242/goatcounter](https://github.com/arp242/goatcounter)", with clear and easy-to-read documentation. You can configure it according to your actual needs. The GoatCounter + Zeabur solution only involves a single service, with the database using sqlite mounted in a volume, so the deployment is very simple.

### Deploying with Zeabur

[Zeabur](https://zeabur.com?referralCode=pseudoyu) requires a Developer Plan for container application deployment, which costs $5/month. However, for image services like this, the overall usage and cost are relatively low, and the monthly quota is sufficient to deploy many services. You can choose according to your needs. The overall deployment process is much simpler compared to fly.io. All operations can be completed using the web interface, without the need to install additional command-line tools.

#### Register on zeabur

![zeabur_login](https://image.pseudoyu.com/images/zeabur_login.png)

Visit the [Zeabur](https://zeabur.com?referralCode=pseudoyu) official website and click on the top right corner to log in with your GitHub account authorization.

#### Create a New Project

![zeabur_new_project](https://image.pseudoyu.com/images/zeabur_new_project.png)

After entering the main interface, click the `Create Project` button in the top right corner.

![zeabur_hk_region](https://image.pseudoyu.com/images/zeabur_hk_region.png)

I chose the AWS data center in Hong Kong. Different data centers have some differences in access speed, performance, and price. You can choose according to your needs.

#### Configure Image Deployment

![zeabur_build](https://image.pseudoyu.com/images/zeabur_build.png)

In the next step, choose to deploy using a Docker container image.

![zeabur_docker_custom_config](https://image.pseudoyu.com/images/zeabur_docker_custom_config.png)

Since we're using a self-built image and there's no official GoatCounter template, we click to choose custom.

![zeabur_prebuilt_edit_toml](https://image.pseudoyu.com/images/zeabur_prebuilt_edit_toml.png)

At this step, you can fill in various configuration items on the interface yourself, but perhaps because I'm used to fly.io's file configuration mode, I chose to `Edit TOML file` in the bottom left corner. You can also directly copy my configuration file and modify it.

```toml
name = "yu-goatcounter"

[source]
image = "pseudoyu/goatcounter"

[[ports]]
id = "web"
port = 8080
type = "HTTP"

[[volumes]]
id = "goatcounter-data"
dir = "/data"

[env]
PORT = { default = "8080" , expose = true }
GOATCOUNTER_DB = { default = "sqlite3://data/goatcounter.sqlite3" , expose = true }
```

![zeabur_prebuilt_goatcounter_toml](https://image.pseudoyu.com/images/zeabur_prebuilt_goatcounter_toml.png)

After configuration, click the deploy button in the bottom right corner.

#### Deployment Complete

![yu-goatcounter_project](https://image.pseudoyu.com/images/yu-goatcounter_project.png)

After clicking deploy, wait for a moment, and there will be a generated default project name. You can modify it to a more readable name, such as `yu-goatcounter`, in the settings in the upper left corner.

#### Configure Custom Domain

![zeabur_create_domain](https://image.pseudoyu.com/images/zeabur_create_domain.png)

After the service is deployed, we need to bind a domain to access the website through the public network. Zeabur provides free second-level domains like `xx.zeabur.app`, or you can bind your own domain.

![zeabur_custom_domain](https://image.pseudoyu.com/images/zeabur_custom_domain.png)

The generated domain can be used directly without any other configuration, such as `goatcounter.zeabur.app`. If you're using a custom domain, you need to add a CNAME record in your domain management backend, pointing to a data center address in the format of `xxx.cname.zeabur-dns.com`.

![cloudflare_goatcounter_config](https://image.pseudoyu.com/images/cloudflare_goatcounter_config.png)

For example, my domain is hosted on Cloudflare, and the added CNAME record is as shown in the above image. I asked the official support, and they said if you choose the AWS HK data center, you can use Cloudflare's proxy, which theoretically would be faster. You can configure according to your needs.

Additionally, if you choose the Huawei Cloud data center, you need to file for domain registration and add an extra TXT record. You can follow the prompts to operate.

![zeabur_custom_domain_success](https://image.pseudoyu.com/images/zeabur_custom_domain_success.png)

A green display indicates successful configuration. At this point, our GoatCounter service deployment is complete.

#### Data Backup

We had this section in our configuration:

```toml
[[volumes]]
id = "goatcounter-data"
dir = "/data"
```

This function mounts the `/data` directory inside the container (where our sqlite database is located) to a storage volume with the id `goatcounter-data`. If you don't mount a storage volume, data will be lost when the container restarts or redeploys.

Regarding this storage volume point, Zeabur's interface doesn't have a very intuitive display and management operation, to the extent that I always doubt whether my configuration is effective.

![zeabur_add_goatcounter_backup](https://image.pseudoyu.com/images/zeabur_add_goatcounter_backup.png)

After researching for a while, I found that you can first pause the service in the settings, then add a new backup in the backup module above. After clicking download, you can see our backup file locally, with the directory hierarchy as follows:

```plaintext
data/
└── goatcounter-data
    └── goatcounter.sqlite3
```

This indicates that our data has been successfully persisted. I hope Zeabur can have a more intuitive display on the interface.

### Deploying with fly.io

For a purely free solution, you can still refer to the article I mentioned "[Build Your Free Blog Comment System from Scratch (Remark42 + fly.io)](https://www.pseudoyu.com/en/2024/07/22/free_commenting_system_using_remark42_and_flyio/)". Only the `fly.toml` configuration part is different. I've also provided the configuration file I use - "[fly.toml](https://github.com/pseudoyu/goatcounter-on-fly/blob/master/fly.toml)" for reference.

### Deploying with Docker and docker-compose

Interestingly, because the author of goatcounter is very persistent and feels that containerizing such a single-file application would actually increase maintenance costs, no official image is provided. However, having an image is still convenient for deploying on your own VPS or serverless platform. So I used Github Actions to create a CI for building images and uploading to Docker Hub. You can use it if needed. The corresponding Dockerfile and Docker Compose file can also be referenced from this [Commit](https://github.com/pseudoyu/goatcounter/commit/b98de9873ee331133a39b409fd4bb00cf55c8a05), or you can directly use `pseudoyu/goatcounter` and the `docker-compose.yml` file.

```yaml
version: '3'

services:
  goatcounter:
    image: pseudoyu/goatcounter
    ports:
      - 8080:8080
    environment:
      - PORT=8080
      - GOATCOUNTER_DB=sqlite3://data/goatcounter.sqlite3
    volumes:
      - ./data:/data
    restart: unless-stopped
```

## GoatCounter Configuration Instructions

In the above section, we completed the deployment of the GoatCounter service. Now we can access our analytics system service through the generated/custom domain. For example, I access it through `https://goatcounter.pseudoyu.com`.

![goatcounter_create_user](https://image.pseudoyu.com/images/goatcounter_create_user.png)

The first login requires creating a user. Fill in the email and password, then click `Create`.

![goatcounter_dashboard_success](https://image.pseudoyu.com/images/goatcounter_dashboard_success.png)

After successful login, there's no data yet, and a script will be prompted, which we'll use in our blog configuration later.

## Configuring GoatCounter for the Blog

Following the above, we've completed the deployment and basic configuration of the GoatCounter service. Now we need to add the analytics component to our blog posts. Taking my Hugo blog as an example:

```html
<script data-goatcounter="https://goatcounter.pseudoyu.com/count"
        async src="//goatcounter.pseudoyu.com/count.js"></script>
```

![add_goatcounter_script_in_hugo](https://image.pseudoyu.com/images/add_goatcounter_script_in_hugo.png)

Add the above code to the `head` of my Hugo theme. For example, in my Hugo theme, it's in the `layouts/partials/head.html` file. Different themes or different SSG frameworks might have slightly different locations, but they're broadly similar.

One thing to note is that goatcounter ignores requests from `localhost` to avoid too much dirty data during local preview. Therefore, you won't see data when debugging locally; you need to deploy the webpage to see access data.

![final_display_of_goatcounter](https://image.pseudoyu.com/images/final_display_of_goatcounter.png)

The effect after collecting data is roughly as shown in the above image. You can also set some configuration items, add new pages, view detailed data, etc., in the GoatCounter interface. This includes displaying the visit count for each page. You can explore according to the documentation.

## Conclusion

At this point, our blog analytics system is set up! This article is part of my blog setup and deployment tutorial series. The main body of the blog theme is complete, with only some details like in-blog search remaining for experience optimization. I hope this can be of reference to everyone.