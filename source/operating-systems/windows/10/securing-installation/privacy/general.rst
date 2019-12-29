.. _windows-10-reasonable-privacy-general:

General
#######
:cmdmenu:`⌘ + r --> ms-settings:privacy-general`

.. rubric:: Let apps use advertising ID to make ads more interesting to you
            based on your app usage (turning this off will reset your ID)

.. wregedit:: Disable Advertising ID via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\
              AdvertisingInfo
  :names:     Enabled
  :types:     DWORD
  :data:      0
  :no_section:

.. wregedit:: Allow GPO to override Disable Advertising ID via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\
              AdvertisingInfo
  :names:     DisabledByGroupPolicy
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

.. wgpolicy:: Disable Advertising ID via machine GPO
  :key_title: Computer Configuration -->
              Administrative Templates -->
              System -->
              User Profiles -->
              Turn off the advertising ID
  :option:    ☑
  :setting:   Enabled
  :no_section:

.. rubric:: Let websites provide locally relevant content by accessing my
            language list

.. wregedit:: Disable language list access via Registry
  :key_title: HKEY_CURRENT_USER\Control Panel\International\User Profile
  :names:     HttpAcceptLanguageOptOut
  :types:     DWORD
  :data:      1
  :no_section:

    .. note::
      There is no GPO equivalent.

.. rubric:: Let Windows track app launches to improve Start and search results

.. wregedit:: Disable windows tracking of app launches via Registry
  :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
              Explorer\Advanced
  :names:     Start_TrackProgs
  :types:     DWORD
  :data:      0
  :no_section:
  :no_launch:

    .. note::
      There is no GPO equivalent.

.. rubric:: Show me suggested content in the Settings app

.. wregedit:: Disable suggested content in settings app via Registry
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
  :no_launch:

    .. note::
      There is no GPO equivalent.

.. rubric:: Rreferences

#. `General Privacy Windows Management Settings <https://docs.microsoft.com/en-us/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-general>`_
#. `Disable Suggested Content via Registry <https://www.tenforums.com/tutorials/100541-turn-off-suggested-content-settings-app-windows-10-a.html#option2>`_
