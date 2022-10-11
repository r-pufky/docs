.. _service-ssh-client-configuration:

Client Configuration
####################
Typical end-user SSH configuration needs.

See :ref:`service-ssh-create-certificates` for generating certificates to use.

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
See `detailed explanation <https://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/>`_
on ``config`` file. `internal-sftp <http://postsbylukman.blogspot.com/2017/09/difference-between-internal-sftp-and.html>`_
is the default now and is built from the same code as ``sftp-server`` but also
includes support for ChrootDirectories.

.. literalinclude:: source/config
  :caption: **0600 user user** ``~/.ssh/config``

Importing RSA Keys for Putty/WinSCP on Windows
**********************************************
See Puttygen Documentation.

#. Copy RSA private key to windows computer.
#. :cmdmenu:`⌘ + r --> puttygen --> Conversions --> Import Key (Select Private Key)`
#. Rename Key Comment to ``user@server``.
#. :cmdmenu:`Save private key` in a ``.ppk`` file to local machine.
#. Delete RSA keys (use `sdelete64 <https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete>`_).
#. Update public key in ``authorized_keys`` file with comment about key being
   used.
