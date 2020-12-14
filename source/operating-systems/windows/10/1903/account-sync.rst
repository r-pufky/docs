.. _w10-1903-disable-account-sync:

Disable Account Sync
####################
If using a *live* account, Microsoft will automaticall upload your account data
to their servers. Disable this.

.. danger::
  After every major windows update, verify these settings.

:term:`Registry` Machine
************************
.. wregedit:: Disable user account sync via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync
  :names:     DisableSettingSync
  :types:     DWORD
  :data:      2
  :no_section:

.. wregedit:: Disable user account sync override via Registry
  :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\SettingSync
  :names:     DisableSettingSyncUserOverride
  :types:     DWORD
  :data:      1
  :no_section:
  :no_launch:

:term:`GPO` Computer
********************
.. wgpolicy:: Disable user account sync via machine GPO
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

.. rubric:: References

#. `Disabling Microsoft Account Sync <https://www.tenforums.com/tutorials/43246-enable-disable-sync-your-settings-windows-10-a.html>`_
