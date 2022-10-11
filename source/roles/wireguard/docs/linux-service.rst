.. _service-wireguard-linux-service:

Linux Setup
###########
5.6+ Kernels required unless explicitly backported.

Debian
******
Debian **Bullseye** and later (``5.6`` Kernels+) have wireguard built into the
Kernel as well as the packages in the main repository. No additional setup needs
to be done other than installing the ``wireguard`` package. Releases before
Buster are not supported.

**Buster** setup:

.. code-block:: bash
  :caption: **0644 root root** /etc/apt/sources.list.d/unstable-wireguard.list

  deb https://deb.debian.org/debian/ unstable main

.. code-block:: bash
  :caption: **0644 root root** /etc/apt/preferences.d/wireguard-limit-unstable

  Package: *
  Pin: release a=unstable
  Pin-Priority: 150

.. code-block:: bash
  :caption: Install Kernel headers, wireguard, and reboot.

  apt update && apt upgrade
  apt install linux-headers-amd64
  apt install wireguard

Ubuntu
******
Ubuntu **18.04** and later have wireguard built in. Just install the
``wireguard`` package.

Autostart Tunnel as Service
***************************
Tunnels may be autostarted as services.

.. code-block:: bash
  :caption: Start tunnel on boot.

  systemctl enable wg-quick@{TUNNEL}

.. code-block:: bash
  :caption: Start tunnel on demand.

  systemctl status/stop/start/restart wg-quick@{TUNNEL}

`Reference <https://community.hetzner.com/tutorials/install-and-configure-wireguard-vpn-debian>`__
