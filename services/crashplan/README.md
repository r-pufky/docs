Crashplan Pro
-------------
Crashplan Pro (For Small Business) is now the only 'consumer' level option for
crashplan.

[Dedicated server setup](crashplan-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
2. [Important File Locations](#important-file-locations)
3. [Docker Creation](#docker-creation)
4. [Initial Setup](#initial-setup)
5. [Taking over existing backups](#taking-over-existing-backups)

Docker Ports Exposed
--------------------

| Port | Protocol | Purpose           |
|------|----------|-------------------|
| 5800 | TCP      | GUI web interface |
| 5900 | TCP      | GUI via VNC       |

Important File Locations
------------------------
Relative to docker container

| File        | Purpose                         |
|-------------|---------------------------------|
| /config/var | Crashplan identity certs        |
| /storage    | Default map for backup location |

Docker Creation
---------------
If first-run, just launch the docker container to generate the correct
configuration directory structure, afterwards you can stop and inject your
current certificates into the configuration directory.

```bash
docker run -t -d \
  --name=crashplan \
  --net=host \
  --restart=unless-stopped \
  -p 5800:5800 \
  -e USER_ID=0 \
  -e GROUP_ID=0 \
  -e KEEP_APP_RUNNING=1 \
  -e SECURE_CONNECTION=1 \
  -e TZ=America/Los_Angeles \
  -v /etc/localtime:/etc/localtime:ro \
  -v /data/services/crashplan:/config:rw \
  -v /data:/storage:ro \
  -v /:/root-mount:ro \
  jlesage/crashplan-pro:latest
```
 * Crashplan should run as root to be able to read/backup all files
 * `/storage` is the default location; however, you can mount any directory as
   long as it doesn't overwrite docker image directories. `/data` is free to use
 * `/` is mapped to `/root-mount` to enable backup of any files on `/` for the
   host that also exist in the docker image.
 * Map your backup drives as *read only*.
 * Use should use [`-t -d`][3] is needed to keep the container in interactive
   mode otherwise as soon as the container is idle it will sleep, which will
   stop background running services.


```bash
docker stop crashplan
```

Initial Setup
-------------

## Add existing certs
If you have a current crashplan installation, you can copy your crashplan
identity to `/config/var`.

/config/var
```
.identity
service.pem
.ui_info
```

## Bump inotify limits
Increase [inotify max watch limits][2] on host so crashplan can watch monitored
files.

/etc/sysctl.conf
```bash
fs.inotify.max_user_watches=1048576
```

Then reload `sysctl` or `reboot`.
```bash
sysctl -p /etc/sysctl.conf
```

Then restart crashplan
```bash
docker start crashplan
```

Taking over existing backups
----------------------------
Read [docker container documentation here][3].

Backup tasks will need to migrated if the locations have changed due to running
in a docker container (these are usually `/` based backups like `/etc`).

If identity was imported then no adoption of a backup set is needed.

[1]: https://github.com/jlesage/docker-crashplan-pro
[2]: https://support.code42.com/CrashPlan/4/Troubleshooting/Linux_real-time_file_watching_errors
[3]: https://github.com/jlesage/docker-crashplan-pro#taking-over-existing-backup