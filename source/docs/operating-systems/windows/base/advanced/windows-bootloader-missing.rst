.. _wbase-specific-windows-fixes-windows-bootloader-missing:

Windows Bootloader Missing / Multiple OS
########################################
Fix the UEFI bootloader if it is missing or has extra entries.

Restart in Diagnostics Mode:

:cmdmenu:`shift + restart --> troubleshooting --> command prompt`

.. note::
  :cmdmenu:`shift` can be held during normal boot to get to the same menu.

First remove any extra EFI boot configuration data from other operating
systems.

.. code-block::
  :caption: Remove extra EFI entries before rebuilding Boot Configuration Data
            for Windows.
  :emphasize-lines: 3-4, 10

  diskpart
  list disk
  sel disk 0
  sel vol 2
  assign letter=Z:
  exit
  cd Z:
  cd EFI
  dir
  rmdir -S ubuntu

.. note::
  Look for ~100MB FAT32 partition, this is the standard partition Windows uses
  for storing EFI data. Adjust highlighted lines as needed for specific case.
  ``ubuntu`` removed here. ``Boot`` and ``Microsoft`` should be left intact.

.. code-block::
  :caption: Fix MBR, scan for all OS's on drive and rebuild Boot Configuration
            Data for Windows.

  bootrec /fixmbr
  bootrec /scanos
  bootrec /rebuildbcd

Restart machine.

If there are extra menu options, you may also edit UEFI boot options in firmware
or use EasyUEFI to do it in windows directly.

`Reference <https://linuxbsdos.com/2015/09/05/how-to-delete-grub-files-from-a-boot-efi-partition-in-windows-10/>`__

`Reference <https://www.easyuefi.com/index-us.html>`__
