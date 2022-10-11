.. _service-pihole:

`Pi-Hole`_
##########
Block nefarious websites & Ads.

.. toctree::
   :hidden:
   :maxdepth: -1

   basic-configuration
   troubleshooting

.. role:: pihole
  :galaxy:      https://galaxy.ansible.com/r_pufky/pihole
  :source:      https://github.com/r-pufky/ansible_pihole
  :service_doc: https://wiki.servarr.com/radarr
  :update:      2022-10-08
  :open:

  Clients will send DNS requets to Pi-Hole. Pi-Hole will either block, resolve
  or foward those requests to the router. The router will be able to resolve
  local DNS names and forward remaining unknown queries to upstream DNS
  servers.

  Optionally, if the router supports *destination NAT*, all DNS traffic will be
  routed directly to *Pi-Hole*. This catches hard-coded DNS servers that many
  phone apps, IoT devices, and applications use.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

.. note::
  FTL API should not be acessible from any other interface.

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
