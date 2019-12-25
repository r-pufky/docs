.. _salt-minion-configuration:

Minion Configuration
####################
Initial configuration to connect to the Salt Master server as configured in
:ref:`salt-master-configuration`. Salt Master should be setup to manage the minion
configurations remotely.

``/etc/salt/minion`` is the minion flat-file config, however making changes in
``/etc/salt/minion.d/`` for each specific conifugration area is preferred to
clarify minion changes, as well as enabling easy management on the config. Any
file with ``.conf`` will be loaded in this directory and take precedence over
the flat file.

Windows minion configuration files are located in ``c:\salt\conf\minion`` and
``c:\salt\conf\minion.d\`` respectively.

Schedule Section
****************
Determines how often Salt Minion runs, when it runs and how many resources it is
allowed to use.

This will enable the Salt Minion, apply state on boot, check state every 60
minutes and have a max of two running processes at once.

.. literalinclude:: source/_schedule.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/_schedule.conf``
  :linenos:

File Section
************
Files are compared to master files using *sha512* hashes.

.. literalinclude:: source/file.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/file.conf``
  :linenos:

Logging Section
***************
Set minions to only log errors by default.

.. literalinclude:: source/logging.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/logging.conf``
  :linenos:

Pillar Section
**************
Minion will use the same pillar environment as the salt environment and not
raise immediate errors if requested pillar data does not exist (default Python
values will be used instead).

.. literalinclude:: source/pillar.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/pillar.conf``
  :linenos:

Primary Section
***************
Minion will run as root and check in every 60 seconds on the default port,
verifying files and permissions on startup. It will not timeout waiting for a
reponse from the Master, and will not cache pillar data.

.. literalinclude:: source/primary.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/primary.conf``
  :linenos:
  :emphasize-lines: 4

.. _salt-minion-configuration-security-section:

Security Section
****************
Require 4096 bit keys for signing as well as accepting Master messages. PKI
access is restricted and the Master server is independently verified using a
fingerprint.

.. literalinclude:: source/security.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/security.conf``
  :linenos:
  :emphasize-lines: 4-5,10

.. note::
  Copy ``master_sign.pub`` to ``/etc/salt/pki/minion``. See Master
  :ref:`salt-master-configuration-security-section`.

.. note::
  For the initial configuration ``master_finger`` does not need to be setup,
  however it is highly recommended to seed configuration files to always
  maintain a chain of trust by `verifying the master service independently`_.

  .. code-block:: bash
    :caption: Determine Salt Master fingerprint (on Salt Master).

    salt-key -f master.pub

`Startup Section`_
******************
Defines the default startup states for Salt Minion. Launch minion into
``highstate``.

.. literalinclude:: source/startup.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/startup.conf``
  :linenos:

State Section
*************
Defines the default state and state options to use for minion runs. Run minions
using the ``prod`` environment.

.. literalinclude:: source/state.conf
  :caption: **0644 root root** ``/etc/salt/minion.d/state.conf``
  :linenos:

.. _Startup Section: https://docs.saltstack.com/en/latest/ref/states/startup.html
.. _verifying the master service independently: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-salt-master-and-minion-servers-on-ubuntu-14-04