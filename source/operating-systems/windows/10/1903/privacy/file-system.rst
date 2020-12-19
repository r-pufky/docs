.. _w10-1903-reasonable-privacy-file-system:

File System
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-broadfilesystemaccess`

.. dropdown:: Allow access to file system on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Option is worded poorly. This prevents apps from accessing private data on the
  file system.

  Leave enabled. Can restrict document folder access from all apps and Windows.
  There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    ``Deny`` will disable all access.

    .. wregedit:: Disable access to file system on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\broadFileSystemAccess
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. dropdown:: Allow app access to file system on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-1903-privacy-app-list` to generate a list of apps for more fine
  grained control of app access. There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable app ccess to file system on this device
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\broadFileSystemAccess
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

.. rubric:: References

#. `Access to File Systems <https://www.tenforums.com/tutorials/104030-allow-deny-apps-access-file-system-windows-10-a.html>`_
