.. _w10-1903-disable-delivery-optimization:

Disable Delivery Optimization
#############################
By default updates are shared and downloaded via P2P for all Windows machines.
Disable this.

.. ggui:: Disable Delivery Optimization
  :key_title: ⌘ + r -->
              ms-settings:delivery-optimization
  :option:    Allow downloads from other PCs
  :setting:   ☐
  :no_section:
  :no_launch:

:term:`Registry` Machine
************************
.. wregedit:: Disable delivery optimization via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\DeliveryOptimization
  :names:     DODownloadMode
  :types:     DWORD
  :data:      0
  :no_section:

:term:`GPO` Computer
********************
.. wgpolicy:: Disable delivery optimization via machine GPO
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

    .. note:: 
      Either disable entirely, or enable with the ``Bypass (100)`` option.

.. rubric:: References

#. `Disable P2P Updates Group Policy <https://www.tenforums.com/windows-updates-activation/94567-windows-update-using-all-available-bandwidth-disabled-p2p-updates-3.html>`_
#. `Disable P2P Updates Registry <https://social.technet.microsoft.com/Forums/en-US/e1f7090b-2e93-4276-a12b-ee5c2463bb58/how-can-we-disable-peer-to-peer-update-with-gpo?forum=win10itprogeneral>`_

.. _Disable Wifi Sharing: https://www.thewindowsclub.com/disable-wi-fi-sense-windows-10-enterprise
