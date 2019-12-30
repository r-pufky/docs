.. _gpg-prep-yubikey:

Prep Yubikey
############
.. attention::
  :term:`Yubikey Password/PINs` may be up to **127 ASCII characters** long.

.. gtable:: Default Yubikey Passwords
  :c0: Default User Pin,
       Default Admin Pin
  :c1: 123456,
       12345678
  :no_key_title:
  :no_section:
  :no_launch:

Verify Geniue Yubikey
*********************
Ensure Yubikey is geniue and has not been tampered with during any step of the
supply chain.

#. https://www.yubico.com/genuine/
#. :cmdmenu:`Verify Device`
#. Touch Yubikey when prompted.

.. note::
  Yubico must be able to see the make and model of the device during the
  verification process.

``Verification Complete`` is displayed for genuine keys. Failure means potential
compromise and should be thrown out after it is confirmed to fail again.

Reset Yubikey
*************
This will `destroy any openpgp material`_ on the key and reset to the default
key state. Do this even if the Yubikey is new.

.. code-block:: bash
  :caption: Reset Yubikey openpgp.

  ykman openpgp reset

Alternatively using the `Yubikey Personalization Tool`_ will provide options to
do this via a GUI.

.. note::
  If the Yubikey is not brand new, ensure you are not deleting any other
  :term:`2FA` configurations.

.. code-block:: bash
  :caption: Show current Yubikey card shows with default values.

  gpg --card-status

* If not found, re-insert the key. There is a known race condition that may
  occur with older GPG libraries.
* Ensure latest firmware version using :term:`Yubikey Manager`.
* Ensure device has ``CCID`` mode enabled using :term:`Yubikey Manager`. Most
  firmware past ``3.1.8`` will have this permenantly enabled and not listed.

Configure Yubikey
*****************
Configure behavior of Yubikey so short touches will provide GPG material, while
long touches will provide Yubico OTP. This prevents accidental touches spewing
keystrokes into whatever is open. NFC is also disabled to force physical touch
to use key.

#. :cmdmenu:`Yubikey Manager --> Applications --> OTP`
#. Delete ``Slot 1``.
#. Configure ``Slot 2`` to use ``Yubico OTP``.

.. note::
  Newer keys can just use the :guilabel:`swap` button.

.. figure:: source/yubikey-otp.png
  :width: 90%

  Swapped button press lengths.

#. :cmdmenu:`Yubikey Manager --> Interfaces --> NFC --> Disable All`
#. :cmdmenu:`Save Interfaces`

.. figure:: source/yubikey-nfc.png
  :width: 90%

  All NFC options are disabled to requirement phyiscal presence.

Setup openpgp on Yubikey
************************
Prepare Yubikey to load GPG key material.

.. code-block:: bash
  :caption: Edit openpgp application on Yubikey.
  :emphasize-lines: 1

  $ gpg --card-edit

  Reader ...........: Yubico YubiKey OTP FIDO CCID 0
  Application ID ...: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  Version ..........: 3.4
  Manufacturer .....: Yubico
  Serial number ....: XXXXXXXXXX
  Name of cardholder: [not set]
  Language prefs ...: [not set]
  Sex ..............: unspecified
  URL of public key : [not set]
  Login data .......: [not set]
  Signature PIN ....: forced
  Key attributes ...: rsa4096 rsa4096 rsa4096
  Max. PIN lengths .: 127 127 127
  PIN retry counter : 3 3 3
  Signature counter : 0

.. code-block:: bash
  :caption: Set the **admin** password (Remember to use the Default PIN if needed).
  :emphasize-lines: 1,4,13,16

  gpg/card> admin
  Admin commands are allowed

  gpg/card> passwd
  gpg: OpenPGP card no. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX detected

  1 - change PIN
  2 - unblock PIN
  3 - change Admin PIN
  4 - set the Reset Code
  Q - quit

  Your selection? 3
  PIN changed.

  Your selection? Q

.. code-block:: bash
  :caption: Set the **user** password (Remember to use the Default PIN if needed).
  :emphasize-lines: 1,4,13,16

  gpg/card> admin
  Admin commands are allowed

  gpg/card> passwd
  gpg: OpenPGP card no. XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX detected

  1 - change PIN
  2 - unblock PIN
  3 - change Admin PIN
  4 - set the Reset Code
  Q - quit

  Your selection? 1
  PIN changed.

  Your selection? Q

.. code-block:: bash
  :caption: Set the **name** used in the GPG credentials to load.
  :emphasize-lines: 1-3

  gpg/card> name
  Cardholders surname: {USER LAST NAME}
  Cardholders given name: {USER FIRST NAME}

.. code-block:: bash
  :caption: Set the **language** for the GPG user.
  :emphasize-lines: 1-2

  gpg/card> lang
  Language preferences: en

.. code-block:: bash
  :caption: Set the **URL** to locaiton of user's GPG public key.
  :emphasize-lines: 1-2

  gpg/card> url
  URL to retrieve public key: https://keybase.io/{USER}/pgp_keys.asc

.. note::
  As shown using https://keybase.io as the location, but any publically
  accessible location with the public key material will work.

.. code-block:: bash
  :caption: Set **login** to GPG email account used.
  :emphasize-lines: 1-2

  gpg/card> login
  Login data (account name): {GPG USER EMAIL ADDRESS}

.. code-block:: bash
  :caption: Set **forcesig** to always require PIN to access GPG key material.
  :emphasize-lines: 1

  gpg/card> forcesig

.. code-block:: bash
  :caption: Verify configuration and quit to save.
  :emphasize-lines: 8-13,19

  gpg/card> {PRESS ENTER}

  Reader ...........: Yubico YubiKey OTP FIDO CCID 0
  Application ID ...: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  Version ..........: 3.4
  Manufacturer .....: Yubico
  Serial number ....: XXXXXXXXXX
  Name of cardholder: {USER FIRST NAME} {USER LAST NAME}
  Language prefs ...: en
  Sex ..............: unspecified
  URL of public key : https://keybase.io/{USER}/pgp_keys.asc
  Login data .......: {GPG USER EMAIL ADDRESS}
  Signature PIN ....: forced
  Key attributes ...: rsa4096 rsa4096 rsa4096
  Max. PIN lengths .: 127 127 127
  PIN retry counter : 3 3 3
  Signature counter : 0

  gpg/card> quit

.. code-block:: bash
  :caption: Require touch each time `authentication, encryption or signing request`_ occurs.
  :emphasize-lines: 1-3

  ykman openpgp set-touch aut fixed
  ykman openpgp set-touch sig fixed
  ykman openpgp set-touch enc fixed

.. note::
  *Fixed* is the same as *on* but requires a `new certificate to be loaded`_ if
  this option is ever disabled.

.. _new certificate to be loaded: https://developers.yubico.com/PGP/Card_edit.html
.. _authentication, encryption or signing request: https://suchsecurity.com/gpg-and-ssh-with-yubikey-on-windows.html
.. _destroy any openpgp material: https://support.yubico.com/support/solutions/articles/15000006421-resetting-the-openpgp-applet-on-the-yubikey
.. _Yubikey Personalization Tool: https://www.yubico.com/products/services-software/download/yubikey-personalization-tools/
