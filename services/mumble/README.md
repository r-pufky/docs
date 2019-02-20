Mumble Server
-------------
High quality VOIP server with pub cert auth and ACLs.

[Dedicated server setup](transmission-dedicated.md)

[Docker repository][1]

1. [Ports Exposed](#ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Server Setup](#server-setup)
1. [Modifying Settings](#modifying-settings)

Ports Exposed
-------------

| Port  | Protocol | Exposed/Public | Purpose      |
|-------|----------|----------------|--------------|
| 64738 | TCP      | Public         | Server/Voice |
| 64738 | UDP      | Public         | Voice        |

Important File Locations
------------------------

| File                                        | Purpose       |
|---------------------------------------------|---------------|
| /etc/mumble-server.ini                      | Configuration |
| /var/lib/mumble-server/mumble-server.sqlite | Server DB     |

Server Setup
------------

```bash
apt install mumble-server
```

/etc/mumble-server.ini
```bash
registerName=<SERVER_NAME>
registerPassword=<PASSWORD>
registerUrl=<SERVER_URL>
```
 * Register password cannot be changed. Don't lose your password.
 * SERVER_NAME appears in the public channel listing
 * SERVER_URL is a reference URL for the channel
 * See [example config](mumble-server.ini)

### Re-configure package and set `superuser` password.
```bash
dpkg-reconfigure mumble-server
systemctl start mumble-server
```

References
----------
[Mumble and Murmur server homepage][1]

[Setting superuser password][2]


[1]: http://mumble.sourceforge.net/
[2]: http://mumble.sourceforge.net/Running_Murmur#Setting_the_SuperUser_Password