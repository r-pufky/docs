.. _w10-1903-reasonable-privacy-general:

General
#######
:cmdmenu:`⌘ + r --> ms-settings:privacy-general`

.. dropdown:: Let apps use advertising ID to make ads more interesting to you
              based on your app usage (turning this off will reset your ID.)
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable Advertising ID
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  AdvertisingInfo
      :names:     Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

    .. wregedit:: Allow GPO to override Disable Advertising ID
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
                  AdvertisingInfo
      :names:     DisabledByGroupPolicy
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable Advertising ID
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  User Profiles -->
                  Turn off the advertising ID
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

.. dropdown:: Let websites provide locally relevant content by accessing my
              language list
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable language list access
      :key_title: HKEY_CURRENT_USER\Control Panel\International\User Profile
      :names:     HttpAcceptLanguageOptOut
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

.. dropdown:: Let Windows track app launches to improve Start and search results
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable windows tracking of app launches
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  Explorer\Advanced
      :names:     Start_TrackProgs
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. dropdown:: Show me suggested content in the settings app
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in

    .. wregedit:: Disable suggested content in settings app
      :key_title: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
                  ContentDeliveryManager
      :names:     SubscribedContent-338393Enabled,
                  SubscribedContent-353694Enabled,
                  SubscribedContent-353696Enabled
      :types:     DWORD,
                  DWORD,
                  DWORD
      :data:      0,
                  0,
                  0
      :no_section:
      :no_caption:

.. rubric:: Rreferences

#. `General Privacy Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general>`_
#. `Disable Suggested Content via Registry <https://www.tenforums.com/tutorials/100541-turn-off-suggested-content-settings-app-windows-10-a.html#option2>`_
