..  _service-ssh-windows-service:

Windows Service
###############
Windows 10 has a beta which allows for ``sshd`` and ``ssh-agent`` use to access
the windows system. This covers the manual installation process, there is also a
beta you may install via optional features.

:download:`Download OpenSSH Binaries <https://github.com/PowerShell/Win32-OpenSSH/releases>`
and extract to ``c:\Program Files\``.

.. code-block:: powershell
  :caption: Install OpenSSH, generate host keys, set file permissions, and open
            firewall port 22 (powershell as admin).

  cd c:\Program Files\OpenSSH
  powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
  ./ssh-keygen.exe -A
  powershell.exe -ExecutionPolicy Bypass -File ./FixHostFilePermissions.ps1
  New-NetFirewallRule -Protocol TCP -LocalPort 22 -Direction Inbound -Action Allow -DisplayName SSH

.. gui::   Enable sshd service
  :label:  Service
  :nav:    ⌘ --> services.msc
  :path:   SSHD --> General
  :value0:   Service name, sshd
  :value1:   Startup type, {AUTOMATIC}
  :value2: Service status, {STARTED}
  :update: 2021-02-19

Set up publickey authentication:

* Create ``c:\Users\{USER}\.ssh``.

.. code-block:: powershell
  :caption: Grant SSHD service read permissions to ``.ssh`` directory.

  icacls c:\users\{USER}\.ssh /grant "NT Service\sshd:R" /T

`Reference <https://winscp.net/eng/docs/guide_windows_openssh_server>`__