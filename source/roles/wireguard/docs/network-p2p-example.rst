.. _service-wireguard-network-p2p-example:

Point to Point Example
######################
This setup enables a private network connection to the server, preventing other
clients on that network from communicating to other clients. DNS and any network
access not directly addressed to the private network will egress through the
client's standard network stack.

This creates a /24 network that all machines use, while only allowing point to
point communications from each client to the server.

Server
******
.. literalinclude:: source/server.conf
  :caption: **0600 root root** /etc/wireguard/server.conf

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@server

Clients
*******
.. literalinclude:: source/client.conf
  :caption: **0600 root root** /etc/wireguard/client.conf

.. warning::
  Windows clients do **not** use the ``SaveConfig`` option. Remove this line if
  configuring a Windows client.

.. code-block:: bash
  :caption: Bring up the tunnel for testing.

  systemctl enable wg-quick@client

Testing
*******
.. code-block:: bash
  :caption: Show server network status and ping a client.

  wg
  ping 172.31.255.250

.. code-block:: bash
  :caption: Show client network status and ping server. Pinging other clients should fail.

  wg
  ping 172.31.255.254
  ping 172.31.255.100
