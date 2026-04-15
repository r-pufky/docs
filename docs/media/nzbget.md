# NZBGet
NZBGet Server.

!!! example "Migrated to ansible collection"
    Use [r_pufky.arr.nzbget][a].

!!! tip
    * The UID/GID should be set to a user/group that has access to your media.
      All media clients should run under the same user to run correctly.
    * Your downloader will report the download path **mapped in the downloader
      service**. You need to map this exact path in NZBGet for it to be able to
      post-process downloads properly.

## [NZB Import Process][d]
Store all folders on fast, local drives (avoid network shares for QueueDir or
InterDir).

1. NZBs added to NzbDir or API are picked up and queued.
2. Queue info is moved to QueueDir.
3. Articles are downloaded to the InterDir, then combined and verified (using
   PAR2 if needed).
4. RAR or 7z files are unpacked in the same directory (InterDir) after
   verification.
5. Once unpacking is complete, files are moved to DestDir — finished download
   location.
6. If enabled, scripts from ScriptDir run after completion (e.g. renaming,
   sorting, uploading).

## InterDir
Directory to store intermediate files.

Temporary working directory where all download processing, like repairs and
unpacking, takes place. After a job succeeds, the final files are moved to the
destination folder (DestDir), and the temporary files in InterDir are deleted.
DirectWrite uses this folder for post-processing.

Place InterDir on a fast disk (preferably SSD), and keep it separate from both
DestDir and the directory where Sonarr/Radarr transfers articles.

When you use a fast disk for InterDir, you eliminate disk writing
speed bottlenecks. By placing InterDir and DestDir on separate physical hard
drives, you also reduce disk wear.

Use local disk.

## Reverse Proxy
NZBGet should be run via a Reverse Proxy, allowing you to isolate and wrap
connections in SSL. [See NGINX][b] for more details.
[See Base Proxy Control][c] for basic proxy configuration.

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    server {
      listen                  443 ssl http2;
      server_name             nzbget.{DOMAIN} nzbget;

      location / {
        proxy_pass            http://nzbget:6791;
        include               /etc/nginx/conf.d/proxy-control.conf;
        proxy_set_header Host $host;
      }
    }
    ```

!!! abstract "/etc/nginx/conf.d/reverse_proxy.conf"
    0644 root:root

    ``` nginx
    server {
      location /nzbget/ {
        proxy_pass            https://nzbget:6791/;
        include               /etc/nginx/conf.d/proxy-control.conf;
        proxy_set_header Host $host;
      }
    }
    ```

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/arr/docs
[b]: ../service/nginx/README.md
[c]: ../service/nginx/manual/setup.md#setup-base-reverse-proxy
[d]: https://nzbget.com/documentation/nzbget-path-and-folder-structure-guide
