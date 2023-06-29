.. _gpg-manjaro:

Manjaro GPG Yubikey
###################
Configure Yubikey for SSH authentication on Manjaro based linux.

Required Materials
******************
#. Pre-configured Yubikey using :ref:`gpg-export-to-yubikey`.

.. code-block:: bash
  :caption: Install GPG and security card agents on machine.

  sudo pacman -Syu gnupg pcsclite ccid hopenpgp-tools yubikey-personalization
  sudo systemctl enable pcscd.service
  sudo systemctl start pcscd.service

Configure GPG/GPG Agent
***********************
This will enable SSH usage with the gpg-agent.

.. code-block:: bash
  :caption: A base version is here

  wget https://raw.githubusercontent.com/drduh/config/master/gpg-agent.conf -P ~/.gnupg

.. literalinclude:: source/gpg-agent.conf
  :caption: **0644 user user** ``~/.gnupg/gpg-agent.conf``

Download :download:`gpg-agent.conf <source/gpg-agent.conf>`

.. literalinclude:: source/gpg.conf
  :caption: **0600** user user** ``~/.gnupg/gpg.conf``

Download :download:`gpg.conf <source/gpg.conf>`

See :ref:`gpg-import` for importing your public key and assigning ultimate trust
for use.

.. code-block:: bash
  :caption: **0644 user user** ``~/.bashrc``

  export GPG_TTY="$(tty)"
  export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
  gpgconf --launch gpg-agent
  gpg-connect-agent updatestartuptty /bye > /dev/null

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

SSH Through a Bastion
*********************
All latest versions of SCP and SSH support multiple jump proxies for transfers.
GPG agent will be forwarded automatically (two authentication touches) if agent
forwarding is enabled.

.. code-block:: bash
  :caption: SSH through a bastion

  ssh -J {USER}@{BASTION} {STANDARD SSH COMMAND}

This may also be setup to auto proxy via the config file; enabling autoproxy
SSH and SCP transfers.

.. code-block:: bash
  :caption: **0644 {USER} {USER}** ``~/.ssh/config``

  Host {HOST}
  User {USER}
  HostName {HOST}
  ProxyJump {USER}@{BASTION}

`Reference: <https://superuser.com/questions/456438/how-do-i-scp-a-file-through-an-intermediate-server>`__

`Reference: <https://superuser.com/questions/174160/scp-over-a-proxy-with-one-command-from-local-machine>`__

SCP Transfer File Through a Bastion
***********************************
All latest versions of SCP and SSH support multiple jump proxies for transfers.
GPG agent will be forwarded automatically (two authentication touches) if agent
forwarding is enabled.

.. code-block:: bash
  :caption: SCP through bastion

  scp -o ProxyJump={USER}@{BASTION} {STANDARD SCP COMMAND}

  scp -J {USER}@{BASTION} {STANDARD SCP COMMAND}

`Reference: <https://superuser.com/questions/456438/how-do-i-scp-a-file-through-an-intermediate-server>`__

`Reference: <https://superuser.com/questions/174160/scp-over-a-proxy-with-one-command-from-local-machine>`__