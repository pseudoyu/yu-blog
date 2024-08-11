---
title: "Build Your Free Blog Comment System from Scratch (Remark42 + fly.io)"
date: 2024-07-22T01:10:42+08:00
draft: false
tags: ["commenting-system", "serverless", "fly.io", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

In the article "What Changed in My Blog in 2024", I introduced the blog system I built using Serverless platforms and some open-source projects, and also started this series of tutorials to document the entire process of building and deploying.

This article is about the solution for the commenting system.

## Evolution of Commenting Systems

![remark42_comments](https://image.pseudoyu.com/images/remark42_comments.png)

I often feel that comments are not just communication between readers and authors, but the content itself is also part of the article. Sometimes the thoughts and discussions in comments can be more valuable than the article itself. Therefore, I have always placed great importance on the commenting system. I am unwilling to trust some third-party hosted services, do not want any censorship, and want the style to be as minimalist as possible and consistent with my blog style.

During the development of my blog, the commenting system solution has gone through several iterations. Regarding the types and choices of commenting systems, I very much like the developer [reorx](https://reorx.com/)'s detailed introduction in "Changing Blog Commenting Systems". I won't elaborate further here; this article focuses more on personal experience and detailed setup process.

### Disqus

The first blog commenting system I used was the notorious Disqus, a cumbersome and user privacy-collecting well-known commenting system. Because it loads slowly and the free version often comes with some ads, it was really unbearable. Plus, at that time, there were basically no comments, so there was no migration burden. I abandoned it after using it for a short time.

### Utterances

So I switched to another commenting system based on GitHub issues called utterances. It generates an issue for each article, and users comment on the issue by authorizing GitHub login. The advantage of this method is that it only needs to authorize an utterances-bot for management, without the need to deploy services and maintain databases by yourself. However, after using it for a while, I felt there were several shortcomings:

- It relies on the GitHub API for comment management. If the interface changes later or restrictions are placed on this type of commenting method using issues, it would be unstable.
- Readers must authorize GitHub login, which is very inconvenient for non-technical people or readers using mobile devices.
- It pollutes the Issues record of the GitHub repository and is also inconvenient for subsequent migration to other systems.

### Cusdis + Supabase + Vercel

Cusdis is an open-source commenting system focusing on data privacy made by [Randy](https://lutaonan.com/). It's very lightweight, only about 5kb after gzipping. From the name, you can see it's hard to bear Disqus, so he made an alternative version. Therefore, it also supports importing historical data from Disqus, which is very thoughtful.

I've been using it since mid-2021, exactly three years now. Except for the initial hassle with deployment platforms due to Heroku and Railway successively charging, it has been running steadily. However, I've also encountered some issues in use:

- Probably due to some modifications made by WeChat's built-in browser, the comment component can't be seen when the blog is opened from WeChat chat/dialogue.
- Although you can enter an email address, it doesn't support subscribing to comment replies.
- The administrator needs to manually review comments, but the TG Bot for comment notifications often fails, causing missed comments.

However, overall, it's still a highly recommended solution even today. It's lightweight, easy to self-deploy, and has a minimalist and good-looking style. For setup instructions, refer to "Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)".

Given that Railway has cancelled its Free Plan since August last year, if you still want to use it completely free, you can use Vercel/Netlify/Zeabur to deploy the main project for free, and deploy a free PostgreSQL database instance on [Supabase](https://supabase.com), passing the link as an environment variable to the Cusdis service. Other procedures are similar.

Also, because its core features haven't been updated for a long time, it seems a bit rudimentary compared to other more mature commenting systems. However, as I also adhere to the principle of "good enough is good enough", I never had the idea of migrating/updating. I only participated in some development of the Cusdis V2 version for a while when I was learning front-end, but I didn't do it for long.

Due to the constant failure of Vercel deployment upgrades in April, which caused me to not receive comments for nearly a few weeks, plus I did have some functional requirements, so I made up my mind to migrate and explored new solutions.

### Remark42 + fly.io

After researching around, I chose [Remark42](https://remark42.com/) which [reorx](https://reorx.com/) finally selected in the article "Changing Blog Commenting Systems".

Just in terms of configuration options, it's much richer than Cusdis. Currently, I've configured several common social account logins (GitHub, Twitter, Telegram, email), anonymous commenting is allowed, it supports email subscription for reply notifications, and I've also set up TG bot notifications. It's deployed on [fly.io](https://fly.io), with go single binary + single file database, a very comfortable solution. For more detailed introduction and advantages of Remark42, you can refer to the article mentioned above.

Although Remark42 provides some migration solutions, it doesn't inherently support Cusdis which I was using. But since it's written in Golang, I added migration logic myself and seamlessly migrated the 438 comments data accumulated over these years.

## Remark42 + fly.io Deployment Instructions

The Remark42 + fly.io solution only involves a single service, with the database using boltdb mounted in a volume, but all operations are within fly.io's Free Plan.

Below, I'll introduce how to build this free commenting system from scratch.

Remark42's code itself is open source - "GitHub - umputun/remark42", and it provides an officially maintained image. The documentation is clear and easy to read, and you can configure it according to your actual needs.

### Install `flyctl` Command Line Tool

[fly.io](https://fly.io) differs greatly from Railway, Zeabur, etc. that I used before in that most operations are based on command line and configuration files, rather than operating in a web management backend. So first, you need to install the `flyctl` command line tool according to the [documentation](https://fly.io/docs/flyctl/install/).

Taking macOS as an example, I use `brew` for installation:

```bash
brew install flyctl
```

### Authorize Login

Open the terminal tool and use the following command for authorized login:

```bash
flyctl auth login
```

![fly_auth_login](https://image.pseudoyu.com/images/fly_auth_login.png)

![fly_auth_web](https://image.pseudoyu.com/images/fly_auth_web.png)

Log in to your account or create a new account on the web end. After completion, click "Continue as xxx" to complete the authorization login of the `flyctl` command line.

### Create Application Directory

![create_fly_config](https://image.pseudoyu.com/images/create_fly_config.png)

Since I usually manually manage configurations rather than using their official templates, I create a directory like `remark42-on-fly` and put all configuration files, environment variables, etc. in this path.

And use VS Code for editing (you can also use vim or other editors/IDEs).

### Configuration File

fly.io mainly uses `.toml` format configuration files for service management. Here is the configuration file corresponding to the service I deployed:

```toml
app = 'yu-remark42-01'
primary_region = 'hkg'

[build]
  image = 'umputun/remark42:latest'

[[mounts]]
  source = 'remark42_data_01'
  destination = '/srv/var'

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = false
  auto_start_machines = true
  min_machines_running = 1
  processes = ['app']

[env]
  REMARK_URL = 'https://yu-remark42-01.fly.dev/'
  SECRET = 'remark42-secret'
  SITE= 'remark42-demo'
  ADMIN_SHARED_ID= ''

[[vm]]
  cpu_kind = 'shared'
  cpus = 1
  memory_mb = 256
```

Here's a detailed configuration explanation:

- `app`: Application name, I used `yu-remark42-01` here, you can modify it according to your actual situation
- `primary_region`: Deployment region, you can choose the region you want to deploy from this [list](https://fly.io/docs/reference/regions/#fly-io-regions), I chose Hong Kong
- `[Build]`, this part is mainly about service image configuration
  - `image`: Service image, using the officially provided `umputun/remark42:latest`, you can specify the tag version if needed
- `[[mounts]]`, this part is mainly about mounting data volume configuration, as Remark42 uses boltdb database, it needs persistent storage
  - `source`: Data volume name, I used `remark42_data_01` here
  - `destination`: Mount directory, I mounted it to `/srv/var`, which is Remark42's default data storage directory
- `[http_service]`, this part is mainly about service-related configuration
  - `internal_port`: Internal service port, using 8080
  - `force_https`: Force the use of HTTPS
  - `auto_stop_machines`: Set to `false`
  - `auto_start_machines`: Set to `true`, i.e., auto-start
  - `min_machines_running`: Minimum number of running machines, set to 1
  - `processes`: Service process, set to `app`
- `[env]`, configure environment variables
  - `REMARK_URL`: URL of Remark42 service, I used `https://yu-remark42-demo.fly.dev/` here, which is automatically generated by fly.io, it needs to be changed later if you have a custom domain
  - `SITE`: Site name, I used `remark42-demo` here
  - `SECRET`: Custom JWT Token, I used `remark42-secret` here
  - `ADMIN_SHARED_ID`: Administrator ID, I used an empty string here, i.e., no administrator, can be supplemented later
- `[[vm]]`, this part is mainly about machine-related configuration
  - `cpu_kind`: CPU type, set to `shared`
  - `cpus`: Number of CPUs, set to 1
  - `memory_mb`: Memory, set to 256MB

### Create Service

After completing and checking the configuration, run the following command to create the service:

```bash
flyctl launch
```

![fly_launch_remark42](https://image.pseudoyu.com/images/fly_launch_remark42.png)

### Environment Variable Configuration

Currently, we have only deployed the service and have not set environment variables, so the service will have problems starting. Next, we set environment variables, put them in the `prod.env` file:

```plaintext
AUTH_GITHUB_CID=<your_github_cid>
AUTH_GITHUB_CSEC=<your_github_csec>
AUTH_TWITTER_CID=<your_twitter_cid>
AUTH_TWITTER_CSEC=<your_twitter_csec>
AUTH_ANON=true
AUTH_TELEGRAM=true
TELEGRAM_TOKEN=<your_telegram_token>
NOTIFY_ADMINS=telegram
NOTIFY_TELEGRAM_CHAN=<your_telegram_group>
NOTIFY_USERS=email
AUTH_EMAIL_ENABLE=true
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_TLS=true
SMTP_USERNAME=xxx@gmail.com
SMTP_PASSWORD=<your_password>
AUTH_EMAIL_FROM=xxx@gmail.com
NOTIFY_EMAIL_FROM=xxx@gmail.com
```

The environment variable part is relatively complex, refer to the [documentation](https://remark42.com/docs/configuration/authorization/) for specific parameters.

#### Login/Authorization Configuration

I configured anonymous commenting, GitHub, Twitter, and Telegram methods, you can configure other login methods according to your situation.

- Anonymous login
  - `AUTH_ANON`: Whether to allow anonymous comments, I chose to allow, i.e., users can comment without logging in
- GitHub login
  - `AUTH_GITHUB_CID` and `AUTH_GITHUB_CSEC`: Client ID and Client Secret of GitHub OAuth App
- Twitter login
  - `AUTH_TWITTER_CID` and `AUTH_TWITTER_CSEC`: Client ID and Client Secret of Twitter OAuth App
- Telegram login
  - `AUTH_TELEGRAM`: Whether to allow Telegram login
  - `TELEGRAM_TOKEN`: Telegram Bot Token, created through `botfather`
- Email login
  - `AUTH_EMAIL_ENABLE`: Whether to allow email login
  - `AUTH_EMAIL_FROM`: Sending email for email login

#### Notification Configuration

- Telegram notification for administrators, refer to [this part of the documentation](https://remark42.com/docs/configuration/telegram/) for creating and configuring Telegram Bot
  - `NOTIFY_ADMINS`: Method of notifying administrators, choose telegram
  - `NOTIFY_TELEGRAM_CHAN`: If enabling telegram notification for administrators, need to configure the corresponding Channel id, just fill in the id part after `t.me/xxx`, such as `pseudoyuchat`
- Email notification for users, refer to [this part of the documentation](https://remark42.com/docs/configuration/email/) for configuring email SMTP, etc.
  - `NOTIFY_USERS`: Method of notifying users, I chose email, i.e., email notification, so you need to configure the SMTP below
  - `NOTIFY_EMAIL_FROM`: Sending address for email notifications

#### Email SMTP Configuration

The email login and email notification mentioned above both need to configure SMTP server, this part can also be configured according to your email service provider [referring to the documentation](https://remark42.com/docs/configuration/email/).

- `SMTP_HOST`: SMTP server address
- `SMTP_PORT`: SMTP server port
- `SMTP_TLS`: Whether to enable TLS
- `SMTP_USERNAME`: SMTP username
- `SMTP_PASSWORD`: SMTP password

### Import Environment Variables to Service

After completing the environment variable configuration according to the above instructions, run the following command in the directory where the configuration file and environment variable file are located to import the environment variables:

```bash
fly secrets import < prod.env
```

![fly_secret_import](https://image.pseudoyu.com/images/fly_secret_import.png)

![deploy_status_remark42](https://image.pseudoyu.com/images/deploy_status_remark42.png)

After execution, check the service status in the fly.io console. If the status is `Deployed`, it indicates successful deployment.

### Configure Custom Domain (Optional)

If you don't want to use the default domain provided by fly.io, you can configure a custom domain.

![custom_domain_flyio](https://image.pseudoyu.com/images/custom_domain_flyio.png)

Enter the fly.io console, select the `yu-remark42-01` service you just deployed, click the `Certificates` option on the left, then click `Add a Certificate` in the upper right corner, and follow the prompts to add a custom domain.

![custom_domain_dns_in_fly](https://image.pseudoyu.com/images/custom_domain_dns_in_fly.png)

After clicking `Create Certificate`, there will be a page showing the DNS records you need to add. Follow the prompts to add them.

![cloudflare_dns_remark42](https://image.pseudoyu.com/images/cloudflare_dns_remark42.png)

![flyio_certificate_success](https://image.pseudoyu.com/images/flyio_certificate_success.png)

For example, my domain is hosted on Cloudflare, I added two DNS records according to the prompts. Return to the page and click `Check again` or wait for a while and refresh to view. If all show green, the configuration is successful.

![change_remark_url](https://image.pseudoyu.com/images/change_remark_url.png)

At this point, we can modify `REMARK_URL` to the custom domain in `fly.toml`, then execute the following command to redeploy the service. Any subsequent changes to the configuration file can be updated using this command:

```bash
fly deploy
```

## Configuring Remark42 in Your Blog

Now that we've completed the deployment of the Remark42 service, we need to add the Remark42 comment component to our blog posts. I'll use my Hugo blog as an example.

### Define Hugo Theme Comments Component

I created a new `comments.html` file in the `layouts/partials` directory of my Hugo blog to define the Remark42 comment component:

```html
<div class="comments">
  <div class="title">
    <span>Comments</span>
    <span class="counter"><span class="remark42__counter" data-url="{{ .Permalink }}"></span></span>
  </div>
  <div id="remark42">
  </div>
</div>

<script>
  var remark_config = {
    host: 'https://comments.pseudoyu.com',
    site_id: 'pseudoyu.com',
    components: ['embed', 'counter'],
    max_shown_comments: 20,
    simple_view: true,
    theme: 'light',
  }
</script>

<script>
    (function () {
      // init or reset remark42
      const remark42 = window.REMARK42
      if (remark42) {
        remark42.destroy()
        remark42.createInstance(remark_config)
      } else {
        for (const component of remark_config.components) {
          var d = document, s = d.createElement('script');
          s.src = `${remark_config.host}/web/${component}.mjs`;
          s.type = 'module';
          s.defer = true;
          // prevent the <script> from loading mutiple times by InstantClick
          s.setAttribute('data-no-instant', '')
          d.head.appendChild(s);
        }
      }
    })();
</script>
```

The `host` and `site_id` in `remark_config` need to be modified according to your actual configuration. Other parts of the configuration can remain unchanged or be adjusted according to the documentation.

After configuring the `comments` component, include it at the bottom of the article in `layouts/posts/single.html`:

```html
{{ partial "comments.html" . }}
```

![add_comments_code_in_hugo](https://image.pseudoyu.com/images/add_comments_code_in_hugo.png)

The general position is as shown in the image. If you're using another theme or blog system, you'll need to find the corresponding template file for your articles and modify it.

### Local Preview/Deploy Website

![test_remark42_embedded](https://image.pseudoyu.com/images/test_remark42_embedded.png)

At this point, you can preview locally or deploy the website to check if the comment system is displaying correctly. With this, our service deployment is complete.

### Get User ID and Configure Admin

![get_user_id_remark42](https://image.pseudoyu.com/images/get_user_id_remark42.png)

After logging in, authorizing, and testing comments, you can click on the avatar in Remark42 to open the management page. Double-click and then `CMD/Ctrl+C` to get the User ID starting with `github_` or other platforms. You can configure this in `ADMIN_SHARED_ID` (change the `fly.toml` configuration file and run `fly deploy` to redeploy). This will make you an administrator, and administrators have the authority to delete and manage other users' comments.

## Other Considerations

I exported the comment data from Cusdis in JSON format according to certain conditions, and converted and migrated the format through a Go program, thus preserving all previous comments.

Because Cusdis itself doesn't provide an export function and the migration need is too niche, I didn't directly contribute code to the upstream or write it into a complete script. Friends with similar needs can refer to this PR for processing - "feat: add cusdis to remark42 migrator support by pseudoyu · Pull Request #1 · pseudoyu/remark42".

## Conclusion

The above is the process of building my blog's comment system. The setup and configuration of a comment system are relatively complex, and the configuration method in this article may become outdated over time. If you encounter problems, refer more to the [official documentation](https://remark42.com/docs/getting-started/installation/).

This is one of my blog building and deployment series tutorials. If you're interested in building data statistics systems, in-blog search, etc., please stay tuned. I hope this can be of reference to everyone.
