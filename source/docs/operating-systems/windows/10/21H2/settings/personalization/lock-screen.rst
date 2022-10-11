.. _w10-21h2-settings-personalization-lock-screen:

Lock screen
###########
.. regedit:: Disable get fun facts, tips, tricks, and more on your lock
             screen
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             ContentDeliveryManager
  :value0:   SubscribedContent-338387Enabled, {DWORD}, 0
  :update:   2021-02-19
  :open:

  Contacts Microsoft servers to get information to display.

.. regedit:: Enable show lock screen background picture on the sign-in screen
  :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
  :value0:   DisableLogonBackgroundImage, {DWORD}, 0
  :ref:      https://www.tenforums.com/tutorials/9108-enable-disable-sign-screen-background-image-windows-10-a.html
  :update:   2021-02-19
  :open:
