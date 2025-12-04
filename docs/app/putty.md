# Putty


## Enable Keepalives

!!! example "putty ➔ connection ➔ enable tcp keepalives"
!!! example "putty ➔ connection ➔ seconds between keepalives ➔ 5"


## Export Settings
``` powershell
regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham
```


## Launch Putty with [Specific Profile][a]
``` powershell
putty.exe -load "{SESSION}"  # Use from CLI or add to Windows shortcut.
```


## [Changing Escape Characters][b]
Sometimes the terminal escape sequences that are sent are changed if you are
running through multiple screen sessions.

``` bash
stty -a  # Determine the current escape sequences.

# Determine the actual control sequence sent.
ctrl + v,  # {DESIRED KEY PRESS}. Prints sequence to terminal.

# Set the correct escape sequence.
stty erase ^H
```


## Forwarding X Windows
Use [VcXsrv][c] instead of xming. This is fully functional and does not have
copy/paste or resizing disabled. Install as normal.

!!! abstract "c:\Program Files\VcXsrv\config.xlaunch"
    ``` xml
    <?xml version="1.0" encoding="UTF-8"?>
    <XLaunch WindowMode="MultiWindow" ClientMode="NoClient" LocalClient="False" Display="-1" LocalProgram="xcalc" RemoteProgram="xterm" RemotePassword="" PrivateKey="" RemoteHost="" RemoteUser="" XDMCPHost="" XDMCPBroadcast="False" XDMCPIndirect="False" Clipboard="True" ClipboardPrimary="True" ExtraParams="" Wgl="True" DisableAC="False" XDMCPTerminate="False"/>
    ```

Set xlaunch shortcut to use config.
``` powershell
"c:\Program Files\VcXsrv\xlaunch.exe" -run config.xlaunch
```

[a]: http://superuser.com/questions/248099/a-putty-shortcut-that-automatically-launches-a-profile
[b]: https://unix.stackexchange.com/questions/43103/backspace-tab-not-working-in-terminal-using-ssh
[c]: https://sourceforge.net/projects/vcxsrv/files/vcxsrv
