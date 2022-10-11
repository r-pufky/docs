.. _gpg-import:

Import GPG Master Public Key
############################
This will set ultimate trust for the `GPG Master Public Key`_ certificate you
created when backing up GPG state. Any of one these options below can be used.

.. note::
  Besides the locally exported public key file option, both other options assume
  that the public key has been published to keyservers. Yubikey can
  `automatically import`_ the correct certificate assuming the key was setup
  correctly. See :ref:`gpg-publish-key`.

.. code-block:: bash
  :caption: GPG Public Key from File.
  :emphasize-lines: 1

  $ gpg --import YOUR_PUBLIC_GPG_KEY.asc
  gpg: key 0x################: public key "FIRST LAST <EMAIL>" imported
  gpg: Total number processed: 1
  gpg:               imported: 1

.. code-block:: bash
  :caption: GPG Public Key from Keyserver.
  :emphasize-lines: 1

  $ gpg --receive-keys $KEYID  --keyserver hkp://pgp.mit.edu
  gpg: requesting key 0x################ from hkps server pgp.mit.edu
  [...]
  gpg: key 0x################: public key "FIRST LAST <EMAIL>" imported
  gpg: Total number processed: 1
  gpg:               imported: 1

.. code-block:: bash
  :caption: GPG Public Key from Yubikey URL.
  :emphasize-lines: 1,3

  $ gpg --card-edit

  gpg/card> fetch
  gpg: requesting key from 'https://keybase.io/{USER}/pgp_keys.asc'
  gpg: key ################: public key "FIRST LAST <EMAIL>" imported
  gpg: Total number processed: 1
  gpg:               imported: 1

Trust GPG Public Key Locally
****************************
Each machine on which the signing, encryption and authentication certificates
are used must trust the GPG Master Public key to prevent errors.

.. code-block:: bash
  :caption: Set Ultimate Trust for GPG Master Public Key.
  :emphasize-lines: 1,3,7,25-26,30,38,40,43,45-49

  $ gpg --edit-key $KEYID

  gpg> trust

  pub# rsa4096/################
       created: 2019-01-01  expires: never       usage: C
       trust: unknown       validity: unknown
  sub> rsa4096/################
       created: 2019-01-01  expires: never       usage: S
  sub> rsa4096/################
       created: 2019-01-01  expires: never       usage: E
  sub> rsa4096/################
       created: 2019-01-01  expires: never       usage: A

  Please decide how far you trust this user to correctly verify other users' keys
  (by looking at passports, checking fingerprints from different sources, etc.)

    1 = I don't know or won't say
    2 = I do NOT trust
    3 = I trust marginally
    4 = I trust fully
    5 = I trust ultimately
    m = back to the main menu

  Your decision? 5
  Do you really want to set this key to ultimate trust? (y/N) y

  pub# rsa4096/################
       created: 2019-01-01  expires: never       usage: C
       trust: ultimate      validity: ultimate
  sub> rsa4096/################
       created: 2019-01-01  expires: never       usage: S
  sub> rsa4096/################
       created: 2019-01-01  expires: never       usage: E
  sub> rsa4096/################
       created: 2019-01-01  expires: never       usage: A

  gpg> save

  $ gpg --list-secret-keys
  /home/{USER}/.gnupg/pubring.kbx
  -------------------------------
  sec#  rsa4096 2019-01-01 [C]
        ########################################
  uid           [ultimate] FIRST LAST <EMAIL>
  uid           [ultimate] [jpeg image of size 5877]
  ssb>  rsa4096 2019-01-01 [S]
  ssb>  rsa4096 2019-01-01 [E]
  ssb>  rsa4096 2019-01-01 [A]

.. note::
  * Use the imported public key ID for ``$KEYID``.
  * ``gpg --list-secret-keys`` should show ``#`` for private cert not on
    machine, and ``>`` for your signing, authentication and encryption certs on
    the Yubikey.

.. _automatically import: https://withinboredom.info/blog/2017/11/18/signing-commits-ssh-with-yubikey-and-windows/
.. _GPG Master Public Key: https://stackoverflow.com/questions/31784368/how-to-give-highest-trust-level-to-an-openpgp-certificate-in-kleopatra
