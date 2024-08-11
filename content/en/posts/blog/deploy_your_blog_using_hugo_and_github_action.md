---
title: "Hugo + GitHub Action: Building Your Automated Blog Publishing System"
date: 2022-05-29T20:39:29+08:00
draft: false
tags: ["hugo", "github", "github action", "github pages", "cloudflare", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

In a previous article, "Free Personal Blog System Setup and Deployment Solution (Hugo + GitHub Pages + Cusdis)", I mentioned using Hugo, a static site generator, to truly build my personal blog. I made some personal customizations and configurations based on the hugo-theme-den theme from the Hugo open-source community to meet my needs.

My solution primarily consists of the following core components:

1. Personal blog source repository for version control of blog configurations and all article .md source files, coupled with GitHub Action for automated deployment, automatically generating static sites and pushing them to the GitHub Pages blog publishing repository.
2. (Optional) GitHub Pages blog publishing repository, named in the form of username.github.io, using GitHub Pages for website deployment, which can use custom domain names through CNAME resolution configuration.
3. (Optional) Cloudflare account and Cloudflare Pages project.
4. Hugo theme repository, fork your favorite theme, and version control your personal customization and configuration, linked to the personal blog source repository via git submodule.
5. Other component source repositories, such as umami website data statistics and Cusdis website comment system, etc.

The following text will provide a detailed explanation of the setup, local testing, automated deployment, and maintenance processes, which I hope will be helpful to everyone.

## Building a Blog with Hugo

![hugo_website](https://image.pseudoyu.com/images/hugo_website.png)

Hugo is a blogging tool implemented in Go that uses Markdown for article editing, automatically generates static site files, supports rich theme configurations, and can also embed plugins like comment systems through JavaScript, offering high customization. Besides Hugo, there are other choices like Gatsby, Jekyll, Hexo, Ghost, etc., which are similar in implementation and usage. You can choose according to your preference.

### Installing Hugo

I'm using macOS, so I use the official recommended homebrew method to install the Hugo program. The process is similar for other systems.

```bash
brew install hugo
```

After completion, use the following command to verify:

```bash
hugo version
```

### Creating a Hugo Website

After installing the Hugo program using the above command, you can create, configure, and locally debug the website using the hugo new site command.

```bash
hugo new site blog-test
```

![hugo_new_site](https://image.pseudoyu.com/images/hugo_new_site.png)

### Configuring the Theme

After creating our site using the above command, we need to configure the theme. The Hugo community has a rich selection of themes, which you can choose from the official website's Themes menu based on your preferred style and preview effects. After selection, you can enter the theme project repository, which usually has detailed installation and configuration instructions. Below, I'll demonstrate the configuration process using the hugo-theme-den theme I'm currently using as an example.

#### Linking the Theme Repository

We can directly git clone the theme repository for use, but this method has some drawbacks. When you later modify the theme, it may conflict with the original theme, making version management and subsequent updates inconvenient. I chose to fork the original theme repository to my own account and use git submodule to link the repository. This way, I can maintain the theme modifications separately in the future.

```bash
cd blog-test/
git init
git submodule add https://github.com/pseudoyu/hugo-theme-den themes/hugo-theme-den
```

![hugo_init_theme](https://image.pseudoyu.com/images/hugo_init_theme.png)

#### Updating the Theme

If you've cloned someone else's blog project for modification, you need to use the following command to initialize:

```bash
git submodule update --init --recursive
```

If you need to synchronize the latest modifications from the theme repository, run the following command:

```bash
git submodule update --remote
```

#### Initializing Theme Configuration and Publishing

Each theme usually provides some sample configurations and initial pages. When starting to use a theme, you can copy the files from its exampleSite/ directory to the site directory and adjust the configuration based on that.

```bash
cp -rf themes/hugo-theme-den/exampleSite/* ./
```

After initializing the basic theme configuration, we can configure site details in the config.toml file. Refer to the theme's documentation for specific configuration items.

![hugo_theme_config](https://image.pseudoyu.com/images/hugo_theme_config.png)

After completion, you can publish new articles using the hugo new command.

```bash
hugo new posts/blog-test.md
```

![hugo_new_post](https://image.pseudoyu.com/images/hugo_new_post.png)

#### Local Site Debugging

Hugo generates static web pages. When editing and debugging locally, we can use the hugo server command for real-time local preview debugging without needing to regenerate each time.

```bash
hugo server
```

![hugo_server](https://image.pseudoyu.com/images/hugo_server.png)

After running the service, we can access our local preview webpage through the browser at http://localhost:1313.

![hugo_server_preview](https://image.pseudoyu.com/images/hugo_server_preview.png)

### Purchasing a Domain Name

As an externally published website, we need to purchase a domain name and configure its resolution to point to the server where our website is located, allowing the outside world to access it conveniently. There are many domain name purchasing platforms; I've used Cloudflare, NameSilo, GoDaddy, etc. I ultimately prefer Cloudflare because it also provides powerful features like CDN, website data analysis, and custom rules.

First, we need to register a Cloudflare account. After logging in, select "Register Domain" from the left sidebar and search for the domain you want to register.

![cloudflare_register_domain](https://image.pseudoyu.com/images/cloudflare_register_domain.png)

After selecting your desired domain, click and choose the purchase duration and fill in your personal information.

![cloudflare_register_domain_choose](https://image.pseudoyu.com/images/cloudflare_register_domain_choose.png)

Choose a payment method; it's recommended to select automatic renewal to avoid forgetting to renew.

![cloudflare_register_domain_payment](https://image.pseudoyu.com/images/cloudflare_register_domain_payment.png)

Select Personal for the type and click to complete the purchase.

![cloudflare_register_done](https://image.pseudoyu.com/images/cloudflare_register_done.png)

Wait for Cloudflare to process, and then you can view the information.

![cloudflare_domain](https://image.pseudoyu.com/images/cloudflare_domain.jpg)

### Publishing Blog with Cloudflare Pages (Recommended)

**[Updated 2024-06-30]**

#### Introduction to Cloudflare Pages

GitHub Pages is already a free and powerful static website hosting platform that seamlessly integrates with GitHub code repositories. However, its access speed in China is not ideal. Since my domain is already hosted on Cloudflare, I tried Cloudflare Pages, which is a static website hosting service launched by Cloudflare. It's completely free (at least I haven't exceeded the free quota so far) and can directly connect to GitHub code repositories, achieving the same automated deployment functionality as GitHub Pages while providing better access routes. It's currently a better solution.

![cloudflare_pages_create](https://image.pseudoyu.com/images/cloudflare_pages_create.png)

#### Creating a Cloudflare Pages Project

First, we need to register a Cloudflare account, then select the "Workers & Pages" menu on the left and click to create a project.

![cloudflare_pages_with_git](https://image.pseudoyu.com/images/cloudflare_pages_with_git.png)

The next step offers two options: directly uploading static files or connecting to git. The first option is usually suitable for single-page or very low-frequency update projects that don't need GitHub code hosting, such as single HTML page websites. Connecting to git allows for better automatic building of new web pages for each blog submission, which is the method we'll use.

#### Building with Hugo

![yu_blog_test_build_hugo_cloudflare_pages](https://image.pseudoyu.com/images/yu_blog_test_build_hugo_cloudflare_pages.png)

Since Cloudflare Pages provides almost all common website building tools on the market, such as Next.js, Astro, Hugo, etc., we can choose from two methods for deployment:

1. Directly use the building tools provided by Cloudflare Pages to generate static web pages and deploy them online based on the repository code.
2. Generate a static web page repository or branch similar to the GitHub Pages method mentioned above, and deploy it online directly through Cloudflare Pages.

![cloudflare_build_site_hugo_in_progress](https://image.pseudoyu.com/images/cloudflare_build_site_hugo_in_progress.png)

![cloudflare_pages_build_done](https://image.pseudoyu.com/images/cloudflare_pages_build_done.png)

The first method can greatly simplify our deployment process. All we need to do is link the blog source repository we created above (such as my repository pseudoyu/yu-blog). Each submission will automatically build and deploy, only requiring a wait of a few tens of seconds to complete, without the need to write various GitHub Actions build commands like with GitHub Pages. It's very convenient and the most recommended method.

The second method is actually similar to the GitHub Pages approach and is more suitable for websites with special requirements for the build process. For example, when building my personal blog website, I simultaneously execute some Python in GitHub Actions to automatically update my About page. These complex operations cannot be directly handled by the building tools provided by Cloudflare Pages, so I chose the second method.

You can directly use the following simplified GitHub Actions in your blog source repository:

```yml
name: deploy

on:
    push:
    workflow_dispatch:
    schedule:
        # Runs everyday at 8:00 AM
        - cron: "0 0 * * *"

jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              with:
                  submodules: true
                  fetch-depth: 0

            // Other steps you want to add

            - name: Setup Hugo
              uses: peaceiris/actions-hugo@v2
              with:
                  hugo-version: "latest"

            - name: Build Web
              run: hugo

            - name: Deploy Web
              uses: peaceiris/actions-gh-pages@v3
              with:
                  github_token: ${{ secrets.GITHUB_TOKEN }}
                  publish_dir: ./public
                  publish_branch: cf-pages
```

on indicates the trigger conditions for GitHub Action. I set three conditions: push, workflow_dispatch, and schedule:

- push: Execute GitHub Action after a push action occurs in this project repository
- workflow_dispatch: Can be manually called from the Action toolbar in the GitHub project repository
- schedule: Execute GitHub Action on a schedule, such as my setting to execute every morning Beijing time, mainly to use some automated statistical CI to automatically update my blog's about page, such as this week's coding time, audio and video records, etc. If you don't need the timing feature, you can delete this condition

jobs represents the tasks in GitHub Action. We set up a build task, runs-on indicates the GitHub Action running environment, we chose ubuntu-latest. Our build task includes four main steps: Checkout, Setup Hugo, Build Web, and Deploy Web, where run is the command to execute, and uses is a plugin in GitHub Action. We used the peaceiris/actions-hugo@v2 and peaceiris/actions-gh-pages@v3 plugins. In the Checkout step, setting submodules to true in with can synchronize the submodules of the blog source repository, which is our theme module.

The above GitHub Actions will push the static files generated by the blog to the cf-pages branch, because we choose this branch for deployment in Cloudflare Pages. If we need to add some additional steps, we can add some custom steps before the build, which is very flexible. For specific applications, you can see the "GitHub - yu-blog/.github/workflows/deploy.yml" example.

#### Configuring Custom Domain

![custom_domain_yu_blog](https://image.pseudoyu.com/images/custom_domain_yu_blog.png)

Setting up a custom domain is also very simple. Just select custom domain in the navigation bar and add the domain you want to bind.

![cf_pages_custom_domain_dns](https://image.pseudoyu.com/images/cf_pages_custom_domain_dns.png)

If it's a domain registered/hosted in Cloudflare, you can directly select "Activate Domain", which will automatically add DNS resolution. If it's a domain from another platform, manually add CNAME resolution.

![custom_domain_wait_dns](https://image.pseudoyu.com/images/custom_domain_wait_dns.png)

After configuring DNS, just wait for it to take effect.

### Publishing Blog with GitHub Pages

#### Creating a Repository

The GitHub Pages project needs to follow the special naming format of username.github.io. After establishing the repository, you can configure your registered custom domain in the settings to point to the URL generated by GitHub Pages. Additionally, you need to change the baseURL in the blog site configuration file config.toml to your custom domain, in the format of "https://www.pseudoyu.com/". This allows the blog site to properly access the website service generated by GitHub Pages.

![github_pages_repo](https://image.pseudoyu.com/images/github_pages_repo.png)

#### Domain Resolution

After registering according to the steps above, you need to set up DNS resolution with your domain hosting provider. Here, we need to choose CNAME, pointing to our GitHub Pages URL.

![cloudflare_cname_config](https://image.pseudoyu.com/images/cloudflare_cname_config.png)

Because CNAME resolution can't set the root domain, meaning you can only set www.pseudoyu.com or other subdomains, not pseudoyu.com, we can use Cloudflare's custom rules to set domain redirection. The specific configuration is as follows, just replace my domain with your own. Even if you registered your domain through NameSilo, you can add a site through Cloudflare to implement this functionality, or other hosting platforms have similar features, just follow their instructions to configure.

![cloudflare_cname_rule_config](https://image.pseudoyu.com/images/cloudflare_cname_rule_config.png)

After completing the above preparations, we can now access our GitHub Pages through our custom domain. Currently, because the project repository is empty, visiting will show a 404 page.

We want the static website generated by Hugo to be hosted through the GitHub Pages service, without having to maintain the service ourselves, which is more stable and secure. Therefore, we need to upload the static web page files generated by Hugo to the GitHub Pages project repository.

#### Manual Publishing

After editing blog content and debugging locally through hugo server, we can generate static web page files using the hugo command.

```bash
hugo
cd public/
```

![hugo_gen_pages](https://image.pseudoyu.com/images/hugo_gen_pages.png)

Hugo by default stores generated static web page files in the public/ directory. We can initialize the public/ directory as a git repository and associate it with our pseudoyu/pseudoyu.github.io remote repository to push our web page static files.

```bash
git init
git remote add origin git@github.com:pseudoyu/pseudoyu.github.io
git add .
git commit -m "add test"
```

![hugo_public_init](https://image.pseudoyu.com/images/hugo_public_init.png)

After checking the file modifications, you can push to the GitHub Pages repository using git push origin master. Wait a few minutes, and you can access our blog site through our custom domain, completely consistent with our local hugo server debugging.

#### Automated Publishing

Through the above commands, we can manually publish our static files, but there are still some drawbacks:

1. The publishing steps are still cumbersome, requiring switching to the public/ directory for uploading after local debugging.
2. Unable to backup and version control the blog .md source files.

Therefore, we need a simple and smooth way to publish the blog. First, let's initialize the repository for the blog source files, such as my repository pseudoyu/yu-blog.

Because our blog is based on GitHub and GitHub Pages, we can use the official GitHub Action for CI automatic publishing. I'll explain this in detail below. GitHub Action is a continuous integration and continuous delivery (CI/CD) platform that can be used to automate build, test, and deployment pipelines. Currently, many workflows have been developed, which can be directly used with simple configuration.

The configuration is located in the repository directory .github/workflows, with a .yml suffix. My GitHub Action configuration is pseudoyu/yu-blog deploy.yml, and an example configuration for automatic publishing is as follows:

```yml
name: deploy

on:
    push:
    workflow_dispatch:
    schedule:
        # Runs everyday at 8:00 AM
        - cron: "0 0 * * *"

jobs:
    build:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout
              uses: actions/checkout@v2
              with:
                  submodules: true
                  fetch-depth: 0

            - name: Setup Hugo
              uses: peaceiris/actions-hugo@v2
              with:
                  hugo-version: "latest"

            - name: Build Web
              run: hugo

            - name: Deploy Web
              uses: peaceiris/actions-gh-pages@v3
              with:
                  PERSONAL_TOKEN: ${{ secrets.PERSONAL_TOKEN }}
                  EXTERNAL_REPOSITORY: pseudoyu/pseudoyu.github.io
                  PUBLISH_BRANCH: master
                  PUBLISH_DIR: ./public
                  commit_message: ${{ github.event.head_commit.message }}
```

First, you need to change the EXTERNAL_REPOSITORY in the above deploy.yml to your own GitHub Pages repository, such as my setting pseudoyu/pseudoyu.github.io.

Because we need to push from the blog repository to an external GitHub Pages repository, specific permissions are required. You need to create a Token under GitHub account's Setting - Developer setting - Personal access tokens.

![github_psersonal_access_token](https://image.pseudoyu.com/images/github_psersonal_access_token.png)

The permissions need to enable repo and workflow.

![yu_blog_personal_token](https://image.pseudoyu.com/images/yu_blog_personal_token.png)

After configuration, copy the generated Token (Note: it will only appear once), then add the PERSONAL_TOKEN environment variable as the Token we just created in the Settings - Secrets - Actions of our blog source repository. This way, GitHub Action can access the Token.

After completing the above configuration, push the code to the repository, which will trigger GitHub Action, automatically generating blog pages and pushing them to the GitHub Pages repository.

![yu_blog_ci](https://image.pseudoyu.com/images/yu_blog_ci.png)

When the GitHub Pages repository is updated, it will automatically trigger the official page deployment CI, achieving our website publication.

![page_build_ci](https://image.pseudoyu.com/images/page_build_ci.png)

After the above configuration, we have achieved local Hugo blog setup and version control, GitHub Pages website deployment and publishing, Hugo theme management and updates, and other functions, implementing a complete system. Now, whenever we finish editing blog content locally using familiar Markdown syntax, we only need to push the code and wait a few minutes to access the updated website through our custom domain.

### Component Extensions

A complete blog system also requires some components, such as website data statistics and comment systems. I have written comprehensive Serverless setup tutorials for these two core needs, which you can deploy and configure according to your requirements.

- [Building a Free Personal Blog Data Statistics System from Scratch (umami + Vercel + Heroku)]([https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/))
- [Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)]([https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/))

## Conclusion

The above is the free blog automatic deployment system I implemented using Hugo and GitHub Action. My implementation repository is in the pseudoyu/yu-blog repository, and my customized theme repository is in pseudoyu/hugo-theme-den.

I've also implemented many interesting automated personal statistics functions using GitHub Action, automatically updating my GitHub Profile. The project repository is pseudoyu/pseudoyu. You can explore .github/workflows on your own. These systems are continuously being improved, and I welcome everyone to contribute and exchange ideas.

## References

> 1. [Hugo Official Website](https://gohugo.io)
> 2. [GitHub Action](https://github.com/features/actions)
> 3. [GitHub Pages](https://pages.github.com)
> 4. [Cloudflare Official Website](https://www.cloudflare.com)
> 5. [Free Personal Blog System Setup and Deployment Solution (Hugo + GitHub Pages + Cusdis)]([https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/](https://www.pseudoyu.com/en/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/))
> 6. [Building a Free Personal Blog Data Statistics System from Scratch (umami + Vercel + Heroku)]([https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/](https://www.pseudoyu.com/en/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/))
> 7. [Lightweight Open Source Free Blog Comment System Solution (Cusdis + Railway)]([https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/))
> 8. [My Pseudoyu Personal Blog](https://www.pseudoyu.com)
> 9. [My GitHub Profile](https://github.com/pseudoyu)