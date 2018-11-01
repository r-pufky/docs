Playon Dedicated Recorder
-------------------------
Uses [Windows 10 base Xen template](README.md#windows-10), and assumes
post template setup scripts have been run.

* Memory: 8GB
* Disk: 60GB

1. [Ports Exposed](#ports-exposed)
1. [Services Used](#services-used)
1. [Server Setup](#server-setup)
1. [References](#references)

Ports Exposed
-------------
| Port        | Protocol |Purpose                              |
|-------------|----------|-------------------------------------|
| 22          | TCP      | SSHD for sshfs connections          |
| 57331*      | TCP/UDP  | For streaming to other playon apps  |
* Only if you use playon to stream recordings / provide a media library, by
  default this can be safetly disabled.

Services Used
-------------
| Service       | Purpose                                                              |
|---------------|----------------------------------------------------------------------|
| SSH           | SSHFS remote file access for copying videos                          |
| CRD           | Chrome Remote Desktop for remote login                               |
| RDC           | Remote desktop (localhost connection only) for Chrome Remote Desktop |
| Flash         | Adobe flash used for recording via playon                            |
| Playon Server | mediamallserver.exe Server used to manage recordings and accounts    |

Server Setup
------------
* Setup [Chrome Remote Desktop][1]
* Setup [SSH][2] with only public key authentication

### Install Playon

* Ensure you are connected via the VM console (not CRD) for install, otherwise
  installer will fail.
* Install [Playon Desktop][3], but do not launch immediately
* Connect via CRD
* Launch Playon, skip through helper setup screens
* Open settings (lower left gear); all tabs not mentioned are disabled / unused

Video Performance Tab
```
Quality > HD
Check > Allow resumable playback
Advanced options > H.264 Recording Profile > High
```

System Check Tab
```
Check > Notify Automatically
```

Channels Tab
* Disable all channels not used
* Login to channels

References
----------
[Playon Minimum requirements][5]
[Playon User Guide][6]


[1]: https://github.com/r-pufky/docs/blob/master/windows-gaming.md#hiding-local-desktop-for-chrome-remote-desktop
[2]: https://github.com/r-pufky/docs/blob/master/windows-gaming.md#enabling-ssh-access
[3]: https://www.playon.tv/getplayon
[4]: https://forums.webosnation.com/webos-apps-games/297294-port-forwarding-playon.html
[5]: https://www.playon.tv/support/minreqs#minreq-details
[6]: https://www.playon.tv/user-guide/intro