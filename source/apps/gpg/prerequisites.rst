.. _gpg-prerequisites:

Prerequisites
#############
Carefully follow these instructions before setting up GPG and Yubikeys to remain
in a secure state. Failure to follow these instructions may expose private key
material to bad actors.

Required Materials
******************
#. Live USB OS, with persistent storage to setup additional packages. Tails Live
   USB `setup instructions`_ is preferred (most secure), other `live USB`_
   will work but be less secure. Instructions assume Debian-based system.
#. Hardware-backed Encrypted USB drive `Ironkey`_ (most secure), or USB drive
   with software encryption `using VeraCrypt`_ (less secure).
#. Yubikey (or other hardware security key support 4096bit RSA certificates)
   `nano`_ or `Yubikey 5`_.
#. A complete copy of these instructions or secondary device Internet access.
#. A photo to associate with your GPG master key.

This assumes usage of an Ironkey with Yubikeys on a Debian-base system for
configuration.

Live USB Setup
**************
GPG generation should be done on a air-gapped, temporal, encrypted OS to
minimize secret key exposure. Persistent disk should be created so that packages
may be installed / updated as needed (e.g. Yubikey manager). All GPG operations
should be done **offline** with the exception of uploading public keys to
services.

Set a **root** password.

.. danger::
  Do **not** store secret material directly on live USB filesystems.

.. note::
  Network is required for this step. Disable after packages are installed.

.. code-block:: bash
  :caption: Update and install Yubikey management.

  apt update && apt upgrade
  apt-add-repository ppa:yubico/stable
  apt update
  apt install software-properties-common yubikey-manager yubikey-manager-qt scdaemon hopenpgp-tools gpg

.. note::
  `yubikey-manager-qt` is a GUI frontend which has limited functionality but
  does provide easy ways to ensure specific applets are enabled. `scdaemon`
  enables smartcard support for gpg.

.. hint::
  Ubuntu **18.04+** needs to add ``universe multiverse`` repositories to all apt
  sources in ``/etc/apt/sources.list``.

Ironkey
*******
Setup a working ironkey either through :ref:`gpg-prerequisites-initalize` or
:ref:`gpg-prerequisites-reset` before unlocking for GPG use.

.. _gpg-prerequisites-initalize:

Initalize Ironkey
=================
Do this if fresh Ironkey, or creating a new master key.

.. danger::
  This is **data destructive**.

.. code-block:: bash
  :caption: Initalize Ironkey.

  /media/user/IRONKEY/linux/linux64/ikd300_initalize

.. _gpg-prerequisites-reset:

Reset Ironkey
=============
Wipes a working Ironkey to a default state.

.. danger::
  This is **data destructive**.

.. code-block:: bash
  :caption: Reset Ironkey.

  /media/user/IRONKEY/linux/linux64/ikd300_resetdevice

.. note::
  Max **16** character password. Ironkey will wipe device after 10 failed
  attempts and force phsyical re-insertion after every 3 failed attempts.

Unlock Ironkey
==============
Mount an unlocked Ironkey for GPG usage.

.. code-block:: bash
  :caption: Unlock Ironkey.

  sudo /media/user/IRONKEY/linux/linux64/ikd300_login

* Open browser, click on ``KINGSTON`` to automount to ``/media/user/KINGSTON``.
* This is your hardware-backed encrypted storage.

.. important::
  The Ironkey is the only **safe** location to store secret key material.

.. _setup instructions: https://tails.boum.org/install/win/usb-download/index.en.html
.. _live USB: https://www.ubuntu.com/#download
.. _Ironkey: https://www.kingston.com/us/usb/encrypted_security/IKD300
.. _using VeraCrypt: https://github.com/drduh/YubiKey-Guide#backup-keys
.. _nano: https://www.yubico.com/product/Yubikey-5-nano/#Yubikey-5-nano
.. _Yubikey 5: https://www.yubico.com/product/Yubikey-5-nfc/#Yubikey-5-nfc