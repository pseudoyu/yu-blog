---
title: "ECOM6013 Topic 4 Website Design, Testing and Maintenance"
date: 2020-09-16T21:25:28+08:00
draft: false
tags: ["e-commerce", "hku", "ecom6013"]
categories: ["Notes"]
authors:
- "Arthur"
---

# ECOM6013 E-Commerce Technologies

## Topic 4 Website Design, Testing and Maintenance

**Planing: The Systems Development Life Cycle**
1. Systems analysis/planing
   * Busisess objectives
   * System functionalities
   * Information requirements 
2. Systems design
3. Building the system
4. Testing
5. Implementation

![website_life_cycle](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/website_life_cycle.png)

**Quality Consideration**
* Navigation
* Accessibility
* Scalability
* Reliability
* Maintainability
* Usability
* Compatibility and interoperability
* Security
* Readability

**In-House / Outsourcing (Hiring vendors to provide services)**
* Build own / outsourcing
* Host own / outsourcing (preferred)

**Implementation, Maintenance, and Optimization**

*Systems break down unpredictably*

* Ongoing maintenance
* Benchmarking

**Website Optimization**
* Page generation
* Page delivery
* Page Content

**Simple vs. Multi-tier Website Architecture**

*System architecture: Arrangement of software, machinery, and tasks in an information system*

***Two-tier***
* Web server
* Database server

![two_tier_architecture](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/two_tier_architecture.png)

***Three-tier***
* Web application servers
* Backend, legacy databases

![three_tier_architecture](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/three_tier_architecture.png)

**Web Server Software**
* Appache
  * Leading web server software
  * works on UNIX, Linux OS
  * Reliable
  * Stable
  * Open source
* Microsoft's Internet Information Server (IIS)
  * Second major web server software
  * works on Windows OS
  * Integrated
  * Easy to use

**Basic Functionality Provided by Web Servers**
* Processing of HTTP requests
* Security services (Secure Sockets Layer) / Transport Layer Security
* File transfer protocol
* Search engine
* Data capture
* E-mail
* Site management tools
  * Verify links
  * Identify files
  * Monitor customer purchases
  * Marketing campign effictiveness
  * Track hits and other statistics
  * ...

**Dynamic Page Generation Tools**
 
*Contents stored in database and fetched when needed*

* CGI
* ASP
* JSP
* ODBC
* JDBC

Advantages
* Lower menu costs
* Permits easy online market segmentation
* Enables cost-free price discrimination
* Enable content management system (CMS)

**Application Servers**
* Provide specific business functionality required for a website
* Isolate business applictaions from Web servers and databases (middleware)
* Sigle-function applictaions being replaced by integrated software tools that combine all functionality needed for e-commerce site

**E-Commerce Merchants Server Software**
* Provides basic functions for sales
  * Online catalog
  * Shopping cart
  * Credit card processing

***Packages***
* Integrated environment that includes most of functionality needed
  * Shopping cart
  * Merchandises display
  * Order management
* Different options for different-sized businesses
  * Small, Medium - Yahoo Small Business, open-source solutions
  * Mid-range - IBM Wbsphere Commerce Express,...
  * Hign-end - IBM WebSphere Professional/Enterprise,...
* Cloud-based SaaS solutions
* Key factors
  * Functionality
  * Support for different models (e.g. m-commerce)
  * Business process modeling tools
  * Visual site management and reporting
  * Performance and scalability
  * Connectivity to existing business systems
  * Compliance with standards
  * Global and multicultural capability
  * Local sales tax and shipping rules

**Hardware Platform**
* Demand Side (overall customer demand)
  * Number of simultaneous users in peak periods
  * User profile
  * Type of content (dynamic/static)
  * Required security
  * Number of items in inventory
  * Number of page requests
  * Speed of legacy application
* Supply Side
  * Scalability
    * Vertically (increase processing power of individual components)
    * Horizontally (multiple computers to share workload)
    * Improve processing architecture
    * Outsource hosting

**Eight Most Important Factors in Successful E-Commerce Site Design**
* Functionality
* Informational
* Ease of use
* Redundant navigation
* Ease of purchase
* Multi-browser functionality
* Simple graphics
* Legible text

**Personalization Tools**
* Persinalization (personal preference, prior history)
* Customization (better fit the needs)
* Cookies (primary method to achieve personalization)

**Policy Set**
* Privacy policy
* Accessibility (mainly for the disabled)

**Mobile Website/Applications**
* Type of m-commerce software
  * Moble website
  * Mobile web app
  * Native app
  * Hybrid app

**Mobile Presence**
* Identify business objectives, system functionality, and information requirements
  * Driving sales
  * Branding
  * Building customer community
  * Advertising and promotion
  * Gathering customer feedback
  * ...
* Choices
  * Mobile first design (most efficient)
  * Mobile website (least expensive)
    * Responsive web design (RWD) - for different screen resolution
      * Automates the inclusion of content based on profiles
      * Fluid design
      * Optimized performance
      * Technically complex (implement, maintain and test)
      * Higher cost, larger database
    * Adaptive web design (AWD) - for different devices
  * Mobile web app (can utilize browser API)
  * Native app (most expensive)
    * Use device hardware (usually better performance)
    * Offline
  * [Progressive Web App (PWA)](https://web.dev/what-are-pwas/)
* Platform constraints
  * Graphics
  * File size
* Features needed to be considered
  * Hardware
  * Connectivity
  * Displays
  * Interface

**Useful Resources**
* [W3School](https://www.w3schools.com/whatis/)
* [Mozilla Development Network (MDN)](https://developer.mozilla.org/en-US/)
* [Google Web Dev](https://developers.google.com/web)

**Build Own Websites**
* [Wix Free Website Builder](https://wix.com)
* [Shopify Site Builder](https://shopify.com)
* [WordPress](https://wordpress.com)
* [Hugo](https://gohugo.io)