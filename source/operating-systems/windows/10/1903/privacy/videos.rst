.. _w10-1903-reasonable-privacy-videos:

Videos
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-videos`

.. rubric:: Allow access to video libraries on this device

.. wregedit:: Disable access to video libraries on this device via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              CapabilityAccessManager\ConsentStore\videosLibrary
  :names:     Value
  :types:     SZ
  :data:      Deny
  :no_section:
  :no_launch:

    .. note::
      There is no GPO equivalent.