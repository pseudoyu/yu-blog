---
title: "Adding Privacy and Copyright Protection to Your Image Hosting with WebP Cloud and Cloudflare WAF"
date: 2024-07-02T06:12:47+08:00
draft: false
tags: ["image-hosting", "cloudflare", "waf", "webp cloud", "serverless", "blog"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

In the article "Building Your Free Image Hosting System from Scratch (Cloudflare R2 + WebP Cloud + PicGo)", I constructed a free image hosting system using Cloudflare R2 and optimized images through [WebP Cloud](https://webp.se/).

While using WebP Cloud, I discovered it offered features like custom Proxy User Agent and watermarking. This sparked an idea: could I use WebP Cloud to protect the source links of my image hosting, making WebP Cloud's proxy links the sole entry point for accessing all my images, while also uniformly adding my exclusive copyright watermark?

This article documents this practice, serving as a supplementary chapter to the image hosting setup.

## Requirement Analysis

![webp_proxy_info](https://image.pseudoyu.com/images/webp_proxy_info.png)

My current image hosting solution involves hosting images on Cloudflare R2 and accessing them through WebP Cloud, a powerful image proxy tool for optimization. However, both the proxy link `image.pseudoyu.com` and the source link `images.pseudoyu.com` can access my images, with the former being optimized and the latter being the original image I saved.

### Privacy Protection

In fact, photos taken with our phones, digital cameras, and other devices carry EXIF (EXchangeable Image File Format) information, which usually includes sensitive data such as the shooting device, time, and location. We can manually remove this metadata through some technical means, but the process is cumbersome and prone to oversight.

![webp_exif_remove](https://image.pseudoyu.com/images/webp_exif_remove.png)

Upon consulting WebP Cloud's documentation, I found that it indeed provides automatic EXIF information erasure without additional configuration. However, visitors can still access the original image through the source link exposed by Cloudflare R2. To prevent this, I need to restrict users to only request through WebP Cloud proxy links, ensuring they cannot obtain any useful information when accessing the Cloudflare R2 source links.

### Copyright Protection

![randy_pic_copyright](https://image.pseudoyu.com/images/randy_pic_copyright.png)

I previously saw Randy's experience on Twitter of his own desk setup photo being misused.

As someone who dabbles in photography myself, although my work may not have particular commercial value, it is still my creation and deserves copyright protection. Therefore, I want to uniformly add my own copyright watermark to the images to prevent unauthorized use by others.

## Implementation Plan

With the requirements clear, the task essentially divides into two parts:

1. Ensure users can only access my images through WebP Cloud proxy links, prohibiting direct access to original image links.
2. Automatically add my copyright watermark to all images at the WebP Cloud proxy level, without manual intervention.

Below is my implementation plan with detailed steps.

### WebP Custom User Agent + Cloudflare WAF

After chatting with [Nova Kwok](https://x.com/n0vad3v), the developer of [WebP Cloud](https://webp.se/), I discovered that WebP Cloud provides a custom "Proxy User Agent" feature. He recommended configuring corresponding rules in Cloudflare WAF to protect image security, as detailed in the documentation -- "[Security | WebP Cloud Services Docs](https://docs.webp.se/webp-cloud/security/#cloudflare)".

#### WebP Cloud Configuration

When we access web pages or image links on the internet, the request usually includes a User Agent field, generally containing information such as browser version. Websites can perform specific logic processing for different User Agents.

WebP Cloud defaults to using `WebP Cloud Services/1.0` as the value, meaning that regardless of what terminal device or browser the user is using to access the image, the request to Cloudflare R2 will be unified as the User Agent value defined by WebP Cloud, which is customizable by the user.

![webp_custom_user_agent](https://image.pseudoyu.com/images/webp_custom_user_agent.png)

Therefore, we log into the WebP Cloud console and set the "Proxy User Agent" field to a custom value, such as `pseudoyu.com/1.0`.

#### Cloudflare WAF Configuration

![cloudflare_waf_intro](https://image.pseudoyu.com/images/cloudflare_waf_intro.png)

[WAF (Web Application Firewall)](https://developers.cloudflare.com/waf) is a firewall service provided by Cloudflare that allows custom rules to be set to restrict specific requests for website security. After logging into Cloudflare, click on "Websites" in the left sidebar, enter the domain name you want to protect, select "Security" - "WAF" in the sidebar to use it for free (Note: This is not the account-level WAF on the outermost layer). Free accounts can set up to five custom rules.

![waf_create_rule](https://image.pseudoyu.com/images/waf_create_rule.png)

Click "Create Rule" to enter the settings page.

![user_agent_protection_waf](https://image.pseudoyu.com/images/user_agent_protection_waf.png)

Click "Edit Expression" to the right of "Expression Preview" and enter the following rule:

```plaintext
(http.user_agent ne "pseudoyu.com/1.0") and (http.host eq "images.pseudoyu.com")
```

First, you need to replace `pseudoyu.com/1.0` with the custom User Agent value you set in WebP Cloud earlier. Additionally, to prevent images from other self-deployed services on the same domain from being affected, I added the condition `(http.host eq "images.pseudoyu.com")`, which only applies to the access link of the image hosting. This part needs to be replaced with your own image hosting domain host.

Select "Block" from the "Select Action" dropdown. This will match our rule and block specific network requests. Click "Deploy/Save" after editing.

I'm using the [recommended rule](https://docs.webp.se/webp-cloud/security/#cloudflare) currently provided in the official WebP Cloud documentation. It may be adjusted for new features in the future, so you can refer directly to the documentation.

![block_by_waf_example](https://image.pseudoyu.com/images/block_by_waf_example.png)

After completing the configuration, when we try to access source links starting with `images.pseudoyu.com` again, they will be blocked by WAF, for example:

[images.pseudoyu.com/images/new_mbp_setup.jpg](https://images.pseudoyu.com/images/new_mbp_setup.jpg)

However, links proxied through WebP Cloud can be accessed normally, for example:

[image.pseudoyu.com/images/new_mbp_setup.jpg](https://image.pseudoyu.com/images/new_mbp_setup.jpg)

This perfectly meets our requirements.

### Adding Copyright Watermark to Images Using WebP Cloud

After the operations above, we have ensured that users can only access our images through WebP Cloud proxy links. The next step is to add copyright watermarks to the images.

![webp_watermark_feature](https://image.pseudoyu.com/images/webp_watermark_feature.png)

Again, upon consulting WebP Cloud's documentation, I found that it provides a "Watermark" feature in the "Visual Effects" module, which can add custom watermarks to images. It uses the `Fabric.js` library for implementation and offers some visual editing options. They even wrote an interesting blog post -- "[Implementing Real-time Watermark Preview with Fabric.js](https://blog.webp.se/dashboard-fabric-zh/)".

![watermark_list_webp](https://image.pseudoyu.com/images/watermark_list_webp.png)

Enter the WebP console, select "Visual Effects" on the left, and click "Create Watermark" in the upper right corner to configure some custom watermark styles.

![pseudoyu_copyright](https://image.pseudoyu.com/images/pseudoyu_copyright.png)

This is my configuration, which adds a light gray `@pseudoyu` text at the bottom center of the image.

![webp_purge_all_cache](https://image.pseudoyu.com/images/webp_purge_all_cache.png)

Note that WebP Cloud caches image data for users. Therefore, if you want previously uploaded images to apply the watermark or update to a new watermark, you need to click "Purge All Cache" in the proxy configuration to clear the cache.

![apply_watermark_webp](https://image.pseudoyu.com/images/apply_watermark_webp.png)

After editing the watermark, go to the detailed configuration page of the proxy, scroll down to the "Watermark Setting" module, select the watermark you just created, and click "Save" in the upper right corner.

I won't demonstrate the effect separately, as all the images in this article have had watermarks added in this way.

## Conclusion

![webp_thoughts](https://image.pseudoyu.com/images/webp_thoughts.png)

It's only been three days since I started using [WebP Cloud](https://webp.se/), and initially, I thought it was just a CDN-like tool for accelerating image access. After tinkering with it, I discovered many interesting aspects. The Free Quota provided for individual free users is sufficient to give everyone a better image experience, which aligns with their principle of "doing the right thing".

The team focuses more on technical accumulation and practice, writing numerous blog posts -- "[WebP Cloud Services Blog](https://blog.webp.se/)". Reading these in leisure time, one can feel their enthusiasm. Recently, due to an experience shared in "Weekly Review #63 - An Unpleasant Flower Ordering Experience, Merchants and Consumers, and the Increasingly AI-driven World", I've been pondering the issue of "bad money driving out good". I believe teams that insist on doing the right thing without making too many compromises to commercialization deserve to be seen by more people and deserve to fare better. Though my influence is limited, I hope these tutorials can help more people learn about them.