Windows Reinstall
-----------------
Common things to remember when reinstalling a Windows machine.

* Remove any existing junctions, otherwise copy with halt on them.
* Copy /Users/* to somewhere
* Copy /Programs/<wanted programs> somewhere
* Copy /Programs x86/<wanted programs> somewhere

### Dump existing registry, in case of missed values
```win + r > regedit```
 * Select Computer > right click > Export

### Gamesave Manager
 * Copy installed directory `/Program Files (x86)/GameSave Manager v3`
 * Copy db and custom save configs from `%appdata%/roaming/GameSave Manager 3`

### Putty
 * Export putty settings (or go through full registry dump)

```powershell
regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham
```

### WinSCP
 * Launch > Tools > Export configuration to file

```powershell
regedit /e "%userprofile%\Desktop\winscp.reg" "HKEY_CURRENT_USER\Software\Martin Prikryl\WinSCP 2"
```

### MusicBee
 * Copy any special files from installation directory to new (e.g. plugins, etc)
   `Program Files (x86)/MusicBee`
 * Copy configuration data from `%appdata%/roaming/musicbee`

### Mumble
 * Copy certificate database `%appdata%/roaming/Mumble`
 * Export client config

```powershell
regedit /e "%userprofile%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\Mumble\Mumble
```

### Claws-mail
 * Backup entire directory, includes config `Program Files (x86)/claws`

### Gaming
 * Origin, backup whole directory, includes saves `Program Files (x86)/Origin`
 * Uplay, backup whole directory, includes saves `Program Files (x86)/Ubisoft`
   * Cloud save are generally *not* backed up.
 * Steam, backup user data, includes save `Program Files (x86)/Steam/userdata`
