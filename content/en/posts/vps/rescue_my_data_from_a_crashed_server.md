---
title: "How I Rescued Critical Data When My Cloud Server Crashed"
date: 2024-07-01T15:30:00+08:00
draft: false
tags: ["vps", "server", "vps", "linux", "serverless", "self-hosting"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

## Preface

On Friday, my 2C2G server purchased from BandwagonHost suddenly reported a kernel error, making it impossible to connect via SSH or restart. After a series of circuitous rescue attempts, I finally managed to salvage over a thousand images from my image hosting service. Still shaken by the experience, I'd like to document the rescue process and, incidentally, discuss the new image hosting solution I've set up.

## Server Rescue

This server had been running stably for about a year and a half, hosting many of my critical services, including over a thousand irreplaceable images for my blog's image hosting service, persistently stored on the host via Docker Volume.

### Server Downtime

To this day, I'm still uncertain about what exactly went wrong. That morning, I needed to update the image version of my RSSHub instance running on the server. I thought I might as well update all services to their latest versions. So, I ran a series of `docker pull` and `docker-compose` restart operations. Everything seemed fine until the last service suddenly failed to start its container, reporting an error similar to `not enough space`. I assumed that downloading too many images might have filled up the disk, so I ran a series of `docker image prune --all`, `docker volume prune`, and `docker system prune` commands, freeing up nearly 10GB of space. I tried again, but it still didn't work.

As a developer with only a smidgen of server maintenance experience, my first instinct was to restart. Little did I know, this would mark the beginning of a day-long nightmare.

![uptime_kuma_status](https://image.pseudoyu.com/images/uptime_kuma_status.png)

After the restart, my Uptime Kuma alerted me that all services were offline, and I could no longer connect to the machine via SSH.

![bwg_kernel_panic](https://image.pseudoyu.com/images/bwg_kernel_panic.jpg)

I quickly logged into BandwagonHost's online console, only to discover a kernel error preventing startup. Even a forced restart proved ineffective. I immediately submitted a support ticket and reached out to my DevOps friends for help.

### Data Rescue

![ask_strrl_about_vps](https://image.pseudoyu.com/images/ask_strrl_about_vps.png)

STRRL suggested that there might be an issue with the `rootfs`. However, given that this small cloud provider doesn't offer advanced boot options or other additional features, we could only wait for official technical support. Still, the thought of losing a year and a half's worth of unbackup image hosting data made me anxious, so I started looking for ways to rescue the data.

![bwg_vps_snapshot](https://image.pseudoyu.com/images/bwg_vps_snapshot.png)

After investigating BandwagonHost's console, I found that they provide weekly backups that can be instantly converted into snapshots. The most recent one was from June 22nd, which was fortunate. My first thought was to restore the machine directly from the snapshot. If today's operations had caused some configuration issue, then a snapshot from a week ago should boot normally. Full of hope, I waited about ten minutes for the snapshot restoration, only to encounter the same error. Still not giving up, I tried restoring the June 15th backup as well, but to no avail.

At this point, I realized the gravity of the situation and even prepared for the worst-case scenario of losing all data. While waiting for a response to my support ticket, I started searching for similar cases and eventually discovered that BandwagonHost's snapshot images can be downloaded. I found an article titled "Tutorial on downloading, unzipping, and viewing data from BandwagonHost backup snapshot image files .tar.gz and .disk files."

So, I downloaded the snapshot image and obtained a `.disk` file. This file seemed to be in a proprietary format. According to the tutorial, it can be converted using Virtual Box's command-line tool `vboxmanage convertfromraw`. However, after downloading from the official website, I found it doesn't support M-chip Macs. So, I installed and executed the conversion on my old 2019 Intel Mac, resulting in a `.vmdk` file.

After the conversion, I mounted this `.vmdk` as a disk on a Virtual Box CentOS virtual machine, only to encounter the same error.

![7zip_format](https://image.pseudoyu.com/images/7zip_format.png)

So, I tried a different approach and found that the [7-Zip](https://arc.net/l/quote/tirhqejc) software supports extracting common virtual machine formats, but the client is only available for Windows.

![x7z_vmdk_x](https://image.pseudoyu.com/images/x7z_vmdk_x.jpg)

Although theoretically, I could use the command-line version [p7zip](https://github.com/p7zip-project/p7zip) on macOS, I encountered errors during extraction. So, that avenue was blocked too. I came up with a roundabout solution: I downloaded a Win11 virtual machine, installed the 7-Zip software, and successfully extracted the files.

![fuse_load_img](https://image.pseudoyu.com/images/fuse_load_img.png)

Another problem arose: the resulting files were Linux disk image files in `1.img`, `2.img` format, which couldn't be loaded on macOS. I asked my company's operations team, tried fiddling with fuse, but still couldn't load them.

![ufs_load_img_log](https://image.pseudoyu.com/images/ufs_load_img_log.jpg)

There was some good news during this time. While scouring the internet, I discovered a data recovery software called UFS Explorer. I tried it and found it could load the files normally, except that files over 768k required a paid version. Of course, I didn't intend to pay, but seeing that the files were indeed readable gave me peace of mind. At least the data was there; the rest was just a technical problem.

![bwg_reply](https://image.pseudoyu.com/images/bwg_reply.png)

Meanwhile, BandwagonHost responded to my ticket, suggesting I try restarting or reinstalling... 🤣

![str_orbstack_img](https://image.pseudoyu.com/images/str_orbstack_img.png)

Giving up on ticket communication, I continued trying to rescue my data from the `img` file. The ever-resourceful STRRL told me that OrbStack can start a Linux Machine, and I could mount this `img` as a Linux disk.

```bash
sudo losetup -fP 1.img
mkdir /mnt/bwg
sudo mount /dev/loop0 /mnt/bwg
```

Using these commands, I successfully mounted my `img` disk image to the OrbStack Ubuntu machine.

![rescue_image_from_bwg_img](https://image.pseudoyu.com/images/rescue_image_from_bwg_img.png)

When I saw my images appear in the command line output, I was almost moved to tears 😭.

```bash
tar -czvf cheverto_chevereto_images.tar.gz cheverto_chevereto_images/
rsync -acvP ./cheverto_chevereto_images.tar.gz pseudoyu@[yu-mac-studio]:~/Downloads/
```

![rsync_service](https://image.pseudoyu.com/images/rsync_service.jpg)

I quickly created a `tar` package and transferred it to my local Mac using `rsync`. After extracting it locally, I finally saw all my images.

### Migrating the Image Hosting System to r2

However, due to this experience, I no longer trust the stability of server-based image hosting. I spent half a day setting up a new free image hosting system — "Building Your Free Image Hosting System from Scratch (Cloudflare R2 + WebP Cloud + PicGo)".

![rclone_service](https://image.pseudoyu.com/images/rclone_service.jpg)

As for uploading existing data to `r2`, I used `rclone` to complete the migration. Mission accomplished!

## Conclusion

I've started reconsidering issues of service deployment and data security. I plan to move some important data to the cloud rather than relying on single machines, and continue migrating some services to serverless platforms like [fly.io](https://fly.io) and [Zeabur](https://zeabur.com/).
