.. _gpg-windows-forward:

Windows Forward GPG
###################
Forward your ``gpg-agent`` to a linux machine for signing and encrypt/decrypt
operations. This is currently only possible using ``WSL``, not Putty.

First a USB WSL bridge is setup with a GPG relay enabling GPG usage in WSL. GPG
may be forwarded from WSL to other Linux machines.

Bridges must be created until Windows `WSL supports USB passthru`_.

.. warning::
  Fowarding gpg-agent credentials should **ONLY** be done on trusted machines.
  See recent `security breach`_.

  Using GPG relay on the local machine is safer, but not ideal.

`Reference <https://blog.nimamoh.net/yubi-key-gpg-wsl2/>`__

Setup GPG Relay in WSL
**********************

Required Materials
==================
#. `npiperelay`_ downloaded. **Verify Integrity**.
#. `wsl-ssh-pageant`_ **Verify Integrity**.
#. Recent Linux Distro on WSL2 installed. See :ref:`w10-wsl`.
#. `Putty`_ installed.
#. Pre-configured Yubikey using :ref:`gpg-export-to-yubikey`.

Install WSL USB Bridges on Windows
==================================
Windows does not support sockets. These utilities provide UNIX sockets to WSL
systems; which utimately enable the use of Yubikeys.

#. Copy the latest `npiperelay`_ to ``%appdata%\npiperelay\npiperelay.exe``
#. Copy the latest `wsl-ssh-pageant`_ to
   ``%appdata%\wsl-ssh-pageant\wsl-ssh-pageant-amd64-gui.exe``
#. Enable Putty Support, see :ref:`gpg-windows-configure-gpg-agent`

.. code-block:: powershell
  :caption: Restart ``gpg-connect-agent`` to pickup putty support, if changed.

  gpgconf --kill gpg-agent
  gpg-connect-agent /bye

Install GPG Relay on WSL
========================
This script will setup a GPG relay daemon using the USB socket bridge setup
above. Download the script.

.. danger::
  Review this script. Never blindly execute Internet scripts.

.. code-block:: bash
  :caption: Create ``gnupg`` empty directory.

  mkdir ~/.gnupg
  chmod 0700 ~/.gnupg

.. code-block:: bash
  :caption: From your WSL instance.

  mkdir -p ~/.local/bin
  wget https://gist.github.com/andsens/2ebd7b46c9712ac205267136dc677ac1/raw/574f8c96fc3961fa8f953ee9335a9de3388ba256/gpg-agent-relay -O ~/.local/bin/gpg-agent-relay
  chmod +x ~/.local/bin/gpg-agent-relay

.. code-block:: bash
  :caption: **0600 {USER} {USER}** ``~/.bashrc``

  $HOME/.local/bin/gpg-agent-relay start
  export SSH_AUTH_SOCK=$HOME/.gnupg/S.gpg-agent.ssh

Logout and Login

.. code-block:: bash
  :caption: Verify GPG relay works.

  gpg-agent-relay status
  gpg --card-status

Forward GPG to Linux
********************
`GPG Agent Forwarding`_ requires gnupg > **2.1.17** on both machines.

.. danger::
  Fowarding gpg-agent credentials should **ONLY** be done on trusted machines.
  See recent `security breach`_. Here be dragons.

Determine Sockets
=================

.. code-block:: bash
  :caption: Find your extra socket on your local machine.

  gpgconf --list-dir agent-extra-socket

.. code-block:: bash
  :caption: Find the socket on the remote machine.

  gpgconf --list-dir agent-socket

Update SSHD Config
==================
The remote system needs to be updated to force removal of sockets before
creating new ones; which will enable automatic forwarding of ``gpg-agent``.
Without this the socket will manually need to be re-created every login.

.. code-block:: bash
  :caption: **0600 root root** ``/etc/ssh/sshd_config``

  StreamLocalBindUnlink yes

Restart SSHD.

Create GPG Tunnel Config
========================

.. code-block:: bash
  :caption: **0600 {USER} {USER}** ``~/.ssh/config``

  Host {REMOTE}
    HostName {REMOTE IP OR FDQN}
    RemoteForward {REMOTE SOCKET} {LOCAL EXTRA SOCKET}

Connect using the ssh config remote name.

Troubleshooting
***************

``--notify-await`` message on start
===================================
Your WSL instance does not support socket notification of a service starting.
You will need to modify the ``gpg-agent-relay`` script to work for your
distribution or find another WSL distribution to run.

``gpg: error retrieving {GPGID} via WKD: General error``
========================================================
You need to import your {GPGID} public key into the local keyring to use it.

.. code-block:: bash
  :caption: Import your public key. Either use keybase, keyservers, or exported
            key.

  https://keybase.io/rpufky/pgp_keys.asc | gpg --import

.. code-block:: bash
  :caption: Optionally fully trust your key. If you are certain it is valid.

  $ gpg --list-keys
  $ gpg --edit-key {KEY ID}

  > trust
  > 5
  > quit

.. rubric:: References

#. `gpg-agent-relay <https://gist.github.com/andsens/2ebd7b46c9712ac205267136dc677ac1>`_
#. `Yubikey, GPG, WSL1 <https://justyn.io/blog/using-a-yubikey-for-gpg-in-wsl-windows-subsystem-for-linux-on-windows-10/>`_

.. _npiperelay: https://github.com/NZSmartie/npiperelay/releases
.. _wsl-ssh-pageant: https://github.com/benpye/wsl-ssh-pageant/releases
.. _security breach: https://matrix.org/blog/2019/05/08/post-mortem-and-remediations-for-apr-11-security-incident
.. _WSL supports USB passthru: https://github.com/microsoft/WSL/issues/5158
.. _GPG Agent Forwarding: https://wiki.gnupg.org/AgentForwarding
.. _Putty: https://www.putty.org/
