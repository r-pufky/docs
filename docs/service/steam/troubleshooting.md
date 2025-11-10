# Troubleshooting

## Failed to determine free disk space for ... error 75
This happens when steamcmd cannot query the underlying data store remaining
quota. Common with ZFS backed data stores. Either set an explicit quota or
ignore it.

``` bash
sudo zfs set quota=2T zpool1/games
```

## 0x0 or disk write errors
No permissions to write updates to the data mount.

Explicitly set permissions for Conan Exiles files.
``` bash
chown -R conan:conan /data/server/ConanSandbox
```

## Wine Taking Long Time for First Start
**winehq** may potentially take ~5 minutes on first boot to launch, due to
blocking on boot events.

!!! danger "Error"
    0014:err:ole:get_local_server_stream Failed: 80004002
    __wine_kernel_init boot event wait timed out

This is a suspected issue with the GCC build toolchain, but has not been
resolved yet. Steam role should pre-mitigate this, however, system updates
could change that. Letting it run will resolve itself.

``` bash
wineboot --update
xvfb-run --autoservernum wineboot --update
```

Reference:

* https://bugs.winehq.org/show_bug.cgi?id=38653
* https://ubuntuforums.org/archive/index.php/t-1499348.html
