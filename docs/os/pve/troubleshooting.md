# Troubleshooting


## Ascii codec can't decode byte 0xe2 in position
See [Failed to run vncproxy](#failed-to-run-vncproxy).


## [Failed to run vncproxy][a]
SSH vncproxy proxy tunnel between pve nodes are not auto-accepted.

VM consoles can be access on each local cluster node, but not on remote cluster
nodes. May be confirmed by manually ssh'ing to other nodes and confirming that
the *connection is denied* or the *host key has changed*. Frequently happens
when node host keys are regenerated.

Resolve by clearing root and host **known_hosts** and syncing pve certificates.

``` bash
# On affected nodes
rm /root/.ssh/known_hosts
rm /etc/ssh/ssh_known_hosts
pvecm updatecerts
```


## Wrong Timezone
Containers assume UTC. Explicitly set timezone.

``` bash
timedatectl
timedatectl list-timezones
timedatectl set-timezone America/Los_Angeles
```


## [Corrupted Terminal Characters or No UTF-8 Support][b]
Containers do not have locals set by default. Specify default locales for the
container to use.

!!! abstract "/etc/default/locale"
    0644 root:root

    ``` bash
    LANG="en_US.UTF-8"
    LANGUAGE="en_US:en"
    LC_CTYPE="en_US.UTF-8"
    LC_NUMERIC="en_US.UTF-8"
    LC_TIME="en_US.UTF-8"
    LC_COLLATE="en_US.UTF-8"
    LC_MONETARY="en_US.UTF-8"
    LC_MESSAGES="en_US.UTF-8"
    LC_PAPER="en_US.UTF-8"
    LC_NAME="en_US.UTF-8"
    LC_ADDRESS="en_US.UTF-8"
    LC_TELEPHONE="en_US.UTF-8"
    LC_MEASUREMENT="en_US.UTF-8"
    LC_IDENTIFICATION="en_US.UTF-8"
    ```

``` bash
# Update locales and save.
locale-gen en_US.UTF-8
dpkg-reconfigure --frontend=noninteractive locales
update-locale LAN=en_US.UTF-8
```

Reference:

* https://old.reddit.com/r/Proxmox/comments/dhgez0/console_utf8


## [LXC Long Boot Times or No Console][c]
Debian based systems will pause for up to **5** minutes on boot waiting for
**SLAAC** IPv6 configuration information; appearing to have no console. Disable
IPv6 if not actively used.

[a]: https://forum.proxmox.com/threads/task-error-failed-to-run-vncproxy.49954
[b]: https://old.reddit.com/r/Proxmox/comments/dhgez0/console_utf8
[c]: https://forum.proxmox.com/threads/no-console-with-proxmox-5-0-beta-2-and-debian-9-containers.35313
