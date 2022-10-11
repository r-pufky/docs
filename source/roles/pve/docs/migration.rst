.. _pve-migration:

Migration
#########
Migration to PVE from other hypervisors and docker container imports.

Docker Migration
****************
Proxmox can run docker in a LXC container until services are de-dockerized and
moved.

.. danger::
  **high** security risk. Most container security benefits are removed to enable
  docker to run in an LXC container. Migrate these services ASAP!

Enable container filesystem overlay for docker support.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/modules-load.d/modules.conf``

  aufs
  overlay

.. code-block:: bash

  reboot

.. gui::    Create container to host Docker
  :path:    datacenter --> {SERVER} --> {RMB} --> create ct
  :value0:  General,
  :value1:  › Hostname, {HOST}
  :value2:  › Unprivileged container, ☑
  :value3:  › password, {PASS}
  :value4:  Template,
  :value5:  › Storage, {LOCAL}
  :value6:  › Template, {CONTAINER IMAGE}
  :value7:  Root Disk,
  :value8:  › Storage, local-lvm
  :value9:  › Disk size, 20GB
  :value10: CPU,
  :value11: › Cores, 64
  :value12: Memory,
  :value13: › Memory, 125000

  Memory is in ``MiB`` not ``MB``. Create but do **not** start container. Note
  the ID of the container.

Remove security constraints on container.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/pve/lxc/{ID}.conf``

  lxc.apparmor.profile: unconfined
  lxc.cgroup2.devices.allow: a
  lxc.cap.drop:

.. code-block:: bash
  :caption: Start container and `install docker <https://docs.docker.com/engine/install/ubuntu/>`_.

  apt update && apt upgrade
  apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  apt-key fingerprint 0EBFCD88
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  apt update && apt install docker-ce docker-ce-cli containerd.io

Enable overlay filesystem for docker.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/docker/daemon.json``

  {
      "storage-driver": "overlay2"
  }

.. code-block:: bash

  service docker restart

Map proxmox ZFS drive to container.

.. code-block:: bash
  :caption: Mount the ZFS volume for usage (proxmox shell).

  pct set {COTAINER ID} -mp{XX} mp=/host/dir,/container/mount/point

.. note::
  ``XX`` is the numeric mount point, starting at zero. See
  ``/etc/pve/nodes/NODE/lxc/{ID}.conf`` for available mount points.

  Reboot container for the mountpoint to be added.

`Reference <https://danthesalmon.com/running-docker-on-proxmox/>`__

`Reference <https://old.reddit.com/r/Proxmox/comments/g3wozs/best_way_to_run_docker_in_proxmox/>`__
