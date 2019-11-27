.. _gpg-with-yubikey:

GPG with Yubikey
################
Details creating a GPG Master Key & subkeys, with an embedded photo and
exporting subkeys to multiple Yubikeys. Additional documents provide setup for
using Yubikeys for SSH authentication on different client operating systems.

Subkeys are issued from the master key and are used for specific actions
essentially 'on behalf of' the master identity. These subkeys are loaded onto
Yubikeys for everyday use. As they are subkeys, these can be revoked as needed
or the master key can be revoked/changed to invalidate all subkeys at once. The
master key should be kept offline and encrypted and **only** the subkeys used in
day to day usage.

Core (out of date) `instructions are here`_. Alternative step-by-step
walkthrough instructions for configuring `multi-platform GPG/Yubikey SSH usage
are here`_. `OpenPGP for Beginners`_ is a good starting point if you have no
understanding of what this is.

insert links here.

.. rubric:: References

#. `Using Yuibikey with OpenPGP <https://support.yubico.com/support/solutions/articles/15000006420-using-your-Yubikey-with-openpgp>`_
#. `Using GPG for SSH Authentication <https://www.linode.com/docs/security/authentication/gpg-key-for-ssh-authentication/>`_

.. _instructions are here: https://github.com/drduh/YubiKey-Guide
.. _OpenPGP for Beginners: https://zacharyvoase.com/2009/08/20/openpgp/
.. _multi-platform GPG/Yubikey SSH usage are here: https://www.forgesi.net/gpg-smartcard/



.. toctree::
   :hidden:
   :maxdepth: -1

   prerequisites
   prep-yubikey
   gpg-master
   gpg-subkeys
   gpg-backup
   export-to-yubikey
   gpg-cleanup
   gpg-import
   windows
   ubuntu
   errors
   glossary