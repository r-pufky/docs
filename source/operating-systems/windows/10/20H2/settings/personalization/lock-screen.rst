.. _w10-20h2-settings-personalization-lock-screen:

Lock screen
###########
.. dropdown:: Disable get fun facts, tips, tricks, and more on your lock screen
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in
  :open:

  Contacts Microsoft servers to get information to display.

  .. dropdown:: :term:`Registry`
    :title: font-weight-bold
    :animate: fade-in
    :open:

    .. wregedit:: Disable get fun facts, tips, tricks, and more on your lock
                  screen
      :key_title: HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\
                  ContentDeliveryManager
      :names:     SubscribedContent-338387Enabled
      :types:     DWORD
      :data:      0
      :no_section:
      :no_caption:

.. TODO::
  ``Show lock screen background picture on the sign-in screen`` should be set,
  no discovered options yet.
