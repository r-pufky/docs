.. _w10-20h2-settings-system-shared-experiences:

Shared Experiences
##################

Nearby Sharing
**************
.. dropdown:: Disable share content with a nearby device by using Bluetooth and Wi-Fi
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Automatically connects to machines for sharing files.

  .. regedit:: Disable share content with a nearby device by using Bluetooth and Wi-Fi
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CDP
    :value0:   NearShareChannelUserAuthzPolicy, {DWORD}, 0
    :value1:   CdpSessionUserAuthzPolicy,       {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/97582-turn-off-nearby-sharing-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` off, ``1`` my devices only, ``2`` everyone.

  .. regedit:: Disable share content with a nearby device by using Bluetooth and Wi-Fi
    :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\CDP\
               SettingsPage
    :value0:   NearShareChannelUserAuthzPolicy, {DWORD}, 0
    :value1:   BluetoothLastDisabledNearShare,  {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/97582-turn-off-nearby-sharing-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

    ``0`` off, ``1`` my devices only, ``2`` everyone.

Share across devices
********************
.. dropdown:: Disable let apps on other devices (including linked phones and
              tablets) open and message apps on this device, and vice versa
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Automatically accepts connections for sharing files.

  .. gpo::    Disable let apps on other devices (including linked phones and
              tablets) open and message apps on this device, and vice versa
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Group Policy -->
              Continue experiences on this device
    :value0:  ☑, {DISABLED}
    :ref:     https://www.windowscentral.com/how-disable-shared-experiences-windows-10
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable let apps on other devices (including linked phones and
               tablets) open and message apps on this device, and vice versa
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
    :value0:   EnableCdp, {DWORD}, 0
    :ref:      https://www.windowscentral.com/how-disable-shared-experiences-windows-10
    :update:   2021-02-19
    :generic:
    :open:
