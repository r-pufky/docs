.. _gpg-glossary:

GPG Glossary
############

.. glossary::
  :abbr:`2FA`
    `Two Factor Authentication`_. Combines two different factors to
    provide strong authentication:

    #. Something you know.
    #. Something you have.
    #. Something you are.

  :abbr:`Yubikey Manager`
    Application that will manage Yubikey configuration. There is a
    `GUI Yubikey Manager`_ and a `CLI Yubikey Manager`_.

  :abbr:`Yubikey Password/PINs`
  :abbr:`PIN`
    Password for ``user`` and ``admin`` accounts for a Yubikey. Can be up to
    **127 ASCII characters** long.

    The user password is used whenever GPG material needs to be accessed on the
    card. Daily usage.

    The admin password is used to reset the user password and perform
    administrative functions on the Yubikey itself. Limited usage.

  :abbr:`Signing Key`
    Key used to cryptographically sign data. This enables others to verify that
    data sent by you has not been altered.

  :abbr:`Encryption Key`
    Key used to encrypt data. Data is typically signed with the
    :term:`Signing Key` after encryption.

  :abbr:`Authentication Key`
    Key used to Authenicate to systems (e.g. SSH). This will allow other systems
    to load your public GPG key and enable access to systems without needing any
    information from you.

.. _CLI Yubikey Manager: https://developers.yubico.com/yubikey-manager/
.. _GUI Yubikey Manager: https://www.yubico.com/products/services-software/download/yubikey-manager/
.. _Two Factor Authentication: https://en.wikipedia.org/wiki/Multi-factor_authentication