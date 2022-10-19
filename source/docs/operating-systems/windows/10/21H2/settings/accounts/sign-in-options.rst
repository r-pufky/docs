.. _w10-21h2-settings-accounts-sign-in-options:

Sign-in options
###############

Manage how you sign into your device
************************************
.. dropdown:: Disable Windows Hello Face, Fingerprint, PIN
  :icon: shield-lock
  :animate: fade-in

  Facial recognition (Hello-Face) and Fingerprint ID are used to automatically
  unlock your computer with your camera/fingerprint reader. Disable this.

  .. gpo::    Disable the use of Biometrics
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Biometrics --> Allow the use of biometrics
    :value0:  ☑, {DISABLED}
    :ref:     https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable user login with Biometrics
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Biometrics --> Allow users to log on using biometrics
    :value0:  ☑, {DISABLED}
    :ref:     https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
    :update:  2021-02-19
    :generic:
    :open:

  .. gpo::    Disable domain user login with Biometrics
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Biometrics --> Allow domain users to log on using biometrics
    :value0:  ☑, {DISABLED}
    :ref:     https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
    :update:  2021-02-19
    :generic:
    :open:

  .. gui::    Disable facial recognition schedule tasks
    :label:   Task Scheduler
    :nav:     ⌘ --> Task Scheduler --> Task Scheduler Library
    :path:    Microsoft --> Windows --> HelloFace --> FODCleanupTask -->
              {RMB} --> Disable
    :value0:  Name, FODCleanupTask
    :ref:     https://github.com/adolfintel/Windows10-Privacy#hello-face
    :update:  2021-02-19
    :generic:
    :open:

.. dropdown:: Disable Picture Password
  :icon: shield-lock
  :animate: fade-in

  .. gpo::    Disable the use of Biometrics
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Logon --> Turn off picture password sign-in
    :value0:  ☑, {ENABLED}
    :ref:     https://www.top-password.com/blog/disable-windows-10-face-recognition-or-fingerprint-login
    :update:  2021-02-19
    :generic:
    :open:

Require Sign-in
***************
.. dropdown:: If you've been away, should Windows require you to sign-in again?
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  Require sign-in when PC wakes from sleep.

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

  .. gpo::    Disable local account security questions
    :path:    Computer Configuration -->
              Administrative Templates -->
              Windows Components -->
              Credential User Interface -->
              Prevent the use of security questions for local accounts
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/117755-enable-disable-security-questions-local-accounts-windows-10-a.html
              https://www.cyclonis.com/windows-10-security-questions-not-secure/
    :update:  2022-01-20
    :generic:
    :open:

Privacy
*******
.. dropdown:: Disable Show account details such as my email address on the sign-in screen.
  :color: primary
  :icon: shield-lock
  :animate: fade-in
  :class-container: sd-shadow-sm

  .. gpo::    Disable Show account details such as my email address on the
              sign-in screen
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              Logon --> Block user from showing account details on sign-in
    :value0:  ☑, {ENABLED}
    :ref:     https://www.tenforums.com/tutorials/52908-enable-disable-sign-screen-email-address-windows-10-a.html
    :update:  2021-02-19
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

  Disable caching of credentials for auto-login. This causes spurious update
  user account password resets, see:
  :ref:`wbase-specific-windows-fixes-reset-password`.