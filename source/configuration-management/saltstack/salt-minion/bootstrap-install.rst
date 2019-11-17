.. _salt-bootstrap-install:

`Bootstrap Install`_
####################
Bootstrap install will automatically setup and install a salt minion on a
machine, including related dependencies, such as apt repositories, if needed.

.. danger::
  This does not validate the bootstrap script before executing it. A manual
  install (or setting up a trusted install script) is preferred to randomly
  downloading scripts and executing them from the Internet. See
  :ref:`salt-linux-manual-install` or :ref:`salt-windows-manual-install` for
  manual steps.

.. code-block:: bash
  :caption: Install a salt minion that uses the Python 3 environment.

  curl https://bootstrap.saltstack.com/stable/bootstrap-salt.sh -o salt.sh
  salt.sh -x python3

.. _Bootstrap Install: https://github.com/saltstack/salt-bootstrap