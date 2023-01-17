---
title: "基于 frp 内网穿透的瘦客户端开发工作流"
date: 2022-07-05T10:00:16+08:00
draft: false
tags: ["frp", "proxy", "network", "dev-environment", "devices", "tools"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

![leopold_fc660c](https://image.pseudoyu.com/images/leopold_fc660c.jpg)

在之前的『[GitHub - 个人工具箱](https://github.com/pseudoyu/yu-tools)』项目中，我提到家里放置了一台长期开机的 Mac Studio 和一个装了 Ubuntu 系统的 Raspberry Pi 3b+ 微型树莓派设备，在家时我通常是将 Mac Studio 连接显示器进行操作或通过 Chromebook 终端 SSH 连接访问。

结束居家办公后，需要每天往返于公司与家里。因为不想每天背着电脑通勤，我将之前的 16 寸 MacBook Pro 主力开发机（真的很重）留在了公司用于工作项目开发使用。虽然可以通过 GitHub 与 GitLab 同步代码，以及通过 OneDrive 与 iCloud 同步文件，每天总还是觉得是在维护两套桌面开发环境，有些配置环境的变更需要双倍的工作量，带来了很大的心智负担。

此外，家里的 M1 Max 芯片机器性能远好于老 Intel MacBook Pro 笔记本，于是，我开始琢磨公网远程访问家庭设备的方案，并实践一种瘦客户端工作流，本文是对这套工作流的一个记录与总结。

## 瘦客户端（thin client）工作流

被『[Teahour](https://teahour.fm)』Podcast 的这期『[#95 - 用 Chromebook 做开发是什么样的体验？](https://teahour.fm/95)』种草，第一次了解到了瘦客户端（thin client）开发这种模式。

### 基本概念

瘦客户端开发是一种日渐流行的开发模式，它的主要理念是自己所使用的开发输入设备（如笔记本、平板电脑等）上并不安装各种开发环境，而是通过终端、VS Code Remote 或 Jetbrains Client 等客户端程序作为入口来连接自己的远程主机或服务器。这种方式有如下好处：

1. 可以最大程度简化自己的开发环境，只需要一个终端和一个浏览器即可完成大部分开发工作，可以降低设备成本，甚至使用 Chromebook 或 iPad 即可完成日常开发工作
2. 减少办公场所的限制，可以携带便携设备在咖啡厅或其他场合自由使用，比起本机运行各种开发环境，这种方式也拥有更久的续航
3. 不论从哪个设备上进行开发访问，都能确保自己的开发环境与进度保持一致，降低环境同步与维护成本
4. 往往我们的开发环境为 macOS 或 Window 操作系统，有时本地开发环境会与实际项目运行环境存在一定差异，而在 Linux 系统进行远程开发可以有效降低这种差异，提高开发效率
5. 我们可以将大多数的成本集中在一台性能较为强劲的设备，满足长期开发需求
6. 在有临时的开发需求时，我们可以随开随停一些云服务器，节约成本并提升开发效率
7. 像 Deep Learning 等领域需要使用 GPU 等特定设备进行运算，无法在本地机器进行开发

### 我的瘦客户端工作流

![thin_client_structure](https://image.pseudoyu.com/images/thin_client_structure.png)

为了降低成本，我的瘦客户端工作流主要基于我自己所搭建的一套内网穿透方案（下文会详细讲述方案原理及搭建方法），在公网中从各个 Client 访问家里性能较强的主机与 Server，完成主要开发工作。

我目前 Client 端的主要设备为：

1. 16 寸 MacBook Pro，长期放在公司，作为工作机使用，主要用于浏览网页、文档以及通过 iTerm2 终端工具连接到各个远程主机或 Server 进行开发工作，并通过 Git 管理代码与项目
2. Google Pixelbook Go，主要是在咖啡店、家中沙发或其他地方进行一些技术学习、博客撰写或个人项目开发

而我的 Server 端分以下几类：

1. Mac Studio 主机，连接电源长期开机，是我的主力 Server，通过内网穿透供客户端从公网连接访问，在家办公或学习时连接显示器与键鼠也可以作为客户端连接其他服务器主机
2. Raspberry Pi，装了 Ubuntu 系统作为主要服务运行与调试环境，主要运行一些服务，通过内网穿透供客户端从公网连接访问
3. 个人阿里云 ECS、腾讯云轻量级服务器或其他公司提供的项目开发环境，主要用于一些项目服务的运行与调试，如链环境等
4. GitHub Codespaces，参加了内测，GitHub 为个人项目提供多达 10 个项目的运行环境，我主要用于 Solidity、Rust 或前端学习项目的开发，这样可以保障在不同机器甚至浏览器连接时保持一致的环境，不需要自己重新配置搭建，不过出于安全性考虑我不会运行工作项目或一些涉及个人敏感信息的项目

### 我的瘦客户端开发工作体验

瘦客户端并不仅仅是一种工具技巧上的优化，其初衷本就是一种工作模式的“极简主义”。践行了几个月这样的开发模式，能明显感觉到自己用于开发环境调试与维护的时间减少了，而将更多的注意力放在代码与服务本身，“即开即用”与“随开随停”两种模式的无缝切换也让自己可以时刻切换工作状态与项目，极大减少了环境冷启动、配置等时间成本。

虽然我对软硬件有着自己的使用体验追求，但并不是一个方方面面都追求极致的人，而是遵循着一种“Just Enough”的理念，满足我的当下使用需求即可。例如网络环境方面，我家中就是普通的 100M 宽带网络环境，也并未在带宽与路由器上有刻意折腾。整体体验下来，不管是打字输入还是获取实时显示，操作过程中的网络延迟几乎可以忽略不计（我的主要使用场景为使用 macOS 系统下的 VS Code Remote 或 iTerm2 终端工具，通过 SSH 连接至远程主机或服务器进行开发，以及偶尔使用 Termius 的 SFTP 功能进行文件传输，可供参考），也几乎没有因网络环境而断连的情况。

我仅在配置树莓派时使用过 VNC 进行远程桌面控制，并未进行其他高度依赖于图形界面的操作，网络延迟尚可接受但并不是很建议。

## 网络远程访问需求分析

![raspberry_pi](https://image.pseudoyu.com/images/raspberry_pi.jpg)

关于异地网络访问的方案与原理，少数派的这篇『[异地网络远程访问指北](https://sspai.com/prime/story/remote-lan-access-guide-01)』中已经对各个方案进行了详细的叙述与评估，我仅仅按照个人需求从方案易用性、费用等维度进行考虑，大家可自行阅读选取适合的方案。

首先，我整理了一下网络条件与需求。

网络条件：

1. 租房随便办的短期宽带，没有提供公网 ip，申请估计也很麻烦
2. 家庭无线路由器好像也是小米一个普通的，没有怎么折腾
3. 因为工作和个人开发需要，在阿里云和腾讯云都有服务器长期续费，有公网 ip

远程连接需求：

1. 通过公网 SSH 访问 Mac Studio 主机，并能够在有需求的时候开放特定端口
2. 通过公网 SSH 访问树莓派，并能够在有需求的时候开放特定端口
3. 要求连接稳定快速，且尽量复用已有软件与服务，避免额外开支
4. 易于拓展新设备（如购入新的树莓派）与配置新端口映射（开放新的服务）
5. 因为家里的网络完全由 Surge 作为软路由托管，已经进行了关闭 DHCP 等配置，因此尽量不要在光猫与路由器层作配置
6. 能够对家庭网络环境连接情况与树莓派 Server 资源情况进行实时监控

## frp 内网穿透方案

经过一番调研，我选择了开源项目『[GitHub - fatedier/frp](https://github.com/fatedier/frp)』，根据其官方文档描述：

> frp 是一个专注于内网穿透的高性能的反向代理应用，支持 TCP、UDP、HTTP、HTTPS 等多种协议。可以将内网服务以安全、便捷的方式通过具有公网 IP 节点的中转暴露到公网。通过在具有公网 IP 的节点上部署 frp 服务端，可以轻松地将内网服务穿透到公网，同时提供诸多专业的功能特性。

这完美满足了我的需求，我仅仅需要复用自己购置的具有公网 ip 的阿里云服务器作为中转服务器，部署 frp 服务端，暴露对应端口，在需要从公网访问的家庭设备中部署 frp 客户端并进行端口映射，即可实现内网穿透。

### 方案架构

![frp_structure](https://image.pseudoyu.com/images/frp_structure.png)

首先，我在自己有公网 ip 的服务器上部署了 frp 服务端并暴露了对应的端口。

我家中的内网环境下主要有两台长期连接电源开机的设备，一台 Mac Studio 主机，一台装了 Ubuntu 操作系统的树莓派 Server，主要通过网线/Wifi 连接至无线路由器。我在两台机器分别按照官方说明安装了运行了 frp 客户端，通过配置连接至 frp 服务端，并对 SSH 等需要开启的服务端口映射（如将树莓派的 SSH 服务端口 22 映射到阿里云服务器的 6002）。值得一提的是，因为 frp 客户端会主动发送请求服务端，因此即使更换了网络环境也无需重新配置，仅需要保证其网络环境能访问到安装了 frp 服务端的中转服务器即可。

此时，我的阿里云中转服务器已经可以将我们的内网环境与服务暴露在公网环境中了。当我在公司时，就可以使用笔记本、平板或手机通过阿里云服务器的公网+对应服务的端口进行访问了，如通过终端远程 SSH 连接至 Mac Studio 进行开发工作。

同时，我们会想对家里的网络环境以及两台主机的状态进行实时监控，以便于维护。我使用了 Surge macOS 端作为软路由托管了家中所有设备的网络，并使用了 Surge iOS 端的云通知功能，对家庭的网络状态进行实时监控。此外，我使用了 ServerCat 软件对家中的树莓派 Server 进行资源监控，甚至可以精确到温度等，与云服务器体验无异。

![servercat_monitor_raspberry_pi](https://image.pseudoyu.com/images/servercat_monitor_raspberry_pi.png)

frp 的配置比较简单，按照官方文档进行配置即可，我的配置流程如下。

### frp 服务端配置

我的阿里云装了 CentOS 操作系统，其他 Linux 发行版也大同小异。

#### 服务安装与配置

首先登录阿里云服务器的终端，通过以下命令安装下载 frp 程序（注意，需要根据自己的操作系统从『[GitHub - fatedier/frp](https://github.com/fatedier/frp)』项目的 [releases](https://github.com/fatedier/frp/releases) 页面下载自己操作系统对应的版本、解压并进入目录。

```bash
wget https://github.com/fatedier/frp/releases/download/v0.43.0/frp_0.43.0_linux_amd64.tar.gz
tar -zxvf frp_0.43.0_linux_amd64.tar.gz
cd frp_0.43.0_linux_amd64/
```

其中的 `frps` 与 `frps.ini` 是我们需要关注的文件。`frps` 即服务端程序，而 `frps.ini` 则为对应的配置文件。我们使用 `vi frps.ini` 编辑配置文件：

```plaintext
[common]
bind_port = 7000
dashboard_port = 7002
token = password
dashboard_user = admin
dashboard_pwd = 123456
vhost_http_port = 8080
```

因为我想通过控制台可视化我们的 frp 服务的运行状况，因此同时还配置了 dashboard 相关参数，可以根据自己的需要进行选择，保存或记住本配置，后续使用 frp 客户端连接服务端时需要与之对应。保存配置后即可通过 `./frps -c frps.ini` 启动服务端。

当然，我们需要配置其开启自启与后台运行，以免每次重启服务器都需要重新配置。

```bash
vi /lib/systemd/system/frps.service
```

添加如下内容并保存，注意需要将 `frps` 与 `frps.ini` 的路径改为自己的实际路径。

```plaintext
[Unit]
Description=frps service
After=network.target syslog.target
Wants=network.target

[Service]
Type=simple
ExecStart=/path/to/frps -c /path/to/frps.ini

[Install]
WantedBy=multi-user.target
```

#### 服务启动与开机自启配置

完成配置后，即可通过 `systemctl start frps` 启动服务端。

我们在命令行键入以下命令配置服务开机自启：

```bash
systemctl enable frps
```

至此，我们的服务端配置完毕。

### frp 客户端配置

#### 服务安装与配置

frp 客户端配置和服务端配置类似，通过 `wget` 命令下载对应版本的 frp 程序，解压并进入目录。

```bash
wget https://github.com/fatedier/frp/releases/download/v0.43.0/frp_0.43.0_linux_amd64.tar.gz
tar -zxvf frp_0.43.0_linux_amd64.tar.gz
cd frp_0.43.0_linux_amd64/
```

其中的 `frpc` 与 `frpc.ini` 是我们需要关注的文件。`frpc` 即客户端程序，而 `frpc.ini` 则为对应的配置文件。我们使用 `vi frpc.ini` 编辑配置文件：

```plaintext
[common]
server_addr = 114.114.114.114
server_port = 7000
token = password

[pi]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6001
```

此处的 `server_addr` 和 `server_port` 需填写实际的中转服务器的公网 ip 与端口，`token` 需填写之前配置的 token；下面为自己的需要连接的服务配置端口映射，`local_ip` 与 `local_port` 需填写客户端的本地 ip 与端口，如需要开启 SSH 服务则为 `127.0.0.1` 与 `22`，而最后的 `remote_port` 则为该端口在中转服务器中的端口映射。

#### 服务启动与开机自启配置

##### Ubuntu

在树莓派的 Ubuntu 系统中，我们通过 `vi /etc/systemd/system/frpc.service` 新建或编辑 fprc 服务配置文件，添加如下内容并保存，同样，需要将 `fprc` 与 `fprc.ini` 修改为自己的实际路径。

```plaintext
[Unit]
Description=frpc daemon
After=syslog.target  network.target
Wants=network.target

[Service]
Type=simple
ExecStart=/path/to/frpc -c /path/to/frpc.ini
Restart= always
RestartSec=1min
ExecStop=/usr/bin/killall frpc

[Install]
WantedBy=multi-user.target
```

完成配置后，通过 `sudo systemctl enable frpc.service` 开启服务自启，通过 `sudo systemctl start frpc.service` 启动客户端服务。

##### macOS

而在 macOS 系统中，我们则通过 `vi ~/Library/LaunchAgents/frpc.plist` 编辑 plist 来添加服务自启，同样需要将 `fprc` 与 `fprc.ini` 修改为自己的实际路径。

```plaintext
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST 1.0//EN
http://www.apple.com/DTDs/PropertyList-1.0.dtd >
<plist version="1.0">
<dict>
<key>Label</key>
<string>frpc</string>
<key>ProgramArguments</key>
<array>
<string>/path/to/frpc</string>
<string>-c</string>
<string>/path/to/frpc.ini</string>
</array>
<key>KeepAlive</key>
<true/>
<key>RunAtLoad</key>
<true/>
</dict>
</plist>
```

至此，我们就可以在公网环境下通过中转服务器的对应端口了解到我们的内网服务了，且不论是服务端还是客户端，服务都会开机自启。我们可以通过 `<公网 ip>` + 刚在服务端配置的 `dashboard_port` 端口访问 frp 控制台，查看各服务流量情况。

![frp_dashboard](https://image.pseudoyu.com/images/frp_dashboard.png)

## 总结

以上就是我对公网远程访问家庭设备与瘦客户端工作流的实践与总结，这带来了一种很有趣的、有别于传统模式的开发体验，有兴趣的同学可以自行尝试。希望本文对你有所帮助。

## 参考资料

> 1. [GitHub - fatedier/frp](https://github.com/fatedier/frp)
> 2. [Teahour #95 - 用 Chromebook 做开发是什么样的体验？](https://teahour.fm/95)
