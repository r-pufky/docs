Windows Setup
---------------------
Standard Windows setup used for gaming. Removes known tracking.

Windows 10 pro

Execution Policy: **Unrestricted** (See: Setting Execution Policy)

Assumes Admin Rights

[Setting Execution Policy][8]
--------------------------
Powershell scripts require unrestricted exectuion policy to be set to
execute. By default this is **disabled** and is the **correct choice**.
Once you've executed scripts, you **must** manually reset this to restricted
or you leave yourself open to bad things. This persists across sessions.

### Check and set unrestricted policy (powershell as admin)
```powershell
get-executionpolicy
set-executionpolicy unrestricted
Y
```

### Set restricted policy (powershell as admin)
```powershell
set-executionpolicy restricted
Y
```

Removing pre-installed [Windows packages][6]
---------------------------------------
Certain packages (and windows store applications) cannot be removed with
[programs & applications][7]. This removes those applications using Windows
built-in package manager.
* _Remove-AppxProvisionedPackage_ will remove packages for newly provisioned
  accounts
* _Remove-AppxPackage_ removes for the current user
* _Get-AppxPackage -AllUsers_ will return results for all users on system

### Remove packages with [remove-crapware.ps1](remove-crapware.ps1) (powershell as admin)
```powershell
remove-crapware.ps1
```

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

Force upgrade licenses to Windows 10
------------------------------------
This will force your system to [check in for Windows 10 eligibility][4], instead
of randomly waiting up to a month.

### [force-upgrade-to-10.cmd](force-upgrade-to-10.cmd) (cmd as admin)
```cmd
force-upgrade-to-10.cmd
```

### Upgrade
* Ensure latest Windows updates are applied, system rebooted
* Run [force-upgrade-to-10.cmd][3] as admin, this will force upgrade checks
* Once the upgrade is verified, you must upgrade via upgrade utility to transfer license
  * Once the upgrade finishes, the license is tied to the hardware

```start > settings > update & security > activation```
* Verify activation status
* Grab the windows key with the [ShowKeyPlus][5]

### Forcing Activation Checks (cmd as admin)
```cmd
slmgr.vbs /ato
```

[1]: http://winaero.com/blog/how-to-format-any-drive-in-windows-8-1-with-refs/
[2]: http://blog.architecting.it/2012/07/10/windows-server-2012-windows-server-8-resilient-file-system/w8-refs-2/
[3]: https://github.com/r-pufky/docs/blob/master/force-upgrade-to-10.cmd
[4]: http://www.tenforums.com/tutorials/5705-activate-windows-10-a.html
[5]: http://www.tenforums.com/tutorials/7745-product-key-view-windows-10-a.html
[6]: https://thomas.vanhoutte.be/miniblog/delete-windows-10-apps/
[7]: http://www.makeuseof.com/tag/3-clever-powershell-functions-upgrading-windows-10/
[8]: http://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system
