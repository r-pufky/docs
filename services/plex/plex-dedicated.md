Plex Media Server
-----------------
Media streaming service.

1. [Ports Exposed](#ports-exposed)
2. [Important File Locations](#important-file-locations)
3. [Server Setup](#server-setup)
4. [Legacy Plex Fixes](#legacy-plex-fixes)

[Ports Exposed][1]
------------------

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

Important File Locations
------------------------

| File                     | Purpose                   |
|--------------------------|---------------------------|
| /var/lib/plexmediaserver | Plex media server library |

Server Setup
------------
Setup the [plex repository][2] and install. If using PlexPass, you must sign in
and manually download the install package.

/etc/apt/sources.list.d/plexmediaserver.list
```bash
deb https://downloads.plex.tv/repo/deb ./public main
```

Add apt repository key and install
```bash
curl https://downloads.plex.tv/plex-keys/PlexSign.key | sudo apt-key add -
apt update && apt install plexmediaserver
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
 * Setup /tmp to use at most 4G of RAM for storage (note: tmpfs only allocates
   space from actual items stored).

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

Legacy Plex Fixes
-----------------

### [Backup state configuration][4]

```bash
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
echo ".dump metadata_item_settings" | sudo sqlite3 com.plexapp.plugins.library.db | grep -v TABLE | grep -v INDEX > viewstate-information-settings.sql
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
sudo cp -av Media /tmp/media-backup
sudo cp -av Metadata /tmp/metadata-backup
```
 * This exports the viewstate

### Restoring Plex State Configuration

```bash
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugin\ Support/Databases
cat viewstate-information-settings.sql | sudo sqlite3 com.plexapp.plugins.library.db
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server
sudo cp -av /tmp/media-backup Media
sudo cp -av /tmp/metadata-backup Metadata
```

### Plex Stuck at Initial Startup

```bash
sudo service plexmediaserver stop
sudo ps -ef | grep -i plex
sudo kill -9 <any remaining PID’s>
cd /var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/Plugins
rm -f Service.bundle Framwork.bundle
sudo service plexmediaserver start
sudo reboot
```

[1]: https://support.plex.tv/articles/201543147-what-network-ports-do-i-need-to-allow-through-my-firewall/
[2]: https://support.plex.tv/articles/235974187-enable-repository-updating-for-supported-linux-server-distributions/
[3]: https://support.plex.tv/articles/206225077-how-to-use-secure-server-connections/
[4]: https://plexapp.zendesk.com/hc/en-us/articles/201154527-Move-Viewstate-Ratings-from-One-Install-to-Another