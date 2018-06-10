Nzbget Server
-------------
Usenet downloader.

[Dedicated server setup](nzbget-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
2. [Important File Locations](#important-file-locations)
3. [Docker Creation](#docker-creation)
4. [SSH Tunneling](#ssh-tunneling)

[Docker Ports Exposed][2]
-------------------------

| Port | Protocol | Purpose                           |
|------|----------|-----------------------------------|
| 6789 | TCP      | Default nzbget webservice (http)  |
| 6791 | TCP      | Default nzbget webservice (https) |
 * If https is enabled, http is disabled

Important File Locations
------------------------
Relative to docker container

| File       | Purpose                         |
|------------|---------------------------------|
| /config    | Nzbget main service directory   |
| /downloads | Nzbget main downloads directory |

Docker Creation
---------------
You can copy your existing configuration to docker `/config` directory
adjusting for paths.

```bash
docker run -d \
  --name nzbget \
  --network host \
  --restart unless-stopped \
  -e UGID=1001 \
  -e PGID=1001 \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/nzbget:/config \
  -v /data/downloads:/downloads \
  linuxserver/nzbget:latest
```
 * The UID/GID should be set to a user/group that have access to your media.
 * Map your media directly to where it was before on the docker container to
   prevent needing to modify any libraries. This should be read-only.
 * See [nzbget.conf](nzbget.conf) for example configuration (adjust paths).

### Create OpenSSL certificates for https
This will creat self-signed certificates, you can use actual ones if you have
one.

```bash
apt install openssl
sudo openssl req -x509 -nodes -days 36500 -newkey rsa:4096 -keyout /data/services/nzbget/nzbget.key -out /data/services/nzbget/nzbget.crt
```

SSH Tunneling
-------------
If you don't want to expose any service ports, you can enable local only access
then tunnel with SSH.

### Only allow localhost access to webface

nzbget.conf
```
ControlIP=127.0.0.1
```

### Tunnel with SSH

```bash
ssh -L 6791:localhost:6791 <user>@<host>
```

[1]: https://hub.docker.com/r/linuxserver/nzbget/