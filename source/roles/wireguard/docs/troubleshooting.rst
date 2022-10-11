.. _service-wireguard-troubleshooting:

Troubleshooting
###############

Debugging
*********
Issues with wireguard connections can be debugged by enabling dynamic debug in
the kernel. Requires Kernel ``5.6``.

.. code-block:: bash
  :caption: Enable wireguard dynamic kernel debugging and show log.

  echo 'module wireguard +p' | sudo tee /sys/kernel/debug/dynamic_debug/control
  dmesg -wH

.. code-block:: bash
  :caption: Disable wireguard dynamic kernel debugging.

  echo 'module wireguard -p' | sudo tee /sys/kernel/debug/dynamic_debug/control

SSH not working, UFW allowing SSH, No NAT
*****************************************
Expresses as pings between clients through the wireguard server work correctly,
but SSH'ing fails. UFW on the wireguard server is enabled and allowing SSH
traffic. Disabling UFW allows SSH connections to happen.

Solution: Traffic needs to be tagged in IP tables to allow wireguard to
wireguard traffic to be forwarded; otherwise this is not tagged as inbound
traffic to the wireguard server in UFW and subsequently blocked.

.. code-block:: bash
  :caption: **0600 root root** /etc/wireguard/server.conf

  iptables -A FORWARD -i {INTERFACE} -o {INTERFACE} -m conntrack --ctstate NEW -j ACCEPT

`Reference <https://serverfault.com/questions/985482/wireguard-access-between-clients-ufw-block>`__
