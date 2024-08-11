---
title: "Building a Free Personal Blog Analytics System from Scratch (umami + Vercel + Heroku)"
date: 2022-05-21T16:56:47+08:00
draft: false
tags: ["hugo", "umami", "heroku", "vercel", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

![umami_dashboard_white](https://image.pseudoyu.com/images/umami_dashboard_white.png)

Previously, I wrote an article titled "Free Personal Blog System Setup and Deployment Solution (Hugo + GitHub Pages + Cusdis)", detailing my blog system built using Serverless and some open-source projects. I also started a series to document the setup process.

A few days ago, I came across an article by [Reorx](https://reorx.com) titled "Deploy umami for Personal Website Analytics". He introduced the [umami](https://umami.is) project and demonstrated its serverless deployment using [Railway](https://railway.app).

However, since I had previously used [Heroku](https://www.heroku.com/)'s free Postgres database service and deployed with [Vercel](http://vercel.com/) when setting up [Cusdis](https://cusdis.com), I wanted to continue using these platforms for umami to reduce setup and maintenance costs.

The following text will record the specific setup and deployment process. Thanks to the official one-click deployment method, the entire setup process was very smooth.

**[2024-06-30 Update]**

Later, as Heroku discontinued its free plan, if you still want to use it completely free, you can use Vercel/Netlify/Zeabur for free deployment of the main project + Supabase for deploying PostgreSQL database instances. Pass the link as an environment variable to the Umami service. The rest of the process remains applicable.

## Setup and Deployment Instructions

### Creating a Postgres Database with Heroku

#### Creating the Postgres Database

First, register for a Heroku account. After logging in successfully, click the button in the upper right corner to create a new application.

![cretae_app_in_heroku_1](https://image.pseudoyu.com/images/cretae_app_in_heroku_1.png)

Enter the instance name, and choose the region as you prefer. I selected United States. Click create.

![cretae_app_in_heroku_2](https://image.pseudoyu.com/images/cretae_app_in_heroku_2.png)

After creation, search and select the Postgres database in the Adds-on section of the Resources Tab.

![add_heroku_postgres](https://image.pseudoyu.com/images/add_heroku_postgres.png)

Choose the Free Plan. The Postgres database in Heroku is free and can be used continuously, eliminating setup and maintenance costs.

![heroku_postgres_plan](https://image.pseudoyu.com/images/heroku_postgres_plan.png)

After creation, check the `DATABASE_URL` in Settings, which will be used later for deployment.

![postgres_data_url](https://image.pseudoyu.com/images/postgres_data_url.jpg)

Click on the newly added Postgres add-on to proceed with settings.

![postgres_addon_details](https://image.pseudoyu.com/images/postgres_addon_details.png)

Once inside, select View Credentials in the Settings page and record the configuration parameters.

![heroku_credentials](https://image.pseudoyu.com/images/heroku_credentials.png)

![postgres_settings](https://image.pseudoyu.com/images/postgres_settings.jpg)

#### Initializing the Postgres Database

As database initialization is required, I used the DataGrip database management tool for connection, which is quite convenient. You can also connect and configure through the Heroku CLI.

![postgres_config](https://image.pseudoyu.com/images/postgres_config.jpg)

Umami needs to be initialized using the official [umami/sql/schema.postgresql.sql](https://github.com/mikecao/umami/blob/master/sql/schema.postgresql.sql) script.

![postgres_init_script](https://image.pseudoyu.com/images/postgres_init_script.png)

After execution, the database will have five tables with initialized data, and you can proceed with subsequent deployment work.

### One-Click Deployment of umami Service Using Vercel

#### Deploying the umami Service

After creating the database instance, you can deploy the umami service with one click through Vercel.

Visit the [Running on Vercel](https://umami.is/docs/running-on-vercel) module in the [umami official documentation](https://umami.is) for operation instructions and one-click deployment script.

![running_on_vercel](https://image.pseudoyu.com/images/running_on_vercel.png)

After clicking the one-click deployment button, you will be redirected to Vercel's one-click deployment page to create a Github repository for umami.

![vercel_create_umami_repo](https://image.pseudoyu.com/images/vercel_create_umami_repo.png)

Next, you need to enter the `DATABASE_URL` parameter address recorded when deploying the Heroku Postgres instance earlier, and you need to fill in a custom string `HASH_SLAT`.

![vercel_config_umami](https://image.pseudoyu.com/images/vercel_config_umami.png)

Click Deploy to start deployment. It will be completed in a few minutes.

![vercel_deploy](https://image.pseudoyu.com/images/vercel_deploy.png)

![vecel_deploy_done](https://image.pseudoyu.com/images/vecel_deploy_done.png)

#### Accessing the umami Service

After deployment, click Dashboard or the assigned Vercel domain to access the service. You will see the umami login interface.

![umami_login](https://image.pseudoyu.com/images/umami_login.png)

For the first login, enter the default username `admin` and default password `umami`. After successful login, you will be redirected to the umami management page. You can click on the avatar in the upper right corner to change your password.

![umami_change_password](https://image.pseudoyu.com/images/umami_change_password.png)

#### Configuring Personal Website to umami Service

After completing the basic account configuration, click on the Websites tab in the sidebar, then click Add Website.

![umami_add_website_1](https://image.pseudoyu.com/images/umami_add_website_1.png)

Fill in the basic website information. If you check the share link, it will generate a publicly accessible URL. I added it as a bookmark on my iPad's home screen, which also works great as a data dashboard.

![umami_add_website_2](https://image.pseudoyu.com/images/umami_add_website_2.png)

#### Configuring umami Script to Personal Blog Website

After creating the website, obtain the umami script.

![get_umami_script](https://image.pseudoyu.com/images/get_umami_script.jpg)

Once obtained, add the umami script to your personal website. I use the static blog Hugo, adding it within the `<head>` tag in the theme.

![set_umami_script](https://image.pseudoyu.com/images/set_umami_script.jpg)

After configuration and deployment, you can start tracking website data.

![umami_dashboard_white](https://image.pseudoyu.com/images/umami_dashboard_white.png)

#### Configuring Custom Script Name

Using the official `umami.js` script name might be blocked by some filtering rules. Therefore, we can customize the script name to achieve more accurate website data tracking.

The official also provides a convenient modification method. You can add the `TRACKER_SCRIPT_NAME` environment variable in the umami service already deployed in Vercel, configuring it to a custom name.

![umami_script_environment_varible](https://image.pseudoyu.com/images/umami_script_environment_varible.png)

After configuration, redeploy, and then change the script name in your personal website script.

![change_umami_script](https://image.pseudoyu.com/images/change_umami_script.jpg)

#### Configuring Custom Domain

If you don't want to use the `vercel.app` domain provided by Vercel, you can add a custom domain in Vercel. Follow the official Vercel guide to configure `CNAME` etc. for your domain provider.

![set_custom_domain](https://image.pseudoyu.com/images/set_custom_domain.png)

For example, I use a domain hosted by [Cloudflare](https://www.cloudflare.com), so I need to add domain resolution first.

![cloudflare_canme_config](https://image.pseudoyu.com/images/cloudflare_canme_config.png)

According to the official instructions, Cloudflare also needs to add a page rule. After configuration, you can complete the custom domain configuration.

![cloudflare_page_rule](https://image.pseudoyu.com/images/cloudflare_page_rule.png)

## Conclusion

The above is the complete process of adding the umami website statistics service to our website. Once configured, it requires no subsequent maintenance and allows for convenient website data tracking through the dashboard. This is one of my blog setup and deployment series tutorials. Please stay tuned, and I hope it can be of reference to everyone.

## References

> 1. [umami](https://umami.is)
> 2. [Deploy umami for Personal Website Analytics](https://reorx.com/blog/deploy-umami-for-personal-website/)
> 3. [Vercel Official Website](http://vercel.com)
> 4. [Heroku Official Website](https://www.heroku.com)