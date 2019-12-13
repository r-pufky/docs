..  _service-ssh-windows-setup:

`SSHD Windows Setup`_
**********************
Windows 10 has a beta which allows for ``sshd`` and ``ssh-agent`` use to access
the windows system. This covers the manual installation process, there is also a
beta you may install via optional features.

:download:`Download OpenSSH Binaries <https://github.com/PowerShell/Win32-OpenSSH/releases>`
and extract to ``C:\Program Files\``.

.. code-block:: powershell
  :caption: Install OpenSSH, generate host keys, set file permissions, and open
            firewall port 22 (powershell as admin).

  cd C:\Program Files\OpenSSH
  powershell.exe -ExecutionPolicy Bypass -File install-sshd.ps1
  ./ssh-keygen.exe -A
  powershell.exe -ExecutionPolicy Bypass -File ./FixHostFilePermissions.ps1
  New-NetFirewallRule -Protocol TCP -LocalPort 22 -Direction Inbound -Action Allow -DisplayName SSH

.. wservice:: Enable sshd service
  :key_title: SSHD --> General
  :option:    Startup type,
              Service status
  :setting:   Automatic,
              Started
  :no_section:

Set up publickey authentication:

* Create ``C:\Users\{USER}\.ssh``.

.. code-block:: powershell
  :caption: Grant SSHD service read permissions to ``.ssh`` directory.

  icacls C:\users\{USER}\.ssh /grant "NT Service\sshd:R" /T

.. _SSHD Windows Setup: https://winscp.net/eng/docs/guide_windows_openssh_server