.. _w10-20h2-settings-update-and-security-delivery-optimization:

Delivery Optimization
#####################
.. dropdown:: Disable Allow downloads from other PCs
  :color: primary
  :icon: note
  :animate: fade-in
  :class-container: sd-shadow-sm
  :open:

  .. gpo::    Disable delivery optimization
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Delivery Optimization -->
              Download Mode
    :value0:  ☑, {ENABLED}
    :value1:  Download Mode, Bypass (100)
    :ref:     https://social.technet.microsoft.com/Forums/en-US/e1f7090b-2e93-4276-a12b-ee5c2463bb58/how-can-we-disable-peer-to-peer-update-with-gpo?forum=win10itprogeneral
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable delivery optimization
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows
               DeliveryOptimization
    :value0:   DODownloadMode, {DWORD}, 0
    :ref:      https://social.technet.microsoft.com/Forums/en-US/e1f7090b-2e93-4276-a12b-ee5c2463bb58/how-can-we-disable-peer-to-peer-update-with-gpo?forum=win10itprogeneral
    :update:   2021-02-19
    :generic:
    :open:
