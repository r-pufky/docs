.. _w10-20h2-settings-personalization-lock-screen:

Lock screen
###########
.. todo::
  ``Show lock screen background picture on the sign-in screen`` should be set,
  no discovered options yet.

.. regedit:: Disable get fun facts, tips, tricks, and more on your lock
             screen
  :path:     HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
             ContentDeliveryManager
  :value0:   SubscribedContent-338387Enabled, {DWORD}, 0
  :update:   2021-02-19
  :open:

  Contacts Microsoft servers to get information to display.
