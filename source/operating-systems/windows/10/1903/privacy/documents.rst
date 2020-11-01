.. _w10-1903-reasonable-privacy-documents:

Documents
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-documents`

.. rubric:: Allow access to document libraries on this device

.. wregedit:: Disable access to document libraries on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\documentsLibrary
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:
  :no_launch:

    .. note::
      There is no GPO equivalent.