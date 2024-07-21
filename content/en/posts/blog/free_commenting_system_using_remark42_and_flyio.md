---
title: "从零开始搭建你的免费博客评论系统（Remark42 + fly.io）"
date: 2024-07-22T01:10:42+08:00
draft: false
tags: ["commenting-system", "serverless", "fly.io", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## 前言

在「[2024 年了，我的博客有了什么变化](https://www.pseudoyu.com/en/2024/06/29/what_changed_in_my_blog_2024/)」一文中，我介绍了自己使用 Serverless 平台和一些开源项目搭建的博客系统，也开启了这个系列教程来记录搭建和部署全过程。

本篇是关于评论系统的解决方案。

## 评论系统迭代

![remark42_comments](https://image.pseudoyu.com/images/remark42_comments.png)

我常常觉得评论不仅仅是读者与作者之间的沟通互动，其内容本身也是文章的一部分，甚至常常有些评论的思考与观点讨论会比文章本身更有价值，所以对于评论系统一直很重视，并不愿意信任一些第三方托管的服务，不希望有什么审查，也想风格尽可能简约，并与自己的博客风格相符。

在博客发展过程中，评论系统方案也经历过几次迭代，关于评论系统的类型和选择，我很喜欢的开发者 [reorx](https://reorx.com/) 在「[更换博客评论系统](https://reorx.com/blog/blog-commenting-systems/)」中有详细的介绍了，我不作更多引申了，本文更重个人体验与详细的搭建过程。

### Disqus

我最早使用的博客评论系统是万恶的 Disqus，一个笨重且会收集用户隐私的知名评论系统，因为加载比较慢，且免费版本经常会附带一些广告，实在难以忍受，再加上当时其实也基本上没什么评论，并没有什么迁移负担，用了没多久就直接弃用了。

### Utterances

于是换成了另一个基于 GitHub issues 的评论系统 utterances，它会为每篇文章生成一个 issue，用户通过授权 GitHub 登录来对 issue 发表评论。这种方式的好处是只需要授权一个 utterances-bot 来进行管理，无需自己部署服务，维护数据库等。但是用了一段时间后，觉得有几点不足：

- 基于 GitHub API 进行评论管理，如之后接口变动或对这类利用 issue 进行评论的方式进行限制，会不太稳定
- 读者必须要授权 GitHub 登录，非技术人员或使用移动端阅读的读者使用起来很不方便
- 会污染 GitHub 仓库的 Issues 记录，也不方便后续迁移到其他系统

### Cusdis + Supabase + Vercel

Cusdis 是 [Randy](https://lutaonan.com/) 做的一个注重数据隐私的开源的评论系统，十分轻量，经过 gzipped 后大约只有 5kb，从名字来看也知道是难以忍受 Disqus，自己做了一个替代版，因此它也是支持 Disqus 历史数据导入的，很贴心。

从 2021 年中就开始使用了，到现在整整三年了，除了最开始的时候因为 Heroku、Railway 相继收费而折腾了一下部署平台外，一直都稳稳地运行着，不过我在使用中也有遇到一些问题：

- 大概是由于微信内置浏览器做了一些魔改，在博客从微信聊天/对话打开是看不到评论组件的
- 尽管可以输入邮箱，但并不支持订阅评论回复
- 需要管理员手动审核评论，但评论提醒的 TG Bot 时常失效而错过评论

不过整体来说时至今日依然是十分值得推荐的方案，轻量，方便自部署，风格也简约好看，搭建教程参看「[轻量级开源免费博客评论系统解决方案 （Cusdis + Railway）](https://www.pseudoyu.com/en/2022/05/24/free_and_lightweight_blog_comment_system_using_cusdis_and_railway/)」。

鉴于 Railway 从去年 8 月起已经取消了 Free Plan，如果依然想完全免费使用，可以使用 Vercel/Netlify/Zeabur 免费部署主项目，并在 [Supabase](https://supabase.com) 上部署一个免费的 PostgreSQL 数据库实例，把链接作为环境变量传入 Cusdis 服务中即可，其他流程大同小异。

另外因为其核心功能已经许久没有什么更新，比起其他较为成熟的评论系统也显得有些简陋，不过由于我也秉持着够用即可的原则，一直没动迁移/更新的念头，只有在其中一阵子在学前端时还参与了一些 Cusdis V2 版本的开发，不过也没做多久。

由于四月时 Vercel 部署升级的时候一直失败，导致接近几周的时间没收到评论，再加上确实有了一些功能需求，所以下定决心进行迁移，探究起了新的方案。

### Remark42 + fly.io

调研了一圈后选择了 [reorx](https://reorx.com/) 在「[更换博客评论系统](https://reorx.com/blog/blog-commenting-systems/)」一文中最后选定的 [Remark42](https://remark42.com/)。

单纯就配置选项来说比起 Cusdis 还是丰富了不少，目前配置了常用的几种社交账号登录（GitHub、Twitter、Telegram、邮箱）、可以匿名评论、支持邮件订阅回复提醒并且也设置了 TG bot 提醒，并且部署在 [fly.io](https://fly.io/)，go 单二进制 + 数据库单文件，很舒服的解决方案，更详细的 Remark42 的介绍和优势可以参看上面那篇文章。

虽然 Remark42 提供了一些迁移方案，但本身并不支持我使用的 Cusdis，但好在它是用 Golang 写的，我自己添加了迁移逻辑，将这些年沉淀下来的 438 条评论数据都无缝迁移过来了。

## Remark42 + fly.io 部署说明

Remark42 + fly.io 的方案仅牵扯到单个服务，数据库使用的是 sqlite 挂载于 volume 中，但所有操作都在 fly.io 的 Free Plan 中。

下面将从零开始介绍如何搭建这个免费评论系统。

Remark42 本身代码开源 —— 「[GitHub - umputun/remark42](https://github.com/umputun/remark42)」，并提供了官方维护的镜像，文档清晰易读，可以根据自己的实际需求进行配置。

### 安装 `flyctl` 命令行工具

[fly.io](https://fly.io) 与我之前使用的 Railway、Zeabur 等很大的一个不同点是它大部分操作基于命令行与配置文件，而不是在网页端管理后台进行操作，所以首先需要根据[文档](https://fly.io/docs/flyctl/install/)安装 `flyctl` 命令行工具。

以 macOS 为例，我使用 `brew` 进行安装：

```bash
brew install flyctl
```

### 授权登录

打开终端工具，使用以下命令进行授权登录：

```bash
flyctl auth login
```

![fly_auth_login](https://image.pseudoyu.com/images/fly_auth_login.png)

![fly_auth_web](https://image.pseudoyu.com/images/fly_auth_web.png)

在 Web 端进行账户登录或新建账号，完成后点击 `Continue as xxx` 即完成 `flyctl` 命令行的授权登录。

### 创建应用目录

![create_fly_config](https://image.pseudoyu.com/images/create_fly_config.png)

由于我通常会手动进行进行配置管理，而不是用它官方的模板，所以我会新建一个类似 `remark42-on-fly` 的目录，并将所有的配置文件、环境变量等放在这个路径下。

并使用 VS Code 进行编辑（也可以使用 vim 或者其他编辑器/IDE）。

### 配置文件

fly.io 主要是使用 `.toml` 格式的配置文件进行服务管理，以下是我部署的服务对应的配置文件：

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

我进行详细的配置说明：

- `app`：应用名称，这里我使用了 `yu-remark42-01`，可以根据自己的实际情况进行修改
- `primary_region`：部署区域，可以从这个[列表](https://fly.io/docs/reference/regions/#fly-io-regions)中选择自己想部署的区域，我选择了香港
- `[Build]`，这个部分主要是服务镜像相关的配置
  - `image`：服务镜像，使用了官方提供的 `umputun/remark42:latest`，如有需要可以指定 tag 版本
- `[[mounts]]`，这个部分主要是挂载数据卷的配置，由于 Remark42 使用 sqlite 数据库，需要持久化存储
  - `source`：数据卷名称，这里我使用了 `remark42_data_01`
  - `destination`：挂载目录，这里我挂载到了 `/srv/var`，这个目录是 Remark42 默认的数据存储目录
- `[http_service]`，这个部分主要是服务相关的配置
  - `internal_port`：服务内部端口，使用 8080
  - `force_https`：强制使用 HTTPS
  - `auto_stop_machines`：设置为 `false`
  - `auto_start_machines`：设置为 `true`，即自动启动
  - `min_machines_running`：最小运行机器数，设置为 1
  - `processes`：服务进程，设置为 `app`
- `[env]`，配置环境变量
  - `REMARK_URL`：Remark42 服务的 URL，这里我使用了 `https://yu-remark42-demo.fly.dev/`，这是 fly.io 自动生成的，后续如果有了自定义域名则需要更改
  - `SITE`：站点名称，这里我使用了 `remark42-demo`
  - `SECRET`：自定义的 JWT Token，这里我使用了 `remark42-secret`
  - `ADMIN_SHARED_ID`：管理员 ID，这里我使用了空字符串，即没有管理员，后续可以补充
- `[[vm]]`，这个部分主要是机器相关的配置
  - `cpu_kind`：CPU 类型，设置为 `shared`
  - `cpus`：CPU 数量，设置为 1
  - `memory_mb`：内存，设置为 256MB

### 创建服务

完成并检查配置后，运行以下命令进行服务创建：

```bash
flyctl launch
```

![fly_launch_remark42](https://image.pseudoyu.com/images/fly_launch_remark42.png)

### 环境变量配置

目前只是部署了服务，并没有设置环境变量，因此服务启动会有问题，接下来我们设置环境变量，放在`prod.env` 文件中：

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

环境变量的部分相对比较复杂，具体参数参看[文档](https://remark42.com/docs/configuration/authorization/)。

#### 登录/授权配置

我配置了匿名评论、GitHub、Twitter 与 Telegram 几种方式，可以根据自己的情况配置其他登录方式。

- 匿名登录
  - `AUTH_ANON`：是否允许匿名评论，我选择了允许，即用户可以不登录评论
- GitHub 登录
  - `AUTH_GITHUB_CID` 与 `AUTH_GITHUB_CSEC`：GitHub OAuth App 的 Client ID 与 Client Secret
- Twitter 登录
  - `AUTH_TWITTER_CID` 与 `AUTH_TWITTER_CSEC`：Twitter OAuth App 的 Client ID 与 Client Secret
- Telegram 登录
  - `AUTH_TELEGRAM`：是否允许 Telegram 登录
  - `TELEGRAM_TOKEN`：Telegram Bot Token，通过 `botfather` 创建
- 邮箱登录
  - `AUTH_EMAIL_ENABLE`：是否允许邮箱登录
  - `AUTH_EMAIL_FROM`：邮箱登录的发送邮箱

#### 通知配置

- Telegram 通知管理员，参看[文档这部分](https://remark42.com/docs/configuration/telegram/)进行 Telegram Bot 的创建和配置
  - `NOTIFY_ADMINS`：通知管理员的方式，选择 telegram
  - `NOTIFY_TELEGRAM_CHAN`：如启用 telegram 通知管理员，需要配置对应 Channel id，只需要填写 `t.me/xxx` 后面的 id 部分即可，如 `pseudoyuchat`
- Email 通知用户，参看[文档这部分](https://remark42.com/docs/configuration/email/)进行邮箱 SMTP 等配置
  - `NOTIFY_USERS`：通知用户的方式，我选择了了 email, 即邮件通知，则需要配置下文的 SMTP
  - `NOTIFY_EMAIL_FROM`：邮箱通知的发送地址

#### 邮件 SMTP 配置

上文的邮箱登录与邮箱通知都需要配置 SMTP 服务器，这部分也可以根据自己的邮箱服务商[参照文档](https://remark42.com/docs/configuration/email/)进行配置。

- `SMTP_HOST`：SMTP 服务器地址
- `SMTP_PORT`：SMTP 服务器端口
- `SMTP_TLS`：是否启用 TLS
- `SMTP_USERNAME`：SMTP 用户名
- `SMTP_PASSWORD`：SMTP 密码

### 导入环境变量到服务

根据以上说明完成环境变量配置后，在配置文件和环境变量文件所在目录运行以下命令导入环境变量：

```bash
fly secrets import < prod.env
```

![fly_secret_import](https://image.pseudoyu.com/images/fly_secret_import.png)

![deploy_status_remark42](https://image.pseudoyu.com/images/deploy_status_remark42.png)

执行完成后到 fly.io 控制台查看服务状态即可，如为 `Deployed` 状态即表示部署成功。

### 配置自定义域名（可选）

如果你不想使用 fly.io 提供的默认域名，可以配置自定义域名。

![custom_domain_flyio](https://image.pseudoyu.com/images/custom_domain_flyio.png)

进入 fly.io 控制台，选择刚部署的 `yu-remark42-01` 服务，点击左侧的 `Certificates` 选项，然后点击右上角 `Add a Certificate`，按照提示添加自定义域名即可。

![custom_domain_dns_in_fly](https://image.pseudoyu.com/images/custom_domain_dns_in_fly.png)

点击 `Create Certificate` 后，会有一个页面显示你所需要添加的 DNS 记录，按照提示添加即可。

![cloudflare_dns_remark42](https://image.pseudoyu.com/images/cloudflare_dns_remark42.png)

![flyio_certificate_success](https://image.pseudoyu.com/images/flyio_certificate_success.png)

例如我的域名托管在 Cloudflare，我按照提示添加了两条 DNS 记录，返回页面后点击 `Check again` 或等待一段时间后刷新查看，都显示绿色即为配置成功。

![change_remark_url](https://image.pseudoyu.com/images/change_remark_url.png)

此时，我们可以在 `fly.toml` 中修改 `REMARK_URL` 为自定义域名，然后执行以下命令重新部署服务即可，之后对配置文件进行任何改动都可以使用该命令进行更新：

```bash
fly deploy
```

## 博客配置 Remark42

上文我们完成的 Remark42 服务的部署，现在则需要在我们的博文中加入 Remark42 评论组件。

以我使用的 Hugo 博客为例。

### 定义 Hugo 主题 Comments 组件

我在 Hugo 博客的 `layouts/partials` 目录下新建了一个 `comments.html` 文件，用于定义 Remark42 评论组件：

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

`remark_config` 中的 `host` 与 `site_id` 需要根据自己的实际配置进行修改，其他部分配置可以保持不变，或根据文档进行调整。

配置好 `commnets` 组件后，在 `layouts/posts/single.html` 中文章底部引入：

```html
{{ partial "comments.html" . }}
```

![add_comments_code_in_hugo](https://image.pseudoyu.com/images/add_comments_code_in_hugo.png)

大体位置如图所示，如使用的是其他主题或博客系统，则需要找到自己文章对应的模板文件进行修改。

### 本地预览/部署网站

![test_remark42_embedded](https://image.pseudoyu.com/images/test_remark42_embedded.png)

此时可以在本地预览或部署网站以查看评论系统是否正常显示，至此我们的服务部署完成。

### 获取 User ID 并配置 Admin

![get_user_id_remark42](https://image.pseudoyu.com/images/get_user_id_remark42.png)

登录授权完成后并测试评论后，可在 Remark42 中点击头像打开管理页面，双击后 `CMD/Ctrl+C` 可以获取以 `github_` 或其他平台开头的 User ID，可以将其配置到 `ADMIN_SHARED_ID` 中（更改 `fly.toml` 配置文件并运行 `fly deploy` 重新部署，即可成为管理员，管理员有权限对其他用户的评论进行删除等管理操作。

## 其他

我把之前 Cusdis 中的评论数据按照一定格式导出 json 格式的数据，并通过 go 程序进行格式转换与迁移，因此保留了之前所有的评论。

因为 Cusdis 本身不提供导出功能且迁移的需求太过小众，我并没有直接向上游贡献代码，也没有写成完善的脚本，有类似需求的朋友可以参考这个 PR 进行处理 —— 「[feat: add cusdis to remark42 migrator support by pseudoyu · Pull Request \#1 · pseudoyu/remark42](https://github.com/pseudoyu/remark42/pull/1/)」。

## 总结

以上就是我的博客评论系统的搭建过程，评论系统的搭建与配置相对繁复，且本文的配置方式或许会随时时间而过时，遇到问题可多参照[官方文档](https://remark42.com/docs/getting-started/installation/)。

这是我的博客搭建部署系列教程之一，如对数据统计系统、博客内搜索等搭建感兴趣，请持续关注，希望能对大家有所参考。
