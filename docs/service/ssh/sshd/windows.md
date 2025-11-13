# Windows


## Enable SSHD

!!! example "⌘ + r ➔ ms-settings:optionalfeatures ➔ OpenSSH ➔ Install"

!!! example "⌘ ➔ services.msc ➔ OpenSSH SSH Server"
    * Startup type: **{AUTOMATIC}**

Allow SSH through Windows Firewall
``` powershell
# Run as administrator.
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
```

### [Set up publickey authentication][a]

Grant SSHD service read permissions to **.ssh** directory.
``` powershell
mkdir c:\Users\{USER}\.ssh

icacls c:\users\{USER}\.ssh /grant "NT Service\sshd:R" /T
```

[a]: https://winscp.net/eng/docs/guide_windows_openssh_server
