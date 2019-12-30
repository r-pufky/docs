.. _gpg-encryption:

Encrypting Files
################
Files may encrypted for any recipient you have a public key for.

.. note::
  If you are encrypting files for yourself, use your email address associated
  with your public key as the recipient.

Configure Yubikey for SSH authentication on windows.

Required Materials
******************
#. Pre-configured Yubikey using :ref:`gpg-export-to-yubikey`.

Import Public Key
*****************
If the public key is not your own and cannot be found on keyservers, it must be
manually imported.

.. code-block:: bash
  :caption: Import a publick key

  gpg --import {KEY}

`Encrypt File`_
***************
.. code-block:: bash
  :caption: Encrypt a file for a given recipient.

  gpg --encrypt --recipient {EMAIL} {FILE}

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

.. rubric:: References

#. `GPG Manual <https://www.gnupg.org/gph/de/manual/r1023.html>`_

.. _Encrypt File: https://www.gnupg.org/gph/en/manual/x110.html