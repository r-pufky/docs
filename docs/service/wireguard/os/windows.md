# Windows

## Setup
Download latest [Windows Installer](https://download.wireguard.com/windows-client).

``` powershell
# Install
winget install --id=WireGuard.WireGuard -e

# Silent install
Start-Process msiexec.exe -ArgumentList '/q', '/I', 'wireguard-amd64-0.1.0.msi' -Wait -NoNewWindow -PassThru | Out-Null
Start-Process 'C:\Program Files\WireGuard\wireguard.exe' -ArgumentList '/uninstallmanagerservice' -Wait -NoNewWindow -PassThru | Out-Null
```

Reference:

* https://superuser.com/questions/1026496/automatic-services-doesnt-start-automatically-after-windows-restart

## Add Pre-configured Tunnel
Pre-configured tunnels may be added as a separate service.

The service is set to **automatic (delayed)** as this will guarantee the
service starting if the network is not available when the service first starts.
This mainly happens due to a very large hosts file or network being unavailable
at boot.

``` powershell
# Install my-tunnel.conf as a startup tunnel (powershell as admin).

Start-Process 'C:\Program Files\WireGuard\wireguard.exe' -ArgumentList '/installtunnelservice', 'my-tunnel.conf' -Wait -NoNewWindow -PassThru | Out-Null
Start-Process sc.exe -ArgumentList 'config', 'WireGuardTunnel$my-tunnel', 'start= delayed-auto' -Wait -NoNewWindow -PassThru | Out-Null
Start-Service -Name WireGuardTunnel$my-tunnel -ErrorAction SilentlyContinue
```

Reference:

* https://superuser.com/questions/1026496/automatic-services-doesnt-start-automatically-after-windows-restart