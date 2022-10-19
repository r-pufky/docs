.. _netplan:

Netplan
#######
Replacement for ``ifconfig`` scripts to abstract network configuration to *yaml*
files.

General Usage
*************
Usage is typically done by generating a plan and applying it. The old moniker of
``ifup``/``ifdown`` no longer applies. `bridge-utils`_ should not be used
independently with Netplan. Netplan should take care of *all* network
configuration.

Make changes in ``/etc/netplan/01-netcfg.yaml`` by default. See `reference`_ for
configuration options.

.. code-block:: bash
  :caption: Generate new configurations from the plan.

  netplan generate --debug

.. code-block:: bash
  :caption: Apply the network plan to the system.

  netplan --debug apply

.. code-block:: bash
  :caption: Check the status of generated devices.

  networkctl list

.. code-block:: bash
  :caption: Show all interfaces.

  ip a


Bridging
********
This is useful for providing a network interface to be used for VM's /
containers. The bridged network can be assigned an IP address directly and used
as well; however there seems to be an issue with using a bridge network with
KVM as well as the host network. See `reference`_ and `general bridging help`_.

In most cases for advanced configuration the base adapter *should not* be
configured for an IP address, the resulting bonded or bridged device should.

.. literalinclude:: source/01-netcfg-bridged-networks.yaml
  :caption: Two nics bridged together, using dhcp, ipv4, a specific MAC address
            with spanning tree and forward delay disabled. Original `bridged
            networks`_ reference.
  :linenos:

.. literalinclude:: source/01-netcfg-bonded-bridged-networks.yaml
  :caption: Two nics bonded together in the default configuration, with a bridge
            created on top of the bonded interface. Original `bonded bridged
            networks`_ reference.

.. literalinclude:: source/01-netcfg-bonded-with-bridge.yaml
  :caption: Three nics, two bonded together with a custom mode and primary set.
            The bridged network is a single card with spanning tree and forward
            delay disabled.

Default Route Issues
********************
Netplan does not `currently allow route or metric configuration`_ for DHCP
enabled device. This creates issues when there are multiple adapters all
connected at the same time -- the default route is last network brought up. This
works around the issue by `manually setting networkd`_ **after** netplan is run.

* Configure netplan as normal and note interface designations.
* Apply config.

.. code-block:: bash
  :caption: Copy desired default route adapter setting to ``/etc``.

  netplan --debug apply
  cp /run/systemd/network/10-netplan-{ADAPTER}.network /etc/systemd/network

.. literalinclude:: source/10-netplan-bond0.network
  :caption: **0644 root root** ``/etc/systemd/network/10-netplan-{ADAPTER}.network``
  :linenos:
  :emphasize-lines: 10

.. note::
  ``RouteMetric`` higher number is lower priority. Default is 100. Whenever a
  new netplan configuration is applied ensure this this is still set.

.. _netplan-kvm-issue:

KVM Specific Issues
*******************
There seems to be an issue with Netplan bridging, KVM, and using the same
bridged for host networking traffic as well as VM traffic. The workaround is to
have a separate bridged adapter. This is a `longstanding bug`_ with KVM and can
be fixed by modifying `sysctl settings`_.

.. important::
  By default Docker will add ``-P FORWARD DROP`` rule to iptables to prevent
  specific exploitation vectors for containers. Unfortunately, this is applied
  to **all** interfaces, regardless of whatever interface docker uses; this rule
  is re-applied everytime the docker service is started. `Iptables by default
  filters bridged interfaces`_.

This will result in KVM virtual machines on a system with Docker to not be able
to use a Bridge for network communication. As a bridge is a layer 2 device, it
really shouldn't be filtering IP packets anyways. You can just disable bridged
adapters from applying the iptables. If you still use the bridge adapter for
system traffic, *consider* munging the filter instead.

Test Fix
========
.. code-block:: bash
  :caption: Disable IP filtering on bridged interfaces.

  echo "0" /proc/sys/net/bridge/bridge-nf-call-iptables
  echo "0" /proc/sys/net/bridge/bridge-nf-call-ip6tables
  echo "0" /proc/sys/net/bridge/bridge-nf-call-arptables

.. note::
  This will not persist across reboots, verify everything now works.

Permenant Fix
=============
Make the fix permenant by updating settings for ``sysctl`` as well as UFW
`sysctl settings`_.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/sysctl.conf``
  :lineno-start: 79

  net.bridge.bridge-nf-call-ip6tables = 0
  net.bridge.bridge-nf-call-iptables = 0
  net.bridge.bridge-nf-call-arptables = 0

.. code-block:: bash
  :caption: **0644 root root** ``/etc/ufw/sysctl.conf``
  :lineno-start: 43

  net.bridge.bridge-nf-call-ip6tables = 0
  net.bridge.bridge-nf-call-iptables = 0
  net.bridge.bridge-nf-call-arptables = 0

There is a `longstanding bug`_ with ``sysctl`` in debian based systems not
applying ``sysctl.conf`` properly with network settings. This can be resolved
using a root cronjob:

.. code-block:: bash
  :caption: ``crontab -e``

  @reboot sleep 15; /sbin/sysctl -p

.. code-block:: bash
  :caption: Ensure settings are applied by rebooting and verifying.

  reboot
  sysctl -a | grep bridge

.. rubric:: References

#. `Bridging under Ubuntu 18.04 and Netplan <https://webby.land/2018/04/27/bridging-under-ubuntu-18-04/>`_

.. _reference: https://netplan.io/reference
.. _bridge-utils: https://ubuntuforums.org/showthread.php?t=2391884
.. _bonded bridged networks: https://serverfault.com/questions/910955/problems-with-setting-up-bonding-on-netplan-ubuntu-server-18-04
.. _bridged networks: https://www.tomechangosubanana.com/2018/kvm-bridged-to-the-lan-with-dhcp/
.. _general bridging help: https://askubuntu.com/questions/971126/17-10-netplan-config-with-bridge
.. _Iptables by default filters bridged interfaces: https://serverfault.com/questions/162366/iptables-bridge-and-forward-chain
.. _longstanding bug: https://bugs.launchpad.net/ubuntu/+source/procps/+bug/50093
.. _sysctl settings: https://serverfault.com/questions/431590/how-to-make-sysctl-network-bridge-settings-persist-after-a-reboot
.. _currently allow route or metric configuration: https://bugs.launchpad.net/netplan/+bug/1781652
.. _manually setting networkd: https://askubuntu.com/questions/1042582/how-to-set-default-route-with-netplan-ubuntu-18-04-server-2-nic