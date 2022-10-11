.. _wbase-run-windows-on-usb:

Run Windows On USB
##################
Download the `WinToUSB <https://www.easyuefi.com/wintousb>`__ tool and install.
Select a Windows 10 ISO that is one version behind the current version
(otherwise you must register the tool).

#. Select the windows ISO to use.
#. Set appropriate Windows version for your hardware license.
#. Set :cmdmenu:`GPT for UEFI`.
#. Create disk. This will take a few minutes as Windows 10 is actually being
   installed to the USB drive.

Once done, just select the :cmdmenu:`Windows Boot Manager` label for the USB
disk to boot into a clean Windows install.

.. caution::
  Remember to update to the latest Windows version.

`Reference <https://www.pcmag.com/article/352209/how-to-run-windows-10-from-a-usb-drive>`__
