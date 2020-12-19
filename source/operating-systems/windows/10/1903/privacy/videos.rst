.. _w10-1903-reasonable-privacy-videos:

Videos
######
:cmdmenu:`⌘ + r --> ms-settings:privacy-videos`

.. dropdown:: Allow access to video libraries on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Leave enabled. Can restrict video folder access from all apps and Windows.
  There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Deny`` will disable all access.

    .. wregedit:: Disable access to video libraries on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\videosLibrary
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. dropdown:: Allow app access to video libraries on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable app ccess to video libraries on this device
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\videosLibrary
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. rubric:: References

#. `Access to Video Library <https://www.tenforums.com/tutorials/102567-allow-deny-os-apps-access-videos-library-windows-10-a.html>`_

