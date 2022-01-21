.. _wbase-specific-windows-fixes-usb-devices-slow:

USB Devices Slow
################
In Windows 1809+ default USB removal policy changed to ``Quick removal`` for
additional safety instead of ``Better performance`` for additional speed; as a
result USB devices may appear slower than normal. This reverts to the old
behavior.

.. gui::   Enable Better Performance for USB Devices
  :path:   ⌘ + x -->
           Disk Management -->
           RMB {USB DEVICE} -->
           Properties -->
           Policies
  :value0: Removal policy,
  :value1: › ☑, Better performance
  :value2: Write-caching policy,
  :value3: › ☑, Enable write caching on the device
  :ref:    https://docs.microsoft.com/en-us/windows/client-management/change-default-removal-policy-external-storage-media
  :update: 2021-02-19
