.. _w10-20h2-settings-privacy-general:

General
#######
:cmdmenu:`⌘ + r --> ms-settings:privacy-general`

Change privacy options
**********************
.. dropdown:: Disable Let apps use advertising ID to make ads more interesting
              to you based on your app usage (turning this off will reset your
              ID.)
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Let apps use advertising ID to make ads more
                  interesting to you based on your app usage (turning this off
                  will reset your ID.)
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  User Profiles -->
                  Turn off the advertising ID
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Let apps use advertising ID to make ads more
                  interesting to you based on your app usage (turning this off
                  will reset your ID.)
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

  `Reference <https://www.tenforums.com/tutorials/76453-enable-disable-advertising-id-relevant-ads-windows-10-a.html#option4>`__

.. dropdown:: Disable Let websites provide locally relevant content by accessing
              my language list
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Let websites provide locally relevant content by
                  accessing my language list
      :key_title: HKEY_CURRENT_USER\Control Panel\International\User Profile
      :names:     HttpAcceptLanguageOptOut
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/82980-turn-off-website-access-language-list-windows-10-a.html>`__

.. dropdown:: Disable Let Windows track app launches to improve Start and search
              results
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  See :ref:`w10-20h2-settings-personalization-start-most-used-apps` for
  additional app tracking disable.

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Let Windows track app launches to improve Start and
                  search results
      :key_title: User Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Edge UI
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Let Windows track app launches to improve Start and
                  search results
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\EdgeUI
      :names:     DisableMFUTracking
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/128523-enable-disable-app-launch-tracking-windows-10-a.html>`__

.. dropdown:: Disable Show me suggested content in the settings app
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

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

  `Reference <https://www.tenforums.com/tutorials/100541-turn-off-suggested-content-settings-app-windows-10-a.html>`__
