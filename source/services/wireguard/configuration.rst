.. _service-wireguard-configuration:

Wireguard Configuration
#######################
Standard configuration for Wireguard VPN. Assumes wireguard server is running on
a Debian host.

.. gport:: Ports (Wireguard)
  :port:     51820
  :protocol: UDP
  :type:     Public
  :purpose:  Wireguard Server endpoint.
  :no_key_title:
  :no_caption:
  :no_launch:

Only the server endpoint needs to be exposed publically. Clients can globally
roam as long as they have working Internet connections and can send UDP traffic
to the given port.

Key Generation
**************
Public/Private keys need to be generated for each machine using wireguard. A
barebones utility is provided, generated keys are not OS specific.

.. code-block:: bash
  :caption: **0755 user user** wggen

  #!/bin/bash
  # Generate wireguard keys.
  WG=/usr/bin/wg
  TEE=/usr/bin/tee

  if [ -z "$1" ]; then
      echo "Requires name for output files."
      exit 1
  else
      name=$1
  fi

  ${WG} genkey | ${TEE} ${1}.key | ${WG} pubkey > ${1}.pub
  chmod 0400 ${1}.{key,pub}

.. note::
  Standard precautions should be used for private key material. The private key
  will enable anyone to impersonate that client on the VPN.

Point To Point Private Network
******************************
This setup enables a private network connection to the server, preventing other
clients on that network from communicating to other clients. DNS and any network
access not directly addressed to the private network will egress through the
client's standard network stack.

This creates a /24 network that all machines use, while only allowing point to
point communications from each client to the server.

Server
======
.. literalinclude:: source/server.conf
  :caption: **0600 root root** /etc/wireguard/server.conf

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@server

Clients
=======
.. literalinclude:: source/client.conf
  :caption: **0600 root root** /etc/wireguard/client.conf

.. warning::
  Windows clients do **not** use the ``SaveConfig`` option. Remove this line if
  configuring a Windows client.

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@client

Testing
=======
.. code-block:: bash
  :caption: Show server network status and ping a client.

  wg
  ping 172.31.255.250

.. code-block:: bash
  :caption: Show client network status and ping server. Pinging other clients should fail.

  wg
  ping 172.31.255.254
  ping 172.31.255.100

VPN Network
***********
Behaves like a traditional VPN network. All traffic and DNS lookups are routed
through the connection to be resolved in the VPN server location.

Server
======
.. code-block:: bash
  :caption: Enabled IP traffic forwarding on ``iptables``.

  echo 1 > /proc/sys/net/ipv4/ip_forward
  echo 1 > /proc/sys/net/ipv6/ip_forward

.. code-block:: bash
  :caption: **0644 root root** /etc/sysctl.conf

  net.ipv4.ip_forward = 1
  net.ipv6.conf.all.forwarding = 1

.. literalinclude:: source/vpn-server.conf
  :caption: Automatically adjust ``iptables`` rules to allow forwarded traffic when VPN is up.

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@server

Client
======
.. literalinclude:: source/vpn-client.conf
  :caption: Route all traffic through VPN connection.

.. important::
  Set a custom DNS server if needed. DNS is resolved at the VPN server.

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@vpn-client

Testing
=======
From the client access the Internet and verify that your data is routed through
the VPN server.

A quick test can be verifying different IP's from https://whatismyip.com.
