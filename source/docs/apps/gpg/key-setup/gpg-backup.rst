.. _gpg-backup:

Backup GPG Keys
###############
Exporting subkeys will delete the key locally. Backing up ``$GNUPGHOME`` before
exporting will allow the export of multiple of the same subkey. Make your own
determination on if this security practice is acceptable to you.

.. danger::
  Ensure machine is **air-gapped** (no transmission devices on) during this
  step.

  Store on a (hardware) encrypted device.

Confirm Key State
*****************
Ensure master and subkeys are created and locally stored before exporting.

.. code-block:: bash

  gpg --list-keys

.. note::
  * ``>`` indicates a key is exported to card already (``ssb>``).
  * ``sec#`` indicates only stubs created (a private cert on different machine).
  * The master and subkeys should be listed with no modifiers if properly setup
    to export to a key.

.. _gpg-export-keys:

Export GPG Keys
***************
Master and Subkeys will be encrypted with your passphrase when exported.

.. code-block:: bash
  :caption: Export master, subkeys and public key.

  gpg --armor --export-secret-keys $KEYID > $GPGBACKUP/private/$KEYID.master.asc
  gpg --armor --export-secret-subkeys $KEYID > $GPGBACKUP/private/$KEYID.subkeys.asc
  gpg --armor --export $KEYID > $GPGBACKUP/public/$KEYID.asc
  cp $GNUPGHOME/openpgp-revocs.d/* $GPGBACKUP/private

.. note::
  The exported public key may be used in keybase.io, and manually imported into
  other GPG programs.

  GPG Public key export can be used to manually import into other GPG clients if
  you do not want to use keyservers.

.. code-block:: bash
  :caption: Export SSH RSA public key.

  gpg --export-ssh-key $KEYID > $GPGBACKUP/public/$KEYID.ssh.pub

.. note::
  The `SSH RSA Public Key`_ comment will use the authentication short key ID
  (``openpgp:0xXXXXXXXX``).

  See :ref:`service-ssh-client-configuration` for importing keys.

.. code-block:: bash
  :caption: Backup GNUPG state for multiple Yubikey initalizations.

  sudo cp -avi $GNUPGHOME $GPGBACKUP

.. _gpg-publish-key:

Publish Public Key
******************
Export the public key to public keyservers for GPG encrypt/decrypt/signing.
Without publishing you can still use SSH.

.. danger::
  Network is required for this step. Disable network immediately afterwards.

.. code-block:: bash
  :caption: Export public key to `SKS keyservers`_.

  gpg --keyserver hkp://pgp.mit.edu --send-key $KEYID

.. note::
  * This will export to major keyservers. These are all syncronized so only a
    single server is needed.
  * Also consider exporting public key to https://keybase.io.
  * The default gpg server is ``hkps://hkps.pool.sks-keyservers.net``

.. _SSH RSA Public Key: https://lists.gnupg.org/pipermail/gnupg-devel/2016-January/030682.html
.. _SKS keyservers: https://superuser.com/questions/227991/where-to-upload-pgp-public-key-are-keyservers-still-surviving