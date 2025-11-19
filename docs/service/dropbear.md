# Dropbear
Remote unlock encrypted root filesystems over SSH on boot.

!!! example "Migrated to ansible collection"
    Use [r_pufky.deb.dropbear][a].

!!! warning
    Most systems do not encrypt **/boot** and therefore dropbear keys should be
    considered compromised/untrusted; use separate keys when using dropbear!

!!! tip
    * Dropbear host identification keys are a special format, not a standard
      SSH keypair.
    * Dropbear host keys are binary files and cannot be stored encrypted in the
      {host,group}_vars directory. Ansible will try to automatically decrypt
      this file and fail due to UTF-8 encoding issues. Storing within ansible
      but outside of {host,group}_vars to prevent decryption until the binary
      file is copied, wherein the decryption happens correctly.
    * Remote Unlock using the dropbear key **ssh -i ~/.ssh/dropbear
      root@remote_host**.

See [Wireguard][b] to enable wireguard service on boot for fully encrypted
remote boot root FS unlock.

## Reference[^1]

[^1]: https://linuxconfig.org/how-to-install-and-configure-dropbear-on-linux

[a]: https://galaxy.ansible.com/ui/repo/published/r_pufky/deb/docs
[b]: wireguard/README.md
