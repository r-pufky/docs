.. _salt-saltstack:

SaltStack
#########
Configuration management for Linux, Windows, & OSX.

Salt encrypts data communications, as well as providing only minion data needed
to minions. Supports GPG encryption of sensitive data out of the box, no special
services required.

Working assumptions:

* Salt Master runs unprivileged (see: :ref:`salt-non-root-user`).
* Two main enivronments ``prod`` and ``dev``.
* Service directory structure enforces separation of ``prod`` and ``dev``
  environments and minimizes globally avaliable data. (see:
  :ref:`salt-service-directory-best-practices`).
* Minion examples executed from the Master can be executed locally on the Minion
  with ``salt-call``.

Related Material:

* :ref:`salt-requirements` for minimum requirements and file locations.
* :ref:`salt-service-setup` for basic Salt service setup.
* :ref:`salt-master` for Salt Master basic configuration.
* :ref:`salt-minion` for Salt Minion basic configuration.
* :ref:`salt-gpg` for GPG usage with Salt Pillar data.
* :ref:`salt-minion-management` for managing minions on Salt Master.
* :ref:`salt-frequent-commands` for frequently used commands.
* :ref:`salt-common-issues` for common issues with saltstack.
* :ref:`salt-working-notes` for in progress notes.

.. toctree::
   :hidden:
   :maxdepth: -1

   requirements
   service-setup
   salt-master/index
   salt-minion/index
   frequent-commands
   common-issues
   working-notes