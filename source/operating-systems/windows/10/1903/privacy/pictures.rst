.. _w10-1903-reasonable-privacy-pictures:

Pictures
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-pictures`

.. rubric:: Allow access to picture libraries on this device

.. wregedit:: Disable access to picture libraries on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\picturesLibrary
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:
  :no_launch:

    .. note::
      There is no GPO equivalent.