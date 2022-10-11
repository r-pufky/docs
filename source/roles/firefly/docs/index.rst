.. _service-firefly:

Firefly III
###########
Self-hosted financial manager.

.. toctree::
   :hidden:
   :maxdepth: -1

   network
   basic-configuration
   troubleshooting

.. role:: firefly
  :galaxy:      https://galaxy.ansible.com/r_pufky/firefly
  :source:      https://github.com/r-pufky/ansible_firefly
  :service_doc: https://www.firefly-iii.org/
  :update:      2022-10-09
  :open:

  A database backend should already exist with either a pre-existing firefly
  database, or full permissions to create tables in the database when applying
  the role. Local storage should be locked down to prevent sensitive data from
  leaking.

  * ``firefly_app_url`` should remain localhost as it does not effect proxied
    or non-proxied connections. Existing documentation on the web is wrong.
  * ``firefly_trusted_proxies`` should be set to the known proxy IP address so
    all other connections are denied by default. Setting to ``**`` will enable
    all connections (insecure).

  ..  collapse:: README.md

    .. literalinclude:: ../README.md

Ports
*****
.. literalinclude:: ../defaults/main/ports.yml

Defaults
********
.. literalinclude:: ../defaults/main/main.yml

Config
******
.. literalinclude:: ../defaults/main/config.yml
