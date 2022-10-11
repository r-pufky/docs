.. _wbase-specific-windows-fixes-reset-password:

Reset Password
##############
Windows 10+ has a habit of locking out after updates. If there is no
alternative account to login with, then the password must be cleared from the
SAM database on disk using a Live USB image:

#. Download `Hiren BootCD ISO <https://www.hirensbootcd.org/download/>`__.
#. Use ``dd`` or :ref:`wbase-pro-install-boot-disk` to create a bootable USB
   drive.
#. Boot USB drive to Hiren's BootCD
#. :cmdmenu:`utilities --> securit --> passwords --> lazesoft password security`

.. note::
  Accounts may only be reset and unlocked (no password); passwords cannot be
  set in this tool without a license. Reseting the account will also clear
  saved tokens, such as chrome autologins.

If there is an alternative account to login with (no admin required) then reset
your password from safe mode:

Be sure to hold ``shift`` until the troubleshooting options appear.
:cmdmenu:`Login Screen --> shift (hold) + Restart --> Troubleshoot --> Advanced options --> Startup Settings --> Restart -> Enable Safe Mode with Command Prompt`

.. code-block:: powershell
  :caption: Find the correct user and set password.

  net user
  net user {USER} {PASS}

Recent updates now require a valid login when booting to safe mode, but do not
require an admin account.

`Reference <https://www.passfab.com/windows-tips/windows-10-password-incorrect-after-update.html>`__

`Reference <https://www.wimware.com/how-to/reset-windows-10-password-command-prompt.html>`__
