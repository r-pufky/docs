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
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Require Sign-in plugged in
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  Power Management -->
                  Sleep Settings -->
                  Require a password when a computer wakes (plugged in)
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

    .. wgpolicy:: Require Sign-in on battery
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  Power Management -->
                  Sleep Settings -->
                  Require a password when a computer wakes (on battery)
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:
      :no_launch:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Require Sign-in for all users
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Power
                  PowerSettings\0e796bdb-100d-47d6-a2d5-f7d2daa51f51
      :names:     DCSettingIndex,
                  ACSettingIndex
      :types:     DWORD,
                  DWORD
      :data:      1,
                  1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/11129-turn-off-require-sign-wakeup-windows-10-a.html>`__

Privacy
*******
.. dropdown:: Disable Show account details such as my email address on the sign-in screen.
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Show account details such as my email address on the
                  sign-in screen
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  System -->
                  Logon -->
                  Block user from showing account details on sign-in
      :option:    ☑
      :setting:   Enabled
      :no_section:
      :no_caption:

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable Show account details such as my email address on the
                  sign-in screen
      :key_title: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
      :names:     BlockUserFromShowingAccountDetailsOnSignin
      :types:     DWORD
      :data:      1
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/52908-enable-disable-sign-screen-email-address-windows-10-a.html>`__

.. dropdown:: Disable Use my sign-in info to automatically finish setting up my
              device after an update or restart
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Disable caching of credentials for auto-login. Registry edits require per-user
  SID edits, only GPO is shown.
    
  .. dropdown:: :term:`GPO`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wgpolicy:: Disable Use my sign-in info to automatically finish setting up my
                  device after an update or restart
      :key_title: Computer Configuration -->
                  Administrative Templates -->
                  Windows Components -->
                  Windows Logon Options -->
                  Sign-in and lock last interactive user automatically after a restart
      :option:    ☑
      :setting:   Disabled
      :no_section:
      :no_caption:

  `Reference <https://www.tenforums.com/tutorials/49963-use-sign-info-auto-finish-after-update-restart-windows-10-a.html>`__
