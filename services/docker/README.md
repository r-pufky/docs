Docker Setup
============
Setting up docker on Ubuntu. See [getting started][eg].

1. [Installing](#installing)
1. [Common Management Tasks](#common-management-tasks)
1. [Bridged Adapters](#bridged-adapters)

Installing
----------
Add docker repository for latest docker packages.
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"
apt update && apt install docker-ce
```

### Add docker user for containers that can set effective UID.
Containers operate with their own internal UID when accessing volume mounts,
most allow you to specify UID and GID of the running services for proper access.
Create a docker user with no privileges so we can explicitly set file
restrictions in mounted volumes for containers.

```bash
adduser --system --home /etc/docker --shell /bin/false docker
```

Common Management Tasks
-----------------------
See [cheetsheet][o3].

Do **NOT** expose `docker.sock` to [containers, even in read-only][9w].

### Docker [Compose for Multiple Containers][xi]
Enables the management of multiple docker containers within a single YAML file
to manage them as a 'service'. Additionally eases modification and updates of
those containers. This is _preferred_ to running standalone containers.

Each YAML file represents a service and is generally stored in separate
directory representing the _service name_.

docker-compose.yml
```yaml
version: "3"

services:
  mycontainer:
    image: <repo>/<container>:<tag>
    network_mode: host
    restart: unless-stopped
    ports:
      - '3000:3000'
      - '4000:4000/udp'
    environment:
      - ENV_VAR=value
    volumes:
      - /etc/localtime:/etc/localtime:ro
  mycontainer2:
    image: <repo>/<container>:<tag>
    restart: unless-stopped
    expose:
      - '3000'
    depends_on:
      - mycontainer
    volumes:
      - /etc/localtime:/etc/localtime:ro
```
* Ports need quotes to interpret the number correctly, as YAML interprets (LOL)
  [values in XX:XX as _Time_][wl].
* `expose` explicitly exposes ports within the isolated services networks for
  other services to use, it is not publically accessible.
* `depends_on` will require other named docker container to start before this
  container.

### Turnup Composed Services
```bash
docker-compose up -d
```
* `--remove-orphans` will delete containers removed from the config.
* Any changes to containers will be re-configured automatically, including new
  images.
* services are auto labeled as `service_container_instance`. Service being the
  directory name, container being the container name and instnace being the
  specific numbered instance (typically 1).
* **Ensure you are the right user**; standard sudo will launch jobs with your
  username. _Switch Users_ or `sudo su - root -c "docker-compose up -d"`.

### Pull new images for Services
This will automatically pull any new images for containers.
```bash
docker-compose pull
```

### List Running Services
```bash
docker-compose ps
```

Create a standalone container
-----------------------------
Enables the use of `host` network without additional networking options (e.g.
exposed docker ports appear as if they are on the host). Needs to be manully run
every time to create a container.

Great for one-time usage; however _compose is preferred in almost all cases_.

```bash
docker run -t -d \
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
* Always restarts the container, unless explicitly stopped.
* Map /etc/localtime to set the containers timezone properly.
* If the container is not found, it will automatically be pulled.
* Using `create` instead of `run -d` will create the container but not start it
  in the background automatically.
* Use should use [`-t -d`][rm] is needed to keep the container in interactive
  mode otherwise as soon as the container is idle it will sleep, which will
  stop background running services.

### Pull a docker container to use:
```bash
docker pull <repo>/<container>:<tag>
```
* Pulls a copy of the container to local docker image store.
* Can store multiple tagged versions of a container.

### Listing containers.
```bash
docker container ls -a
```
* `-a` is used to list _non-running_ containers as well.

### Show stored images.
Shows all downloaded images.
```bash
docker images
```

### Remove an image.
Deletes a container from local storage.
```bash
docker rmi <repo>/<container>:<tag>
```

### Remove a container.
This removes a created container. It does _not_ remove the image the container
is based on. See [Removean image][oq].
```bash
docker rm <name>
```

### Open shell on running container
```bash
docker exec -it <name> /bin/bash
```

### Get container settings
Return all current configuration settings for a given container.
```bash
docker inspect <name>
```

### Follow logs for running container
```bash
docker logs -f <name>
```

### Interactive docker shell that [respects terminal size][ul]

.bash_profile
```bash
docker-shell() {
  sudo docker exec -it -u $2 $1 /bin/bash -c "stty cols $COLUMNS rows $LINES && /bin/bash";
}
export -f docker-shell
```
* use: `docker-shell [instance] [user]`.

### Update all docker images already downloaded
```bash
docker images | grep -v REPOSITORY | awk '{print $1}' | xargs -L1 docker pull
```

### Stop all docker containers
```bash
docker stop $(docker ps -aq)
```

#### Show docker container stats
```bash
docker stats <container>
```
* Remove _container_ to display all running services.

Bridged Adapters
----------------
By default Docker will add `-P FORWARD DROP` rule to [iptables to prevent][rx]
specific exploitation vectors for containers. Unfortunately, this is applied to
**all** interfaces, regardless of whatever interface docker uses; this rule is
re-applied everytime the service is started. [Iptables by default filters
bridged interfaces][yv].

This will result in KVM virtual machines on a system with Docker to not be able
to use a Bridge for network communication. As a bridge is a layer 2 device, it
really shouldn't be filtering IP packets anyways. You can just disable bridged
adapters from applying the iptables. If you still use the bridge adapter for
system traffic, consider munging the filter instead.

Disable IP filtering on bridged interfaces:
```bash
echo "0" /proc/sys/net/bridge/bridge-nf-call-iptables
echo "0" /proc/sys/net/bridge/bridge-nf-call-ip6tables
echo "0" /proc/sys/net/bridge/bridge-nf-call-arptables
```
* This will validate bridging is fixed but not persist across reboots.

Update settings for sysctl as well as [UFW sysctl][yv]:

/etc/sysctl.conf
```bash
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
```

/etc/ufw/sysctl.conf
```bash
net.bridge.bridge-nf-call-ip6tables = 0
net.bridge.bridge-nf-call-iptables = 0
net.bridge.bridge-nf-call-arptables = 0
```

There is a [longstanding bug][pm] bug with sysctl in debian/ubuntu not applying
sysctl.conf properly with network settings. This can be resolved using a root
cronjob:

`sudo crontab -e`
```bash
@reboot sleep 15; /sbin/sysctl -p
```

Ensure settings are applied by rebooting and checking settings are set.
```bash
reboot
sysctl -a | grep bridge
```

[oq]: #remove-an-image
[eg]: https://docs.docker.com/get-started/
[o3]: https://github.com/wsargent/docker-cheat-sheet
[rm]: https://stackoverflow.com/questions/30209776/docker-container-will-automatically-stop-after-docker-run-d
[ul]: https://stackoverflow.com/questions/38786615/docker-number-of-lines-in-terminal-changing-inside-docker/49281526#49281526
[rx]: https://serverfault.com/questions/162366/iptables-bridge-and-forward-chain
[pm]: https://bugs.launchpad.net/ubuntu/+source/procps/+bug/50093
[yv]: https://serverfault.com/questions/431590/how-to-make-sysctl-network-bridge-settings-persist-after-a-reboot
[9w]: https://www.lvh.io/posts/dont-expose-the-docker-socket-not-even-to-a-container.html
[xi]: https://docs.docker.com/v17.09/compose/overview/
[wl]: https://docs.docker.com/v17.09/compose/compose-file/#service-configuration-reference