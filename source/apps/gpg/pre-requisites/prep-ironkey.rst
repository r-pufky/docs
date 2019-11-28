.. _gpg-prep-ironkey:

Prep Ironkey
############
Setup a working ironkey either through :ref:`gpg-prerequisites-initalize` or
:ref:`gpg-prerequisites-reset` before unlocking for GPG use.

.. _gpg-prerequisites-initalize:

Initalize Ironkey
*****************
Do this if fresh Ironkey, or creating a new master key.

.. danger::
  This is **data destructive**.

.. code-block:: bash
  :caption: Initalize Ironkey.

  /media/user/IRONKEY/linux/linux64/ikd300_initalize

.. _gpg-prerequisites-reset:

Reset Ironkey
*************
Wipes a working Ironkey to a default state.

.. danger::
  This is **data destructive**.

.. code-block:: bash
  :caption: Reset Ironkey.

  /media/user/IRONKEY/linux/linux64/ikd300_resetdevice

.. note::
  Max **16** character password. Ironkey will wipe device after 10 failed
  attempts and force phsyical re-insertion after every 3 failed attempts.

Unlock Ironkey
**************
Mount an unlocked Ironkey for GPG usage.

.. code-block:: bash
  :caption: Unlock Ironkey.

  sudo /media/user/IRONKEY/linux/linux64/ikd300_login

* Open browser, click on ``KINGSTON`` to automount to ``/media/user/KINGSTON``.
* This is your hardware-backed encrypted storage.

.. important::
  The Ironkey is the only **safe** location to store secret key material.