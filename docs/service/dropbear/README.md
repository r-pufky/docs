# Dropbear
Remote unlock encrypted root filesystems over SSH on boot.

!!! example "Migrated to ansible collection"
    Use [r_pufky.deb.dropbear][a].

!!! warning
    Most systems do not encrypt **/boot** and therefore dropbear keys should be
    considered compromised/untrusted; use separate keys when using dropbear!

See [Wireguard][b] to enable wireguard service on boot for fully encrypted
remote boot root FS unlock.


## Reference[^1]

[^1]: https://linuxconfig.org/how-to-install-and-configure-dropbear-on-linux

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/deb/docs
[b]: ../wireguard/README.md
