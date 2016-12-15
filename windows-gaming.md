Windows Setup
---------------------
Standard Windows setup used for gaming. Removes known tracking.

Windows 10 pro. Assumes admin rights.


Format ReFS on using a [single drive][1]
----------------------------------------
ReFS allows for integrated file checksums, duplication and error recovery,
however by default it requires two disks. This will allow you to use this
filesystem on a single disk.

### Edit Windows Registry (regedit as admin)
> Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control

> New **Key**: MiniNT

> New **DWORD**: AllowRefsFormatOverNonmirrorVolume = 1

* Reboot

### Setup disk for ReFS (powershell as admin)
```powershell
diskpart
list disk
select disk [#]
clean
create partition primary
format fs=refs quick
```

### Mount disk and format with integrity enabled
```win + x > computer management > disk utilities```
* Mount ReFS partition to a drive letter
* Reformat drive with [integrity enabled][2]

```format X: /fs:refs /i:enabled /q```

### Verifiy ReFS with Integrity is working (powershell as admin)
* Write a temporary file the drive and use this to lookup on the filesystem.

```Get-Item X:\<file> | Get-FileIntegrity```
* Enabled and Enforced should be set to True

[1]: http://winaero.com/blog/how-to-format-any-drive-in-windows-8-1-with-refs/
[2]: http://blog.architecting.it/2012/07/10/windows-server-2012-windows-server-8-resilient-file-system/w8-refs-2/
