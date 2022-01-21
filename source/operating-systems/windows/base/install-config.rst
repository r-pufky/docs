.. _wbase-pro-install:

Windows Pro Install
###################
Initial setup of a USB stick to install Windows without a Live Account.

.. _wbase-pro-install-boot-disk:

Creating a UEFI USB Boot Disk
*****************************
Using the Windows Media Creation Tool will create a USB boot disk, however
this will be using MBR. This specific setup will create a UEFI USB boot disk:

* Download full windows 10 ISO image with `Windows Media Creation Tool <https://www.microsoft.com/en-us/software-download/windows10>`__

   * Create installation media for a different PC.
   * Select correct options (typically, english, windows 10 pro, 64-bit).
   * Select save location for the ISO file.

* Create a reusable USB boot Disk with `Ventoy <https://www.ventoy.net/en/index.html>`__

   * Download `latest version <https://www.ventoy.net/en/download.html>`__.
   * Extract and run excutable ``ventory2disk.exe``; existing ventory installs
     can be upgraded as well.
   * Once USB drive is setup, just copy the ISO to the root of the USB disk.
   * Reboot and select the ISO to boot into.

Installing Windows 10 Without Live Account
******************************************

#. Delete all existing partitions.
#. Skip / check later all attempts to enter product key.
#. Select **use a personal account** (non-organizational).
#. Create a **local account**:

    * Create new account.
    * Sign-in **without** a microsoft account.

    .. note::
      This can be found on the lower left corner of the create acount screen.

#. See version specific instructions to finish setup: :ref:`w10-21h2`,
   :ref:`w10-20h2`.
