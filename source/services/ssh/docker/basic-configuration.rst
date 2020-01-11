.. _service-ssh-docker-basic-configuration:

Basic Configuration
###################
See `OpenSSH Documentation`_.

:ref:`service-ssh-generate-certificates` before starting.

Authorized Key Files
********************
.. code-block:: bash
  :caption: Create secured user certificate and directory.

  cat {USER}.pub > /etc/ssh/authorized_keys/{USER}
  chmod 0755 /etc/ssh/authorized_keys
  chmod 0644 /etc/ssh/authorized_keys/{USER}
  chown root:root -R /etc/ssh/authorized_keys

Secure SSHD Config
******************
This will provide a default configuration which only allows non-root public key
authenticated users to login, chrooted (locked) to ``/data``; and disabling
forwarding of all traffic. Public keys are setup to use
``/etc/authorized_keys/{USER}`` for authenticating the user.

.. literalinclude:: source/sshd_config
  :caption: **0644 root root** ``/etc/ssh/sshd_config``
  :emphasize-lines: 12, 14, 15, 17, 19, 21, 22, 23, 28, 33, 35, 36-38

Fail2Ban Config
***************
Setup :ref:`service-fail2ban-system` before starting.

.. code-block:: ini
  :caption: **0644 root root** ``/data/jail.d/docker-sshd.conf``

  [docker-sshd]
  enabled  = true
  port     = ssh
  filter   = sshd[mode=aggressive]
  logpath  = /var/log/syslog
  bantime  = -1
  findtime = 86400
  maxretry = 5

* Restart ``f2b-system``.
* Assumes ``/var/log/syslog`` is mounted to ``/var/log/syslog`` **read-only** on
  ``f2b-system``.
* Attempt an invalid SSH login and watch the docker logs to see if SSH is
  getting properly identified ``docker logs f2b-system``.

.. _OpenSSH Documentation: https://www.openssh.com/