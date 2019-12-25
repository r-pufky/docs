.. _salt-frequent-commands:

Frequent Commands
#################
Most commands support *globbing* and *regex* matching on Minions and Grains to
execute commands. See :ref:`salt-common-issues` for additional debugging
information.

General Master Commands
***********************
Run Command On Minions From Salt Master
=======================================
.. code-block:: bash

  salt {MINION} cmd.run 'ifconfig'
  salt -G os:ubuntu cmd.run 'df -h'

Get Status of All Minions
=========================
.. code-block:: bash

  salt-run manage.status

Show Minions On A Subnet
========================
.. code-block:: bash

  salt -S '10.5.5.0/24' network.ip_addrs

Show Avaliable Grains On Minions
================================
.. code-block:: bash

  salt {MINION} grains.items

List Active Jobs
================
.. code-block:: bash

  salt-run jobs.active

.. note::
  Useful for long-running comamnds (e.g. 'no response' commands) where the
  command will not finish before`timeout` is reached. See `jobs`_ and
  :ref:`salt-common-issues-no-return`.

`Generate New Master Certificates`_
===================================
Salt Master uses a RSA 4096bit key and a OpenSSL public key.

.. code-block:: bash

  ssh-keygen -t rsa -b 4096 -f master.pem
  openssl rsa -in master.pem -pubout -out master.pub

.. note::
  These keys should have **no password**. Replace existing files in
  ``/etc/salt/pki/master`` and ensure Minions are updated accordingly. See
  Minion :ref:`salt-minion-configuration-security-section`.

General Minion Commands
***********************
Useful for testing as well as immediately applying changes outside of the minion
run window.

Run A Specific State
====================
Useful to isolate failures or apply a specific state change.

.. code-block:: bash

  sudo salt-call -l debug state.sls {STATE NAME} pillarenv=dev saltenv=dev

Manual Minion Run with Specific Environments
============================================
.. code-block:: bash

  salt {MINION} state.highstate pillarenv=dev saltenv=dev
  salt-call state.highstate pillarenv=dev saltenv=dev

Print Only `Changes or Errors`_
===============================
By default ``state.highstate`` will print detailed information. This will focus
output on changes and errors.

.. code-block:: bash

  salt {MINION} state.highstate saltenv=prod --state-output=changes
  salt {MINION} state.highstate saltenv=prod --state-output=mixed

.. note::
  * ``changes`` will log standard messages on changes and errors.
  * ``mixed`` will log terse messages for changes and standard messages for
    errors.

.. _Changes or Errors: https://stackoverflow.com/questions/15953082/is-there-a-way-to-display-only-changes-and-errors
.. _jobs: https://docs.saltstack.com/en/latest/ref/runners/all/salt.runners.jobs.html#salt.runners.jobs.list_job
.. _Generate New Master Certificates: https://docs.mirantis.com/mcp/q4-18/mcp-operations-guide/saltstack-operations/salt-master-cert/replace-ssh-rsa.html