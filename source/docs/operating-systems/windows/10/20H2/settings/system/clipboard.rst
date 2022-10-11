.. _w10-20h2-settings-system-clipboard:

Clipboard
#########

Clipboard history
*****************
.. dropdown:: Disable save multiple items to the clipboard to use later. Press
              the Windows Logo Key + V to view your clipboard history and paste
              from it.
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Long term multi-item storage of clipboard will likely contain passwords or
  confidential material.

  .. gpo::    Disable save multiple items to the clipboard to use later.
              Press the Windows Logo Key + V to view your clipboard history
              and paste from it.
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Allow Clipboard History
    :value0:  ☑, {DISABLED}
    :ref:     https://www.top-password.com/blog/disable-clipboard-history-in-windows-10/#:~:text=Method%202%3A%20Disable%20Clipboard%20History,OK%20and%20reboot%20your%20computer.
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable save multiple items to the clipboard to use later.
               Press the Windows Logo Key + V to view your clipboard history
               and paste from it.
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
    :value0:   AllowClipboardHistory, {DWORD}, 0
    :ref:      https://www.top-password.com/blog/disable-clipboard-history-in-windows-10/#:~:text=Method%202%3A%20Disable%20Clipboard%20History,OK%20and%20reboot%20your%20computer.
    :update:   2021-02-19
    :generic:
    :open:


Sync across devices
*******************
.. dropdown:: Disable paste text on your other devices when you sign in with a
              Microsoft account or work account.
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :animate: fade-in

  Sync of clipboard data will likely contain passwords or confidential material,
  and should **not** be transmitted to MS services even if encrypted.

  .. gpo::    Disable paste text on your other devices when you sign in with a
              Microsoft account or work account.
              and paste from it.
    :path:    Computer Configuration -->
              Administrative Templates -->
              System -->
              OS Policies -->
              Allow Clipboard syncronization across devices
    :value0:  ☑, {DISABLED}
    :ref:     https://www.tenforums.com/tutorials/110048-enable-disable-clipboard-sync-across-devices-windows-10-a.html
    :update:  2021-02-19
    :generic:
    :open:

  .. regedit:: Disable paste text on your other devices when you sign in with a
               Microsoft account or work account.
    :path:     HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System
    :value0:   AllowCrossDeviceClipboard, {DWORD}, 0
    :ref:      https://www.tenforums.com/tutorials/110048-enable-disable-clipboard-sync-across-devices-windows-10-a.html
    :update:   2021-02-19
    :generic:
    :open:
