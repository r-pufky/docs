.. _windows-10-pro-install:

Windows 10 Pro Install
######################
Initial setup of a USB stick to install Windows without a Live Account.

Creating a UEFI USB Boot Disk
*****************************
Using the `Windows Media Creation Tool`_ will create a USB boot disk, however
this will be using MBR. This specific setup will create a UEFI USB boot disk:

* Download full windows 10 ISO image with `Windows Media Creation Tool`_

   * Create installation media for a different PC.
   * Select correct options (typically, english, windows 10 pro, 64-bit).
   * Select save location for the ISO file.

* Create bootable media with `Rufus`_

   * GPT partition scheme for UEFI.
   * NTFS.
   * Other options are OK for defaults.
   * Once image is applied, dump decompressed Windows 10 drivers for your
     hardware to USB drive as well.

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

#. See :ref:`windows-10-pro-securing-install` to finish setup.

.. _Windows Media Creation Tool: https://www.microsoft.com/en-us/software-download/windows10
.. _Rufus: https://rufus.akeo.ie