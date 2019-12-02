.. _apps-putty:

Putty Configuration
###################
Generic notes until more finalized.

Putty Timeouts
**************

:cmdmenu:`putty --> connection --> enable tcp keepalives`

:cmdmenu:`putty --> connection --> seconds between keepalives --> 5`

.. code-block:: powershell
  :caption: Export putty settings (or go through full registry dump).

  regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham

Create a `putty shortcut that launches a profile`.

Changing Escape Characters
**************************
Sometimes the terminal escape sequences that are sent are changed if you are
running through multiple screen sessions into docker, etc.

.. code-block:: bash
  :caption: Determine the current escape sequences.

  stty -a

.. note::
  Find the escape sequence you are looking for (e.g. erase is for delete).

.. code-block:: bash
  :caption: Determine the actual control sequence sent.

  ctrl + v, {DESIRED KEY PRESS}

.. note::
  This will print the escape sequence to the terminal

.. code-block:: bash
  :caption: Set the correct sequence.

  stty erase ^H

.. note::
  * Sets the correct escape sequence.
  * Press the key instead of manually typing it.

Forwarding X Windows
********************
Use `VcXsrv`_ instead of xming. This is fully functional and does not have
copy/paste or resizing disabled. Install as normal.

:download:`config.xlaunch example file <source/config.xlaunch>`.

#. Save X window server settings to config file

   * :cmdmenu:`start --> xlaunch`
   * Run through the configuration and save options to file ``config.xlaunch``.
   * Move ``config.xlaunch`` to ``c:\Program Files\VcXsrv\``.


#. Edit xlaunch shortcut

   * ``C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VcXsrv``
   * :cmdmenu:`XLaunch --> RMB --> properties --> Target`

     .. code-block:: powershell

       "C:\Program Files\VcXsrv\xlaunch.exe" -run config.xlaunch

#. Save and launch ``XLaunch``. Settings should load automatically and start
   xserver.

.. rubric:: References

#. `Backspace tab not working in terminal <https://unix.stackexchange.com/questions/43103/backspace-tab-not-working-in-terminal-using-ssh>`_

.. _VcXsrv: https://sourceforge.net/projects/vcxsrv/files/vcxsrv/
.. _putty shortcut that launches a profile: http://superuser.com/questions/248099/a-putty-shortcut-that-automatically-launches-a-profile
