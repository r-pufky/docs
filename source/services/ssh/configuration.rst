.. _service-ssh-configuration:

SSH Configuration
#################
Typical end-user SSH configuration needs.

Generate RSA Keys
*****************
Always use a strong password on keys, that is not your login password.

.. code-block:: bash
  :caption: Generate 4096bit RSA keys.

  ssh-keygen -b 4096 -t rsa -f {KEYNAME}
  chmod 0600 {KEYNAME}
  chmod 0640 {KEYNAME}.pub

.. code-block::
  :caption: Add Public Key to Authorized Keys for Use.

  cat {KEYNAME}.pub >> ~/.ssh/authorized_keys

.. _service-ssh-tunneling:

Restricting SSH Tunneling
*************************
Restrict what local ports and IP's can be accessed via SSH tunneling.

All on one line, comma separated with the public key cert afterwards.

* ``no-port-forwarding``: disable all port forwarding.
* ``no-X11-forwarding``: disable X11 forwarding.
* ``no-agent-forwarding``: disable agent forwarding.
* ``permitopen``: explicitly allow port to be opened.

Disable X11 forwarding but allow ports ``80,4243,32400`` to be forwarded.

.. code-block:: bash
  :caption: **0600 user user** ``~/.ssh/authorized_keys``

  no-X11-forwarding,permitopen="localhost:80",permitopen="localhost:4243",permitopen="10.10.10.10:32400" {PUBKEY DUMP}

Allow connection, but disables all forwarding.

.. code-block:: bash
  :caption: **0600 user user** ``~/.ssh/authorized_keys``

  no-port-forwarding {PUBKEY DUMP}

SSH Host Configuration
**********************
Setup SSH to automatically select correct options when using hosts/shortcuts.
See `detailed explanation`_ on ``config`` file.

.. literalinclude:: source/config
  :caption: **0600 user user** ``~/.ssh/config``

Importing RSA Keys for Putty/WinSCP on Windows
**********************************************
See `Puttygen Documentation`_.

#. Copy RSA private key to windows computer.
#. :cmdmenu:`win + r --> puttygen`
#. :cmdmenu:`File --> Load Private Key (Select RSA Private Key)`
#. Rename Key Comment to ``user@server``.
#. Save private key as ``RSA 4096`` in a ``.ppk`` file to local machine.
#. Delete RSA keys (use `sdelete64`_).
#. Update public key in ``authorized_keys`` file with comment about key being
   used.

.. _sdelete64: https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete
.. _Puttygen Documentation: http://winscp.net/eng/docs/ui_puttygen
.. _detailed explanation: https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/
