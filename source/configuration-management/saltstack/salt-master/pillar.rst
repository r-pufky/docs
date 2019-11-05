.. _salt-using-pillar:

`Using Pillar`_
###############
Pillar manages dynamic client data sent to minions; it also can handle GPG
encrypted blocks and only decrypt those blocks for minions who have access. This
also enables you to store your configuration in a repository without worrying
about leaking secrets. See :ref:`salt-master-pillar` for master pillar directory
setup.

Pillar top.sls
**************
Specifies how minions are matched to determine what environment a minion gets
data from. These should be matched to the structure in :ref:`salt-master-file`.
``top.sls`` files must exist for each environment, and additional ones may be
used to logically categorize data to be consumed `Using Pillar`_.

Pillar Environment Data
***********************
By default data is merged and applied based on where the minion is defined in
top files. You can specify a specific environment (and are required to when
using ``pillar_source_merging_strategy: none``) to get pillar values for that
environment:

.. code-block:: bash

  pillarenv=dev

.. code-block:: bash

  pillarenv=prod

See :ref:`salt-gpg` for encrypting pillar data.

.. _Using Pillar: https://docs.saltstack.com/en/latest/topics/tutorials/pillar.html