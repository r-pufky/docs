.. _wbase-specific-windows-fixes-enable-bitlocker-on-usb-drives-over-rdp:

Enable Bitlocker on USB drives over RDP
#######################################
By default, bitlocker does not allow encryption to be enabled on USB devices
over RDP connections -- this happens because RDP treats USB drives as mapped
network drives and not external drives. This enables direct drive access for RDP
connections. This is unsafe.

.. gpo::   Enable bitlocker on usb drives over rdp policy
  :path:   Computer Configuration -->
           Administrative Templates -->
           System -->
           Removable Storage Access
  :value0: All Removable Storage: Allow direct access in remote sessions, Enabled
  :ref:    https://superuser.com/questions/962125/bitlocker-refuses-to-enable-via-rdp-on-data-drive-but-ok-on-the-os-drive
  :update: 2021-02-19
