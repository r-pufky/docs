.. _gpg-prerequisites:

Pre-Requisites
##############
Carefully follow these instructions before setting up GPG and Yubikeys to remain
in a secure state. Failure to follow these instructions may expose private key
material to bad actors.

Required Materials:

#. Live USB OS, with persistent storage to setup additional packages. Tails Live
   USB `setup instructions`_ is preferred (most secure), other `live USB`_
   will work but be less secure. Instructions assume Debian-based system.
#. Hardware-backed Encrypted USB drive `Ironkey`_ (most secure), or USB drive
   with software encryption `using VeraCrypt`_ (less secure).
#. `Yubikey 5`_ (or other hardware security key support 4096bit RSA
   certificates).
#. A complete copy of these instructions or secondary device Internet access.
#. A photo to associate with your GPG master key.

This assumes usage of an Ironkey with Yubikeys on a Debian-base system for
configuration.

#. :ref:`gpg-prep-live-usb`.
#. :ref:`gpg-prep-ironkey`.
#. :ref:`gpg-prep-yubikey`.

.. rubric:: References

#. `Yubikey Device Setup <https://developers.yubico.com/PIV/Guides/Device_setup.html>`_
#. `GPG Yubikey 5 <https://zeos.ca/post/2018/gpg-yubikey5/>`_
#. `GPG Card Administration <https://www.gnupg.org/howtos/card-howto/en/ch03.html>`_

.. _setup instructions: https://tails.boum.org/install/win/usb-download/index.en.html
.. _live USB: https://ubuntu.com/#download
.. _Ironkey:  https://www.kingston.com/unitedstates/us/usb-flash-drives/ironkey-d300-encrypted-usb-flash-drive
.. _using VeraCrypt: https://github.com/drduh/YubiKey-Guide#backup
.. _Yubikey 5: https://www.yubico.com/products/yubikey-5-overview/

.. toctree::
   :hidden:
   :maxdepth: -1

   prep-live-usb
   prep-ironkey
   prep-yubikey
