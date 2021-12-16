.. _w10-1903-disable-account-sync:

Disable Account Sync
####################
If using a *live* account, Microsoft will automatically upload your account data
to their servers. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Disable user account sync
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Disable account sync and prevent users from turning it on.

  .. gpo::    Disable user account sync
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Sync your settings -->
              Do not sync
    :value0:  ☑, {ENABLED}
    :value1:  ☐, Allow users to turn syncing on
    :ref:     https://www.tenforums.com/tutorials/43246-enable-disable-sync-your-settings-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable user account sync
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync
    :value0:   DisableSettingSync, {DWORD}, 2
    :ref:      https://www.tenforums.com/tutorials/43246-enable-disable-sync-your-settings-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

  .. regedit:: Disable user account sync override
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync
    :value0:   DisableSettingSyncUserOverride, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/43246-enable-disable-sync-your-settings-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:
