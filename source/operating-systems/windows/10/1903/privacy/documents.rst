.. _w10-1903-reasonable-privacy-documents:

Documents
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-documents`

.. regedit:: Allow access to document libraries on this device
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\documentsLibrary
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/102595-allow-deny-os-apps-access-documents-library-windows-10-a.html
  :update:   2021-02-19

  Leave enabled. Can restrict document folder access from all apps and Windows.
  There is no GPO equivalent.

  ``Deny`` will disable all access.

.. regedit:: Disable app ccess to document libraries on this device
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             CapabilityAccessManager\ConsentStore\documentsLibrary
  :value0:   Value, {SZ}, Allow
  :ref:      https://www.tenforums.com/tutorials/102595-allow-deny-os-apps-access-documents-library-windows-10-a.html
  :update:   2021-02-19

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.
