.. _salt-common-issues:

Common Issues
#############
Common issues encountered during use and development.

Run Salt Minion with Debugging
******************************
.. code-block:: bash

  systemctl stop salt-minion
  salt-minion -l debug

Run Salt Master with Debugging
******************************
.. code-block:: bash

  systemctl stop salt-master
  salt-master -l debug

Debug jinja Templates
*********************
This will enable debug logging with custom messages and variables.

.. code-block:: jinja

  {%- do salt.log.debug('my_var: ' ~ my_var) %}


Minon Frequently Times Out or does Not Connect
**********************************************
There is a bug where pillar data needs to be refreshed before a minion can
connect. This is solved by `forcing a pillar refresh then applying state`_.

.. code-block:: bash

  salt {MINION} saltutil.refresh_pillar

.. _salt-common-issues-no-return:

Minion did not return. [Not connected].
***************************************
Expresses as ``salt-call`` working correctly locally on minion, but command
issued from the Salt Master fails with this message. Generally caused by the
minion not checking in with the master within the timeout period for the
command, or the Salt Master being moved to another server.

.. code-block:: bash
  :caption: Verify the Salt Minion can ping the Salt Master.

  systemctl stop salt-minion
  salt-call test.ping
  nc -v -z {MASTER} 4505
  nc -v -z {MASTER} 4506

.. code-block:: bash
  :caption: Remove the minion from Salt Master (Salt Master).

  salt-key -d {MINION}

.. code-block:: bash
  :caption: Restart the Minion (Salt Minion).

  systemctl restart salt-minion

.. code-block:: bash
  :caption: Re-add to Salt Master (Salt Master).

  salt-key -a {MINION}

.. note::
  Ping should be successful and both ports should be open. Run Minion in
  ``debug`` mode for more info if re-adding does not work.

.. _salt-common-issues-jinja:

Rendering SLS '{PILLAR DATA}' failed: Jinja variable ...
********************************************************
Be sure to expose required pillar data for nodegroups; otherwise states will
fail with the error:

.. pull-quote::
  *Rendering SLS '{PILLAR DATA}' failed: Jinja variable ...*

No Top file or External Nodes Data Matches Found
************************************************
Typically caused by bad file resolution or default environment the minion is
running in.

.. code-block:: bash
  :caption: Run Minion in debug mode.

  systemctl stop salt-minion
  salt-minion -l debug

.. code-block:: bash
  :caption: Run Master in debug mode.

  systemctl stop salt-master
  salt-master -l debug

.. code-block:: bash
  :caption: Force highstate from master or locally if failed.

  salt {MINION} state.highstate saltenv=prod
  salt-call -l debug state.apply saltenv=prod

Show Avaliable Files to Minions
*******************************
.. code-block:: bash

  salt-run fileserver.file_list saltenv=dev

Clear Minion Cache
******************
Stop the minion and delete cache in ``/var/cache/salt/minion``.

.. code-block:: bash

  salt-call saltutil.clear_cache
  salt {MINION} saltutil.clear_cache

.. note::
  * Only the local or remote call needs to be made.
  * Must run with ``root`` perms to execute.

.. _forcing a pillar refresh then applying state: https://github.com/saltstack/salt/issues/32144