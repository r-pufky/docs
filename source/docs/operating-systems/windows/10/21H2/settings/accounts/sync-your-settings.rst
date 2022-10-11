.. _w10-21h2-settings-accounts-sync-your-settings:

Sync Your Settings
##################
If using a *live* account, Microsoft will automatically upload your account
data to their servers. Disable this.

.. danger::
  After every major windows update, verify these settings.

.. dropdown:: Sync Your Settings
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
