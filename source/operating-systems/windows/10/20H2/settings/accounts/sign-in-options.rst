.. _w10-20h2-settings-accounts-sign-in-options:

Sign-in options
###############

Require Sign-in
***************
.. dropdown:: If you've been away, should Windows require you to sign-in again?
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Require sign-in whenever PC wakes from sleep.

  .. gpo::    Require Sign-in plugged in
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Power Management -->
              Sleep Settings -->
              Require a password when a computer wakes (plugged in)
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/11129-turn-off-require-sign-wakeup-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Require Sign-in on battery
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Power Management -->
              Sleep Settings -->
              Require a password when a computer wakes (on battery)
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/11129-turn-off-require-sign-wakeup-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Require Sign-in for all users
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Power
               PowerSettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51
    :value0:   DCSettingIndex, {DWORD}, 1
    :value1:   ACSettingIndex, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/11129-turn-off-require-sign-wakeup-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

Privacy
*******
.. dropdown:: Disable Show account details such as my email address on the sign-in screen.
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  .. gpo::    Disable Show account details such as my email address on the
              sign-in screen
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Logon -->
              Block user from showing account details on sign-in
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/52908-enable-disable-sign-screen-email-address-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable Show account details such as my email address on the
               sign-in screen
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
    :value0:   BlockUserFromShowingAccountDetailsOnSignin, {DWORD}, 1
    :ref:      https://www.tenforums.com/tutorials/52908-enable-disable-sign-screen-email-address-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:

.. gpo::    Disable Use my sign-in info to automatically finish setting up my
            device after an update or restart
  :path:    Computer Configuration -->
            Administrative Templates -->
            Windows Components -->
            Windows Logon Options -->
            Sign-in and lock last interactive user automatically after a restart
  :value0:  ☑, {DISABLED}
  :ref:     https://www.tenforums.com/tutorials/49963-use-sign-info-auto-finish-after-update-restart-windows-10-a.html
  :update:  2021-02-19

  Disable caching of credentials for auto-login. Registry edits require per-user
  SID edits, only GPO is shown.
