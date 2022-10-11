.. _service-ssh-linux-service:

Linux Service
#############

.. _service-ssh-centralize-keys:

Centralize Authorized Key Files
*******************************
Redirect all key files to a specific directory and link to users; allowing for
easier central management of keys.

.. code-block:: bash
  :caption: Create secured user certificate directory.

  mkdir /etc/ssh/authorized_keys/{USER}
  chown {USER}:{USER} /etc/ssh/authorized_keys/{USER}
  chmod 0700 /etc/ssh/authorized_keys/{USER}

.. code-block:: bash
  :caption: Move existing user ssh configuration to central location and link if
            needed.

  mv /home/{USER}/.ssh/* /etc/ssh/authorized_keys/{USER}
  ln -s /etc/ssh/authorized_keys/{USER} /home/{USER}/.ssh

Secure SSHD Config
******************
This will provide a default configuration which only allows non-root public key
authenticated users to login. Public keys are setup to use
``/etc/ssh/authorized_keys/{USER}`` for authenticating the user.

.. literalinclude:: source/sshd_config
  :caption: **0644 root root** ``/etc/ssh/sshd_config``
  :emphasize-lines: 2,5-8,15,25-27,30-32,34,41

Add Users to Access Group
*************************
.. code-block:: bash
  :caption: Add {USER} to ``ssh`` group to enable ssh service access.

  addgroup {USER} ssh

.. code-block:: bash
  :caption: Restart SSH service to load changes.

  systemctl restart ssh

`Reference <https://www.cyberciti.biz/tips/openssh-deny-or-restrict-access-to-users-and-groups.html>`__

.. _service-ssh-ufw:

Allow SSH Connections Through UFW
*********************************
UFW may be configured by default to block connections, verify this is not the
case. The general default is to deny incoming connections, allow outgoing, and
enable SSH.

.. code-block:: bash
  :caption: Get current status.

  ufw status

.. code-block:: bash
  :caption: Deny incoming connections except SSH, allow outgoing.

  ufw default deny incoming
  ufw default allow outgoing
  ufw allow ssh

.. tip::
  Know what services are running. Blocking all incoming connections might not be
  what you want to do.

`Reference <https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-ubuntu-18-04>`__

Create a Port Forwarding Only User
**********************************
Useful to forward services without providing shell a login.

.. code-block:: bash
  :caption: Add port forwarding user and generate key.

  adduser --disabled-password --home /etc/ssh/port-forwards-only --shell /bin/false port-forwards-only
  addgroup port-forwards-only ssh
  mkdir /etc/ssh/port-forwards-only
  chmod 0700 /etc/ssh/port-forwards-only
  chown port-forwards-only:port-forwards-only /etc/ssh/port-forwards-only
  ssh-keygen -b 4096 -t rsa -f /etc/ssh/port-forwards-only/port-forwards-only
  cat /etc/ssh/port-forwards-only/port-forwards-only.pub >> /etc/ssh/port-forwards-only/authorized_keys

See :ref:`service-ssh-tunneling` add only ``permitopen`` lines.

Verify Restrictions
===================
Attempt to login with a shell as well as port forwarding working.

.. code-block:: bash
  :caption: Verify port forwarding user cannot actually get a shell.

  ssh -vvv -N -L 5901:{SERVER}:5900 -i ~/.ssh/port-forwards-only port-forwards-only@{SERVER}
  ssh -vvv -i ~/.ssh/port-forwarding-only port-forwards-only@{SERVER}
  ssh -vvv -i port-forwards-only@{SERVER}

.. note::
  Only port forwarding should work (``-N``). Interactive logins with and without
  cert should fail.
