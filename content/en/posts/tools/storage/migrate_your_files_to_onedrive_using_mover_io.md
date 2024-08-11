---
title: "Seamlessly Migrating Cloud Drive Files to OneDrive Using mover.io Service"
date: 2022-05-22T13:06:12+08:00
draft: false
tags: ["data", "mover.io", "onedrive", "google drive"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《Here, After Us - Mayday》" >}}

## Preface

Recently, the school sent an email stating that they would be transitioning email services from Google to Microsoft, and the previously unlimited Google Drive storage would be discontinued, replaced by 5TB of OneDrive space. I had been using Google Drive's file service to synchronize and backup files across my multiple devices, accumulating nearly 300GB of data. Due to the slow download speeds of Google Drive in mainland China requiring a proxy, I opted for the officially recommended [mover.io](https://mover.io) service to perform a cloud migration, eliminating the need to download and re-upload files locally. Here, I document the migration process.

## mover.io Service

![mover_io](https://image.pseudoyu.com/images/mover_io.png)

The mover.io service is a cloud storage migration tool provided by Microsoft. It supports the migration of files from various cloud service providers to Microsoft OneDrive, including Google Drive, Dropbox, Box, and others. It offers migration services for organizations, schools, and individuals alike.

For individual users, we utilize the Transfer Wizard to conduct the migration.

![mover_transfer_wizard](https://image.pseudoyu.com/images/mover_transfer_wizard.png)

## Migration Process

### Register/Log in to mover.io Account

First, we need to register a mover.io account and log in. You can use Microsoft authorization to log in or use your existing mover.io account.

![mover_io_login](https://image.pseudoyu.com/images/mover_io_login.png)

### Authorize Migration Data Source

After successful login, the interface clearly provides operational instructions. Simply follow the steps.

![mover_transfer_wizard_setting](https://image.pseudoyu.com/images/mover_transfer_wizard_setting.png)

#### Select Migration Source

Click the Authorize New Connector button, choose Google Drive (Single User), select the Google account containing the files you wish to migrate, and authorize.

![mover_source_google](https://image.pseudoyu.com/images/mover_source_google.png)

Once authorized, a list of all files to be migrated will appear.

![mover_source_done](https://image.pseudoyu.com/images/mover_source_done.png)

#### Select Migration Destination

Click the Authorize New Connector button, choose OneDrive for Business (Single User), select this data source, and authorize. Currently, the destination data source only supports Microsoft family products like OneDrive and SharePoint.

![mover_choose_dest](https://image.pseudoyu.com/images/mover_choose_dest.png)

![mover_dest_onedrive](https://image.pseudoyu.com/images/mover_dest_onedrive.png)

After authorization, a file list of the migration destination cloud storage will appear.

![mover_dest_onedrive_done](https://image.pseudoyu.com/images/mover_dest_onedrive_done.png)

### Migrate Data

Once both the source and destination data sources are set up, you can select Start Copy to begin the migration process.

![mover_start_copy](https://image.pseudoyu.com/images/mover_start_copy.png)

### Wait for Migration Completion

After completing the above operations, the migration process will commence. You only need to wait for it to finish. You can check the progress through the Migration Manager after logging in.

![mover_wait_migration_done](https://image.pseudoyu.com/images/mover_wait_migration_done.png)

Due to differences in source file sizes, migration times will vary for each individual. Based on testing, the migration speed reference is as follows:

![mover_migration_speed](https://image.pseudoyu.com/images/mover_migration_speed.png)

## Conclusion

The above outlines the process I used to migrate all Google Drive files to OneDrive using the mover.io service. I hope this proves helpful to everyone.

## References

> 1. [mover.io Official Website](https://mover.io/)
> 2. [Transfer Google Drive
(HKU Connect Google Drive > HKU Microsoft OneDrive)](https://its.hku.hk/kb/ways-on-reducing-storage-on-google-drive-google-photos-and-gmail/#b-transfer-google-drive)