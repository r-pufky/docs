.. _w10-20h2-settings-privacy-pictures:

Pictures
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-pictures`

See :ref:`wbase-determining-app-list` to generate a list of apps for more fine
grained control of app access.

Allow access to picture libraries on this device
************************************************
.. regedit:: Enable Allow access to picture libraries on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\picturesLibrary
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/102590-allow-deny-os-apps-access-pictures-library-windows-10-a.html
  :update:   2021-02-19

  Do not configure or leave enabled. Can restrict picture folder access from all
  apps and Windows. There is no GPO equivalent.

  ``Deny`` will disable all access.

Allow app access to picture libraries on this device
****************************************************
.. regedit:: Enable Allow app access to picture libraries on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\picturesLibrary
  :value0:   Value, {SZ}, Allow
  :ref: https://www.tenforums.com/tutorials/102590-allow-deny-os-apps-access-pictures-library-windows-10-a.html
  :update:   2021-02-19

  Do not configure or leave enabled. Can restrict picture folder access from all
  apps and Windows. There is no GPO equivalent.

Choose which apps can access your pictures library
**************************************************
See :ref:`w10-20h2-settings-privacy-pictures`.
