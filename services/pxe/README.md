PXE Server
----------
PXE network boot server setup.

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [References](#references)

[Ports Exposed][1]
------------------

| Port | Protocol | Exposed/Public | Purpose                         |
|------|----------|----------------|---------------------------------|
| 69   | UDP      | Public         | Main service port for TFTP boot |

Important File Locations
------------------------

| File                   | Purpose                  |
|------------------------|--------------------------|
| /var/lib/tftpboot      | Directory hosting images |
| /etc/default/tftpd-hpa | Confguration             |

Server Setup
------------

```bash
apt install tftpd-hpa
```

Add server IP to configuration [example here](tftpd-hpa)

/etc/default/tftpd-hpa
```bash
TFTP_ADDRESS="<IP>:69"
```

### Router Configuration
Add TFTP server IP to DHCP options on router.

 * Enable network booting
 * Enter tftp server IP
 * Enter pxe image: `pxelinux.0`
 * Save and reload DHCP

[Script to automount ISO for booting](mount-tftp-image)

References
----------
[Ubuntu PXE server installation][1]

[Ubuntu PXE server howto][2]

[1]: https://help.ubuntu.com/community/PXEInstallServer
[2]: http://www.serenux.com/2010/05/howto-setup-your-own-pxe-boot-server-using-ubuntu-server/