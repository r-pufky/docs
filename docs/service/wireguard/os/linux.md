# Linux
All modern linux distributions support wireguard with 5.6+ Kernels.

=== "Manjaro"
    ``` bash
    pamac install wireguard-dkms wireguard-tools wireguard-ui
    ```

=== "Debian"
    ``` bash
    apt install wireguard
    ```
=== "Ubuntu"
    ``` bash
    apt install wireguard
    ```


## [Autostart Tunnel as Service][a]
  :caption: Start tunnel on boot.
``` bash
systemctl enable wg-quick@{TUNNEL}

# Start tunnel on demand.
systemctl status/stop/start/restart wg-quick@{TUNNEL}
```

[a]: https://community.hetzner.com/tutorials/install-and-configure-wireguard-vpn-debian
