---
title: "Docker 基础与实践"
date: 2022-09-07T01:30:48+08:00
draft: false
tags: ["container", "docker", "devops", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## 前言

这是工作实践系列容器部分的第一篇，主要介绍 Docker 的基础知识与实践。

作为一个后端开发，我刚开始工作的时候其实主要都是在本地调试的，并没有怎么了解过 Docker 的相关使用。直到后来开始接触较为复杂的底层链开发，因为链或其相关工具的依赖关系比较复杂，也涉及很多版本冲突问题，在本机或服务器上每次需要配置复杂的环境，且每次重启后很多服务与配置都需要重新部署，繁琐且容易出现一些莫名的跨平台错误。

因此逐渐开始采用编写项目特定 Dockerfile 并编译镜像的方式进行后续的开发调试，部署的机器仅需安装 Docker 环境（以及 Docker Compose），而不需要本地安装各种依赖，很便捷。后续也和 Leader 一起基于 Docker 镜像、GitLab CI 与 k8s 环境配置了项目的 CI/CD 流程，极大提升了开发调试效率。

本文将基于这些经验对 Docker 相关的概念与实践进行总结，希望能有所帮助。

## Docker 简介

我们所开发的服务往往以二进制的方式运行在操作系统中，而 Docker 是一种容器技术，将我们的应用程序及相关依赖打包在一个容器中，容器往往是基于一个较为轻量级的 Linux 镜像，是多层镜像的堆叠，我们的应用往往在最上层，这些依赖关系在 Dockerfile 中进行指定。

使用容器进行部署比起在本机或远程服务器有很多明显的优势。

1. 无需在操作系统上安装各类环境和依赖（除了 Docker 自身）。如果采用原有的服务启动模式，开发流程会变得十分繁琐，需要开发与运维不断沟通，配合完成环境配置与部署，并且如果一台机器上部署了多个服务，也极易造成依赖/版本冲突问题。
2. 可以拥有独立的部署环境。我们通过为不同的项目编写 Dockerfile 来构建镜像，将应用所需环境与依赖打包在镜像中，可以很方便地运行同个应用的不同版本，或为 MySQL 这样的通用服务运行多个实例，并且可以通过 Docker 命令或 Docker Compose 命令进行管理，一键启动/暂停。
3. Docker 并不强依赖于操作系统本身的版本，同一个 Docker 镜像可以在不同的操作系统（Windows、macOS、不同发行版的 Linux）上运行，易于服务的分享、迁移与跨平台部署等。
4. 与虚拟机相比，Docker 容器没有内核而只包含应用层，体积更小，启动速度更快，更加轻量级。

当然，Docker 容器的兼容性相比操作系统与虚拟机相对更差一些，如 VM 能够运行任意其他操作系统，能满足更特定的一些需求。

## Docker 基础操作

### 安装 Docker

Docker 的安装很简单，在[官网](https://www.docker.com)下载自己操作系统对应的安装包并按照指引进行安装即可。

#### macOS

我个人的 macOS 系统起初是安装了 [Docker Desktop](https://www.docker.com/products/docker-desktop/)，可以通过图形化界面对镜像、容器进行管理，很方便但是占用较高，比较耗电。

后来尝试了 [Colima](https://github.com/abiosoft/colima)，一个较为轻量级的容器运行环境，在 macOS 系统上本机调试十分方便，推荐使用，根据项目官方文档安装并配置环境即可。我直接通过 `brew` 包管理工具来进行安装：

```bash
brew install colima
```

安装完成后运行 `colima start` 即可启动容器，运行 `colima stop` 停止容器，更多命令可以通过 `colima --help` 查看。

我通过了如下命令启动了自己的常用开发环境，大家可以根据自己的需求自行配置：

```bash
colima start -c 8 -m 16 -a x86_64 -p docker-amd
```

#### CentOS

比起本机开发，Docker 更常用的应用场景是在服务器上部署应用，我常用的操作系统是 `CentOS 7`，可以通过 `yum` 包管理工具安装：

```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager  --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
```

安装完成后，启动 Docker 服务并配置其开机自启：

```bash
systemctl enable docker
systemctl start docker
```

### Docker 镜像

Docker 主要有镜像和容器两个概念，可以认为镜像是通过 Dockerfile 编译出来的容器的一个模板，而容器是镜像的一个实例。

#### Dockerfile

我们通过 Dockerfile 来指定应用所需环境与依赖，其基本格式如下：

```dockerfile
FROM <image>

ENV USERNAME=admin \
    PASSWORD=123456

RUN mkdir -p <app-directory>

COPY . /<app-directory>

CMD ["<command>", "<entrypoint file>"]
```

完成 Dockerfile 编写后，我们可以在同级目录（或指定 Dockerfile）下通过 `docker build` 命令来构建镜像：

```bash
# 镜像构建
docker build -t <image:tag> .
```

#### 存储、加载镜像

我们可以把本地编译好的镜像存储为 `tar` 包来进行分享：

```bash
docker save -o <image-name>.tar <image-name>
```

当需要使用镜像时则可以通过 `docker load` 命令来加载 tar 包：

```bash
docker load -i <image-name>.tar
```

#### 上传、拉取镜像

当然，通过镜像 `tar` 包的方式来进行分享并不那么便捷，有的镜像可能会很大，传输也不方便。因此，我们可以通过 `docker push` 命令来将镜像推送至官方镜像仓库或企业/个人的私有库（像我所在的项目就是通过 Harbor 来管理镜像），并通过 `docker pull` 命令来进行拉取。

```bash
# 拉取官方镜像（简写）
docker pull <image:tag>

# 拉取官方镜像（完整命令）
docker pull docker.io/library/<image:tag>

# 推送镜像至官方镜像仓库 Docker Hub
docker push <image:tag>

# 推送镜像至私有库（需要配置鉴权）
docker tag <image:tag> <private-repo-path>/<image:tag>
docker push <private-repo-path>/<image:tag>
```

#### Docker 镜像操作

针对 Docker 镜像，我常用到的操作就是查看、删除与重命名 tag，更多命令可以通过 `docker image --help` 或官网查看。

```bash
# 查看所有镜像
docker images

# 删除镜像
docker rmi <image:tag>

# 重命名镜像
docker tag <old-image:tag> <new-image:tag>
```

### 容器操作

#### 查看容器

当我们通过 Docker 或 Docker Compose 命令启动镜像后，可以通过以下命令查看服务状态：

```bash
# 查看运行中容器
docker ps

# 查看所有容器
docker ps -a
```

#### 通过镜像启动/停止实例

当我们通过 Dockerfile 编译好了所需镜像后，可以通过 `docker run` 命令启动镜像实例，并在命令中加入一些配置来满足我们的服务需求，我的常用操作如下：

```bash
# 运行容器
docker run <image:tag>

# 运行容器并指定名称
docker run --name <server-name> <image:tag>

# 以 detached 模式运行容器
docker run -d <image:tag>

# 端口映射
docker run -p6000:6379 <image:tag>

# 配置环境变量
docker run -e USERNAME=admin -e PASSWORD=123456 <image:tag>
```

#### 启动/停止容器服务

当我们通过镜像创建实例后，可以通过如下命令来启动/停止容器服务：

```bash
# 启动/重启容器
docker start <container-id>

# 暂停容器
docker stop <container-id>
```

#### 查看日志

当我们的通过 Docker 启动服务后，还常常需要查看其运行日志以便于调试，可以通过 `docker logs` 进行查看，具体命令如下：

```bash
# 查看日志
docker logs <container-id>

# 滚动查看日志
docker logs -f <container-id>
```

#### 进入容器

有时我们还需要进入 Docker 容器服务内部进行服务查看与调试，可以通过 `docker exec` 命令进入容器，具体命令如下：

```bash
# 根据 id 进入特定容器
docker exec -it <container-id> <command>
```

#### Docker 网络

Docker 容器实例运行于网络中，我们上文的各个命令未指定网络，所以服务会运行在默认网络下，我们可以通过以下命令来查看网络：

```bash
# 查看所有网络
docker network ls
```

如果不想运行在默认网络中，我们可以通过如下命令创建自定义网络：

```bash
# 创建自定义网络
docker network create <network-name>
```

创建了我们的自定义网络后，在创建容器实例时我们可以通过 `--network` 参数来指定网络：

```bash
docker run --network <network-name> <image:tag>
```

#### Docker 数据持久化

使用 Docker 实例运行服务后，我们的数据会保存在容器中，当容器被删除后，数据也会被删除，对于一些需要长期运行的服务来说会造成数据丢失。因此，我们需要进行数据的持久化，我常用 host 挂载与 container 挂载两种方式。

我们可以通过将宿主机的某个具体的目录挂载映射至容器内的目录来实现持久化：

```bash
# 通过宿主机目录挂载容器内目录
docker run -v <host-file-path>:<container-file-path> <image:tag>
```

也可以通过 container 挂载的方式，使用 volume 来实现持久化：

```bash
# 可以通过名字来引用 volume
# Docker 会自动生成一个路径
# Windows: C:\ProgramData\docker\volumes
# Linux: /var/lib/docker/volumes
# macOS: /var/lib/docker/volumes
docker run -v <volume-name>:<container-file-path> <image:tag>
```

如果只是需要挂载，不需要对文件进行具体的管理查看等，我们也可以通过 container 匿名挂载的方式，不指定 volume 名称，而使用其自动生成的目录：

```bash
# Docker 会自动生成一个路径
# Windows: C:\ProgramData\docker\volumes
# Linux: /var/lib/docker/volumes
# macOS: /var/lib/docker/volumes
docker run -v <container-file-path> <image:tag>
```

## Docker Compose

Docker 提供了丰富的命令供我们使用，但是使用命令行操作不易于记忆，且如果应用依赖多个环境/服务，则需要分别运行与管理多个容器，造成不便。因此，我们可以通过 Docker Compose 工具来进行管理。

Docker Compose 是一个用于定义和运行多容器 Docker 应用程序的工具，其通过 `.yaml` 文件来进行配置管理。我在日常工作中使用最高频率的也是 Docker Compose，只有一些很简单的应用才会使用 `docker run` 命令来启动，也便于统一管理和后续的配置调整。

### 安装

macOS 系统如果安装了 Docker Desktop 则已经自带了 Docker Compose，可以直接使用。如果是 Linux 系统则需要单独安装，我这里同样以 `CentOS 7` 为例：

```bash
curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

完成安装后就可以使用 `docker-compose` 命令了。

### 配置管理

Docker Compose 的配置文件是一个 `yaml` 文件，其基本格式如下：

```yaml
version: '3'
services:
	contrainer-1:
    	image: <image-name>
        ports:
        	- <host>:<container>
        volumes:
        	- <host-file-path>:<container-file-path>
        environment:
        	<ENV-KEY>=<ENV-VALUE>
    contrainer-2:
    	image: <image-name>
        ports:
        	- <host>:<container>
        volumes:
        	- <volume-name-1>:<container-file-path>
        environment:
        	<ENV-KEY>=<ENV-VALUE>
volumes:
	volume-name-1:
    	driver: local
```

其大部分配置都很直观，如服务名称、镜像名称、端口映射、文件挂载、环境变量等。

其中，`version` 表示配置文件的版本，`services` 表示服务列表，`volumes` 表示挂载的卷列表。

在具体的 `services` 中，`image` 表示镜像名称，`ports` 表示端口映射，`volumes` 表示文件挂载，`environment` 表示环境变量，更多配置可以根据项目需要进行查看。

### 常用命令

#### 启动/停止服务

跟 `docker run` 命令类似，Docker Compose 也提供了 `up` 和 `down` 命令来启动和停止服务。

```bash
# 启动服务
docker-compose -f <name>.yaml up

# 以 detached 模式启动服务
docker-compose -f <name>.yaml up -d

# 停止服务
docker-compose -f <name>.yaml down
```

#### 查看日志

我们可以通过 `logs` 命令来查看服务的日志。

```bash
# 查看日志
docker-compose logs <container-id>

# 滚动查看日志
docker-compose logs -f <container-id>
```

## 实用操作命令

除了以上基础命令外，我常用的还有以下几个常用命令。

### 清除无用容器

当我们因配置或程序运行时调用出错而导致容器实例退出时，其依然会保留，可以通过 `docker ps -a` 命令来查看，我们可以通过以下组合命令进行清理：

```bash
docker rm `docker ps -a | grep Exited | awk '{print $1}'`
```

### 批量导入本地镜像

当我们需要将大量本地镜像导入机器时，如果一个个导入会非常麻烦，我们可以将镜像放入同一个目录并通过以下命令进行批量导入：

```bash
for i in `ls`; do docker load < $i ; done
```

## 总结

以上就是我对 Docker 容器技术的基础知识与实用操作的讲解，希望对你有所帮助。其实 Docker 的内容还有很多，如在上一个项目中尝试用到 Docker 的 `Buildkit` 特性，极大减小了最终构建镜像的大小，以及使用到 `buildx` 来实现跨平台兼容等等，本文旨在讲解基础知识与实践中常用的命令，这些拓展部分如果大家感兴趣的话后续再进行更新。

## 参考资料

> 1. [Docker 官网](https://www.docker.com)
> 2. [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=3c-iBn73dDE)
