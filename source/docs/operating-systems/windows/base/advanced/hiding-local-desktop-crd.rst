.. _wbase-specific-windows-fixes-hiding-local-desktop-crd:

Hiding Local Desktop for Chrome Remote Desktop
##############################################
By default Chrome Remote Desktop will always show locally what is happening when
you remotely connect. This disables this feature and presents a login screen
instead, allowing you to work privately remotely. CRD will open a connection,
then locally connect to remote desktop to hide your current session.

Installing CRD (Chrome Remote Desktop):

* Sign in to Chrome.
* Disable all sync'ing with account (if wanted).
* Install the Remote Desktop Extension.
* Launch the installer.

:cmdmenu:`share (green button) --> accept and install --> run msi installer`

* On Authorize screen click :cmdmenu:`continue`

:cmdmenu:`CRD --> my computers --> enable remote connections`

* Create a PIN for connection.
* ☐ Improve CRD.

.. regedit:: Enable remote access curtain for CRD regedit
  :path:     HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome
  :value0:   RemoteAccessHostRequireCurtain, {DWORD}, 1
  :ref:      https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
  :update:   2021-02-19

.. regedit:: Enable RDP security regedit
  :path:     HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\
             Terminal Server\WinStations\RDP-Tcp
  :value0:   SecurityLayer, {DWORD}, 1
  :ref:      https://support.google.com/chrome/a/answer/2799701?hl=en&vid=0-243350879834-1495198101821
  :update:   2021-02-19

:cmdmenu:`⌘ + r --> control --> System and Security --> System --> Remote Settings --> Remote`

* ☑ Allow remote connections to this computer.
* ☐ Allow connections only from computers running Remote Desktop with Network
  Level Authentication.

.. gui::   Block inbound rdp connections firewall
  :label:  Firewall
  :nav:    ⌘ -->Control Panel --> System and Security --> Windows Defender Firewall
  :path:   Advanced Settings --> Inbound Rules
  :value0:    Remote Desktop - Shadow (TCP-in), {BLOCK}
  :value1: Remote Desktop - User Mode (TCP-in), {BLOCK}
  :value2: Remote Desktop - User Mode (UDP-in), {BLOCK}
  :ref:    https://superuser.com/questions/723832/windows-firewall-blocks-remote-desktop-with-custom-port
  :update: 2021-02-19

`Reference <https://remotedesktop.google.com/access>`__
