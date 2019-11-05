.. _salt-state-management:

`State Management`_
###################
States apply specific configurations to minions. See `State Reference`_.

Any ``.sls`` file in :ref:`salt-master-file` will be evaluated as a SaLt State
file. Subdirectories can be referenced as packages via the dir name if there is
an ``init.sls`` file present. Directories do not require ``.sls`` files for
traversal.

.. code-block:: bash
  :caption: Directly apply a state to a minion.

  salt '*' state.sls {STATE FILE NAME} saltenv=prod
  salt-call state.sls {STATE FILE NAME} saltenv=prod

Any state files may be referenced in other state files, using dotted access
notation from that environments root to access them.

.. code-block:: bash
  :caption: Example of state package use in top file.

  ls -1 /srv/salt/static/prod/other/app/
  init.sls

.. code-block:: yaml
  :caption: **0644 salt salt** ``/srv/salt/static/prod/top.sls``

  prod:
    'my_host';
      - other.app

Install a Package
*****************

.. code-block:: yaml
  :caption: **0644 salt salt** ``/src/salt/static/prod/apache.sls``

  apache2:
    pkg:
      - installed

Deploy File with Content from Server
************************************

.. code-block:: bash

  ls -1 /srv/salt/static/prod/config
  .bashrc

.. code-block:: yaml
  :caption: **0644 salt salt** ``/srv/salt/static/prod/top.sls``

  prod:
    /root/.bashrc
      file.managed:
        - user: root
        - group: root
        - mode: 0600
        - source: salt://bachrc/bashrc

.. _State Management: https://docs.saltstack.com/en/2016.11/topics/tutorials/starting_states.html
.. _State Reference: https://docs.saltstack.com/en/latest/ref/states/