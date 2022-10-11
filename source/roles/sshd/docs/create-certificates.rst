.. _service-ssh-create-certificates:

Create Certificates
###################
This setup assumes that a systems certificates for users are centrally located
in ``/etc/ssh/authorized_keys/{USER}``. See :ref:`service-ssh-centralize-keys`
for service setup with public key authentication.

**Always** use a strong password on keys that is not your login password.

.. code-block:: bash
  :caption: Generate 4096 bit RSA certificates & add user to SSH group.

  ssh-keygen -b 4096 -t rsa -f /home/{USER}/.ssh/{USER}
  cat /home/{USER}/.ssh/{USER}.pub >> home/{USER}/.ssh/authorized_keys
  chmod 0600 /home/{USER}/.ssh/*
  chmod 0640 /home/{USER}/.ssh/*.pub
  addgroup {USER} ssh

.. note::
  The private key ``{USER}`` needs to be used to SSH into this host. Copy
  the publikc key ``{USER}.pub`` to the ``authorized_keys`` on other hosts
  to be able to login to those hosts.

`Reference <https://help.ubuntu.com/community/SSH/OpenSSH/Keys>`__
