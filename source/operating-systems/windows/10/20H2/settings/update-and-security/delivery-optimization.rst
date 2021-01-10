.. _w10-20h2-delivery-optimization:

Delivery Optimization
#####################
.. dropdown:: Disable Allow downloads from other PCs
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:
  
  `Reference <https://social.technet.microsoft.com/Forums/en-US/e1f7090b-2e93-4276-a12b-ee5c2463bb58/how-can-we-disable-peer-to-peer-update-with-gpo?forum=win10itprogeneral>`_
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable delivery optimization
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Delivery Optimization -->
                  Download Mode
      :option:    ☑,
                  Download Mode
      :setting:   Enabled,
                  Bypass (100)
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable delivery optimization
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows
                  DeliveryOptimization
      :names:     DODownloadMode
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
