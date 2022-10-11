.. _service-unifi-controller:

Unifi Controller
################
Manage Ubiquity Unifi APs & Switches.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   basic-configuration

.. role:: radarr
  :galaxy:      https://galaxy.ansible.com/r_pufky/unifi
  :source:      https://github.com/r-pufky/ansible_unifi
  :service_doc: https://help.ui.com/hc/en-us/categories/6583256751383-UniFi
  :update:      2022-10-09
  :open:

  You may copy your existing configuration to ``unifi_data`` directory
  adjusting paths.

  * Read :ref:`example-vlan-network` for detailed configuration instructions on
    an example network.

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml
