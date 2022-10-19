.. _w10-21h2-settings-privacy-general:

General
#######
:cmdmenu:`⌘ + r --> ms-settings:privacy-general`

Change privacy options
**********************
.. dropdown:: Disable Let apps use advertising ID to make ads more interesting
              to you based on your app usage (turning this off will reset your
              ID.)
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable Let apps use advertising ID to make ads more
              interesting to you based on your app usage (turning this off
              will reset your ID.)
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              User Profiles -->
              Turn off the advertising ID
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/76453-enable-disable-advertising-id-relevant-ads-windows-10-a.html#option4
    :update:  2021-02-19
    :generic:
    :open:

.. regedit:: Disable Let websites provide locally relevant content by
             accessing my language list
  :path:     HKEY_CURRENT_USER\Control Panel\International\User Profile
  :value0:   HttpAcceptLanguageOptOut, {DWORD}, 1
  :ref:      https://www.tenforums.com/tutorials/82980-turn-off-website-access-language-list-windows-10-a.html
  :update:   2021-02-19

.. dropdown:: Disable Let Windows track app launches to improve Start and search
              results
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  See :ref:`Disable Show most used apps
  <w10-21h2-settings-personalization-start-most-used-apps>` for additional app
  tracking disable.

  .. gpo::    Disable Let Windows track app launches to improve Start and
              search results
    :path:    User Configuration -->
              Administrative Templates -->
              Windows Components -->
              Edge UI -->
              Turn off tracking of app usage
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/128523-enable-disable-app-launch-tracking-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

.. regedit:: Disable Show me suggested content in the settings app
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             ContentDeliveryManager
  :value0:   SubscribedContent-338393Enabled, {DWORD}, 0
  :value1:   SubscribedContent-353694Enabled, {DWORD}, 0
  :value2:   SubscribedContent-353696Enabled, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/100541-turn-off-suggested-content-settings-app-windows-10-a.html
  :update:   2021-02-19
