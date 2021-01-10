.. _w10-20h2-wi-fi:

Wi-Fi
#####

Hotspot 2.0 networks
********************
.. dropdown:: Disable let me use online sign-up to get connected
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Don't show a list of providers for hotspot connections.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.tips-howto.com/tips-how-to-activate-hotspot-2-0-wi-fi-networks-in-windows-10/>`_

    .. wregedit:: Disable let me use online sign-up to get connected
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WlanSvc\AnqpCache
      :names:     OsuRegistrationStatus
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
