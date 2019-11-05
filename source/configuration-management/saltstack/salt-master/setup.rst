.. _salt-master-configuration:

`Salt Master Configuration`_
############################
``/etc/salt/master`` is the master flat-file config, however making changes in
``/etc/salt/master.d/`` for each specific conifugration area is preferred to
clarify server changes, as well as enabling easy management on the config. Any
file with ``.conf`` will be loaded in this directory and take precedence over
the flat file.

.. _salt-master-file:

File Section
************
Where salt locates files and states to apply to minions. This will create three
branches. Base is applied to all environments and is unused in this config.
Files are compared using *sha512* hashing.

Files can be directly checked out from a revision system (like git). Adding or
removing file paths require a reload of the master server.

.. literalinclude:: ../source/master/file.conf
  :caption: **0644 root root** ``/etc/salt/master.d/file.conf``
  :linenos:

.. _salt-master-pillar:

`Pillar Section`_
*****************
Pillar defines the dynamic client data sent to minions and acts as an ACL for
access to that data. Prod and Dev environments are used, forcing missing data
requested by a minion to halt state application, and prevents error messages on
minions (reported on server). This prevents leaking potentially sensitive data
users shouldn't have access to if a formula fails.

.. literalinclude:: ../source/master/pillar.conf
  :caption: **0644 root root** ``/etc/salt/master.d/pillar.conf``
  :linenos:

Primary Section
***************
Primary configuration for salt-master. This forces the master to run as
``salt``, ensures the master is validated before started (perms, etc), pings
minions on AES key rotation and prevents minions from unmanaging themselves. See
:ref:`salt-non-root-user` for setup instructions.

.. literalinclude:: ../source/master/primary.conf
  :caption: **0644 root root** ``/etc/salt/master.d/primary.conf``
  :linenos:

Security Section
****************
Security configuration. Require 4096 bit keys for signing. All messages are
signed. All minions added require manaul approval. Use *SSL/TLS1.2* for protcol
encryption. See :ref:`salt-tls-protocol` for cert creation.

``drop_messages_signature_fail`` is set to False, as this requires minions to
have verifiable signing certs, which self-signed certs cannot provide. Otherwise
this option will drop any message that is not verified to a root CA.

.. literalinclude:: ../source/master/security.conf
  :caption: **0644 root root** ``/etc/salt/master.d/security.conf``
  :linenos:

State Section
*************
Defines how states are applied to minions. Minions will immediately fail is
there is an error, instead of continuing to apply state.

.. literalinclude:: ../source/master/state.conf
  :caption: **0644 root root** ``/etc/salt/master.d/state.conf``
  :linenos:

See :ref:`salt-minion-management` for managing minions on Salt Master.

.. _Salt Master Setup: https://docs.saltstack.com/en/latest/ref/configuration/master.html
.. _Pillar Section: https://docs.saltstack.com/en/latest/topics/pillar/