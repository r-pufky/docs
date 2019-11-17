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

`Bootstrap Install`_
********************
Bootstrap install will automatically setup and install a salt minion on a
machine, including related dependencies, such as apt repositories, if needed.

.. danger::
  This does not validate the bootstrap script before executing it. A manual
  install (or setting up a trusted install script) is preferred to randomly
  downloading scripts and executing them from the Internet. See
  :ref:`salt-minion-manual` for manual steps.

.. code-block:: bash
  :caption: Install a salt minion that uses the Python 3 environment.

  curl https://bootstrap.saltstack.com/stable/bootstrap-salt.sh -o salt.sh
  salt.sh -x python3

.. _salt-minion-manual:

`Linux Manual Install`_
***********************
A minion will not send the initial cert request until the minion is started.
By default ``salt`` should resolve to an IP, which can be changed in the minion
configuration file.

Generally, you should manage the minion configuration file via salt after the
initial install and master connection.

Platform releases may be found at: http://repo.saltstack.com/py3/.

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

`Windows Manual Install`_
*************************
:download:`Latest Windows Minion Installer <https://repo.saltstack.com/windows/>`

Installer can be launched from the `CLI or GUI`_, dependencies are included with
the installer. The minion will be installed to ``C:\salt``.

.. code-block:: powershell
  :caption: The salt-minion can be managed like a normal windows service.

  sc start salt-minion
  net start salt-minion

Windows CLI Install
===================
.. code-block:: powershell
  :caption: Installing Windows Minion from powershell (as admin).

  Salt-Minion-2019.2.0-Py3-AMD64-Setup.exe /S /master={SALT MASTER} /minion-name={MINION NAME} /start-minion-delayed

Windows GUI Install
===================
* Specify the master name.
* Specify the minion name.
* Optionally provide a default configuration file.
* Enable delayed start (allows highstates requiring reboots to work).

Minion Configuration
********************
Initial configuration to connect to the Salt Master server as configured in
:ref:`salt-master-configuration`. Salt Master should be setup to manage the minion
configurations remotely.

``/etc/salt/minion`` is the minion flat-file config, however making changes in
``/etc/salt/minion.d/`` for each specific conifugration area is preferred to
clarify minion changes, as well as enabling easy management on the config. Any
file with ``.conf`` will be loaded in this directory and take precedence over
the flat file.

Windows minion configuration files are located in ``C:\salt\conf\minion`` and
``C:\salt\conf\minion.d\`` respectively.

Schedule Section
================
Determines how often Salt Minion runs, when it runs and how many resources it is
allowed to use.

This will enable the Salt Minion, apply state on boot, check state every 60
minutes and have a max of two running processes at once.

.. literalinclude:: source/minion/_schedule.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/_schedule.conf``
  :linenos:

File Section
============
Files are compared to master files using *sha512* hashes.

.. literalinclude:: source/minion/file.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/file.conf``
  :linenos:

Logging Section
===============
Set minions to only log errors by default.

.. literalinclude:: source/minion/logging.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/logging.conf``
  :linenos:

Pillar Section
==============
Minion will use the same pillar environment as the salt environment and not
raise immediate errors if requested pillar data does not exist (default Python
values will be used instead).

.. literalinclude:: source/minion/pillar.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/pillar.conf``
  :linenos:

Primary Section
===============
Minion will run as root and check in every 60 seconds on the default port,
verifying files and permissions on startup. It will not timeout waiting for a
reponse from the Master, and will not cache pillar data.

.. literalinclude:: source/minion/primary.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/primary.conf``
  :linenos:
  :emphasize-lines: 4

Security Section
================
Require 4096 bit keys for signing as well as accepting Master messages. PKI
access is restricted and the Master server is independently verified using a
fingerprint.

.. literalinclude:: source/minion/security.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/security.conf``
  :linenos:
  :emphasize-lines: 8

.. note::
  For the initial configuration ``master_finger`` does not need to be setup,
  however it is highly recommended to seed configuration files to always
  maintain a chain of trust by `verifying the master service independently`_.

  .. code-block:: bash
    :caption: Determine Salt Master fingerprint (on Salt Master).

    salt-key -f master.pub

`Startup Section`_
==================
Defines the default startup states for Salt Minion. Launch minion into
``highstate``.

.. literalinclude:: source/minion/startup.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/startup.conf``
  :linenos:

State Section
=============
Defines the default state and state options to use for minion runs. Run minions
using the ``prod`` environment.

.. literalinclude:: source/minion/state.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/state.conf``
  :linenos:

.. _Salt Minion: https://www.linode.com/docs/security/ssl/create-a-self-signed-tls-certificate
.. _Linux Manual Install: https://docs.saltstack.com/en/latest/topics/best_practices.html
.. _Windows Manual Install: https://repo.saltstack.com/#windows
.. _CLI or GUI: https://docs.saltstack.com/en/latest/topics/installation/windows.html
.. _Startup Section: https://docs.saltstack.com/en/latest/ref/states/startup.html
.. _32 bit binaries on 64 bit systems: https://askubuntu.com/questions/741410/skipping-acquire-of-configured-file-main-binary-i386-packages-as-repository-x
.. _Bootstrap Install: https://github.com/saltstack/salt-bootstrap
.. _verifying the master service independently: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-salt-master-and-minion-servers-on-ubuntu-14-04