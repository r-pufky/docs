.. _w10-21h2-standalone-privacy-messaging:

Messaging
#########
:cmdmenu:`⌘ + r --> ms-settings:privacy-messaging`

These messaging value0s are not available in the GUI. See
:ref:`Messaging <w10-21h2-settings-privacy-messaging>` for GUI value0s.

.. dropdown:: Turn off message sync
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. gpo::    Disable message sync
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Messaging -->
              Allow Message Service Cloud Sync
    :value0:  ☑, {DISABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#1812-messaging
    :update:  2021-02-19
    :generic:
    :open:
