.. _ubuntu-creating-ssh-certificates:

Creating SSH Certificates
#########################
This setup assumes that a systems certificates for users are centrally located
in ``/etc/ssh/authorized_keys/{USERNAME}``. See :ref:`secure-ssh-connections`
for service setup with public key authentication.

Initial Setup
=============
The system should only need to be configured once. Each user needs to be
configured independently.

.. code-block:: bash
  :caption: Create secured user certificate directory.

  mkdir /etc/ssh/authorized_keys/{USERNAME}
  chown {USERNAME}:{USERNAME} /etc/ssh/authorized_keys/{USERNAME}
  chmod 0700 /etc/ssh/authorized_keys/{USERNAME}

.. code-block:: bash
  :caption: Move existing user ssh configuration to central location and link if
            needed.

  mv /home/{USERNAME}/.ssh/* /etc/ssh/authorized_keys/{USERNAME}
  ln -s /etc/ssh/authorized_keys/{USERNAME} /home/{USERNAME}/.ssh

.. _ubuntu-generate-certificates:

Generate Certificates
=====================

.. code-block:: bash
  :caption: Generate 4096 bit RSA certificates & add user to SSH group.

  ssh-keygen -b 4096 -t rsa -f /home/{USERNAME}/.ssh/{USERNAME}
  cat /home/{USERNAME}/.ssh/{USERNAME}.pub >> home/{USERNAME}/.ssh/authorized_keys
  chmod 0600 /home/{USERNAME}/.ssh/*
  chmod 0640 /home/{USERNAME}/.ssh/*.pub
  usermod -a -G ssh {USERNAME}

.. note::
  The private key ``{USERNAME}`` needs to be used to SSH into this host. Copy
  the publikc key ``{USERNAME}.pub`` to the ``authorized_keys`` on other hosts
  to be able to login to those hosts.