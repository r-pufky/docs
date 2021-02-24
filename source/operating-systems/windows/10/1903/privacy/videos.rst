.. _w10-1903-reasonable-privacy-videos:

Videos
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-videos`

.. regedit:: Allow access to video libraries on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\videosLibrary
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/102567-allow-deny-os-apps-access-videos-library-windows-10-a.html
  :update:   2021-02-19

  ``Deny`` will disable all access.

  Leave enabled. Can restrict video folder access from all apps and Windows.
  There is no GPO equivalent.

.. regedit:: Allow app ccess to video libraries on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\videosLibrary
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/102567-allow-deny-os-apps-access-videos-library-windows-10-a.html
  :update:   2021-02-19

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.
