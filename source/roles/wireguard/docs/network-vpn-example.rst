.. _service-wireguard-network-vpn-example:

VPN Example
###########
Behaves like a traditional VPN network. All traffic and DNS lookups are routed
through the connection to be resolved in the VPN server location.

`Reference <https://www.ckn.io/blog/2017/11/14/wireguard-vpn-typical-setup/>`__

Server
******
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
******
.. literalinclude:: source/vpn-client.conf
  :caption: Route all traffic through VPN connection.

.. important::
  Set a custom DNS server if needed. DNS is resolved at the VPN server.

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@vpn-client

Testing
*******
From the client access the Internet and verify that your data is routed through
the VPN server.

A quick test can be verifying different IP's from https://www.whatismyip.com.
