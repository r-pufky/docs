.. _salt-minion:

`Salt Minion`_
##############
All minions by default need to be able to resolve the ``salt`` hostname to the
salt-master. This can be changed in the minion configuration files.

Minions should be run as ``root``. Minions require root to properly install
software, update apt and execute commands.

.. note::
  If you plan on installing docker, you need to use ``source_interface_name`` or
  ``source_address`` when configuring the minion, otherwise salt could pick up
  the Docker interface and use that. This will cause the minion to be unable to
  respond to the master.

Related Material:

* :ref:`salt-bootstrap-install` for automatic bootstrap installation.
* :ref:`salt-linux-manual-install` for installing salt-minion on Linux.
* :ref:`salt-windows-manual-install` for installing salt-minion on Windows.
* :ref:`salt-minion-configuration` for configuring salt-minion.

.. toctree::
  :hidden:
  :maxdepth: -1

  bootstrap-install
  linux-manual-install
  windows-manual-install
  minion-configuration

.. _Salt Minion: https://www.linode.com/docs/guides/create-a-self-signed-tls-certificate/
