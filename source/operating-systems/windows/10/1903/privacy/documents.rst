.. _w10-1903-reasonable-privacy-documents:

Documents
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-documents`

.. dropdown:: Allow access to document libraries on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Leave enabled. Can restrict document folder access from all apps and Windows.
  There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Deny`` will disable all access.

    .. wregedit:: Disable access to document libraries on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\documentsLibrary
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. dropdown:: Allow app access to document libraries on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable app ccess to document libraries on this device
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\documentsLibrary
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. rubric:: References

#. `Access to Document Library <https://www.tenforums.com/tutorials/102595-allow-deny-os-apps-access-documents-library-windows-10-a.html>`_
