---
title: "SonarQube Code Quality Check Tool Configuration"
date: 2021-10-27T01:57:23+08:00
draft: false
tags: ["code check", "devops"]
categories: ["Tools"]
authors:
- "pseudoyu"
---

## Preface

Recently, I've been responsible for managing code repositories and conducting code reviews for some of the company's projects. I've been using SonarQube, a code quality check tool that, when integrated with GitLab CI, can automatically perform code quality checks and output inspection reports for each merge request or commit.

This article documents the complete configuration process for importing projects through GitLab repositories, serving as a reference for configuring other projects.

## SonarQube Project Configuration

### Project Dashboard

![sonarqube_homepage](https://image.pseudoyu.com/images/sonarqube_homepage.png)

The SonarQube project dashboard is shown in the image above, which analyzes project code quality using a rating system. After each code analysis, it provides a multi-dimensional analysis of the code in a visually intuitive manner. Before merging branches, submitters can refer to the analysis results to modify and improve their code, reducing unnecessary workload for code reviewers.

![sonarqube_code_detail](https://image.pseudoyu.com/images/sonarqube_code_detail.png)

Clicking on specific metrics allows for a deeper dive into code files, identifying detected issues and providing an effective reference for manual code review.

### Project Setup

![how_to_analyze](https://image.pseudoyu.com/images/how_to_analyze.png)

Click "Add Project" in the upper right corner to choose from different analysis methods. It supports common code repository automation workflows such as Jenkins, GitLab CI, and GitHub Actions. This article will primarily explain the configuration method for GitLab CI.

![import_gitlab_project](https://image.pseudoyu.com/images/import_gitlab_project.png)

After selecting GitLab CI, choose the project repository from your associated GitLab account to proceed with further configuration.

![project_code](https://image.pseudoyu.com/images/project_code.png)

Taking a Go project as an example, first, we need to manually create a `sonar-project.properties` file and paste the configuration information as instructed.

![create_token.png](https://image.pseudoyu.com/images/create_token.png.png)

![config_cicd_var](https://image.pseudoyu.com/images/config_cicd_var.png)

Then, we need to create a Token for the project and fill in the Token and URL variable values in GitLab under "Settings" - "CI/CD" - "Variables" configuration options.

### CI Configuration

After the basic project configuration, we need to configure the GitLab CI workflow through `.gitlab-ci.yml`. My configuration is shown in the image below:

![config_gitlan_ci](https://image.pseudoyu.com/images/config_gitlan_ci.png)

I have primarily set it up so that when a merge request is made to the repository, if there are changes in the `src` directory, the `testing` pipeline is executed, performing a code quality check through SonarQube.

GitLab CI can also include deployment scripts, used in conjunction with the SonarQube tool to optimize workflows. The project's CI script needs to add corresponding Runners to execute.

![sonar_check_begin](https://image.pseudoyu.com/images/sonar_check_begin.png)

When a merge request is detected, the sonarqube-check will be triggered and executed, ultimately returning the execution results.

![sonar_check_success](https://image.pseudoyu.com/images/sonar_check_success.png)

![sonarqube_status](https://image.pseudoyu.com/images/sonarqube_status.png)

At this point, opening the project page in SonarQube will show the analysis information, completing this code quality check.

## Conclusion

The above describes the complete process of configuring the SonarQube code quality check tool for an existing Go project in a GitLab repository. Automated code quality checks are an important part of standardized development and operations processes, especially in team projects. Good standards help optimize workflows and improve overall project quality.

In the future, I will continue to document the configuration and use of open-source tools for development and operations standards used in work. If there are any errors or omissions, please feel free to communicate and correct.

## References

> 1. [SonarQube Document](https://docs.sonarqube.org/latest/)