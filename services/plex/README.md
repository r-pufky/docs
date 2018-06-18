Plex Media Server
-----------------
Media streaming service.

All media clients should run under the same user to run correctly.

[Dedicated server setup / service notes](plex-dedicated.md)

[Docker repository][1]

1. [Docker Ports Exposed](#docker-ports-exposed)
1. [Important File Locations](#important-file-locations)
1. [Docker Creation](#docker-creation)
1. [Fixing Playback Issues](#fixing-playback-issues)

[Docker Ports Exposed][2]
-------------------------

| Port  | Protocol | Purpose                                                 |
|-------|----------|---------------------------------------------------------|
| 32400 | TCP      | Plex Media Server Access                                |
| 1900  | UDP      | (Optional) Plex DLNA Server                             |
| 3005  | TCP      | (Optional) Control Plex Home Theater via Plex Companion |
| 5353  | UDP      | (Optional) Bonjour/Avahi discovery                      |
| 8324  | TCP      | (Optional) Control Plex for Roku via Plex Companion     |
| 32410 | UDP      | (Optional) GDM network discovery                        |
| 32412 | UDP      | (Optional)  GDM network discovery                       |
| 32413 | UDP      | (Optional) GDM network discovery                        |
| 32414 | UDP      | (Optional) GDM network discovery                        |
| 32469 | TCP      | (Optional) Plex DLNA Server                             |
 * Using host networking will expose all of these ports. It may be better to
   specify just `32400`.

Important File Locations
------------------------
Relative to docker container

| File    | Purpose                   |
|---------|---------------------------|
| /config | Plex media server library |

Docker Creation
---------------
You can copy your existing library from `/var/lib/plexmediaserver/*` to docker
`/config` directory to auto-import your existing plex library.

```bash
docker run -t -d \
  --name plex \
  --network host \
  --restart unless-stopped \
  -e PLEX_UID=1001 \
  -e PLEX_GID=1001 \
  -e PLEX_CLAIM="<claimToken>" \
  -e TZ=America/Los_Angeles \
  -e /etc/localtime:/etc/localtime:ro \
  -v /data/services/plexmediaserver:/config \
  -v /data/media:/data/media:ro \
  -v /tmp:/transcode \
  -v /tmp/Transcode/tmp:/tmp \
  plexinc/pms-docker:plexpass
```
 * The UID/GID should be set to a user/group that have access to your media.
 * Map your media directly to where it was before on the docker container to
   prevent needing to modify any libraries. This should be read-only.
 * `/transcode` needs to be mapped to a **fast** drive. See
   [setup /transcode with tempfs](#setup-transcode-with-tempfs) to run
   transcoding in memory.
 * We additionally map the plex `/tmp` directory to a subdirectory for the
   transcoding directory. Plex updated the transcoding to split video encoding
   to `/transcode` while the audio encoding is transcoded in `/tmp`. This causes
   the `EAE timeout! EAE not running, or wrong folder? Could not read` Error.
   Moving /tmp fixes this.
 * PLEX_CLAIM token is used to identify the server for your account. This is
   only used on initial startup without a pre-existing config. Generate a token
   here: https://www.plex.tv/claim
 * Use should use [`-t -d`][3] is needed to keep the container in interactive
   mode otherwise as soon as the container is idle it will sleep, which will
   stop background running services.

```bash
docker stop plex
```

### Setup /transcode with tmpfs
Transcoding is disk intensive and requires a fast (SSD or better) drive to make
latencies transparent. This will setup /tmp with tmpfs (running in memory) to
do transcoding in RAM, which will make playback and seeks nearly instantanenous.

On the docker host:

/etc/fstab
```bash
tmpfs  /tmp  tmpfs  defaults,size=4G  0  0
```
 * Setup /tmp to use at most 4G of RAM for storage (tmpfs only allocates space
   from actual items stored).
 * Note: Ensure that **/transcode** is set on the plex server to properly map to
   the docker host /tmp directory.

Reboot to enable.

### Enable secure server connection

 * Ensure `32400` is forwarded to the router
 * Enable [DNS Rebinding][3] on router

### Initial setup
If not using a plex claim token or manual port forwarding you may need to setup
plex manually from the machine. Setup a SSH port forward

```bash
ssh -L 32400:<Server IP>:32400 -N <user>@<host>
```

Then nagivate to `http://localhost:32400/web` to finish setup.

```bash
docker start plex
```

Fixing Playback Issues
----------------------
### Playback Fails / App Crashes
Generally this happens when you are playing media on Plex Home Theater or Plex
app, where `transcoding` is being used. The app will crash generally with a
message of `Conversation failed. Transcoder crashed or failed to start up`. This
usuall happens because the transcoder was not able to write to the transcoding
directory.

 * Ensure `Transcoding` directory is setup properly on Plex Server.
 * Ensure `/tmp/Transcode` is owned by the right user. Changing the running user
   on docker without re-creating this directory will cause this to happen.

### [Spinning playback icon, no playback][5]
Generally if `transcoding` is setup right, then this is related to the `audio
transcoding` failing. Turn on `debug logging` on the server and look for the
`EAE timeout! EAE not running, or wrong folder? Could not read` error. This
means you need to remap the docker `/tmp` directory to your transcoding
directory, as plex updated transcoding and split out audio and video encoding
into separate locations. Video transcodes in `/transcode` while audio transcodes
in `/tmp`. Mapping `/tmp` in docker to the transcoding directory fixes this.

```docker
-v /tmp/Transcode/tmp:/tmp
```

[1]: https://hub.docker.com/r/plexinc/pms-docker/
[2]: https://support.plex.tv/articles/201543147-what-network-ports-do-i-need-to-allow-through-my-firewall/
[3]: https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections/
[4]: https://www.cb-net.co.uk/linux/running-plex-from-a-docker-container-on-ubuntu-16-04-lts-16-10/
[5]: https://forums.plex.tv/discussion/265492/transcoder-fails-when-transcode-is-on-a-network-share/p4