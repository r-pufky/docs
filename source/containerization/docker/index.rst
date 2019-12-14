.. _docker:

Docker
######
Setting up docker on Ubuntu. See `getting started`_.

.. danger::
  Do **NOT** expose ``docker.sock`` to `containers, even in read-only`_.

Install Docker Service
**********************

.. code-block:: bash
  :caption: Add docker repository for latest docker packages.

  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable"
  apt update && apt install docker-ce

Containers operate with their own internal UID when accessing volume mounts,
most allow you to specify UID and GID of the running services for proper access.
Create a docker user with no privileges so we can explicitly set file
restrictions in mounted volumes for containers.

.. code-block:: bash
  :caption: Add docker user for containers that can set effective UID.

  adduser --system --home /etc/docker --shell /bin/false docker

Create A Standalone Container
*****************************
Enables the use of ``host`` network without additional networking options (e.g.
exposed docker ports appear as if they are on the host). Needs to be manully run
every time to create a container.

Great for one-time usage; however compose is preferred in *almost all cases*.

.. code-block:: bash
  :caption: Create a standalone docker container.

  docker run -t -d \
    --name {CONTAINER NAME} \
    --network host \
    --restart unless-stopped \
    -p 3000:3000 \
    -p 4000:4000/udp \
    -v /etc/localtime:/etc/localtime:ro \
    {REPO}/{CONTAINER}:{TAG}

* Runs a container detached, using host network exposing port 3000 and
  port 4000 UDP.
* Always restarts the container, unless explicitly stopped.
* Map ``/etc/localtime`` to set the containers timezone properly.
* If the container is not found, it will automatically be pulled.
* Using ``create`` instead of ``run -d`` will create the container but not start
  it in the background automatically.
* Daemon mode `-t -d`_ is needed to keep the container in interactive mode;
  otherwise as soon as the container is idle it will sleep, stopping the
  background running services.

`Compose with Containers`_
**************************
Enables the management of multiple docker containers within a single YAML file
to manage them as a service unit. Additionally eases modification and updates of
those containers. This is *preferred* to running standalone containers. Commands
mirror standard *docker* commands but are called with ``docker-compose``.

.. important::
  **Expose** ports are visible internally on the *docker network* for the
  container.

  **Ports** are ports that are publicly visible from *outside* the *docker
  network*.

  Generally with compose only reverse proxy ports are set as *Ports* and the
  containers *Expose* port internally for the proxy.

Each YAML file represents a service and is generally stored in separate
directory representing the *service name*.

.. literalinclude:: source/docker-compose.yaml
  :caption: **0640 root staff** ``{SERVICE NAME}/docker-compose.yaml``

* All ports need quotes to be interpreted correctly, as YAML interprets (LOL)
  `values in XX:XX as Time`_.
* **Expose** explicitly exposes ports within the isolated services networks for
  other services to use, it is not publically accessible.
* ``depends_on`` will require other named docker container to start before this
  container.
* ``stop_grace_period`` is optional, but `enables a longer shutdown time`_ for
  a given docker container, if shutdown requires more than 10 seconds (e.g.
  writing data to database, etc).

.. code-block:: bash
  :caption: Turnup All Composed Services

  docker-compose up -d

* ``--remove-orphans`` will delete containers removed from the config.
* Use in conjunction with ``docker-compose pull`` to automatically update
  images, then restart containers with the new images.
* Any changes to containers will be re-configured automatically, including new
  images.
* services are auto labeled as ``{SERVICE}_{CONTAINER}_{INSTANCE}``. Service
  being the directory name, container being the container name and instance
  being the specific numbered instance (typically 1).
* **Ensure you are the right user**; standard sudo will launch jobs with your
  username. *Switch Users* or ``sudo su - root -c "docker-compose up -d"``.

Common Management Tasks
***********************
See `cheetsheet`_. Compose commands mirror standard ``docker`` commands but are
called with ``docker-compose``. Individual compose containers may be managed
with the ``docker`` command as well using the
``{SERVICE}_{CONTAINER}_{INSTANCE}`` moniker.

.. code-block:: bash
  :caption: Pull new images for composed Services.

  docker-compose pull

.. code-block:: bash
  :caption: List Running Services.

  docker ps

.. code-block::
  :caption: Pull a docker container to use.

  docker pull {REPO}/{CONTAINER}:{TAG}

* Pulls a copy of the container to local docker image store.
* Can store multiple tagged versions of a container.

.. code-block:: bash
  :caption: List containers.

  docker container ls -a

* ``-a`` is used to list *non-running* containers as well.

.. code-block:: bash
  :caption: Show stored images.

  docker images

.. code-block:: bash
  :caption: Remove an image from local storage.

  docker rmi {REPO}/{CONTAINER}:{TAG}

.. code-block:: bash
  :caption: Remove a container.

  docker rm {NAME}

* This removes a created container. It does *not* remove the image the container
  is based on.

.. code-block:: bash
  :caption: Open shell on running container.

  docker exec -it {NAME} /bin/bash

.. code-block:: bash
  :caption: Get all current configuration settings for a given container.

  docker inspect {NAME}

.. code-block:: bash
  :caption: Follow logs for running container.

  docker logs -f {NAME}

.. code-block:: bash
  :caption: Update all docker images already downloaded.

  docker images | grep -v REPOSITORY | awk '{print $1}' | xargs -L1 docker pull

.. code-block:: bash
  :caption: Stop all docker containers.

  docker stop $(docker ps -aq)

.. code-block:: bash
  :caption: Show docker container stats.

  docker stats {NAME}

* Remove ``{NAME}`` to display all running services.

Interactive Docker Shell that `Respects Terminal Size`_
*******************************************************
Dynamically re-size docker container shell terminal to whatever terminal you are
using.

.. code-block:: bash
  :caption: **0700 user user** ``~/.bash_profile``

  docker-shell() {
    sudo docker exec -it -u $2 $1 /bin/bash -c "stty cols $COLUMNS rows $LINES && /bin/bash";
  }
  export -f docker-shell

* usage: ``docker-shell {INSTANCE} {USER}``.

.. _docker-bridged-adapters:

Docker Bridged Adapters
***********************
By default Docker will add ``-P FORWARD DROP`` rule to `iptables to prevent`_
specific exploitation vectors for containers. Unfortunately, this is applied to
**all** interfaces, regardless of whatever interface docker uses; this rule is
re-applied everytime the service is started. `Iptables by default filters
bridged interfaces`_.

This will result in KVM virtual machines on a system with Docker to not be able
to use a Bridge for network communication. As a bridge is a layer 2 device, it
really shouldn't be filtering IP packets anyways. You can just disable bridged
adapters from applying the iptables. If you still use the bridge adapter for
system traffic, consider munging the filter instead.

.. code-block:: bash
  :caption: Disable IP filtering on bridged interfaces.

  echo "0" /proc/sys/net/bridge/bridge-nf-call-iptables
  echo "0" /proc/sys/net/bridge/bridge-nf-call-ip6tables
  echo "0" /proc/sys/net/bridge/bridge-nf-call-arptables

* This will validate bridging is fixed but not persist across reboots.

Update settings for sysctl as well as UFW sysctl:

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sysctl.conf``

  net.bridge.bridge-nf-call-ip6tables = 0
  net.bridge.bridge-nf-call-iptables = 0
  net.bridge.bridge-nf-call-arptables = 0

.. code-block:: bash
  :caption: **0644 root root** ``/etc/ufw/sysctl.conf``

  net.bridge.bridge-nf-call-ip6tables = 0
  net.bridge.bridge-nf-call-iptables = 0
  net.bridge.bridge-nf-call-arptables = 0

There is a `longstanding bug`_ bug with sysctl in debian/ubuntu not applying
``sysctl.conf`` properly with network settings. This can be resolved using a
root cronjob:

.. code-block:: bash
  :caption: ``sudo crontab -e``

  @reboot sleep 15; /sbin/sysctl -p

.. code-block:: bash
  :caption: Ensure settings are applied by rebooting and checking settings are set.

  reboot
  sysctl -a | grep bridge

Compose Containers on `Different Networks`_
*******************************************
Setup network isolation of compose containers to minimize exposure. By default
all containers will end up on the same default network. This enables network
`isolation`_ of containers.

Create a custom network named ``custom_net_name`` on the subnet
``172.40.0.0/16`` for this compose container. Containers will automatically
recieve an IP on this network when turning up.

.. code-block:: yaml
  :caption:  **0640 root staff** ``{SERVICE}/docker-compose.yml``

  networks:
    custom_net_name:
      driver: bridge
      ipam:
        config:
          - subnet: 172.40.0.0/16

Containers can be specified with static IP's within the compose definition.

.. code-block:: yaml
  :caption:  **0640 root staff** ``{SERVICE}/docker-compose.yml``

  services:
    my_container:
      ...
      networks:
        custom_net_name:
          ipv4_address: 172.40.1.1

Accessing Networks from Other Compose Containers
================================================
Custom networks may be explicitly accessed by other containers (e.g. a reverse
proxy) by explicitly defining them within the compose definition.

.. code-block:: yaml
  :caption:  **0640 root staff** ``{SERVICE}/docker-compose.yml``

  networks:
    custom_net_name:
      external: true
  ...
  services:
    my_proxy:
      networks:
        my_proxy_network:
        custom_net_name:

* ``custom_net_name`` is a network defined in another container. Once this is
  added, the proxy container will be able to do DNS resolution of container
  names as usual, including proxying traffic to that network.

Default Gateway is Not Correct
==============================
`Docker does not provide a way`_ to set the `appropriate default gateway`_ for
multi-network containers. This results in `non-deterministic`_ source IP
`routing`_.

.. warning::
  When a container is connected to multiple networks, its external connectivity
  is provided via the first non-internal network, in lexical order.

The current fix is to inspect the container and find the first *gateway* listed
in the connected networks. This will be the *default gateway* for the container.

There is currently no clean way to set a default gateway via compose.

.. code-block:: bash
  :caption: Inspect docker container to show networks and gateway.

  docker inspect {NAME}

Forward Traffic via Specific Interfaces
=======================================
Nginx can forward traffic via specific interfaces for *location* definitions
which may workaround this issue for specific containers.

.. code-block:: yaml
  :caption:  **0640 root staff** ``{SERVICE}/docker-compose.yml``

  networks:
    custom_net_name:
      external: true
  ...
  services:
    my_proxy:
      networks:
        my_proxy_network:
          ipv4_address: 172.1.1.1
        custom_net_name:
          ipv4_address: 172.2.1.1

* ``custom_net_name`` is a network defined in another container. Once this is
  added, the proxy container will be able to do DNS resolution of container
  names as usual, including proxying traffic to that network.

.. code-block:: bash
  :caption: Use IPv4 address for ``proxy_bind`` command for specific nginx
            locations.

  location / {
    proxy_bind 172.2.1.1;
    proxy_pass ...
  }

Explore `Image Filesystem`_
***************************
Container filesystems can be explored without launching the container by
specifying a replacement entrypoint. This is helpful for debugging issues.

.. code-block:: bash
  :caption: Explore container filesystem.

  docker run --rm -it --entrypoint=/bin/sh {IMAGE}

* ``--rm`` will automatically remove the container when finished executing.
* ``-it`` will launch an interactive terminal.
* ``-entrypoint`` will override the existing entrypoint for the image.

Copy Data From Container
************************
Files can be copied directly out of containers.

.. code-block:: bash
  :caption: Copy data from docker container.

  docker {NAME}:/local/container/file .

Tagging Docker Images
*********************
Docker images can be tagged with `multiple tags`_ for the same image.

.. code-block:: bash
  :caption: Create two tages for the same image.

  docker tag {ID} {USER}/{IMAGE}:0.2
  docker tag {ID} {USER}/{IMAGE}:latest

.. code-block:: bash
  :caption: Multiple tags during docker image build.

  docker build -t {USER}/{IMAGE}:0.2 -t {USER}/{IMAGE}:latest .
  docker push {USER}/{IMAGE}

Push Image to Docker Hub
************************
Login to Docker Hub and push via the correct tag.

.. code-block:: bash
  :caption: Login and push image based on tags.

  docker login
  docker push {USER}/{IMAGE}:{TAG}

Docker Container Not Getting Interrupt Signals
**********************************************
Caused by the container Dockerfile not properly using the ``Exec`` specification
for `the entrypoint script`_. Exec will hand over the process and enable signals
to propagate into the container when ``docker stop`` is issued.

.. code-block:: dockerfile
  :caption: Specify entrypoint properly in Dockerfile.

  ENTRYPOINT ["/my/entrypoint/script/with/signals"]


`GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown Error`_
**************************************************************
Docker push requires *gnome-keyring* to login by default and will fail producing
the error: *GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown*. This can be
bypassed by replacing the functionality with ``gnupg2`` and ``pass``.

.. code-block:: bash
  :caption: Install gnupg2 and pass to prevent error.

  apt install gnupg2 pass
  docker login
  docker push

.. _getting started: https://docs.docker.com/get-started/
.. _cheetsheet: https://github.com/wsargent/docker-cheat-sheet
.. _-t -d: https://stackoverflow.com/questions/30209776/docker-container-will-automatically-stop-after-docker-run-d
.. _Respects Terminal Size: https://stackoverflow.com/questions/38786615/docker-number-of-lines-in-terminal-changing-inside-docker/49281526#49281526
.. _iptables to prevent: https://serverfault.com/questions/162366/iptables-bridge-and-forward-chain
.. _longstanding bug: https://bugs.launchpad.net/ubuntu/+source/procps/+bug/50093
.. _Iptables by default filters bridged interfaces: https://serverfault.com/questions/431590/how-to-make-sysctl-network-bridge-settings-persist-after-a-reboot
.. _containers, even in read-only: https://www.lvh.io/posts/dont-expose-the-docker-socket-not-even-to-a-container/
.. _Compose with Containers: https://docs.docker.com/v17.09/compose/overview/
.. _values in XX:XX as Time: https://docs.docker.com/v17.09/compose/compose-file/#service-configuration-reference
.. _Different Networks: https://runnable.com/docker/docker-compose-networking
.. _isolation: https://www.docker.com/blog/docker-networking-design-philosophy/
.. _Image Filesystem: https://stackoverflow.com/questions/20813486/exploring-docker-containers-file-system
.. _GDBus.Error:org.freedesktop.DBus.Error.Service Unknown Error: https://stackoverflow.com/questions/50151833/cannot-login-to-docker-account
.. _the entrypoint script: https://hynek.me/articles/docker-signals/
.. _enables a longer shutdown time: https://docs.docker.com/compose/compose-file/#stop_grace_period
.. _multiple tags: https://stackoverflow.com/questions/31963525/is-it-possible-for-image-to-have-multiple-tags
.. _Login to Docker Hub: https://stackoverflow.com/questions/34434231/how-to-authenticate-for-docker-push
.. _Docker does not provide a way: https://github.com/docker/libnetwork/issues/1141#issuecomment-215522809
.. _non-deterministic: https://dustymabe.com/2016/05/25/non-deterministic-docker-networking-and-source-based-ip-routing/
.. _appropriate default gateway: https://stackoverflow.com/questions/36882945/change-default-route-in-docker-container
.. _routing: https://github.com/moby/moby/issues/21741
