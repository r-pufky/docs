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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. ggui:: Disable delivery optimization
      :key_title: ⌘ + r -->
                  ms-settings:delivery-optimization
      :option:    Allow downloads from other PCs
      :setting:   ☐
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable delivery optimization
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization
      :names:     DODownloadMode
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    The service can be disabled entirely or left enabled with the ``Bypass
    (100)`` option, effectively disabling it.

    .. wgpolicy:: Disable delivery optimization
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Delivery Optimization -->
                  Download Mode
      :option:    ☑,
                  Download Mode
      :setting:   Disabled,
                  Bypass (100)
      :no_section:
      :no_caption:

.. rubric:: References

#. `Disable P2P Updates Group Policy <https://www.tenforums.com/windows-updates-activation/94567-windows-update-using-all-available-bandwidth-disabled-p2p-updates-3.html>`_
#. `Disable P2P Updates Registry <https://social.technet.microsoft.com/Forums/en-US/e1f7090b-2e93-4276-a12b-ee5c2463bb58/how-can-we-disable-peer-to-peer-update-with-gpo?forum=win10itprogeneral>`_

.. _Disable Wifi Sharing: https://www.thewindowsclub.com/disable-wi-fi-sense-windows-10-enterprise
