.. _salt-nodegroups:

`Nodegroups`_
#############
Nodegroups allow the automatic grouping and application of states to minions
based on minion attributes. These are applied for all matches. Commonly used to
apply a based configuration to specific types of OS, environment, or setup.

Create Nodegroups
*****************
Add node configuration to the salt master and restart for the nodegroups to be
picked up.

.. literalinclude:: ../source/master/nodegroups.conf
  :caption: **0644 root root** ``/etc/salt/master.d/nodegroups.conf``
  :linenos:

* This will create two nodegroups, one matching ``os_family`` grain to a debian
  based system (e.g. will apply to debian, ubuntu, etc), and one matching debian
  specifically.
* See `Compound Matchers`_ for matching syntax.

.. code-block:: bash

  systemctl restart salt-master

Apply State to Nodegroups
*************************
States can now be applied to nodegroups and layered based on setup.

.. literalinclude:: ../source/top.sls
  :caption: **0644 salt salt** ``/srv/salt/env/prod/top.sls``
  :linenos:

* If *host1* is a *Debian* machine, it will have *linux-base* then *debian* and
  finally *host1* applied.
* If another host is a *Debian* install, it will have *linux-base* then *debian*
  applied.
* An *Ubuntu* machine will only have *linux-base* applied.
* See :ref:`salt-common-issues-jinja` for common access errors with nodegroups.

.. _Nodegroups: https://docs.saltstack.com/en/latest/topics/targeting/nodegroups.html
.. _Compound Matchers: https://docs.saltstack.com/en/latest/topics/targeting/compound.html#targeting-compound