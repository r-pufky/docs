..  _service-wireguard-windows-setup:

Wireguard Windows Setup
#######################
Modern state-of-the-art VPN designed to be simplier and faster that IPsec and
openVPN.

:download:`Download latest Windows Installer <https://download.wireguard.com/windows-client>`.

Slient Install
**************
Wireguard may be installed silently via ``msiexec``.

.. code-block:: powershell
  :caption: Install wireguard and remove `default auto-start GUI`_ (powershell as admin).

  Start-Process msiexec.exe -ArgumentList '/q', '/I', 'wireguard-amd64-0.1.0.msi' -Wait -NoNewWindow -PassThru | Out-Null
  Start-Process 'C:\Program Files\WireGuard\wireguard.exe' -ArgumentList '/uninstallmanagerservice' -Wait -NoNewWindow -PassThru | Out-Null

Add Pre-configured Tunnel
*************************
Pre-configured tunnels may be added as a separate service.

.. code-block:: powershell
  :caption: Install ``my-tunnel.conf`` as a startup tunnel (powershell as admin).

  Start-Process 'C:\Program Files\WireGuard\wireguard.exe' -ArgumentList '/installtunnelservice', 'my-tunnel.conf' -Wait -NoNewWindow -PassThru | Out-Null
  Start-Process sc.exe -ArgumentList 'config', 'WireGuardTunnel$my-tunnel', 'start= delayed-auto' -Wait -NoNewWindow -PassThru | Out-Null
  Start-Service -Name WireGuardTunnel$my-tunnel -ErrorAction SilentlyContinue

.. note::
  The service is set to ``automatic (delayed)`` as this will `guarantee the
  service starting`_ if the network is not available when the service first
  starts. This mainly happens due to a very large hosts file or network being
  unavailable at boot.

.. _default auto-start GUI: https://superuser.com/questions/1026496/automatic-services-doesnt-start-automatically-after-windows-restart
.. _guarantee the service starting: https://superuser.com/questions/1026496/automatic-services-doesnt-start-automatically-after-windows-restart