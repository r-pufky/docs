.. _salt-gpg:

`GPG Encrypt Pillar Data`_
##########################

* `Alternative GPG Reference`_
* `GPG CLI Reference`_

``/etc/salt/gpgkeys`` is a required hard-coded directory. Ensure only the
salt-master user has access to this.

.. note::
  salt-master requires no password for GPG decryption to work. Secure your
  certs. You may want to enforce expiration on certs as well.

If entropy generation is slow (typical on VM's), install `haveged`_ to speed up
entropy collection.

.. _gpg-key-creation:

.. code-block:: bash
  :caption: Generate GPG keys for salt-master encryption/decryption.

  mkdir -p /etc/salt/gpgkeys
  chmod 0700 /etc/salt/gpgkeys
  gpg --gen-key --homedir /etc/salt/gpgkeys

.. important::
   * Default option (``RSA and RSA``).
   * ``4096`` bit key.
   * ``0`` (cert does not expire).
   * ``salty (salt@example.com)``.
   * **NO** password.

.. code-block:: bash
  :caption: Export public key for signing data.

  gpg --homedir /etc/salt/gpgkeys --armor --export > salty_public_key.gpg

``salt_public_key.gpg`` is used by anyone on any system to create encrypted data
that only the server can read.

.. code-block:: bash
  :caption: Import the public key for signing (stored in ``~/.gnupg``).

  gpg --import salt_public_key.gpg

.. _encrypting-data:

Encrypting Data
***************

.. note::
  The entire PGP block should be added to Pillar; the *blank vertical space* can
  be removed. ``salty`` is the name of the recipient of the data.

.. code-block:: bash
  :caption: Text

  echo -n "super_secret_server_stuff" | gpg --armor --batch --trust-model always --encrypt --recipient salty

.. code-block:: bash
  :caption: Files

  gpg --armor --batch --trust-model always --encrypt --recipient salty {FILE}

.. note::
  The contents of this file should be what is placed in Pillar. It will be
  written as ``{FILE}.asc``. ``salty`` is the name of the recipient of the data
  (see :ref:`gpg-key-creation`).

.. warning::
  Binary data cannot be stored GPG encrypted in pillar for Python 3 versions of
  saltstack due to Python 3 strict handling of text vs. binary data type. This
  results in a binary data render error for GPG on salt. `Binary support is
  being explicitly added`_.

.. _encrypt-shadow-passwords:

Encrypt Shadow Passwords
************************
The `salt user state documentation`_ recommends using ``openssl passwd -1`` to
generate a bash passwd hash. This *only hashes MD5*; modern distributuions of
linux hash *sha512*. Use either the ``mkpasswd`` tool or the `python script`_
below to generate a *salted, sha512 hash* in the correct format for consumption
in ``/etc/shadow``. Then GPG encrypt the password when storing in Pillar.

.. code-block:: bash
  :caption: Using ``mkpasswd``.

  apt install whois
  mkpasswd -m sha-512

.. code-block:: bash
  :caption: Python 3 version.

  python3 -c "import crypt, getpass; print(crypt.crypt(getpass.getpass('password to hash: '), crypt.mksalt(crypt.METHOD_SHA512)))"

.. _add-to-pillar:

Add to Pillar
*************
Prefix any Pillar file using GPG encryped data with ``#!yaml|gpg`` and insert
the GPG message block as the value for a key. Use a pipe (``|``) to denote a GPG
message. Blank lines between the begin/version and body can be removed. Standard
YAML indentation rules for long text blocks apply.

.. literalinclude:: ../source/gpg.sls
  :linenos:
  :emphasize-lines: 1,3

Refresh Pillar and Push Data
****************************
Regenerate cached Pillar data and push new values (e.g. updated GPG data) to
minions if automatic refresh isn't fast enough. Minions that have been given
access to the specific pillar will be able to see the decrypted data.

.. code-block:: bash
  :caption: Manual refresh of Pillar data.

  salt '*' saltutil.refresh_pillar
  salt pillar.items

.. _GPG Encrypt Pillar Data: http://joshbolling.com/2017/05/28/protect-pillar-data-with-gpg/
.. _Alternative GPG Reference: https://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.gpg.html
.. _GPG CLI Reference: http://blog.ghostinthemachines.com/2015/03/01/how-to-use-gpg-command-line/
.. _haveged: https://www.digitalocean.com/community/tutorials/how-to-setup-additional-entropy-for-cloud-servers-using-haveged
.. _salt user state documentation: https://docs.saltstack.com/en/latest/ref/states/all/salt.states.user.html
.. _python script: https://serverfault.com/questions/330069/how-to-create-an-sha-512-hashed-password-for-shadow
.. _Binary support is being explicitly added: https://github.com/saltstack/salt/issues/51879