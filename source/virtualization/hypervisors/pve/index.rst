.. _pve:

Prxomox (PVE)
#############
Prepare a USB drive with the latest ISO image from the `Proxmox repository <https://www.proxmox.com/en/downloads/category/proxmox-virtual-environment>`_.

Ports
*****
.. ports:: Proxmox Ports
  :value0:          22;     {TCP}; {RESTRICTED}; SSH (cluster, management only) 
  :value1:          85;     {TCP}; {RESTRICTED}; REST API Pvedaemon on
                                                 127.0.0.1:85 (cluster only)
  :value2:         111; {TCP/UDP};     {PUBLIC}; Rpcbind (NFS services)
  :value3:        3128;     {TCP};     {PUBLIC}; Spice proxy (client remote viewer)
  :value4:   5404-5405;     {UDP}; {RESTRICTED}; Corosync cluster traffic
                                                 (cluster only)
  :value5:   5900-5999;     {TCP};     {PUBLIC}; VNC Web console websockets
  :value6:        8006;     {TCP}; {RESTRICTED}; Web Interface (management only)
  :value7: 60000-60050;     {TCP}; {RESTRICTED}; Live Migrations (cluster only)
  :ref:    https://pve.proxmox.com/wiki/Firewall#_ports_used_by_proxmox_ve
  :update: 2021-01-20
  :delim: ;
  :open:

Install Service
***************
#. Select ``Install Proxmox VE``
#. Accept EULA
#. Select installation drive with default options
#. Set country, timezone, and keyboard layout
#. Enter ``root`` password & valid ``email`` address
#. Set network interface. Use static settings and **FQDN** hostname
#. Start installation

.. important::
  The correct **FQDN** must be used as `changing the hostname <https://pve.proxmox.com/wiki/Renaming_a_PVE_node>`_
  afterwards is error prone and not recommended for clustering.

Access the default webface for proxmox at ``https://{HOST}:8006``.

`Reference <https://www.youtube.com/watch?v=7OVaWaqO2aU>`__

Configuration
*************
The default installation is open, insecure, and must be configured.
Configuration management is not used to minimize attack surface and resource
consumption. Reboot server after steps are completed to ensure changes are
applied.

`Reference <https://www.youtube.com/watch?v=GoZaMgEgrHw>`__

Enable Automatic & Non-subscription Updates
===========================================
Only changed or added lines are shown for files in this section.

.. code-block:: bash

  apt install vim unattended-upgrades

Add the non-subscription repository.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/sources.list``

  deb http://download.proxmox.com/debian/pve {DEBIAN CODENAME} pve-no-subscription

Remove the subscription repository.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/sources.list.d/pve-enterprise.list``

  #deb https://enterprise.proxmox.com/debian/pve {DEBIAN CODENAME} pve-enterprise

Enable automatic updates.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/apt.conf.d/20auto-upgrades``

  APT::Periodic::Update-Package-Lists "1";
  APT::Periodic::Unattended-Upgrade "1";

Enable unattended upgrades (only changed lines shown). Proxmox servers should be
rebooted at different times.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/apt.conf.d/50unattended-upgrades``

  Unattended-Upgrade::Origins-Pattern {
    "origin=Debian,codename=${distro_codename}-updates";
    ...
  }

  Unattended-Upgrade::Mail "root";
  Unattended-Upgrade::MailOnlyOnError "true";
  Unattended-Upgrade::Remove-Unused-Dependencies "true";
  Unattended-Upgrade::Automatic-Reboot "true";
  Unattended-Upgrade::Automatic-Reboot-Time "05:00";
  Acquire::http::Dl-Limit "0";

.. code-block:: bash
  :caption: Validate unattended-upgrades configuration.

  unattended-upgrade -d

.. code-block:: bash
  :caption: Upgrade server to latest patches.

  apt update && apt upgrade && apt dist-upgrade

Add Local User, Sudo, & Secure SSH
==================================
Proxmox requires ``root`` SSH for `cluster communications <https://old.reddit.com/r/Proxmox/comments/as6koe/prevent_ssh_login_as_root_without_keys/>`_.
This uses public key authentication, so disable password authentication.
Add a local user for primary login and ``sudo`` configuration use.

.. code-block:: bash
  :caption: Add a local user.

  apt install sudo
  adduser {USER}
  usermod -aG sudo {USER}

See :ref:`service-ssh-configuration` to generate a public key for the new user
and add to ``/home/{USER}/.ssh/authorized_keys``.

.. important::
  Start an SSH connection to prevent lockout while configuring.

Force ``sshd`` to use public key only (only explicitly enabled lines are shown).

.. code-block:: bash
  :caption: **0644 root root** ``/etc/ssh/sshd_config``

  LoginGraceTime 2m
  PermitRootLogin prohibit-password
  StrictModes yes
  MaxAuthTries 3
  MaxSessions 10

  PubkeyAuthentication yes
  PasswordAuthentication no
  ChallengeResponseAuthentication no
  UsePAM yes
  X11Forwarding yes
  PrintMotd no
  AcceptEnv LANG LC_*
  Subsystem       sftp    /usr/lib/openssh/sftp-server

.. code-block:: bash

  service sshd restart

.. note::
  Confirm that SSH publickey login works with new user before continuing.

Enable fail2ban
===============
Enable automatic banning for SSH and `Web GUI <https://documentation.online.net/en/dedicated-server/tutorials/administration/proxmox-first-step>`_
login failures.

.. code-block:: bash

  apt install fail2ban

Add proxmox WebUI filter.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/fail2ban/filter.d/proxmox.conf``

  # Fail2Ban configuration file
  #
  # Author: Cyril Jaquier
  #
  # $Revision: 569 $
  #

  [Definition]

  # Option:  failregex
  # Notes.:  regex to match the password failure messages in the logfile. The
  #          host must be matched by a group named "host". The tag "<HOST>" can
  #          be used for standard IP/hostname matching and is only an alias for
  #          (?:::f{4,6}:)?(?P<host>\S+)
  # Values:  TEXT
  #

  failregex = pvedaemon\[.*authentication failure; rhost=<HOST> user=.* msg=.*

  # Option:  ignoreregex
  # Notes.:  regex to ignore. If this regex matches, the line is ignored.
  # Values:  TEXT
  #
  ignoreregex =

Enable SSH & WebUI banning.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/fail2ban/jail.d/proxmox.conf``

  [sshd]
  enabled  = true
  port     = ssh
  filter   = sshd
  logpath  = /var/log/auth.log

  [proxmox]
  enabled = true
  port    = https,http,8006
  filter  = proxmox
  logpath = /var/log/daemon.log

Restart service and verify jails are started.

.. code-block:: bash

  service fail2ban restart
  cat /var/log/fail2ban.log

Add Wireguard Kernel Support
============================
This is only needed if ``LXC containers`` or ``promox`` will use wireguard.
VM's can use wireguard without it being enabled in the proxmox kernel.

As of proxmox 7, wireguard backports are no longer needed (running kernel
``5.11``).

.. code-block:: bash
  :caption: Update and install wireguard.

  apt update && apt install pve-headers
  apt install wireguard wireguard-tools wireguard-dkms
  modprobe wireguard

Enabled wireguard on boot.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/modules-load.d/modules.conf``

  wireguard

Enable Hardware Virtualization (IOMMU)
======================================

.. code-block:: bash
  :caption: **0644 root root** ``/etc/default/grub``

  GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on"

.. note::
  * AMD: ``IOMMU`` & ``SVM`` enabled in BIOS. Use ``amd_iommu`` for grub.
  * Intel: ``IOMMU`` & ``VT-d`` enabled in BIOS. Use ``intel_iommu`` for grub.

Enable hardware virtualization kernel modules on boot.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/modules-load.d/modules.conf``

  vfio
  vfio_iommu_type1
  vfio_pci
  vfio_virqfd

.. code-block:: bash
  :caption: Update boot image with IOMMU changes.

  update-grub
  reboot

Setup Networking
================
Both management and LCX/VM adaptors should be used through ``bridges`` and not
the physical adaptor directly. This allows for hardware changes and updates with
minimal reconfiguration & failure.

In proxmox 7, you may need to install ``ifupdown2`` if container networking is
`not working <https://forum.proxmox.com/threads/update-to-7-network-problem.92452/>`_.

.. gui::   Create management interface
  :path:   datacenter --> {SERVER} --> system --> network --> create --> bridge
  :value0: Name, vmbr0
  :value1: IPv4, {IP_CIDR}
  :value2: Gateway, {GATEWAY}
  :value3: Autostart, ☑
  :value4: VLAN Aware, ☑
  :value5: Bridge ports, {ADAPTOR}

  ``vmbr0`` is used as the management interface. Typical default adaptor is
  ``eno1``. The UI will show available adaptors. Server address should be on the
  ``management`` VLAN.

  .. note::
    If there only a single adaptor in the system this is all that is needed;
    LXC/VM's will use ``vmbr0`` as a bridge (not recommended).

.. gui::   Create bonded interface
  :path:   datacenter --> {SERVER} --> system --> network --> create --> bond
  :value0: Name, bond0
  :value1: Autostart, ☑
  :value2: Slaves, {ADAPTOR 1} {ADAPTOR 2}
  :value3: Mode, LACP (802.3ad)
  :value4: Hash policy, layer2+3

  ``bond0`` is the bonded device the bridge will use. No IP should be set.
  Adaptors are shown in management interface and should be separated by a space.

  .. note::
    This assumes ``802.3ad`` has been enabled on the switch.
     
    .. gui::   Create 802.3ad link aggregation.
      :path:   unifi --> devices --> device --> port --> edit -->
               profile overrides ---> operation --> aggregate
      :value0: aggregate ports, 3-4

      Unifi requires ``802.3ad`` ports to be next to each other. ``3-4`` used as
      example. :cmdmenu:`Apply Profile Override` to enable.

.. gui::   Create bonded, bridged interface for LXC/VM's
  :path:   datacenter --> {SERVER} --> system --> network --> create --> bridge
  :value0: Name, vmbr1
  :value1: Autostart, ☑
  :value2: VLAN Aware, ☑
  :value3: Bridge ports, bond0

  ``vmbr1`` is the bridge device used by LXC/VM's. No IP should be set.

.. gui::   Setup Proxmox DNS Servers
  :path:   datacenter --> {SERVER} --> system --> dns
  :value0: DNS Server 1, {INTERNAL_DNS}
  :value1: DNS Server 2, 1.1.1.1
  :value2: DNS Server 3, 1.0.0.1

.. _pve-add-datacenter-cluster:

Add to Datacenter Cluster
*************************
Servers can be `added to a cluster <https://pve.proxmox.com/wiki/Cluster_Manager>`_
to share configuration and migration of LXC/VM's. Any number of servers can be
added; HA is only available after ``3`` servers are in the cluster.

.. important::
  Server **must** be added to an existing cluster **before** adding LXC/VM's,
  otherwise they will be deleted when VM info is sync'ed from the first cluster
  server. This is done to prevent duplicate LXC/VM ID's which will cause
  migration and management issues.

  If an existing proxmox server has LCX/VM's, the cluster should be created on
  that machine, and subsequent servers added afterwards.

  Be sure that server IP and hostnames are in the correct state.

.. note::
  This can be done even after restricting SSH. Copy the join info and connect
  with the root password for the first proxmox install. It may appear to fail,
  but this is due to the services being reloaded. Just reload the site (either
  server) and they should appear connected.

.. gui::   Create a new Cluster
  :path:   datacenter --> cluster --> create cluster
  :value0: Cluster Name, {NAME}
  :value1: Cluster Network Link, 0
  :value2: Cluster Network IP, {IP_CIDR}

  :cmdmenu:`datacenter --> cluster --> join information --> copy information`

.. gui::   Add second server to cluster
  :path:   datacenter --> cluster --> join cluster
  :value0: Information, {PASTE JOIN INFORMATION}
  :value1: Password, {PASS}

Firewall
********
Restrict hypervisor access to cluster and specific management clients. See
:ref:`pve-add-datacenter-cluster` to setup clustering before this step if using
multiple servers.

`Reference <https://pve.proxmox.com/wiki/Firewall>`__

`Reference <https://lowendspirit.com/postinstall-configuration-of-proxmox-ve-6-2>`__

`Reference <https://www.kiloroot.com/secure-proxmox-install-sudo-firewall-with-ipv6-and-more-how-to-configure-from-start-to-finish/>`__

.. _pve-datacenter-firewall:

Datacenter Firewall
===================
Datacenter firewall defines rules that can be applied to all systems in the
cluster.

.. important::
  Open a SSH connection to the server before enabling firewall in case of
  lockout. Disable active firewall with ``pve-firewall stop`` if access breaks.
  Remember to re-enable this.

  LXC/VM bridged traffic is unaffected unless per LXC/VM firewalls are
  enabled.

.. gui:: Create ``cluster`` IP set for firewall
  :path: datacenter --> firewall --> ipset --> create
  :value0: IPSet, Cluster
  :value1: Comment, pve servers

.. gui::   Add cluster IPs to cluster IP set
  :path:   datacenter --> firewall --> ipset --> Cluster --> add
  :value0: IP/CIDR, {PVE SERVER 1}
  :value1: IP/CIDR, {PVE SERVER 2}

.. gui::   Create ``management`` IP sets for firewall
  :path:   datacenter --> firewall --> ipset --> create
  :value0: IPSet, Management
  :value1: Comment, pve remote access

.. gui::   Add cluster IPs to ``management`` IP set
  :path:   datacenter --> firewall --> ipset --> Management --> add
  :value0: IP/CIDR, {REMOTE CLIENT IP 1}
  :value1: IP/CIDR, {REMOTE CLIENT IP 2}

.. gui::   Create a ``proxmox`` ``Security Group`` for services
  :path:   datacenter --> firewall --> security group --> create
  :value0: Name, pve
  :value1: Comment, pve hypervisor firewall

.. gui::    Live Migration Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, +cluster
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 60000:60050
  :value9:      Comment, Live Migrations
  :value10:   Log level, nolog

.. gui::    Corosync cluster traffic Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, +cluster
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {UDP}
  :value7:  Source port,
  :value8:   Dest. port, 5404:5405
  :value9:      Comment, Corosync cluster traffic
  :value10:   Log level, nolog

.. gui::    Web Interface Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, +management
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 8006
  :value9:      Comment, Web Interface
  :value10:   Log level, nolog

.. gui::    VNC Web Console Websockets Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source,
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 5900:5999
  :value9:      Comment, VNC Web console websockets
  :value10:   Log level, nolog

.. gui::    Pvedaemon Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, +cluster
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 85
  :value9:      Comment, pvedaemon (listens 127.0.0.1:85) REST API
  :value10:   Log level, nolog

.. gui::    SSH (Cluster traffic) Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, +cluster
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 22
  :value9:      Comment, SSH (cluster traffic)
  :value10:   Log level, nolog

.. gui::    SSH (Management traffic) Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, +management
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 22
  :value9:      Comment, SSH (management traffic)
  :value10:   Log level, nolog

.. gui::    Rpcbind (NFS services TCP) Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, 
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 111
  :value9:      Comment, rpcbind (NFS services)
  :value10:   Log level, nolog

.. gui::    Rpcbind (NFS services UDP) Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, 
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {UDP}
  :value7:  Source port,
  :value8:   Dest. port, 111
  :value9:      Comment, rpcbind (NFS services)
  :value10:   Log level, nolog

.. gui::    Spice proxy Rule
  :path:    datacenter --> firewall --> security group --> pve --> add
  :value0:    Direction, {IN}
  :value1:       Action, {ACCEPT}
  :value2:       Source, 
  :value3:  Destination,
  :value4:       Enable, ☑
  :value5:        Macro,
  :value6:     Protocol, {TCP}
  :value7:  Source port,
  :value8:   Dest. port, 3128
  :value9:      Comment, spice proxy (client remote viewer)
  :value10:   Log level, nolog

Enable the security group & add drop rule.

.. gui::   Enable the security group
  :path:   datacenter --> firewall --> insert: security group --> pve
  :value0: Security Group, pve
  :value1: Interface,
  :value2: Enable, ☑

.. gui::    Add DROP Rule (disabled)
  :path:    datacenter --> firewall --> add 
  :value0:    Direction, {IN}
  :value1:       Action, {DROP}
  :value2:    Interface,
  :value3:       Source, 
  :value4:  Destination,
  :value5:       Enable, ☐
  :value6:        Macro,
  :value7:     Protocol,
  :value8:  Source port,
  :value9:   Dest. port,
  :value10:      Comment, Drop all other traffic
  :value11:   Log level, nolog

.. note::
  Add unchecked (**not** enabled) and move to **bottom** of rule list.

Enable firewall & drop policy.

.. gui::   Enable firewall
  :path:   datacenter --> firewall --> options 
  :value0: Input Policy, {ACCEPT}
  :value1:     Firewall, {YES}

.. warning::
  Set input policy before enabling firewall, or you will drop all traffic.

.. gui::   Enable DROP policy Rule
  :path:   datacenter --> firewall --> Drop all other traffic 
  :value0: Enable, ☑

Cluster Firewall
================
Set :ref:`pve-datacenter-firewall` first to load global ``pve`` security group.
Configure for each specific server in the cluster.

.. gui::   Enabled the security group on cluster
  :path:   datacenter --> {SERVER} --> firewall --> insert: security group --> pve
  :value0: Security Group, pve
  :value1: Interface,
  :value2: Enable, ☑

.. gui::    Add DROP Rule (disabled)
  :path:    datacenter --> {SERVER} --> firewall --> add 
  :value0:    Direction, {IN}
  :value1:       Action, {DROP}
  :value2:    Interface,
  :value3:       Source, 
  :value4:  Destination,
  :value5:       Enable, ☐
  :value6:        Macro,
  :value7:     Protocol,
  :value8:  Source port,
  :value9:   Dest. port,
  :value10:      Comment, Drop all other traffic
  :value11:   Log level, nolog

.. note::
  Add unchecked (**not** enabled) and move to **bottom** of rule list.

Enable firewall & drop policy.

.. gui::   Enable firewall
  :path:   datacenter --> {SERVER} --> firewall --> options 
  :value0: Firewall, {YES}

.. gui::   Enable DROP policy Rule
  :path:   datacenter --> firewall --> Drop all other traffic 
  :value0: Enable, ☑

Remove Subscription Notice
**************************
This will prompt on every login. `Disable notification <https://johnscs.com/remove-proxmox51-subscription-notice/>`_.

.. code-block:: bash
  :caption: Disable subscription notice.

  sed -Ezi.bak "s/(Ext.Msg.show\(\{\s+title: gettext\('No valid sub)/void\(\{ \/\/\1/g" /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js && systemctl restart pveproxy.service

.. note::
  This will disconnect you if executing through the promox web UI. Clear browser
  cache (:cmdmenu:`shift + reload`) and reconnect to download new javascript.

Mount External ZFS Pool
***********************
ZFS utils are already installed. ZFS can be directly imported on the cluster and
will automatically appear in the WebUI afterwards.

.. code-block:: bash

  zpool import {POOLNAME}

Add ISOs
********
ISOs may be uploaded via the GUI
:cmdmenu:`datacenter --> {SERVER} --> local --> iso images --> upload` or
directly to ``/var/lib/vz/template/iso/`` if large.

Add Container Templates
***********************
Templates are updated `via the GUI <https://pve.proxmox.com/pve-docs/chapter-pct.html#pct_container_images>`_
:cmdmenu:`datacenter --> {SERVER} --> local --> ct templates` or command line.

.. code-block:: bash
  
  pveam update
  pveam available
  pveam download {STORAGE} {NAME}

Docker Migration
****************
Proxmox can run docker in a LXC container until services are de-dockerized and
moved.

`Reference <https://danthesalmon.com/running-docker-on-proxmox/>`__

`Reference <https://old.reddit.com/r/Proxmox/comments/g3wozs/best_way_to_run_docker_in_proxmox/>`__

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
  :path:    datacenter --> {SERVER} --> RMB --> create ct
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

Migrate from XCP
****************
See :ref:`xcp-exporting-vm-disks` to export disks first.

.. code-block:: bash
  :caption: Copy disks to server.

  scp {VM}.raw {SERVER}:/var/lib/vz/images/

Create new VM with **same** disk size in ``local-lvm``. This should mirror
the existing VM configuration in the other hypervisor, including MAC, CPU, Disk,
and Memory. Ensure VM is off.

.. code-block:: bash
  :caption: Find VM mounted disk and copy data to it.

  lvdisplay
  dd if=/var/lib/vz/images/{VM}.raw bs=1M of=/dev/pve/{VM DISK}

.. note::
  VM disk labels are generally in the format of ``vm-{ID}-disk-{NUMBER}``.

.. tip::
  Start the VM. Verify that ``/etc/network/interfaces`` use the correct
  interfaces for the new VM.

Troubleshooting
***************

ascii codec can't decode byte 0xe2 in position
==============================================
Sed :ref:`pve-corrupted-terminal`.

.. _pve-corrupted-terminal:

Failed to run vncproxy
======================
Root cause is ssh vncproxy proxy tunnel between pve nodes is
`not auto-accepted. <https://forum.proxmox.com/threads/task-error-failed-to-run-vncproxy.49954/>`_.

VM consoles can be access on each local cluster node, but not on remote cluster
nodes. May be confirmed by manually ssh'ing to other nodes and confirming that
the *connection is denied* or the *host key has changed*. Frequently happens
when node host keys are regenerated.

Resolve by clearing root and host `known_hosts` and sync'ing pve certificates.

.. code-block:: bash
  :caption: On affected nodes

  rm /root/.ssh/known_hosts
  rm /etc/ssh/ssh_known_hosts
  pvecm updatecerts

Wrong Timezone
==============
Containers assume UTC. Explicitly set timezone.

.. code-block:: bash

  timedatectl
  timedatectl list-timezones
  timedatectl set-timezone America/Los_Angeles

Corrupted Terminal Characters or No UTF-8 Support
=================================================
Containers do not have `locals set by default <https://old.reddit.com/r/Proxmox/comments/dhgez0/console_utf8/>`_.

Specify default locales for the container to use.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/default/locale``

  LANG="en_US.UTF-8"
  LANGUAGE="en_US:en"
  LC_CTYPE="en_US.UTF-8"
  LC_NUMERIC="en_US.UTF-8"
  LC_TIME="en_US.UTF-8"
  LC_COLLATE=en_US.UTF-8
  LC_MONETARY="en_US.UTF-8"
  LC_MESSAGES=en_US.UTF-8
  LC_PAPER="en_US.UTF-8"
  LC_NAME="en_US.UTF-8"
  LC_ADDRESS="en_US.UTF-8"
  LC_TELEPHONE="en_US.UTF-8"
  LC_MEASUREMENT="en_US.UTF-8"
  LC_IDENTIFICATION="en_US.UTF-8"

.. code-block:: bash
  :caption: Update locales and save.

  locale-gen en_US.UTF-8
  dpkg-reconfigure --frontend=noninteractive locales
  update-locale LAN=en_US.UTF-8

LXC Long Boot Times or No Console
=================================
Debian based systems will pause for up to ``5`` minutes on boot waiting for
``SLAAC`` IPv6 configuration information; appearing to have `no console <https://forum.proxmox.com/threads/no-console-with-proxmox-5-0-beta-2-and-debian-9-containers.35313/>`_.
Disable IPv6 if not actively used.

See :ref:`additional-ubuntu-fixes-disable-ipv6`.

.. rubric:: References (Unused)

.. rubric:: GPU Passthru for Windows, Plex servers
On proxmox 7, use ``cgroup2`` in place of ``cgroup``.

#. `GPU passthru to Windows VM <https://www.youtube.com/watch?v=fgx3NMk6F54>`_
#. `Proxmox, Plex w/ PCI passhtru & hardware encoding <https://www.youtube.com/watch?v=-HCzLhnNf-A>`_
#. `Guide to GPU passthru <https://old.reddit.com/r/homelab/comments/b5xpua/the_ultimate_beginners_guide_to_gpu_passthrough/>`_

.. rubric:: Wireguard on unprivleged containers

#. `Wireguard use on unprivileged containers <https://securityboulevard.com/2019/04/howto-install-wireguard-in-an-unprivileged-container-proxmox/>`_

.. rubric:: Full disk encryption on Proxmox

#. `FDE proxmox installation <https://www.sidorenko.io/post/2019/09/full-encrypted-proxmox-installation/>`_
