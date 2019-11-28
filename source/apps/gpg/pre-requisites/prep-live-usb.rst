.. _gpg-prep-live-usb:

Prep Live USB
#############
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