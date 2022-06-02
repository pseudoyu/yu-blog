---
title: "SonarQube 代码质量检查工具配置"
date: 2021-10-27T01:57:23+08:00
draft: false
tags: ["code check", "devops"]
categories: ["Tools"]
authors:
- "Arthur"
---

## 前言

最近负责公司一部分项目的代码仓库管理及 code review 等，用到了 SonarQube 这一代码质量检查工具，通过集成 GitLab CI，能够实现在每次合并请求/提交时自动执行代码质量检查并输出检测报告。

本文记录了通过 GitLab 仓库导入项目的配置全流程，以便其他项目配置时参考。

## SonarQube 项目配置

### 项目面板

![sonarqube_homepage](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sonarqube_homepage.png)

SonarQube 项目面板如上图所示，会以评级的方式对项目代码质量进行分析。每次进行代码分析后，可以很直观地对代码进行多维度的分析，在合并分支前，提交人员可参照分析结果对代码进行修改完善，减少了代码审阅人员不必要的工作量。

![sonarqube_code_detail](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sonarqube_code_detail.png)

点击具体指标则可以深入代码文件对检测出的问题进行标识，为人工 code review 提供了有效参照。

### 项目配置

![how_to_analyze](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/how_to_analyze.png)

点击右上角「新增项目」，可选择不同的分析方式，支持 Jenkins, GitLab CI 及 GitHub Actions 等常用代码仓库自动化工作流方式，本文将主要说明 GitLab CI 的配置方式。

![import_gitlab_project](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/import_gitlab_project.png)

选择 GitLab CI 后，选择关联 GitLab 帐号中的项目仓库，进行后续配置。

![project_code](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/project_code.png)

以 Go 项目为例，首先，我们需要按照提示手动创建 `sonar-project.properties` 文件并粘贴配置信息。

![create_token.png](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/create_token.png.png)

![config_cicd_var](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/config_cicd_var.png)

然后需要为项目创建 Token，并在 GitLab 中 「设置」-「CI/CD」-「变量」配置选项中填写 Token 及 URL 变量值。

### CI 配置

进行基本项目配置后，需要通过 `.gitlab-ci.yml` 配置 GitLab CI 工作流，我的配置如下图所示：

![config_gitlan_ci](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/config_gitlan_ci.png)

我主要设置了当仓库进行合并请求时，如 `src` 目录下的代码有改变，则执行 `testing` 流水线，通过 SonarQube 进行代码质量检查。

GitLab CI 中还可以添加部署等脚本，与 SonarQube 工具配合使用，以实现工作流的优化。项目的 CI 脚本需要添加相应的 Runner 运行。

![sonar_check_begin](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sonar_check_begin.png)

当检测到合并请求时，sonarqube-check 会被触发执行，最终返回执行结果。

![sonar_check_success](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sonar_check_success.png)

![sonarqube_status](https://cdn.jsdelivr.net/gh/pseudoyu/image-hosting@master/images/sonarqube_status.png)

此时点开 SonarQube 中项目的页面，则已经有了分析信息，本次代码质量检查完成。

## 总结

以上就是对 GitLab 仓库中现有 Go 项目配置 SonarQube 代码质量检查工具的全流程。代码质量自动化检查是开发运维规范流程中重要的环节，尤其是在团队项目中，好的规范有助于工作流的优化，提升项目的整体质量。

后续也将会对工作中用到的开发运维规范开源工具配置与使用进行记录，如有错漏，敬请交流指正。

## 参考资料

> 1. [SonarQube Document](https://docs.sonarqube.org/latest/)