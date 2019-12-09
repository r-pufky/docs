.. _salt-minion-management:

Minion Management
#################
Minions are managed on the Salt Master via their client certificates.
Manipulating these certificates provides or revokes access. See
:ref:`salt-state-management` for managing minion states.

Signing Cert Requests
*********************
A minion cannot connect and apply salt states until the certificate request is
approved on the Salt Master. Globbing is supported.

.. code-block:: bash
  :caption: Show all *unaccepted* certs and sign one (Salt Master).

  salt-key -l unaccepted
  salt-key -a {HOSTNAME}

.. _salt-minion-show-all-certs:

.. code-block:: bash
  :caption: Show *all* certs on Salt Master (Salt Master).

  salt-key -L

`Revoking Certs`_
*****************
Disables Salt access for a specific minion, or removes unapproved certificates.

See :ref:`salt-minion-show-all-certs` for getting a certificate list.

.. code-block:: bash
  :caption: Remove minion from salt server (Salt Master).

  salt-key -d {HOSTNAME}

Salt will remove the key material automatically.

.. _Revoking Certs: https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html