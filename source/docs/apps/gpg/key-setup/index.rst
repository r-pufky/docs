.. _gpg-key-setup:

Key Setup
#########
This will setup a secure GPG Master Key, GPG subkeys, and offload those subkeys
to a hardware backed Yubikey device.

#. Create a :ref:`gpg-master` (Your digital Identity).
#. :ref:`gpg-subkeys` from Master Key.
#. :ref:`gpg-backup`.
#. :ref:`gpg-export-to-yubikey` for secure daily use.
#. :ref:`gpg-cleanup` to prevent compromise & data loss.
#. :ref:`gpg-import` for client use.

.. toctree::
   :hidden:
   :maxdepth: -1

   gpg-master
   gpg-subkeys
   gpg-backup
   export-to-yubikey
   gpg-cleanup
   gpg-import