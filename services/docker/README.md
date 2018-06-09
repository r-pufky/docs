Docker Setup
------------
Setting up docker on ubuntu 16.04. See [getting started][1]

4. [Installing](#installing)
5. [Common Management Tasks](#common-management-tasks)

Installing
----------

Add docker repository for latest docker packages.
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"
apt update && apt install docker-ce
```

## Add docker user for containers that can set effective UID.
Containers operate with their own internal UID when accessing volume mounts,
most allow you to specify UID and GID of the running services for proper access.
In these cases, we create a docker user with no privleges so we can explicitely
set file restrictions in mounted volumes for containers.

```bash
sudo adduser --system --home /etc/docker --shell /bin/false docker
```

Common Management Tasks
-----------------------
See [cheetsheet][2]

## Create a standalone container
Enables the use of `host` network without additional networking options (e.g.
exposed docker ports appear as if they are on the host). Needs to be manully run
every time to create a container.

```bash
docker run -d \
  --name <conatiner name> \
  --network host \
  --restart unless-stopped \
  -p 3000:3000 \
  -p 4000:4000/udp \
  -v /etc/localtime:/etc/localtime:ro \
  <repo>/<container>:<tag>
```
 * Runs a container detached, using host network exposing port 3000 and
   port 4000 UDP.
 * Always restarts the container, unless explicitly stopped
 * Map /etc/localtime to set the containers timezone properly
 * If the container is not found, it will automatically be pulled
 * Using `create` instead of `run -d` will create the container but not start it
   in the background automatically

## Pull a docker container to use:

```bash
docker pull <repo>/<container>:<tag>
```
 * Pulls a copy of the container to local docker image store
 * Can store multiple tagged versions of a container

## Listing containers.

```bash
docker container ls -a
```
 * -a is used to list *non-running* containers as well

## Show stored images.
Shows all downloaded images.

```bash
docker images
```

## Remove an image.
Deletes a container from local storage.

```bash
docker rmi <repo>/<container>:<tag>
```

## Remove a container.
This removes a created container. It does *not* remove the image. See [Remove
an image](#remove-an-image).

```bash
docker rm <name>
```

## Open shell on running container

```bash
docker exec -it <name> /bin/bash
```

## Get container settings
Return all current configuration settings for a given container.

```bash
docker inspect <name>
```

## Follow logs for running container

```bash
docker logs -f <name>
```

[1]: https://docs.docker.com/get-started/
[2]: https://github.com/wsargent/docker-cheat-sheet