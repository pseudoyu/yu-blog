---
title: "Build Your Free Image Hosting System from Scratch (Cloudflare R2 + WebP Cloud + PicGo)"
date: 2024-06-30T14:12:47+08:00
draft: false
tags: ["image-hosting", "cloudflare", "r2", "webp cloud", "serverless", "s3", "blog", "picgo"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

In the article "What Changed in My Blog in 2024", I introduced the blog system I built using Serverless platforms and some open-source projects, and also started this series of tutorials to document the entire build and deployment process.

This article is about the solution for the image hosting system.

**[2024-07-02 Update]**

I wrote a new tutorial implementing privacy and copyright protection for the image hosting system, which can be considered an additional chapter.

- [Add Privacy and Copyright Protection to Your Image Hosting Using WebP Cloud and Cloudflare WAF](https://www.pseudoyu.com/en/2024/07/02/protect_your_image_using_webp_and_cloudflare_waf/)

## Image Hosting Solution Iterations

At the beginning of setting up my blog, due to the limited content and few illustrations, most of the images were directly placed in the `static` directory of my Hugo blog repository. I didn't feel any inconvenience until I needed to publish on multiple platforms. After copying the blog's markdown source files, all the images were unable to display because they were using relative paths to the blog. I had to re-upload the images one by one, which was very cumbersome.

It was then that I began to understand the concept of image hosting - uploading images to a dedicated storage service and using them via public links. This not only allows for unified management but also effectively reduces the size of blog repository files and improves the loading speed of the website.

### GitHub + jsDelivr CDN + PicGo

Initially, I created a new GitHub repository "GitHub - image-hosting", uploaded directly to the repository through PicGo, and changed the image path returned by PicGo to the CDN-accelerated link from [jsDelivr](https://www.jsdelivr.com/). It was quite convenient and even had version control.

However, the good times didn't last long. jsDelivr suffered DNS pollution and was blocked in mainland China, causing my blog images to be completely unloadable for a long period. This made me have some concerns about this purely CDN-dependent approach. Additionally, hosting images on GitHub is based on code repositories, and uploading images relies on code commits, which can easily pollute the commit history. It's ultimately a kind of abuse, and if there are issues with account/repository access, it's easy to lose all the images. So I started looking for other solutions.

### Aliyun OSS + PicGo

The second option that came to mind was object storage provided by cloud service providers. Services like Amazon S3 and Aliyun OSS not only provide publicly accessible links but also offer advantages such as access control, data backup, and scalability. They provide an optimal solution for file data storage and management at a relatively low cost.

As I wanted to optimize access for users in mainland China, I ultimately chose Aliyun OSS. The configuration wasn't complicated, and I still used PicGo for uploading and converting to Aliyun OSS links. There was a noticeable improvement in access speed.

![aliyunoss_invoice](https://image.pseudoyu.com/images/aliyunoss_invoice.jpeg)

However, due to the pay-as-you-go billing model, the continuously growing cost was a consideration for a non-profit personal blog. In early 2023, there was a period when my blog traffic was quite high, and the monthly bills kept increasing. Additionally, if I wanted to use a custom access domain for Aliyun OSS, I needed to go through the filing process. Since my domain is hosted through Cloudflare, I didn't consider filing. So after using it for a few months, I considered changing the image hosting solution again.

### Chevereto + PicGo

After some research, I deployed the free self-hosted version of [Chevereto](https://github.com/rodber/chevereto-free) using a Docker image on my Bandwagon server (with good connectivity, CN2GIA DC6 data center), and mounted the images as a Docker Volume on the host.

To be honest, Chevereto's interface style is a bit outdated, still using the old php service. The free version hasn't been maintained or upgraded for a long time, but it's comprehensive in functionality. It can still use PicGo to interface with Chevereto's API for image uploading and other operations, and the stability is good. So I used it for a year and a half.

But I was too careless about the stability of self-hosted services and the preciousness of data. A few days ago, the server suddenly went down, with a kernel error that prevented it from rebooting. The service being down was one thing, but I couldn't export my image data from the past year and a half. I contacted technical support through a ticket, but they only replied twice in a day, once telling me to restart, and once suggesting I hire a network administrator to investigate.

I had to be self-reliant. After searching through various solutions online and struggling for a day, I finally managed to solve it. But this lesson gave me a whole new understanding of the backup and stability of self-hosted services with important data. Additionally, when I wanted to redeploy, I found that the free version images had been taken offline, leaving only a yearly paid License version. So I abandoned the original solution.

### Cloudflare R2 + WebP Cloud + PicGo

![cloudflare_r2_free_tier](https://image.pseudoyu.com/images/cloudflare_r2_free_tier.png)

So I turned back to the object storage of cloud service providers and discovered the R2 object storage service provided by the cyber bodhisattva Cloudflare. The free plan includes 10 GB of storage capacity per month, which is completely sufficient for personal use. The services and data security of a large company also provide assurance.

To optimize user access, I also used a "WebP Cloud" service to proxy the images from R2, further reducing image size at the proxy level. Although the speed for domestic users is certainly not comparable to Aliyun OSS's network, under the comprehensive conditions of no need for filing, stability, and being free, this is the best solution I could think of.

On the computer side, it's still almost one-click upload through the PicGo client and generates markdown image links that can be directly used in the blog. Once configured, it's very smooth to use.

## Image Hosting Setup Instructions

Although the Cloudflare R2 + WebP Cloud + PicGo solution involves multiple components and platforms, all operations are within the Free Plan. This is the solution I ultimately chose, and below I will introduce how to build this free image hosting system from scratch.

### Cloudflare R2

R2 is a free object storage service launched by Cloudflare. You need to register a free [Cloudflare account](https://www.cloudflare.com/zh-cn/) to use it. After registering and logging in, click R2 on the left sidebar to access the service. However, it's worth noting that activating the R2 service requires binding a credit card (major domestic and international credit cards are accepted), but no charges will be made. It's mainly used to verify user identity.

#### Creating an Image Hosting Bucket

![cloudflare_r2_interview](https://image.pseudoyu.com/images/cloudflare_r2_interview.png)

After activating the R2 service, click the "Create bucket" button in the top right corner to create a new bucket.

![cloudflare_r2_create_bucket](https://image.pseudoyu.com/images/cloudflare_r2_create_bucket.png)

On the creation configuration page, you need to fill in the bucket name. It's recommended to use something identifiable, as it will be used later when configuring uploads.

For the location, select "Automatic", but you can additionally configure a location hint. Since I will be using the "WebP Cloud" service's US West data center for image proxy optimization later, I chose "North America West (WNAM)" here. You can choose other regions based on your needs, but Cloudflare doesn't guarantee that you will definitely be allocated to the specified region.

![cloudflare_r2_create_done](https://image.pseudoyu.com/images/cloudflare_r2_create_done.png)

Click the "Create bucket" button to complete the creation. At this point, we can already upload files to our "yu-r2-test" bucket. You can choose to upload files or folders directly on the web page.

You can also use the S3 API for uploading. We will rely on this method for uploading using the PicGo client later, but it requires some additional configuration. Click the "Settings" option in the navigation bar to configure.

![cloudflare_r2_config](https://image.pseudoyu.com/images/cloudflare_r2_config.png)

First, we need to enable the "R2.dev subdomain". This is for the public address needed to access the images later. Click "Allow access" and enter "allow" as prompted to enable it.

![r2_dev_domain_allow](https://image.pseudoyu.com/images/r2_dev_domain_allow.png)

After completion, a public web address ending with `r2.dev` will be displayed, which is the address we will use to access images later.

#### Custom Image Hosting Domain (Optional)

However, the assigned address is quite long and not easy to remember. We can use a "Custom domain" to bind our exclusive domain name. Click the "Connect domain" button.

![r2_custom_domain_setup](https://image.pseudoyu.com/images/r2_custom_domain_setup.png)

Enter the domain name you want to bind, such as `yu-r2-test.pseudoyu.com`, and click continue.

![cloudflare_r2_custom_domain](https://image.pseudoyu.com/images/cloudflare_r2_custom_domain.png)

![r2_custom_domain_dns_wait](https://image.pseudoyu.com/images/r2_custom_domain_dns_wait.png)

Connect the domain and wait for the DNS resolution to take effect.

![r2_bucket_status](https://image.pseudoyu.com/images/r2_bucket_status.png)

After completion, the bucket status should show "Allowed" for "Public URL access", and "Domain" should display the custom domain name we just set up, indicating successful configuration.

#### Configuring Bucket Access API

![yu_bucket_preview](https://image.pseudoyu.com/images/yu_bucket_preview.png)

When we've completed the above configuration, we can return to the bucket "Objects" interface, upload a sample image, and click on the details to display the access address for that image. At this point, we have an accessible image hosting service.

However, manually uploading images through the Cloudflare page each time is obviously not convenient enough. R2 provides an S3-compatible API, which allows for easy use of some client/command-line tools for operations such as uploading and deleting.

![create_r2_api_token](https://image.pseudoyu.com/images/create_r2_api_token.png)

![create_r2_api_key](https://image.pseudoyu.com/images/create_r2_api_key.png)

Return to the R2 main page, click "Manage R2 API Tokens" in the top right corner, then click "Create API token" after entering.

![r2_apikey_conifg](https://image.pseudoyu.com/images/r2_apikey_conifg.png)

Enter a token name, select "Object Read and Write" for "Permissions" and assign this API to the previously created Bucket. This minimizes permissions and ensures data security. Other options can be kept as default.

![api_key_config_details](https://image.pseudoyu.com/images/api_key_config_details.png)

After creation is complete, all keys will be displayed. We need the following three pieces of information for PicGo. However, as they will only be shown once, it's advisable to keep these parameter information safe in a password manager or elsewhere.

At this point, we have completed the configuration part on Cloudflare R2. Next, we need to configure the PicGo client.

### PicGo

PicGo is a tool software for quickly uploading and obtaining image URLs, with a relatively rich plugin ecosystem supporting multiple image hosting services. Its GitHub repository is "GitHub - Molunerfinn/PicGo", and you can download the corresponding platform client for use.

#### Configuring R2 Image Hosting

PicGo itself doesn't include S3 image hosting, but it can be supported through the "GitHub - wayjam/picgo-plugin-s3" plugin.

![picgo_s3_plugin](https://image.pseudoyu.com/images/picgo_s3_plugin.png)

Select to install in "Plugin Settings", and a new Amazon S3 option will appear in "Image Hosting Settings". Click to enter the configuration options.

![r2_picgo_s3_config](https://image.pseudoyu.com/images/r2_picgo_s3_config.png)

There are several configuration items that need particular attention:

- **Application Key ID**, fill in the Access Key ID from the R2 API
- **Application Key**, fill in the Secret Access Key from the R2 API
- **Bucket Name**, fill in the Bucket name created in R2, such as `yu-r2-test` in my example above
- **File Path**, the file path uploaded to R2, I chose to use `{fileName}.{extName}` to preserve the original file name and extension
- **Custom Node**, fill in the "Jurisdiction-specific endpoint for S3 clients" from the R2 API, i.e., the S3 Endpoint in the format `xxx.r2.cloudflarestorage.com`
- **Custom Domain Name**, fill in the `xxx.r2.dev` format domain generated earlier or the custom domain name, such as `yu-r2-test.pseudoyu.com` that I configured

Other configurations can be kept as default. After confirming that the parameters are correct, click "Confirm" and "Set as Default Image Hosting".

#### Image Upload

![upload_r2_with_picgo](https://image.pseudoyu.com/images/upload_r2_with_picgo.png)

After completing the above configuration, we can directly drag files into the "Upload Area" to upload images. If it displays correctly after upload, the configuration is successful. The generated link will automatically be in the system clipboard, and you can directly paste it where needed.

![picgo_custom_url_format](https://image.pseudoyu.com/images/picgo_custom_url_format.png)

And you can select the corresponding format in the link format, such as URL or Markdown format links that can be used in blogs. Here, I made a small configuration: in the left "PicGo Settings" - "Custom Link Format", I modified it to `![$fileName]($url)`, and selected "Custom" in the link format of the upload area. This way, after I upload, it will generate a Markdown image link with the file name as the Alt text based on the file name.

### WebP Cloud Image Optimization

At this point, we have completed the entire image hosting setup, configuration, and upload process. However, usually, the images we screenshot locally or take with cameras are quite large, which would take a long time for visitors to load and are not directly suitable for internet publishing.

![tiny_png_compress](https://image.pseudoyu.com/images/tiny_png_compress.png)

For a long time, I used a very clumsy method: the API of the online website "TinyPNG" combined with an open-source macOS client application. I would drag images into it for compression before uploading to the image hosting through PicGo. This usually could reduce the image size by more than 50% with minimal loss in image quality. It was cumbersome but effective.

After changing the image hosting solution this time, I also started looking for more intelligent image optimization services, and thought of "WebP Cloud".

I actually learned about this service last year one evening when I was watching people play rhythm games in an arcade in a Hangzhou shopping mall with [STRRL](https://x.com/strrlthedev). He showed me the news that a blog post by [Nova Kwok](https://x.com/n0vad3v) had topped the Hacker News rankings, and we spent half an hour looking at it together. At that time, I only knew it was a service for optimizing images, but didn't understand it in detail.

So I opened the official website "webp.se" again to look at a more detailed introduction.

![webp_se_intro](https://image.pseudoyu.com/images/webp_se_intro.png)

In simple terms, this is a CDN-like image proxy SaaS service that can significantly reduce image size while maintaining almost the same image quality, thus speeding up overall site loading. As it has developed, in addition to reducing image size, it now offers more practical features such as caching, adding watermarks, image filters, and provides custom header configuration options.

After looking around, I felt it could well meet my blog image optimization needs, so I started to tinker with the configuration.

#### Configuring WebP Cloud

![webp_cloud_login](https://image.pseudoyu.com/images/webp_cloud_login.png)

First, log in to the [WebP Cloud](https://dashboard.webp.se/) platform through GitHub authorization.

![webp_cloud_overview](https://image.pseudoyu.com/images/webp_cloud_overview.png)

The page is very intuitive, mainly showing the Free Quota and additional Quota data under the current Plan, as well as some usage statistics.

Click the "Create Proxy" button to add configuration.

![webp_cloud_config](https://image.pseudoyu.com/images/webp_cloud_config.png)

- To optimize access for users in China, I chose the US West "Hillsboro, OR" region for "Proxy Region"
- Fill in a custom name for "Proxy Name"
- "Proxy Origin URL" is important, you need to fill in the R2 custom domain name we configured earlier, such as `yu-r2-test.pseudoyu.com` in my case. If you haven't configured a custom domain name, fill in the `xxx.r2.dev` format domain provided by R2

![yu_webp_test](https://image.pseudoyu.com/images/yu_webp_test.png)

The `xxx.webp.li` format shown under "Visitor" in the Basic info section of the image is our proxy address.

For example, the file [yu-r2-test.pseudoyu.com/new_mbp_setup.jpg](https://yu-r2-test.pseudoyu.com/new_mbp_setup.jpg) we previously uploaded to R2 through PicGo can be accessed using this link: [dc84642.webp.li/new_mbp_setup.jpg](https://dc84642.webp.li/new_mbp_setup.jpg).

~~If you don't like the default proxy address, you can contact the developer through the chat in the bottom right corner or by email to customize the domain name. There might be a more automated configuration process in the future.~~

**[2024-07-06 Update]**

Custom domain configuration is now supported. For detailed instructions, please refer to "Custom Domain | WebP Cloud Services Docs".

#### Changing PicGo Configuration

![change_pic_go_config](https://image.pseudoyu.com/images/change_pic_go_config.png)

It's important to note that since the images we ultimately need to place in the blog are links that have been proxied through WebP Cloud, we need to return to PicGo's "Image Hosting Settings" and change the "Custom Domain" to the WebP Cloud proxy address we just configured, which is in the format `xxx.webp.li` or other custom domain names.

#### WebP Cloud Usage

Free users have 2000 Free Quota per day, meaning they can proxy 2000 image access requests, and provide 100M of image cache. This is completely sufficient for general users. If there are some specific periods with higher traffic, you can also purchase additional Quota, which is very cheap.

If the Quota is exceeded, access will be 301 redirected to the source image address, without compression by the WebP Cloud service, but it will still be usable. If the cache exceeds 100M, it will be cleared according to the LRU algorithm, so it can still ensure that some high-frequency requested images can have a good access experience.

![yu_webp_uasge](https://image.pseudoyu.com/images/yu_webp_uasge.png)

My blog's daily visits are around 300-500 visits. Adding some RSS subscriptions and crawler traffic, according to WebP Cloud statistics, the daily requests are about 4000-5000, with 10000+ on days when I publish new posts.

![webp_cloud_price](https://image.pseudoyu.com/images/webp_cloud_price.png)

So for now, I've chosen the Lite plan, combined with some additional usage to cover peak traffic. I plan to observe for a while longer to see how it goes.

## Conclusion

The above is my image hosting system setup solution. All the images in this article were also uploaded using PicGo, stored in Cloudflare R2, and optimized through WebP Cloud proxy.

This is one of my blog setup and deployment series tutorials. If you're interested in setting up comment systems, data statistics systems, etc., please stay tuned. I hope this can be of reference to everyone.
