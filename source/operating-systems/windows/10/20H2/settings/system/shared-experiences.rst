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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    ``0`` off, ``1`` my devices only, ``2`` everyone.

    `Reference <https://www.tenforums.com/tutorials/97582-turn-off-nearby-sharing-windows-10-a.html>`_

    .. wregedit:: Disable share content with a nearby device by using Bluetooth and Wi-Fi
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CDP
      :names:     NearShareChannelUserAuthzPolicy,
                  CdpSessionUserAuthzPolicy
      :types:     DWORD,
                  DWORD
      :data:      0,
                  0
      :no_section:
      :no_caption:

    .. wregedit:: Disable share content with a nearby device by using Bluetooth and Wi-Fi
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  CDP\SettingsPage
      :names:     NearShareChannelUserAuthzPolicy,
                  BluetoothLastDisabledNearShare
      :types:     DWORD,
                  DWORD
      :data:      0,
                  0
      :no_section:
      :no_caption:
      :no_launch:

Share across devices
********************
.. dropdown:: Disable let apps on other devices (including linked phones and
              tablets) open and message apps on this device, and vice versa
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Automatically accepts connections for sharing files.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    `Reference <https://www.windowscentral.com/how-disable-shared-experiences-windows-10>`_

    .. wgpolicy:: Disable let apps on other devices (including linked phones and
                  tablets) open and message apps on this device, and vice versa
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  Group Policy -->
                  Continue experiences on this device
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable let apps on other devices (including linked phones and
                  tablets) open and message apps on this device, and vice versa
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
      :names:     EnableCdp
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:
