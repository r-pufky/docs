.. _gpg-operations:

`GPG Operations <https://gnupg.org/documentation/manpage.html>`_
################################################################
Operations (decrypt, encrypt, sign) using GPG. Setup Yubikey using
:ref:`gpg-export-to-yubikey`.

.. note::
  If you are encrypting files for yourself, use your email address associated
  with your public key as the recipient.

Import
******
If the public key is not your own and cannot be found on keyservers, it must be
manually imported.

.. code-block:: bash
  :caption: Import a public key from a file.

  gpg --import {KEY FILE}

.. code-block:: bash
  :caption: Import a public key from a keyserver.

  gpg --recv {KEYID}

Export
******
The public key can be exported as well for others to encrypt data for you.

.. code-block:: bash
  :caption: Export public key for signing data.

  gpg --homedir /some/custom/.gnupg --armor --export > my_public_key.gpg

Encrypt
*******
.. code-block:: bash
  :caption: Encrypt a file for a given recipient.

  gpg --armor --batch --trust-model always --encrypt --recipient {GPGID} {FILE}

.. note::
  ``--trust-model`` will prevent GPG from warning about untrusted key
   recipients.

.. code-block:: bash
  :caption: Text.

  echo -n "super_secret_server_stuff" | gpg --armor --batch --trust-model always --encrypt --recipient {GPGID}

Create a Detached Signature
***************************
This is used to validate that the GPG encrypted file has not been changed.

.. code-block:: bash
  :caption: Create a detached signature for a given file.

  gpg --detach-sign {FILE}.gpg

Validate File Using Detached Signature
**************************************
.. code-block:: bash
  :caption: Import the public key if needed.

  gpg --import {PUBLIC KEY}

.. code-block:: bash
  :caption: Verify the GPG encrypted file.

  gpg --verify {FILE}.sig

`Reference <https://www.gnupg.org/gph/de/manual/r1023.html>`_
