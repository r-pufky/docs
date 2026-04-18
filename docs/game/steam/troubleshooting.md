# Troubleshooting

## Please confirm your network connection and try again.
Steam uses **client-download.steampowered.com** to detect internet connectivity
through **public/steambootstrapper_english.txt**. DNS updates or failure to
resolve those DNS names will cause Steam to fail.

!!! danger ""
    ILocalize::AddFile() failed to load file "public/steambootstrapper_english.txt".
    [  0%] Checking for available update...
    KeyValues Error: LoadFromBuffer: missing {   (current key: '<!doctype') in file manifest [offset: 20]

    ../tier1/KeyValues.cpp (2925) : Assertion Failed: Error while parsing text KeyValues for resource manifest
    [----] Verifying installation...
    [  0%] Downloading Update...
    [  0%] Checking for available update...
    KeyValues Error: LoadFromBuffer: missing {   (current key: '<!doctype') in file manifest [offset: 20]

    ../tier1/KeyValues.cpp (2925) : Assertion Failed: Error while parsing text KeyValues for resource manifest
    [----] !!! Fatal Error: Steamcmd needs to be online to update.	 Please confirm your network connection and try again.
    threadtools.cpp (3294) : Assertion Failed: Illegal termination of worker thread 'Thread(0x0x670f5380/0x0xf051db'

### Statically map DNS name
Allows for immediate use of Steam but will break when IP's change. Set, run
Steam commands, then unset.

``` bash
# Resolve first usable IP address for media.steampowered.com.
dig +short media.steampowered.com | grep -m 1 '^[0-9.]*$'
dig +short media.steampowered.com | grep -E -o '([0-9]{1,3}\.){3}[0-9]{1,3}'
> 23.214.22.163
```

!!! abstract "/etc/hosts"
    0644 {USER}{USER}

    ``` bash
    # Always remove after running steamcmd!
    23.214.22.163  client-download.steampowered.com
    ```

### Wait for propagation
Alternatively waiting for DNS propagation will resolve this issue, but may take
up to 72 hours for global propagation.

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

## [Wine Taking Long Time for First Start][a]
**winehq** may potentially take ~5 minutes on first boot to launch, due to
blocking on boot events.

!!! danger ""
    0014:err:ole:get_local_server_stream Failed: 80004002
    __wine_kernel_init boot event wait timed out

This is a suspected issue with the [GCC build toolchain][b], but has not been
resolved yet. Steam role should pre-mitigate this, however, system updates
could change that. Letting it run will resolve itself.

``` bash
wineboot --update
xvfb-run --autoservernum wineboot --update
```

[a]: https://bugs.winehq.org/show_bug.cgi?id=38653
[b]: https://ubuntuforums.org/archive/index.php/t-1499348.html
