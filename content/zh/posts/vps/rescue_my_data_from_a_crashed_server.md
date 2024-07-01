---
title: "当云服务器崩溃时，我是如何救援重要数据的"
date: 2024-07-01T15:30:00+08:00
draft: false
tags: ["vps", "server", "vps", "linux", "serverless", "self-hosting"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## 前言

周五的时候我在搬瓦工平台购买的 2C2G 服务器突然内核报错，连不上 ssh 也 无法重启。经过了迂回的各种抢救方案，终于救回了一千多张图床的的图片，心有余悸，记录一下救援过程，顺便折腾了一套新的图床方案。

## 服务器救援

这台服务器大约已经稳定运行了一年半，运行了我许多重要服务，还有我博客图床的一千多张无备份的图片通过 Docker Volume 持久化在主机上。

### 服务器宕机

其实我至今仍不知道出了什么问题，早上刚好需要更新服务器上的我运行的 RSSHub 实例的镜像版本，于是想着干脆把所有服务都更新到最新吧，于是一通 `docker pull` 和 `docker-compose` 重启操作，前面的都没什么问题，直到最后一个服务突然启动容器失败，报了一个类似 `not enough space` 的错误，我心想着可能是下载的镜像太多了导致磁盘满了，于是又一通 `docker image prune --all`、`docker volume prune` 和 `docker system prune` 操作，释放出了接近 10G 的空间，重试，依然不行。

作为一个有且仅有一点服务器运维经验的开发来说，我第一反应想到的就是重启，未曾想，这才是一天噩梦的开始。

![uptime_kuma_status](https://image.pseudoyu.com/images/uptime_kuma_status.png)

没想到重启后我的 Uptime Kuma 提醒我所有服务都下线了，也无法再通过 ssh 连上机子了。

![bwg_kernel_panic](https://image.pseudoyu.com/images/bwg_kernel_panic.jpg)

于是赶紧登录到搬瓦工的线上控制台，发现内核报错，无法启动，强制重启也依然不生效，于是先提交了一个工单，并且赶紧求援我的 DevOps 朋友们。

### 拯救数据

![ask_strrl_about_vps](https://image.pseudoyu.com/images/ask_strrl_about_vps.png)

STRRL 说应该 `rootfs` 出现了问题，不过鉴于这种小云厂商并没有提供什么高级启动等额外的功能，只能等官方技术支持处理了，但想到我有一年半毫无备份的图床数据在上面，依然很慌，于是开始想办法抢救数据。

![bwg_vps_snapshot](https://image.pseudoyu.com/images/bwg_vps_snapshot.png)

研究了一下搬瓦工的控制台，发现它提供一个大约每周一次的备份，并且可以一键将备份转为快照，最近的一次在 6.22 日，还好。我首先想到的是直接通过快照恢复机器，如果是我今天的操作导致了什么配置问题，那理应一周前的快照是能正常启动的，于是满怀信心地等待了十几分钟的快照恢复，结果依然报了同样的错误。依然不死心，把 6.15 的备份也恢复了一下，依然不行。

这下意识到了事情的严重性，甚至做好了数据全部丢失的最坏打算，但在等待工单回复时开始检索类似情况，最后发现搬瓦工机器的快照镜像是可以下载的，并找到了一篇「[搬瓦工备份快照镜像文件 .tar.gz 下载解压后打开 .disk 文件查看数据教程](https://www.bandwagonhost.net/7558.html)」。

于是先下载了快照镜像，得到了一个 `.disk` 文件，这个文件应该是一个专属格式，看教程可以通过 Virtual Box 的命令行工具 `vboxmanage convertfromraw` 来进行格式转换，但官网下载后发现并不支持 M 芯片的 Mac，于是又在之前的老 19 款 Intel Mac 上安装并且执行转换，得到了一个 `.vmdk` 文件。

转换完成后将这个 `.vmdk` 作为一个磁盘挂载到 Virtual Box CentOS 虚拟机上，发现依然报同样的错误。

![7zip_format](https://image.pseudoyu.com/images/7zip_format.png)

于是另辟蹊径，发现 [7-Zip](https://arc.net/l/quote/tirhqejc) 软件支持常见虚拟机格式的解压，但客户端只有 Windows 版本。

![x7z_vmdk_x](https://image.pseudoyu.com/images/x7z_vmdk_x.jpg)

虽然按理说可以在 macOS 上使用命令行版本 [p7zip](https://github.com/p7zip-project/p7zip) 来执行，但我解压时会报错，所以又堵住了一条路，想了个曲线救国的方式，通过虚拟机下载了一个 Win11，下载了 7-Zip 软件直接解压成功了。

![fuse_load_img](https://image.pseudoyu.com/images/fuse_load_img.png)

问题又来了，得到的是 `1.img`、`2.img` 这样格式的 Linux 磁盘镜像文件，macOS 上无法加载，又问了我司运维朋友，折腾了一下 fuse 但是还是无法加载。

![ufs_load_img_log](https://image.pseudoyu.com/images/ufs_load_img_log.jpg)

期间倒也是有好消息，在全网搜罗的时候发现了一个数据恢复软件 UFS Explorer，尝试了一下可以正常加载，只是超过 768k 的文件则需要付费，当然没打算，只是看到文件确实是可以识读之后心里就安心了许多，至少数据还在，剩下都是技术问题了。

![bwg_reply](https://image.pseudoyu.com/images/bwg_reply.png)

期间搬瓦工的工单也恢复了，让我重启或重装试试。。。🤣

![str_orbstack_img](https://image.pseudoyu.com/images/str_orbstack_img.png)

放弃了工单沟通，继续抢救我 `img` 中的数据，万能的 STRRL 告诉我 OrbStack 可以启动一个 Linux Machine，然后可以把这个 `img` 作为一个 Linux 磁盘挂载上去。

```bash
sudo losetup -fP 1.img
mkdir /mnt/bwg
sudo mount /dev/loop0 /mnt/bwg
```

通过以上命令成功把我的 `img` 磁盘镜像挂载到了 OrbStack 的 Ununtu 机器上。

![rescue_image_from_bwg_img](https://image.pseudoyu.com/images/rescue_image_from_bwg_img.png)

当我看到我的图片出现在命令行输出结果时，感动得都快流泪了 😭。

```bash
tar -czvf cheverto_chevereto_images.tar.gz cheverto_chevereto_images/
rsync -acvP ./cheverto_chevereto_images.tar.gz pseudoyu@[yu-mac-studio]:~/Downloads/
```

![rsync_service](https://image.pseudoyu.com/images/rsync_service.jpg)

紧接着赶紧打个 `tar` 包，然后通过 `rsync` 传到了我本地的 Mac 上，本机解压后，终于看到了我所有的图片。

### 迁移图床系统至 r2

但由于这一次的遭遇，不再信任服务器单机部署的图床稳定性了，花了半天折腾了一套新的免费图床系统 —— 「[从零开始搭建你的免费图床系统 （Cloudflare R2 + WebP Cloud + PicGo）](https://www.pseudoyu.com/zh/2024/06/30/free_image_hosting_system_using_r2_webp_cloud_and_picgo/)」。

![rclone_service](https://image.pseudoyu.com/images/rclone_service.jpg)

至于现有的数据传到 `r2`，我则是使用了 `rclone` 来进行上传，彻底完成迁移，大功告成！

## 总结

也开始重新考虑了服务部署、数据安全等问题，准备还是将一些重要的数据上云而不再依赖单机，也继续把一些服务迁移到 [fly.io](https://fly.io)[、Zeabur](https://zeabur.com/) 等 serverless 平台。
