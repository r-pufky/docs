.. _salt-linux-manual-install:

`Linux Manual Install`_
#######################
A minion will not send the initial cert request until the minion is started.
By default ``salt`` should resolve to an IP, which can be changed in the minion
configuration file.

Generally, you should manage the minion configuration file via salt after the
initial install and master connection.

Platform releases may be found at: https://repo.saltstack.com.

.. code-block:: bash
  :caption: **0644 root root** ``/etc/apt/sources.list.d/saltstack.list``

  deb [arch=amd64] http://repo.saltstack.com/py3/{DISTRO}/{VERSION}/amd64/latest {CODENAME} main

.. note::
  ``[arch=amd64]`` is required to prevent the *skipping acquire of configured
  file main/binary-i386/packages* message for `32 bit binaries on 64 bit
  systems`_.

.. code-block:: bash
  :caption: Add the salt repository signing key.

  wget -O - https://repo.saltstack.com/py3/{DISTRO}/{VERSION}/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -

.. code-block:: bash
  :caption: Install salt.

  sudo apt update && sudo apt install salt-minion

.. _Linux Manual Install: https://docs.saltstack.com/en/latest/topics/best_practices.html
.. _32 bit binaries on 64 bit systems: https://askubuntu.com/questions/741410/skipping-acquire-of-configured-file-main-binary-i386-packages-as-repository-x
