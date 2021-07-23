.. _gpg-debian:

Debian GPG Yubikey
##################
Configure Yubikey for SSH authentication on Debian based linux.

Required Materials
******************
#. Pre-configured Yubikey using :ref:`gpg-export-to-yubikey`.

.. code-block:: bash
  :caption: Install GPG and security card agents on machine.

  apt update && apt upgrade
  apt install wget gnupg2 gnupg-agent dirmngr cryptsetup scdaemon pcscd secure-delete hopenpgp-tools yubikey-personalization

.. hint::
  Ubuntu **18.04+** needs to add ``universe multiverse`` repositories to all apt
  sources in ``/etc/apt/sources.list``. Additional dependencies:

  ``apt install libssl-dev swig libpcsclite-dev``

.. code-block:: bash
  :caption: _Optionally_ install yubikey manager to manage yubikeys.

  apt install python3-pip python3-pyscard
  pip3 install PyOpenSSL
  pip3 install yubikey-manager
  service pcscd start
  ~/.local/bin/ykman openpgp info

Configure GPG/GPG Agent
***********************
This will enable SSH usage with the gpg-agent.

.. literalinclude:: source/gpg-agent.conf
  :caption: **0644 user user** ``~/.gnupg/gpg-agent.conf``

Download :download:`gpg-agent.conf <source/gpg-agent.conf>`

.. literalinclude:: source/gpg.conf
  :caption: **0600** user user** ``~/.gnupg/gpg.conf``

Download :download:`gpg.conf <source/gpg.conf>`

See :ref:`gpg-import` for importing your public key and assigning ultimate trust
for use.

Verify SSH Works
****************
Ensure Yubikey is readable by GPG. This assumes you already setup:

  #. ``~/.ssh/authorized_keys`` on the target machine with your *exported*
     GPG SSH RSA Public Key; see :ref:`gpg-export-keys`. Reference
     :ref:`service-ssh` for remote SSH configuration.
  #. **Trusted** the GPG Master Public Key on the local machine; see
     :ref:`gpg-import`.

#. Connect with SSH as normal.
#. A ``Pin Entry`` pop-up window should appear. It may not be in focus. Enter
   your **user** :term:`PIN`.

   .. figure:: source/pinentry.png

#. :cmdmenu:`OK`
#. There will be *no prompt* in putty, but the Yubikey will start blinking.
   **Tap** Your Key to login.

.. note::
  * Number is the Yubikey serial number.
  * Holder is the First/Last name of the GPG certificate on the key.
  * Your key will blink when waiting for password or touch.

`Reference <https://github.com/drduh/YubiKey-Guide>`__
