---
title: "通过 mover.io 服务无缝迁移云端网盘文件至 OneDrive"
date: 2022-05-22T13:06:12+08:00
draft: false
tags: ["data", "mover.io", "onedrive", "google drive"]
categories: ["Tools"]
authors:
- "Arthur"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

最近学校发了邮件说要把邮箱服务从 Google 转移到 Microsoft，而且原先的 Google Drive 无限流量也将取消，转移为 5T 的 OneDrive。我原先一直用着 Google Drive 的文件服务，在我的多个设备之间同步和备份文件，到现在也差不多占了 300 多 GB 的空间。因为 Google Drive 在内地需要代理，下载速度很慢，因此，我采用了官方推荐的 [mover.io](https://mover.io) 服务来进行云端迁移，无需下载到本地转存，记录一下迁移过程。

## mover.io 服务

![mover_io](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_io.png)

mover.io 服务是微软提供的一个网盘迁移服务，支持将很多云服务商提供的网盘文件迁移到 Microsoft OneDrive 上，比如 Google Drive、Dropbox、Box 等。它为机构、学校以及个人都提供了迁移服务。

对于个人用户，我们使用 Transfer Wizard 来进行迁移。

![mover_transfer_wizard](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_transfer_wizard.png)

## 迁移流程

### 注册/登录 mover.io 账户

首先，我们需要注册一个 mover.io 账户，并登录，可以使用 Microsoft 授权登录或使用原来的 mover.io 账户。

![mover_io_login](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_io_login.png)

### 授权迁移数据源

登录成功后，界面清晰地给出了操作说明，按照步骤操作即可。

![mover_transfer_wizard_setting](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_transfer_wizard_setting.png)

#### 选择迁移来源

点击 Authorize New Connector 按钮，选择 Google Drive (Single User)，选择需要迁移文件所在的 Google 账户并授权。

![mover_source_google](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_source_google.png)

授权完成后，就会出现所有需要迁移的文件列表。

![mover_source_done](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_source_done.png)

#### 选择迁移目标

点击 Authorize New Connector 按钮，选择 OneDrive for Business (Single User)，选择该数据源并授权。目前目标数据源只支持微软家族的 OneDrive 和 SharePoint 等。

![mover_choose_dest](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_choose_dest.png)

![mover_dest_onedrive](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_dest_onedrive.png)

授权完成后，就会出现迁移目标网盘的文件列表。

![mover_dest_onedrive_done](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_dest_onedrive_done.png)

### 迁移数据

来源数据源与目标数据源都迁移完成后，即可选择 Start Copy 开始迁移流程。

![mover_start_copy](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_start_copy.png)

### 等待迁移完成

完成上述操作后，迁移流程已经开始，仅需等待完成即可，可以通过登录后的 Migration Manager 进行进度查看。

![mover_wait_migration_done](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_wait_migration_done.png)

因为源文件大小不同，迁移时间每个人各不相同，经测试，迁移速度参照如下：

![mover_migration_speed](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/mover_migration_speed.png)

## 总结

以上就是我用过 mover.io 服务将所有 Google Drive 文件迁移到 OneDrive 上的过程，希望对大家有所帮助。

## 参考资料

> 1. [mover.io 官网](https://mover.io/)
> 2. [Transfer Google Drive
(HKU Connect Google Drive > HKU Microsoft OneDrive)](https://its.hku.hk/kb/ways-on-reducing-storage-on-google-drive-google-photos-and-gmail/#b-transfer-google-drive)