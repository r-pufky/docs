.. _w10-1903-reasonable-privacy-file-system:

File System
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-broadfilesystemaccess`

.. note::
  Option is worded poorly. This prevents apps from accessing private data on the
  file system.

.. rubric:: Allow access to file system on this device

.. wregedit:: Disable access to file system on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\broadFileSystemAccess
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:
  :no_launch:

    .. note::
      There is no GPO equivalent.