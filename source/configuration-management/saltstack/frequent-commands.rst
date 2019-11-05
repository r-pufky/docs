.. _salt-frequent-commands:

Frequent Commands
#################
Most commands support *globbing* and *regex* matching on Minions and Grains to
execute commands. See :ref:`salt-common-issues` for additional debugging
information.

General Master Commands
***********************

.. code-block:: bash
  :caption: Run a command on Minion and all Ubuntu machines from Salt Master (Salt Master).

  salt {MINION} cmd.run 'ifconfig'
  salt -G os:ubuntu cmd.run 'df -h'

.. code-block:: bash
  :caption: Get status of all minions.

  salt-run manage.status

.. code-block:: bash
  :caption: Show minions on a subnet.

  salt -S '10.5.5.0/24' network.ip_addrs

.. code-block:: bash
  :caption: Show avaliable grains on minions.

  salt {MINION} grains.items

.. code-block:: bash
  :caption: List active jobs.

  salt-run jobs.active

.. note::
  Useful for long-running comamnds (e.g. 'no response' commands) where the
  command will not finish before`timeout` is reached. See `jobs`_ and
  :ref:`salt-common-issues-no-return`.

General Minion Commands
***********************
Useful for testing as well as immediately applying changes outside of the minion
run window.

Manual Minion Run with Specific Environments
********************************************
.. code-block:: bash

  salt {MINION} state.highstate pillarenv=dev saltenv=dev

Print Only `Changes or Errors`_
*******************************
By default ``state.highstate`` will print detailed information. This will focus
output on changes and errors.

.. code-block:: bash

  salt {MINION} state.highstate saltenv=prod --state-output=changes
  salt {MINION} state.highstate saltenv=prod --state-output=mixed

* ``changes`` will log standard messages on changes and errors.
* ``mixed`` will log terse messages for changes and standard messages for
  errors.

.. _Changes or Errors: https://stackoverflow.com/questions/15953082/is-there-a-way-to-display-only-changes-and-errors
.. _jobs: https://docs.saltstack.com/en/latest/ref/runners/all/salt.runners.jobs.html#salt.runners.jobs.list_job