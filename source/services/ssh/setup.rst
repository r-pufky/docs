.. _service-ssh-setup:

SSH Setup
#########
Secure Shell.

See `OpenSSH Documentation`_.

Centralize Authorized Key Files
*******************************
Redirect all key files to a specific directory and link to users; allowing for
easier central management of keys.

.. literalinclude:: source/sshd_config
  :caption: **0644 root root** ``/etc/ssh/sshd_config``
  :emphasize-lines: 2,7,13,16-19,21-25

.. note::
  This will provide a default configuration which only allows non-root public
  key authenticated users to login.

  Public keys are setup to use ``/etc/ssh/{USER}/authorized_keys`` for
  authenticating the user.

.. code-block:: bash
  :caption: Add {USER} to ``ssh`` group to enable ssh service access.

  addgroup {USER} ssh

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

Verify restrictions
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

.. rubric:: References

#. `Basic SSH Public Key Authentication Setup <https://help.ubuntu.com/community/SSH/OpenSSH/Keys>`_
#. `Deny/Allow/Restrict SSH access to users and groups <https://www.cyberciti.biz/tips/openssh-deny-or-restrict-access-to-users-and-groups.html>`_

.. _OpenSSH Documentation: https://www.openssh.com/