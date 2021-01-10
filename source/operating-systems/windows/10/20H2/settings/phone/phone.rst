.. _w10-20h2-phone:

Phone
#####

.. dropdown:: Disable Add a phone
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Phones are easy vectors that can bring in outside threats. Do not pair.
  
  `Reference <https://www.windowscentral.com/how-disable-phone-pc-linking-feature-windows-10>`_
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Add a phone
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  Group Policy -->
                  Phone-PC linking this device
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``EnableMMX`` is an unfortunate name, but correct.

    .. wregedit:: Disable Add a phone
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
      :names:     EnableMmx
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
