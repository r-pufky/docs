.. _salt-master:

Salt Master
###########
Salt Master manages and orchestrates Salt Minions, applying state to minions
through the use of static, Pillar (dynamic data), and Formulas (Templates).
Minions can be targetted individually or grouped based on attributes (Grains)
via :ref:`salt-nodegroups`.

Salt encrypts data communications, as well as providing only minion data needed
to minions. Supports GPG encryption of sensitive data out of the box, no special
services required.

Working assumptions:

* Salt Master runs unprivileged (see: :ref:`salt-non-root-user`).
* Two main enivronments ``prod`` and ``dev``.
* Service directory structure enforces separation of ``prod`` and ``dev``
  environments and minimizes globally avaliable data. (see:
  :ref:`salt-service-directory-best-practices`).

Related Material:

* :ref:`salt-master-configuration` for initial Salt Master setup.
* :ref:`salt-using-pillar` for basic Pillar (dynamic data) usage.
* :ref:`salt-nodegroups` for grouping minions based on attributes (Grains).
* :ref:`salt-state-management` for managing Salt States.
* :ref:`salt-state-management` for managing Salt Formulas (Templates).
* :ref:`salt-minion-management` for managing minions on Salt Master.
* :ref:`salt-gpg` for GPG usage with Salt Pillar data.

.. toctree::
   :hidden:
   :maxdepth: -1

   setup
   pillar
   nodegroups
   state-management
   formula-management
   minion-management
   gpg