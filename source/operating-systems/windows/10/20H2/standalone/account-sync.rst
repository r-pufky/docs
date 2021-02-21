.. _w10-20h2-standalone-account-sync:

Account Sync
############
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

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    
    .. wregedit:: Disable user account sync
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync
      :names:     DisableSettingSync
      :types:     DWORD
      :data:      2
      :no_section:
      :no_caption:

    .. wregedit:: Disable user account sync override
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync
      :names:     DisableSettingSyncUserOverride
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in

    .. wgpolicy:: Disable user account sync
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Sync your settings -->
                  Do not sync
      :option:    ☑,
                  ☐
      :setting:   Enabled,
                  Allow users to turn syncing on.
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/43246-enable-disable-sync-your-settings-windows-10-a.html>`__
