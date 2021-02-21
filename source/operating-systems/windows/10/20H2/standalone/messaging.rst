.. _w10-20h2-standalone-privacy-messaging:

Messaging
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-messaging`

These messaging options are not available in the GUI. See
:ref:`Messaging <w10-20h2-settings-privacy-messaging>` for GUI options.

.. dropdown:: Turn off message sync
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable message sync
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Messaging -->
                  Allow Message Service Cloud Sync
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``1`` enable message sync.

    .. wregedit:: Disable message sync
      :key_title: HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Messaging
      :names:     AllowMessageSync
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  `Reference <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging>`__
