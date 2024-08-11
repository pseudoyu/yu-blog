---
title: "Thin Client Development Workflow Based on frp Internal Network Penetration"
date: 2022-07-05T10:00:16+08:00
draft: false
tags: ["frp", "proxy", "network", "dev-environment", "devices", "tools"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="'Here After Us - Mayday'" >}}

## Preface

![leopold_fc660c](https://image.pseudoyu.com/images/leopold_fc660c.jpg)

In my previous project ["GitHub - Personal Toolbox"](https://github.com/pseudoyu/yu-tools), I mentioned that I have a Mac Studio that's always on at home and a Raspberry Pi 3b+ microcomputer running Ubuntu. When at home, I usually operate the Mac Studio connected to a monitor or access it via SSH from my Chromebook terminal.

After ending remote work, I need to commute between the office and home daily. Not wanting to carry a laptop every day, I left my previous 16-inch MacBook Pro main development machine (which is really heavy) at the office for work project development. Although I can synchronize code through GitHub and GitLab, and files through OneDrive and iCloud, I still felt like I was maintaining two desktop development environments every day. Some configuration environment changes required double the workload, bringing a significant mental burden.

Moreover, the M1 Max chip machine at home performs far better than the old Intel MacBook Pro laptop. So, I started to explore solutions for accessing home devices remotely via the public network and practiced a thin client workflow. This article is a record and summary of this workflow.

## Thin Client Workflow

I was inspired by this episode of the ["Teahour"](https://teahour.fm) Podcast: ["#95 - What's it like to develop on a Chromebook?"](https://teahour.fm/95), where I first learned about the thin client development model.

### Basic Concepts

Thin client development is an increasingly popular development model. Its main idea is that the development input devices you use (such as laptops, tablets, etc.) do not install various development environments. Instead, they use terminal, VS Code Remote, or Jetbrains Client and other client programs as entry points to connect to your remote host or server. This method has the following advantages:

1. It can simplify your development environment to the greatest extent. You only need a terminal and a browser to complete most development work, which can reduce device costs. You can even use a Chromebook or iPad to complete daily development work.
2. It reduces office location restrictions. You can carry portable devices and work freely in cafes or other places. Compared to running various development environments locally, this method also has longer battery life.
3. No matter which device you use for development access, you can ensure that your development environment and progress remain consistent, reducing environment synchronization and maintenance costs.
4. Often our development environment is macOS or Windows operating system. Sometimes the local development environment may have some differences from the actual project running environment. Remote development in a Linux system can effectively reduce these differences and improve development efficiency.
5. We can concentrate most of our costs on a relatively powerful device to meet long-term development needs.
6. When there are temporary development needs, we can start and stop some cloud servers as needed, saving costs and improving development efficiency.
7. In fields like Deep Learning that require specific devices such as GPUs for computation, development cannot be done on local machines.

### My Thin Client Workflow

![thin_client_structure](https://image.pseudoyu.com/images/thin_client_structure.png)

To reduce costs, my thin client workflow is mainly based on an internal network penetration solution I set up myself (the scheme principle and setup method will be explained in detail later). It accesses the more powerful host and server at home from various clients in the public network to complete the main development work.

My main devices on the client side are currently:

1. 16-inch MacBook Pro, long-term placement in the office, used as a work machine, mainly for browsing web pages, documents, and connecting to various remote hosts or servers for development work through the iTerm2 terminal tool, and managing code and projects through Git.
2. Google Pixelbook Go, mainly used in coffee shops, on the couch at home, or other places for some technical learning, blog writing, or personal project development.

My servers are divided into the following categories:

1. Mac Studio host, connected to power and always on, is my main server. It is accessible to clients from the public network through internal network penetration. When working or studying at home, it can also be used as a client to connect to other server hosts when connected to a display and keyboard/mouse.
2. Raspberry Pi, installed with Ubuntu system as the main service running and debugging environment, mainly running some services, accessible to clients from the public network through internal network penetration.
3. Personal Alibaba Cloud ECS, Tencent Cloud lightweight server, or other project development environments provided by the company, mainly used for running and debugging some project services, such as chain environments.
4. GitHub Codespaces, participated in the internal test. GitHub provides running environments for up to 10 personal projects. I mainly use it for Solidity, Rust, or front-end learning project development. This way, I can ensure a consistent environment when connecting from different machines or even browsers, without having to reconfigure and set up myself. However, for security considerations, I won't run work projects or some projects involving personal sensitive information.

### My Thin Client Development Experience

The thin client is not just an optimization of tools and techniques; its original intention is a kind of "minimalism" in work mode. After practicing this development mode for several months, I can clearly feel that the time I spend on debugging and maintaining the development environment has decreased, and I've put more attention on the code and services themselves. The seamless switching between "instant use" and "on-demand" modes also allows me to switch work states and projects at any time, greatly reducing time costs such as environment cold start and configuration.

Although I have my own pursuit of software and hardware user experience, I'm not a person who pursues extremes in all aspects. Instead, I follow a "Just Enough" philosophy, satisfying my current usage needs. For example, in terms of network environment, I just have an ordinary 100M broadband network environment at home, and I haven't deliberately tinkered with bandwidth and routers. Overall, whether it's typing input or obtaining real-time display, the network latency during operation is almost negligible (my main usage scenario is using VS Code Remote or iTerm2 terminal tool on macOS system to connect to remote hosts or servers for development via SSH, and occasionally using Termius's SFTP function for file transfer, for reference). There are almost no disconnections due to network environment.

I've only used VNC for remote desktop control when configuring the Raspberry Pi, and haven't performed other operations that are highly dependent on the graphical interface. The network latency is acceptable but not highly recommended.

## Network Remote Access Requirement Analysis

![raspberry_pi](https://image.pseudoyu.com/images/raspberry_pi.jpg)

Regarding the schemes and principles of remote network access, the article ["Remote LAN Access Guide"](https://sspai.com/prime/story/remote-lan-access-guide-01) on Sspai has already detailed and evaluated various schemes. I only consider the ease of use and cost of the scheme according to personal needs. You can read and choose the appropriate scheme yourself.

First, I sorted out the network conditions and requirements.

Network conditions:

1. Short-term broadband casually set up for renting, no public IP provided, applying for one is probably very troublesome.
2. The home wireless router seems to be just an ordinary Xiaomi one, haven't tinkered with it much.
3. Due to work and personal development needs, I have long-term renewed servers on Alibaba Cloud and Tencent Cloud, with public IPs.

Remote connection requirements:

1. Access the Mac Studio host via SSH through the public network, and be able to open specific ports when needed.
2. Access the Raspberry Pi via SSH through the public network, and be able to open specific ports when needed.
3. Require stable and fast connection, and try to reuse existing software and services to avoid additional expenses.
4. Easy to expand new devices (such as purchasing new Raspberry Pis) and configure new port mappings (opening new services).
5. Because the home network is completely managed by Surge as a software router, configurations such as closing DHCP have already been made, so try not to make configurations at the optical modem and router level.
6. Be able to monitor the connection status of the home network environment and the resource status of the Raspberry Pi server in real time.

## frp Internal Network Penetration Solution

After some research, I chose the open-source project ["GitHub - fatedier/frp"](https://github.com/fatedier/frp). According to its official documentation:

> frp is a high-performance reverse proxy application focusing on intranet penetration. It supports multiple protocols like TCP, UDP, HTTP, HTTPS. It can securely and conveniently expose intranet services to the public network through nodes with public IP. By deploying frp server on nodes with public IP, intranet services can be easily penetrated to the public network, while providing many professional functional features.

This perfectly meets my needs. I only need to reuse my purchased Alibaba Cloud server with a public IP as a transit server, deploy the frp server, expose the corresponding ports, deploy the frp client on home devices that need to be accessed from the public network and perform port mapping, to achieve internal network penetration.

### Solution Architecture

![frp_structure](https://image.pseudoyu.com/images/frp_structure.png)

First, I deployed the frp server on my server with a public IP and exposed the corresponding ports.

In my home intranet environment, there are mainly two devices that are always connected to power and turned on, a Mac Studio host and a Raspberry Pi server with Ubuntu operating system, mainly connected to the wireless router via network cable/Wi-Fi. I installed and ran the frp client on both machines according to the official instructions, configured to connect to the frp server, and mapped the service ports that need to be opened (such as mapping the SSH service port 22 of the Raspberry Pi to port 6002 of the Alibaba Cloud server). It's worth mentioning that because the frp client actively sends requests to the server, there's no need to reconfigure even if the network environment changes, as long as its network environment can access the transit server where the frp server is installed.

At this point, my Alibaba Cloud transit server can expose our intranet environment and services to the public network environment. When I'm at the office, I can use a laptop, tablet, or phone to access through the public network of the Alibaba Cloud server + the corresponding service port, such as remotely SSH connecting to Mac Studio for development work via terminal.

At the same time, we want to monitor the status of the home network environment and the two hosts in real time for maintenance. I used the Surge macOS client as a software router to manage all devices in the home network, and used the cloud notification function of the Surge iOS client to monitor the home network status in real time. In addition, I used the ServerCat software to monitor the resources of the Raspberry Pi server at home, even down to the temperature, which is no different from the cloud server experience.

![servercat_monitor_raspberry_pi](https://image.pseudoyu.com/images/servercat_monitor_raspberry_pi.png)

The configuration of frp is relatively simple, just follow the official documentation. My configuration process is as follows.

### frp Server Configuration

My Alibaba Cloud is installed with CentOS operating system, other Linux distributions are similar.

#### Service Installation and Configuration

First log in to the terminal of the Alibaba Cloud server, and install and download the frp program through the following commands (note that you need to download the version corresponding to your operating system from the [releases](https://github.com/fatedier/frp/releases) page of the ["GitHub - fatedier/frp"](https://github.com/fatedier/frp) project, decompress and enter the directory.

```bash
wget https://github.com/fatedier/frp/releases/download/v0.43.0/frp_0.43.0_linux_amd64.tar.gz
tar -zxvf frp_0.43.0_linux_amd64.tar.gz
cd frp_0.43.0_linux_amd64/
```

The `frps` and `frps.ini` are the files we need to focus on. `frps` is the server program, while `frps.ini` is the corresponding configuration file. We use `vi frps.ini` to edit the configuration file:

```plaintext
[common]
bind_port = 7000
dashboard_port = 7002
token = password
dashboard_user = admin
dashboard_pwd = 123456
vhost_http_port = 8080
```

Because I want to visualize the operation of our frp service through the console, I also configured dashboard-related parameters, which you can choose according to your own needs. Save or remember this configuration, as it will be needed later when connecting the frp client to the server. After saving the configuration, you can start the server with `./frps -c frps.ini`.

Of course, we need to configure it to start automatically and run in the background to avoid having to reconfigure every time the server restarts.

```bash
vi /lib/systemd/system/frps.service
```

Add the following content and save, note that you need to change the paths of `frps` and `frps.ini` to your actual paths.

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

#### Service Start and Boot Auto-start Configuration

After completing the configuration, you can start the server with `systemctl start frps`.

We enter the following command in the command line to configure the service to start automatically at boot:

```bash
systemctl enable frps
```

At this point, our server configuration is complete.

### frp Client Configuration

#### Service Installation and Configuration

The frp client configuration is similar to the server configuration. Download the corresponding version of the frp program through the `wget` command, decompress and enter the directory.

```bash
wget https://github.com/fatedier/frp/releases/download/v0.43.0/frp_0.43.0_linux_amd64.tar.gz
tar -zxvf frp_0.43.0_linux_amd64.tar.gz
cd frp_0.43.0_linux_amd64/
```

The `frpc` and `frpc.ini` are the files we need to focus on. `frpc` is the client program, while `frpc.ini` is the corresponding configuration file. We use `vi frpc.ini` to edit the configuration file:

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

The `server_addr` and `server_port` here need to be filled with the actual public IP and port of the transit server, and `token` needs to be filled with the token configured earlier; below is the port mapping configuration for the service you need to connect, `local_ip` and `local_port` need to be filled with the local IP and port of the client, such as `127.0.0.1` and `22` if you need to enable SSH service, while the last `remote_port` is the port mapping of this port in the transit server.

#### Service Start and Boot Auto-start Configuration

##### Ubuntu

In the Ubuntu system of the Raspberry Pi, we create or edit the fprc service configuration file through `vi /etc/systemd/system/frpc.service`, add the following content and save, similarly, you need to modify `fprc` and `fprc.ini` to your actual paths.

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

After completing the configuration, enable service auto-start with `sudo systemctl enable frpc.service`, and start the client service with `sudo systemctl start frpc.service`.

##### macOS

In the macOS system, we edit the plist through `vi ~/Library/LaunchAgents/frpc.plist` to add service auto-start, similarly, you need to modify `fprc` and `fprc.ini` to your actual paths.

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

At this point, we can access our intranet services through the corresponding ports of the transit server in the public network environment, and the services will start automatically at boot, whether on the server side or the client side. We can access the frp console through `<public IP>` + the `dashboard_port` port we just configured on the server side to view the traffic situation of each service.

![frp_dashboard](https://image.pseudoyu.com/images/frp_dashboard.png)

## Conclusion

The above is my practice and summary of public network remote access to home devices and thin client workflow. This brings an interesting development experience that is different from the traditional mode. Interested readers can try it themselves. I hope this article is helpful to you.

## References

> 1. [GitHub - fatedier/frp](https://github.com/fatedier/frp)
> 2. [Teahour #95 - What's it like to develop on a Chromebook?](https://teahour.fm/95)