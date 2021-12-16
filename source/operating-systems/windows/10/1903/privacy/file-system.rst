.. _w10-1903-reasonable-privacy-file-system:

File System
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-broadfilesystemaccess`

.. regedit:: Allow access to file system on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\broadFileSystemAccess
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/104030-allow-deny-apps-access-file-system-windows-10-a.html
  :update:   2021-02-19

  Option is worded poorly. This prevents apps from accessing private data on the
  file system.

  Leave enabled. Can restrict document folder access from all apps and Windows.
  There is no GPO equivalent.

  ``Deny`` will disable all access.

.. regedit:: Allow app ccess to file system on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\broadFileSystemAccess
  :value0:   Value, {SZ}, Allow
  :ref: https://www.tenforums.com/tutorials/104030-allow-deny-apps-access-file-system-windows-10-a.html
  :update:   2021-02-19

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.
