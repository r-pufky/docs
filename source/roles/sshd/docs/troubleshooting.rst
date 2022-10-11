.. _service-ssh-troubleshooting:

Troubleshooting
###############

Enable Debug Mode
*****************
Print verbose messages to ``/var/log/syslog`` to help in debugging issues.

.. literalinclude:: source/ssh
  :caption: **0644 root root** ``/etc/default/ssh``
  :emphasize-lines: 5

.. code-block:: bash
  :caption: Reload and restart SSHD.

  systemctl daemon-reload
  service ssh restart

.. note::
  After a login attempt, the service may need to be restarted to test again.

  Check ``/var/log/syslog`` for debug information.

Could not open authorized keys '{X}': Permission denied
*******************************************************
The keyfile could not be accessed. This generally happens when SSHD drops
privileges to the user when logging in and the user cannot access the keyfile.

#. Directory containing keyfile is **readable** and **executable** by the user.
#. Keyfile is **0600**.