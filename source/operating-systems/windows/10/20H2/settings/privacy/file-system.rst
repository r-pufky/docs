.. _w10-20h2-settings-privacy-file-system:

File System
###########
:cmdmenu:`⌘ + r --> ms-settings:privacy-broadfilesystemaccess`

Option is worded poorly. This prevents apps from accessing private data on the
file system.

See :ref:`w10-determining-app-list` to generate a list of apps for more fine
grained control of app access. There is no GPO equivalent.

Allow access to file system on this device
******************************************
.. dropdown:: Enable Allow access to file system on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Do not configure or leave enabled. Can restrict document folder access from
  all apps and Windows. There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``Deny`` will disable all access.

    .. wregedit:: Enable Allow access to file system on this device
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\broadFileSystemAccess
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/104030-allow-deny-apps-access-file-system-windows-10-a.html>`__

Allow app access to file system on this device
**********************************************
.. dropdown:: Enable Allow app access to file system on this device
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Do not configure or leave enabled. Can restrict document folder access from
  all apps and Windows. There is no GPO equivalent.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Enable Allow app access to file system on this device
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  CapabilityAccessManager\ConsentStore\broadFileSystemAccess
      :names:     Value
      :types:     SZ
      :data:      Allow
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/104030-allow-deny-apps-access-file-system-windows-10-a.html>`__

Choose which apps can access your file system
*********************************************
See :ref:`w10-20h2-settings-privacy-file-system`.
