.. _service-dovecot-account:

Adding Accounts
###############
Accounts use separate passwords from shell logins using `imap.passwd`_.

Add a User/Password
*******************
`Virtual users`_ are stored in ``/etc/imap.passwd`` and is formatted exactly
like `/etc/passwd`_, but password is included and no login shell is required.
The IMAP password created should be **different** from the login password for
that user.

.. code-block:: bash
  :caption: Create SHA512 hashed password for user.

  doveadm pw -s SHA512-CRYPT

.. note::
  Copy full generated hash, including hashtype.

.. code-block:: bash
  :caption: Add User to ``/etc/imap.passwd``.

  {USER}:{PASSWORD HASH}:{UID from /etc/passwd}:{GID from /etc/passwd}::{USER HOME DIRECTORY}

.. _Virtual users: https://wiki.dovecot.org/VirtualUsers
.. _/etc/passwd: https://wiki.dovecot.org/AuthDatabase/PasswdFile
.. _imap.passwd: https://wiki.dovecot.org/HowTo/SimpleVirtualInstall