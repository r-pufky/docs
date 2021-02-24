.. _w10-1903-disable-delivery-optimization:

Disable Delivery Optimization
#############################
By default updates are shared and downloaded via P2P for all Windows machines.
Disable this.

.. dropdown:: Disable delivery optimization
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  .. dropdown:: GUI
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. ggui:: Disable delivery optimization
      :key_title: ⌘ + r -->
                  ms-settings:delivery-optimization
      :option:    Allow downloads from other PCs
      :setting:   ☐
      :no_section:
      :no_caption:
      :no_launch:

  .. gpo::    Disable delivery optimization
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Delivery Optimization -->
              Download Mode
    :value0:  ☑, {DISABLED}
    :value1:  Download Mode, Bypass (100) 
    :ref:     https://www.tenforums.com/windows-updates-activation/94567-windows-update-using-all-available-bandwidth-disabled-p2p-updates-3.html
    :update:  2021-02-19
    :generic:
    :open:

    The service can be disabled entirely or left enabled with the ``Bypass
    (100)`` option, effectively disabling it.

  .. regedit:: Disable delivery optimization
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization
    :value0:   DODownloadMode, {DWORD}, 0
    :ref:      https://social.technet.microsoft.com/Forums/en-US/e1f7090b-2e93-4276-a12b-ee5c2463bb58/how-can-we-disable-peer-to-peer-update-with-gpo?forum=win10itprogeneral
    :update:   2021-02-19
    :generic:
    :open:
