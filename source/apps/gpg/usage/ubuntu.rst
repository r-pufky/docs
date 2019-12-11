.. _gpg-ubuntu:

Ubuntu GPG Yubikey
##################
Configure Yubikey for SSH authentication on Ubuntu.

Gnome-keyring implements both ssh-agent and gpg-agent with a `broken
implementation`_ that does not support smart cards. This will be disabled.

Required Materials
******************
#. Pre-configured Yubikey using :ref:`gpg-export-to-yubikey`.

.. code-block:: bash
  :caption: Install GPG and Yubikey manager on machine.

  apt update && apt upgrade
  apt-add-repository ppa:yubico/stable
  apt update
  apt install software-properties-common yubikey-manager yubikey-manager-qt scdaemon gpg pcscd
  apt remove libpam-gnome-keyring

.. note::
  `yubikey-manager-qt` is a GUI frontend which has limited functionality but
  does provide easy ways to ensure specific applets are enabled. `scdaemon`
  enables smartcard support for gpg.

.. hint::
  Ubuntu **18.04+** needs to add ``universe multiverse`` repositories to all apt
  sources in ``/etc/apt/sources.list``.

Configure GPG Agent
*******************
This will enable SSH usage with the gpg-agent.

.. code-block:: bash
  :caption: **0644 user user** ``~/.gnupg/gpg-agent.conf``

  enable-ssh-support

.. literalinclude:: source/.gpg-yubikey
  :caption: **0700 user user** ``~/.gpg-yubikey``

Download :download:`.gpg-yubikey <source/.gpg-yubikey>`

Setup the GPG environment when logging in with user.

.. code-block:: bash
  :caption: **0600 user user** ``~/.bash_profile``

  . ~/.gpg-yubikey

.. code-block:: bash
  :caption: **0600 user user** ``~/.bashrc``

  . ~/.gpg-yubikey

Allow User to Automount Yubikeys
********************************

.. code-block:: bash
  :caption: **0755 root root** ``/etc/udev/rules.d/99-yubikeys.rules``

  ACTION=="add",SUBSYSTEM=="usb", ATTR{idVendor}=="1050", ATTR{idProduct}=="0404", OWNER="{USER}"

.. note::
  Be sure to set ``OWNER`` to your username.

Disable Gnome SSH Fuckery
*************************
.. ggui:: Disable gnome SSH agent on startup.
  :key_title: Ubuntu --> Settings --> Session --> Startup --> Advanced
  :option:  ☐
  :setting: Launch gnome services on startup
  :no_section:
  :no_caption:
  :no_launch:

  .. note::
    May be listed as SSH agent

.. code-block:: bash
  :caption: **0644 root root** ``/etc/X11/Xsession.options``
  :emphasize-lines: 1

  #use-ssh-agent

**Reboot**.

Verify SSH Works
****************
Ensure Yubikey is readable by GPG. This assumes you already setup:

  #. ``~/.ssh/authorized_keys`` on the target machine with your *exported*
     GPG SSH RSA Public Key; see :ref:`gpg-export-keys`.
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

.. rubric:: References

#. `Yubikey SSH <https://occamy.chemistry.jhu.edu/references/pubsoft/YubikeySSH/index.php>`_

.. _broken implementation: https://zeos.ca/post/2015/gpg-smartcard/
.. _GPG public: https://stackoverflow.com/questions/31784368/how-to-give-highest-trust-level-to-an-openpgp-certificate-in-kleopatra
.. _imported automatically: https://withinboredom.info/blog/2017/11/18/signing-commits-ssh-with-yubikey-and-windows/
