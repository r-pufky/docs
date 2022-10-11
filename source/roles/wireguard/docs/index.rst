.. _service-wireguard:

Wireguard
#########
Modern state-of-the-art VPN designed to be simplier and faster that IPsec and
openVPN.

.. toctree::
   :hidden:
   :maxdepth: -1

   key-generation
   linux-service
   windows-service
   initramfs
   network-p2p-example
   network-vpn-example
   troubleshooting

.. role:: wireguard
  :galaxy:      https://galaxy.ansible.com/r_pufky/wireguard
  :source:      https://github.com/r-pufky/ansible_wireguard
  :service_doc: https://www.wireguard.com/
  :ref:         https://www.wireguard.com/papers/wireguard.pdf
  :update:      2022-10-08
  :open:

  Only the server endpoint needs to be exposed publically. Clients can globally
  roam as long as they have working Internet connections and can send UDP
  traffic to the given port.

  * Role handles all steps that are provided in this documentation.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml

InitRAMFS
*********
.. literalinclude:: ../defaults/main/initramfs.yml

Adapters
********
.. literalinclude:: ../defaults/main/adapter.yml