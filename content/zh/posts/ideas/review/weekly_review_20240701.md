---
title: "周报 #63 - 抢救服务器数据、博客的变化与人的 AI 化现象"
date: 2024-07-01T08:30:00+08:00
draft: true
tags: ["review", "life", "blog", "vps", "ai"]
categories: ["Ideas"]
authors:
- "pseudoyu"
---

{{<audio src="audios/photograph.mp3" caption="《Photograph - Ed Sheeran》" >}}

## 前言

本篇是对 `2024-06-24` 到 `2024-06-30` 这周生活的记录与思考。

周五的时候服务器突然 Kernel Panic，无法重启，经过了迂回的各种抢救方案，终于救回了一千多张图床的的图片，心有余悸，顺便折腾了一套新的图床方案；想到上一次写博客搭建教程已经是两年多前，不论是内容还是组件都经过了许多变化，于是重新开启系列；一次不愉快的买花和维权体验，思考了 AI 越来越拟人化的现在，人却似乎变得 AI 化了的现象。

## 抢救服务器

这周最惊魂未定的经历就是稳定运行了一年半的搬瓦工服务器突然内核报错无法启动。

服务器上运行了我许多重要服务，还有我博客图床的一千多张无备份的图片通过 Docker Volume 持久化在主机上，经历了非常跌宕起伏的抢救过程，最终抢救数据成功 🥳。

### 起因

其实我至今不知道出了什么问题，早上刚好需要更新服务器上的我运行的 RSSHub 示例的镜像版本，于是想着干脆把所有服务都更新到最新把，于是一通 `docker pull` 和 `docker-compose` 重启操作，前面的都没什么问题，直到最后一个服务突然启动容器失败，报了一个 `not enough space` 的错误，我心想着可能是下载的镜像太多了导致磁盘满了，于是又一通 `docker image prune --all`、`docker volume prune` 和 `docker system prune` 操作，释放除了接近 10G 的空间，重试，依然不行。

作为一个有且仅有一点服务器运维经验的开发来说，我第一反应想到的就是重启，未曾想，这才是一天噩梦的开始。

![uptime_kuma_status](https://image.pseudoyu.com/images/uptime_kuma_status.png)

没想到重启后我的 Uptime Kuma 提醒我所有服务都下线了，也无法再通过 ssh 连上机子了。

![bwg_kernel_panic](https://image.pseudoyu.com/images/bwg_kernel_panic.jpg)

于是赶紧登录到搬瓦工的线上控制台，发现内核报错，无法启动，强制重启也依然不生效，于是先提交了一个工单，并且赶紧求援我的 devOps 朋友们。

![ask_strrl_about_vps](https://image.pseudoyu.com/images/ask_strrl_about_vps.png)

STRRL 说应该 `rootfs` 出现了问题，不过鉴于这种小云厂商并没有提供什么高级启动等额外的功能，只能等官方技术支持处理了，但想到我有一年半毫无备份的图床数据在上面，依然很慌，于是开始想办法抢救数据。

![bwg_vps_snapshot](https://image.pseudoyu.com/images/bwg_vps_snapshot.png)

研究了一下搬瓦工的控制台，发现它提供一个大约每周一次的，并且可以一键将备份转为快照，最近的一次在 6.22 日，还好。我首先想到的是直接通过快照恢复机器，如果是我今天的操作导致了什么配置问题，那理应一周前的快照是能正常启动的，于是满怀信心地等待了十几分钟的快照恢复，结果依然报了同样的错误。依然不死心，把 6.15 的备份也恢复了一下，依然不行。

这下意识到了事情的严重性，甚至做好了数据全部丢失的最坏打算，但在等待工单回复时开始检索类似情况，最后发现搬瓦工机器的快照镜像是可以下载的，并找到了一篇「[搬瓦工备份快照镜像文件 .tar.gz 下载解压后打开 .disk 文件查看数据教程](https://www.bandwagonhost.net/7558.html)」。

于是先下载了快照镜像，得到了一个专属的 `.disk` 文件，这个文件应该是一个专属格式，看教程可以通过 Virtual Box 的命令行工具 `vboxmanage convertfromraw` 来进行格式转换，但官网下载后发现并不支持 M 芯片的 mac，

## 有趣的事与物

### 输入

虽然大部分有意思的输入会在 「[Yu's Life](https://t.me/pseudoyulife)」 Telegram 频道里自动同步，不过还是挑选一部分在这里列举一下，感觉更像一个 newsletter 了。

#### 书籍

- [**索拉里斯星**](https://book.douban.com/subject/35049755/)，与三体的设定类似，索拉里斯星围绕着双星旋转，但是不同于三体的降临或是拯救，索拉里斯星其实或许根本并不关心地球和上面渺小的人类，只是人类单向的自我中心罢了，甚至想用自己更为“高尚”的思想与价值观去改变它，探索也不过只是伪善。。
- [**Normal People**](https://book.douban.com/subject/34453257/)，很喜欢这个英剧，这两天看其他书的时候突然想到了这本，打算补一下原著。
- [**What My Bones Know**](https://book.douban.com/subject/35754687/)，去年看了一小半，这两天想到关于家庭和心理疗愈的问题，就睡前又翻了几页。
- [**阿特拉斯耸耸肩**](https://book.douban.com/subject/33445309/)，读者送的，开始读了。

#### 收藏

- [CS193p - Developing Apps for iOS](https://cs193p.sites.stanford.edu/2023)
- [SwiftUI Tutorials | Apple Developer Documentation](https://developer.apple.com/tutorials/swiftui)

#### 文章

- [How I Use Obsidian](https://macwright.com/2024/06/16/how-i-use-obsidian)
- [给 Hugo 博客的代码区块更换主题](https://blog.douchi.space/blog-code-syntax-highlighting/)

#### 视频

- [vlog #60｜女程序员下班后的学习记录｜啃 Celestia 的文档｜Modular Blockchain｜英语日常练习｜桌面小装修｜入手了新设备](https://www.bilibili.com/video/BV1Jr421F7W9)
- [《博德之门 3》青出于蓝，变革虽大但在某个方面其实是完美的延续【就知道玩游戏】](https://www.bilibili.com/video/BV1CS411A7xw)
- [vlog #61｜女程序员下班后的学习记录｜状态混乱就快去学习吧｜RUST｜在读《被讨厌的勇气》｜运动带给我的变化｜日常英语学习｜TEDTalk](https://www.bilibili.com/video/BV1L1421k7bK)
