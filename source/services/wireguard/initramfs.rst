.. _service-wireguard-initramfs:

wireguard-initramfs
###################
Enable wireguard while booting.

This enables the used of Dropbear and related unlock utilities over a wireguard
network before a system has booted.

Install
*******
Install :ref:`service-wireguard` first, then install the latest package from
https://github.com/r-pufky/wireguard-initramfs:

.. code-block:: bash
  :caption: Install wireguard-initramfs

  wget https://github.com/r-pufky/wireguard-initramfs/archive/refs/tags/2021-07-04.tar.gz
  tar xvf 2021-07-04.tar.gz
  cd wireguard-initramfs-2021-07-04
  make install

Configure
*********
.. code-block:: bash
  :caption: **0644 root root** /etc/wireguard-initramfs/config

  # Wireguard interface name.
  INTERFACE=example_vpn

  # CIDR wireguard interface address.
  INTERFACE_ADDR=172.31.255.10/32

  # Peer public key (server's public key).
  PEER_PUBLIC_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

  # IP:PORT of the peer (server); any reachable IP/DNS.
  PEER_ENDPOINT=wg.example.com:51820

  # Client Private key. Specify location of file containing only the private key.
  CLIENT_PRIVATE_KEYFILE=/etc/wireguard-initramfs/private_key

  # Persistent Keepalive. Required to ensure connection for non-exposed ports.
  PERSISTENT_KEEPALIVES=25

  # Allowed IP's (CIDR) on wireguard; for boot this should be the peer (server).
  ALLOWED_IPS=172.31.255.254/32

.. code-block:: bash
  :caption: **0600 root root** /etc/wireguard-initramfs/private_key

  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

.. note::
  Most systems do not encrypt ``/boot`` so private key material is exposed and
  considered **compromised/untrusted**. Boot wireguard network should be
  **different** & untrusted, versus the network used after booting. Always
  restrict ports and access on the wireguard server.

.. code-block:: bash
  :caption: Add wireguard to initramfs.

  update-initramfs -u
  update-grub
  reboot

Dropbear Remote Unlock
**********************
Unlock an encrypted root filesystem remotely on boot over wireguard.

Ensure that both Dropbear and :ref:`service-wireguard`,
:ref:`service-wireguard-initramfs` are setup and working correctly.
Then set dropbear to only listen over wireguard network:

.. code-block:: bash
  :caption: **0644 root root** /etc/dropbear-initramfs/config

  DROPBEAR_OPTIONS='... -p 172.31.255.10:22 ...'

.. code-block:: bash
  :caption: Update dropbear config in initramfs.

  update-initramfs -u
  update-grub
  reboot

* The boot wireguard network should be separate from your normal wireguard
  network. Protect the server endpoint and restrict all ports not needed.
* The boot and running wireguard networks should have different keys.
* Set UFW on the host as well for further protection.
