.. _w10-1903-reasonable-privacy-pictures:

Pictures
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-pictures`

.. regedit:: Allow access to picture libraries on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\picturesLibrary
  :value0:   Value, {SZ}, Deny
  :ref:      https://www.tenforums.com/tutorials/102590-allow-deny-os-apps-access-pictures-library-windows-10-a.html
  :update:   2021-02-19

  Leave enabled. Can restrict picture folder access from all apps and Windows.
  There is no GPO equivalent.

  ``Deny`` will disable all access.

.. regedit:: Allow app access to picture libraries on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\picturesLibrary
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/102590-allow-deny-os-apps-access-pictures-library-windows-10-a.html
  :update:   2021-02-19

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.
