---
title: "Hugo + GitHub Action，搭建你的博客自动发布系统"
date: 2022-05-29T20:39:29+08:00
draft: false
tags: ["hugo", "github", "github action", "github pages", "cloudflare", "serverless", "self-host", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

在之前的一篇《[免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）](https://www.pseudoyu.com/zh/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)》中，我提到了自己通过 [Hugo](https://gohugo.io) 这个静态网站生成器来真正搭建我的个人博客，并在 Hugo 开源社区中 [hugo-theme-den](https://github.com/shaform/hugo-theme-den) 这个主题基础上进行了一些个人定制化改造和配置，满足了自己的需求。

我的方案主要分为以下几个核心部分：

1. 个人博客源仓库，对博客配置及所有文章 `.md` 源文件进行版本管理，配合 GitHub Action 进行自动化部署，自动生成静态站点推送到 GitHub Pages 博客发布仓库。
2. GitHub Pages 博客发布仓库，以 `username.github.io` 形式命名的仓库，使用 GitHub Pages 实现网站部署，可以通过配置域名 CNAME 解析使用自定义域名。
3. Hugo 主题仓库，fork 喜欢的主题，并对自己的个人定制化改造配置进行版本管理，通过 `git submodule` 的方式链接到个人博客源仓库。
4. 其他组件源仓库，如 [umami 网站数据统计](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)及 [Cusdis 网站评论系统](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)等。

下文会对搭建、本地测试、自动化部署维护等过程进行详细讲解，希望对大家所有帮助。

## 使用 Hugo 搭建博客

![hugo_website](https://image.pseudoyu.com/images/hugo_website.png)

[Hugo](https://gohugo.io) 是用 Go 实现的博客工具，采用 Markdown 进行文章编辑，自动生成静态站点文件，支持丰富的主题配置，也可以通过 js 嵌入像是评论系统等插件，高度定制化。除了 Hugo 外， 还有 Gatsby、Jekyll、Hexo、Ghost 等选择，实现和使用都差不多，可以根据自己的偏好进行选择。

### 安装 Hugo

我使用的是 macOS，所以使用官方推荐的 homebrew 方式进行 hugo 程序的安装，其他系统也类似。

```bash
brew install hugo
```

完成后，使用以下命令进行验证：

```bash
hugo version
```

### 创建 Hugo 网站

通过上述命令安装 hugo 程序后，就可以通过 `hugo new site` 命令进行网站创建、配置与本地调试了。

```bash
hugo new site blog-test
```

![hugo_new_site](https://image.pseudoyu.com/images/hugo_new_site.png)

### 配置主题

当通过上文命令创建我们的站点后，需要进行主题配置，Hugo 社区有了很丰富的主题，可以通过官网 [Themes](https://themes.gohugo.io) 菜单选择自己喜欢的风格，查看预览效果，选择后可以进入主题项目仓库，一般都会有很详细的安装及配置说明。下面我就以我目前在使用的 [hugo-theme-den](https://github.com/shaform/hugo-theme-den) 这个主题为例，演示一下配置流程。

#### 关联主题仓库

我们可以将主题仓库直接 `git clone` 下来进行使用，但这种方式有一些弊端，当之后自己对主题进行修改后，可能会与原主题产生一些冲突，不方便版本管理与后续更新。我采用的是将原主题仓库 `fork` 到自己的账户，并使用 `git submodule` 方式进行仓库链接，这样后续可以对主题的修改进行单独维护。

```bash
cd blog-test/
git init
git submodule add https://github.com/pseudoyu/hugo-theme-den themes/hugo-theme-den
```

![hugo_init_theme](https://image.pseudoyu.com/images/hugo_init_theme.png)

#### 更新主题

如果是 clone 了其他人的博客项目进行修改，则需要用以下命令进行初始化：

```bash
git submodule update --init --recursive
```

如果需要同步主题仓库的最新修改，需要运行以下命令：

```bash
git submodule update --remote
```

#### 初始化主题配置及发布

每个主题一般都会提供一些实例配置与初始页面，开始使用主题时可以将其 `exampleSite/` 目录下的文件复制到站点目录下，在此基础上进行调整配置。

```bash
cp -rf themes/hugo-theme-den/exampleSite/* ./
```

初始化主题基础配置后，我们可以在 `config.toml` 文件中进行站点细节配置，具体配置项参考各主题说明文档。

![hugo_theme_config](https://image.pseudoyu.com/images/hugo_theme_config.png)

完成后，可以通过 `hugo new` 命令发布新文章。

```bash
hugo new posts/blog-test.md
```

![hugo_new_post](https://image.pseudoyu.com/images/hugo_new_post.png)

#### 本地调试站点

Hugo 会生成静态网页，我们在本地编辑调试时可以通过 `hugo server` 命令进行本地实时调试预览，无须每次都重新生成。

```bash
hugo server
```

![hugo_server](https://image.pseudoyu.com/images/hugo_server.png)

运行服务后，我们可以通过浏览器 `http://localhost:1313` 地址访问我们的本地预览网页。

![hugo_server_preview](https://image.pseudoyu.com/images/hugo_server_preview.png)

### 使用 GitHub Pages 前期准备

#### 域名购买

作为一个对外发布的网站，我们需要购买一个域名并配置解析，指向我们网站所在的服务器，才能让外界以比较方便的方式访问。域名购买平台很多，我用过的有 [Cloudflare](https://www.cloudflare.com)、[NameSilo](https://www.namesilo.com)、[GoDaddy](https://www.godaddy.com) 等，我最后常用的还是 Cloudflare，因为其同时还提供了 CDN、网站数据分析、定制规则等强大功能。

首先我们需要注册一个 Cloudflare 账户，登录后选择左侧边栏的“注册域”，并搜索自己想注册的域名。

![cloudflare_register_domain](https://image.pseudoyu.com/images/cloudflare_register_domain.png)

选择了心仪的域名后，点击并选择购买时限并填写个人信息。

![cloudflare_register_domain_choose](https://image.pseudoyu.com/images/cloudflare_register_domain_choose.png)

选择付款方式，建议可以选择自动续订，以免忘记续费。

![cloudflare_register_domain_payment](https://image.pseudoyu.com/images/cloudflare_register_domain_payment.png)

类型选择 Personal 即可，并点击完成购买。

![cloudflare_register_done](https://image.pseudoyu.com/images/cloudflare_register_done.png)

等待 Cloudflare 处理后即可查看信息。

![cloudflare_domain](https://image.pseudoyu.com/images/cloudflare_domain.jpg)

#### GitHub Pages 仓库

GitHub Pages 项目需要符合 `username.github.io` 的特殊命名格式，仓库建立完成后，可以在设置中配置自己注册的自定义域名来指向 GitHub Pages 生成的网址。此外，需要将博客站点配置文件 `config.toml` 中的 `baseURL` 改为自己的自定义域名，格式为 `"https://www.pseudoyu.com/"`，这样博客站点才能正常访问 GitHub Pages 生成的网站服务。

![github_pages_repo](https://image.pseudoyu.com/images/github_pages_repo.png)

#### 域名解析

按照上文步骤注册好后，需要在域名托管商进行 DNS 解析，在这里我们需要选择 CNAME，指向我们的 GitHub Pages 网址。

![cloudflare_cname_config](https://image.pseudoyu.com/images/cloudflare_cname_config.png)

因为 CNAME 解析没办法设置 root 域名，即只能设置 `www.pseudoyu.com` 或其他子域名，而不是 `pseudoyu.com`，因此，我们可以通过 Cloudflare 上自定义规则设置域名重定向，具体配置如下，仅需将我的域名替换成自己的域名即可。即使你是通过 NameSilo 注册的域名，也可以通过 Cloudflare 来添加站点以实现功能，或者其他托管平台也有类似的功能，按照说明配置即可。

![cloudflare_cname_rule_config](https://image.pseudoyu.com/images/cloudflare_cname_rule_config.png)

### GitHub Pages 发布博客

完成上述准备工作后，我们现在已经可以通过自定义域名来访问我们的 GitHub Pages 页面了，目前因为项目仓库是空的，访问后会报 `404` 页面。

我们希望 Hugo 生成的静态网站能通过 GitHub Pages 服务进行托管，而无需自己维护服务，更稳定、安全，因此我们需要上传 Hugo 生成的静态网页文件至 GitHub Page 项目仓库。

#### 手动发布

当我们编辑博客内容并通过 `hugo server` 本地调试后，就可以通过 `hugo` 命令生成静态网页文件了。

```bash
hugo
cd public/
```

![hugo_gen_pages](https://image.pseudoyu.com/images/hugo_gen_pages.png)

Hugo 默认会将生成的静态网页文件存放在 `public/` 目录下，我们可以通过将 `public/` 目录初始化为 git 仓库并关联我们的 `pseudoyu/pseudoyu.github.io` 远程仓库来推送我们的网页静态文件。

```bash
git init
git remote add origin git@github.com:pseudoyu/pseudoyu.github.io
git add .
git commit -m "add test"
```

![hugo_public_init](https://image.pseudoyu.com/images/hugo_public_init.png)

核对文件修改后，即可通过 `git push origin master` 推送到 GitHub Pages 仓库，稍等几分钟即可通过我们的自定义域名来访问我们的博客站点了，和我们 `hugo server` 本地调试完全一致。

#### 自动发布

通过上述命令我们可以手动发布我们的静态文件，但还是有以下弊端：

1. 发布步骤还是比较繁琐，本地调试后还需要切换到 `public/` 目录进行上传
2. 无法对博客 `.md` 源文件进行备份与版本管理

因此，我们需要简单顺滑的方式来进行博客发布，首先我们初始化博客源文件的仓库，如我的仓库为 [pseudoyu/yu-blog](https://github.com/pseudoyu/yu-blog)。

因为我们的博客基于 GitHub 与 GitHub Pages，可以通过官方提供的 GitHub Action 进行 CI 自动发布，下面我会进行详细讲解。GitHub Action 是一个持续集成和持续交付(CI/CD) 平台，可用于自动执行构建、测试和部署管道，目前已经有很多开发好的工作流，可以通过简单的配置即可直接使用。

配置在仓库目录 `.github/workflows` 下，以 `.yml` 为后缀。我的 GitHub Action 配置为 [pseudoyu/yu-blog deploy.yml](https://github.com/pseudoyu/yu-blog/blob/master/.github/workflows/deploy.yml)，自动发布示例配置如下：

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

`on` 表示 GitHub Action 触发条件，我设置了 `push`、`workflow_dispatch` 和 `schedule` 三个条件：

- `push`，当这个项目仓库发生推送动作后，执行 GitHub Action
- `workflow_dispatch`，可以在 GitHub 项目仓库的 Action 工具栏进行手动调用
- `schedule`，定时执行 GitHub Action，如我的设置为北京时间每天早上执行，主要是使用一些自动化统计 CI 来自动更新我博客的关于页面，如本周编码时间，影音记录等，如果你不需要定时功能，可以删除这个条件

`jobs` 表示 GitHub Action 中的任务，我们设置了一个 `build` 任务，`runs-on` 表示 GitHub Action 运行环境，我们选择了 `ubuntu-latest`。我们的 `build` 任务包含了 `Checkout`、`Setup Hugo`、`Build Web` 和 `Deploy Web` 四个主要步骤，其中 `run` 是执行的命令，`uses` 是 GitHub Action 中的一个插件，我们使用了 `peaceiris/actions-hugo@v2` 和 `peaceiris/actions-gh-pages@v3` 这两个插件。其中 `Checkout` 步骤中 `with` 中配置 `submodules` 值为 `true` 可以同步博客源仓库的子模块，即我们的主题模块。

首先需要将上述 `deploy.yml` 中的 `EXTERNAL_REPOSITORY` 改为自己的 GitHub Pages 仓库，如我的设置为 `pseudoyu/pseudoyu.github.io`。

因为我们需要从博客仓库推送到外部 GitHub Pages 仓库，需要特定权限，要在 GitHub 账户下 `Setting - Developer setting - Personal access tokens` 下创建一个 Token。

![github_psersonal_access_token](https://image.pseudoyu.com/images/github_psersonal_access_token.png)

权限需要开启 `repo` 与 `workflow`。

![yu_blog_personal_token](https://image.pseudoyu.com/images/yu_blog_personal_token.png)

配置后复制生成的 Token（注：只会出现一次），然后在我们博客源仓库的 `Settings - Secrets - Actions` 中添加 `PERSONAL_TOKEN` 环境变量为刚才的 Token，这样 GitHub Action 就可以获取到 Token 了。

完成上述配置后，推送代码至仓库，即可触发 GitHub Action，自动生成博客页面并推送至 GitHub Pages 仓库。

![yu_blog_ci](https://image.pseudoyu.com/images/yu_blog_ci.png)

而 GitHub Pages 仓库更新后，又会自动触发官方页面部署 CI，实现我们的网站发布。

![page_build_ci](https://image.pseudoyu.com/images/page_build_ci.png)

经过上述配置，我们已经实现了 Hugo 博客本地搭建及版本管理、GitHub Pages 部署网站发布，Hugp 主题管理及更新等功能，实现了完整的系统。现在每当我们本地通过熟悉的 Markdown 语法完成博客内容编辑后，只需要推送代码，等待几分钟，即可通过我们的自定义域名访问更新后的网站。

### 组件拓展

一个完整的博客系统还需要一些组件，如网站数据统计、评论系统等，我针对这两个核心需求也写了完整的 Serverless 搭建教程，可根据需求进行部署配置。

- [从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
- [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)

## 总结

以上就是我通过 Hugo 与 GitHub Action 实现的免费博客自动部署系统，我自己的实现仓库在 [pseudoyu/yu-blog](https://github.com/pseudoyu/yu-blog) 仓库中，我定制化的主题仓库在 [pseudoyu/hugo-theme-den](https://github.com/pseudoyu/hugo-theme-den) 中。

我使用 GitHub Action 还实现了很多好玩的自动化个人统计功能，自动更新我的[GitHub Profile](https://github.com/pseudoyu)，项目仓库为 [pseudoyu/pseudoyu](https://github.com/pseudoyu/pseudoyu)，可以进入 `.github/workflows` 中自行探索。这些系统还在不断完善中，欢迎大家参与贡献与交流。

## 参考资料

> 1. [Hugo 官网](https://gohugo.io)
> 2. [GitHub Action](https://github.com/features/actions)
> 3. [GitHub Pages](https://pages.github.com)
> 4. [Cloudflare 官网](https://www.cloudflare.com)
> 5. [免费的个人博客系统搭建及部署解决方案（Hugo + GitHub Pages + Cusdis）](https://www.pseudoyu.com/zh/2022/03/24/free_blog_deploy_using_hugo_and_cusdis/)
> 6. [从零开始搭建一个免费的个人博客数据统计系统（umami + Vercel + Heroku）](https://www.pseudoyu.com/zh/2022/05/21/free_blog_analysis_using_umami_vercel_and_heroku/)
> 7. [轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/zh/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)
> 8. [我的 Pseudoyu 个人博客](https://www.pseudoyu.com)
> 9. [我的 GitHub Profile](https://github.com/pseudoyu)
