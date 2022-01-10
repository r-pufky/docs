.. _service-signal:

`Signal`_
#########
Send encrypted notifications directly to Signal users.

Uses :ref:`1804-server-base-install`.

Files
*****
.. files:: Signal Files
  :value0: ~/.local/share/signal-cli,
           Default location for private Signal keys for messaging
  :value2: /data/signal/data, Location for service Signal keys for messaging
  :value3: /data/signal/cli/bin, Signal binary
  :open:

Server Setup
************
Download the `Latest Release`_.

.. code-block:: bash
  :caption: Install dependencies.

  apt install default-jre

.. code-block:: bash
  :caption: Create signal system user.

  adduser --system --home /data/signal --shell /bin/false signal

.. code-block:: bash
  :caption: Install dependencies and extract release.

  tar xvf signal-cli-*.tar.gz -C /data/signal/cli
  chmod go-rwx /data/signal
  chown -R signal /data/signal

Link to Phone
=============
The binary can be setup as `the primary account`_ however this will remove
access from your phone (unless it is registered with a second number). It is
better to link it to an existing account if you only have a single number
instead. Access can be remotely disabled this way.

.. code-block:: bash
  :caption: Generate link request (this will eventually timeout).

  ./signal-cli link -n {DEVICE NAME}

.. note::
  This will generate a ``tsdevice://`` URI. This needs to be copied as is to
  generate a scannable QR code.

  Do not quit the process as it is pending approval. Once approved you will see
  the message ``Associated with: +{INTERNATIONAL PHONE NUMBER}``.

.. code-block:: bash
  :caption: Generate QR code on CLI and scan with phone to approve.

  qrencode -t ansi256 'tsdevice:// ...'

.. important::
  ``tsdevice`` must be quoted, otherwise an invalid QR code will be generated.

Send Test Message
=================
Send a test message to ensure everything works then copy cofiguration keys for
service.

.. code-block:: bash
  :caption: Send test message.

  ./signal-cli -u +{INTERNATIONAL PHONE NUMBER} send -m "This is a test message" +{INTERNATIONAL PHONE NUMBER}

.. note::
  You can actually send the message from and to the same number. It will be
  received in Signal as a ``Note to Self``.

.. code-block:: bash
  :caption: Copy configuration to service directory.

  cp -av ~/.local/share/signal-cli/data /data/signal/
  chmod go-rwx -R /data/signal
  chown -R signal /data/signal

.. warning::
  These files **must** be secured as any access to these credentials will allow
  messages to be sent as you.

  Access can be disabled in the Signal App at any time.

Send SSH Login Notification
***************************
Enables Signal messaging when a user logs into the system via SSH.

Script will only send notifications on opening SSH connections.

.. literalinclude:: source/ssh-signal-notify
  :caption: **0700 signal signal** ``/data/signal/ssh-signal-notify``
  :emphasize-lines: 7

.. code-block:: bash
  :caption: **0644 root root** ``/etc/pam.d/sshd``

  ## Add at end of file.
  # Alert successful logins via signal.
  session    optional    pam_exec.so seteuid /data/signal/ssh-signal-notify

.. note::
  ``pam_exec`` will not have user environment variables by default. See
  `pam_exec reference`_ for environment variables. Enabling user environment
  variables is **dangerous**.

  Enable ``debug`` and check ``/var/log/auth.log`` if notification does not
  fire. Any errors with optional scripts are generally dropped sliently.

.. rubric:: References

#. `PAM Reference <https://www.tecmint.com/configure-pam-in-centos-ubuntu-linux/>`_
#. `Signal CLI Reference <https://github.com/AsamK/signal-cli/blob/master/man/signal-cli.1.adoc>`_
#. `Signal CLI Docker <https://hub.docker.com/r/kayvan/signal-cli>`_
#. `SSH Login Notifications with Signal <https://8192.one/post/ssh_login_notification_signal/>`_
#. `pam_exec Reference <http://www.linux-pam.org/Linux-PAM-html/sag-pam_exec.html>`_
#. `Run sshd login script one <https://unix.stackexchange.com/questions/507811/running-a-script-prior-to-ssh-login-but-only-once>`_

.. _pam_exec reference: http://www.linux-pam.org/Linux-PAM-html/sag-pam_exec.html
.. _Latest Release: https://github.com/AsamK/signal-cli/releases/latest
.. _the primary account: https://github.com/AsamK/signal-cli
.. _Signal: https://signal.org/
