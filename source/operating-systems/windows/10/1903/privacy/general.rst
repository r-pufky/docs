.. _w10-1903-reasonable-privacy-general:

General
#######
:cmdmenu:`⌘ + r --> ms-settings:privacy-general`

.. dropdown:: Let apps use advertising ID to make ads more interesting to you
              based on your app usage (turning this off will reset your ID.)
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Advertising ID
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              User Profiles -->
              Turn off the advertising ID
    :value0:  ☑, {ENABLED}
    :ref:     https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Advertising ID
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
               AdvertisingInfo
    :value0:   Enabled, {DWORD}, 0
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Allow GPO to override Disable Advertising ID
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
               AdvertisingInfo
    :value0:   DisabledByGroupPolicy, {DWORD}, 1
    :ref:      https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general
    :update:   2021-02-19
    :generic:
    :open:

.. regedit:: Disable Let websites provide locally relevant content by accessing
             mylanguage list
  :path:     HKEY_CURRENT_USER\Control Panel\International\User Profile
  :value0:   HttpAcceptLanguageOptOut, {DWORD}, 1
  :ref: https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general
  :update:   2021-02-19

.. regedit:: Disable Let Windows track app launches to improve Start and search
             results
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             Explorer\Advanced
  :value0:   Start_TrackProgs, {DWORD}, 0
  :ref: https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general
  :update:   2021-02-19

.. regedit:: Disable Show me suggested content in the settings app
  :path:     HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\
             ContentDeliveryManager
  :value0:   SubscribedContent-338393Enabled, {DWORD}, 0
  :value1:   SubscribedContent-353694Enabled, {DWORD}, 0
  :value2:   SubscribedContent-353696Enabled, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/100541-turn-off-suggested-content-settings-app-windows-10-a.html#value02
  :update:   2021-02-19
