---
title: "Docker Fundamentals and Practices"
date: 2022-09-07T01:30:48+08:00
draft: false
tags: ["container", "docker", "devops", "programming", "work practice series", "work", "practice", "backend"]
categories: ["Develop"]
authors:
- "pseudoyu"
---

{{<audio src="audios/here_after_us.mp3" caption="《后来的我们 - 五月天》" >}}

## Preface

This is the first article in the container section of the work practice series, primarily introducing the basic knowledge and practices of Docker.

As a backend developer, when I first started working, I mainly debugged locally and hadn't really learned about Docker usage. It wasn't until later when I began to engage with more complex underlying chain development that I encountered issues. Because of the intricate dependency relationships of chains or their related tools, along with version conflict problems, configuring complex environments on local machines or servers each time became necessary. Moreover, many services and configurations needed to be redeployed after every restart, making the process cumbersome and prone to inexplicable cross-platform errors.

Therefore, I gradually began to adopt the approach of writing project-specific Dockerfiles and compiling images for subsequent development and debugging. Deployment machines only needed to install the Docker environment (and Docker Compose), without the need to install various dependencies locally, which was very convenient. Later, together with my team leader, we configured the project's CI/CD process based on Docker images, GitLab CI, and the k8s environment, greatly improving development and debugging efficiency.

This article will summarize Docker-related concepts and practices based on these experiences, hoping to be of some help.

## Introduction to Docker

The services we develop often run as binaries in the operating system, while Docker is a container technology that packages our application and related dependencies in a container. Containers are typically based on a lightweight Linux image and are a stack of multiple layers of images. Our application is usually at the top layer, and these dependency relationships are specified in the Dockerfile.

Using containers for deployment has many clear advantages over deploying on local machines or remote servers.

1. No need to install various environments and dependencies on the operating system (except for Docker itself). If we adopt the original service startup mode, the development process would become very cumbersome, requiring constant communication between developers and operations to complete environment configuration and deployment. Moreover, if multiple services are deployed on one machine, it's very easy to cause dependency/version conflict issues.

2. Can have independent deployment environments. We build images by writing Dockerfiles for different projects, packaging the required environment and dependencies for the application in the image. This makes it convenient to run different versions of the same application, or run multiple instances of common services like MySQL. These can be managed through Docker commands or Docker Compose commands, allowing one-click startup/pause.

3. Docker is not strongly dependent on the version of the operating system itself. The same Docker image can run on different operating systems (Windows, macOS, different distributions of Linux), facilitating service sharing, migration, and cross-platform deployment.

4. Compared to virtual machines, Docker containers do not have a kernel and only contain the application layer, making them smaller in size, faster to start, and more lightweight.

Of course, the compatibility of Docker containers is relatively poorer compared to operating systems and virtual machines. For example, VMs can run any other operating system and can meet more specific needs.

## Basic Docker Operations

### Installing Docker

Installing Docker is simple. Download the installation package corresponding to your operating system from the [official website](https://www.docker.com) and follow the instructions to install.

#### macOS

For my personal macOS system, I initially installed [Docker Desktop](https://www.docker.com/products/docker-desktop/), which allows management of images and containers through a graphical interface. It's convenient but consumes more resources and is power-intensive.

Later, I tried [Colima](https://github.com/abiosoft/colima), a relatively lightweight container runtime environment. It's very convenient for local debugging on macOS systems. I recommend using it. You can install and configure the environment according to the project's official documentation. I installed it directly using the `brew` package management tool:

```bash
brew install colima
```

After installation, run `colima start` to start the container, and `colima stop` to stop the container. More commands can be viewed through `colima --help`.

I started my common development environment with the following command, which you can configure according to your own needs:

```bash
colima start -c 8 -m 16 -a x86_64 -p docker-amd
```

#### CentOS

Compared to local development, Docker is more commonly used for deploying applications on servers. My frequently used operating system is `CentOS 7`, which can be installed through the `yum` package management tool:

```bash
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager  --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
```

After installation, start the Docker service and configure it to start automatically on boot:

```bash
systemctl enable docker
systemctl start docker
```

### Docker Images

Docker mainly has two concepts: images and containers. An image can be considered as a template for a container compiled through a Dockerfile, while a container is an instance of an image.

#### Dockerfile

We use Dockerfile to specify the environment and dependencies required for the application. Its basic format is as follows:

```dockerfile
FROM <image>

ENV USERNAME=admin \
    PASSWORD=123456

RUN mkdir -p <app-directory>

COPY . /<app-directory>

CMD ["<command>", "<entrypoint file>"]
```

After completing the Dockerfile, we can build the image using the `docker build` command in the same directory (or specify the Dockerfile):

```bash
# Build image
docker build -t <image:tag> .
```

#### Storing and Loading Images

We can store locally compiled images as `tar` packages for sharing:

```bash
docker save -o <image-name>.tar <image-name>
```

When we need to use the image, we can load the tar package using the `docker load` command:

```bash
docker load -i <image-name>.tar
```

#### Uploading and Pulling Images

Of course, sharing through image `tar` packages is not so convenient, and some images may be very large, making transfer inconvenient. Therefore, we can use the `docker push` command to push images to the official image repository or enterprise/personal private repositories (like the project I'm working on uses Harbor to manage images), and use the `docker pull` command to pull them.

```bash
# Pull official image (shorthand)
docker pull <image:tag>

# Pull official image (full command)
docker pull docker.io/library/<image:tag>

# Push image to official image repository Docker Hub
docker push <image:tag>

# Push image to private repository (authentication required)
docker tag <image:tag> <private-repo-path>/<image:tag>
docker push <private-repo-path>/<image:tag>
```

#### Docker Image Operations

For Docker images, the operations I frequently use are viewing, deleting, and renaming tags. More commands can be viewed through `docker image --help` or on the official website.

```bash
# View all images
docker images

# Delete image
docker rmi <image:tag>

# Rename image
docker tag <old-image:tag> <new-image:tag>
```

### Container Operations

#### Viewing Containers

After we start an image through Docker or Docker Compose commands, we can view the service status through the following commands:

```bash
# View running containers
docker ps

# View all containers
docker ps -a
```

#### Starting/Stopping Instances from Images

After we have compiled the required image through Dockerfile, we can start an image instance through the `docker run` command, and add some configurations in the command to meet our service needs. My common operations are as follows:

```bash
# Run container
docker run <image:tag>

# Run container and specify name
docker run --name <server-name> <image:tag>

# Run container in detached mode
docker run -d <image:tag>

# Port mapping
docker run -p6000:6379 <image:tag>

# Configure environment variables
docker run -e USERNAME=admin -e PASSWORD=123456 <image:tag>
```

#### Starting/Stopping Container Services

After we create an instance from an image, we can start/stop the container service through the following commands:

```bash
# Start/restart container
docker start <container-id>

# Pause container
docker stop <container-id>
```

#### Viewing Logs

After we start a service through Docker, we often need to view its running logs for debugging. We can view them through `docker logs`, with specific commands as follows:

```bash
# View logs
docker logs <container-id>

# View logs in follow mode
docker logs -f <container-id>
```

#### Entering Containers

Sometimes we need to enter the Docker container service internally for service inspection and debugging. We can enter the container through the `docker exec` command, with specific commands as follows:

```bash
# Enter specific container by id
docker exec -it <container-id> <command>
```

#### Docker Network

Docker container instances run within a network. In our previous commands, we didn't specify a network, so the services will run under the default network. We can view networks through the following command:

```bash
# View all networks
docker network ls
```

If we don't want to run in the default network, we can create a custom network through the following command:

```bash
# Create custom network
docker network create <network-name>
```

After creating our custom network, we can specify the network through the `--network` parameter when creating container instances:

```bash
docker run --network <network-name> <image:tag>
```

#### Docker Data Persistence

After running services with Docker instances, our data will be saved in the containers. When the containers are deleted, the data will also be deleted, which can cause data loss for some services that need to run for a long time. Therefore, we need to persist the data. I commonly use host mounting and container mounting.

We can achieve persistence by mounting a specific directory of the host machine to a directory inside the container:

```bash
# Mount host directory to container directory
docker run -v <host-file-path>:<container-file-path> <image:tag>
```

We can also use container mounting, using volumes to achieve persistence:

```bash
# You can reference the volume by name
# Docker will automatically generate a path
# Windows: C:\ProgramData\docker\volumes
# Linux: /var/lib/docker/volumes
# macOS: /var/lib/docker/volumes
docker run -v <volume-name>:<container-file-path> <image:tag>
```

If we only need to mount and don't need specific file management or viewing, we can also use container anonymous mounting, not specifying a volume name, but using its automatically generated directory:

```bash
# Docker will automatically generate a path
# Windows: C:\ProgramData\docker\volumes
# Linux: /var/lib/docker/volumes
# macOS: /var/lib/docker/volumes
docker run -v <container-file-path> <image:tag>
```

## Docker Compose

Docker provides rich commands for us to use, but using command-line operations is not easy to remember, and if an application depends on multiple environments/services, it requires running and managing multiple containers separately, causing inconvenience. Therefore, we can use the Docker Compose tool for management.

Docker Compose is a tool for defining and running multi-container Docker applications, which uses `.yaml` files for configuration management. In my daily work, I use Docker Compose most frequently, only using the `docker run` command to start very simple applications, which is also convenient for unified management and subsequent configuration adjustments.

### Installation

If you have installed Docker Desktop on macOS, it already comes with Docker Compose, which can be used directly. If it's a Linux system, it needs to be installed separately. Here I'll take `CentOS 7` as an example:

```bash
curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

After installation, you can use the `docker-compose` command.

### Configuration Management

The configuration file for Docker Compose is a `yaml` file, with its basic format as follows:

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

Most of the configurations are intuitive, such as service name, image name, port mapping, file mounting, environment variables, etc.

Among them, `version` represents the version of the configuration file, `services` represents the list of services, and `volumes` represents the list of mounted volumes.

In specific `services`, `image` represents the image name, `ports` represents port mapping, `volumes` represents file mounting, `environment` represents environment variables. More configurations can be viewed according to project needs.

### Common Commands

#### Starting/Stopping Services

Similar to the `docker run` command, Docker Compose also provides `up` and `down` commands to start and stop services.

```bash
# Start service
docker-compose -f <name>.yaml up

# Start service in detached mode
docker-compose -f <name>.yaml up -d

# Stop service
docker-compose -f <name>.yaml down
```

#### Viewing Logs

We can view service logs through the `logs` command.

```bash
# View logs
docker-compose logs <container-id>

# View logs in follow mode
docker-compose logs -f <container-id>
```

## Practical Operation Commands

In addition to the above basic commands, I often use the following common commands.

### Clearing Unused Containers

When our container instances exit due to configuration or program runtime errors, they will still be retained. We can view them through the `docker ps -a` command. We can clean them up through the following combined command:

```bash
docker rm `docker ps -a | grep Exited | awk '{print $1}'`
```

### Batch Import of Local Images

When we need to import a large number of local images into a machine, it would be very troublesome to import them one by one. We can put the images in the same directory and use the following command for batch import:

```bash
for i in `ls`; do docker load < $i ; done
```

## Conclusion

The above is my explanation of the basic knowledge and practical operations of Docker container technology. I hope it's helpful to you. In fact, there's still a lot more content about Docker. For example, in the previous project, we tried to use Docker's `Buildkit` feature, which greatly reduced the size of the final built image, and used `buildx` to achieve cross-platform compatibility, etc. This article aims to explain basic knowledge and commonly used commands in practice. If you're interested in these extended parts, I'll update them later.

## References

> 1. [Docker Official Website](https://www.docker.com)
> 2. [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=3c-iBn73dDE)