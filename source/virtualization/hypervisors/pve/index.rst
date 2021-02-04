.. _pve:

Prxomox (PVE)
#############
Prepare a USB drive with the latest ISO image from the `Proxmox repository <https://www.proxmox.com/en/downloads/category/proxmox-virtual-environment>`_.

.. gport:: Ports Exposed (Proxmox)
  :port:     22,
             85,
             111,
             3128,
             5404-5405,
             5900-5999,
             8006,
             60000-60050
  :protocol: TCP,
             TCP,
             TCP/UDP,
             TCP,
             UDP,
             TCP,
             TCP,
             TCP
  :type:     Restricted (cluster; management),
             Restricted (cluster),
             Public,
             Public,
             Restricted (cluster),
             Public,
             Restricted (management),
             Restricted (cluster)
  :purpose:  SSH,
             Pvedaemon (listens 127.0.0.1:85) REST API,
             Rpcbind (NFS services),
             Spice proxy (client remote viewer),
             Corosync cluster traffic,
             VNC Web console websockets,
             Web Interface,
             Live Migrations
  :no_key_title:
  :no_caption:
  :no_launch:

  `Reference <https://pve.proxmox.com/wiki/Firewall#_ports_used_by_proxmox_ve>`__

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

  deb http://download.proxmox.com/debian buster pve-no-subscription

Remove the subscription repository.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/sources.list.d/pve-enterprise.list``

  #deb https://enterprise.proxmox.com/debian/pve buster pve-enterprise

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
This is only needed if ``LXC containers`` or ``promox`` will use wireguard. VM's
can use wireguard without it being enabled in the proxmox kernel.

.. todo::
  Remove `wireguard configuration <https://nixvsevil.com/posts/wireguard-in-proxmox-lxc/>`_
  when proxmox releases ``5.6`` kernel to stable (built-in to kernel).

Add debian backports for wireguard usage.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/sources.list``

  deb http://deb.debian.org/debian buster-backports main

.. code-block:: bash
  :caption: Update and install wireguard.

  apt update && apt install pve-headers
  apt install -t buster-backports wireguard-dkms
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

.. ggui:: Create management interface. 
  :key_title: datacenter --> {SERVER} --> system --> network --> create --> bridge
  :option:    Name,
              IPv4,
              Gateway,
              Autostart,
              VLAN Aware,
              Bridge ports
  :setting:   vmbr0,
              {SERVER MANAGEMENT CIDR ADDRESS},
              {GATEWAY ADDRESS},
              ☑,
              ☑,
              {ADAPTOR}
  :no_section:
  :no_launch:

  ``vmbr0`` is used as the management interface. Typical default adaptor is
  ``eno1``. The UI will show available adaptors.

  .. note::
    If there only a single adaptor in the system this is all that is needed;
    LXC/VM's will use ``vmbr0`` as a bridge (not recommended).

.. ggui:: Create bonded interface.
  :key_title: datacenter --> {SERVER} --> system --> network --> create --> bond
  :option:    Name,
              Autostart,
              Slaves,
              Mode,
              Hash policy
  :setting:   bond0,
              ☑,
              {ADAPTOR 1} {ADAPTOR 2},
              LACP (802.3ad),
              layer2+3
  :no_section:
  :no_launch:

  ``bond0`` is the bonded device the bridge will use. No IP should be set.
  Adaptors are shown in management interface and should be separated by a space.

  .. note::
    This assumes ``802.3ad`` has been enabled on the switch.
     
    .. ggui:: Create 802.3ad link aggregation.
      :key_title: unifi --> devices --> device --> port --> edit -->
                  profile overrides ---> operation --> aggregate
      :option:    aggregate ports
      :setting:   3-4
      :no_section:
      :no_launch:

      Unifi requires ``802.3ad`` ports to be next to each other. ``3-4`` used as
      example. :cmdmenu:`Apply Profile Override` to enable.

.. ggui:: Create bonded, bridged interface for LXC/VM's. 
  :key_title: datacenter --> {SERVER} --> system --> network --> create --> bridge
  :option:    Name,
              Autostart,
              VLAN Aware,
              Bridge ports
  :setting:   vmbr1,
              ☑,
              ☑,
              bond0
  :no_section:
  :no_launch:

  ``vmbr1`` is the bridge device used by LXC/VM's. No IP should be set.

.. ggui:: Setup Proxmox DNS Servers.
  :key_title: datacenter --> {SERVER} --> system --> dns
  :option:    DNS Server 1,
              DNS Server 2,
              DNS Server 3
  :setting:   {INTERNAL DNS SERVER},
              1.1.1.1,
              1.0.0.1
  :no_section:
  :no_launch:

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

.. ggui:: Create a new Cluster.
  :key_title: datacenter --> cluster --> create cluster
  :option:    Cluster Name,
              Cluster Network Link,
              Cluster Network IP
  :setting:   {NAME},
              0,
              {SERVER MANAGEMENT CIDR ADDRESS}
  :no_section:
  :no_launch:

  :cmdmenu:`datacenter --> cluster --> join information --> copy information`

.. ggui:: Add second server to cluster.
  :key_title: datacenter --> cluster --> join cluster
  :option:    Information,
              Password
  :setting:   {PASTE JOIN INFORMATION},
              {ROOT PASSWORD ON CLUSTER SERVER}
  :no_section:
  :no_launch:

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

.. ggui:: Create ``cluster`` IP set for firewall.
  :key_title: datacenter --> firewall --> ipset --> create
  :option:    IPSet,
              Comment
  :setting:   Cluster,
              pve servers
  :no_section:
  :no_launch:

.. ggui:: Add cluster IPs to cluster IP set.
  :key_title: datacenter --> firewall --> ipset --> Cluster --> add
  :option:    IP/CIDR,
              IP/CIDR
  :setting:   {PVE SERVER 1},
              {PVE SERVER 2}
  :no_section:
  :no_launch:

.. ggui:: Create ``management`` IP sets for firewall.
  :key_title: datacenter --> firewall --> ipset --> create
  :option:    IPSet,
              Comment
  :setting:   Management,
              pve remote access
  :no_section:
  :no_launch:

.. ggui:: Add cluster IPs to ``management`` IP set.
  :key_title: datacenter --> firewall --> ipset --> Management --> add
  :option:    IP/CIDR,
              IP/CIDR
  :setting:   {REMOTE CLIENT IP 1},
              {REMOTE CLIENT IP 2}
  :no_section:
  :no_launch:

.. ggui:: Create a ``proxmox`` ``Security Group`` for services.
  :key_title: datacenter --> firewall --> security group --> create
  :option:    Name,
              Comment
  :setting:   pve,
              pve hypervisor firewall
  :no_section:
  :no_launch:

.. ggui:: Live Migration Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              +cluster,
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              60000:60050,
              Live Migrations,
              nolog
  :no_section:
  :no_launch:

.. ggui:: Corosync cluster traffic Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              +cluster,
              {EMPTY},
              ☑,
              {EMPTY},
              udp,
              {EMPTY},
              5404:5405,
              Corosync cluster traffic,
              nolog
  :no_section:
  :no_launch:

.. ggui:: Web Interface Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              +management,
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              8006,
              Web Interface,
              nolog
  :no_section:
  :no_launch:

.. ggui:: VNC Web Console Websockets Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              {EMPTY},
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              5900:5999,
              VNC Web console websockets,
              nolog
  :no_section:
  :no_launch:

.. ggui:: Pvedaemon Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              +cluster,
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              85,
              pvedaemon (listens 127.0.0.1:85) REST API,
              nolog
  :no_section:
  :no_launch:

.. ggui:: SSH (Cluster traffic) Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              +cluster,
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              22,
              SSH (cluster traffic),
              nolog
  :no_section:
  :no_launch:

.. ggui:: SSH (Management traffic) Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              +management,
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              22,
              SSH (management traffic),
              nolog
  :no_section:
  :no_launch:

.. ggui:: Rpcbind (NFS services TCP) Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              {EMPTY},
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              111,
              rpcbind (NFS services),
              nolog
  :no_section:
  :no_launch:

.. ggui:: Rpcbind (NFS services UDP) Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              {EMPTY},
              {EMPTY},
              ☑,
              {EMPTY},
              udp,
              {EMPTY},
              111,
              rpcbind (NFS services),
              nolog
  :no_section:
  :no_launch:

.. ggui:: Spice proxy Rule.
  :key_title: datacenter --> firewall --> security group --> pve --> add
  :option:    Direction,
              Action,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              ACCEPT,
              {EMPTY},
              {EMPTY},
              ☑,
              {EMPTY},
              tcp,
              {EMPTY},
              3128,
              spice proxy (client remote viewer),
              nolog
  :no_section:
  :no_launch:

Enable the security group & add drop rule.

.. ggui:: Enable the security group.
  :key_title: datacenter --> firewall --> insert: security group --> pve
  :option:    Security Group,
              Interface,
              Enable
  :setting:   pve,
              {EMPTY},
              ☑
  :no_section:
  :no_launch:

.. ggui:: Add DROP Rule (disabled).
  :key_title: datacenter --> firewall --> add 
  :option:    Direction,
              Action,
              Interface,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              DROP,
              {EMPTY},
              {EMPTY},
              {EMPTY},
              ☐,
              {EMPTY},
              {EMPTY},
              {EMPTY},
              {EMPTY},
              Drop all other traffic,
              nolog
  :no_section:
  :no_launch:

.. note::
  Add unchecked (**not** enabled) and move to **bottom** of rule list.

Enable firewall & drop policy.

.. ggui:: Enable firewall.
  :key_title: datacenter --> firewall --> options 
  :option:    Input Policy,
              Firewall
  :setting:   ACCEPT,
              Yes
  :no_section:
  :no_launch:

.. warning::
  Set input policy before enabling firewall, or you will drop all traffic.

.. ggui:: Enable DROP policy Rule.
  :key_title: datacenter --> firewall --> Drop all other traffic 
  :option:    Enable
  :setting:   ☑
  :no_section:
  :no_launch:

Cluster Firewall
================
Set :ref:`pve-datacenter-firewall` first to load global ``pve`` security group.
Configure for each specific server in the cluster.

.. ggui:: Enabled the security group on cluster.
  :key_title: datacenter --> {SERVER} --> firewall --> insert: security group --> pve
  :option:    Security Group,
              Interface,
              Enable
  :setting:   pve,
              {EMPTY},
              ☑
  :no_section:
  :no_launch:

.. ggui:: Add DROP Rule (disabled).
  :key_title: datacenter --> {SERVER} --> firewall --> add 
  :option:    Direction,
              Action,
              Interface,
              Source,
              Destination,
              Enable,
              Macro,
              Protocol,
              Source port,
              Dest. port,
              Comment,
              Log level
  :setting:   in,
              DROP,
              {EMPTY},
              {EMPTY},
              {EMPTY},
              ☐,
              {EMPTY},
              {EMPTY},
              {EMPTY},
              {EMPTY},
              Drop all other traffic,
              nolog
  :no_section:
  :no_launch:

.. note::
  Add unchecked (**not** enabled) and move to **bottom** of rule list.

Enable firewall & drop policy.

.. ggui:: Enable firewall.
  :key_title: datacenter --> {SERVER} --> firewall --> options 
  :option:    Firewall
  :setting:   Yes
  :no_section:
  :no_launch:

.. ggui:: Enable DROP policy Rule.
  :key_title: datacenter --> firewall --> Drop all other traffic 
  :option:    Enable
  :setting:   ☑
  :no_section:
  :no_launch:

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

.. ggui:: Create container to host Docker.
  :key_title: datacenter --> {SERVER} --> RMB --> create ct
  :option:    General,
              › Hostname,
              › Unprivileged container,
              › password,
              Template,
              › Storage,
              › Template,
              Root Disk,
              › Storage,
              › Disk size,
              CPU,
              › Cores,
              Memory,
              › Memory
  :setting:   ,
              {HOST},
              ☑,
              {PASS},
              ,
              local,
              {CONTAINER IMAGE},
              ,
              local-lvm,
              20GB,
              ,
              64,
              ,
              125000
  :no_section:
  :no_launch:

  Memory is in ``MiB`` not ``MB``. Create but do **not** start container. Note
  the ID of the container.

Remove security constraints on container.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/pve/lxc/{ID}.conf``

  lxc.apparmor.profile: unconfined
  lxc.cgroup.devices.allow: a
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
``SLAAC`` IPv6 configuration information; appearing to have `no console <https://forum.proxmox.com/threads/no-console-with-proxmox-5-0-beta-2-and-debian-9-containers.35313/
>`_.
Disable IPv6 if not actively used.

See :ref:`additional-ubuntu-fixes-disable-ipv6`.

.. rubric:: References (Unused)

.. rubric:: GPU Passthru for Windows, Plex servers

#. `GPU passthru to Windows VM <https://www.youtube.com/watch?v=fgx3NMk6F54>`_
#. `Proxmox, Plex w/ PCI passhtru & hardware encoding <https://www.youtube.com/watch?v=-HCzLhnNf-A>`_
#. `Guide to GPU passthru <https://old.reddit.com/r/homelab/comments/b5xpua/the_ultimate_beginners_guide_to_gpu_passthrough/>`_

.. rubric:: Wireguard on unprivleged containers

#. `Wireguard use on unprivileged containers <https://securityboulevard.com/2019/04/howto-install-wireguard-in-an-unprivileged-container-proxmox/>`_

.. rubric:: Full disk encryption on Proxmox

#. `FDE proxmox installation <https://www.sidorenko.io/post/2019/09/full-encrypted-proxmox-installation/>`_
