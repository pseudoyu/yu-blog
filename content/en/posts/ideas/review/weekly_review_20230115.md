---
title: "周报 #26 - 博客、客制化键盘和新服务器"
date: 2023-01-15T19:57:33+08:00
draft: false
tags: ["review", "life", "home", "cat", "hugo", "pagefind", "open-source"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

![weekly_review_20230115_photo](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/weekly_review_20230115_photo.png)

本篇是对 `2023-01-10` 到 `2023-01-15` 这周生活的记录与思考。

已经临近假期，虽然也算不上对过年有着多少仪式感。去年的那段时间花了一周多的时间通了『宝可梦 阿尔宙斯』和重温了『火焰之纹章 风花雪月』，过年当天煮了火锅并跟家里人视频通话了，似乎年就这样过去了。但由于今年决定了要回家，有寄养捏捏以及过年期间各种安排的事，倒是没能多放松，想把很多事提前做完，能匀出一些时间好好陪家人了。

工作上这周状态一般般，写完已经上线的需求出了几个细节小问题，不得不拖着 leader 和我一起加班处理，还有一部分年前要上线的新功能还没测完，还剩下两三天时间；和朋友做的项目也遇到了一些问题，原本负责前端的朋友因故离开了，不得不再去负责他的部分，上线也会有一些拖延，过年也没法真正清闲下来，也算是一个不小的调整吧。

因为要寄养在同事家，保险起见今天去了趟宠物医院检查，顺便剪个指甲。医生说状态很健康，之前的一些小病症已经基本康复了，也夸我照顾得好，开心。不过想到寄养还是有些舍不得和不放心，年后也会早些回来了，毕竟有了牵挂。

接受了一个有点神奇的采访，收到了一个巨可爱的键盘，继续优化了一下自己的博客（~~不写文章就知道优化主题了~~），还有很多有意思的事。

## 有趣的事与物

### 博客折腾

我目前版本的个人博客大概已经运行了接近三年了，之前也用过服务器自己搭建 [WordPress](https://wordpress.com/) 等方案，后来因为不够稳定性且数据迁移很麻烦，我转向了 Hugo 静态博客 + GitHub 自动部署 + Cloudflare 托管这种一劳永逸的方案，详细可以看『[2022 年了，聊聊我为什么还在写博客](https://www.pseudoyu.com/en/2022/06/12/why_i_still_write_blog_in_2022/)』和『[Hugo + GitHub Action，搭建你的博客自动发布系统](https://www.pseudoyu.com/en/2022/05/29/deploy_your_blog_using_hugo_and_github_action/)』。

而我选择用 Hugo 除了因为我主业是 Go 开发导致的有点莫名但并没有什么用的亲切感外，还有一个最主要的原因就是目前在用的主题『[den](https://github.com/shaform/hugo-theme-den)』，这是一个台湾的开发者自己写的主题，当时他因为构建速度等因素考虑打算从 [Pelican](https://github.com/getpelican/pelican) 转向 [Hugo](https://gohugo.io/)，但又喜欢自己原来的主题，所以自己复刻实现了一个，具体可以看他的这篇『[從 Pelican 及 WordPress 轉移到 Hugo](https://city.shaform.com/zh/2018/07/22/migrate-from-pelican-and-wordpress-to-hugo/)』。

我大概是 18 年关注到他的技术和个人想法输出的博客，可以说很大程度上我后来的文章风格与思维模式都受到了他很大的影响。而这种带着些老式互联网遗风的主题又刚好完美在我的审美上，于是一番折腾搭建上了，沿用到现在。

由于是个人使用为主，这个主题虽然很美观简约，但还是有一些功能缺失的地方，于是在使用的这三年里也不断根据自己的使用需求修修补补，去年也把自己对 RSS Feeds、相关文章、友链这一块的改动提了 pr，有一些经过了一些沟通后合并到了主分支里，还有几个还没改动（~~太偷懒了~~）。

最近刚好在 [P.J. Wu 吳秉儒](https://twitter.com/WuPingJu) 的博客里发现了 [Pagefind](https://pagefind.app/) 这一网页搜索方案，研究了一下集成到了我的博客里，效果很不错。

![pagefind_and_hugo_2](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/pagefind_and_hugo_2.png)

它采用了将文章索引文件预先生成而不是实时检索的方案，速度很快，也不需要额外的后端服务，很适合静态博客的部署方案。关于 Pagefind 的介绍和使用可以看看 [P.J. Wu 吳秉儒](https://twitter.com/WuPingJu) 的这一篇『[如何透過 Pagefind 在 Zola 產生的靜態網站裡加入搜尋功能](https://pinchlime.com/blog/how-to-add-a-search-function-to-zola-generated-static-websites-via-pagefind/)』，但是是集成进 Zola 博客框架并通过 Netlify 发布的，原理差不多。关于 Hugo 的集成方式我折腾配置一下再出一篇文章吧，可以预先通过[这个网址](https://www.pseudoyu.com/en/search)体验一下，或者点击导航栏的『Search』（加上了回到顶部功能，可以直接点击返回）。

我将它结合进了我原本的 GitHub CI 自动发布流，体验很无缝，并且通过 Hugo 的 shortcode 的方式集成一个搜索页面 UI 来供使用，很强大，也会向主题仓库提一下 pr 支持，看看这一块有没有需求。

但其实使用下来对中文支持有一些问题，没法很好的分词，比如『区块链』这个词直接搜索会无法匹配，改为『区块 链』，自己主动分词后才能得到想要的效果，也在页面注明了搜索方式了，~~又不是不能用~~，看看后续有没有更好的方案了。

![pagefind_and_hugo_1](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/pagefind_and_hugo_1.png)

有意思的是，本来这周的博客折腾已经到此为止了，但是突然 GitHub 发邮件提醒我有 pr 和评论，有一个陌生的朋友 fork 了我的博客并且做了一些样式调整和改动，增加了一些功能，后来还直接把自己改好的 css 文件发我参照了。

![github_blog_pr](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/github_blog_pr.png)

其实原本只是自用的一些方案，也常常陷入折腾了一下午主题没写一个字却自得其乐的状态，没想到也会有一些人关注到、认可并且采用，还能反过来解决不少我的一些问题，感觉很奇妙，有点慢慢感受到像是开源或是 work in public 的乐趣，总能有一些意想不到的收获。于是昨天晚上一通折腾，修改了好几个一直有点问题但是没改/没当回事的样式问题，还增加了回到顶部的按钮效果，还挺开心的。

### 服务器

之前周报提到过自己研究清楚通过 [Nginx Proxy Manager](https://nginxproxymanager.com/) 给自己的服务器进行反向代理后，上线了几个常用的服务和站点，比如之前的 [zlib.pseudoyu.com](https://zlib.pseudoyu.com/) 图书检索服务，因为得到了一些关注，也被一些群组和频道收录了，所以还是想着得持续维护下去保持服务稳定性和访问速度，但之前都是一些低性能的机子，几个服务就跑满了，于是趁着搬瓦工推出了一个新的还不错的 Plan，入了几台，2C2G + 40G 硬盘 + CN2GIA DC6 的线路，完全够一些服务的长期稳定运行了。

![yu_services_vps](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/yu_services_vps.png)

之前也还有一些机子，跑一些自己的基础服务，有些也搭载一些小应用给朋友用，这次也好好整理了一下，把所有服务都迁移到了一台机子，这里就得赞美一下 Docker 和 docker-compose 的管理方式了，数据迁移也太无缝了。全部迁移完，居然也才占用了一半的样子，幸福。

因为机器也多了（幸福的烦恼），所以也找了一个开源的监控服务进行管理，有一种赛博资本家的感觉，监督着这些机子好好工作不许偷懒。

![yu_server_status](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/yu_server_status.png)

### 桌面 Setup 与键盘

可能因为不打游戏，其实自己并不是一个资深的键盘爱好者，对于不同轴体、键帽的差异也很难说得清楚，之前也大多用的 Mac 自带的剪刀脚键盘，并没有觉得什么不适。

大概是在 20 年底，被她问到说有什么一直很想要但自己可能又不太下定决心买的东西，当时想了半天，说了 HHKB，其实比起实际需求更多只是好奇，而老式电池仓的这种复古设计也完全在我的审美上。

几天后收到了，是 HHKB Professional Hybrid Type-S 静音版，老式 IBM 风格的配色，静电容的手感，再加上小巧的体积，很喜欢，在桌面上也非常协调。

![keyboard_hhkb_type_s_1](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/keyboard_hhkb_type_s_1.jpg)

每天早上开始学习、工作前总是先会简单布置一下环境，小心翼翼地放上键盘，而这把键盘陪伴着我从香港到北京，甚至每次外出去咖啡馆也都会带上，刚开始可能只是习惯，慢慢竟变成了一种仪式感，似乎这样让写码和写作都带上了一些乐趣。

![keyboard_hhkb_type_s_2](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/keyboard_hhkb_type_s_2.jpg)

用了一年多后，因为很喜欢静电容的手感，不由得想尝试一下剩下几把经典，于是同样作为礼物，我收到了一把 RealForce PFU 联名版 87 键，这把的颜值也很不错，暗光环境下有种金属感，不过可能是由于习惯了 HHKB 的特殊键位，突然转换到 87 常常有些不适应，所以反倒是给她用来打游戏更多一些，反正键盘也拯救不了我的游戏操作手残。

![realforce_pfu_87](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/realforce_pfu_87.jpg)

RealForce 后来也就闲置了。而自己也确实有些用不习惯大尺寸键盘了，于是寄给了远在澳洲的倪（这么一想我的第一把机械键盘也是他送我的，一把 Cherry 的，但是轴体倒是忘了，当时还在用 Win 的时候在家用了快一年，也很不错）。

虽然 HHKB 和 RealForce 这两把知名度感觉更高一些，但我个人体验下来在誉为静电容三大经典中作工最精致、质感最好的反而是我去年年中才入手的 Leopold FC660C，配色和敲击感都更舒服，真正让人有些享受其中，后续成为了我家里桌面的主力键盘。

![keyboard_leopold_fc660c](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/keyboard_leopold_fc660c.jpg)

其实至此，自己键盘使用的需求已经完全满足了，也没太多心力去追求极致去玩客制化。然而，一个深夜刷到了稚晖君的『[【自制】我做了一把 模 块 化 机 械 键 盘 !【软核】](https://www.bilibili.com/video/BV19V4y1J7Hx)』，一把从电路硬件到固件代码都重新设计定义、自己做的键盘，这谁忍得住啊。

而在国庆的时候，刚好看到和 B 站出了联名款键盘，毫不犹豫下单了，果然猛男粉还是很有吸引力的，这也是我某种意义上的第一把客制化。

![keyboard_hello_word_75](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/keyboard_hello_word_75.jpeg)

接着就是几个月的漫长等待，终于在这一周到了我手上，不得不说颜值和手感都很绝，迅速更换了我的桌面布局，快乐地敲了一周。可能颜值才是第一生产力吧，感觉这周写文章和代码量都上去了，晓瑜表示“怎么换了把键盘你人设都变了喂”。

![chat_with_xiaoyu_about_keyboard](https://pseudoyu.oss-cn-hangzhou.aliyuncs.com/images/chat_with_xiaoyu_about_keyboard.png)

我没有什么收藏癖，也没有想追求极致的手感或是客制化方案，只是我一直对桌面陈设、电脑、键盘和工具软件等会和我朝夕相处的事物有着极大的折腾欲望，哪怕只是几秒速度提升或是一点点心情体验的改善，于我来说也是一件何乐而不为的事。

## 个人生活剪影

### 学习

日语没学...第一周打卡失败！

### 输出

输出这一块，给 GoCN 翻译了一篇『[[译] Go 1.20 新变化！第一部分：语言特性](https://www.pseudoyu.com/en/2023/01/12/golang_120_language_changes/)』；上一篇周报发完认识了不少新朋友，这周也发了不少推讲博客搭建相关的；和少数派约了一篇稿，不过还不知道什么时候写。

### 输入

#### 书籍

- **我的职业是小说家**，这本书从 10 月就开始读了，中间各种事反而落下了一些读书的进度，最近在空余时间慢慢在读，太喜欢村上的讲话风格了，想把他的每本书都补一遍。

#### 动漫

- **灵能百分百**，几年前看过一次，觉得设定有点意思但是并不算太细细品味，最近想着再补一下，第一季有很多主要角色的缘起、羁绊与改变，搞笑日常之余带给人很多想法与思考。第二第三季一口气刷完了，如果说第一季只是描述一些羁绊，第二第三季就给我带来了太多的感动，角色的成长，身边人的变化，尽管是超能力者的设定，却在点滴日常里不断自我否认以及在身边人的影响下自我接纳，最喜欢记者会后 mob 和灵幻的侧身对话场景，情感已经在不言中。
- **文豪野犬**，早有听说，刚开始追。
- **三体**，大概追番剧的心态就是看你还能有什么迷幻操作。