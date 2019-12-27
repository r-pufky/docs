.. _glossary:

Glossary
########

See :ref:`icon-explanation` for documentation specific symbols.

GPG/Encryption
**************
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

Mail
****
.. glossary::

  :abbr:`MTA`
    Mail Transport Agent: handles mail server to server (e.g. other domains).

  :abbr:`MDA`
    Mail Delivery Agent: handles user access to email (e.g. IMAP).

  :abbr:`MUA`
    Mail User Agent: user client to check email (e.g. thunderbird/outlook).

Networking
**********
See :ref:`vlan-101` for Unifi network specific terms.

.. glossary::

  :abbr:`UBNT`
    Ubiquiti Networks. This is a common Acronym used for their devices.

  :abbr:`Unifi`
    A line of products from UBNT.

Operating Systems
*****************
.. glossary::

  :abbr:`GPO`
    Group Policy for Windows. Provides centralized management and configuration
    of operating systems, applications, and users' settings

  :abbr:`Registry`
    Hierarchical database that stores low-level settings for Windows and
    applications that opt to use the registry.

  :abbr:`WSL`
    Windows Subsystem for Linux. Run linux distros in windows 10. See
    :ref:`os-windows-wsl`.

.. _CLI Yubikey Manager: https://developers.yubico.com/yubikey-manager/
.. _GUI Yubikey Manager: https://www.yubico.com/products/services-software/download/yubikey-manager/
.. _Two Factor Authentication: https://en.wikipedia.org/wiki/Multi-factor_authentication