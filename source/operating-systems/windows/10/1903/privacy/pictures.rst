.. _w10-1903-reasonable-privacy-pictures:

Pictures
########
:cmdmenu:`⌘ + r --> ms-settings:privacy-pictures`

.. dropdown:: Allow access to picture libraries on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Leave enabled. Can restrict picture folder access from all apps and Windows.
  There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Deny`` will disable all access.

    .. wregedit:: Disable access to picture libraries on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\picturesLibrary
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. dropdown:: Allow app access to picture libraries on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable app access to picture libraries on this device
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\picturesLibrary
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. rubric:: References

#. `Access to Picture Library <https://www.tenforums.com/tutorials/102590-allow-deny-os-apps-access-pictures-library-windows-10-a.html>`_
